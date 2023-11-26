## Hack Steps

1. Read usernames and passwords lists
2. Try to find a valid username via subtly different error messages
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
❯❯ Elapsed: 36 seconds || Trying (83/101): argentina                                         
🗹 Valid username: argentina
⦗4⦘ Brute forcing password.. 
❯❯ Elapsed: 59 seconds || Trying (52/101): thomas                                            
🗹 Valid username: argentina
🗹 Valid password: thomas
⦗5⦘ Logging in.. OK
🗹 Finished in: 60 seconds
🗹 The lab should be marked now as solved
```

## Want to go faster?
Check the [Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20subtly%20different%20responses) for this lab in both single-threaded and multi-threaded approaches.
