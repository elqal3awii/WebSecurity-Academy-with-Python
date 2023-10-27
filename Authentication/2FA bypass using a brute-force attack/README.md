# Hack Steps

1. GET /login page and extract the session from cookie header and csrf token from the body
2. POST /login with valid credentials, extracted session and the csrf token
3. Obtain the new session
4. GET /login2 with the new session
5. Extract the csrf token from the body of /login2
6. POST the mfa-code with the new session and the new extracted csrf token
7. Repeat the process with all possbile numbers 

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python 2fa_bypass_using_a_brute_force_attack.py
```

# Expected Output

```
[#] Brute forcing the mfa-code of carlos..
[*] Elapsed: 19 minutes || Failed: 1 || (587/10000) 0588 => Incorrect
✅ Correct code: 0589
✅ New session: 2xAatFfbH1ezWx6fvMtM9R0zE62I7MnP
Use this session in your browser to login as carlos

✅ Finished in: 19 minutes

[!] Failed codes count: 1 
[!] Failed codes: ["0316"]
```
