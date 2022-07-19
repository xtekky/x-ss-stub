If u debug TikTok api requests, sometimes you encounter the x-ss-stub param on post requests and wonder what it is, well here is an in-depth analysis, enjoy.

![image](https://user-images.githubusercontent.com/98614666/179641196-93b63478-e10a-422f-a33c-631d7344d683.png)

#### Encryption algorithm:
- Couldn't be simpler, its an md5 hash, in uppercase

![image](https://user-images.githubusercontent.com/98614666/179641595-9243ed30-a230-4da5-beba-99afd3f44084.png)

#### Encrypted data:
- The encrypted data is the urlencoded post data/body

![image](https://user-images.githubusercontent.com/98614666/179642146-8c1d4755-a906-48b5-b5ac-6a5c8fab37bc.png)

#### use case:
- x-ss-stub may be required as encryption key/param for some algorithms such as x-gorgon


#### python script to generate x-ss-stub:
```python
import hashlib

data = "password=4z6d6f6c75604535313434&account_sdk_source=app&username=7d7xx0ze6exx&mix_mode=1&multi_login=1"

print(str(hashlib.md5(data.encode()).hexdigest()).upper())
```
