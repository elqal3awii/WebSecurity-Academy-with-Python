# Hack Steps

1. Fetch the login page
2. Extract the csrf token and session cookie
3. Login as wiener
4. Fetch wiener's profile
5. Extract the csrf token needed for subsequent requests
6. Add 10 gift cards to the cart
7. Apply the coupon SIGNUP30
8. Place order
9. Fetch the email client
10. Collect the received gift card codes
11. Redeem the codes one by one
12. Repeat the stpes from 6 to 11 multiple times (42 is enough to get the price of the leather jacket)
13. Add the leather jacket the cart
14. Plac order
15. Confirm order

# Run Script

1. Change the URL of the lab
2. Change the domain of the exploit server
3. Start script

```
~$ python infinite_money_logic_flaw.py
```

# Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Fetching wiener's profile.. OK
⦗5⦘ Extracting the csrf token needed for subsequent requests.. OK
⦗6⦘ Adding 10 gift cards to the cart (1/43).. OK
⦗7⦘ Applying the coupon SIGNUP30.. OK
⦗8⦘ Placing order.. OK
⦗9⦘ Fetching the email client.. OK
⦗10⦘ Collecting the received gift card codes.. OK
⦗11⦘ Redeeming the code w36tUymh1O (1/10)..
⦗11⦘ Redeeming the code UuQuZJtK0u (2/10)..
                    ..................
⦗11⦘ Redeeming the code yUP4oPJA3Y (10/10).. OK
⦗6⦘ Adding 10 gift cards to the cart (2/43).. OK
⦗7⦘ Applying the coupon SIGNUP30.. OK
⦗8⦘ Placing order.. OK
⦗9⦘ Fetching the email client.. OK
⦗10⦘ Collecting the received gift card codes.. OK
⦗11⦘ Redeeming the code xR8H0Ar22K (1/10)..
⦗11⦘ Redeeming the code 0xwyMFQltS (2/10)..
                    ..................
⦗11⦘ Redeeming the code 6RW6dh2YJf (10/10).. OK
                    ..................
                    ..................
⦗6⦘ Adding 10 gift cards to the cart (43/43).. OK
⦗7⦘ Applying the coupon SIGNUP30.. OK
⦗8⦘ Placing order.. OK
⦗9⦘ Fetching the email client.. OK
⦗10⦘ Collecting the received gift card codes.. OK
⦗11⦘ Redeeming the code xgep1WhmcW (1/10)..
⦗11⦘ Redeeming the code KanEic27xZ (2/10)..
                    ..................
⦗11⦘ Redeeming the code xRrcFI0r3f (10/10).. OK
⦗12⦘ Adding the leather jacket the cart.. OK
⦗13⦘ Placing order.. OK
⦗14⦘ Confirming order.. OK
🗹 The lab should be marked now as solved
```
