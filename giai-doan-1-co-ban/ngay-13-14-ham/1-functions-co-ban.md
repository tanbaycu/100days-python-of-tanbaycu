# Lý Thuyết 1: Functions Cơ Bản

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Hiểu rõ khái niệm và tầm quan trọng của functions
- Nắm vững cú pháp khai báo và sử dụng functions
- Biết cách viết functions hiệu quả và clean code
- Áp dụng functions vào các bài toán thực tế

## 1. Functions Là Gì?

### Khái Niệm
Function (hàm) là một khối code được đặt tên, có thể được gọi nhiều lần trong chương trình. Functions giúp:
- Tái sử dụng code
- Tổ chức code rõ ràng
- Dễ bảo trì và debug
- Chia nhỏ bài toán phức tạp

### Tại Sao Cần Functions?

**Không có Functions:**
```python
# Tính diện tích hình chữ nhật 1
dai_1 = 10
rong_1 = 5
dien_tich_1 = dai_1 * rong_1
print(f"Diện tích 1: {dien_tich_1}")

# Tính diện tích hình chữ nhật 2
dai_2 = 8
rong_2 = 6
dien_tich_2 = dai_2 * rong_2
print(f"Diện tích 2: {dien_tich_2}")

# Tính diện tích hình chữ nhật 3
dai_3 = 12
rong_3 = 4
dien_tich_3 = dai_3 * rong_3
print(f"Diện tích 3: {dien_tich_3}")
```

**Có Functions:**
```python
def tinh_dien_tich(dai, rong):
    """Tính diện tích hình chữ nhật"""
    return dai * rong

# Sử dụng
dien_tich_1 = tinh_dien_tich(10, 5)
dien_tich_2 = tinh_dien_tich(8, 6)
dien_tich_3 = tinh_dien_tich(12, 4)

print(f"Diện tích 1: {dien_tich_1}")
print(f"Diện tích 2: {dien_tich_2}")
print(f"Diện tích 3: {dien_tich_3}")
```

## 2. Cú Pháp Function

### Cú Pháp Cơ Bản
```python
def ten_function(parameter1, parameter2, ...):
    """Docstring - mô tả function"""
    # Thân function
    return gia_tri_tra_ve  # Tùy chọn
```

### Ví Dụ Cụ Thể
```python
def chao_hoi(ten):
    """Chào hỏi một người"""
    return f"Xin chào {ten}!"

def cong_hai_so(a, b):
    """Cộng hai số"""
    ket_qua = a + b
    return ket_qua

def in_thong_tin():
    """In thông tin không có return"""
    print("Đây là một function không có return")
```

## 3. Các Loại Functions

### 3.1 Function Không Có Return
```python
def in_menu():
    """In menu lựa chọn"""
    print("1. Thêm sản phẩm")
    print("2. Xóa sản phẩm")
    print("3. Thoát")

# Sử dụng
in_menu()
```

### 3.2 Function Có Return
```python
def tinh_bmi(can_nang, chieu_cao):
    """Tính chỉ số BMI"""
    bmi = can_nang / (chieu_cao ** 2)
    return bmi

def phan_loai_bmi(bmi):
    """Phân loại BMI"""
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"

# Sử dụng
bmi = tinh_bmi(70, 1.75)
phan_loai = phan_loai_bmi(bmi)
print(f"BMI: {bmi:.2f} - {phan_loai}")
```

### 3.3 Function Return Nhiều Giá Trị
```python
def tinh_toan_co_ban(a, b):
    """Thực hiện các phép tính cơ bản"""
    cong = a + b
    tru = a - b
    nhan = a * b
    chia = a / b if b != 0 else None
    return cong, tru, nhan, chia

# Sử dụng
ket_qua_cong, ket_qua_tru, ket_qua_nhan, ket_qua_chia = tinh_toan_co_ban(10, 5)
print(f"Cộng: {ket_qua_cong}")
print(f"Trừ: {ket_qua_tru}")
print(f"Nhân: {ket_qua_nhan}")
print(f"Chia: {ket_qua_chia}")
```

## 4. Scope (Phạm Vi) Biến

### 4.1 Local Scope
```python
def test_local():
    x = 10  # Biến local
    print(f"Trong function: {x}")

test_local()
# print(x)  # Lỗi! x không tồn tại ngoài function
```

### 4.2 Global Scope
```python
y = 20  # Biến global

def test_global():
    print(f"Trong function: {y}")  # Có thể đọc biến global

test_global()
print(f"Ngoài function: {y}")
```

### 4.3 Thay Đổi Biến Global
```python
count = 0  # Biến global

def tang_count():
    global count
    count += 1
    print(f"Count hiện tại: {count}")

tang_count()  # Count hiện tại: 1
tang_count()  # Count hiện tại: 2
```

## 5. Docstring - Tài Liệu Hóa Function

### Cách Viết Docstring
```python
def tinh_lai_suat(tien_goc, lai_suat, thoi_gian):
    """
    Tính lãi suất đơn giản
    
    Args:
        tien_goc (float): Số tiền gốc
        lai_suat (float): Lãi suất theo năm (%)
        thoi_gian (int): Thời gian (năm)
    
    Returns:
        float: Số tiền lãi
    
    Example:
        >>> tinh_lai_suat(1000000, 5, 2)
        100000.0
    """
    lai = tien_goc * (lai_suat / 100) * thoi_gian
    return lai

# Xem docstring
print(tinh_lai_suat.__doc__)
help(tinh_lai_suat)
```

## 6. Best Practices

### 6.1 Đặt Tên Function
```python
# Tốt
def tinh_dien_tich_hinh_tron(ban_kinh):
    return 3.14159 * ban_kinh ** 2

def kiem_tra_so_chan(so):
    return so % 2 == 0

# Không tốt
def func1(x):
    return 3.14159 * x ** 2

def f(n):
    return n % 2 == 0
```

### 6.2 Function Chỉ Làm Một Việc
```python
# Tốt - Mỗi function làm một việc
def doc_file(ten_file):
    """Đọc nội dung file"""
    with open(ten_file, 'r', encoding='utf-8') as file:
        return file.read()

def xu_ly_du_lieu(du_lieu):
    """Xử lý dữ liệu"""
    return du_lieu.strip().upper()

def ghi_file(ten_file, noi_dung):
    """Ghi nội dung vào file"""
    with open(ten_file, 'w', encoding='utf-8') as file:
        file.write(noi_dung)

# Không tốt - Function làm quá nhiều việc
def xu_ly_file(ten_file_doc, ten_file_ghi):
    """Function làm quá nhiều việc"""
    # Đọc file
    with open(ten_file_doc, 'r', encoding='utf-8') as file:
        du_lieu = file.read()
    
    # Xử lý dữ liệu
    du_lieu = du_lieu.strip().upper()
    
    # Ghi file
    with open(ten_file_ghi, 'w', encoding='utf-8') as file:
        file.write(du_lieu)
```

## 7. Ví Dụ Thực Tế

### 7.1 Hệ Thống Quản Lý Lương
```python
def tinh_luong_co_ban(luong_co_ban, so_ngay_lam):
    """Tính lương cơ bản"""
    return luong_co_ban * so_ngay_lam

def tinh_thuong(luong_co_ban, hieu_suat):
    """Tính thưởng theo hiệu suất"""
    if hieu_suat >= 90:
        return luong_co_ban * 0.2
    elif hieu_suat >= 80:
        return luong_co_ban * 0.1
    elif hieu_suat >= 70:
        return luong_co_ban * 0.05
    else:
        return 0

def tinh_thue(tong_luong):
    """Tính thuế thu nhập"""
    if tong_luong <= 11000000:
        return 0
    elif tong_luong <= 25000000:
        return (tong_luong - 11000000) * 0.05
    else:
        return 700000 + (tong_luong - 25000000) * 0.1

def tinh_luong_thuc_linh(luong_co_ban, so_ngay_lam, hieu_suat):
    """Tính lương thực lĩnh"""
    luong_cb = tinh_luong_co_ban(luong_co_ban, so_ngay_lam)
    thuong = tinh_thuong(luong_co_ban, hieu_suat)
    tong_luong = luong_cb + thuong
    thue = tinh_thue(tong_luong)
    thuc_linh = tong_luong - thue
    
    return {
        'luong_co_ban': luong_cb,
        'thuong': thuong,
        'tong_luong': tong_luong,
        'thue': thue,
        'thuc_linh': thuc_linh
    }

# Sử dụng
ket_qua = tinh_luong_thuc_linh(1000000, 22, 85)
print(f"Lương cơ bản: {ket_qua['luong_co_ban']:,}")
print(f"Thưởng: {ket_qua['thuong']:,}")
print(f"Tổng lương: {ket_qua['tong_luong']:,}")
print(f"Thuế: {ket_qua['thue']:,}")
print(f"Thực lĩnh: {ket_qua['thuc_linh']:,}")
```

### 7.2 Hệ Thống Phân Tích Điểm Học Sinh
```python
def tinh_diem_trung_binh(diem_list):
    """Tính điểm trung bình"""
    if not diem_list:
        return 0
    return sum(diem_list) / len(diem_list)

def xep_loai_hoc_luc(diem_tb):
    """Xếp loại học lực"""
    if diem_tb >= 9:
        return "Xuất sắc"
    elif diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def kiem_tra_len_lop(diem_tb, diem_toan, diem_van):
    """Kiểm tra điều kiện lên lớp"""
    if diem_tb >= 5 and diem_toan >= 4 and diem_van >= 4:
        return True
    return False

def phan_tich_hoc_sinh(ten, diem_toan, diem_van, diem_anh, diem_ly, diem_hoa):
    """Phân tích toàn diện học sinh"""
    diem_list = [diem_toan, diem_van, diem_anh, diem_ly, diem_hoa]
    diem_tb = tinh_diem_trung_binh(diem_list)
    hoc_luc = xep_loai_hoc_luc(diem_tb)
    len_lop = kiem_tra_len_lop(diem_tb, diem_toan, diem_van)
    
    return {
        'ten': ten,
        'diem_trung_binh': diem_tb,
        'hoc_luc': hoc_luc,
        'len_lop': len_lop,
        'diem_chi_tiet': {
            'toan': diem_toan,
            'van': diem_van,
            'anh': diem_anh,
            'ly': diem_ly,
            'hoa': diem_hoa
        }
    }

# Sử dụng
ket_qua = phan_tich_hoc_sinh("Nguyễn Văn A", 8.5, 7.0, 6.5, 8.0, 7.5)
print(f"Học sinh: {ket_qua['ten']}")
print(f"Điểm trung bình: {ket_qua['diem_trung_binh']:.2f}")
print(f"Học lực: {ket_qua['hoc_luc']}")
print(f"Lên lớp: {'Có' if ket_qua['len_lop'] else 'Không'}")
```

## 8. Lỗi Thường Gặp

### 8.1 Quên Return
```python
# Sai
def tinh_tong(a, b):
    ket_qua = a + b
    # Quên return

# Đúng
def tinh_tong(a, b):
    ket_qua = a + b
    return ket_qua
```

### 8.2 Thay Đổi Biến Global Không Đúng Cách
```python
# Sai
count = 0
def tang_count():
    count = count + 1  # Lỗi UnboundLocalError

# Đúng
count = 0
def tang_count():
    global count
    count = count + 1
```

### 8.3 Đặt Tên Trùng Với Built-in Functions
```python
# Sai
def len(my_list):
    return "Độ dài custom"

# Đúng
def tinh_do_dai(my_list):
    return len(my_list)
```

## 9. Bài Tập Thực Hành

### Bài 1: Máy Tính Đơn Giản
```python
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b

def may_tinh():
    """Máy tính đơn giản"""
    print("Chọn phép tính:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    
    lua_chon = input("Nhập lựa chọn (1-4): ")
    
    if lua_chon in ['1', '2', '3', '4']:
        so_1 = float(input("Nhập số thứ nhất: "))
        so_2 = float(input("Nhập số thứ hai: "))
        
        if lua_chon == '1':
            print(f"Kết quả: {cong(so_1, so_2)}")
        elif lua_chon == '2':
            print(f"Kết quả: {tru(so_1, so_2)}")
        elif lua_chon == '3':
            print(f"Kết quả: {nhan(so_1, so_2)}")
        elif lua_chon == '4':
            print(f"Kết quả: {chia(so_1, so_2)}")
    else:
        print("Lựa chọn không hợp lệ!")

# Chạy máy tính
may_tinh()
```

## 10. Tổng Kết

Functions là nền tảng quan trọng trong lập trình Python. Chúng giúp:
- Tái sử dụng code hiệu quả
- Tổ chức chương trình rõ ràng
- Dễ bảo trì và phát triển
- Chia nhỏ bài toán phức tạp

### Điểm Quan Trọng Cần Nhớ:
1. **Đặt tên function rõ ràng** - Tên phải mô tả chức năng
2. **Mỗi function làm một việc** - Nguyên tắc Single Responsibility
3. **Sử dụng docstring** - Tài liệu hóa code
4. **Xử lý lỗi** - Kiểm tra input và edge cases
5. **Return có ý nghĩa** - Trả về giá trị phù hợp

### Lộ Trình Học Tiếp:
- **Tiếp theo**: Parameters & Arguments chi tiết
- **Nâng cao**: Lambda functions, Decorators
- **Thực hành**: Các dự án lớn sử dụng functions 