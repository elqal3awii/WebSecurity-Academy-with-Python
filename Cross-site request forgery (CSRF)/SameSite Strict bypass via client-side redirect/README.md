# Hack Steps

1. Exploit the redirection functionality that occurs after a comment is submitted in order to redirect the victim to their profile and change their email using URL parameters
2. Deliver the exploit to the victim
3. The victim's email will be changed after he trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python samesite_strict_bypass_via_client_side_redirect.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after he trigger the exploit
🗹 Check your browser, it should be marked now as solved
```
