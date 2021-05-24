# mybirthday
* Bài này chúng ta có thể nhìn thấy trong ida là có 1 lỗi buffer overflow
* Lợi dụng lỗi chúng ta có offset từ chỗ nhập đến biến v5(biến cần thay đổi giá trị) là 0x18
* Điều kiện để chúng ta có thể cat flag là thay đổi giá trị của biến v5 trong ida thành 0xCABBFEFF thì lúc này chương trình sẽ gọi cho chúng ta 1 shell để cat flag

![mybirthday](https://user-images.githubusercontent.com/51597903/119294483-c0b63580-bc7e-11eb-99a3-6cae9c997a05.png)


# Bank1
* Bài này đề chỉ cho chúng ta nc 61.28.237.24 30202, và khi vào thì chúng ta sẽ được nhập 1 chuỗi bất kỳ
* Do đó mình nghĩ ngay đế buffer overflow và nhập 1 chuỗi thật dài
* Kết quả là flag được in ra trên màn hình

![Bank1](https://user-images.githubusercontent.com/51597903/119293394-88155c80-bc7c-11eb-8da2-1b246954a470.png)


# Bank2
* Vào Ida chúng ta thấy ở đây hàm main sẽ gọi hàm Register() và hàm này sẽ có 1 lỗi buffer overflow ở hàm gets()
* Bài này tương tự bài mybirthday chúng ta cũng sẽ đi thay đổi giá trị của biến balance thành giá trị 0x66A44 để gọi hàm getFlag() và có được flag thôi
* Offset của bài này là 0x40

![Bank2](https://user-images.githubusercontent.com/51597903/119294825-8e590800-bc7f-11eb-8512-34d0c9376808.png)


# Bank3
* Bank3 thì tương tự Bank2 nhưng chỉ khác ở chỗ đó là hàm Register() không có gọi hàm getFlag()
* Do đó chúng ta sẽ phải tự gọi hàm getFlag() bằng cách làm tràn stack cho đến return address của hàm Register() và thay đổi giá trị ở đây thành địa chỉ của hàm getFlag()
* Offset của bài này là 0x50, và địa chỉ của hàm getFlag() là 0x8048506

![Bank3](https://user-images.githubusercontent.com/51597903/119294901-bb0d1f80-bc7f-11eb-884e-159d3cf20e8b.png)


# Bank4
* Bank4 lại là 1 phiên bản nâng cấp của Bank3 là cũng sẽ gọi hàm nhưng có thêm truyền tham số. Hàm Register() cũng không gọi hàm getFlag()
* Tuy nhiên hàm getFlag() lần này lại cần những điều kiện nhất định để có thể cat được flag (biến o1 và o2 phải bằng 1)
* Đầu tiên chúng ta sẽ gọi hàm up2() với 3 tham số truyền vào sao cho tham số thứ 1 = tham số thứ 2, tham số thứ ba thì sẽ = 0x12345678 để đạt được biến o2 = 1, sau đó quay lại hàm main()
* Tiếp theo chúng ta gọi hàm up1() với 2 tham số truyền vào sao cho tham số thứ nhất = 0x1337, tham số thứ hai = 0xDEAD, trước đó thì biến o2  phải = 1, sau đó lại quay về hàm main()
* Cuối cùng chúng ta chỉ cần gọi hàm getFlag() thế là xong 
* Offset của bài này là 0x50, địa chỉ các hàm cần thiết u2 = 0x80488db, u1 = 0x80488a5, getFlag = 0x8048906, main = 0x80489b0

![Bank4](https://user-images.githubusercontent.com/51597903/119295001-f4458f80-bc7f-11eb-9b82-de8fd9c7b85d.png)


# Bank5
* Bank5 khá thú vị vì nó cũng gọi hàm gets() trong hàm Register() tuy nhiên không hề có hàm getFlag() nào cả, cũng không thể chèn shellcode vào bất cứ vùng nào có quyền rwx, cũng không thể leak được địa chỉ để tìm libc của bài
* Vậy hướng exploit là chúng ta sẽ dùng ropchain
* May mắn thay chúng ta sử dụng 1 công cụ ROPgadget và dễ dàng tìm được 1 ropchain phù hợp để gọi 1 shell
* Việc còn lại là chỉ cần ghi đè địa chỉ trả về của hàm Register() thành địa chỉ đầu tiên của ropchain là xong
* Offset của bài này là 0x50

![Bank5](https://user-images.githubusercontent.com/51597903/119295078-1fc87a00-bc80-11eb-9afb-5bc3e7fae98c.png)


# Bank6
* Ở bài này trong hàm Register() chúng ta chỉ được nhập 1036 kí tự vào biến name
* Biến name thì chúng ta có thể lấy được địa chỉ vì chương trình sẽ in ra màn hình
* Tuy nhiên ở bài này chúng ta không thể tính offset khá căng, mặt khác chúng ta lại có thể ghi shellcode vào 1 số vùng trong đó có stack
* Sau 1 hồi debug thì nhận thấy nếu nhập đủ 1036 hoặc hơn thì khi từ Register() quay về welcome() và từ welcome thì nó đã bị ghi đè địa chỉ thành những kí tự chúng ta nhập vào khi nãy
* Thế là ý tưởng giải quyết bài này do mình có thể lấy được địa chỉ nơi mình nhập và có thể ghi shellcode, nên mình quyết định ghi shellcode vào stack và return về nó. Vấn đề cuối cùng chính là làm sao để điều khiển việc ret về shellcode vì không thể tính được offset
* Do đó mình quyết định ghi sh vào stack và còn lại mình sẽ ghi địa chỉ stack mà mình leak được ở trên thì như ở trên khi nhập 1036 kí tự vào thì chắc chắn địa chỉ trả về của hàm welcome() sẽ bị ghi đè thành những kí tự mình nhập ở trên, và thế là thành công

![Bank6](https://user-images.githubusercontent.com/51597903/119349830-d6504d00-bcc8-11eb-844d-0309b13b6e8c.png)


# SecretWeapon
* Bài này chúng ta sẽ bị random địa chỉ do đó không thể nào chúng ta ret về hàm arsenal() được
* Tuy nhiên chúng ta được chương trình in ra 1 địa chỉ đó là địa chỉ của hàm townsquare(), nhờ đó chúng ta có thể dễ dàng tính được base của vùng code nhờ vào ida và địa chỉ hàm townsquare()
* Khi đã tính được base chúng ta sẽ  dễ dàng tính được địa chỉ hàm arsenal() vì offset của hàm cũng có trong ida
* Sau đó chúng ta chỉ cần ghi đè địc chỉ trả về thành địa chỉ của hàm arsenal() và lấy được shell
* offset của bài này 0x1c, các offset của arsenal() = 0x12D6, của townsquare() = 0x12ff

![SecretWeapon](https://user-images.githubusercontent.com/51597903/119295368-da587c80-bc80-11eb-8d3f-613ab75e292d.png)
