## Hack Steps

1. Change the dynamically-generating link of password change functionality via X-Forwarded-Host header to point to your exploit server
2. Extract the temporary token from you server logs
3. Use the token to change carlos password

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit servers
3. Start script

```
~$ cargo run
```

# Expected Output

```
1. Change the dynamically generated link via X-Forwarded-Host header.. ☑️
2. Get temp-forgot-password-token of the carlos from exploit sever logs.. ☑️
3. Changing the password of the carlos.. ☑️
✅ Password changed to: Hacked
```
