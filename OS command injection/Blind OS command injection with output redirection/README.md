## Hack Steps

1. Fetch the feedback page
2. Extract the csrf token and session cookie
3. Inject payload into the name field when submitting a feedback to execute the `whoami` command and redirect the output to a text file in a writable directory
4. Read the new created file


## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection point: name
⦗1⦘ Fetching the feedback page.. OK
⦗2⦘ Extracting the csrf token and session cookie.. OK
⦗3⦘ Injecting payload to execute the `whoami` command and redirect the output to whoami.txt.. OK
⦗4⦘ Reading whoami.txt.. OK => peter-0jgr96
🗹 The lab should be marked now as solved
```
