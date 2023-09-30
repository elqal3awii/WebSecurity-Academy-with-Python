# Hack Steps

1. Fetch administrator page via URL id parameter
2. Extract the password from source code
3. Login as administrator
4. Delete carlos

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python user_id_controlled_by_request_parameter_with_password_disclosure.py
```

# Expected Output

```
1. Fetching administrator profile page.. OK
2. Extracting password from source code.. OK => 3gaulaq4bt7xwrt1utec
3. Fetching login page to get valid session and csrf token.. OK
4. Logging in as administrator.. OK
5. Deleting carlos.. OK
🗹 Check your browser, it should be marked now as solved
```
