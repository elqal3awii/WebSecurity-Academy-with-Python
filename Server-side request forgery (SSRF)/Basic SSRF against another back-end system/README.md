## Hack Steps

1. Inject payload into 'stockApi' parameter to scan the internal network
2. Delete carlos from the admin interface

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection point: stockApi
⦗1⦘ Injecting payload to scan the internal netwrok (192.168.0.15:8080/admin)..
⦗1⦘ Injecting payload to scan the internal netwrok (192.168.0.120:8080/admin)..
                            ....................
⦗1⦘ Injecting payload to scan the internal netwrok (192.168.0.218:8080/admin).. OK
⦗2⦘ Deleting carlos from the admin interface.. OK
🗹 The lab should be marked now as solved
```
