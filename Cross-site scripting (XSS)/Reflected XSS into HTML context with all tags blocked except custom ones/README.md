## Hack Steps

1. Craft a script that will redirect the victim to the vulnerable website with the injected payload in the search query parameter
2. Deliver the exploit to the victim
3. The alert() function will be called after they trigger the exploit

## Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python main.py
```

## Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The alert() function will be called after they trigger the exploit
🗹 The lab should be marked now as solved
```
