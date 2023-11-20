# Hack Steps

1. Inject payload into 'TrackingId' cookie to make the database return an error containing the administrator password
2. Extract the administrator password
3. Fetch the login page
4. Extract the csrf token and session cookie
5. Login as the administrator
6. Fetch the administrator profile

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python visible_error_based_sql_injection.py
```

# Expected Output

```
[#] Injection point: TrackingId
1. Injecting payload to retrieve the administrator password.. OK
2. Extracting administrator password.. OK => 8j94jjw4yfqsy0uv43pf
3. Fetching login page.. OK
4. Extracting the csrf token and session cookie.. OK
5. Logging in as the administrator.. OK
6. Fetching the administrator profile.. OK
🗹 The lab should be marked now as solved
```
