## Hack Steps

1. Inject payload into the body of the request
2. Send multiple request to the main page to cache it with the injected payload

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Poisoning the geolocate.js file via a fat GET request (3/35)..
❯❯ Poisoning the geolocate.js file via a fat GET request (15/35).. OK
🗹 The main page is poisoned successfully as it request the poisoned geolocate.js file
🗹 The lab should be marked now as solved
```
