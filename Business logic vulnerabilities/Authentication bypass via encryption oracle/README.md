## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie to login
3. Login as wiener
4. Extract the stay-logged-in cookie
5. Fetch a post page with the stay-logged in cookie value in the notification cookie to decrypt it
6. Extract the decrypted value
7. Extract the csrf token to post a comment
8. Post a comment with PADDINGadministrator:NUMBERS in the email field ( where PADDING is 9 bytes and NUMBERS is extracted from the decrypted value in the previous step )
9. Extract the notification cookie
10. Decode the notification cookie with base64
11. Remove the first two blocks and encode the remaining blocks
12. Place the last encoded value in the stay-logged-in cookie and delete carlos

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie to login.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Extracting the stay-logged-in cookie.. OK
⦗5⦘ Fetching a post page with the stay-logged in cookie value in the notification cookie to decrypt it.. OK
⦗6⦘ Extracting the decrypted value.. OK => wiener:1698616140241
⦗7⦘ Extracting the csrf token to post a comment.. OK
⦗8⦘ Posting a comment with 123456789administrator:1698616140241 in the email field.. OK
⦗9⦘ Extracting the notification cookie.. OK
⦗10⦘ Decoding the notification cookie with base64.. OK
⦗11⦘ Removing the first two blocks and encode the remaining blocks.. OK => wpM5mrYZ8yTjJag3UH01LKks2N8HfkKlEmxlakgwXsc=
⦗12⦘ Placing the last encoded value in the stay-logged-in cookie and delete carlos.. OK
🗹 The lab should be marked now as solved
```
