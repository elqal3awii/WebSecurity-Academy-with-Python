## Hack Steps

1. Adjust the frame dimensions and the decoy button offset
2. Set the email field using a URL query parameter
3. Set the sandbox attribute of the iframe to "allow-form" to bypass the frame buster script
4. Deliver the exploit to the victim

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
🗹 The victim's email will be changed after clicking on the decoy button
🗹 The lab should be marked now as solved
```
