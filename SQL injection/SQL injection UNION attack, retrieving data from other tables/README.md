## Hack Steps

1. Inject payload into 'category' query parameter to retrieve administrator password from users table
2. Fetch the login page
3. Extract the csrf token and session cookie
4. Login as the administrator
5. Fetch the administrator profile

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection parameter: category
⦗1⦘ Retrieving administrator password from users table.. OK => ea8i69juc9uio1fgpabz
⦗2⦘ Fetching the login page.. OK
⦗3⦘ Extracting the csrf token and session cookie.. OK
⦗4⦘ Logging in as the administrator.. OK
⦗5⦘ Fetching the administrator profile.. OK
🗹 The lab should be marked now as solved
```
