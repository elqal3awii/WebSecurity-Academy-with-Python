# Hack Steps
1. Hash every the password
2. Encrypt every tha hash with the username in the cookie
3. GET /my-account page with every encrypted cookie

# Run Script
1. Change the URL of the lab
2. Change the PATH for you passwords list
3. Start script
```
~$ python brute_forcing_a_stay_logged_in_cookie.py
```

# Expected Output
```
[#] Brute frocing password of carlos..
[*] Password: 121212     => NOT Correct
✅ Correct pass: : 000000

✅ Finished in: 0 minutes
```
# Test Samples
This test is done using only 100 passwods. What about 10K passwords?
Or what about 100K passwords?

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/username_enumeration_via_different_responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.

