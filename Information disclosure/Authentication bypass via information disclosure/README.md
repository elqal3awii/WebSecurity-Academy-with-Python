## Hack Steps

1. Fetch the login page
2. Extract the session and the csrf token
3. Login as wiener
4. Extract the new session
5. Delete carlos from the admin panel bypassing access using a custom header

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Getting session and csrf token.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Getting a new session as wiener.. OK
⦗5⦘ Deleting carlos from the admin panel bypassing access using a custom header.. OK
🗹 The lab should be marked now as solved
```
