## Hack Steps

1. Read usernames and passwords lists
2. Try to find a valid username via different error messages
3. Brute force the password of that valid username
4. Login with the valid credentials

## Run Script

1. Change the URL of the lab
2. Make sure the passwords and usernames files exist in the root directory (Authentication directory) or change its path accordingly
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Reading usernames list.. OK
⦗2⦘ Reading password list.. OK
⦗3⦘ Trying to find a valid username..
❯❯ Elapsed: 24  seconds || Trying (58/101): am
🗹 Valid username: am
⦗4⦘ Brute forcing password..
❯❯ Elapsed: 43  seconds || Trying (42/101): soccer
🗹 Valid username: am
🗹 Valid password: soccer
⦗5⦘ Logging in.. OK
🗹 Finished in: 44 seconds
🗹 The lab should be marked now as solved
```

## Test Samples

This test is done using only 100 users & 100 passwods. What about 10K users & 10K passwords?
Or what about 100K users & 100K passwords?

You can see the comparison I made with these numbers when solving [this lab with Rust](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust
