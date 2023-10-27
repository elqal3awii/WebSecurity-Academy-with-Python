# Hack Steps

1. Fetch the register page
2. Extract the csrf token and session cookie to register a new account
3. Register a new account with a suitable offset and dontwannacry.com before the real domain
4. Fetch the email client
5. Extract the link of account registration
6. Complete the account registration by following the link
7. Fetch the login page
8. Extract the csrf token and session cookie to login
9. Login to the new account
10. Delete carlos from the admin panel

# Run Script

1. Change the URL of the lab
2. Change the domain of the exploit server
3. Start script

```
~$ python inconsistent_handling_of_exceptional_input.py
```

# Expected Output

```
⦗1⦘ Fetching the register page.. OK
⦗2⦘ Extracting the csrf token and session cookie to register a new account.. OK
⦗3⦘ Registering a new account with a suitable offset and dontwannacry.com before the real domain.. OK
⦗4⦘ Fetching the email client.. OK
⦗5⦘ Extracting the link of account registration.. OK
⦗6⦘ Completing the account registration by following the link.. OK
⦗7⦘ Fetching the login page.. OK
⦗8⦘ Extracting the csrf token and session cookie to login.. OK
⦗9⦘ Logging in to the new account.. OK
⦗10⦘ Deleting carlos from the admin panel.. OK
🗹 Check your browser, it should be marked now as solved
```
