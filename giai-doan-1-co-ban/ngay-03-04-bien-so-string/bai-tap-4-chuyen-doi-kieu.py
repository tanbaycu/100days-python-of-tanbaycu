# Bài Tập 4: Chuyển Đổi Kiểu Dữ Liệu
# Ngày 3-4: Type Conversion và Error Handling

print("=== BÀI TẬP 4: CHUYỂN ĐỔI KIỂU DỮ LIỆU ===")

# PHẦN A: CHUYỂN ĐỔI CƠ BẢN
print("\n" + "="*50)
print("PHẦN A: CHUYỂN ĐỔI CƠ BẢN")
print("="*50)

# Bài A1: String sang Number
print("\n--- Bài A1: String sang Number ---")
so_str = "123"
diem_str = "8.5"
nam_str = "2024"

so_int = int(so_str)
diem_float = float(diem_str)
nam_int = int(nam_str)

print(f"String '{so_str}' → int: {so_int} (type: {type(so_int)})")
print(f"String '{diem_str}' → float: {diem_float} (type: {type(diem_float)})")
print(f"String '{nam_str}' → int: {nam_int} (type: {type(nam_int)})")

# Bài A2: Number sang String
print("\n--- Bài A2: Number sang String ---")
tuoi = 18
diem_tb = 8.75
so_lon = 1000000

tuoi_str = str(tuoi)
diem_str = str(diem_tb)
so_lon_str = str(so_lon)

print(f"int {tuoi} → string: '{tuoi_str}' (type: {type(tuoi_str)})")
print(f"float {diem_tb} → string: '{diem_str}' (type: {type(diem_str)})")
print(f"int {so_lon} → string: '{so_lon_str}' (type: {type(so_lon_str)})")

# Bài A3: Float và Int qua lại
print("\n--- Bài A3: Float ↔ Int ---")
so_thuc = 9.7
so_nguyen = 15

# Float → Int (cắt phần thập phân)
so_thuc_thanh_int = int(so_thuc)
print(f"float {so_thuc} → int: {so_thuc_thanh_int}")

# Int → Float
so_nguyen_thanh_float = float(so_nguyen)
print(f"int {so_nguyen} → float: {so_nguyen_thanh_float}")

# Làm tròn trước khi chuyển
so_thuc_lam_tron = round(so_thuc)
print(f"round({so_thuc}) = {so_thuc_lam_tron}")

# PHẦN B: XỬ LÝ LỖI
print("\n" + "="*50)
print("PHẦN B: XỬ LÝ LỖI CHUYỂN ĐỔI")
print("="*50)

print("\n--- Bài B1: Các lỗi thường gặp ---")

# Ví dụ các string không thể chuyển đổi
cac_string_loi = ["abc", "12.5.7", "3.14.15", "", "  ", "12a34"]

for s in cac_string_loi:
    print(f"\nThử chuyển '{s}' sang int:")
    try:
        ket_qua = int(s)
        print(f"  Thành công: {ket_qua}")
    except ValueError as e:
        print(f"  Lỗi: {e}")

# Bài B2: Validation an toàn
print("\n--- Bài B2: Validation an toàn ---")

def chuyen_doi_an_toan(s, kieu):
    """Chuyển đổi string một cách an toàn"""
    try:
        if kieu == "int":
            return int(s), True
        elif kieu == "float":
            return float(s), True
    except ValueError:
        return None, False

# Test với nhiều giá trị
test_values = ["123", "45.6", "abc", "12.34.56", "  789  "]

for val in test_values:
    # Thử chuyển sang int
    ket_qua_int, thanh_cong_int = chuyen_doi_an_toan(val.strip(), "int")
    print(f"'{val}' → int: {ket_qua_int if thanh_cong_int else 'THẤT BẠI'}")
    
    # Thử chuyển sang float
    ket_qua_float, thanh_cong_float = chuyen_doi_an_toan(val.strip(), "float")
    print(f"'{val}' → float: {ket_qua_float if thanh_cong_float else 'THẤT BẠI'}")
    print()

# PHẦN C: ỨNG DỤNG VỚI INPUT
print("\n" + "="*50)
print("PHẦN C: ỨNG DỤNG VỚI INPUT")
print("="*50)

print("\n--- Bài C1: Nhận và xử lý input ---")
# Simulation input (thay cho input() thực tế)
input_values = ["25", "8.5", "abc", "2024"]

for inp in input_values:
    print(f"\nGiả sử user nhập: '{inp}'")
    
    # Kiểm tra có phải số không
    if inp.strip().isdigit():
        so = int(inp)
        print(f"  → Đây là số nguyên: {so}")
        print(f"  → Số này {'chẵn' if so % 2 == 0 else 'lẻ'}")
    elif inp.strip().replace('.', '').isdigit() and inp.count('.') == 1:
        so_thuc = float(inp)
        print(f"  → Đây là số thực: {so_thuc}")
        print(f"  → Phần nguyên: {int(so_thuc)}")
    else:
        print(f"  → Đây là text, không phải số")

# PHẦN D: BOOLEAN CONVERSION
print("\n" + "="*50)
print("PHẦN D: CHUYỂN ĐỔI BOOLEAN")
print("="*50)

print("\n--- Bài D1: Truthiness trong Python ---")
cac_gia_tri = [
    0, 1, -1, 0.0, 3.14,
    "", "hello", " ",
    [], [1, 2], {},
    None, True, False
]

for gia_tri in cac_gia_tri:
    bool_value = bool(gia_tri)
    print(f"{str(gia_tri):10} → bool: {bool_value:5} (type: {type(gia_tri).__name__})")

# PHẦN E: ỨNG DỤNG THỰC TẾ
print("\n" + "="*50)
print("PHẦN E: ỨNG DỤNG THỰC TẾ")
print("="*50)

# Bài E1: Máy tính đơn giản với validation
print("\n--- Bài E1: Máy tính với validation ---")

def may_tinh_an_toan(so1_str, so2_str, phep_toan):
    """Máy tính với xử lý lỗi"""
    try:
        so1 = float(so1_str)
        so2 = float(so2_str)
        
        if phep_toan == "+":
            return so1 + so2, True
        elif phep_toan == "-":
            return so1 - so2, True
        elif phep_toan == "*":
            return so1 * so2, True
        elif phep_toan == "/":
            if so2 == 0:
                return "Không thể chia cho 0", False
            return so1 / so2, True
        else:
            return "Phép toán không hợp lệ", False
            
    except ValueError:
        return "Số không hợp lệ", False

# Test máy tính
test_cases = [
    ("10", "5", "+"),
    ("8.5", "2", "*"),
    ("15", "0", "/"),
    ("abc", "5", "+"),
    ("10", "3", "%")
]

for so1, so2, phep in test_cases:
    ket_qua, thanh_cong = may_tinh_an_toan(so1, so2, phep)
    print(f"{so1} {phep} {so2} = {ket_qua}")

# Bài E2: Xử lý dữ liệu học sinh
print("\n--- Bài E2: Xử lý dữ liệu học sinh ---")

# Dữ liệu thô từ file CSV giả lập
du_lieu_tho = [
    "Nguyen Van An,18,8.5",
    "Le Thi Binh,abc,7.2",  # Tuổi sai
    "Tran Van Duc,19,def",  # Điểm sai
    "Pham Thi Lan,20,9.0"
]

danh_sach_hoc_sinh = []

for dong in du_lieu_tho:
    cac_phan = dong.split(",")
    if len(cac_phan) == 3:
        ten = cac_phan[0].strip()
        tuoi_str = cac_phan[1].strip()
        diem_str = cac_phan[2].strip()
        
        # Chuyển đổi tuổi
        try:
            tuoi = int(tuoi_str)
            if tuoi < 0 or tuoi > 100:
                print(f"Cảnh báo: Tuổi {tuoi} của {ten} không hợp lý")
                continue
        except ValueError:
            print(f"Lỗi: Tuổi '{tuoi_str}' của {ten} không hợp lệ")
            continue
        
        # Chuyển đổi điểm
        try:
            diem = float(diem_str)
            if diem < 0 or diem > 10:
                print(f"Cảnh báo: Điểm {diem} của {ten} không hợp lý")
                continue
        except ValueError:
            print(f"Lỗi: Điểm '{diem_str}' của {ten} không hợp lệ")
            continue
        
        # Thêm vào danh sách nếu hợp lệ
        danh_sach_hoc_sinh.append({
            'ten': ten,
            'tuoi': tuoi,
            'diem': diem
        })

print(f"\nDữ liệu hợp lệ:")
for hs in danh_sach_hoc_sinh:
    print(f"- {hs['ten']}: {hs['tuoi']} tuổi, điểm {hs['diem']}")

# PHẦN F: CÂU HỎI VÀ BÀI TẬP
print("\n" + "="*50)
print("PHẦN F: CÂU HỎI TRẮC NGHIỆM")
print("="*50)

print("\nCâu 1: int('123') trả về gì?")
print("A) '123'   B) 123   C) 123.0   D) Lỗi")
print(f"Đáp án: {int('123')}")

print("\nCâu 2: float('3.14') trả về gì?")
print("A) 3.14   B) '3.14'   C) 3   D) Lỗi")
print(f"Đáp án: {float('3.14')}")

print("\nCâu 3: int(7.9) trả về gì?")
print("A) 7   B) 8   C) 7.9   D) Lỗi")
print(f"Đáp án: {int(7.9)}")

print("\nCâu 4: str(42) trả về gì?")
print("A) 42   B) '42'   C) 42.0   D) Lỗi")
print(f"Đáp án: '{str(42)}'")

print("\nCâu 5: bool('') trả về gì?")
print("A) True   B) False   C) ''   D) Lỗi")
print(f"Đáp án: {bool('')}")

# PHẦN G: THÁCH THỨC
print("\n" + "="*50)
print("PHẦN G: THÁCH THỨC")
print("="*50)

# Thách thức 1: Smart Input Parser
print("\n--- Thách thức 1: Smart Input Parser ---")

def phan_tich_input(user_input):
    """Phân tích input thông minh"""
    inp = user_input.strip()
    
    # Kiểm tra boolean
    if inp.lower() in ['true', 'yes', 'y', 'có', 'có']:
        return True, 'boolean'
    elif inp.lower() in ['false', 'no', 'n', 'không']:
        return False, 'boolean'
    
    # Kiểm tra số nguyên
    if inp.isdigit() or (inp.startswith('-') and inp[1:].isdigit()):
        return int(inp), 'integer'
    
    # Kiểm tra số thực
    try:
        if '.' in inp:
            return float(inp), 'float'
    except ValueError:
        pass
    
    # Mặc định là string
    return inp, 'string'

# Test với nhiều input
test_inputs = [
    "123", "-456", "3.14", "true", "false",
    "hello", "yes", "không", "0", "0.0"
]

for inp in test_inputs:
    gia_tri, kieu = phan_tich_input(inp)
    print(f"'{inp}' → {gia_tri} (type: {kieu})")

# Thách thức 2: Chuyển đổi hệ số
print("\n--- Thách thức 2: Chuyển đổi hệ số ---")

def chuyen_doi_he_so(so, he_nguon, he_dich):
    """Chuyển đổi giữa các hệ số"""
    # Chuyển về hệ 10 trước
    if he_nguon == 2:  # Binary
        so_he_10 = int(so, 2)
    elif he_nguon == 8:  # Octal
        so_he_10 = int(so, 8)
    elif he_nguon == 16:  # Hexadecimal
        so_he_10 = int(so, 16)
    else:  # Decimal
        so_he_10 = int(so)
    
    # Chuyển sang hệ đích
    if he_dich == 2:
        return bin(so_he_10)[2:]  # Bỏ '0b'
    elif he_dich == 8:
        return oct(so_he_10)[2:]  # Bỏ '0o'
    elif he_dich == 16:
        return hex(so_he_10)[2:]  # Bỏ '0x'
    else:
        return str(so_he_10)

# Test chuyển đổi hệ số
print(f"Số 10 (hệ 10) → hệ 2: {chuyen_doi_he_so('10', 10, 2)}")
print(f"Số 1010 (hệ 2) → hệ 10: {chuyen_doi_he_so('1010', 2, 10)}")
print(f"Số 255 (hệ 10) → hệ 16: {chuyen_doi_he_so('255', 10, 16)}")
print(f"Số FF (hệ 16) → hệ 10: {chuyen_doi_he_so('FF', 16, 10)}")

print("\n" + "="*50)
print("HOÀN THÀNH BÀI TẬP CHUYỂN ĐỔI KIỂU!")
print("Bạn đã học:")
print("1. Chuyển đổi cơ bản (int, float, str)")
print("2. Xử lý lỗi ValueError")
print("3. Validation input an toàn")
print("4. Boolean conversion và truthiness")
print("5. Ứng dụng thực tế")
print("6. Chuyển đổi hệ số")
print("="*50) 