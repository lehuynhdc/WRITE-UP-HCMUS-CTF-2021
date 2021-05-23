# Description

- Nhìn tên chall là nghi vấn git directory leak rồi. Test thử trên url: `/.git`, `/.git/index`,... đều báo 403.
- Test thử ô input với post request: /etc/password => 200 ok.
- Vậy là biết được idea của author là sử dụng lfi vuln để leak git directory.
- Trước tiên phải lấy được các commit-sha thông qua history (`.git/logs/refs/heads/main`) và context của chúng (`.git/objects/{2_bit_dau}/{38_bit_cuoi}`) và cuối cùng là dùng tool để extract các commit để xem được nội dung của các dữ liệu đã được commit trước đó.
- Để dể dàng lấy được context chính xác của từng commit-sha thì phải encode nó thông qua **LFI wrapper** `php://filter/convert.base64-encode/resource=.git/objects/{2_bit_dau}/{38_bit_cuoi}`.
## Khó Khăn

- Author sử dụng token -> không thể dùng tool bên ngoài được, phải tự code tool.
## Usage
 
 - Tạo folder `~/hades101`, đặt hades_dumpgit.py vào thư mục trên, và run nó.
 - Sử dụng `extractor.sh` của tool (GitTool) để extract : `./extractor.sh ~/hades101 hades_extract`
