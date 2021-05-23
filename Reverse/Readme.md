### Written by Konoha

# Faded
+ Vì đây là file được viết bằng python nên sử dụng `pyi-archive_viewer` để decompile lại file thực thi.
+ Cú pháp: `pyi-archive_viewer authentication` Sau đó `X authentication` để extract file, tiếp tục `output.pyc` để lưu vào file *output.pyc* 
+ Vì flag không biến đổi gì nên có thể xem flag bằng câu lệnh `cat`. Nếu flag bị biến đổi thì phải đưa file `.pyc` về file `.py` để đọc code
> FLAG: HCMUS-CTF{Python_is_fun_somehow}

# AndroidRev
+ Các tool, web sử dụng: **Bytecode-Viewer-2.9.22.jar** để decompile và đọc code java, **apktool_2.5.0.jar** để dump file để có thể xem phần resources, *https://www.md5online.org/md5-decrypt.html* để decrypt MD5.
+ Đầu tiên dump file **androidrev.apk** sau đó đọc đưa file **androidrev.apk** vào **Bytecode-Viewer-2.9.22.jar**, đọc  code tại file **/com/hcmusctf/androidrev/FlagChecker.class** hàm **checkFlag** để hiểu rõ bản chất vấn đề.
+ Giải thích một chút về `var0.getString(2131492904)` tại hàm "me": chương trình sẽ lấy chuỗi tương ứng với số *2131492904*; để tìm ra được chuỗi tương ứng với số này, vào file `R.class` và tìm kiếm số này và lấy tên biến được gán chuỗi đó (Ví dụ: số *2131492904* thì lấy tên biến tương ứng là *ml*) sau đó vào folder được dump file **androidrev.apk** ra bởi **apktool_2.5.0.jar**, ở **androidrev\res\values** sẽ thấy được file *strings.xml*, mở lên và tìm chuỗi tương ứng với tên biến (Ví dụ chữ *ml* thì sẽ được chuỗi *slauqe*). Tương tự các phần còn lại, ta rút gọn được vấn đề:
```java
me(var0, dh(MD5, var3[0]), 6e9a4d130a9b316e9201238844dd5124) 
me(var0, dh(MD5, var3[1]), 7c51a5e6ea3214af970a86df89793b19) 
me(var0, dh(MD5, var3[2]), e5f20324ae520a11a86c7602e29ecbb8) 
me(var0, dh(MD5, var3[3]), 1885eca5a40bc32d5e1bca61fcd308a5) 
me(var0, dh(MD5, var3[4]), da5062d64347e5e020c5419cebd149a2) 
me(var0, dh(SHA-256, var1), 58150e58ae8a7275fcce5aea7d983ab5654f549cbeecedec27c89fe8246937d5) 
```
+ Sử dụng *https://www.md5online.org/md5-decrypt.html* để decrypt các mã MD5 trên.
> FLAG: HCMUS-CTF{peppa-9876543-BAAAM-A1z9-3133337}

# WeirdProtocol
+ Sử dụng `Detect it Easy` xem sơ qua file, và phát hiện ở phần resources có một tệp nhị phân.
+ Sử dụng `pestudio` để dump file từ resource ra và reverse cả 2 file. Hiểu được chương trình `WeirdProtocol.exe` khi thực thi sẽ cho nhập password, sau đó chương trình sẽ gửi 2 lần, lần 1 sẽ là gửi độ dài của chuỗi nhập, lần 2 sẽ là gửi chuỗi nhập.
+ Ở file server chú ý tại:
```c
	if ( !j__memcmp(Buf1, Buf2, 32u) )
	{
		for ( i = 0; i < 30; ++i )
	  		v6[i] ^= v12[(int)i % v10[0]];
		Str = v6;	
	}
	else
	{
		Str = "Nice try buddy";
	}
```
+ Đoạn này sẽ kiểm tra Buf1(sử dụng chuỗi đã nhập và biến đổi các thứ) và Buf2 (được gán phía trên) có giống nhau không, sau đó sẽ biến đổi chuỗi nhập *V12* với *V6* thành flag và gán vào *Str*.
+ Sử dụng v6[0] đến v6[9] để XOR với 'HCMUS-CTF{' thì thấy được của chuỗi *hellohello*. Thử sử dụng chuỗi input là *hellohellohellohellohellohellohellohello* để nhập vào từ client.
+ Tại server, path tại địa chỉ *00327994* từ `jnz     short loc_3279FC` thành `jz     short loc_3279FC`. Flag sẽ gửi xuống server.
```
[+] Please enter the password: hellohellohellohellohellohellohellohello
[+] Connecting to the online service ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
[+] Fail, reconnecting ...
-----> HCMUS-CTF{not_so_weird_hehexd}
```
> FLAG: HCMUS-CTF{not_so_weird_hehexd}
