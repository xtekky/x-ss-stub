import hashlib

data = "password=4z6d6f6c75604535313434&account_sdk_source=app&username=7d7xx0ze6exx&mix_mode=1&multi_login=1"

print(str(hashlib.md5(data.encode()).hexdigest()).upper())
