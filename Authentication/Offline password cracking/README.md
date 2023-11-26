## Hack Steps

1. Post a comment with a malicious XSS payload
2. Fetch the exploit sever logs
3. Extract the encoded cookie from logs
4. Decode the encoded cookie
5. Crack this hash using any online hash cracker

## Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Posting a comment with a malicious XSS payload.. OK
⦗2⦘ Fetching the exploit sever logs.. OK
⦗3⦘ Extracting the encoded cookie from logs.. OK
⦗4⦘ Decoding the encoded cookie.. OK
🗹 Password hash: 26323c16d5f4dabff3bb136f2460a943
⦗#⦘ Crack this hash using any online hash cracker
```
s