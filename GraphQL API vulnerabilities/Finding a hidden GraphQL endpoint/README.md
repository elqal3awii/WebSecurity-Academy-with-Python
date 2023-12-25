## Hack Steps

1. Find the hidden endpoint by trying multiple paths
2. Bypassing the introspection defenses by appending `__schema` with a new line before `{`
3. Analyze the introspection result
4. Delete carlos using the appropriate mutation

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Deleting carlos.. OK
🗹 The lab should be marked now as solved
```
