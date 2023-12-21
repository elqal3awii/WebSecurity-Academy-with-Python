## Hack Steps

1. Fetch a post page
2. Extract the session cookie and the csrf token to post a comment
3. Post a comment with a payload to get the User Agent of the victim
4. Wait until the victim view comments to extract their User-Agent from server logs
5. Store the malicious javascript file on your exploit server
6. Poison the main page for specific subset of users

## Run Script

1. Change the URL of the lab
2. Change the DOMAIN of the expoit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching a post page.. OK
⦗2⦘ Extracting the session cookie and the csrf token to post a comment.. OK
⦗3⦘ Posting a comment with a payload to get the User Agent of the victim.. OK
⦗4⦘ Waiting until the victim view comments to extract their User-Agent from server logs.. OK
⦗5⦘ Storing the malicious javascript file on your exploit server.. OK
❯❯ Victim's User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
⦗6⦘ Poisoning the main page for specific subset of users (3/10)..
⦗6⦘ Poisoning the main page for specific subset of users (10/10).. OK
🗹 The main page is poisoned successfully
🗹 The lab may not be marked as solved automatically for unknown reasons
🗹 Use the User-Agent string with burp if so
```
