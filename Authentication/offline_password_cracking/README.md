## Hack Steps
1. Exploit XSS vulnerability in comment functionlity
2. Extract victim cookie from the exploit server logs
3. Decode the cookie to get the hashed password
4. Crack the hash to get the plain password

# Run Script
1. change the URL of the lab
2. Start script
```
~$ cargo run
```

# Expected Output
```
1. Exploit XSS in comment functionality.. ☑️
2. Get stay-logged-in cookie of the victim from exploit sever logs.. ☑️
3. Decoding the encrypted cookie.. ☑️
✅ Password hash: 26323c16d5f4dabff3bb136f2460a943
Crack this hash using any online hash cracker
```

