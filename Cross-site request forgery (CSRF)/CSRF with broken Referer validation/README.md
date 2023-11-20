# Hack Steps

1. Add the `Referrer-Policy` header to your exploit server response headers
2. Craft an HTML form for changing the email address with an auto-submit script that changes the Referer header value using the `history.pushState()` method
3. Deliver the exploit to the victim
4. The victim's email will be changed after they trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python csrf_with_broken_referer_validation.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The victim's email will be changed after they trigger the exploit
🗹 The lab should be marked now as solved
```
