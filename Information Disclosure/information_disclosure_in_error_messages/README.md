# Hack Steps

1. Inject a single quote in the product ID parameter to cause an error
2. Extract the framework name
3. Submit the answer

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python information_disclosure_in_error_messages.py
```

# Expected Output

```
1. Injecting the payload.. OK
2. Extracting the framework name.. OK => Apache Struts *.*.*
3. Submitting the answer.. OK
[#] Check your browser, it should be marked now as solved
```
