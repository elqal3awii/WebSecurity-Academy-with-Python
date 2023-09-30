# Hack Steps
1. Get a valid session using valid creds
2. GET /login2 page
3. Brute force the mfa-codes

# Run Script
1. Change the URL of the lab
2. Start script
```
~$ python 2fa_broken_logic.py
```

# Expected Output
```
1. Obtaining a valid session.. OK
2. GET /login2 page.. OK
3. Start brute forcing mfa-code ..
[*] 1467 => Incorrect
[*] 1468 => Correct
✅ Finished in: 4 minutes
```

