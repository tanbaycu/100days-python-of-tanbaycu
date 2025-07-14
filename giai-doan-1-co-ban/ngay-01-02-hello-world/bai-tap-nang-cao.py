# Bài Tập Nâng Cao - Ngày 1-2
# Dành cho những bạn muốn thử thách bản thân

print("🚀 BÀI TẬP NÂNG CAO - NGÀY 1-2 🚀")
print("=" * 50)

# Bài 1: Máy tính 4 phép toán
print("\n--- Bài 1: Máy tính 4 phép toán ---")
print("🧮 MÁY TÍNH NÂNG CAO")

so_a = float(input("Nhập số thứ nhất: "))
so_b = float(input("Nhập số thứ hai: "))

print(f"\n📊 KẾT QUẢ TÍNH TOÁN:")
print(f"{so_a} + {so_b} = {so_a + so_b}")
print(f"{so_a} - {so_b} = {so_a - so_b}")
print(f"{so_a} × {so_b} = {so_a * so_b}")

if so_b != 0:
    print(f"{so_a} ÷ {so_b} = {so_a / so_b:.2f}")
else:
    print(f"{so_a} ÷ {so_b} = Không thể chia cho 0!")

# Bài 2: Tính diện tích hình chữ nhật
print("\n--- Bài 2: Tính diện tích hình chữ nhật ---")
print("📐 TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT")

chieu_dai = float(input("Chiều dài (m): "))
chieu_rong = float(input("Chiều rộng (m): "))

dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

print(f"\n📊 KẾT QUẢ:")
print(f"Diện tích: {dien_tich} m²")
print(f"Chu vi: {chu_vi} m")

# Phân loại hình chữ nhật
if chieu_dai == chieu_rong:
    print("Đây là hình vuông! 🟦")
elif chieu_dai > chieu_rong:
    print("Hình chữ nhật nằm ngang 📱")
else:
    print("Hình chữ nhật đứng 📱")

# Bài 3: Chuyển đổi tiền tệ
print("\n--- Bài 3: Chuyển đổi tiền tệ ---")
print("💰 CHUYỂN ĐỔI TIỀN TỆ")

# Tỷ giá (cập nhật 2024)
ty_gia_usd = 24000
ty_gia_eur = 26000
ty_gia_jpy = 160

vnd = float(input("Nhập số tiền VND: "))

print(f"\n💵 {vnd:,.0f} VND = {vnd/ty_gia_usd:.2f} USD")
print(f"💶 {vnd:,.0f} VND = {vnd/ty_gia_eur:.2f} EUR")
print(f"💴 {vnd:,.0f} VND = {vnd/ty_gia_jpy:.2f} JPY")

# Bài 4: Tính BMI và phân loại
print("\n--- Bài 4: Tính BMI và phân loại ---")
print("TÍNH CHỈ SỐ BMI")

can_nang = float(input("Cân nặng (kg): "))
chieu_cao = float(input("Chiều cao (m): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"\n📊 BMI của bạn: {bmi:.1f}")

# Phân loại BMI
if bmi < 18.5:
    print("🔵 Thiếu cân")
elif bmi < 25:
    print("🟢 Bình thường")
elif bmi < 30:
    print("🟡 Thừa cân")
else:
    print("🔴 Béo phì")

# Bài 5: Game đoán số đơn giản
print("\n--- Bài 5: Game đoán số đơn giản ---")
print("GAME ĐOÁN SỐ")

import random
so_may = random.randint(1, 10)
so_ban = int(input("Đoán một số từ 1-10: "))

print(f"\nSố của máy: {so_may}")
print(f"Số bạn đoán: {so_ban}")

if so_ban == so_may:
    print("CHÍNH XÁC! Bạn thắng!")
else:
    print("Sai rồi! Chúc bạn may mắn lần sau!")

# Bài 6: Tạo story từ input
print("\n--- Bài 6: Tạo câu chuyện ---")
print("📚 TẠO CÂU CHUYỆN")

ten = input("Tên nhân vật chính: ")
tuoi = input("Tuổi: ")
nghe_nghiep = input("Nghề nghiệp: ")
so_thich = input("Sở thích: ")
dia_diem = input("Địa điểm yêu thích: ")

print(f"\n📖 CÂU CHUYỆN CỦA {ten.upper()}")
print("=" * 40)
print(f"Ngày xửa ngày xưa, có một {nghe_nghiep} tên {ten}, {tuoi} tuổi.")
print(f"{ten} rất thích {so_thich} và thường đi đến {dia_diem}.")
print(f"Mỗi ngày, {ten} đều dành thời gian để {so_thich}.")
print(f"Và họ sống hạnh phúc mãi mãi tại {dia_diem}!")
print("=" * 40)

# Bài 7: Tính tuổi và thông tin
print("\n--- Bài 7: Thông tin chi tiết về tuổi ---")
print("PHÂN TÍCH TUỔI")

nam_sinh = int(input("Năm sinh: "))
nam_hien_tai = 2024

tuoi = nam_hien_tai - nam_sinh
so_ngay = tuoi * 365
so_gio = so_ngay * 24
so_phut = so_gio * 60

print(f"\n📊 THỐNG KÊ CUỘC ĐỜI:")
print(f"Tuổi: {tuoi} tuổi")
print(f"Số ngày sống: {so_ngay:,} ngày")
print(f"Số giờ sống: {so_gio:,} giờ")
print(f"Số phút sống: {so_phut:,} phút")

# Dự đoán tương lai
tuoi_100 = 100 - tuoi
print(f"Còn {tuoi_100} năm nữa bạn sẽ 100 tuổi!")

# Bài 8: Tính tiền tip
print("\n--- Bài 8: Tính tiền tip ---")
print("TÍNH TIỀN TIP")

tong_tien = float(input("Tổng hóa đơn (VND): "))
phan_tram_tip = float(input("Phần trăm tip (10, 15, 20): "))

tien_tip = tong_tien * (phan_tram_tip / 100)
tong_thanh_toan = tong_tien + tien_tip

print(f"\n💰 CHI TIẾT THANH TOÁN:")
print(f"Tổng hóa đơn: {tong_tien:,.0f} VND")
print(f"Tip ({phan_tram_tip}%): {tien_tip:,.0f} VND")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VND")

# Bài 9: ASCII Art đơn giản
print("\n--- Bài 9: ASCII Art ---")
print("🎨 TẠO ASCII ART")

ten_ban = input("Tên của bạn: ")

print(f"\nASCII ART CHO {ten_ban.upper()}")
print("*" * (len(ten_ban) + 10))
print("*" + " " * (len(ten_ban) + 8) + "*")
print("*    " + ten_ban.upper() + "    *")
print("*" + " " * (len(ten_ban) + 8) + "*")
print("*" * (len(ten_ban) + 10))

# Bài 10: Quiz nhỏ
print("\n--- Bài 10: Quiz Python ---")
print("🧠 QUIZ PYTHON CƠ BẢN")

print("Câu hỏi: 2 + 3 * 4 = ?")
dap_an = input("Đáp án của bạn: ")

if dap_an == "14":
    print("Chính xác! Python tính nhân trước, cộng sau.")
else:
    print("Sai rồi! Đáp án đúng là 14 (3*4=12, 2+12=14)")

print("\n" + "=" * 20)
print("HOÀN THÀNH TẤT CẢ BÀI TẬP NÂNG CAO!")
print("Bạn đã sẵn sàng cho ngày 3-4! ��")
print("=" * 20) 