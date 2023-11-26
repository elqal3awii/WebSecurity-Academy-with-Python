## Hack Steps

1. Fetch the login page
2. Extract the csrf to login
3. Login as wiener
4. Fetch wiener profile
5. Extract the csrf token that is needed for email update
6. Craft an HTML form for changing the email address with an auto-submit script and include the extracted csrf token in the form
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
⦗2⦘ Extracting the csrf token to login.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener profile.. OK
⦗5⦘ Extracting the csrf token that is needed for email update.. OK
⦗6⦘ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
