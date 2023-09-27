# Hack Steps

1. Inject payload into 'TrackingId' cookie to extract administrator password via DNS lookup
2. Get the administrator password from your burp collaborator
3. Login as administrator

# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_sql_injection_with_out_of_band_data_exfiltration.py
```

# Expected Output

```
[#] Injection point: TrackingId
[*] Injecting payload to extract administrator password via DNS lookup.. OK
[#] Check your burp collaborator for the administrator password then login
```
