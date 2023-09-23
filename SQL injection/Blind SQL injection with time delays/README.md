# Hack Steps

1. Inject payload into 'TrackingId' cookie to cause a 10 seconds delay
2. Wait for the response 

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ cargo run
```

# Expected Output

```
[#] Injection point: TrackingId
1. Injecting payload to cause a 10 seconds delay.. OK
2. Waiting for the response.. OK
[#] Check your browser, it should be marked now as solved
```
