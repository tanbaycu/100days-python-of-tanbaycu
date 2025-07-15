# Lý Thuyết 1: Classes & Objects Cơ Bản - Nền Tảng OOP

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Hiểu rõ khái niệm Class và Object, mối quan hệ giữa chúng
- Nắm vững cách tạo và sử dụng Classes trong Python
- Thành thạo Attributes và Methods
- Hiểu Constructor và Destructor
- Áp dụng OOP vào các bài toán thực tế

---

## 1. Tại Sao Cần Object-Oriented Programming?

### 1.1 Vấn Đề Với Procedural Programming

**Ví dụ: Quản lý thông tin sinh viên**

```python
# Procedural approach - Khó quản lý và mở rộng
sinh_vien_1_ten = "Nguyễn Văn An"
sinh_vien_1_tuoi = 20
sinh_vien_1_diem = [8.5, 7.0, 9.0]

sinh_vien_2_ten = "Trần Thị Bình"
sinh_vien_2_tuoi = 19
sinh_vien_2_diem = [7.5, 8.0, 8.5]

def tinh_diem_trung_binh_sv1():
    return sum(sinh_vien_1_diem) / len(sinh_vien_1_diem)

def tinh_diem_trung_binh_sv2():
    return sum(sinh_vien_2_diem) / len(sinh_vien_2_diem)

# Vấn đề: Code lặp lại, khó maintain, không scale
```

### 1.2 Giải Pháp OOP

```python
# OOP approach - Clean, scalable, maintainable
class SinhVien:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
    
    def tinh_diem_trung_binh(self):
        return sum(self.diem) / len(self.diem)
    
    def hien_thi_thong_tin(self):
        return f"{self.ten} - {self.tuoi} tuổi - ĐTB: {self.tinh_diem_trung_binh():.2f}"

# Sử dụng
sv1 = SinhVien("Nguyễn Văn An", 20, [8.5, 7.0, 9.0])
sv2 = SinhVien("Trần Thị Bình", 19, [7.5, 8.0, 8.5])

print(sv1.hien_thi_thong_tin())
print(sv2.hien_thi_thong_tin())
```

### 1.3 Lợi Ích Của OOP

1. **Tái sử dụng code**: Một class có thể tạo nhiều objects
2. **Dễ bảo trì**: Thay đổi logic ở một nơi
3. **Mở rộng dễ dàng**: Thêm features mới không ảnh hưởng code cũ
4. **Mô hình hóa thế giới thực**: Classes giống như blueprints của objects thực tế

---

## 2. Khái Niệm Class và Object

### 2.1 Class - Bản Thiết Kế (Blueprint)

**Class** là một template/blueprint định nghĩa:
- **Attributes** (thuộc tính): Dữ liệu mà object sẽ chứa
- **Methods** (phương thức): Hành vi mà object có thể thực hiện

```python
class XeHoi:
    """Class mô tả một chiếc xe hơi"""
    
    # Class attribute (thuộc tính chung cho tất cả objects)
    loai_phuong_tien = "Xe hơi"
    
    def __init__(self, hang, mau, nam_san_xuat):
        # Instance attributes (thuộc tính riêng của từng object)
        self.hang = hang
        self.mau = mau
        self.nam_san_xuat = nam_san_xuat
        self.toc_do = 0
        self.dang_chay = False
    
    # Methods (phương thức)
    def khoi_dong(self):
        self.dang_chay = True
        print(f"Xe {self.hang} {self.mau} đã khởi động")
    
    def tang_toc(self, toc_do_moi):
        if self.dang_chay:
            self.toc_do = toc_do_moi
            print(f"Tăng tốc lên {self.toc_do} km/h")
        else:
            print("Xe chưa khởi động!")
    
    def dung_lai(self):
        self.toc_do = 0
        self.dang_chay = False
        print("Xe đã dừng lại")
```

### 2.2 Object - Thực Thể (Instance)

**Object** là một instance cụ thể được tạo từ class:

```python
# Tạo objects từ class XeHoi
xe_1 = XeHoi("Toyota", "Đỏ", 2020)
xe_2 = XeHoi("Honda", "Xanh", 2021)

# Mỗi object có attributes riêng
print(f"Xe 1: {xe_1.hang} {xe_1.mau}")  # Toyota Đỏ
print(f"Xe 2: {xe_2.hang} {xe_2.mau}")  # Honda Xanh

# Nhưng cùng class attribute
print(xe_1.loai_phuong_tien)  # Xe hơi
print(xe_2.loai_phuong_tien)  # Xe hơi

# Mỗi object có thể thực hiện methods độc lập
xe_1.khoi_dong()
xe_1.tang_toc(60)

xe_2.khoi_dong()
xe_2.tang_toc(80)
```

---

## 3. Attributes - Thuộc Tính

### 3.1 Instance Attributes

**Instance attributes** là thuộc tính riêng của từng object:

```python
class NhanVien:
    def __init__(self, ten, chuc_vu, luong):
        self.ten = ten              # Instance attribute
        self.chuc_vu = chuc_vu      # Instance attribute
        self.luong = luong          # Instance attribute
        self.so_ngay_lam = 0        # Instance attribute với giá trị mặc định

# Mỗi object có attributes riêng
nv1 = NhanVien("An", "Developer", 15000000)
nv2 = NhanVien("Bình", "Designer", 12000000)

print(f"{nv1.ten}: {nv1.luong:,}")  # An: 15,000,000
print(f"{nv2.ten}: {nv2.luong:,}")  # Bình: 12,000,000

# Thay đổi attribute của một object không ảnh hưởng object khác
nv1.luong = 18000000
print(f"{nv1.ten}: {nv1.luong:,}")  # An: 18,000,000
print(f"{nv2.ten}: {nv2.luong:,}")  # Bình: 12,000,000 (không thay đổi)
```

### 3.2 Class Attributes

**Class attributes** là thuộc tính chung cho tất cả objects của class:

```python
class NhanVien:
    # Class attributes
    cong_ty = "ABC Tech Company"
    he_so_thuong = 0.1
    so_luong_nhan_vien = 0
    
    def __init__(self, ten, chuc_vu, luong):
        self.ten = ten
        self.chuc_vu = chuc_vu
        self.luong = luong
        
        # Tăng số lượng nhân viên khi tạo object mới
        NhanVien.so_luong_nhan_vien += 1
    
    def thong_tin_cong_ty(self):
        return f"Nhân viên {self.ten} làm việc tại {NhanVien.cong_ty}"
    
    def tinh_thuong(self):
        return self.luong * NhanVien.he_so_thuong

# Sử dụng
nv1 = NhanVien("An", "Developer", 15000000)
nv2 = NhanVien("Bình", "Designer", 12000000)

print(f"Tổng nhân viên: {NhanVien.so_luong_nhan_vien}")  # 2
print(nv1.thong_tin_cong_ty())
print(f"Thưởng của {nv1.ten}: {nv1.tinh_thuong():,}")

# Thay đổi class attribute ảnh hưởng tất cả objects
NhanVien.he_so_thuong = 0.15
print(f"Thưởng mới của {nv1.ten}: {nv1.tinh_thuong():,}")
print(f"Thưởng mới của {nv2.ten}: {nv2.tinh_thuong():,}")
```

### 3.3 Dynamic Attributes

Python cho phép thêm attributes động:

```python
class SanPham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

sp = SanPham("Laptop", 15000000)
print(f"Sản phẩm: {sp.ten}")

# Thêm attribute động
sp.mau_sac = "Đen"
sp.bao_hanh = "2 năm"

print(f"Màu sắc: {sp.mau_sac}")
print(f"Bảo hành: {sp.bao_hanh}")

# Kiểm tra attribute có tồn tại
print(hasattr(sp, 'mau_sac'))    # True
print(hasattr(sp, 'can_nang'))   # False

# Lấy giá trị attribute an toàn
print(getattr(sp, 'mau_sac', 'Không có'))      # Đen
print(getattr(sp, 'can_nang', 'Không có'))     # Không có
```

---

## 4. Methods - Phương Thức

### 4.1 Instance Methods

**Instance methods** là methods thao tác với instance attributes:

```python
class TaiKhoanNganHang:
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du_ban_dau=0):
        self.so_tai_khoan = so_tai_khoan
        self.ten_chu_tai_khoan = ten_chu_tai_khoan
        self.so_du = so_du_ban_dau
        self.lich_su_giao_dich = []
    
    def nap_tien(self, so_tien):
        """Nạp tiền vào tài khoản"""
        if so_tien > 0:
            self.so_du += so_tien
            self.lich_su_giao_dich.append(f"Nạp: +{so_tien:,} VND")
            print(f"Nạp thành công {so_tien:,} VND. Số dư: {self.so_du:,} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0")
    
    def rut_tien(self, so_tien):
        """Rút tiền từ tài khoản"""
        if so_tien > 0:
            if self.so_du >= so_tien:
                self.so_du -= so_tien
                self.lich_su_giao_dich.append(f"Rút: -{so_tien:,} VND")
                print(f"Rút thành công {so_tien:,} VND. Số dư: {self.so_du:,} VND")
            else:
                print("Số dư không đủ")
        else:
            print("Số tiền rút phải lớn hơn 0")
    
    def kiem_tra_so_du(self):
        """Kiểm tra số dư tài khoản"""
        print(f"Số dư tài khoản {self.so_tai_khoan}: {self.so_du:,} VND")
        return self.so_du
    
    def xem_lich_su(self):
        """Xem lịch sử giao dịch"""
        print(f"Lịch sử giao dịch tài khoản {self.so_tai_khoan}:")
        for giao_dich in self.lich_su_giao_dich:
            print(f"  {giao_dich}")

# Sử dụng
tai_khoan = TaiKhoanNganHang("123456789", "Nguyễn Văn An", 1000000)

tai_khoan.kiem_tra_so_du()
tai_khoan.nap_tien(500000)
tai_khoan.rut_tien(200000)
tai_khoan.xem_lich_su()
```

### 4.2 Class Methods

**Class methods** làm việc với class attributes, sử dụng decorator `@classmethod`:

```python
class SinhVien:
    truong = "Đại học ABC"
    so_luong_sinh_vien = 0
    
    def __init__(self, ten, nganh):
        self.ten = ten
        self.nganh = nganh
        SinhVien.so_luong_sinh_vien += 1
    
    @classmethod
    def thong_tin_truong(cls):
        """Class method để lấy thông tin trường"""
        return f"Trường: {cls.truong}, Tổng sinh viên: {cls.so_luong_sinh_vien}"
    
    @classmethod
    def doi_ten_truong(cls, ten_moi):
        """Class method để thay đổi tên trường"""
        cls.truong = ten_moi
        print(f"Đã đổi tên trường thành: {cls.truong}")
    
    @classmethod
    def tao_sinh_vien_cntt(cls, ten):
        """Factory method tạo sinh viên CNTT"""
        return cls(ten, "Công nghệ thông tin")
    
    @classmethod
    def tao_sinh_vien_kinh_te(cls, ten):
        """Factory method tạo sinh viên Kinh tế"""
        return cls(ten, "Kinh tế")

# Sử dụng class methods
print(SinhVien.thong_tin_truong())

sv1 = SinhVien("An", "Toán học")
sv2 = SinhVien.tao_sinh_vien_cntt("Bình")
sv3 = SinhVien.tao_sinh_vien_kinh_te("Cường")

print(SinhVien.thong_tin_truong())
SinhVien.doi_ten_truong("Đại học XYZ")
```

### 4.3 Static Methods

**Static methods** không cần self hay cls, sử dụng decorator `@staticmethod`:

```python
class TienIch:
    @staticmethod
    def kiem_tra_email(email):
        """Kiểm tra format email"""
        return "@" in email and "." in email
    
    @staticmethod
    def ma_hoa_mat_khau(mat_khau):
        """Mã hóa mật khẩu đơn giản"""
        return "".join(chr(ord(char) + 1) for char in mat_khau)
    
    @staticmethod
    def tinh_khoang_cach(x1, y1, x2, y2):
        """Tính khoảng cách giữa 2 điểm"""
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Sử dụng static methods (không cần tạo object)
print(TienIch.kiem_tra_email("user@example.com"))  # True
print(TienIch.kiem_tra_email("invalid-email"))     # False

mat_khau_ma_hoa = TienIch.ma_hoa_mat_khau("password123")
print(f"Mật khẩu mã hóa: {mat_khau_ma_hoa}")

khoang_cach = TienIch.tinh_khoang_cach(0, 0, 3, 4)
print(f"Khoảng cách: {khoang_cach}")  # 5.0
```

---

## 5. Constructor và Destructor

### 5.1 Constructor (__init__)

**Constructor** được gọi khi tạo object mới:

```python
class KhachHang:
    def __init__(self, ten, email, so_dien_thoai=None):
        """Constructor với validation"""
        print(f"Đang tạo khách hàng: {ten}")
        
        # Validation
        if not ten or not isinstance(ten, str):
            raise ValueError("Tên khách hàng không hợp lệ")
        
        if not email or "@" not in email:
            raise ValueError("Email không hợp lệ")
        
        # Gán attributes
        self.ten = ten.strip().title()
        self.email = email.lower()
        self.so_dien_thoai = so_dien_thoai
        self.ngay_tao = self._lay_ngay_hien_tai()
        self.trang_thai = "Hoạt động"
        
        print(f"Đã tạo khách hàng thành công: {self.ten}")
    
    def _lay_ngay_hien_tai(self):
        """Private method lấy ngày hiện tại"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def hien_thi_thong_tin(self):
        return f"KH: {self.ten} - {self.email} - Tạo: {self.ngay_tao}"

# Sử dụng constructor
try:
    kh1 = KhachHang("nguyễn văn an", "an@email.com", "0123456789")
    print(kh1.hien_thi_thong_tin())
    
    # Sẽ raise exception
    kh2 = KhachHang("", "invalid-email")
except ValueError as e:
    print(f"Lỗi: {e}")
```

### 5.2 Destructor (__del__)

**Destructor** được gọi khi object bị xóa khỏi memory:

```python
class KetNoiDatabase:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connected = False
        print(f"Khởi tạo kết nối đến {host}/{database}")
        self.ket_noi()
    
    def ket_noi(self):
        """Mô phỏng kết nối database"""
        self.connected = True
        print(f"Đã kết nối thành công đến {self.database}")
    
    def thuc_hien_truy_van(self, sql):
        """Thực hiện truy vấn"""
        if self.connected:
            print(f"Thực hiện: {sql}")
            return f"Kết quả từ {self.database}"
        else:
            print("Chưa kết nối database")
    
    def dong_ket_noi(self):
        """Đóng kết nối"""
        if self.connected:
            self.connected = False
            print(f"Đã đóng kết nối đến {self.database}")
    
    def __del__(self):
        """Destructor - tự động đóng kết nối"""
        if hasattr(self, 'connected') and self.connected:
            print(f"Destructor: Đang đóng kết nối đến {self.database}")
            self.dong_ket_noi()

# Sử dụng
db = KetNoiDatabase("localhost", "my_database")
db.thuc_hien_truy_van("SELECT * FROM users")

# Khi object bị xóa, destructor sẽ được gọi
del db  # Hoặc khi kết thúc scope
```

---

## 6. Ví Dụ Thực Tế

### 6.1 Hệ Thống Quản Lý Thư Viện

```python
from datetime import datetime, timedelta

class Sach:
    def __init__(self, ma_sach, tieu_de, tac_gia, nam_xuat_ban, so_luong):
        self.ma_sach = ma_sach
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.so_luong = so_luong
        self.so_luong_co_san = so_luong
        self.danh_sach_muon = []
    
    def co_san_khong(self):
        return self.so_luong_co_san > 0
    
    def muon_sach(self, ma_doc_gia):
        if self.co_san_khong():
            self.so_luong_co_san -= 1
            ngay_muon = datetime.now()
            ngay_tra = ngay_muon + timedelta(days=14)  # Mượn 14 ngày
            
            thong_tin_muon = {
                'ma_doc_gia': ma_doc_gia,
                'ngay_muon': ngay_muon,
                'ngay_tra_du_kien': ngay_tra,
                'da_tra': False
            }
            self.danh_sach_muon.append(thong_tin_muon)
            return True
        return False
    
    def tra_sach(self, ma_doc_gia):
        for thong_tin in self.danh_sach_muon:
            if (thong_tin['ma_doc_gia'] == ma_doc_gia and 
                not thong_tin['da_tra']):
                thong_tin['da_tra'] = True
                thong_tin['ngay_tra_thuc_te'] = datetime.now()
                self.so_luong_co_san += 1
                return True
        return False
    
    def __str__(self):
        return f"{self.tieu_de} - {self.tac_gia} ({self.nam_xuat_ban})"

class DocGia:
    def __init__(self, ma_doc_gia, ten, email, so_dien_thoai):
        self.ma_doc_gia = ma_doc_gia
        self.ten = ten
        self.email = email
        self.so_dien_thoai = so_dien_thoai
        self.ngay_dang_ky = datetime.now()
        self.sach_dang_muon = []
        self.lich_su_muon = []
    
    def muon_sach(self, sach):
        if sach.muon_sach(self.ma_doc_gia):
            self.sach_dang_muon.append(sach.ma_sach)
            self.lich_su_muon.append({
                'ma_sach': sach.ma_sach,
                'tieu_de': sach.tieu_de,
                'ngay_muon': datetime.now()
            })
            return True
        return False
    
    def tra_sach(self, sach):
        if sach.tra_sach(self.ma_doc_gia):
            if sach.ma_sach in self.sach_dang_muon:
                self.sach_dang_muon.remove(sach.ma_sach)
            return True
        return False
    
    def __str__(self):
        return f"Độc giả: {self.ten} (ID: {self.ma_doc_gia})"

class ThuVien:
    def __init__(self, ten_thu_vien):
        self.ten_thu_vien = ten_thu_vien
        self.danh_sach_sach = {}
        self.danh_sach_doc_gia = {}
    
    def them_sach(self, sach):
        self.danh_sach_sach[sach.ma_sach] = sach
        print(f"Đã thêm sách: {sach}")
    
    def dang_ky_doc_gia(self, doc_gia):
        self.danh_sach_doc_gia[doc_gia.ma_doc_gia] = doc_gia
        print(f"Đã đăng ký: {doc_gia}")
    
    def muon_sach(self, ma_doc_gia, ma_sach):
        if (ma_doc_gia in self.danh_sach_doc_gia and 
            ma_sach in self.danh_sach_sach):
            
            doc_gia = self.danh_sach_doc_gia[ma_doc_gia]
            sach = self.danh_sach_sach[ma_sach]
            
            if doc_gia.muon_sach(sach):
                print(f"{doc_gia.ten} đã mượn sách: {sach.tieu_de}")
                return True
            else:
                print(f"Sách '{sach.tieu_de}' hiện không có sẵn")
        return False
    
    def tra_sach(self, ma_doc_gia, ma_sach):
        if (ma_doc_gia in self.danh_sach_doc_gia and 
            ma_sach in self.danh_sach_sach):
            
            doc_gia = self.danh_sach_doc_gia[ma_doc_gia]
            sach = self.danh_sach_sach[ma_sach]
            
            if doc_gia.tra_sach(sach):
                print(f"{doc_gia.ten} đã trả sách: {sach.tieu_de}")
                return True
        return False
    
    def tim_sach(self, tu_khoa):
        ket_qua = []
        for sach in self.danh_sach_sach.values():
            if (tu_khoa.lower() in sach.tieu_de.lower() or 
                tu_khoa.lower() in sach.tac_gia.lower()):
                ket_qua.append(sach)
        return ket_qua
    
    def thong_ke(self):
        tong_sach = len(self.danh_sach_sach)
        tong_doc_gia = len(self.danh_sach_doc_gia)
        sach_dang_muon = sum(1 for sach in self.danh_sach_sach.values() 
                           if sach.so_luong_co_san < sach.so_luong)
        
        print(f"\n=== THỐNG KÊ THƯ VIỆN {self.ten_thu_vien} ===")
        print(f"Tổng số sách: {tong_sach}")
        print(f"Tổng độc giả: {tong_doc_gia}")
        print(f"Sách đang được mượn: {sach_dang_muon}")

# Sử dụng hệ thống
thu_vien = ThuVien("Thư viện Trung tâm")

# Thêm sách
sach1 = Sach("S001", "Python Programming", "John Doe", 2020, 5)
sach2 = Sach("S002", "Data Science", "Jane Smith", 2021, 3)
thu_vien.them_sach(sach1)
thu_vien.them_sach(sach2)

# Đăng ký độc giả
doc_gia1 = DocGia("DG001", "Nguyễn Văn An", "an@email.com", "0123456789")
doc_gia2 = DocGia("DG002", "Trần Thị Bình", "binh@email.com", "0987654321")
thu_vien.dang_ky_doc_gia(doc_gia1)
thu_vien.dang_ky_doc_gia(doc_gia2)

# Mượn và trả sách
thu_vien.muon_sach("DG001", "S001")
thu_vien.muon_sach("DG002", "S001")
thu_vien.tra_sach("DG001", "S001")
thu_vien.muon_sach("DG002", "S001")

# Tìm sách
ket_qua = thu_vien.tim_sach("Python")
print(f"\nKết quả tìm kiếm 'Python': {len(ket_qua)} sách")

# Thống kê
thu_vien.thong_ke()
```

### 6.2 Hệ Thống E-commerce Đơn Giản

```python
from datetime import datetime
from enum import Enum

class TrangThaiDonHang(Enum):
    CHO_XAC_NHAN = "Chờ xác nhận"
    DA_XAC_NHAN = "Đã xác nhận"
    DANG_GIAO = "Đang giao"
    DA_GIAO = "Đã giao"
    HUY = "Hủy"

class SanPham:
    def __init__(self, ma_sp, ten, gia, so_luong, mo_ta=""):
        self.ma_sp = ma_sp
        self.ten = ten
        self.gia = gia
        self.so_luong = so_luong
        self.mo_ta = mo_ta
        self.danh_gia = []
        self.luot_xem = 0
    
    def cap_nhat_so_luong(self, so_luong_moi):
        self.so_luong = so_luong_moi
    
    def giam_so_luong(self, so_luong):
        if self.so_luong >= so_luong:
            self.so_luong -= so_luong
            return True
        return False
    
    def them_danh_gia(self, danh_gia, binh_luan=""):
        self.danh_gia.append({
            'diem': danh_gia,
            'binh_luan': binh_luan,
            'ngay': datetime.now()
        })
    
    def diem_trung_binh(self):
        if not self.danh_gia:
            return 0
        return sum(dg['diem'] for dg in self.danh_gia) / len(self.danh_gia)
    
    def tang_luot_xem(self):
        self.luot_xem += 1
    
    def __str__(self):
        return f"{self.ten} - {self.gia:,} VND (Còn: {self.so_luong})"

class KhachHang:
    def __init__(self, ma_kh, ten, email, dia_chi, so_dien_thoai):
        self.ma_kh = ma_kh
        self.ten = ten
        self.email = email
        self.dia_chi = dia_chi
        self.so_dien_thoai = so_dien_thoai
        self.gio_hang = GioHang()
        self.lich_su_don_hang = []
        self.diem_tich_luy = 0
    
    def them_vao_gio_hang(self, san_pham, so_luong):
        return self.gio_hang.them_san_pham(san_pham, so_luong)
    
    def xoa_khoi_gio_hang(self, ma_sp):
        self.gio_hang.xoa_san_pham(ma_sp)
    
    def dat_hang(self):
        if self.gio_hang.co_san_pham():
            don_hang = DonHang(self, self.gio_hang.sao_chep())
            self.lich_su_don_hang.append(don_hang)
            
            # Tích điểm (1 điểm = 1000 VND)
            self.diem_tich_luy += int(don_hang.tong_tien() / 1000)
            
            # Xóa giỏ hàng
            self.gio_hang.xoa_tat_ca()
            return don_hang
        return None
    
    def __str__(self):
        return f"KH: {self.ten} - Điểm: {self.diem_tich_luy}"

class GioHang:
    def __init__(self):
        self.danh_sach_san_pham = {}  # {ma_sp: {'san_pham': obj, 'so_luong': int}}
    
    def them_san_pham(self, san_pham, so_luong):
        if san_pham.so_luong >= so_luong:
            if san_pham.ma_sp in self.danh_sach_san_pham:
                self.danh_sach_san_pham[san_pham.ma_sp]['so_luong'] += so_luong
            else:
                self.danh_sach_san_pham[san_pham.ma_sp] = {
                    'san_pham': san_pham,
                    'so_luong': so_luong
                }
            return True
        return False
    
    def xoa_san_pham(self, ma_sp):
        if ma_sp in self.danh_sach_san_pham:
            del self.danh_sach_san_pham[ma_sp]
    
    def cap_nhat_so_luong(self, ma_sp, so_luong_moi):
        if ma_sp in self.danh_sach_san_pham:
            self.danh_sach_san_pham[ma_sp]['so_luong'] = so_luong_moi
    
    def tong_tien(self):
        tong = 0
        for item in self.danh_sach_san_pham.values():
            tong += item['san_pham'].gia * item['so_luong']
        return tong
    
    def so_luong_san_pham(self):
        return sum(item['so_luong'] for item in self.danh_sach_san_pham.values())
    
    def co_san_pham(self):
        return len(self.danh_sach_san_pham) > 0
    
    def sao_chep(self):
        gio_hang_moi = GioHang()
        gio_hang_moi.danh_sach_san_pham = self.danh_sach_san_pham.copy()
        return gio_hang_moi
    
    def xoa_tat_ca(self):
        self.danh_sach_san_pham.clear()
    
    def hien_thi(self):
        print("=== GIỎ HÀNG ===")
        if not self.co_san_pham():
            print("Giỏ hàng trống")
            return
        
        for item in self.danh_sach_san_pham.values():
            sp = item['san_pham']
            sl = item['so_luong']
            thanh_tien = sp.gia * sl
            print(f"{sp.ten} x{sl} = {thanh_tien:,} VND")
        
        print(f"Tổng cộng: {self.tong_tien():,} VND")

class DonHang:
    _ma_don_hang_counter = 1
    
    def __init__(self, khach_hang, gio_hang):
        self.ma_don_hang = f"DH{DonHang._ma_don_hang_counter:04d}"
        DonHang._ma_don_hang_counter += 1
        
        self.khach_hang = khach_hang
        self.danh_sach_san_pham = gio_hang.danh_sach_san_pham.copy()
        self.ngay_dat = datetime.now()
        self.trang_thai = TrangThaiDonHang.CHO_XAC_NHAN
        
        # Trừ số lượng sản phẩm
        for item in self.danh_sach_san_pham.values():
            item['san_pham'].giam_so_luong(item['so_luong'])
    
    def cap_nhat_trang_thai(self, trang_thai_moi):
        self.trang_thai = trang_thai_moi
        print(f"Đơn hàng {self.ma_don_hang} đã chuyển sang: {trang_thai_moi.value}")
    
    def tong_tien(self):
        tong = 0
        for item in self.danh_sach_san_pham.values():
            tong += item['san_pham'].gia * item['so_luong']
        return tong
    
    def hien_thi_chi_tiet(self):
        print(f"\n=== ĐON HÀNG {self.ma_don_hang} ===")
        print(f"Khách hàng: {self.khach_hang.ten}")
        print(f"Ngày đặt: {self.ngay_dat.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Trạng thái: {self.trang_thai.value}")
        print("\nChi tiết:")
        
        for item in self.danh_sach_san_pham.values():
            sp = item['san_pham']
            sl = item['so_luong']
            thanh_tien = sp.gia * sl
            print(f"  {sp.ten} x{sl} = {thanh_tien:,} VND")
        
        print(f"\nTổng cộng: {self.tong_tien():,} VND")

# Sử dụng hệ thống E-commerce
print("=== HỆ THỐNG E-COMMERCE ===\n")

# Tạo sản phẩm
sp1 = SanPham("SP001", "Laptop Dell", 15000000, 10, "Laptop gaming cao cấp")
sp2 = SanPham("SP002", "Chuột Logitech", 500000, 50, "Chuột không dây")
sp3 = SanPham("SP003", "Bàn phím cơ", 1200000, 20, "Bàn phím cơ RGB")

# Tạo khách hàng
kh1 = KhachHang("KH001", "Nguyễn Văn An", "an@email.com", 
                "123 Đường ABC, Hà Nội", "0123456789")

# Thêm sản phẩm vào giỏ hàng
kh1.them_vao_gio_hang(sp1, 1)
kh1.them_vao_gio_hang(sp2, 2)
kh1.them_vao_gio_hang(sp3, 1)

# Hiển thị giỏ hàng
kh1.gio_hang.hien_thi()

# Đặt hàng
don_hang = kh1.dat_hang()
if don_hang:
    don_hang.hien_thi_chi_tiet()
    
    # Cập nhật trạng thái đơn hàng
    don_hang.cap_nhat_trang_thai(TrangThaiDonHang.DA_XAC_NHAN)
    don_hang.cap_nhat_trang_thai(TrangThaiDonHang.DANG_GIAO)
    don_hang.cap_nhat_trang_thai(TrangThaiDonHang.DA_GIAO)

# Thêm đánh giá sản phẩm
sp1.them_danh_gia(5, "Sản phẩm rất tốt!")
sp1.them_danh_gia(4, "Giá hơi cao nhưng chất lượng ok")

print(f"\nĐánh giá trung bình {sp1.ten}: {sp1.diem_trung_binh():.1f}/5")
print(f"Khách hàng {kh1.ten} có {kh1.diem_tich_luy} điểm tích lũy")
```

---

## 7. Best Practices

### 7.1 Đặt Tên Class và Method

```python
# Tốt - Class names sử dụng PascalCase
class QuanLyNhanVien:
    def __init__(self, ten_cong_ty):
        self.ten_cong_ty = ten_cong_ty
    
    # Tốt - Method names sử dụng snake_case
    def them_nhan_vien(self, nhan_vien):
        pass
    
    def tinh_tong_luong(self):
        pass

# Không tốt
class quanLyNhanVien:  # Sai naming convention
    def ThemNhanVien(self):  # Sai naming convention
        pass
```

### 7.2 Docstrings và Comments

```python
class TaiKhoanNganHang:
    """
    Class quản lý tài khoản ngân hàng
    
    Attributes:
        so_tai_khoan (str): Số tài khoản
        ten_chu_tai_khoan (str): Tên chủ tài khoản
        so_du (float): Số dư hiện tại
    """
    
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du_ban_dau=0):
        """
        Khởi tạo tài khoản ngân hàng
        
        Args:
            so_tai_khoan (str): Số tài khoản duy nhất
            ten_chu_tai_khoan (str): Tên chủ tài khoản
            so_du_ban_dau (float, optional): Số dư ban đầu. Defaults to 0.
        """
        self.so_tai_khoan = so_tai_khoan
        self.ten_chu_tai_khoan = ten_chu_tai_khoan
        self.so_du = so_du_ban_dau
    
    def rut_tien(self, so_tien):
        """
        Rút tiền từ tài khoản
        
        Args:
            so_tien (float): Số tiền cần rút
            
        Returns:
            bool: True nếu rút thành công, False nếu thất bại
            
        Raises:
            ValueError: Nếu số tiền không hợp lệ
        """
        if so_tien <= 0:
            raise ValueError("Số tiền phải lớn hơn 0")
        
        if self.so_du >= so_tien:
            self.so_du -= so_tien
            return True
        return False
```

### 7.3 Error Handling

```python
class SanPham:
    def __init__(self, ten, gia, so_luong):
        # Validation trong constructor
        if not isinstance(ten, str) or not ten.strip():
            raise ValueError("Tên sản phẩm phải là chuỗi không rỗng")
        
        if not isinstance(gia, (int, float)) or gia <= 0:
            raise ValueError("Giá phải là số dương")
        
        if not isinstance(so_luong, int) or so_luong < 0:
            raise ValueError("Số lượng phải là số nguyên không âm")
        
        self.ten = ten.strip()
        self.gia = float(gia)
        self.so_luong = so_luong
    
    def cap_nhat_gia(self, gia_moi):
        """Cập nhật giá với validation"""
        if not isinstance(gia_moi, (int, float)) or gia_moi <= 0:
            raise ValueError("Giá mới phải là số dương")
        
        gia_cu = self.gia
        self.gia = float(gia_moi)
        print(f"Đã cập nhật giá từ {gia_cu:,} thành {self.gia:,}")

# Sử dụng với error handling
try:
    sp = SanPham("Laptop", 15000000, 10)
    sp.cap_nhat_gia(18000000)
    
    # Sẽ raise exception
    sp.cap_nhat_gia(-1000)
except ValueError as e:
    print(f"Lỗi: {e}")
```

---

## 8. Tổng Kết

Classes và Objects là nền tảng của OOP, giúp:

### Lợi Ích Chính:
1. **Tổ chức code tốt hơn** - Nhóm data và behavior liên quan
2. **Tái sử dụng code** - Một class tạo nhiều objects
3. **Dễ bảo trì** - Thay đổi ở một nơi, ảnh hưởng toàn bộ
4. **Mô hình hóa thực tế** - Classes giống blueprints thực tế

### Điểm Quan Trọng:
- **Class**: Template/Blueprint định nghĩa structure
- **Object**: Instance cụ thể từ class
- **Attributes**: Dữ liệu của object
- **Methods**: Hành vi của object
- **Constructor**: Khởi tạo object
- **Destructor**: Dọn dẹp khi object bị xóa

### Lộ Trình Học Tiếp:
- **Tiếp theo**: Inheritance & Polymorphism
- **Nâng cao**: Encapsulation & Abstraction
- **Thực hành**: Các dự án OOP phức tạp

**"Classes are about creating new types, objects are about creating instances of those types."** 