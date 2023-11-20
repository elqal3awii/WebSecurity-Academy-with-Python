# Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as wiener
4. Add the leather jacket to the cart
5. Confirm order directly without checking out

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python insufficient_workflow_validation.py
```

# Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie to login.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Adding the leather jacket to the cart.. OK
⦗5⦘ Confirming order directly without checking out.. OK
🗹 The lab should be marked now as solved
```
