# Hack Steps
1. Obtain a valid username via subtly different error messages
2. Brute force password of that valid username

# Run Script
1. change the URL of the lab
2. change the PATH for your usernames list
3. change the PATH for you passwords list
4. Start script
```
~$ python username_enumeration_via_different_resposnes.py
```
# Expected Output
```
[#] Enumerate usernames..
Elapsed: 0 minutes || Failed: 0 || Trying (6/101): user                                              
[#] Brute forcing password..
✅ Valid user: user
Elapsed: 0 minutes || Failed: 0 || Trying (74/102): joshua                                            
✅ Login successfully:  username=user,password=joshua
✅ Finished in: 0 minutes
Results was saved to: results
Failed users count: 0
Failed users: [  ]
Failed passwords count: 0
Failed passwords: [  ]
```

# Want to go faster?
Check the [Rust script](https://github.com/elqalawii/portswigger_labs_with_rust/tree/main/Authentication/username_enumeration_via_subtly_different_responses) for this lab in both single-threaded and multi-threaded approaches.

### Happy Hacking 👾
