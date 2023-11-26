## Hack Steps

1. Fetch the 1.txt log file
2. Extract carlos password from the log file
3. Fetch the login page to get valid session and csrf token
4. Login as carlos

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
1. Fetching the 1.txt log file.. OK
2. Extracting password from the log file.. OK => daxpy2ozi7znnixdcgkh
3. Fetching the login page to get valid session and csrf token.. OK
4. Logging in as carlos.. OK
5. Fetching carlos profile.. OK
🗹 The lab should be marked now as solved
```
