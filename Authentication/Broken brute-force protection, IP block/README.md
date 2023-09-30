# Hack Steps
1. Brute force carlos password
2. After every 2 tries, login with correct credentials to bypass blocking

# Run Script
1. Change the URL of the lab
2. Change the PATH of your password list
3. Start script
```
~$ python broken_brute_force_protection_ip_block.py
```

# Expected Output
```
✅ Valid user: carlos
Elapsed:   0 minutes || Failed:   0 || Trying (47/102):                                     

✅ Login successfully: username: ae, password: robert
✅ Finished in: 0 minutes

Restults was saved to: results

[!] Failed password count: 0 
[!] Failed password : []
```
# Test Samples
This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.
