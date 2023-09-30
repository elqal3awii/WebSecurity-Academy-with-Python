## Hack Steps
1. Send multiple passwords in the same login request
2. Obtain the new session from cookie header
3. Login as carlos with the new session

# Run Script
1. Change the URL of the lab
2. Start script
```
~$ python broken_brute_force_protection_multiple_credentials_per_request.py
```

# Expected Output
```
[*] Sending multiple passwords in the same request.. OK
✅ Successfully logged in as carlos
[#] Use this 2aQWuvvBd0vzGRtC4UE3YSTzFzJDPx7Z session in your browser to login as carlos
```

