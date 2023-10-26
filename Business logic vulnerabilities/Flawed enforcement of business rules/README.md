# Hack Steps

1. Fetch the login page
2. Extract csrf token and session cookie
3. Login as wiener
4. Add the leather jacket to the cart
5. Fetch wiener's cart
6. Extract csrf token needed for applying coupons and placing order
7. Apply the coupons one after another repeatedly for a few times
8. Place order
9. Confirm order

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python flawed_enforcement_of_business_rules.py
```

# Expected Output

```
⦗1⦘ Fetching the login page.. OK
⦗2⦘ Extracting csrf token and session cookie.. OK
⦗3⦘ Logging in as wiener.. OK
⦗4⦘ Adding the leather jacket to the cart.. OK
⦗5⦘ Fetching wiener's cart.. OK
⦗6⦘ Extracting csrf token needed for applying coupons and placing order.. OK
⦗7⦘ Applying the coupon NEWCUST5 (1/8)..
⦗7⦘ Applying the coupon SIGNUP30 (2/8)..
⦗7⦘ Applying the coupon NEWCUST5 (3/8)..
            ..............
⦗7⦘ Applying the coupon SIGNUP30 (8/8).. OK
⦗8⦘ Placing order.. OK
⦗9⦘ Confirming order.. OK
🗹 Check your browser, it should be marked now as solved
```