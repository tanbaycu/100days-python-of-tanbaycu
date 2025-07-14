# Bài Tập 3: String (Chuỗi) Chi Tiết
# Ngày 3-4: Xử lý chuỗi và ứng dụng thực tế

print("=== BÀI TẬP 3: STRING CHI TIẾT ===")

# PHẦN A: TẠO VÀ NỐI STRING
print("\n" + "="*50)
print("PHẦN A: TẠO VÀ NỐI STRING")
print("="*50)

# Bài A1: Các cách tạo string
print("\n--- Bài A1: Các cách tạo string ---")
ten_1 = "Nguyen Van An"
ten_2 = 'Le Thi Binh'
loi_chao = """Xin chào,
Chúc bạn một ngày tốt lành!
Hẹn gặp lại."""

print(f"Tên 1: {ten_1}")
print(f"Tên 2: {ten_2}")
print(f"Lời chào:\n{loi_chao}")

# Bài A2: Nối string
print("\n--- Bài A2: Nối string ---")
ho = "Tran"
dem = "Van"
ten = "Duc"

# Cách 1: Dùng +
ho_ten_1 = ho + " " + dem + " " + ten
print(f"Cách 1 (+): {ho_ten_1}")

# Cách 2: f-string (khuyên dùng)
ho_ten_2 = f"{ho} {dem} {ten}"
print(f"Cách 2 (f-string): {ho_ten_2}")

# Cách 3: .format()
ho_ten_3 = "{} {} {}".format(ho, dem, ten)
print(f"Cách 3 (.format): {ho_ten_3}")

# Bài A3: Escape characters
print("\n--- Bài A3: Ký tự đặc biệt ---")
cau_noi = "Cô giáo nói: \"Hôm nay học Python\""
duong_dan = "C:\\Users\\Documents\\file.txt"
dong_moi = "Dòng 1\nDòng 2\nDòng 3"
tab_space = "Cột 1\tCột 2\tCột 3"

print(f"Câu nói: {cau_noi}")
print(f"Đường dẫn: {duong_dan}")
print(f"Nhiều dòng:\n{dong_moi}")
print(f"Tab: {tab_space}")

# PHẦN B: CÁC METHOD CƠ BẢN
print("\n" + "="*50)
print("PHẦN B: CÁC METHOD CƠ BẢN")
print("="*50)

# Bài B1: Độ dài và chuyển đổi case
print("\n--- Bài B1: Độ dài và case ---")
cau_text = "Python Programming is Fun"

print(f"Text gốc: '{cau_text}'")
print(f"Độ dài: {len(cau_text)} ký tự")
print(f"Upper: {cau_text.upper()}")
print(f"Lower: {cau_text.lower()}")
print(f"Title: {cau_text.title()}")
print(f"Capitalize: {cau_text.capitalize()}")
print(f"Swapcase: {cau_text.swapcase()}")

# Bài B2: Tìm kiếm và đếm
print("\n--- Bài B2: Tìm kiếm và đếm ---")
text = "Python is awesome. Python is easy. I love Python!"

print(f"Text: '{text}'")
print(f"Tìm 'Python': vị trí {text.find('Python')}")
print(f"Tìm 'Java': vị trí {text.find('Java')}")
print(f"Đếm 'Python': {text.count('Python')} lần")
print(f"Đếm 'is': {text.count('is')} lần")
print(f"Bắt đầu bằng 'Python': {text.startswith('Python')}")
print(f"Kết thúc bằng '!': {text.endswith('!')}")

# Bài B3: Thay thế
print("\n--- Bài B3: Thay thế ---")
email = "student@email.com"
thay_the_1 = email.replace("@", " [at] ")
thay_the_2 = email.replace(".", " [dot] ")
thay_the_3 = text.replace("Python", "Java")

print(f"Email gốc: {email}")
print(f"Thay @ thành [at]: {thay_the_1}")
print(f"Thay . thành [dot]: {thay_the_2}")
print(f"Thay Python thành Java: {thay_the_3}")

# PHẦN C: KIỂM TRA KIỂU NỘI DUNG
print("\n" + "="*50)
print("PHẦN C: KIỂM TRA KIỂU NỘI DUNG")
print("="*50)

print("\n--- Bài C1: Kiểm tra kiểu ---")
test_strings = [
    "Python123",
    "12345",
    "abcdef",
    "ABC",
    "Hello World",
    "",
    "   ",
    "python_programming"
]

for s in test_strings:
    print(f"\nString: '{s}'")
    print(f"  - isalpha(): {s.isalpha()}")
    print(f"  - isdigit(): {s.isdigit()}")
    print(f"  - isalnum(): {s.isalnum()}")
    print(f"  - isspace(): {s.isspace()}")
    print(f"  - isupper(): {s.isupper()}")
    print(f"  - islower(): {s.islower()}")

# PHẦN D: SLICING (CẮT CHUỖI)
print("\n" + "="*50)
print("PHẦN D: SLICING (CẮT CHUỖI)")
print("="*50)

print("\n--- Bài D1: Cắt chuỗi cơ bản ---")
text = "Python Programming"
print(f"Text gốc: '{text}'")
print(f"Độ dài: {len(text)}")

# Truy cập từng ký tự
print(f"\nTruy cập ký tự:")
print(f"text[0]: '{text[0]}'")
print(f"text[1]: '{text[1]}'")
print(f"text[-1]: '{text[-1]}'")
print(f"text[-2]: '{text[-2]}'")

# Cắt đoạn
print(f"\nCắt đoạn:")
print(f"text[0:6]: '{text[0:6]}'")
print(f"text[7:]: '{text[7:]}'")
print(f"text[:6]: '{text[:6]}'")
print(f"text[::2]: '{text[::2]}'")
print(f"text[::-1]: '{text[::-1]}'")

# PHẦN E: TÁCH VÀ GHÉP
print("\n" + "="*50)
print("PHẦN E: TÁCH VÀ GHÉP")
print("="*50)

print("\n--- Bài E1: Split và Join ---")
cau_van = "Python là ngôn ngữ lập trình mạnh mẽ"
danh_sach_tu = cau_van.split()
print(f"Câu gốc: '{cau_van}'")
print(f"Tách thành từ: {danh_sach_tu}")
print(f"Số từ: {len(danh_sach_tu)}")

# Ghép lại với các ký tự khác
ghep_gach_ngang = "-".join(danh_sach_tu)
ghep_underscore = "_".join(danh_sach_tu)
print(f"Ghép bằng '-': {ghep_gach_ngang}")
print(f"Ghép bằng '_': {ghep_underscore}")

# Tách theo ký tự khác
csv_data = "Tên,Tuổi,Lớp,Điểm"
cac_cot = csv_data.split(",")
print(f"\nCSV data: '{csv_data}'")
print(f"Các cột: {cac_cot}")

# PHẦN F: XỬ LÝ KHOẢNG TRẮNG
print("\n" + "="*50)
print("PHẦN F: XỬ LÝ KHOẢNG TRẮNG")
print("="*50)

print("\n--- Bài F1: Strip methods ---")
messy_text = "   Xin chào Python!   "
print(f"Text gốc: '{messy_text}'")
print(f"strip(): '{messy_text.strip()}'")
print(f"lstrip(): '{messy_text.lstrip()}'")
print(f"rstrip(): '{messy_text.rstrip()}'")

# Xóa ký tự khác
text_with_chars = "***Hello World***"
print(f"\nText với *: '{text_with_chars}'")
print(f"strip('*'): '{text_with_chars.strip('*')}'")

# PHẦN G: FORMAT STRING NÂNG CAO
print("\n" + "="*50)
print("PHẦN G: FORMAT STRING NÂNG CAO")
print("="*50)

print("\n--- Bài G1: f-string với format ---")
ten = "An"
tuoi = 18
diem = 8.567
gia_tien = 1234567

print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Điểm (2 chữ số): {diem:.2f}")
print(f"Điểm (0 chữ số): {diem:.0f}")
print(f"Giá tiền: {gia_tien:,} VND")

# Căn lề
print(f"\nCăn lề:")
print(f"|{ten:>10}|")  # Căn phải
print(f"|{ten:<10}|")  # Căn trái
print(f"|{ten:^10}|")  # Căn giữa
print(f"|{ten:*^10}|") # Căn giữa với ký tự *

# PHẦN H: ỨNG DỤNG THỰC TẾ
print("\n" + "="*50)
print("PHẦN H: ỨNG DỤNG THỰC TẾ")
print("="*50)

# Bài H1: Xử lý tên
print("\n--- Bài H1: Chuẩn hóa tên ---")
ten_nhap_vao = "  nGuYeN    VaN     aN  "
ten_chuan_hoa = " ".join(ten_nhap_vao.strip().split()).title()

print(f"Tên nhập vào: '{ten_nhap_vao}'")
print(f"Tên chuẩn hóa: '{ten_chuan_hoa}'")

# Tạo initials
cac_tu = ten_chuan_hoa.split()
chu_cai_dau = "".join([tu[0] for tu in cac_tu])
print(f"Chữ cái đầu: {chu_cai_dau}")

# Bài H2: Kiểm tra email
print("\n--- Bài H2: Kiểm tra email ---")
emails = [
    "student@gmail.com",
    "invalid.email",
    "test@university.edu.vn",
    "@gmail.com",
    "user@"
]

for email in emails:
    hop_le = "@" in email and "." in email and len(email) > 5
    print(f"Email: {email:20} - {'Hợp lệ' if hop_le else 'Không hợp lệ'}")

# Bài H3: Tạo username từ email
print("\n--- Bài H3: Tạo username ---")
email_mau = "nguyen.van.an@university.edu.vn"
username = email_mau.split("@")[0]
domain = email_mau.split("@")[1]

print(f"Email: {email_mau}")
print(f"Username: {username}")
print(f"Domain: {domain}")

# PHẦN I: CÂU HỎI TRẮC NGHIỆM
print("\n" + "="*50)
print("PHẦN I: CÂU HỎI TRẮC NGHIỆM STRING")
print("="*50)

print("\n--- Quiz String ---")

test_str = "Hello World"

print(f"\nCho string: '{test_str}'")
print("Câu 1: len('Hello World') = ?")
print("A) 10    B) 11    C) 12    D) 9")
print(f"Đáp án: {len(test_str)}")

print("\nCâu 2: 'Hello World'[6] = ?")
print("A) 'W'   B) 'o'   C) ' '   D) 'r'")
print(f"Đáp án: '{test_str[6]}'")

print("\nCâu 3: 'Hello World'.find('o') = ?")
print("A) 3     B) 4     C) 7     D) -1")
print(f"Đáp án: {test_str.find('o')}")

print("\nCâu 4: 'Hello World'.count('l') = ?")
print("A) 2     B) 3     C) 1     D) 4")
print(f"Đáp án: {test_str.count('l')}")

print("\nCâu 5: 'Hello World'[::-1] = ?")
print("A) 'dlroW olleH'  B) 'World Hello'  C) 'Hello'  D) 'World'")
print(f"Đáp án: '{test_str[::-1]}'")

# PHẦN J: BÀI TẬP THÁCH THỨC
print("\n" + "="*50)
print("PHẦN J: BÀI TẬP THÁCH THỨC")
print("="*50)

# Thách thức 1: Kiểm tra palindrome
print("\n--- Thách thức 1: Kiểm tra palindrome ---")
def kiem_tra_palindrome(text):
    # Loại bỏ khoảng trắng và chuyển thành chữ thường
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

cac_tu_test = ["radar", "hello", "A man a plan a canal Panama", "racecar", "python"]

for tu in cac_tu_test:
    ket_qua = kiem_tra_palindrome(tu)
    print(f"'{tu}' là palindrome: {ket_qua}")

# Thách thức 2: Đếm từ và ký tự
print("\n--- Thách thức 2: Phân tích văn bản ---")
van_ban = """Python là một ngôn ngữ lập trình bậc cao, 
dễ học và mạnh mẽ. Python được sử dụng rộng rãi 
trong phát triển web, khoa học dữ liệu và AI."""

# Đếm số dòng
so_dong = van_ban.count('\n') + 1

# Đếm số từ
cac_tu = van_ban.replace('\n', ' ').split()
so_tu = len(cac_tu)

# Đếm số ký tự (không tính space và newline)
so_ky_tu = len(van_ban.replace(' ', '').replace('\n', ''))

# Đếm số câu (tính theo dấu . và !)
so_cau = van_ban.count('.') + van_ban.count('!')

print(f"Văn bản:\n{van_ban}")
print(f"\nPhân tích:")
print(f"- Số dòng: {so_dong}")
print(f"- Số từ: {so_tu}")
print(f"- Số ký tự: {so_ky_tu}")
print(f"- Số câu: {so_cau}")

# Từ xuất hiện nhiều nhất
tu_dem = {}
for tu in cac_tu:
    tu_clean = tu.strip('.,!').lower()
    tu_dem[tu_clean] = tu_dem.get(tu_clean, 0) + 1

tu_pho_bien = max(tu_dem, key=tu_dem.get)
print(f"- Từ phổ biến nhất: '{tu_pho_bien}' ({tu_dem[tu_pho_bien]} lần)")

# Thách thức 3: Tạo mật khẩu từ thông tin
print("\n--- Thách thức 3: Tạo mật khẩu ---")
ho_ten = "Nguyen Van An"
nam_sinh = 2005
mon_yeu_thich = "Python"

# Lấy chữ cái đầu của tên
chu_cai_dau = "".join([tu[0].upper() for tu in ho_ten.split()])

# Lấy 3 ký tự đầu của môn yêu thích
mon_viet_tat = mon_yeu_thich[:3].lower()

# Tạo mật khẩu
mat_khau = f"{chu_cai_dau}{nam_sinh}{mon_viet_tat}!"

print(f"Thông tin:")
print(f"- Họ tên: {ho_ten}")
print(f"- Năm sinh: {nam_sinh}")
print(f"- Môn yêu thích: {mon_yeu_thich}")
print(f"Mật khẩu được tạo: {mat_khau}")

print("\n" + "="*50)
print("HOÀN THÀNH BÀI TẬP STRING CHI TIẾT!")
print("Bạn đã thực hành:")
print("1. Tạo và nối string")
print("2. Tất cả string methods quan trọng")
print("3. Slicing và indexing")
print("4. Format string nâng cao")
print("5. Ứng dụng thực tế")
print("6. Bài tập thách thức")
print("="*50) 