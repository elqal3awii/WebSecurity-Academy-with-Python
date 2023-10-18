# Hack Steps

1. Inject payload into 'stockApi' parameter to delete carlos using SSRF against the local server
2. Check that carlos doesn't exist anymore in the admin panel

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python basic_ssrf_against_the_local_server.py
```

# Expected Output

```
⟪#⟫ Injection point: stockApi
❯ Injecting payload to delete carlos using SSRF against the local server.. OK
🗹 Check your browser, it should be marked now as solved
```
