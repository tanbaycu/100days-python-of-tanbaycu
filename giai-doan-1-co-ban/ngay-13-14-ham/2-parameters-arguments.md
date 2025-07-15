# Lý Thuyết 2: Parameters & Arguments

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Phân biệt được Parameters và Arguments
- Nắm vững các loại parameters trong Python
- Sử dụng thành thạo *args và **kwargs
- Xử lý các trường hợp đặc biệt và edge cases

## 1. Parameters vs Arguments

### Khái Niệm
- **Parameter**: Biến trong định nghĩa function
- **Argument**: Giá trị thực tế truyền vào khi gọi function

```python
def chao_hoi(ten):  # 'ten' là parameter
    return f"Xin chào {ten}!"

# Gọi function
ket_qua = chao_hoi("Nam")  # "Nam" là argument
print(ket_qua)
```

## 2. Các Loại Parameters

### 2.1 Positional Parameters
```python
def gioi_thieu(ten, tuoi, que_quan):
    return f"Tôi là {ten}, {tuoi} tuổi, quê {que_quan}"

# Thứ tự arguments phải đúng
print(gioi_thieu("An", 25, "Hà Nội"))
print(gioi_thieu("Bình", 30, "Hồ Chí Minh"))
```

### 2.2 Keyword Arguments
```python
def gioi_thieu(ten, tuoi, que_quan):
    return f"Tôi là {ten}, {tuoi} tuổi, quê {que_quan}"

# Có thể thay đổi thứ tự với keyword arguments
print(gioi_thieu(que_quan="Đà Nẵng", ten="Cường", tuoi=28))
print(gioi_thieu(tuoi=35, ten="Dung", que_quan="Cần Thơ"))

# Kết hợp positional và keyword
print(gioi_thieu("Hoa", tuoi=22, que_quan="Huế"))
```

### 2.3 Default Parameters
```python
def dang_ky_khoa_hoc(ten, khoa_hoc, hoc_phi=1000000, hinh_thuc="online"):
    return {
        'ten': ten,
        'khoa_hoc': khoa_hoc,
        'hoc_phi': hoc_phi,
        'hinh_thuc': hinh_thuc
    }

# Sử dụng giá trị mặc định
print(dang_ky_khoa_hoc("An", "Python"))

# Ghi đè giá trị mặc định
print(dang_ky_khoa_hoc("Bình", "Java", 1500000))
print(dang_ky_khoa_hoc("Cường", "React", hinh_thuc="offline"))
print(dang_ky_khoa_hoc("Dung", "Django", 2000000, "offline"))
```

### 2.4 Lưu Ý Với Mutable Default Values
```python
# Sai - Nguy hiểm với mutable objects
def them_item(item, danh_sach=[]):
    danh_sach.append(item)
    return danh_sach

# Vấn đề: danh_sach được chia sẻ giữa các lần gọi
print(them_item("táo"))      # ['táo']
print(them_item("cam"))      # ['táo', 'cam'] - Không mong muốn!

# Đúng - Sử dụng None
def them_item_dung(item, danh_sach=None):
    if danh_sach is None:
        danh_sach = []
    danh_sach.append(item)
    return danh_sach

print(them_item_dung("táo"))  # ['táo']
print(them_item_dung("cam"))  # ['cam'] - Đúng!
```

## 3. Variable Arguments

### 3.1 *args - Variable Positional Arguments
```python
def tinh_tong(*args):
    """Tính tổng của nhiều số"""
    tong = 0
    for so in args:
        tong += so
    return tong

# Có thể truyền bất kỳ số lượng arguments nào
print(tinh_tong(1, 2, 3))           # 6
print(tinh_tong(1, 2, 3, 4, 5))     # 15
print(tinh_tong(10, 20))            # 30
print(tinh_tong())                  # 0

def in_thong_tin(ten, *sở_thich):
    """In tên và sở thích"""
    print(f"Tên: {ten}")
    print("Sở thích:")
    for st in sở_thich:
        print(f"  - {st}")

in_thong_tin("An", "đọc sách", "nghe nhạc", "du lịch")
```

### 3.2 **kwargs - Variable Keyword Arguments
```python
def tao_profile(**kwargs):
    """Tạo profile từ keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

# Sử dụng
profile1 = tao_profile(ten="An", tuoi=25, nghe_nghiep="Developer")
profile2 = tao_profile(ten="Bình", tuoi=30, que_quan="Hà Nội", 
                      so_thich="bóng đá")

print(profile1)
print(profile2)

def dang_ky_user(ten, email, **thong_tin_bo_sung):
    """Đăng ký user với thông tin bổ sung"""
    user = {
        'ten': ten,
        'email': email
    }
    
    # Thêm thông tin bổ sung
    user.update(thong_tin_bo_sung)
    
    return user

user = dang_ky_user("An", "an@email.com", tuoi=25, 
                   dia_chi="Hà Nội", sdt="0123456789")
print(user)
```

### 3.3 Kết Hợp *args và **kwargs
```python
def function_phuc_tap(required_param, *args, **kwargs):
    """Function với đầy đủ các loại parameters"""
    print(f"Required: {required_param}")
    
    if args:
        print(f"Args: {args}")
    
    if kwargs:
        print(f"Kwargs: {kwargs}")

# Sử dụng
function_phuc_tap("bắt buộc")
function_phuc_tap("bắt buộc", 1, 2, 3)
function_phuc_tap("bắt buộc", ten="An", tuoi=25)
function_phuc_tap("bắt buộc", 1, 2, 3, ten="An", tuoi=25)
```

## 4. Thứ Tự Parameters

### Quy Tắc Thứ Tự
```python
def function_day_du(
    positional_param,           # 1. Positional parameters
    *args,                      # 2. *args
    keyword_param="default",    # 3. Keyword parameters
    **kwargs                    # 4. **kwargs
):
    pass
```

### Ví Dụ Thực Tế
```python
def xu_ly_don_hang(ma_don_hang, *san_pham, giam_gia=0, **thong_tin_them):
    """Xử lý đơn hàng"""
    print(f"Mã đơn hàng: {ma_don_hang}")
    
    print("Sản phẩm:")
    tong_tien = 0
    for sp in san_pham:
        print(f"  - {sp['ten']}: {sp['gia']:,} VND")
        tong_tien += sp['gia']
    
    print(f"Tổng tiền: {tong_tien:,} VND")
    
    if giam_gia > 0:
        tien_giam = tong_tien * giam_gia / 100
        print(f"Giảm giá: {tien_giam:,} VND")
        tong_tien -= tien_giam
    
    print(f"Thành tiền: {tong_tien:,} VND")
    
    if thong_tin_them:
        print("Thông tin thêm:")
        for key, value in thong_tin_them.items():
            print(f"  {key}: {value}")

# Sử dụng
xu_ly_don_hang(
    "DH001",
    {'ten': 'Laptop', 'gia': 15000000},
    {'ten': 'Chuột', 'gia': 200000},
    giam_gia=10,
    dia_chi="Hà Nội",
    phuong_thuc="COD"
)
```

## 5. Unpacking Arguments

### 5.1 Unpacking Lists/Tuples với *
```python
def tinh_tong_ba_so(a, b, c):
    return a + b + c

# Unpacking list
so_list = [1, 2, 3]
ket_qua = tinh_tong_ba_so(*so_list)
print(ket_qua)  # 6

# Unpacking tuple
so_tuple = (10, 20, 30)
ket_qua = tinh_tong_ba_so(*so_tuple)
print(ket_qua)  # 60
```

### 5.2 Unpacking Dictionaries với **
```python
def gioi_thieu_chi_tiet(ten, tuoi, nghe_nghiep, que_quan):
    return f"{ten}, {tuoi} tuổi, làm {nghe_nghiep}, quê {que_quan}"

# Unpacking dictionary
thong_tin = {
    'ten': 'An',
    'tuoi': 25,
    'nghe_nghiep': 'Developer',
    'que_quan': 'Hà Nội'
}

ket_qua = gioi_thieu_chi_tiet(**thong_tin)
print(ket_qua)
```

## 6. Validation và Error Handling

### 6.1 Kiểm Tra Kiểu Dữ Liệu
```python
def tinh_dien_tich_hinh_chu_nhat(dai, rong):
    """Tính diện tích hình chữ nhật với validation"""
    # Kiểm tra kiểu dữ liệu
    if not isinstance(dai, (int, float)):
        raise TypeError("Chiều dài phải là số")
    if not isinstance(rong, (int, float)):
        raise TypeError("Chiều rộng phải là số")
    
    # Kiểm tra giá trị
    if dai <= 0:
        raise ValueError("Chiều dài phải > 0")
    if rong <= 0:
        raise ValueError("Chiều rộng phải > 0")
    
    return dai * rong

# Sử dụng
try:
    print(tinh_dien_tich_hinh_chu_nhat(5, 3))      # 15
    print(tinh_dien_tich_hinh_chu_nhat(-5, 3))     # ValueError
except (TypeError, ValueError) as e:
    print(f"Lỗi: {e}")
```

### 6.2 Validation Với *args và **kwargs
```python
def tao_san_pham(ten, gia, *danh_muc, **thuoc_tinh):
    """Tạo sản phẩm với validation"""
    # Validate required parameters
    if not isinstance(ten, str) or not ten.strip():
        raise ValueError("Tên sản phẩm phải là chuỗi không rỗng")
    
    if not isinstance(gia, (int, float)) or gia <= 0:
        raise ValueError("Giá phải là số dương")
    
    # Validate categories
    for dm in danh_muc:
        if not isinstance(dm, str):
            raise ValueError("Danh mục phải là chuỗi")
    
    # Validate attributes
    allowed_attrs = ['mau_sac', 'kich_thuoc', 'chat_lieu', 'xuat_xu']
    for attr in thuoc_tinh:
        if attr not in allowed_attrs:
            raise ValueError(f"Thuộc tính '{attr}' không được phép")
    
    return {
        'ten': ten.strip(),
        'gia': gia,
        'danh_muc': list(danh_muc),
        'thuoc_tinh': thuoc_tinh
    }

# Sử dụng
try:
    san_pham = tao_san_pham(
        "Áo thun",
        150000,
        "thời trang",
        "nam",
        mau_sac="đỏ",
        kich_thuoc="L",
        chat_lieu="cotton"
    )
    print(san_pham)
except ValueError as e:
    print(f"Lỗi: {e}")
```

## 7. Ví Dụ Thực Tế

### 7.1 Hệ Thống Đặt Phòng Khách Sạn
```python
def dat_phong(ten_khach, *loai_phong, ngay_checkin=None, ngay_checkout=None, 
              **dich_vu_them):
    """Đặt phòng khách sạn"""
    from datetime import datetime, timedelta
    
    # Validate tên khách
    if not ten_khach or not isinstance(ten_khach, str):
        raise ValueError("Tên khách hàng không hợp lệ")
    
    # Validate loại phòng
    if not loai_phong:
        raise ValueError("Phải chọn ít nhất một loại phòng")
    
    loai_phong_hop_le = ['standard', 'deluxe', 'suite', 'presidential']
    for phong in loai_phong:
        if phong not in loai_phong_hop_le:
            raise ValueError(f"Loại phòng '{phong}' không hợp lệ")
    
    # Xử lý ngày tháng
    if ngay_checkin is None:
        ngay_checkin = datetime.now().date()
    if ngay_checkout is None:
        ngay_checkout = ngay_checkin + timedelta(days=1)
    
    # Tính giá phòng
    gia_phong = {
        'standard': 500000,
        'deluxe': 800000,
        'suite': 1200000,
        'presidential': 2000000
    }
    
    tong_gia_phong = sum(gia_phong[phong] for phong in loai_phong)
    
    # Tính giá dịch vụ thêm
    gia_dich_vu = {
        'spa': 300000,
        'massage': 400000,
        'tour': 500000,
        'xe_dua_don': 200000
    }
    
    tong_gia_dich_vu = 0
    for dv, so_luong in dich_vu_them.items():
        if dv in gia_dich_vu:
            tong_gia_dich_vu += gia_dich_vu[dv] * so_luong
    
    # Tính tổng số ngày
    so_ngay = (ngay_checkout - ngay_checkin).days
    
    # Tạo booking
    booking = {
        'ten_khach': ten_khach,
        'loai_phong': list(loai_phong),
        'ngay_checkin': ngay_checkin,
        'ngay_checkout': ngay_checkout,
        'so_ngay': so_ngay,
        'gia_phong_moi_ngay': tong_gia_phong,
        'tong_gia_phong': tong_gia_phong * so_ngay,
        'dich_vu_them': dich_vu_them,
        'tong_gia_dich_vu': tong_gia_dich_vu,
        'tong_tien': (tong_gia_phong * so_ngay) + tong_gia_dich_vu
    }
    
    return booking

# Sử dụng
from datetime import date

booking = dat_phong(
    "Nguyễn Văn A",
    "deluxe",
    "suite",
    ngay_checkin=date(2024, 1, 15),
    ngay_checkout=date(2024, 1, 18),
    spa=2,
    massage=1,
    tour=1
)

print(f"Khách hàng: {booking['ten_khach']}")
print(f"Loại phòng: {', '.join(booking['loai_phong'])}")
print(f"Số ngày: {booking['so_ngay']}")
print(f"Tổng tiền phòng: {booking['tong_gia_phong']:,} VND")
print(f"Tổng tiền dịch vụ: {booking['tong_gia_dich_vu']:,} VND")
print(f"Tổng cộng: {booking['tong_tien']:,} VND")
```

### 7.2 Hệ Thống Tính Lương Linh Hoạt
```python
def tinh_luong_nhan_vien(ma_nv, luong_co_ban, *phu_cap, 
                        he_so_luong=1.0, **bonus):
    """Tính lương nhân viên với nhiều yếu tố"""
    
    # Validate input
    if not isinstance(ma_nv, str) or not ma_nv:
        raise ValueError("Mã nhân viên không hợp lệ")
    
    if not isinstance(luong_co_ban, (int, float)) or luong_co_ban <= 0:
        raise ValueError("Lương cơ bản phải là số dương")
    
    if not isinstance(he_so_luong, (int, float)) or he_so_luong <= 0:
        raise ValueError("Hệ số lương phải là số dương")
    
    # Tính lương cơ bản sau hệ số
    luong_sau_he_so = luong_co_ban * he_so_luong
    
    # Tính tổng phụ cấp
    tong_phu_cap = 0
    for pc in phu_cap:
        if isinstance(pc, (int, float)) and pc > 0:
            tong_phu_cap += pc
    
    # Tính các khoản bonus
    tong_bonus = 0
    loai_bonus_hop_le = ['hieu_suat', 'du_an', 'le_tet', 'dac_biet']
    
    for loai, so_tien in bonus.items():
        if loai in loai_bonus_hop_le:
            if isinstance(so_tien, (int, float)) and so_tien > 0:
                tong_bonus += so_tien
    
    # Tính tổng lương
    tong_luong = luong_sau_he_so + tong_phu_cap + tong_bonus
    
    # Tính thuế (đơn giản hóa)
    if tong_luong <= 11000000:
        thue = 0
    elif tong_luong <= 25000000:
        thue = (tong_luong - 11000000) * 0.05
    else:
        thue = 700000 + (tong_luong - 25000000) * 0.1
    
    # Tính bảo hiểm (10.5% tổng lương)
    bao_hiem = tong_luong * 0.105
    
    # Lương thực lĩnh
    luong_thuc_linh = tong_luong - thue - bao_hiem
    
    return {
        'ma_nv': ma_nv,
        'luong_co_ban': luong_co_ban,
        'he_so_luong': he_so_luong,
        'luong_sau_he_so': luong_sau_he_so,
        'phu_cap': list(phu_cap),
        'tong_phu_cap': tong_phu_cap,
        'bonus': bonus,
        'tong_bonus': tong_bonus,
        'tong_luong': tong_luong,
        'thue': thue,
        'bao_hiem': bao_hiem,
        'luong_thuc_linh': luong_thuc_linh
    }

# Sử dụng
luong = tinh_luong_nhan_vien(
    "NV001",
    8000000,                    # Lương cơ bản
    500000,                     # Phụ cấp ăn trưa
    300000,                     # Phụ cấp xăng xe
    200000,                     # Phụ cấp điện thoại
    he_so_luong=1.5,           # Hệ số lương
    hieu_suat=1000000,         # Bonus hiệu suất
    du_an=500000,              # Bonus dự án
    le_tet=2000000             # Bonus lễ tết
)

print(f"Mã NV: {luong['ma_nv']}")
print(f"Lương cơ bản: {luong['luong_co_ban']:,} VND")
print(f"Hệ số lương: {luong['he_so_luong']}")
print(f"Lương sau hệ số: {luong['luong_sau_he_so']:,} VND")
print(f"Tổng phụ cấp: {luong['tong_phu_cap']:,} VND")
print(f"Tổng bonus: {luong['tong_bonus']:,} VND")
print(f"Tổng lương: {luong['tong_luong']:,} VND")
print(f"Thuế: {luong['thue']:,} VND")
print(f"Bảo hiểm: {luong['bao_hiem']:,} VND")
print(f"Thực lĩnh: {luong['luong_thuc_linh']:,} VND")
```

## 8. Best Practices

### 8.1 Đặt Tên Parameters Rõ Ràng
```python
# Tốt
def tinh_lai_suat(so_tien_goc, lai_suat_nam, so_nam):
    return so_tien_goc * (lai_suat_nam / 100) * so_nam

# Không tốt
def calc(p, r, t):
    return p * (r / 100) * t
```

### 8.2 Sử Dụng Type Hints
```python
from typing import List, Dict, Optional

def xu_ly_danh_sach_san_pham(
    san_pham: List[Dict[str, any]],
    giam_gia: float = 0.0,
    loai_currency: str = "VND"
) -> Dict[str, any]:
    """Xử lý danh sách sản phẩm với type hints"""
    tong_gia = sum(sp['gia'] for sp in san_pham)
    tien_giam = tong_gia * giam_gia
    
    return {
        'tong_gia': tong_gia,
        'giam_gia': tien_giam,
        'thanh_tien': tong_gia - tien_giam,
        'currency': loai_currency
    }
```

### 8.3 Docstring Chi Tiết
```python
def tinh_khoang_cach_hai_diem(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Tính khoảng cách Euclidean giữa hai điểm trong mặt phẳng 2D.
    
    Args:
        x1 (float): Tọa độ x của điểm thứ nhất
        y1 (float): Tọa độ y của điểm thứ nhất
        x2 (float): Tọa độ x của điểm thứ hai
        y2 (float): Tọa độ y của điểm thứ hai
    
    Returns:
        float: Khoảng cách giữa hai điểm
    
    Raises:
        TypeError: Nếu các tham số không phải là số
    
    Example:
        >>> tinh_khoang_cach_hai_diem(0, 0, 3, 4)
        5.0
        >>> tinh_khoang_cach_hai_diem(1, 1, 4, 5)
        5.0
    """
    import math
    
    # Validate input
    for param in [x1, y1, x2, y2]:
        if not isinstance(param, (int, float)):
            raise TypeError("Tất cả tham số phải là số")
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

## 9. Tổng Kết

Parameters và Arguments là nền tảng để tạo ra các functions linh hoạt và mạnh mẽ:

### Các Điểm Quan Trọng:
1. **Phân biệt Parameters vs Arguments** - Hiểu rõ khái niệm
2. **Sử dụng đúng thứ tự** - Positional → *args → Keyword → **kwargs
3. **Validation đầu vào** - Kiểm tra kiểu và giá trị
4. **Tránh mutable default values** - Sử dụng None thay vì []
5. **Đặt tên rõ ràng** - Parameters phải mô tả chức năng

### Kỹ Thuật Nâng Cao:
- **Unpacking** với * và **
- **Type hints** cho code rõ ràng
- **Error handling** chuyên nghiệp
- **Docstring** chi tiết

### Lộ Trình Học Tiếp:
- **Tiếp theo**: Advanced concepts (Lambda, Decorators, Generators)
- **Thực hành**: Các dự án phức tạp với nhiều parameters
- **Nâng cao**: Functional programming patterns 