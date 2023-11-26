## Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie
3. Login as wiener
4. Add the leather jacket to the cart with a modified price
5. Fetch wiener's cart
6. Extract the csrf token needed for placing order
7. Place order
8. Confirm order

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Adding the leather jacket to the cart with a modified price.. OK
⦗5⦘ Fetching wiener's cart.. OK
⦗6⦘ Extracting the csrf token needed for placing order.. OK
⦗7⦘ Placing order.. OK
⦗8⦘ Confirming order.. OK
🗹 The lab should be marked now as solved
```
