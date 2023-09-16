# Hack Steps

1. Inject payload in 'category' query parameter to retrieve the name of users table
2. Adjust the payload to retrieve the names of username and password columns
3. Adjust the payload to retrieve the administrator password
4. Fetch the login page
5. Extract csrf token and session cookie
6. Login as the administrator
7. Fetch the administrator profile

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python sql_injection_attack_listing_the_database_contents_on_non_oracle_databases.py
```

# Expected Output

```
[#] Injection parameter: category
1. Injecting a payload to retrieve the name of users table.. OK => users_cjmchk
2. Adjusting the payload to retrieve the names of username and password columns.. OK => username_bhfqop | password_qjovik
3. Adjusting the payload to retrieve the administrator password.. OK => xoo4ze81np9mbil2428k
4. Fetching login page.. OK
5. Extracting csrf token and session cookie.. OK
6. Logging in as the administrator.. OK
7. Fetching the administrator profile.. OK
[#] Check your browser, it should be marked now as solved
```
