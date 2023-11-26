## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie
3. Login as wiener
4. Fetch wiener profile
5. Extract the csrf token that is needed for email update
6. Craft an HTML form for changing the email address that includes the extracted csrf token and an img tag which is used to set the csrf cookie via its src and submit the form via its error handler
7. Deliver the exploit to the victim
8. The victim's email will be changed after they trigger the exploit

## Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener profile.. OK
⦗5⦘ Extracting the csrf token that is needed for email update.. OK
⦗6⦘ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
