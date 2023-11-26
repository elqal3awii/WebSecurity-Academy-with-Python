## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as wiener
4. Delete carlos from the admin panel directly without selecting a role

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Deleting carlos from the admin panel directly without selecting a role.. OK
🗹 The lab should be marked now as solved
```
