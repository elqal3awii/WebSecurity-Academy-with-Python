# Hack Steps

1. Craft an HTML form for changing the email address with an auto-submit script and use the GET method rather than POST as the form method
2. Deliver the exploit to the victim
3. The victim's email will be changed after they trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python csrf_where_token_validation_depends_on_request_method.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
