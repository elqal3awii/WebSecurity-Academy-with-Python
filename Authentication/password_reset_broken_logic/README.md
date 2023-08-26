# Hack Steps
1. Send forgot-password request as wiener
2. Extract the token from the email client
3. Send change-password request as carlos

# Run Script
1. Change the URL of the lab
2. Set the new password to what you want
3. Start script
```
~$ python password_reset_broken_logic.py
```

# Expected Output
```
1. Send forgot-password request as wiener.. ☑️
2. Extract the token from the email client.. ☑️
3. Send change-password request as carlos.. ☑️
Carlos password changed succussfully to: Hola!
```