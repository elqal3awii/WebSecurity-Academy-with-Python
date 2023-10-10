# Hack Steps

1. Inject payload into "storeId" parameter to execute the `whoami` command
2. Observe the `whoami` output in the response

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python os_command_injection_simple_case.py
```

# Expected Output

```
❯ Injection point: storeId
❯ Injecting payload to execute the `whoami` command.. OK => peter-neh7X6
🗹 Check your browser, it should be marked now as solved
```
