# Hack Steps

1. Inject payload into storeId XML element to retrieve administrator password using UNION-based attack
2. Extract administrator password from the response body
3. Fetch the login page
4. Extract csrf token and session cookie
5. Login as the administrator
6. Fetch the administrator profile

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python sql_injection_with_filter_bypass_via_xml_encoding.py
```

# Expected Output

```
[#] Injection point: storeId
1. Injecting payload to retrieve administrator password using UNION-based attack.. OK
2. Extracting administrator password from the response.. OK
3. Fetching login page.. OK
4. Extracting csrf token and session cookie.. OK
5. Logging in as the administrator.. OK
6. Fetching the administrator profile.. OK
[#] Check your browser, it should be marked now as solved
```

# Note

- You may need to adjust the pattern when extracting the administrator password (see the comment I left in the script)
