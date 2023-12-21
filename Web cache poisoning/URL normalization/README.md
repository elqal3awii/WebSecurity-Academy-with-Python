## Hack Steps

1. Send multiple request to a non-exist path to cache it with the injected payload
2. Deliver the link to the victim

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Poisoning a non-existent path with the injected payload (4/20)..
⦗1⦘ Poisoning a non-existent path with the injected payload (20/20).. OK
🗹 The path is poisoned successfully
⦗2⦘ Delivering the link to the victim.. OK
🗹 The lab should be marked now as solved
```
