## Hack Steps

1. Inject payload into 'stockApi' parameter to delete carlos using SSRF against the local server
2. Check that carlos doesn't exist anymore in the admin panel

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection point: stockApi
❯❯ Injecting payload to delete carlos using SSRF against the local server.. OK
🗹 The lab should be marked now as solved
```
