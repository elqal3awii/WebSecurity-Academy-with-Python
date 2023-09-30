# Hack Steps
1. Login with correct creds
2. Change username when requesting change password API
3. Repeat the process trying every password

# Run Script
1. Change the URL of the lab
2. Change the PATH of your password list
3. Start script
```
~$ python password_brute_force_via_password_change.py
```

# Expected Output
```
[#] Brute forcing password of carlos..
[*] (30/100) mobilemail => Incorrect
[#] mom => Correct
[#] Password changed to: Hacked

✅ Finished in: 1 minutes
```
# Test Samples
This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.


