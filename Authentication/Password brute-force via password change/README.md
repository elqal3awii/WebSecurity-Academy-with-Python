## Hack Steps

1. Read password list
2. Brute force carlos password via password change functionality and change his password (login as wiener before every try to bypass blocking)
3. Wait 1 minute to bypass blocking
4. Login as carlos with the new password

## Run Script

1. Change the URL of the lab
2. Make sure the passwords file exists in the root directory (Authentication directory) or change its path accordingly
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Reading password list.. OK
⦗2⦘ Brute forcing carlos password.. 
❯❯ Elapsed: 51 seconds || Trying (62/101): jessica                                           
🗹 Correct password: Hacked
🗹 Password was changed to: Hacked
⦗3⦘ Waiting 1 minute to bypass blocking.. OK
⦗4⦘ Logging in as carlos with the new password.. OK
🗹  Finished in: 113 seconds
🗹 The lab should be marked now as solved
```

# Test Samples

This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.
