# Hack Steps
1. Login as carlos
2. Extract the session from the Set-Cookie header
3. Request /login2 using the extracted session
4. Request /my-account directly bypassing 2FA

# Run Script
1. change the URL of the lab
2. Start script
```
~$ cargo run
```
# Expected output
```
1. Logged in as carlos.. ☑️
2. GET /login2 using extracted session.. ☑️
3. GET /my-account directly bypassing 2FA.. ☑️
✅ Logged in successfully as Carlos
```

### Happy Hacking 👾