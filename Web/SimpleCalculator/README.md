# Description
- Biết được source code đang dùng **eval()** để tính các phép tính của mình truyền vào.
- Đầu tiên test sơ bộ qua thì biết chall này đã filter các ký tự alphabet và 1 số ký tự đặc biệt như  ``",',\`,..`` Và giớ hạn length < 20.
- Idea sử dụng php magic vd : (ph.pin.f.o)() => phpinfo() . Bây giờ để bypass filter ta sẽ sử dụng **Bitwise NOT** trong php để đão bit các chữ cái, lợi dụng vào chức năng đó ta có thể đão ngược bit của chuỗi ` ~(phpinfo) => \x8f\x97\x8f\x96\x91\x99\x90 ` và `~\x8f\x97\x8f\x96\x91\x99\x90 => phpinfo`, mà những ký tự unicode này thì không bị filter.
- Payload cuối cùng `http://61.28.237.24:30101/?equation=(~%8c%86%8c%8b%9a%92)(~%9c%9e%8b%df%d0%d5)` <=> **system(cat /*)**  do chúng ta get request trực típ trên url nên phải dùng url encode.
=> `HCMUS-CTF{d4ngErous_eVal}`
