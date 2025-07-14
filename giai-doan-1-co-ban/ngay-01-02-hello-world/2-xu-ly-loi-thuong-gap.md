# Xử Lý Lỗi Thường Gặp - Ngày 1-2

## Mục Tiêu
- Hiểu các loại lỗi phổ biến trong Python
- Biết cách đọc và hiểu error messages
- Học cách debug và sửa lỗi
- Tránh những lỗi cơ bản

---

## Loại Lỗi Trong Python

### 1. Syntax Error (Lỗi Cú Pháp)
**Nguyên nhân**: Code viết sai cú pháp Python

#### Lỗi 1.1: Thiếu Dấu Nháy
```python
# ❌ Sai:
print("Hello World!)  # Thiếu dấu nháy cuối

# ✅ Đúng:
print("Hello World!")
```

**Error Message**:
```
SyntaxError: EOL while scanning string literal
```

#### Lỗi 1.2: Thiếu Dấu Ngoặc
```python
# ❌ Sai:
print("Hello World"  # Thiếu dấu )

# ✅ Đúng:
print("Hello World")
```

**Error Message**:
```
SyntaxError: unexpected EOF while parsing
```

#### Lỗi 1.3: Thụt Đầu Dòng Sai
```python
# ❌ Sai:
if True:
print("Hello")  # Thiếu thụt đầu dòng

# ✅ Đúng:
if True:
    print("Hello")  # 4 spaces thụt đầu dòng
```

**Error Message**:
```
IndentationError: expected an indented block
```

### 2. Name Error (Lỗi Tên Biến)
**Nguyên nhân**: Sử dụng biến chưa được định nghĩa

#### Lỗi 2.1: Biến Chưa Định Nghĩa
```python
# ❌ Sai:
print(ten)  # Biến 'ten' chưa được tạo

# ✅ Đúng:
ten = "Minh"
print(ten)
```

**Error Message**:
```
NameError: name 'ten' is not defined
```

#### Lỗi 2.2: Viết Sai Tên Biến
```python
# ❌ Sai:
ho_ten = "Nguyễn Văn A"
print(hoten)  # Viết sai tên biến (thiếu dấu _)

# ✅ Đúng:
ho_ten = "Nguyễn Văn A"
print(ho_ten)
```

### 3. Type Error (Lỗi Kiểu Dữ Liệu)
**Nguyên nhân**: Sử dụng sai kiểu dữ liệu

#### Lỗi 3.1: Cộng String với Số
```python
# ❌ Sai:
tuoi = input("Tuổi: ")  # input() trả về string
nam_sau = tuoi + 1      # Không thể cộng string với số

# ✅ Đúng:
tuoi = int(input("Tuổi: "))  # Chuyển sang int
nam_sau = tuoi + 1
```

**Error Message**:
```
TypeError: can only concatenate str (not "int") to str
```

#### Lỗi 3.2: Chia Cho 0
```python
# ❌ Sai:
ket_qua = 10 / 0  # Không thể chia cho 0

# ✅ Đúng:
if so_chia != 0:
    ket_qua = 10 / so_chia
else:
    print("Không thể chia cho 0!")
```

**Error Message**:
```
ZeroDivisionError: division by zero
```

### 4. Value Error (Lỗi Giá Trị)
**Nguyên nhân**: Chuyển đổi kiểu dữ liệu không hợp lệ

#### Lỗi 4.1: Chuyển String Thành Số
```python
# ❌ Sai:
tuoi = int("hai mươi")  # Không thể chuyển text thành số

# ✅ Đúng:
tuoi_str = input("Tuổi: ")
try:
    tuoi = int(tuoi_str)
    print(f"Bạn {tuoi} tuổi")
except ValueError:
    print("Vui lòng nhập số!")
```

**Error Message**:
```
ValueError: invalid literal for int() with base 10: 'hai mươi'
```

---

## Cách Đọc Error Messages

### Cấu Trúc Error Message
```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    print(ten)
NameError: name 'ten' is not defined
```

**Giải thích**:
1. **File "test.py"**: Lỗi xảy ra trong file test.py
2. **line 3**: Lỗi ở dòng số 3
3. **print(ten)**: Đoạn code gây ra lỗi
4. **NameError**: Loại lỗi
5. **name 'ten' is not defined**: Mô tả chi tiết lỗi

### Ví Dụ Thực Tế
```python
# File: loi_demo.py
print("Bắt đầu chương trình")
ten = input("Tên: ")
print(f"Xin chào {tem}")  # Lỗi: viết sai 'ten' thành 'tem'
```

**Error Output**:
```
Bắt đầu chương trình
Tên: Minh
Traceback (most recent call last):
  File "loi_demo.py", line 3, in <module>
    print(f"Xin chào {tem}")
NameError: name 'tem' is not defined
```

---

## Kỹ Thuật Debug

### 1. Print Debugging
**Thêm print() để kiểm tra giá trị biến**

```python
# Ví dụ: Debug tính toán
so_a = input("Số a: ")
so_b = input("Số b: ")

print(f"DEBUG: so_a = {so_a}, type = {type(so_a)}")  # Debug
print(f"DEBUG: so_b = {so_b}, type = {type(so_b)}")  # Debug

# Chuyển đổi
so_a = int(so_a)
so_b = int(so_b)

print(f"DEBUG: sau chuyển đổi so_a = {so_a}, so_b = {so_b}")  # Debug

ket_qua = so_a + so_b
print(f"Kết quả: {ket_qua}")
```

### 2. Comment Code
**Tạm thời tắt một phần code để tìm lỗi**

```python
# Ví dụ: Tìm lỗi trong đoạn code dài
ten = input("Tên: ")
tuoi = input("Tuổi: ")

print(f"Tên: {ten}")

# Tạm thời comment để test
# tuoi_int = int(tuoi)
# nam_sinh = 2024 - tuoi_int
# print(f"Năm sinh: {nam_sinh}")

print("Code chạy đến đây")
```

### 3. Sử Dụng Try-Except
**Bắt lỗi và xử lý**

```python
# Ví dụ: Xử lý lỗi nhập liệu
def nhap_so_an_toan():
    while True:
        try:
            so = int(input("Nhập một số: "))
            return so
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập số nguyên!")
            print("Thử lại...")

# Sử dụng
tuoi = nhap_so_an_toan()
print(f"Tuổi của bạn: {tuoi}")
```

---

## Lỗi Thường Gặp Ở Người Mới

### 1. Quên Chuyển Đổi Kiểu
```python
# ❌ Sai:
a = input("Số a: ")
b = input("Số b: ")
tong = a + b  # Sẽ nối chuỗi, không cộng số
print(f"Tổng: {tong}")

# Kết quả: Nếu nhập 5 và 3 → "53" (không phải 8)

# ✅ Đúng:
a = int(input("Số a: "))
b = int(input("Số b: "))
tong = a + b
print(f"Tổng: {tong}")
```

### 2. Đặt Tên Biến Sai Quy Tắc
```python
# ❌ Sai:
2so = 10           # Không được bắt đầu bằng số
class = "10A"      # 'class' là từ khóa Python
số tuổi = 20       # Không được có dấu cách

# ✅ Đúng:
so_thu_hai = 10
lop_hoc = "10A"
so_tuoi = 20
```

### 3. Nhầm Lẫn Về Dấu Nháy
```python
# ❌ Sai:
print('Tôi tên "Minh"')  # Nhầm lẫn dấu nháy

# ✅ Đúng:
print("Tôi tên \"Minh\"")  # Escape quote
# Hoặc:
print('Tôi tên "Minh"')   # Dùng nháy đơn bên ngoài
```

### 4. Quên Import Module
```python
# ❌ Sai:
import math
ket_qua = sqrt(16)  # Lỗi: phải dùng math.sqrt()

# ✅ Đúng:
import math
ket_qua = math.sqrt(16)
```

---

## Tools Debug Trong VS Code

### 1. Sử Dụng Debugger
1. **Đặt breakpoint**: Click vào số dòng (xuất hiện chấm đỏ)
2. **Chạy debug**: `F5` hoặc Run → Start Debugging
3. **Step over**: `F10` (chạy từng dòng)
4. **Watch variables**: Xem giá trị biến trong Debug panel

### 2. Python Interactive Window
1. **Ctrl+Shift+P** → "Python: Start REPL"
2. **Test code từng dòng**:
```python
>>> ten = "Minh"
>>> print(ten)
Minh
>>> type(ten)
<class 'str'>
```

### 3. Pylint (Kiểm Tra Code)
- **Cài đặt**: `pip install pylint`
- **Chạy**: `pylint file.py`
- **Hiển thị lỗi và warnings trong VS Code**

---

## Checklist Debug

### Trước Khi Chạy Code
- [ ] Kiểm tra tất cả dấu nháy đóng mở đúng
- [ ] Kiểm tra tất cả dấu ngoặc đóng mở đúng
- [ ] Kiểm tra thụt đầu dòng đồng nhất
- [ ] Kiểm tra tên biến viết đúng
- [ ] Kiểm tra chuyển đổi kiểu dữ liệu

### Khi Gặp Lỗi
1. **Đọc error message cẩn thận**
2. **Xác định dòng bị lỗi**
3. **Kiểm tra syntax ở dòng đó**
4. **Thêm print() để debug**
5. **Google error message nếu cần**

### Testing Code
```python
# Template test cơ bản
def test_code():
    print("=== TEST BẮT ĐẦU ===")
    
    # Test case 1
    print("Test 1: Input bình thường")
    # Code test...
    
    # Test case 2
    print("Test 2: Input đặc biệt")
    # Code test...
    
    print("=== TEST HOÀN THÀNH ===")

# Chạy test
test_code()
```

---

## Bài Tập Debug

### Bài 1: Tìm và Sửa Lỗi
```python
# Code có lỗi - hãy tìm và sửa:
print("Chào mừng đến chương trình)
ten = input("Tên của bạn: "
print(f"Xin chào {tem}!")
tuoi = input("Tuổi: ")
nam_sinh = 2024 - tuoi
print(f"Bạn sinh năm {nam_sinh}")
```

### Bài 2: Debug Tương Tác
```python
# Chạy code này và sửa lỗi xuất hiện:
def tinh_bmi():
    print("=== TÍNH CHỈ SỐ BMI ===")
    can_nang = input("Cân nặng (kg): ")
    chieu_cao = input("Chiều cao (m): ")
    
    bmi = can_nang / (chieu_cao ** 2)
    print(f"BMI của bạn: {bmi}")

tinh_bmi()
```

### Bài 3: Error Handling
```python
# Viết code xử lý lỗi cho chương trình chia số:
def chia_so():
    try:
        # Code của bạn ở đây
        pass
    except:
        # Xử lý lỗi ở đây
        pass

chia_so()
```

---

## Tips Tránh Lỗi

### 1. Coding Best Practices
- **Đặt tên biến có ý nghĩa**: `ho_ten` thay vì `x`
- **Comment giải thích**: `# Tính tuổi từ năm sinh`
- **Chia nhỏ function**: Mỗi function làm 1 việc
- **Test thường xuyên**: Chạy code sau mỗi vài dòng

### 2. Environment Setup
- **Sử dụng Virtual Environment**
- **Cài đặt linter**: pylint, flake8
- **Git để backup code**
- **Đọc documentation**

### 3. Mindset Debug
- **Bình tĩnh**: Lỗi là bình thường
- **Tỉ mỉ**: Đọc error message cẩn thận  
- **Kiên nhẫn**: Debug từng bước
- **Học hỏi**: Mỗi lỗi là bài học

**Nhớ**: "Debugging is twice as hard as writing the code. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it." - Brian Kernighan

Hoàn thành phần này, bạn sẽ tự tin hơn khi gặp lỗi! 🐛➡️✅ 