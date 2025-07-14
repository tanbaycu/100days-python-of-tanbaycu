# Bài Tập Cơ Bản - Ngày 1-2: Print và Input

## Mục Tiêu
- Học cách sử dụng hàm `print()`
- Học cách sử dụng hàm `input()`
- Hiểu về string (chuỗi)
- Kết hợp input và print

---

## Phần 1: Hàm print() - In Ra Màn Hình

### Lý Thuyết Cơ Bản
```python
print("Nội dung muốn in")
print('Có thể dùng dấu nháy đơn')
print("Hoặc dấu nháy kép")
```

### Bài Tập 1.1: Hello World Cơ Bản
**Yêu cầu**: In ra 3 dòng text khác nhau

```python
# Bài giải:
print("Hello World!")
print("Xin chào Python!")
print("Học lập trình rất thú vị!")
```

**Kết quả**:
```
Hello World!
Xin chào Python!
Học lập trình rất thú vị!
```

### Bài Tập 1.2: In Nhiều Dòng
**Yêu cầu**: In ra thông tin cá nhân (tên, tuổi, sở thích)

```python
# Bài giải:
print("=== THÔNG TIN CÁ NHÂN ===")
print("Tên: Nguyễn Văn A")
print("Tuổi: 20")
print("Sở thích: Lập trình Python")
print("========================")
```

### Bài Tập 1.3: Sử Dụng Ký Tự Đặc Biệt
**Yêu cầu**: Tạo khung đẹp cho text

```python
# Bài giải:
print("*" * 30)
print("*   CHÀO MỪNG ĐÊN PYTHON   *")
print("*" * 30)
print()  # Dòng trống
print("🐍 Python là ngôn ngữ tuyệt vời!")
```

**Kết quả**:
```
******************************
*   CHÀO MỪNG ĐÊN PYTHON   *
******************************

🐍 Python là ngôn ngữ tuyệt vời!
```

---

## Phần 2: Hàm input() - Nhập Từ Bàn Phím

### Lý Thuyết Cơ Bản
```python
# Cú pháp cơ bản
ten = input("Nhập tên của bạn: ")
print("Xin chào " + ten)

# Hoặc dùng f-string (hiện đại hơn)
print(f"Xin chào {ten}")
```

### Bài Tập 2.1: Chào Hỏi Đơn Giản
**Yêu cầu**: Nhập tên và chào hỏi

```python
# Bài giải:
ten = input("Nhập tên của bạn: ")
print("Xin chào " + ten + "!")
print(f"Rất vui được gặp bạn, {ten}!")
```

**Chạy thử**:
```
Nhập tên của bạn: Minh
Xin chào Minh!
Rất vui được gặp bạn, Minh!
```

### Bài Tập 2.2: Thông Tin Chi Tiết
**Yêu cầu**: Nhập nhiều thông tin và hiển thị đẹp

```python
# Bài giải:
print("=== FORM ĐĂNG KÝ ===")
ho_ten = input("Họ và tên: ")
tuoi = input("Tuổi: ")
noi_song = input("Nơi sống: ")
so_thich = input("Sở thích: ")

print("\n" + "="*25)
print("THÔNG TIN CỦA BẠN")
print("="*25)
print(f"Họ tên: {ho_ten}")
print(f"Tuổi: {tuoi}")
print(f"Nơi sống: {noi_song}")
print(f"Sở thích: {so_thich}")
print("="*25)
```

### Bài Tập 2.3: Lời Chào Tùy Chỉnh
**Yêu cầu**: Tạo lời chào dựa trên thời gian trong ngày

```python
# Bài giải:
ten = input("Tên của bạn: ")
buoi = input("Bây giờ là buổi gì? (sáng/chiều/tối): ")

if buoi == "sáng":
    print(f"Chào buổi sáng {ten}! Hôm nay học Python nhé!")
elif buoi == "chiều":
    print(f"Chào buổi chiều {ten}! Tiếp tục coding thôi!")
else:
    print(f"Chào buổi tối {ten}! Học Python buổi tối rất tập trung!")
```

---

## Phần 3: Bài Tập Thử Thách

### Thử Thách 3.1: Máy Tính Cơ Bản
**Yêu cầu**: Nhập 2 số và tính tổng

```python
# Bài giải:
print("=== MÁY TÍNH CƠ BẢN ===")
so_thu_nhat = input("Nhập số thứ nhất: ")
so_thu_hai = input("Nhập số thứ hai: ")

# Chuyển đổi string thành số
so_1 = int(so_thu_nhat)
so_2 = int(so_thu_hai)

tong = so_1 + so_2

print(f"{so_1} + {so_2} = {tong}")
```

**Chạy thử**:
```
=== MÁY TÍNH CƠ BẢN ===
Nhập số thứ nhất: 15
Nhập số thứ hai: 25
15 + 25 = 40
```

### Thử Thách 3.2: Thông Tin Sinh Viên
**Yêu cầu**: Tạo thẻ sinh viên đẹp

```python
# Bài giải:
print("🎓 ĐĂNG KÝ THÔNG TIN SINH VIÊN 🎓")
print("-" * 40)

ho_ten = input("Họ và tên: ")
ma_sv = input("Mã sinh viên: ")
lop = input("Lớp: ")
khoa = input("Khoa: ")
diem_tb = input("Điểm trung bình: ")

print("\n" + "🎓" + "="*38 + "🎓")
print("           THẺ SINH VIÊN")
print("🎓" + "="*38 + "🎓")
print(f"│ Họ tên: {ho_ten:<28}│")
print(f"│ MSSV: {ma_sv:<30}│")
print(f"│ Lớp: {lop:<31}│")
print(f"│ Khoa: {khoa:<30}│")
print(f"│ Điểm TB: {diem_tb:<27}│")
print("🎓" + "="*38 + "🎓")
```

### Thử Thách 3.3: Game Đoán Tuổi
**Yêu cầu**: Đoán tuổi dựa trên năm sinh

```python
# Bài giải:
print("🎯 GAME ĐOÁN TUỔI 🎯")
ten = input("Tên của bạn: ")
nam_sinh = input("Năm sinh của bạn: ")

# Tính tuổi (giả sử hiện tại là 2024)
nam_hien_tai = 2024
tuoi = nam_hien_tai - int(nam_sinh)

print(f"\n🎉 Xin chào {ten}!")
print(f"📅 Năm {nam_hien_tai}, bạn {tuoi} tuổi")

if tuoi < 18:
    print("🧒 Bạn còn nhỏ, học hành chăm chỉ nhé!")
elif tuoi < 25:
    print("👨‍🎓 Tuổi học tập, cố gắng lên!")
else:
    print("👨‍💼 Đã trưởng thành, chúc thành công!")
```

---

## Phần 4: Xử Lý Lỗi Thường Gặp

### Lỗi 1: SyntaxError
```python
# Sai:
print("Hello World!)  # Thiếu dấu nháy

# Đúng:
print("Hello World!")
```

### Lỗi 2: NameError
```python
# Sai:
print(ten)  # Biến chưa được định nghĩa

# Đúng:
ten = input("Nhập tên: ")
print(ten)
```

### Lỗi 3: Quên Chuyển Đổi Kiểu
```python
# Sai:
tuoi = input("Tuổi: ")
nam_sau = tuoi + 1  # Lỗi: không thể cộng string với số

# Đúng:
tuoi = int(input("Tuổi: "))
nam_sau = tuoi + 1
```

---

## Phần 5: Bài Tập Thực Hành Thêm

### Bài 5.1: Máy Tính Nâng Cao
```python
# Yêu cầu: Tính cả 4 phép toán cơ bản
so_a = int(input("Số thứ nhất: "))
so_b = int(input("Số thứ hai: "))

print(f"\n🧮 KẾT QUẢ TÍNH TOÁN:")
print(f"{so_a} + {so_b} = {so_a + so_b}")
print(f"{so_a} - {so_b} = {so_a - so_b}")
print(f"{so_a} × {so_b} = {so_a * so_b}")
print(f"{so_a} ÷ {so_b} = {so_a / so_b}")
```

### Bài 5.2: Tính Diện Tích Hình Chữ Nhật
```python
print("📐 TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT")
chieu_dai = float(input("Chiều dài (m): "))
chieu_rong = float(input("Chiều rộng (m): "))

dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

print(f"\n📊 KẾT QUẢ:")
print(f"Diện tích: {dien_tich} m²")
print(f"Chu vi: {chu_vi} m")
```

### Bài 5.3: Chuyển Đổi Tiền Tệ Đơn Giản
```python
print("💰 CHUYỂN ĐỔI USD SANG VND")
usd = float(input("Số tiền USD: "))
ty_gia = 24000  # 1 USD = 24,000 VND

vnd = usd * ty_gia

print(f"\n💵 {usd} USD = {vnd:,.0f} VND")
print(f"(Tỷ giá: 1 USD = {ty_gia:,} VND)")
```

---

## Kiểm Tra Hiểu Bài

### Quiz 1: Kết quả của đoạn code này là gì?
```python
print("Python")
print("is")
print("awesome!")
```

**Đáp án**:
```
Python
is
awesome!
```

### Quiz 2: Sửa lỗi trong code sau
```python
ten = input("Tên: ")
print("Xin chào " + ten)
print(f"Bạn tên {ten}"  # Thiếu gì?
```

**Đáp án**: Thiếu dấu `)` ở cuối dòng 3

### Quiz 3: Viết code để làm gì?
**Yêu cầu**: Nhập tên và in ra "Tên của bạn có X ký tự"

```python
# Đáp án:
ten = input("Nhập tên: ")
so_ky_tu = len(ten)
print(f"Tên của bạn có {so_ky_tu} ký tự")
```

---

## Bài Tập Về Nhà

### Bài 1: Profile Cá Nhân
Tạo chương trình nhập và hiển thị:
- Tên, tuổi, quê quán
- Môn học yêu thích
- Ước mơ nghề nghiệp
- In ra dưới dạng CV đẹp

### Bài 2: Máy Tính Tiền Tip
Nhập:
- Tổng tiền hóa đơn
- Phần trăm tip (15%, 18%, 20%)
Tính và hiển thị:
- Tiền tip
- Tổng tiền phải trả

### Bài 3: Game Giới Thiệu Bản Thân
Tạo chương trình hỏi:
- 5 câu hỏi về bản thân
- Sau đó tạo ra story ngắn từ các câu trả lời

---

## Ghi Chú Quan Trọng

### Quy Tắc Đặt Tên Biến
```python
# Đúng:
ho_ten = "Minh"
tuoi = 20
diem_toan = 8.5

# Sai:
họ tên = "Minh"      # Có dấu cách
2tuoi = 20           # Bắt đầu bằng số
class = "10A"        # Từ khóa của Python
```

### Tips Viết Code Đẹp
1. **Comment giải thích**: `# Đây là comment`
2. **Tên biến có ý nghĩa**: `diem_toan` thay vì `d`
3. **Xuống dòng hợp lý**: Tách phần logic
4. **Thụt đầu dòng đồng nhất**: 4 spaces

### Shortcuts Hữu Ích
- `Ctrl+/`: Comment/uncomment
- `Ctrl+D`: Duplicate line
- `Alt+↑/↓`: Di chuyển dòng
- `Ctrl+Shift+K`: Xóa dòng

Hoàn thành tất cả bài tập này, bạn đã nắm vững cơ bản về `print()` và `input()`! 🎉 