## Hack Steps

1. Use a parameter entity to issue a DNS lookup to burp collaborator
2. Check your burp collaborator for the DNS lookup

## Run Script

1. Change the URL of the lab
2. Change the domain of the burp collaborator
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection point: Check stock request
❯❯ Using a parameter entity to issue a DNS lookup to burp collaborator.. OK
🗹 Check your burp collaborator for the DNS lookup
🗹 The lab should be marked now as solved
```
