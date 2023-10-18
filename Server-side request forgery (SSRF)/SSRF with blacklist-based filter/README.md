# Hack Steps

1. Inject payload into 'stockApi' parameter to delete carlos using SSRF with input filter bypass
2. Check that carlos doesn't exist anymore in the admin panel

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python ssrf_with_blacklist_based_filter.py
```

# Expected Output

```
⟪#⟫ Injection point: stockApi
❯ Injecting payload to delete carlos using SSRF with input filter bypass.. OK
🗹 Check your browser, it should be marked now as solved
```
