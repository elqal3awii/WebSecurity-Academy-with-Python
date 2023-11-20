# Hack Steps

1. Make the request to change the email using the GET method and include an additional URL parameter to override the method
2. Deliver the exploit to the victim
3. The victim's email will be changed after they trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python samesite_lax_bypass_via_method_override.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
