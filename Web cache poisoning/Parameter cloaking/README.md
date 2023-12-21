## Hack Steps

1. Inject payload as a second query parameter
2. Send multiple request to the main page to cache it with the injected payload

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Poisoning the geolocate.js file using parameter cloaking (3/35)..
❯❯ Poisoning the geolocate.js file using parameter cloaking (15/35).. OK
🗹 The main page is poisoned successfully as it request the poisoned geolocate.js file
🗹 The lab should be marked now as solved
```
