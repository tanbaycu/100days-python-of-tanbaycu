# trinh_bay_ban_than.py - Giới thiệu bản thân định dạng đẹp
# File cần nộp cho ngày 3-4

import datetime

print("CHƯƠNG TRÌNH GIỚI THIỆU BẢN THÂN")
print("=" * 50)

# Thông tin cá nhân
ho_ten = "Nguyen Van An"  # Thay bằng tên thật
tuoi = 18
nam_sinh = 2005
que_quan = "Ha Noi"
truong = "THPT ABC"
lop = "12A1"
mon_yeu_thich = "Python Programming"
so_thich = "Đọc sách, nghe nhạc, học lập trình"
uoc_mo = "Trở thành lập trình viên Python"

# Tính toán thông tin bổ sung
nam_hien_tai = datetime.datetime.now().year
thang_hien_tai = datetime.datetime.now().month
ngay_hien_tai = datetime.datetime.now().day

so_nam_song = nam_hien_tai - nam_sinh
so_thang_con_lai_den_sinh_nhat = 12 - thang_hien_tai if thang_hien_tai <= 12 else 0

# Tạo ASCII Art tên
def tao_ascii_art(ten):
    """Tạo ASCII art đơn giản cho tên"""
    lines = [
        "*" * (len(ten) + 6),
        "*  " + ten.upper() + "  *",
        "*" * (len(ten) + 6)
    ]
    return lines

ascii_art = tao_ascii_art(ho_ten)

# Header với ASCII Art
print("\n" + "=" * 50)
for line in ascii_art:
    print(f"{line:^50}")
print("=" * 50)

# Phần 1: Thông tin cơ bản
print("\n📋 THÔNG TIN CƠ BẢN")
print("-" * 30)
print(f"Họ và tên: {ho_ten}")
print(f"Tuổi: {tuoi}")
print(f"Năm sinh: {nam_sinh}")
print(f"Quê quán: {que_quan}")
print(f"Trường: {truong}")
print(f"Lớp: {lop}")

# Phần 2: Sở thích và đam mê
print(f"\n❤️ SỞ THÍCH VÀ ĐAM MÊ")
print("-" * 30)
print(f"Môn học yêu thích: {mon_yeu_thich}")
print(f"Sở thích: {so_thich}")
print(f"Ước mơ: {uoc_mo}")

# Phần 3: Thống kê thú vị
print(f"\n📊 THỐNG KÊ THÚ VỊ")
print("-" * 30)

# Phân tích tên
cac_tu_ten = ho_ten.split()
so_tu_trong_ten = len(cac_tu_ten)
so_ky_tu_ten = len(ho_ten.replace(" ", ""))
chu_cai_dau = "".join([tu[0] for tu in cac_tu_ten])

print(f"Số từ trong tên: {so_tu_trong_ten}")
print(f"Số ký tự trong tên: {so_ky_tu_ten}")
print(f"Chữ cái đầu: {chu_cai_dau}")

# Thống kê tuổi
so_ngay_song_uoc_tinh = so_nam_song * 365
so_gio_song_uoc_tinh = so_ngay_song_uoc_tinh * 24

print(f"Đã sống khoảng: {so_ngay_song_uoc_tinh:,} ngày")
print(f"Tương đương: {so_gio_song_uoc_tinh:,} giờ")

# Nhóm tuổi
if tuoi < 13:
    nhom_tuoi = "Thiếu nhi"
elif tuoi < 18:
    nhom_tuoi = "Vị thành niên"
elif tuoi < 25:
    nhom_tuoi = "Thanh niên"
else:
    nhom_tuoi = "Trưởng thành"

print(f"Nhóm tuổi: {nhom_tuoi}")

# Phần 4: Hành trình học Python
print(f"\n🐍 HÀNH TRÌNH HỌC PYTHON")
print("-" * 30)

# Giả lập tiến độ học
ngay_hoc = 4  # Đang học ngày 3-4
tong_ngay = 100
phan_tram_hoan_thanh = (ngay_hoc / tong_ngay) * 100

print(f"Ngày học hiện tại: {ngay_hoc}/{tong_ngay}")
print(f"Tiến độ: {phan_tram_hoan_thanh:.1f}%")

# Thanh tiến độ ASCII
thanh_do_dai = 30
so_dau = int(thanh_do_dai * phan_tram_hoan_thanh / 100)
thanh_tien_do = "█" * so_dau + "░" * (thanh_do_dai - so_dau)
print(f"[{thanh_tien_do}] {phan_tram_hoan_thanh:.1f}%")

# Kỹ năng đã học
ky_nang_da_hoc = [
    "Print và Input",
    "Biến và kiểu dữ liệu",
    "Phép toán số học",
    "Xử lý chuỗi (String)",
    "Chuyển đổi kiểu dữ liệu"
]

print(f"\nKỹ năng đã học ({len(ky_nang_da_hoc)} kỹ năng):")
for i, ky_nang in enumerate(ky_nang_da_hoc, 1):
    print(f"  {i}. {ky_nang}")

# Phần 5: Mục tiêu và kế hoạch
print(f"\n🎯 MỤC TIÊU VÀ KẾ HOẠCH")
print("-" * 30)

muc_tieu_gan = [
    "Hoàn thành 100 ngày học Python",
    "Nắm vững các khái niệm cơ bản",
    "Xây dựng dự án đầu tiên",
    "Tham gia cộng đồng Python"
]

print("Mục tiêu gần:")
for i, muc_tieu in enumerate(muc_tieu_gan, 1):
    print(f"  {i}. {muc_tieu}")

muc_tieu_xa = [
    "Trở thành Python Developer",
    "Học Machine Learning",
    "Đóng góp cho Open Source",
    "Tạo ra sản phẩm có ích"
]

print(f"\nMục tiêu xa:")
for i, muc_tieu in enumerate(muc_tieu_xa, 1):
    print(f"  {i}. {muc_tieu}")

# Phần 6: Thông điệp cá nhân
print(f"\n💌 THÔNG ĐIỆP CÁ NHÂN")
print("-" * 30)

thong_diep = f"""
Xin chào! Tôi là {ho_ten}, {tuoi} tuổi.
Tôi đang học lập trình Python với mục tiêu trở thành 
một lập trình viên chuyên nghiệp.

Tôi tin rằng Python là ngôn ngữ tuyệt vời để bắt đầu
hành trình lập trình. Mỗi ngày tôi học được điều mới
và cảm thấy hứng thú hơn với thế giới công nghệ.

Motto của tôi: "Học mỗi ngày, tiến bộ mỗi ngày!"
"""

print(thong_diep)

# Phần 7: Fun Facts
print(f"\n🎉 FUN FACTS VỀ TÔI")
print("-" * 30)

fun_facts = [
    f"Tên tôi có {so_ky_tu_ten} ký tự",
    f"Tôi đã sống được {so_nam_song} năm trên đời",
    f"Trong {tong_ngay} ngày học Python, tôi đã hoàn thành {ngay_hoc} ngày",
    f"Môn yêu thích của tôi có {len(mon_yeu_thich)} ký tự",
    f"Ước mơ của tôi bắt đầu bằng chữ '{uoc_mo[0]}'"
]

for i, fact in enumerate(fun_facts, 1):
    print(f"  {i}. {fact}")

# Phần 8: Contact & Social
print(f"\n📞 LIÊN HỆ")
print("-" * 30)

# Tạo thông tin liên hệ giả lập
email_gia_lap = f"{ho_ten.lower().replace(' ', '.')}@email.com"
github_gia_lap = f"github.com/{ho_ten.lower().replace(' ', '')}"

print(f"Email: {email_gia_lap}")
print(f"GitHub: {github_gia_lap}")
print("Facebook: [Cập nhật sau]")
print("LinkedIn: [Cập nhật sau]")

# Footer
print(f"\n" + "=" * 50)
print("CẢM ƠN BẠN ĐÃ ĐỌC GIỚI THIỆU CỦA TÔI!")
print(f"Cập nhật lần cuối: {ngay_hien_tai}/{thang_hien_tai}/{nam_hien_tai}")
print("Hãy cùng nhau học Python và phát triển!")
print("=" * 50)

# Bonus: Tạo chữ ký ASCII
chu_ky = f"""
    ╔══════════════════════════╗
    ║        {chu_cai_dau:<15} ║
    ║    Python Learner        ║
    ║      Day {ngay_hoc}/100           ║
    ╚══════════════════════════╝
"""

print(chu_ky)

print("\n🎊 Chúc bạn một ngày học Python vui vẻ! 🎊") 