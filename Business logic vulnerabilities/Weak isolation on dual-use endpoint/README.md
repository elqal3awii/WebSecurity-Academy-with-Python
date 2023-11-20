# Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as wiener
4. Fetch wiener's profle
5. Extract the csrf token needed for changing password
6. Change the administrato's password by removing the current-password parameter from the request to skip the validation
7. Fetch the login page
8. Extract the csrf token and session cookie to login
9. Login as administrator
10. Delete carlos from the admin panel

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python weak_isolation_on_dual_use_endpoint.py
```

# Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie to login.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener's profle.. OK
⦗5⦘ Extracting the csrf token needed for changing password.. OK
⦗6⦘ Changing the administrator's password to hacked.. OK
⦗7⦘ Fetching the login page.. OK
⦗8⦘ Extracting the csrf token and session cookie to login.. OK
⦗9⦘ Logging in as administrator.. OK
⦗10⦘ Deleting carlos from the admin panel.. OK
🗹 The lab should be marked now as solved
```
