# ===============================================
# NGÀY 5-6: BÀI TẬP IF/ELSE CƠ BẢN
# Mục tiêu: Nắm vững cấu trúc điều kiện if/else
# ===============================================

print("=== BÀI TẬP IF/ELSE CƠ BẢN ===")
print("Hôm nay chúng ta sẽ học cách ra quyết định trong code!")
print()

# ===============================================
# PHẦN A: IF CƠ BẢN
# ===============================================
print("--- PHẦN A: IF CƠ BẢN ---")
print()

# A1. Kiểm tra số dương
print("A1. Kiểm tra số dương:")
so = 5
if so > 0:
    print(f"{so} là số dương")
print()

# A2. Kiểm tra tuổi người lớn
print("A2. Kiểm tra tuổi người lớn:")
tuoi = 20
if tuoi >= 18:
    print(f"Tuổi {tuoi}: Bạn đã trưởng thành!")
print()

# A3. Kiểm tra mật khẩu
print("A3. Kiểm tra mật khẩu:")
mat_khau = "python123"
if mat_khau == "python123":
    print("Đăng nhập thành công!")
print()

# BÀI TẬP TỰ LÀM A:
print("*** BÀI TẬP TỰ LÀM A ***")
print("1. Tạo biến diem = 8, kiểm tra xem >= 5 thì in 'Đạt'")
print("2. Tạo biến nhiet_do = 25, kiểm tra xem >= 30 thì in 'Nóng'")
print("3. Tạo biến ten = 'Nam', kiểm tra xem == 'Nam' thì in 'Xin chào Nam!'")
print()

# ===============================================
# PHẦN B: IF-ELSE CƠ BẢN
# ===============================================
print("--- PHẦN B: IF-ELSE CƠ BẢN ---")
print()

# B1. Kiểm tra chẵn lẻ
print("B1. Kiểm tra chẵn lẻ:")
so = 7
if so % 2 == 0:
    print(f"{so} là số chẵn")
else:
    print(f"{so} là số lẻ")
print()

# B2. So sánh hai số
print("B2. So sánh hai số:")
a = 10
b = 15
if a > b:
    print(f"{a} lớn hơn {b}")
else:
    print(f"{a} không lớn hơn {b}")
print()

# B3. Kiểm tra điểm đậu/rớt
print("B3. Kiểm tra điểm đậu/rớt:")
diem = 4.5
if diem >= 5:
    print(f"Điểm {diem}: ĐẬU")
else:
    print(f"Điểm {diem}: RỚT")
print()

# BÀI TẬP TỰ LÀM B:
print("*** BÀI TẬP TỰ LÀM B ***")
print("1. Kiểm tra số âm/dương với so = -3")
print("2. Kiểm tra tuổi trẻ em/người lớn với tuoi = 16")
print("3. Kiểm tra giá rẻ/đắt với gia = 50000 (ngưỡng 100000)")
print()

# ===============================================
# PHẦN C: IF-ELIF-ELSE
# ===============================================
print("--- PHẦN C: IF-ELIF-ELSE ---")
print()

# C1. Phân loại điểm học tập
print("C1. Phân loại điểm học tập:")
diem = 8.5
if diem >= 9:
    print(f"Điểm {diem}: Xuất sắc")
elif diem >= 7:
    print(f"Điểm {diem}: Khá")
elif diem >= 5:
    print(f"Điểm {diem}: Trung bình")
else:
    print(f"Điểm {diem}: Yếu")
print()

# C2. Phân loại BMI
print("C2. Phân loại BMI:")
bmi = 22.5
if bmi < 18.5:
    print(f"BMI {bmi}: Thiếu cân")
elif bmi < 25:
    print(f"BMI {bmi}: Bình thường")
elif bmi < 30:
    print(f"BMI {bmi}: Thừa cân")
else:
    print(f"BMI {bmi}: Béo phì")
print()

# C3. Phân loại tháng trong năm
print("C3. Phân loại tháng trong năm:")
thang = 6
if thang in [12, 1, 2]:
    print(f"Tháng {thang}: Mùa đông")
elif thang in [3, 4, 5]:
    print(f"Tháng {thang}: Mùa xuân")
elif thang in [6, 7, 8]:
    print(f"Tháng {thang}: Mùa hè")
else:
    print(f"Tháng {thang}: Mùa thu")
print()

# BÀI TẬP TỰ LÀM C:
print("*** BÀI TẬP TỰ LÀM C ***")
print("1. Phân loại tuổi: <13 (trẻ em), 13-19 (thiếu niên), 20-59 (người lớn), >=60 (cao tuổi)")
print("2. Phân loại nhiệt độ: <0 (băng giá), 0-15 (lạnh), 16-25 (mát), 26-35 (ấm), >35 (nóng)")
print("3. Phân loại thu nhập: <5tr (thấp), 5-15tr (trung bình), 15-30tr (khá), >30tr (cao)")
print()

# ===============================================
# PHẦN D: TOÁN TỬ LOGIC AND, OR, NOT
# ===============================================
print("--- PHẦN D: TOÁN TỬ LOGIC ---")
print()

# D1. Toán tử AND
print("D1. Toán tử AND:")
tuoi = 25
luong = 20000000
if tuoi >= 18 and luong >= 15000000:
    print("Đủ điều kiện vay ngân hàng")
else:
    print("Không đủ điều kiện vay ngân hàng")
print()

# D2. Toán tử OR
print("D2. Toán tử OR:")
diem_toan = 6
diem_ly = 8
if diem_toan >= 7 or diem_ly >= 7:
    print("Có ít nhất 1 môn đạt giỏi")
else:
    print("Chưa có môn nào đạt giỏi")
print()

# D3. Toán tử NOT
print("D3. Toán tử NOT:")
la_hoc_sinh = True
if not la_hoc_sinh:
    print("Không phải học sinh")
else:
    print("Là học sinh")
print()

# D4. Kết hợp nhiều toán tử
print("D4. Kết hợp nhiều toán tử:")
tuoi = 16
co_bang_lai = False
if tuoi >= 18 and co_bang_lai:
    print("Được phép lái xe")
elif tuoi >= 16 and not co_bang_lai:
    print("Có thể học lái xe")
else:
    print("Chưa đủ tuổi học lái xe")
print()

# BÀI TẬP TỰ LÀM D:
print("*** BÀI TẬP TỰ LÀM D ***")
print("1. Kiểm tra học bổng: điểm >= 8 AND gia đình khó khăn")
print("2. Kiểm tra thi đỗ: toán >= 5 OR văn >= 5")
print("3. Kiểm tra vào công viên: tuổi <= 12 OR tuổi >= 60 (miễn phí)")
print()

# ===============================================
# PHẦN E: IF LỒNG NHAU (NESTED IF)
# ===============================================
print("--- PHẦN E: IF LỒNG NHAU ---")
print()

# E1. Kiểm tra đi học
print("E1. Kiểm tra đi học:")
troi_mua = False
co_xe = True

if not troi_mua:
    print("Trời không mưa")
    if co_xe:
        print("  → Đi xe đến trường")
    else:
        print("  → Đi bộ đến trường")
else:
    print("Trời mưa")
    if co_xe:
        print("  → Đi xe cẩn thận")
    else:
        print("  → Ở nhà học online")
print()

# E2. Hệ thống đăng nhập
print("E2. Hệ thống đăng nhập:")
username = "admin"
password = "123456"
is_active = True

if username == "admin":
    print("Username đúng")
    if password == "123456":
        print("  Password đúng")
        if is_active:
            print("    → Đăng nhập thành công!")
        else:
            print("    → Tài khoản bị khóa")
    else:
        print("  → Password sai")
else:
    print("→ Username không tồn tại")
print()

# BÀI TẬP TỰ LÀM E:
print("*** BÀI TẬP TỰ LÀM E ***")
print("1. Kiểm tra mua hàng: có tiền → kiểm tra hàng còn → quyết định mua")
print("2. Xét tuyển đại học: điểm >= 20 → kiểm tra nguyện vọng → kết quả")
print()

# ===============================================
# PHẦN F: SỬ DỤNG IN TRONG IF
# ===============================================
print("--- PHẦN F: SỬ DỤNG IN TRONG IF ---")
print()

# F1. Kiểm tra ngày trong tuần
print("F1. Kiểm tra ngày trong tuần:")
ngay = "thứ 7"
if ngay in ["thứ 7", "chủ nhật"]:
    print(f"{ngay}: Cuối tuần - Nghỉ ngơi!")
else:
    print(f"{ngay}: Ngày thường - Đi làm/học")
print()

# F2. Kiểm tra môn học yêu thích
print("F2. Kiểm tra môn học yêu thích:")
mon_hoc = "toán"
mon_khoa_hoc = ["toán", "lý", "hóa", "sinh"]
if mon_hoc in mon_khoa_hoc:
    print(f"{mon_hoc} là môn khoa học tự nhiên")
else:
    print(f"{mon_hoc} không phải môn khoa học tự nhiên")
print()

# F3. Kiểm tra ký tự đặc biệt
print("F3. Kiểm tra ký tự đặc biệt:")
ky_tu = "@"
ky_tu_dac_biet = "!@#$%^&*()"
if ky_tu in ky_tu_dac_biet:
    print(f"'{ky_tu}' là ký tự đặc biệt")
else:
    print(f"'{ky_tu}' không phải ký tự đặc biệt")
print()

# BÀI TẬP TỰ LÀM F:
print("*** BÀI TẬP TỰ LÀM F ***")
print("1. Kiểm tra màu cơ bản: màu in ['đỏ', 'xanh', 'vàng']")
print("2. Kiểm tra số may mắn: số in [7, 8, 9]")
print("3. Kiểm tra trình duyệt: browser in ['chrome', 'firefox', 'edge']")
print()

# ===============================================
# PHẦN G: IF VỚI CHUỖI
# ===============================================
print("--- PHẦN G: IF VỚI CHUỖI ---")
print()

# G1. Kiểm tra tên bắt đầu
print("G1. Kiểm tra tên bắt đầu:")
ten = "Nguyễn Văn Nam"
if ten.startswith("Nguyễn"):
    print(f"Họ Nguyễn: {ten}")
else:
    print(f"Không họ Nguyễn: {ten}")
print()

# G2. Kiểm tra email hợp lệ
print("G2. Kiểm tra email hợp lệ:")
email = "nam@gmail.com"
if "@" in email and email.endswith(".com"):
    print(f"Email hợp lệ: {email}")
else:
    print(f"Email không hợp lệ: {email}")
print()

# G3. Kiểm tra mật khẩu mạnh
print("G3. Kiểm tra mật khẩu mạnh:")
password = "Python123!"
if len(password) >= 8 and password.isupper() == False and password.islower() == False:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
print()

# G4. Kiểm tra chuỗi rỗng
print("G4. Kiểm tra chuỗi rỗng:")
ten_input = ""
if ten_input:  # Cách ngắn gọn
    print(f"Tên: {ten_input}")
else:
    print("Chưa nhập tên")

# Hoặc cách đầy đủ
if ten_input != "":
    print(f"Tên (cách 2): {ten_input}")
else:
    print("Chưa nhập tên (cách 2)")
print()

# BÀI TẬP TỰ LÀM G:
print("*** BÀI TẬP TỰ LÀM G ***")
print("1. Kiểm tra số điện thoại: bắt đầu '0' và dài 10-11 ký tự")
print("2. Kiểm tra file Python: kết thúc '.py'")
print("3. Kiểm tra tên user: không chứa khoảng trắng và >= 3 ký tự")
print()

# ===============================================
# PHẦN H: THỰC HÀNH TƯƠNG TÁC
# ===============================================
print("--- PHẦN H: THỰC HÀNH TƯƠNG TÁC ---")
print("(Chạy từng đoạn code để test)")
print()

# H1. Máy tính đơn giản
print("H1. Code máy tính đơn giản:")
print('''
# Ví dụ test:
a = 10
b = 5
phep_toan = "+"

if phep_toan == "+":
    print(f"{a} + {b} = {a + b}")
elif phep_toan == "-":
    print(f"{a} - {b} = {a - b}")
elif phep_toan == "*":
    print(f"{a} * {b} = {a * b}")
elif phep_toan == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Không thể chia cho 0")
else:
    print("Phép toan không hợp lệ")
''')

# H2. Game đoán số
print("H2. Code game đoán số:")
print('''
# Ví dụ test:
so_bi_mat = 7
so_doan = 5

if so_doan == so_bi_mat:
    print("Chúc mừng! Bạn đoán đúng!")
elif so_doan < so_bi_mat:
    print("Số bạn đoán nhỏ hơn số bí mật")
else:
    print("Số bạn đoán lớn hơn số bí mật")
''')

# H3. Hệ thống chấm công
print("H3. Code hệ thống chấm công:")
print('''
# Ví dụ test:
gio_vao = 8
gio_ra = 17
gio_lam_chuan = 8

gio_lam_thuc_te = gio_ra - gio_vao

if gio_lam_thuc_te >= gio_lam_chuan:
    gio_tang_ca = gio_lam_thuc_te - gio_lam_chuan
    print(f"Làm đủ giờ. Tăng ca: {gio_tang_ca} giờ")
else:
    gio_thieu = gio_lam_chuan - gio_lam_thuc_te
    print(f"Thiếu {gio_thieu} giờ làm việc")
''')
print()

# ===============================================
# PHẦN I: BÀI TẬP THÁCH THỨC
# ===============================================
print("--- PHẦN I: BÀI TẬP THÁCH THỨC ---")
print()

# I1. Thách thức: Kiểm tra năm nhuận
print("I1. Thách thức: Kiểm tra năm nhuận")
nam = 2024
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận")
else:
    print(f"Năm {nam} không phải năm nhuận")
print()

# I2. Thách thức: Phân loại tam giác
print("I2. Thách thức: Phân loại tam giác")
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không tạo thành tam giác")
print()

# I3. Thách thức: Máy bán nước tự động
print("I3. Thách thức: Máy bán nước tự động")
tien_dua = 15000
gia_nuoc = 12000
tien_thoi = tien_dua - gia_nuoc

if tien_dua >= gia_nuoc:
    print("Giao dịch thành công!")
    if tien_thoi > 0:
        # Tính tiền thối
        to_5000 = tien_thoi // 5000
        to_2000 = (tien_thoi % 5000) // 2000
        to_1000 = (tien_thoi % 5000 % 2000) // 1000
        print(f"Tiền thối: {tien_thoi}đ")
        if to_5000 > 0:
            print(f"  - {to_5000} tờ 5.000đ")
        if to_2000 > 0:
            print(f"  - {to_2000} tờ 2.000đ")
        if to_1000 > 0:
            print(f"  - {to_1000} tờ 1.000đ")
    else:
        print("Vừa đủ tiền!")
else:
    print(f"Thiếu {gia_nuoc - tien_dua}đ")
print()

# ===============================================
# PHẦN J: QUIZ KIỂM TRA
# ===============================================
print("--- PHẦN J: QUIZ KIỂM TRA ---")
print()

print("1. Kết quả của đoạn code sau là gì?")
print("   x = 5")
print("   if x > 3:")
print("       print('A')")
print("   else:")
print("       print('B')")
print("   Đáp án: A")
print()

print("2. Điều kiện nào đúng với x = 10?")
print("   A. x > 5 and x < 15  → True")
print("   B. x > 15 or x < 5   → False")
print("   C. not x == 10       → False")
print("   Đáp án: A")
print()

print("3. Code nào kiểm tra số chẵn đúng?")
print("   A. if x % 2 == 0:")
print("   B. if x / 2 == 0:")
print("   C. if x % 2 == 1:")
print("   Đáp án: A")
print()

print("4. 'Python' in ['Java', 'Python', 'C++'] trả về gì?")
print("   Đáp án: True")
print()

print("5. Sửa lỗi trong code:")
print("   if x = 5:  # Lỗi: dùng = thay vì ==")
print("       print('Five')")
print("   Sửa: if x == 5:")
print()

# ===============================================
# KẾT LUẬN VÀ BƯỚC TIẾP THEO
# ===============================================
print("=== KẾT LUẬN PHẦN 1 ===")
print()
print("Bạn đã học được:")
print("✓ If cơ bản")
print("✓ If-else")
print("✓ If-elif-else")
print("✓ Toán tử logic (and, or, not)")
print("✓ If lồng nhau")
print("✓ Sử dụng 'in' trong if")
print("✓ If với chuỗi")
print("✓ Các thách thức thực tế")
print()
print("Tiếp theo: Thực hành với input() và xây dựng ứng dụng hoàn chỉnh!")
print("=" * 50) 