# Hack Steps

1. Inject payload into 'category' query parameter to retrieve administrator password from users table using concatenation method
2. Fetch the login page
3. Extract csrf token and session cookie
4. Login as the administrator
5. Fetch the administrator profile

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ cargo run
```

# Expected Output

```
[#] Injection parameter: category
1. Retrieving administrator password from users table.. OK => t3yxp9s4v7qgq4valov0
2. Fetching login page.. OK
3. Extracting csrf token and session cookie.. OK
4. Logging in as the administrator.. OK
5. Fetching the administrator profile.. OK
[#] Check your browser, it should be marked now as solved
```
