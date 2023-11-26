## Hack Steps

1. Read usernames and passwords lists
2. Try all users multiple times until on account is locked
3. Brute force password of that valid username (wait 1 minute every 3 password tries to bypass blocking)
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
⦗#⦘ Try number: 0 of all users..
❯❯ Elapsed: 0  minutes || Trying (101/101): autodiscover
⦗#⦘ Try number: 1 of all users..
❯❯ Elapsed: 1  minutes || Trying (101/101): autodiscover
⦗#⦘ Try number: 2 of all users..
❯❯ Elapsed: 2  minutes || Trying (101/101): autodiscover
⦗#⦘ Try number: 3 of all users..
❯❯ Elapsed: 2  minutes || Trying (40/101): affiliate
🗹 Valid username: affiliate
⦗4⦘ Brute forcing password..
⦗*⦘ Waiting 1 minute to bypass blocking..
❯❯ Elapsed: 3  minutes || Trying (3/101): 12345678
⦗*⦘ Waiting 1 minute to bypass blocking..
            ..............
🗹 Valid username: affiliate
🗹 Valid password: 123321
⦗5⦘ Logging in.. OK
🗹 Finished in: 10 minutes
🗹 The lab should be marked now as solved
```

## Test Samples

This test is done using only 100 users & 100 passwods. What about 10K users & 10K passwords?
Or what about 100K users & 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.
