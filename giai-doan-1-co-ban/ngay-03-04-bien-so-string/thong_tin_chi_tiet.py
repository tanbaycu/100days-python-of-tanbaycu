# thong_tin_chi_tiet.py - Form thông tin với validation
# File cần nộp cho ngày 3-4

print("FORM THÔNG TIN CHI TIẾT")
print("=" * 40)

# Thu thập thông tin cơ bản
print("Vui lòng nhập thông tin của bạn:")

# Nhập và validate tên
while True:
    ho_ten = input("Họ và tên: ").strip()
    if ho_ten and len(ho_ten) >= 2:
        # Chuẩn hóa tên
        ho_ten = " ".join(ho_ten.split()).title()
        break
    else:
        print("Tên phải có ít nhất 2 ký tự. Vui lòng nhập lại!")

# Nhập và validate tuổi
while True:
    try:
        tuoi = int(input("Tuổi: "))
        if 10 <= tuoi <= 100:
            break
        else:
            print("Tuổi phải từ 10-100. Vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

# Nhập và validate email
while True:
    email = input("Email: ").strip().lower()
    if "@" in email and "." in email and len(email) >= 5:
        break
    else:
        print("Email không hợp lệ. Vui lòng nhập lại!")

# Nhập số điện thoại
while True:
    sdt = input("Số điện thoại: ").strip()
    # Loại bỏ dấu gạch ngang và space
    sdt_clean = sdt.replace("-", "").replace(" ", "")
    if sdt_clean.isdigit() and len(sdt_clean) >= 10:
        break
    else:
        print("Số điện thoại không hợp lệ. Vui lòng nhập lại!")

# Nhập địa chỉ
dia_chi = input("Địa chỉ: ").strip().title()
if not dia_chi:
    dia_chi = "Chưa cung cấp"

# Nhập trường học
truong = input("Trường học: ").strip().title()
if not truong:
    truong = "Chưa cung cấp"

# Nhập lớp
lop = input("Lớp: ").strip()
if not lop:
    lop = "Chưa cung cấp"

# Nhập môn học yêu thích
mon_yeu_thich = input("Môn học yêu thích: ").strip().title()
if not mon_yeu_thich:
    mon_yeu_thich = "Chưa cung cấp"

# Nhập sở thích
so_thich = input("Sở thích: ").strip()
if not so_thich:
    so_thich = "Chưa cung cấp"

# Tính toán thông tin bổ sung
import datetime
nam_hien_tai = datetime.datetime.now().year
nam_sinh = nam_hien_tai - tuoi

# Tạo username từ email
username = email.split("@")[0]

# Tạo initials từ tên
cac_tu = ho_ten.split()
initials = "".join([tu[0] for tu in cac_tu])

# Phân tích email domain
domain = email.split("@")[1]
if "gmail" in domain:
    email_provider = "Gmail"
elif "yahoo" in domain:
    email_provider = "Yahoo"
elif "edu" in domain:
    email_provider = "Giáo dục"
else:
    email_provider = "Khác"

# Hiển thị thông tin đã xử lý
print("\n" + "=" * 50)
print("THÔNG TIN ĐÃ XỬ LÝ")
print("=" * 50)

print(f"Họ tên: {ho_ten}")
print(f"Tuổi: {tuoi}")
print(f"Năm sinh (ước tính): {nam_sinh}")
print(f"Email: {email}")
print(f"Nhà cung cấp email: {email_provider}")
print(f"Username: {username}")
print(f"Số điện thoại: {sdt}")
print(f"Địa chỉ: {dia_chi}")
print(f"Trường học: {truong}")
print(f"Lớp: {lop}")
print(f"Môn yêu thích: {mon_yeu_thich}")
print(f"Sở thích: {so_thich}")

# Thông tin bổ sung
print("\n" + "-" * 50)
print("THÔNG TIN BỔ SUNG")
print("-" * 50)

print(f"Chữ cái đầu tên: {initials}")
print(f"Số ký tự trong tên: {len(ho_ten.replace(' ', ''))}")
print(f"Số từ trong tên: {len(cac_tu)}")

# Phân loại tuổi
if tuoi < 18:
    nhom_tuoi = "Vị thành niên"
elif tuoi < 25:
    nhom_tuoi = "Thanh niên"
elif tuoi < 60:
    nhom_tuoi = "Trưởng thành"
else:
    nhom_tuoi = "Cao tuổi"

print(f"Nhóm tuổi: {nhom_tuoi}")

# Tạo mã ID duy nhất
ma_id = f"{initials}{nam_sinh}"
print(f"Mã ID: {ma_id}")

# Tạo format hiển thị đẹp
print("\n" + "=" * 50)
print("THẺ THÔNG TIN")
print("=" * 50)

# Tạo khung thẻ
khung_tren = "+" + "-" * 48 + "+"
khung_giua = "|" + " " * 48 + "|"

print(khung_tren)
print(f"|{' ' * 16}THẺ THÔNG TIN{' ' * 16}|")
print(khung_tren)
print(f"| Tên: {ho_ten:<40} |")
print(f"| ID: {ma_id:<42} |")
print(f"| Tuổi: {tuoi:<40} |")
print(f"| Email: {email:<39} |")
print(f"| Trường: {truong:<38} |")
print(f"| Lớp: {lop:<42} |")
print(khung_tren)

# Tạo thống kê
print("\n" + "-" * 50)
print("THỐNG KÊ VÀ PHÂN TÍCH")
print("-" * 50)

# Thống kê ký tự trong tên
chu_cai = sum(1 for c in ho_ten if c.isalpha())
khoang_trang = ho_ten.count(' ')
ky_tu_khac = len(ho_ten) - chu_cai - khoang_trang

print(f"Phân tích tên '{ho_ten}':")
print(f"- Chữ cái: {chu_cai}")
print(f"- Khoảng trắng: {khoang_trang}")
print(f"- Ký tự khác: {ky_tu_khac}")

# Thống kê email
print(f"\nPhân tích email '{email}':")
print(f"- Độ dài: {len(email)} ký tự")
print(f"- Username: {len(username)} ký tự")
print(f"- Domain: {domain}")

# Dự đoán một số thông tin
print(f"\nDự đoán:")
if "nguyen" in ho_ten.lower():
    print("- Có thể là người Việt Nam (họ Nguyễn)")
if tuoi >= 18:
    print("- Đã đủ tuổi bầu cử")
if tuoi <= 22:
    print("- Có thể đang là sinh viên")

# Tạo lời khuyên
print(f"\nLời khuyên:")
if len(username) < 8:
    print("- Nên tạo username dài hơn để bảo mật tốt hơn")
if tuoi < 20:
    print("- Tập trung vào học tập và phát triển kỹ năng")
if "python" in mon_yeu_thich.lower():
    print("- Tiếp tục học Python để trở thành lập trình viên!")

print("\n" + "=" * 50)
print("CẢM ƠN BẠN ĐÃ CUNG CẤP THÔNG TIN!")
print("Dữ liệu đã được xử lý và phân tích thành công.")
print("=" * 50) 