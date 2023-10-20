# Hack Steps

1. Craft an HTML form for changing the email address that includes an auto-submit script and doesn't contain the csrf token
2. Deliver the exploit to the victim
3. The victim's email will be changed after he trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python csrf_where_token_validation_depends_on_token_being_present.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after he trigger the exploit
🗹 Check your browser, it should be marked now as solved
```
