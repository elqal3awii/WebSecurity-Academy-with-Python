# Hack Steps
1. Obtain a valid username via different error messages
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

# Test Samples
### Objective
See how much time the script will take to find a valid credentials

### How to test?
1. Obtain a valid username & password using Burp Suite or by runnig this script with the username & passwords lists provided on the Burp Suite Academy.
2. put the valid credentials at the bottom of both lists (simulating the worst case).

### Run tests
When running this script on a Core i7, 4th generation laptop with 16G RAM, I obtain the following results:

#### 1K users & 1K password
It toke approximately **16.6** minutes 

You can reduce the time to **13.6** minutes 
using single-threaded rust script.

Not an improvment to care about, right? That's because the list is so small.

With mutli-threaded rust script you can reduce the time to only **2** minutes!

But it is still not a very big difference.

#### 10K users & 10K passwords
It toke approximately **154.7** minutes 

You can reduce the time to **135** minutes 
using single-threaded rust script.
Check [Single-threaded Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses/single-threaded) for this lab and run it yourself to see the difference.

With mutli-threaded rust script you can reduce the time to only **13** minutes! things begin to be interesting now.
Check [Multi-threaded Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses/multi-threaded) for this lab and run it yourself to see the difference.

### 100K users & 100K passwords
From the above test, we infere that it should take about **25.7** hours. Of course no one will even think to try it.

With mutli-threaded rust script you can reduce the time to only **2.5** hours! things begin to be interesting now.
Check [Multi-threaded Rust script](https://github.com/elqal3awii/WebSecurity-Academy-with-Rust/tree/main/Authentication/Username%20enumeration%20via%20different%20responses/multi-threaded) for this lab and run it yourself to see the difference.
