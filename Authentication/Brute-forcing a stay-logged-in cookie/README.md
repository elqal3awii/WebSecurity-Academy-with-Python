## Hack Steps

1. Read password list
2. Hash every the password
3. Encrypt every tha hash with the username in the cookie
4. Fetch carlos profile with every encrypted cookie

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
❯❯ Elapsed: 34 seconds || Trying (77/101): qazwsx
🗹 Correct password: 123qwe
🗹 Finished in: 34 seconds
🗹 The lab should be marked now as solved
```

# Test Samples

This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.
