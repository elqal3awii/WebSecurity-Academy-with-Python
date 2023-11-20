# Hack Steps

1. Fetch a post page
2. Extract the session cookie and the csrf token to post a comment
3. Post a comment with the injected payload in the comment field

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python stored_xss_into_html_context_with_nothing_encoded.py
```

# Expected Output

```
⦗1⦘ Fetching a post page.. OK
⦗2⦘ Extracting the session cookie and the csrf token to post a comment.. OK
⦗3⦘ Posting a comment with the injected payload in the comment field.. OK
🗹 The lab should be marked now as solved
```
