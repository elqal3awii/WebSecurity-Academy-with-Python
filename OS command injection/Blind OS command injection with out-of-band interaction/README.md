# Hack Steps

1. Fetch the feedback page
2. Extract the csrf token and session cookie
3. Inject payload into the name field when submitting a feedback to issue a DNS lookup to burp collaborator.
4. Check your burp collaborator for the DNS lookup


# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_os_command_injection_with_out_of_band_interaction.py
```

# Expected Output

```
⟪#⟫ Injection parameter: name
⦗1⦘ Fetching the feedback page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Injecting payload to issue a DNS lookup to burp collaborator.. OK
🗹 Check your burp collaborator for the DNS lookup
🗹 Check your browser, it should be marked now as solved
```
