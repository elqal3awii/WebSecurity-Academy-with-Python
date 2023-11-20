# Hack Steps

1. Craft an HTML form for changing the email address with a script that opens a new tab to force the victim to refresh their cookie and submit the form after a few seconds to make sure that the redirection occurred
2. Deliver the exploit to the victim
3. The victim's email will be changed after they trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python samesite_lax_bypass_via_cookie_refresh.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
