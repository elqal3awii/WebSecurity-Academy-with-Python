# Hack Steps

1. Inject payload into 'productId' XML element to issue a DNS lookup to burp collaborator using a parameter entity
2. Check your burp collaborator for the DNS lookup

# Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python blind_xxe_with_out_of_band_interaction_via_xml_parameter_entities.py
```

# Expected Output

```
⟪#⟫ Injection point: productId
❯ Injecting payload to issue a DNS lookup to burp collaborator using a parameter entity.. OK
🗹 Check your burp collaborator for the DNS lookup
🗹 Check your browser, it should be marked now as solved
```
