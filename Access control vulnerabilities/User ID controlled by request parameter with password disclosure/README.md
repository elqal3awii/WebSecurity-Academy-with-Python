## Hack Steps

1. Fetch administrator page via URL id parameter
2. Extract the password from source code
3. Fetch the login page to get a valid session and the csrf token
4. Login as administrator
5. Delete carlos

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python mian.py
```

## Expected Output

```
⦗1⦘ Fetching administrator profile page.. OK
⦗2⦘ Extracting password from source code.. OK => nmdgmr7vfboi7zme7z42
⦗3⦘ Fetching the login page to get a valid session and the csrf token.. OK
⦗4⦘ Logging in as administrator.. OK
⦗5⦘ Deleting carlos.. OK
🗹 The lab should be marked now as solved
```
