# Phép Toán Số Học trong Python

## 1. Các Phép Toán Cơ Bản

### 1.1 Phép Cộng (+)
```python
a = 5
b = 3
ket_qua = a + b
print(ket_qua)  # 8

# Với số thực
diem1 = 8.5
diem2 = 7.2
tong_diem = diem1 + diem2
print(tong_diem)  # 15.7
```

### 1.2 Phép Trừ (-)
```python
a = 10
b = 4
hieu = a - b
print(hieu)  # 6

# Số âm
tuoi_hien_tai = 2024
nam_sinh = 2005
tuoi = tuoi_hien_tai - nam_sinh
print(tuoi)  # 19
```

### 1.3 Phép Nhân (*)
```python
a = 6
b = 7
tich = a * b
print(tich)  # 42

# Với số thực
chieu_dai = 5.5
chieu_rong = 3.2
dien_tich = chieu_dai * chieu_rong
print(dien_tich)  # 17.6
```

### 1.4 Phép Chia (/)
```python
a = 15
b = 3
thuong = a / b
print(thuong)  # 5.0 (luôn trả về float)

# Chia với số thực
tong_tien = 100000
so_nguoi = 3
moi_nguoi = tong_tien / so_nguoi
print(moi_nguoi)  # 33333.333333333336
```

## 2. Phép Toán Nâng Cao

### 2.1 Chia Lấy Phần Nguyên (//)
```python
a = 17
b = 5
ket_qua = a // b
print(ket_qua)  # 3

# Với số âm
a = -17
b = 5
ket_qua = a // b
print(ket_qua)  # -4
```

### 2.2 Chia Lấy Dư (%)
```python
a = 17
b = 5
du = a % b
print(du)  # 2

# Ứng dụng: kiểm tra số chẵn/lẻ
so = 7
if so % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")  # In ra "Số lẻ"
```

### 2.3 Lũy Thừa (**)
```python
a = 2
b = 3
luy_thua = a ** b
print(luy_thua)  # 8 (2^3)

# Căn bậc hai
so = 16
can_bac_hai = so ** 0.5
print(can_bac_hai)  # 4.0
```

## 3. Thứ Tự Ưu Tiên Phép Toán

Python tuân theo quy tắc toán học:
1. **Ngoặc đơn ()** - cao nhất
2. **Lũy thừa \*\***
3. **Nhân \*, Chia /, Chia nguyên //, Chia dư %**
4. **Cộng +, Trừ -** - thấp nhất

```python
# Ví dụ 1
ket_qua = 2 + 3 * 4
print(ket_qua)  # 14 (không phải 20)

# Ví dụ 2
ket_qua = (2 + 3) * 4
print(ket_qua)  # 20

# Ví dụ 3
ket_qua = 2 ** 3 + 1
print(ket_qua)  # 9 (2^3 + 1)

# Ví dụ 4
ket_qua = 20 / 4 * 2
print(ket_qua)  # 10.0 (từ trái qua phải)
```

## 4. Phép Toán Với Biến

### 4.1 Cập nhật giá trị biến
```python
diem = 8
diem = diem + 1  # diem = 9

# Cách viết ngắn gọn
diem += 1  # tương đương diem = diem + 1
print(diem)  # 10
```

### 4.2 Các toán tử gán
```python
a = 10

a += 5   # a = a + 5  → a = 15
a -= 3   # a = a - 3  → a = 12
a *= 2   # a = a * 2  → a = 24
a /= 4   # a = a / 4  → a = 6.0
a //= 2  # a = a // 2 → a = 3.0
a %= 2   # a = a % 2  → a = 1.0
a **= 3  # a = a ** 3 → a = 1.0
```

## 5. Hàm Toán Học Cơ Bản

### 5.1 Hàm có sẵn
```python
# Giá trị tuyệt đối
so = -5
gia_tri_tuyet_doi = abs(so)
print(gia_tri_tuyet_doi)  # 5

# Làm tròn
so = 8.7
lam_tron = round(so)
print(lam_tron)  # 9

# Làm tròn với số chữ số
so = 8.765
lam_tron_2_chu_so = round(so, 2)
print(lam_tron_2_chu_so)  # 8.77

# Min, Max
a, b, c = 5, 3, 8
so_nho_nhat = min(a, b, c)
so_lon_nhat = max(a, b, c)
print(so_nho_nhat)  # 3
print(so_lon_nhat)  # 8
```

### 5.2 Thư viện math
```python
import math

# Hằng số
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# Hàm lượng giác
goc = 90
sin_90 = math.sin(math.radians(goc))
print(sin_90)  # 1.0

# Logarit
so = 8
log_2 = math.log2(so)
print(log_2)  # 3.0

# Căn bậc hai
so = 16
can_bac_hai = math.sqrt(so)
print(can_bac_hai)  # 4.0
```

## 6. Ứng Dụng Thực Tế

### 6.1 Tính điểm trung bình
```python
diem_toan = 8.5
diem_ly = 7.0
diem_hoa = 9.0

diem_tb = (diem_toan + diem_ly + diem_hoa) / 3
print(f"Điểm trung bình: {diem_tb:.2f}")  # 8.17
```

### 6.2 Tính tiền và tax
```python
gia_goc = 100000
thue = 10  # 10%

tien_thue = gia_goc * thue / 100
tong_tien = gia_goc + tien_thue

print(f"Giá gốc: {gia_goc}")
print(f"Thuế: {tien_thue}")
print(f"Tổng tiền: {tong_tien}")
```

### 6.3 Chuyển đổi đơn vị
```python
# Chuyển độ C sang độ F
do_c = 25
do_f = do_c * 9/5 + 32
print(f"{do_c}°C = {do_f}°F")  # 25°C = 77.0°F

# Chuyển giây sang phút
tong_giay = 125
phut = tong_giay // 60
giay = tong_giay % 60
print(f"{tong_giay} giây = {phut} phút {giay} giây")
```

## 7. Lỗi Thường Gặp

### 7.1 ZeroDivisionError
```python
# Lỗi chia cho 0
a = 10
b = 0
# ket_qua = a / b  # ZeroDivisionError

# Cách xử lý
if b != 0:
    ket_qua = a / b
    print(ket_qua)
else:
    print("Không thể chia cho 0!")
```

### 7.2 OverflowError
```python
# Số quá lớn
# so_lon = 10 ** 1000  # Có thể gây lỗi với float
# Với int thì Python xử lý được số rất lớn
so_lon = 10 ** 100
print(len(str(so_lon)))  # 101 chữ số
```

### 7.3 TypeError với kiểu dữ liệu
```python
# Lỗi khi phép toán với kiểu sai
# ket_qua = "5" + 3  # TypeError

# Sửa lỗi
so_str = "5"
so_int = int(so_str)
ket_qua = so_int + 3
print(ket_qua)  # 8
```

## 8. Bài Tập Thực Hành

### Bài 1: Máy tính cơ bản
```python
# Tạo chương trình nhận 2 số từ user
# Thực hiện tất cả phép toán và hiển thị kết quả
```

### Bài 2: Tính BMI
```python
# BMI = cân nặng / (chiều cao^2)
# Nhận input từ user và tính BMI
```

### Bài 3: Tính tiền điện
```python
# Bậc 1: 0-50 kWh = 1,678 đ/kWh
# Bậc 2: 51-100 kWh = 1,734 đ/kWh
# Bậc 3: >100 kWh = 2,014 đ/kWh
```

---

**Lưu ý**: Luôn kiểm tra input để tránh lỗi chia cho 0 và chuyển đổi kiểu dữ liệu! 