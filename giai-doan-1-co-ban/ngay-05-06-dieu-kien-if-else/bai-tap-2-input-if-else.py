# ===============================================
# NGÀY 5-6: INPUT() KẾT HỢP IF/ELSE
# Mục tiêu: Tạo ứng dụng tương tác với người dùng
# ===============================================

print("=== INPUT() KẾT HỢP IF/ELSE ===")
print("Tạo ứng dụng tương tác thực tế!")
print()

# ===============================================
# PHẦN A: INPUT VÀ IF CƠ BẢN
# ===============================================
print("--- PHẦN A: INPUT VÀ IF CƠ BẢN ---")
print()

# A1. Kiểm tra tuổi đơn giản
print("A1. Kiểm tra tuổi:")
print("Code mẫu:")
print('''
tuoi = int(input("Nhập tuổi của bạn: "))
if tuoi >= 18:
    print("Bạn đã trưởng thành!")
else:
    print("Bạn vẫn còn nhỏ.")
''')
print()

# A2. Kiểm tra điểm số
print("A2. Kiểm tra điểm số:")
print("Code mẫu:")
print('''
diem = float(input("Nhập điểm của bạn: "))
if diem >= 5:
    print(f"Điểm {diem}: ĐẬU")
else:
    print(f"Điểm {diem}: RỚT")
''')
print()

# A3. Đăng nhập đơn giản
print("A3. Đăng nhập đơn giản:")
print("Code mẫu:")
print('''
ten_dang_nhap = input("Tên đăng nhập: ")
mat_khau = input("Mật khẩu: ")

if ten_dang_nhap == "admin" and mat_khau == "123456":
    print("Đăng nhập thành công!")
else:
    print("Sai tên đăng nhập hoặc mật khẩu!")
''')
print()

# BÀI TẬP TỰ LÀM A:
print("*** BÀI TẬP TỰ LÀM A ***")
print("Viết code cho các tình huống sau:")
print("1. Nhập tên, nếu tên là 'Python' thì chào mừng đặc biệt")
print("2. Nhập số, kiểm tra chẵn/lẻ")
print("3. Nhập mật khẩu, kiểm tra độ dài >= 6 ký tự")
print()

# ===============================================
# PHẦN B: CHUYỂN ĐỔI KIỂU DỮ LIỆU AN TOÀN
# ===============================================
print("--- PHẦN B: CHUYỂN ĐỔI KIỂU AN TOÀN ---")
print()

# B1. Kiểm tra số hợp lệ
print("B1. Kiểm tra số hợp lệ:")
print("Code mẫu:")
print('''
so_nhap = input("Nhập một số: ")
if so_nhap.isdigit():
    so = int(so_nhap)
    if so > 0:
        print(f"{so} là số dương")
    else:
        print(f"{so} là số âm hoặc 0")
else:
    print("Bạn chưa nhập đúng định dạng số!")
''')
print()

# B2. Kiểm tra số thực
print("B2. Kiểm tra số thực:")
print("Code mẫu:")
print('''
try:
    so_thuc = float(input("Nhập số thực: "))
    if so_thuc >= 0:
        print(f"Căn bậc 2 của {so_thuc} là {so_thuc ** 0.5:.2f}")
    else:
        print("Không thể tính căn bậc 2 của số âm!")
except:
    print("Định dạng số không hợp lệ!")
''')
print()

# BÀI TẬP TỰ LÀM B:
print("*** BÀI TẬP TỰ LÀM B ***")
print("1. Nhập tuổi, kiểm tra hợp lệ (0-120) trước khi phân loại")
print("2. Nhập điểm, kiểm tra hợp lệ (0-10) trước khi xếp loại")
print("3. Nhập số điện thoại, kiểm tra chỉ chứa số và đủ 10 ký tự")
print()

# ===============================================
# PHẦN C: ỨNG DỤNG THỰC TẾ - CALCULATOR
# ===============================================
print("--- PHẦN C: CALCULATOR NÂNG CAO ---")
print()

print("C1. Calculator với xử lý lỗi:")
print("Code mẫu:")
print('''
print("=== CALCULATOR NÂNG CAO ===")

# Nhập số thứ nhất
try:
    so_1 = float(input("Nhập số thứ nhất: "))
except:
    print("Số thứ nhất không hợp lệ!")
    exit()

# Nhập phép toán
phep_toan = input("Nhập phép toán (+, -, *, /, %, **): ")
if phep_toan not in ["+", "-", "*", "/", "%", "**"]:
    print("Phép toán không hợp lệ!")
    exit()

# Nhập số thứ hai
try:
    so_2 = float(input("Nhập số thứ hai: "))
except:
    print("Số thứ hai không hợp lệ!")
    exit()

# Tính toán
if phep_toan == "+":
    ket_qua = so_1 + so_2
elif phep_toan == "-":
    ket_qua = so_1 - so_2
elif phep_toan == "*":
    ket_qua = so_1 * so_2
elif phep_toan == "/":
    if so_2 != 0:
        ket_qua = so_1 / so_2
    else:
        print("Không thể chia cho 0!")
        exit()
elif phep_toan == "%":
    if so_2 != 0:
        ket_qua = so_1 % so_2
    else:
        print("Không thể chia cho 0!")
        exit()
elif phep_toan == "**":
    ket_qua = so_1 ** so_2

print(f"Kết quả: {so_1} {phep_toan} {so_2} = {ket_qua}")
''')
print()

# ===============================================
# PHẦN D: HỆ THỐNG ĐÁNH GIÁ HỌC TẬP
# ===============================================
print("--- PHẦN D: HỆ THỐNG ĐÁNH GIÁ HỌC TẬP ---")
print()

print("D1. Hệ thống chấm điểm tự động:")
print("Code mẫu:")
print('''
print("=== HỆ THỐNG ĐÁNH GIÁ HỌC TẬP ===")

# Nhập thông tin học sinh
ten_hs = input("Tên học sinh: ")
lop = input("Lớp: ")

# Nhập điểm các môn
print("Nhập điểm các môn (thang điểm 10):")

try:
    diem_toan = float(input("Toán: "))
    diem_ly = float(input("Lý: "))
    diem_hoa = float(input("Hóa: "))
    diem_van = float(input("Văn: "))
    diem_anh = float(input("Anh: "))
except:
    print("Điểm phải là số!")
    exit()

# Kiểm tra điểm hợp lệ
danh_sach_diem = [diem_toan, diem_ly, diem_hoa, diem_van, diem_anh]
ten_mon = ["Toán", "Lý", "Hóa", "Văn", "Anh"]

for i, diem in enumerate(danh_sach_diem):
    if diem < 0 or diem > 10:
        print(f"Điểm {ten_mon[i]} không hợp lệ (0-10)!")
        exit()

# Tính điểm trung bình
diem_tb = sum(danh_sach_diem) / len(danh_sach_diem)

# Xếp loại
if diem_tb >= 9:
    xep_loai = "Xuất sắc"
elif diem_tb >= 8:
    xep_loai = "Giỏi"
elif diem_tb >= 6.5:
    xep_loai = "Khá"
elif diem_tb >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

# Kiểm tra điều kiện lên lớp
mon_duoi_5 = 0
for diem in danh_sach_diem:
    if diem < 5:
        mon_duoi_5 += 1

if mon_duoi_5 == 0:
    ket_qua = "ĐẬU - Lên lớp"
elif mon_duoi_5 <= 2 and diem_tb >= 5:
    ket_qua = "ĐẬU - Lên lớp (có điều kiện)"
else:
    ket_qua = "RỚT - Ở lại lớp"

# In kết quả
print("\\n" + "="*40)
print("        BẢNG ĐIỂM HỌC TẬP")
print("="*40)
print(f"Học sinh: {ten_hs}")
print(f"Lớp: {lop}")
print("-"*40)
for i, diem in enumerate(danh_sach_diem):
    print(f"{ten_mon[i]:<10}: {diem:>5.1f}")
print("-"*40)
print(f"Điểm TB : {diem_tb:>5.1f}")
print(f"Xếp loại: {xep_loai}")
print(f"Kết quả : {ket_qua}")
print("="*40)
''')
print()

# ===============================================
# PHẦN E: GAME ĐOÁN SỐ NÂNG CAO
# ===============================================
print("--- PHẦN E: GAME ĐOÁN SỐ NÂNG CAO ---")
print()

print("E1. Game đoán số với gợi ý:")
print("Code mẫu:")
print('''
import random

print("=== GAME ĐOÁN SỐ ===")
print("Tôi đã nghĩ ra một số từ 1 đến 100")
print("Bạn có 7 lượt đoán!")

so_bi_mat = random.randint(1, 100)
luot_doan = 0
max_luot = 7

while luot_doan < max_luot:
    luot_doan += 1
    print(f"\\nLượt {luot_doan}/{max_luot}")
    
    try:
        so_doan = int(input("Nhập số bạn đoán: "))
    except:
        print("Vui lòng nhập một số nguyên!")
        luot_doan -= 1  # Không tính lượt này
        continue
    
    if so_doan < 1 or so_doan > 100:
        print("Số phải từ 1 đến 100!")
        luot_doan -= 1  # Không tính lượt này
        continue
    
    if so_doan == so_bi_mat:
        print(f"🎉 CHÚC MỪNG! Bạn đã đoán đúng số {so_bi_mat}!")
        print(f"Bạn đã thắng trong {luot_doan} lượt!")
        break
    elif so_doan < so_bi_mat:
        khoang_cach = so_bi_mat - so_doan
        if khoang_cach <= 5:
            print("Rất gần rồi! Số cần tìm LỚN HƠN")
        elif khoang_cach <= 15:
            print("Gần rồi! Số cần tìm LỚN HƠN")
        else:
            print("Còn xa! Số cần tìm LỚN HƠN NHIỀU")
    else:
        khoang_cach = so_doan - so_bi_mat
        if khoang_cach <= 5:
            print("Rất gần rồi! Số cần tìm NHỎ HƠN")
        elif khoang_cach <= 15:
            print("Gần rồi! Số cần tìm NHỎ HƠN")
        else:
            print("Còn xa! Số cần tìm NHỎ HƠN NHIỀU")
    
    if luot_doan == max_luot:
        print(f"\\n😞 Hết lượt! Số bí mật là {so_bi_mat}")
        print("Chúc bạn may mắn lần sau!")
''')
print()

# ===============================================
# PHẦN F: HỆ THỐNG QUẢN LÝ THƯ VIỆN MINI
# ===============================================
print("--- PHẦN F: HỆ THỐNG THƯ VIỆN MINI ---")
print()

print("F1. Quản lý mượn/trả sách:")
print("Code mẫu:")
print('''
print("=== HỆ THỐNG THƯ VIỆN MINI ===")

# Dữ liệu sách có sẵn
sach_co_san = {
    "python": {"ten": "Học Python Cơ Bản", "tac_gia": "Nguyễn Văn A", "so_luong": 5},
    "java": {"ten": "Java Từ Đầu", "tac_gia": "Trần Thị B", "so_luong": 3},
    "web": {"ten": "Lập Trình Web", "tac_gia": "Lê Văn C", "so_luong": 2},
    "ai": {"ten": "Trí Tuệ Nhân Tạo", "tac_gia": "Phạm Thị D", "so_luong": 1}
}

print("Sách có trong thư viện:")
for ma_sach, thong_tin in sach_co_san.items():
    print(f"- {ma_sach}: {thong_tin['ten']} ({thong_tin['so_luong']} cuốn)")

# Nhập thông tin độc giả
ten_doc_gia = input("\\nTên độc giả: ")
ma_sinh_vien = input("Mã sinh viên: ")

# Kiểm tra mã sinh viên hợp lệ
if not ma_sinh_vien.isdigit() or len(ma_sinh_vien) != 8:
    print("Mã sinh viên phải là 8 chữ số!")
    exit()

# Chọn thao tác
print("\\nChọn thao tác:")
print("1. Mượn sách")
print("2. Trả sách")
print("3. Xem thông tin sách")

lua_chon = input("Nhập lựa chọn (1/2/3): ")

if lua_chon == "1":
    ma_sach = input("Nhập mã sách muốn mượn: ").lower()
    
    if ma_sach in sach_co_san:
        if sach_co_san[ma_sach]["so_luong"] > 0:
            sach_co_san[ma_sach]["so_luong"] -= 1
            print(f"\\n✅ Mượn thành công!")
            print(f"Sách: {sach_co_san[ma_sach]['ten']}")
            print(f"Độc giả: {ten_doc_gia}")
            print(f"Còn lại: {sach_co_san[ma_sach]['so_luong']} cuốn")
        else:
            print("\\n❌ Sách đã hết!")
    else:
        print("\\n❌ Không tìm thấy sách!")

elif lua_chon == "2":
    ma_sach = input("Nhập mã sách muốn trả: ").lower()
    
    if ma_sach in sach_co_san:
        sach_co_san[ma_sach]["so_luong"] += 1
        print(f"\\n✅ Trả sách thành công!")
        print(f"Sách: {sach_co_san[ma_sach]['ten']}")
        print(f"Số lượng hiện tại: {sach_co_san[ma_sach]['so_luong']} cuốn")
    else:
        print("\\n❌ Không tìm thấy sách!")

elif lua_chon == "3":
    ma_sach = input("Nhập mã sách cần xem: ").lower()
    
    if ma_sach in sach_co_san:
        thong_tin = sach_co_san[ma_sach]
        print(f"\\n📖 Thông tin sách:")
        print(f"Tên: {thong_tin['ten']}")
        print(f"Tác giả: {thong_tin['tac_gia']}")
        print(f"Số lượng: {thong_tin['so_luong']} cuốn")
        
        if thong_tin['so_luong'] > 0:
            print("Trạng thái: Có thể mượn")
        else:
            print("Trạng thái: Hết sách")
    else:
        print("\\n❌ Không tìm thấy sách!")

else:
    print("\\n❌ Lựa chọn không hợp lệ!")
''')
print()

# ===============================================
# PHẦN G: BÀI TẬP THÁCH THỨC VỚI INPUT
# ===============================================
print("--- PHẦN G: BÀI TẬP THÁCH THỨC ---")
print()

# G1. Thách thức: ATM Machine
print("G1. Thách thức: Máy ATM")
print("Yêu cầu: Tạo chương trình mô phỏng máy ATM với các chức năng:")
print("- Kiểm tra số dư")
print("- Rút tiền (kiểm tra số dư, mệnh giá)")
print("- Chuyển khoản")
print("- Đổi mật khẩu")
print("- Xử lý lỗi đầy đủ")
print()

# G2. Thách thức: Restaurant Order System
print("G2. Thách thức: Hệ thống đặt món")
print("Yêu cầu: Tạo chương trình đặt món ăn với:")
print("- Menu có giá")
print("- Tính tổng tiền")
print("- Áp dụng giảm giá theo điều kiện")
print("- In hóa đơn đẹp")
print()

# G3. Thách thức: Student Management
print("G3. Thách thức: Quản lý sinh viên")
print("Yêu cầu: Chương trình quản lý thông tin sinh viên:")
print("- Thêm/sửa/xóa sinh viên")
print("- Tính điểm trung bình")
print("- Xếp loại")
print("- Tìm kiếm sinh viên")
print("- Thống kê theo xếp loại")
print()

# BÀI TẬP TỰ LÀM G:
print("*** BÀI TẬP TỰ LÀM G ***")
print("Chọn 1 trong 3 thách thức trên và code hoàn chỉnh!")
print()

# ===============================================
# PHẦN H: TIPS VÀ BEST PRACTICES
# ===============================================
print("--- PHẦN H: TIPS VÀ BEST PRACTICES ---")
print()

print("H1. Xử lý Input an toàn:")
print('''
# ❌ Không nên:
tuoi = int(input("Tuổi: "))  # Có thể crash

# ✅ Nên:
try:
    tuoi = int(input("Tuổi: "))
except ValueError:
    print("Vui lòng nhập số!")
    tuoi = 0
''')
print()

print("H2. Kiểm tra input trống:")
print('''
# ❌ Không nên:
ten = input("Tên: ")
if ten == "":
    print("Chưa nhập tên")

# ✅ Nên (ngắn gọn hơn):
ten = input("Tên: ").strip()  # Xóa khoảng trắng thừa
if not ten:
    print("Chưa nhập tên")
''')
print()

print("H3. Validation đầy đủ:")
print('''
def nhap_tuoi():
    while True:
        try:
            tuoi = int(input("Nhập tuổi (0-120): "))
            if 0 <= tuoi <= 120:
                return tuoi
            else:
                print("Tuổi phải từ 0 đến 120!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

tuoi = nhap_tuoi()  # Đảm bảo tuổi hợp lệ
''')
print()

print("H4. Format output đẹp:")
print('''
# In bảng đẹp
print(f"{'Tên':<15} {'Tuổi':>5} {'Điểm':>8}")
print("-" * 30)
print(f"{'Nguyễn Văn A':<15} {20:>5} {8.5:>8.1f}")
''')
print()

# ===============================================
# PHẦN I: DEBUG VÀ TROUBLESHOOTING
# ===============================================
print("--- PHẦN I: DEBUG VÀ TROUBLESHOOTING ---")
print()

print("I1. Lỗi thường gặp với input():")
print()
print("Lỗi 1: ValueError khi chuyển đổi")
print("Code lỗi: so = int(input('Số: '))")
print("Nguyên nhân: User nhập chữ thay vì số")
print("Giải pháp: Dùng try-except")
print()

print("Lỗi 2: So sánh string và number")
print("Code lỗi: if input('Số: ') > 5")
print("Nguyên nhân: input() trả về string")
print("Giải pháp: Chuyển đổi kiểu trước khi so sánh")
print()

print("Lỗi 3: Khoảng trắng thừa")
print("Code lỗi: if input('Tên: ') == 'Nam'  # User nhập ' Nam '")
print("Giải pháp: Dùng .strip() để xóa khoảng trắng")
print()

print("I2. Kỹ thuật debug:")
print('''
# Debug với print()
user_input = input("Nhập gì đó: ")
print(f"Debug: [{user_input}]")  # Thấy được khoảng trắng
print(f"Length: {len(user_input)}")

# Debug với type()
print(f"Type: {type(user_input)}")
''')
print()

# ===============================================
# KẾT LUẬN
# ===============================================
print("=== KẾT LUẬN PHẦN 2 ===")
print()
print("Bạn đã nắm vững:")
print("✓ Kết hợp input() với if/else")
print("✓ Xử lý lỗi đầu vào (try-except)")
print("✓ Validation dữ liệu")
print("✓ Tạo ứng dụng tương tác hoàn chỉnh")
print("✓ Debug và xử lý lỗi")
print("✓ Best practices khi làm việc với input")
print()
print("Tiếp theo: Vòng lặp và cấu trúc dữ liệu!")
print("=" * 50) 