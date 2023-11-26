## Hack Steps

1. Read password list
2. Brute force carlos password (login with as wiener before each try to bypass blocking)
3. Fetch carlos profile

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
❯❯ Elapsed: 51 seconds || Trying (73/100): ginger
⦗#⦘ Making a successful login.. OK
❯❯ Elapsed: 53 seconds || Trying (75/100): joshua
🗹 Correct password: joshua
⦗3⦘ Fetching carlos profile.. OK
🗹 Finished in: 53 seconds
🗹 The lab should be marked now as solved
```

## Test Samples

This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.
