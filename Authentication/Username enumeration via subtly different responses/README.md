# Hack Steps
1. Obtain a valid username via subtly different error messages
2. Brute force password of that valid username

# Run Script
1. Change the URL of the lab
2. Change the PATH of your username list
3. Change the PATH of your password list
4. Start script
```
~$ python username_enumeration_via_different_resposnes.py
```
# Expected Output
```
[#] Enumerate usernames..
Elapsed: 0 minutes || Failed: 0 || Trying (6/101): adam                                              

✅ Valid user: adam
[#] Brute forcing password..
Elapsed: 0 minutes || Failed: 0 || Trying (74/102): joshua                                            

✅ Login successfully:  username: adam, password: joshua

Finished in: 0 minutes

Results was saved to: results

Failed users count: 0
Failed users: [  ]

Failed passwords count: 0
Failed passwords: [  ]
```

# Want to go faster?
Check the [Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20subtly%20different%20responses) for this lab in both single-threaded and multi-threaded approaches.
