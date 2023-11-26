## Hack Steps

1. Make forgot-password request as carlos with the X-Forwarded-Host changed
2. Extract the token from the server logs
3. Change carlos password with the obtained token
4. Login as carlos with the new password
5. Fetch carlos profile

## Run Script

1. Change the URL of the lab
2. Change the DOMAIN of the exploit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Making forgot-password request as carlos with the X-Forwarded-Host changed.. OK
⦗2⦘ Extracting the token from the server logs.. OK
⦗3⦘ Changing carlos password with the obtained token.. OK
🗹 Password was changed to: Hacked
⦗4⦘ Logging in as carlos with the new password.. OK
⦗5⦘ Fetching carlos profile.. OK
🗹 The lab should be marked now as solved
```
