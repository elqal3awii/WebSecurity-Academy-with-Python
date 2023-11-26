## Hack Steps

1. Read usernames and passwords lists
2. Change X-Forwarded-For header to a random IP in every request to bypass blocking
3. Try to find a valid username via response timing
4. Brute force the password of that valid username
5. Login with the valid credentials

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
❯❯ Elapsed: 35 seconds || Trying (77/101): apps
🗹 Valid username: apps
⦗4⦘ Brute forcing password..
❯❯ Elapsed: 52 seconds || Trying (17/101): letmein
🗹 Valid username: apps
🗹 Valid password: letmein
⦗5⦘ Logging in.. OK
🗹 Finished in: 53 seconds
🗹 The lab should be marked now as solved
```

## Want to go faster?

Check the [Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20response%20timing) for this lab in both single-threaded and multi-threaded approaches.
