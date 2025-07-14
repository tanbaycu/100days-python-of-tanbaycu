# Biến và Kiểu Dữ Liệu trong Python

## 1. Biến (Variables) là gì?

Biến là "hộp" để lưu trữ dữ liệu. Giống như bạn ghi tên lên cái hộp để biết bên trong có gì.

### Cách tạo biến:
```python
ten = "Nga"
tuoi = 20
diem = 8.5
```

## 2. Quy Tắc Đặt Tên Biến

### ✅ Đúng:
```python
ten_hoc_sinh = "An"
diem_toan = 9
so_dien_thoai = "0123456789"
```

### ❌ Sai:
```python
2ten = "An"        # Không bắt đầu bằng số
ten-hoc-sinh = "An" # Không dùng dấu gạch ngang
class = "10A"       # Không dùng từ khóa Python
```

### Quy tắc:
- Bắt đầu bằng chữ cái hoặc dấu gạch dưới (_)
- Chỉ chứa chữ cái, số và dấu gạch dưới
- Phân biệt chữ hoa/thường: `Ten` ≠ `ten`
- Không dùng từ khóa Python (`if`, `for`, `class`, ...)

## 3. Kiểu Dữ Liệu Cơ Bản

### 3.1 Số Nguyên (int)
```python
tuoi = 18
so_hoc_sinh = 30
nam_sinh = 2005
```

### 3.2 Số Thực (float)
```python
diem_tb = 8.5
chieu_cao = 1.65
can_nang = 55.2
```

### 3.3 Chuỗi (string/str)
```python
ho_ten = "Nguyen Van An"
lop = "10A1"
dia_chi = "Ha Noi"
```

### 3.4 Boolean (bool)
```python
la_hoc_sinh = True
da_lam_bai = False
```

## 4. Kiểm Tra Kiểu Dữ Liệu

```python
ten = "An"
print(type(ten))     # <class 'str'>

tuoi = 18
print(type(tuoi))    # <class 'int'>

diem = 8.5
print(type(diem))    # <class 'float'>

hoc_gioi = True
print(type(hoc_gioi)) # <class 'bool'>
```

## 5. Gán Lại Giá Trị

```python
# Tạo biến
ten = "An"
print(ten)  # An

# Gán lại
ten = "Binh"
print(ten)  # Binh

# Có thể đổi kiểu
ten = 123
print(ten)  # 123
```

## 6. Gán Nhiều Biến Cùng Lúc

```python
# Cách 1: Gán cùng giá trị
a = b = c = 0

# Cách 2: Gán khác giá trị
ten, tuoi, diem = "An", 18, 8.5
print(ten)   # An
print(tuoi)  # 18
print(diem)  # 8.5
```

## 7. Chuyển Đổi Kiểu Dữ Liệu

### 7.1 Chuyển sang int:
```python
# Từ string
tuoi_str = "18"
tuoi_int = int(tuoi_str)  # 18

# Từ float
diem_float = 8.7
diem_int = int(diem_float)  # 8 (cắt phần thập phân)
```

### 7.2 Chuyển sang float:
```python
# Từ string
diem_str = "8.5"
diem_float = float(diem_str)  # 8.5

# Từ int
tuoi_int = 18
tuoi_float = float(tuoi_int)  # 18.0
```

### 7.3 Chuyển sang string:
```python
# Từ int
tuoi = 18
tuoi_str = str(tuoi)  # "18"

# Từ float
diem = 8.5
diem_str = str(diem)  # "8.5"
```

## 8. Lỗi Thường Gặp

### NameError:
```python
print(ten)  # NameError: name 'ten' is not defined
# Lỗi: chưa tạo biến 'ten'
```

### ValueError:
```python
tuoi = int("abc")  # ValueError: invalid literal
# Lỗi: không thể chuyển "abc" thành số
```

### TypeError:
```python
ket_qua = "5" + 3  # TypeError: can't concatenate str and int
# Lỗi: không thể cộng string với số
```

## 9. Best Practices

### Đặt tên có nghĩa:
```python
# Tốt
so_hoc_sinh = 30
diem_toan = 9
ten_lop = "10A"

# Không tốt
a = 30
b = 9
c = "10A"
```

### Sử dụng snake_case:
```python
# Tốt
ten_hoc_sinh = "An"
diem_trung_binh = 8.5

# Không nên
TenHocSinh = "An"
diemTrungBinh = 8.5
```

### Nhóm biến liên quan:
```python
# Thông tin học sinh
ten_hs = "An"
tuoi_hs = 18
lop_hs = "10A"

# Điểm số
diem_toan = 9
diem_ly = 8
diem_hoa = 7
```

## 10. Bài Tập Thực Hành

### Bài 1: Tạo biến cơ bản
```python
# Tạo các biến sau:
# - Tên bạn
# - Tuổi
# - Điểm trung bình
# - Có phải học sinh giỏi không (boolean)
```

### Bài 2: Chuyển đổi kiểu
```python
# Cho biến: tuoi_str = "18"
# Chuyển thành số nguyên và cộng thêm 2
```

### Bài 3: Fix lỗi
```python
# Code có lỗi, hãy sửa:
2name = "An"
tuoi = "18"
ket_qua = tuoi + 2
```

---

**Tip**: Luôn đặt tên biến có nghĩa để code dễ đọc và bảo trì! 