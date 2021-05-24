#mybirthday
* Bài này chúng ta có thể nhìn thấy trong ida là có 1 lỗi buffer overflow
* Lợi dụng lỗi chúng ta có offset từ chỗ nhập đến biến v5(biến cần thay đổi giá trị) là 0x18
* Điều kiện để chúng ta có thể cat flag là thay đổi giá trị của biến v5 trong ida thành 0xCABBFEFF thì lúc này chương trình sẽ gọi cho chúng ta 1 shell để cat flag

![mybirthday](https://user-images.githubusercontent.com/51597903/119294483-c0b63580-bc7e-11eb-99a3-6cae9c997a05.png)


#Bank1
* Bài này đề chỉ cho chúng ta nc 61.28.237.24 30202, và khi vào thì chúng ta sẽ được nhập 1 chuỗi bất kỳ
* Do đó mình nghĩ ngay đế buffer overflow và nhập 1 chuỗi thật dài
* Kết quả là flag được in ra trên màn hình

![Bank1](https://user-images.githubusercontent.com/51597903/119293394-88155c80-bc7c-11eb-8da2-1b246954a470.png)


#Bank2

![Bank2](https://user-images.githubusercontent.com/51597903/119294825-8e590800-bc7f-11eb-8512-34d0c9376808.png)

#Bank3

![Bank3](https://user-images.githubusercontent.com/51597903/119294901-bb0d1f80-bc7f-11eb-884e-159d3cf20e8b.png)


#Bank4
![Bank4](https://user-images.githubusercontent.com/51597903/119295001-f4458f80-bc7f-11eb-9b82-de8fd9c7b85d.png)


#Bank5

![Bank5](https://user-images.githubusercontent.com/51597903/119295078-1fc87a00-bc80-11eb-9afb-5bc3e7fae98c.png)

#Bank6
![Bank6](https://user-images.githubusercontent.com/51597903/119295153-51d9dc00-bc80-11eb-94e2-e0dcd8a05686.png)


#SecretWeapon

![SecretWeapon](https://user-images.githubusercontent.com/51597903/119295368-da587c80-bc80-11eb-8d3f-613ab75e292d.png)


#StrangerThing
![StrangerThing](https://user-images.githubusercontent.com/51597903/119295256-92395a00-bc80-11eb-843e-58c90a822bda.png)
