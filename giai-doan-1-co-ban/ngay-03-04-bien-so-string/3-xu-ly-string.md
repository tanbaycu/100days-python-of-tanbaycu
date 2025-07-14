# Xử Lý String (Chuỗi) trong Python

## 1. String là gì?

String (chuỗi) là dãy các ký tự. Trong Python, string được đặt trong dấu ngoặc kép hoặc ngoặc đơn.

```python
ten = "Nguyen Van An"
lop = 'lop 10A'
thong_bao = "Chào mừng bạn đến với Python!"
```

## 2. Cách Tạo String

### 2.1 Dấu ngoặc đơn và kép
```python
# Cách 1: Dấu ngoặc kép
ho_ten = "Le Thi Nga"

# Cách 2: Dấu ngoặc đơn  
lop = 'Lop 10A'

# Cách 3: Ba dấu ngoặc (multiline)
thong_tin = """
Tên: Nguyen Van An
Tuổi: 18
Lớp: 10A
"""

# Cách 4: Dấu ngoặc trong string
cau_noi = "Cô giáo nói: 'Các em học bài về nhà'"
cau_noi2 = 'Anh ấy nói: "Tôi thích học Python"'
```

### 2.2 Escape Characters (Ký tự thoát)
```python
# Xuống dòng
text = "Dòng 1\nDòng 2"
print(text)
# Dòng 1
# Dòng 2

# Tab
text = "Cột 1\tCột 2"
print(text)  # Cột 1    Cột 2

# Dấu ngoặc kép trong string
text = "Anh ấy nói: \"Xin chào\""
print(text)  # Anh ấy nói: "Xin chào"

# Dấu gạch chéo ngược
duong_dan = "C:\\Users\\Documents"
print(duong_dan)  # C:\Users\Documents
```

## 3. Nối String

### 3.1 Toán tử + (Concatenation)
```python
ho = "Nguyen"
ten = "An"
ho_ten = ho + " " + ten
print(ho_ten)  # Nguyen An

# Nối nhiều string
chao = "Xin chào "
ten = "An"
cam_on = ", cảm ơn bạn!"
cau_chao = chao + ten + cam_on
print(cau_chao)  # Xin chào An, cảm ơn bạn!
```

### 3.2 f-string (Format string) - Khuyên dùng
```python
ten = "An"
tuoi = 18
# f-string
gioi_thieu = f"Tôi tên {ten}, {tuoi} tuổi"
print(gioi_thieu)  # Tôi tên An, 18 tuổi

# Với tính toán
diem_toan = 8
diem_ly = 7
tb = f"Điểm trung bình: {(diem_toan + diem_ly) / 2}"
print(tb)  # Điểm trung bình: 7.5

# Format số
gia = 150000
text = f"Giá: {gia:,} VND"
print(text)  # Giá: 150,000 VND
```

### 3.3 .format() method
```python
ten = "An"
tuoi = 18
text = "Tôi tên {}, {} tuổi".format(ten, tuoi)
print(text)  # Tôi tên An, 18 tuổi

# Với index
text = "Tôi tên {0}, {1} tuổi, tên tôi là {0}".format(ten, tuoi)
print(text)  # Tôi tên An, 18 tuổi, tên tôi là An
```

## 4. Các Method Quan Trọng

### 4.1 Kiểm tra độ dài
```python
text = "Hello Python"
do_dai = len(text)
print(do_dai)  # 12
```

### 4.2 Chuyển đổi chữ hoa/thường
```python
text = "Hello World"

print(text.upper())     # HELLO WORLD
print(text.lower())     # hello world
print(text.title())     # Hello World
print(text.capitalize()) # Hello world
print(text.swapcase())  # hELLO wORLD
```

### 4.3 Tìm kiếm và thay thế
```python
text = "Python is awesome, Python is easy"

# Tìm vị trí
vi_tri = text.find("Python")
print(vi_tri)  # 0 (vị trí đầu tiên)

vi_tri = text.find("Java")
print(vi_tri)  # -1 (không tìm thấy)

# Đếm số lần xuất hiện
so_lan = text.count("Python")
print(so_lan)  # 2

# Thay thế
text_moi = text.replace("Python", "Java")
print(text_moi)  # Java is awesome, Java is easy

# Thay thế có giới hạn
text_moi = text.replace("Python", "Java", 1)  # Chỉ thay 1 lần
print(text_moi)  # Java is awesome, Python is easy
```

### 4.4 Kiểm tra nội dung
```python
text = "Python123"

print(text.startswith("Python"))  # True
print(text.endswith("123"))       # True
print(text.isalpha())             # False (có số)
print(text.isdigit())             # False (có chữ)
print(text.isalnum())             # True (chữ + số)

text2 = "12345"
print(text2.isdigit())            # True
```

### 4.5 Tách và ghép
```python
# Tách string
text = "apple,banana,orange"
danh_sach = text.split(",")
print(danh_sach)  # ['apple', 'banana', 'orange']

# Tách theo khoảng trắng
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Ghép list thành string
fruits = ['apple', 'banana', 'orange']
text = ", ".join(fruits)
print(text)  # apple, banana, orange
```

### 4.6 Xóa khoảng trắng
```python
text = "   Hello World   "

print(text.strip())   # "Hello World"
print(text.lstrip())  # "Hello World   "
print(text.rstrip())  # "   Hello World"
```

## 5. Slicing (Cắt String)

### 5.1 Truy cập ký tự
```python
text = "Python"
print(text[0])   # P (ký tự đầu)
print(text[1])   # y
print(text[-1])  # n (ký tự cuối)
print(text[-2])  # o
```

### 5.2 Cắt đoạn
```python
text = "Python Programming"

print(text[0:6])    # Python
print(text[7:])     # Programming
print(text[:6])     # Python
print(text[::2])    # Pto rgamn (bước nhảy 2)
print(text[::-1])   # gnimmargorP nohtyP (đảo ngược)
```

## 6. Input và Validation

### 6.1 Nhận input
```python
ten = input("Nhập tên của bạn: ")
print(f"Xin chào {ten}!")

# Input số từ string
tuoi_str = input("Nhập tuổi: ")
tuoi = int(tuoi_str)
print(f"Bạn {tuoi} tuổi")
```

### 6.2 Validation cơ bản
```python
# Kiểm tra tên không rỗng
ten = input("Nhập tên: ").strip()
if ten:
    print(f"Xin chào {ten}")
else:
    print("Tên không được để trống!")

# Kiểm tra số điện thoại
sdt = input("Số điện thoại: ").strip()
if sdt.isdigit() and len(sdt) == 10:
    print("Số điện thoại hợp lệ")
else:
    print("Số điện thoại không hợp lệ")
```

## 7. Format String Nâng Cao

### 7.1 Định dạng số
```python
so = 3.14159
print(f"{so:.2f}")      # 3.14 (2 chữ số thập phân)
print(f"{so:.0f}")      # 3 (không thập phân)

so_nguyen = 1234567
print(f"{so_nguyen:,}") # 1,234,567 (phân cách hàng nghìn)
```

### 7.2 Căn lề
```python
text = "Python"
print(f"|{text:>10}|")  # |    Python| (căn phải)
print(f"|{text:<10}|")  # |Python    | (căn trái)
print(f"|{text:^10}|")  # |  Python  | (căn giữa)
print(f"|{text:*^10}|") # |**Python**| (căn giữa với ký tự *)
```

## 8. Ứng Dụng Thực Tế

### 8.1 Tạo username từ email
```python
email = "nguyen.van.an@gmail.com"
username = email.split("@")[0]
print(username)  # nguyen.van.an
```

### 8.2 Kiểm tra mật khẩu mạnh
```python
password = input("Nhập mật khẩu: ")

# Kiểm tra độ dài
if len(password) < 8:
    print("Mật khẩu phải có ít nhất 8 ký tự")
elif not any(c.isupper() for c in password):
    print("Mật khẩu phải có ít nhất 1 chữ hoa")
elif not any(c.islower() for c in password):
    print("Mật khẩu phải có ít nhất 1 chữ thường")
elif not any(c.isdigit() for c in password):
    print("Mật khẩu phải có ít nhất 1 số")
else:
    print("Mật khẩu mạnh!")
```

### 8.3 Tạo initials từ tên
```python
ho_ten = "Nguyen Van An"
words = ho_ten.split()
initials = "".join([word[0].upper() for word in words])
print(initials)  # NVA
```

## 9. Lỗi Thường Gặp

### 9.1 IndexError
```python
text = "Hello"
# print(text[10])  # IndexError: string index out of range

# Cách xử lý
if len(text) > 10:
    print(text[10])
else:
    print("String không đủ dài")
```

### 9.2 TypeError với số
```python
# Lỗi: cộng string với số
# ket_qua = "5" + 3  # TypeError

# Sửa lỗi
so_str = "5"
so = int(so_str)
ket_qua = so + 3
print(ket_qua)  # 8
```

## 10. Bài Tập Thực Hành

### Bài 1: Xử lý tên
```python
# Nhận tên từ user, chuẩn hóa thành Title Case
# Loại bỏ khoảng trắng thừa
```

### Bài 2: Đếm từ
```python
# Nhận một câu từ user
# Đếm số từ, số ký tự (không tính space)
```

### Bài 3: Tạo mật khẩu
```python
# Tạo mật khẩu từ tên + năm sinh
# VD: "Nguyen Van An" + 2005 → "NVA2005"
```

---

**Tip**: String trong Python là immutable (không thể thay đổi). Mọi method đều trả về string mới! 