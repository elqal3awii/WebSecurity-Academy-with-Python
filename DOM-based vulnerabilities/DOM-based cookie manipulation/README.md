## Hack Steps

1. Craft an iframe with the XSS payload in its src attribute and make its onload handler redirect the victim to the main page, triggering the XSS payload.
2. Deliver the exploit to the victim

## Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The lab should be marked now as solved
```
