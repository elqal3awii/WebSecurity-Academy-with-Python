## Hack Steps

1. fetch the login page
2. Extract the csrf token and session cookie
3. Login as wiener
4. Extract the new csrf token from wiener profile
5. Upload a .htaccess file containing a mapping rule to a custom extension
6. Upload the shell file with the custom extension
7. Fetch the uploaded shell file to read the secret
8. Submit the solution 


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
⦗4⦘ Extracting the new csrf token from wiener profile.. OK
⦗5⦘ Uploading a .htaccess file containing a mapping rule to a custom extension.. OK
⦗6⦘ Uploading the shell file with the custom extension.. OK
⦗7⦘ Fetching the uploaded shell file to read the secret.. OK
❯❯ Secret: k0tN0zmdzem3HZ0fBNv2JZGC5cz8EWq4
⦗8⦘ Submitting the solution.. OK
🗹 The lab should be marked now as solved
```
