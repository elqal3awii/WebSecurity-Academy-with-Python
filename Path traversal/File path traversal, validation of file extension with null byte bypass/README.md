# Hack Steps

1. Inject payload into 'filename' query parameter to retrieve the content of /etc/passwd 
2. Extract the first line as a proof


# Run Script

1. Change the URL of the lab
2. Start script

```
~$ python file_path_traversal_validation_of_file_extension_with_null_byte_bypass.py
```

# Expected Output

```
⟪#⟫ Injection parameter: filename
⦗1⦘ Injecting payload to retrieve the content of /etc/passwd.. OK
⦗2⦘ Extracting the first line as a proof.. OK => root:x:0:0:root:/root:/bin/bash
🗹 The lab should be marked now as solved
```
