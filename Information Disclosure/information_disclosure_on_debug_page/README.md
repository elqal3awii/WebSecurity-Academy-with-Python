# Hack Steps

1. Check the source code of a product page
2. GET the href of the commented a tag named "Debug"
3. Extract the secret key
4. submit the answer

# Run Script

1. change the URL of the lab
2. Start script

```
~$ python information_disclosure_on_debug_page.py
```

# Expected Output

```
1. Checking the source code.. OK
2. Extracting the debug path.. OK => /**/**.php
3. Fetching the debug page.. OK
4. Extracting the secret key.. OK => 8ewgag7yl0vf8dfbti11d0gy6rr1ie37
5. Submitting the answer.. OK
[#] Check your browser, it should be marked now as solved
```
