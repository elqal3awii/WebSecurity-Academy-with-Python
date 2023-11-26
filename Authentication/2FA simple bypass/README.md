## Hack Steps

1. Login as carlos
2. Get the session cookie
3. Fetch the profile page directly bypassing 2FA
4. Extract the name 'carlos' to make sure you logged in as him

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected output

```
⦗1⦘ Logging in as carlos.. OK
⦗2⦘ Fetching the profile page directly bypassing 2FA.. OK
⦗3⦘ Extracting the name 'carlos' to make sure you logged in as him.. OK
🗹 Logged in successfully as carlos
🗹 The lab should be marked now as solved
```
