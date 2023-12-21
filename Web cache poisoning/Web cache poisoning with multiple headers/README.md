## Hack Steps

1. Store the malicious javascript file on your expoit server
2. Send multiple request to the tracking.js file with multiple headers, one causes a redirect and the other makes the redirect point to your exploit server
3. The main page will be poisoned as it request the tracking.js file

## Run Script

1. Change the URL of the lab
2. Change the DOMAIN of the expoit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Storing the malicious javascript file on your exploit server.. OK
⦗2⦘ Poisoning the tracking.js file with multiple headers (3/30)..
⦗2⦘ Poisoning the tracking.js file with multiple headers (17/30).. OK
🗹 The main page is poisoned successfully as it request the tracking.js file
🗹 The lab should be marked now as solved
```
