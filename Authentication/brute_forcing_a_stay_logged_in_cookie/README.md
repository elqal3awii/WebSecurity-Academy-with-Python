# Hack Steps
1. Hash every the password
2. Encrypt every tha hash with the username in the cookie
3. GET /my-account page with every encrypted cookie

# Run Script
1. change the URL of the lab
3. change the PATH for you passwords list
4. Start script
```
~$ cargo run
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

You can see the comparison I made with these numbers when solving the [Lab: Username enumeration via different responses](https://github.com/elqalawii/portswigger_labs_with_rust/tree/main/Authentication/username_enumeration_via_different_responses) to see the big difference in speed between Rust and Python and also between single-threaded and multi-threaded approaches in Rust.

### Happy Hacking 👾
