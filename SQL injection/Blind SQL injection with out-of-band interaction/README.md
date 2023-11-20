# Hack Steps

1. Inject payload into 'TrackingId' cookie to make a DNS lookup to your burp collaborator domain
2. Check your collaborator for incoming traffic

# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_sql_injection_with_out_of_band_interaction.py
```

# Expected Output

```
[#] Injection point: TrackingId
[*] Injecting payload to make a DNS lookup.. OK
[#] Check the DNS lookup in your burp collaborator
🗹 The lab should be marked now as solved
```
