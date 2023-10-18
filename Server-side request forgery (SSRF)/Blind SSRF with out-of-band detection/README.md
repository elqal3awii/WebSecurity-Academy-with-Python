# Hack Steps

1. Inject payload into the Referer header to cause an HTTP request to the burp collaborator
2. Check your burp collaborator for the HTTP request

# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_ssrf_with_out_of_band_detection.py
```

# Expected Output

```
⟪#⟫ Injection point: Referer header
❯ Injecting payload to cause an HTTP request to the burp collaborator.. OK
🗹 Check your burp collaborator for the HTTP request
🗹 Check your browser, it should be marked now as solved
```
