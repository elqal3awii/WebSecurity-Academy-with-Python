## Hack Steps

1. Inject payload into the unkeyed `fehost` cookie
2. Send multiple request to the main page to cache it with the injected payload

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Poisoning the main page with an unkeyed cookie (3/30)..
❯❯ Poisoning the main page with an unkeyed cookie (17/30).. OK
🗹 The main page is poisoned successfully
🗹 The lab should be marked now as solved
```
