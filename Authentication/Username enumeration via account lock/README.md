# Hack Steps
1. Try all users multiple times until on account is locked
2. Brute force password of that valid username
3. Wait 1 minute every 3 password tries to bypass blocking

# Run Script
1. Change the URL of the lab
2. Change the PATH for your usernames list
3. Change the PATH for you passwords list
4. Start script
```
~$ python username_enumeration_via_account_lock.py
```

# Expected Output
```
[#] Enumerate usernames..
[*] Try number 1 of all users..
Elapsed: 3 minutes || Failed: 0 || Trying (6/101): adam                                              
[#] Brute forcing password..
✅ Valid user: adam
Elapsed: 26 minutes || Failed: 0 || Trying (74/102): joshua                                            
✅ Login successfully:  username: adam, password: joshua
✅ Finished in: 0 minutes
Results was saved to: results
Failed users count: 0
Failed users: [  ]
Failed passwords count: 0
Failed passwords: [  ]
```

# Want to go faster?
Check the [Rust script](https://github.com/elqalawii/portswigger_labs_with_rust/tree/main/Authentication/username_enumeration_via_account_lock) for this lab in both single-threaded and multi-threaded approaches.
