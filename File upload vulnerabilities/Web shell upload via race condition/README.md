# Hack Steps

1. fetch the login page
2. Extract the csrf token and session cookie
3. Login as wiener
4. Fetch wiener profile
5. Upload the the shell file via race condition
6. Try to fetch the shell file concurrently from a different thread
7. Submit the solution

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python web_shell_upload_via_race_condition.py
```

# Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener profile.. OK
⦗6⦘ Trying to fetch the shell file (1/10).. OK
⦗5⦘ Uploading the shell file via race condition (2/10).. OK
⦗6⦘ Trying to fetch the shell file (2/10).. OK
⦗6⦘ Trying to fetch the shell file (3/10).. OK
❯ Secret: 2ds7AZuX7upUjFQrnHD9GwcgidVwtMtu
⦗5⦘ Uploading the shell file via race condition (3/10).. OK
⦗7⦘ Submitting the solution.. OK
🗹 The lab should be marked now as solved
```
