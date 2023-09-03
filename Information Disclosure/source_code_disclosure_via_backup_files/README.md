# Hack Steps

1. Fetch /robots.txt file
2. List the hidden directory
3. Fetch the hidden backup file
4. Extract the key
5. Submit the answer

# Run Script

1. change the URL of the lab
2. Start script

```
~$ python source_code_disclosure_via_backup_files.py
```

# Expected Output

```
1. Fetching the robots.txt file.. OK
2. Searching for hidden files.. OK => /backup
3. Fetching the backup directory.. OK
4. Extracting the path to the backup file.. OK => /backup/ProductTemplate.java.bak
5. Fetching the backup file.. OK
6. Extracting key .. OK => xydew2o4wwjnyn3z444f8rn3pdad1ld2
7. Submitting the answer.. OK
[#] Check your browser, it should be marked now as solved
```
