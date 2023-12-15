## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as wiener
4. Fetch wiener's profile
5. Set the preferred name with the malicious payload
6. Post a comment as wiener
7. Fetch the post page to execute the payload

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie to login.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener's profile.. OK
⦗5⦘ Setting the preferred name with the malicious payload.. OK
⦗6⦘ Posting a comment as wiener.. OK
⦗7⦘ Fetching the post page to execute the payload.. OK
🗹 The morale.txt file is successfully deleted
🗹 The lab should be marked now as solved
```
