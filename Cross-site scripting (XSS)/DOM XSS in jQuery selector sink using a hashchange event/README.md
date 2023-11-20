# Hack Steps

1. Craft an iframe that when loaded will append an img element to the hash part of the URL
2. Deliver the exploit to the victim
3. The print() function will be called after they trigger the exploit

# Run Script

1. Change the URL of the lab
2. Change the URL of the exploit server
3. Start script

```
~$ python dom_xss_in_jquery_selector_sink_using_a_hashchange_event.py
```

# Expected Output

```
❯❯ Delivering the exploit to the victim.. OK
🗹 The print() function will be called after they trigger the exploit
🗹 The lab should be marked now as solved
```
