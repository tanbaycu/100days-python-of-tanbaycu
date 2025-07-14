# Bài Tập 2: Số Học Chi Tiết
# Ngày 3-4: Phép toán và ứng dụng thực tế

print("=== BÀI TẬP 2: SỐ HỌC CHI TIẾT ===")

# PHẦN A: PHÉP TOÁN CƠ BẢN
print("\n" + "="*50)
print("PHẦN A: PHÉP TOÁN CƠ BẢN")
print("="*50)

# Bài A1: Tính toán với các số cho trước
print("\n--- Bài A1: Tính toán cơ bản ---")
a = 15
b = 4

print(f"Cho a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

# Bài A2: Thứ tự ưu tiên phép toán
print("\n--- Bài A2: Thứ tự ưu tiên ---")
ket_qua_1 = 2 + 3 * 4
ket_qua_2 = (2 + 3) * 4
ket_qua_3 = 2 ** 3 + 1
ket_qua_4 = 20 / 4 * 2

print(f"2 + 3 * 4 = {ket_qua_1}")
print(f"(2 + 3) * 4 = {ket_qua_2}")
print(f"2 ** 3 + 1 = {ket_qua_3}")
print(f"20 / 4 * 2 = {ket_qua_4}")

# Bài A3: Tính toán với số thực
print("\n--- Bài A3: Số thực ---")
pi = 3.14159
ban_kinh = 5.5

chu_vi_hinh_tron = 2 * pi * ban_kinh
dien_tich_hinh_tron = pi * (ban_kinh ** 2)

print(f"Bán kính hình tròn: {ban_kinh} cm")
print(f"Chu vi: {chu_vi_hinh_tron:.2f} cm")
print(f"Diện tích: {dien_tich_hinh_tron:.2f} cm²")

# PHẦN B: ỨNG DỤNG THỰC TẾ
print("\n" + "="*50)
print("PHẦN B: ỨNG DỤNG THỰC TẾ")
print("="*50)

# Bài B1: Tính tiền mua hàng
print("\n--- Bài B1: Tính tiền mua hàng ---")
gia_ao = 250000
gia_quan = 180000
so_luong_ao = 2
so_luong_quan = 1
giam_gia = 10  # 10%

tong_tien_ao = gia_ao * so_luong_ao
tong_tien_quan = gia_quan * so_luong_quan
tong_tien = tong_tien_ao + tong_tien_quan

tien_giam = tong_tien * giam_gia / 100
tien_phai_tra = tong_tien - tien_giam

print(f"Áo: {gia_ao:,} x {so_luong_ao} = {tong_tien_ao:,} VND")
print(f"Quần: {gia_quan:,} x {so_luong_quan} = {tong_tien_quan:,} VND")
print(f"Tổng tiền: {tong_tien:,} VND")
print(f"Giảm giá {giam_gia}%: -{tien_giam:,} VND")
print(f"Phải trả: {tien_phai_tra:,} VND")

# Bài B2: Chuyển đổi đơn vị
print("\n--- Bài B2: Chuyển đổi đơn vị ---")

# Chuyển độ C sang độ F và Kelvin
do_c = 25
do_f = do_c * 9/5 + 32
do_k = do_c + 273.15

print(f"Nhiệt độ: {do_c}°C")
print(f"= {do_f}°F")
print(f"= {do_k} K")

# Chuyển m/s sang km/h
van_toc_ms = 10
van_toc_kmh = van_toc_ms * 3.6

print(f"\nVận tốc: {van_toc_ms} m/s = {van_toc_kmh} km/h")

# Bài B3: Tính BMI
print("\n--- Bài B3: Tính chỉ số BMI ---")
can_nang = 65  # kg
chieu_cao = 1.70  # m

bmi = can_nang / (chieu_cao ** 2)

print(f"Cân nặng: {can_nang} kg")
print(f"Chiều cao: {chieu_cao} m")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    phan_loai = "Thiếu cân"
elif bmi < 25:
    phan_loai = "Bình thường"
elif bmi < 30:
    phan_loai = "Thừa cân"
else:
    phan_loai = "Béo phì"

print(f"Phân loại: {phan_loai}")

# PHẦN C: TOÁN TỬ GÁN
print("\n" + "="*50)
print("PHẦN C: TOÁN TỬ GÁN")
print("="*50)

print("\n--- Bài C1: Các toán tử gán ---")
x = 10
print(f"x ban đầu: {x}")

x += 5   # x = x + 5
print(f"x += 5: {x}")

x -= 3   # x = x - 3
print(f"x -= 3: {x}")

x *= 2   # x = x * 2
print(f"x *= 2: {x}")

x /= 4   # x = x / 4
print(f"x /= 4: {x}")

x **= 2  # x = x ** 2
print(f"x **= 2: {x}")

# PHẦN D: HÀM TOÁN HỌC
print("\n" + "="*50)
print("PHẦN D: HÀM TOÁN HỌC")
print("="*50)

print("\n--- Bài D1: Hàm có sẵn ---")
danh_sach_so = [-5, 3.7, -2.1, 8, 0]

for so in danh_sach_so:
    print(f"Số: {so}")
    print(f"  - Giá trị tuyệt đối: {abs(so)}")
    print(f"  - Làm tròn: {round(so)}")
    if so >= 0:
        print(f"  - Căn bậc hai: {so ** 0.5:.2f}")
    print()

# Min, Max với nhiều số
print("Với danh sách:", danh_sach_so)
print(f"Số nhỏ nhất: {min(danh_sach_so)}")
print(f"Số lớn nhất: {max(danh_sach_so)}")
print(f"Tổng: {sum(danh_sach_so)}")

# PHẦN E: BÀI TẬP THỰC HÀNH
print("\n" + "="*50)
print("PHẦN E: BÀI TẬP THỰC HÀNH")
print("="*50)

# Bài E1: Tính lãi suất ngân hàng
print("\n--- Bài E1: Tính lãi suất ---")
von_goc = 10000000  # 10 triệu
lai_suat = 6.5      # 6.5% /năm
so_nam = 2

lai = von_goc * lai_suat / 100 * so_nam
tong_tien = von_goc + lai

print(f"Vốn gốc: {von_goc:,} VND")
print(f"Lãi suất: {lai_suat}%/năm")
print(f"Thời gian: {so_nam} năm")
print(f"Tiền lãi: {lai:,} VND")
print(f"Tổng tiền nhận được: {tong_tien:,} VND")

# Bài E2: Chia tiền cho nhóm
print("\n--- Bài E2: Chia tiền nhóm ---")
tong_tien_an = 480000
so_nguoi = 7

moi_nguoi_tra = tong_tien_an // so_nguoi
tien_thua = tong_tien_an % so_nguoi

print(f"Tổng tiền ăn: {tong_tien_an:,} VND")
print(f"Số người: {so_nguoi}")
print(f"Mỗi người trả: {moi_nguoi_tra:,} VND")
print(f"Tiền thừa: {tien_thua:,} VND")

# Bài E3: Tính điểm trung bình có trọng số
print("\n--- Bài E3: Điểm trung bình có trọng số ---")
diem_15p = 8.5
diem_1_tiet = 7.5
diem_cuoi_ky = 9.0

# Trọng số: 15p (1), 1 tiết (2), cuối kỳ (3)
diem_tb = (diem_15p * 1 + diem_1_tiet * 2 + diem_cuoi_ky * 3) / (1 + 2 + 3)

print(f"Điểm 15 phút: {diem_15p} (trọng số 1)")
print(f"Điểm 1 tiết: {diem_1_tiet} (trọng số 2)")
print(f"Điểm cuối kỳ: {diem_cuoi_ky} (trọng số 3)")
print(f"Điểm trung bình: {diem_tb:.2f}")

# PHẦN F: CÂU HỎI TRẮC NGHIỆM
print("\n" + "="*50)
print("PHẦN F: CÂU HỎI TRẮC NGHIỆM")
print("="*50)

print("\n--- Quiz: Hãy tính toán trong đầu ---")

print("\nCâu 1: 7 * 8 + 3 = ?")
print("A) 59    B) 88    C) 56    D) 67")
dap_an_1 = 7 * 8 + 3
print(f"Đáp án: {dap_an_1}")

print("\nCâu 2: 15 // 4 = ?")
print("A) 3.75  B) 3    C) 4     D) 15")
dap_an_2 = 15 // 4
print(f"Đáp án: {dap_an_2}")

print("\nCâu 3: 17 % 5 = ?")
print("A) 3     B) 2    C) 5     D) 12")
dap_an_3 = 17 % 5
print(f"Đáp án: {dap_an_3}")

print("\nCâu 4: 2 ** 3 * 4 = ?")
print("A) 64    B) 32   C) 24    D) 96")
dap_an_4 = 2 ** 3 * 4
print(f"Đáp án: {dap_an_4}")

print("\nCâu 5: round(7.6) = ?")
print("A) 7     B) 8    C) 7.6   D) 7.5")
dap_an_5 = round(7.6)
print(f"Đáp án: {dap_an_5}")

# PHẦN G: THÁCH THỨC
print("\n" + "="*50)
print("PHẦN G: THÁCH THỨC")
print("="*50)

print("\n--- Thách thức 1: Tính tiền taxi ---")
km_dau = 1      # km đầu tiên
gia_km_dau = 15000  # 15k cho km đầu
gia_km_tiep = 12000  # 12k cho km tiếp theo
quang_duong = 8.5   # km

if quang_duong <= km_dau:
    tien_taxi = gia_km_dau
else:
    km_con_lai = quang_duong - km_dau
    tien_taxi = gia_km_dau + (km_con_lai * gia_km_tiep)

print(f"Quãng đường: {quang_duong} km")
print(f"Km đầu ({km_dau} km): {gia_km_dau:,} VND")
print(f"Km còn lại ({quang_duong - km_dau} km): {(quang_duong - km_dau) * gia_km_tiep:,} VND")
print(f"Tổng tiền taxi: {tien_taxi:,} VND")

print("\n--- Thách thức 2: Tính tuổi theo ngày ---")
nam_sinh = 2005
thang_sinh = 8
ngay_sinh = 15

nam_hien_tai = 2024
thang_hien_tai = 3
ngay_hien_tai = 20

# Tính số ngày sống
import datetime
ngay_sinh_date = datetime.date(nam_sinh, thang_sinh, ngay_sinh)
ngay_hien_tai_date = datetime.date(nam_hien_tai, thang_hien_tai, ngay_hien_tai)
so_ngay_song = (ngay_hien_tai_date - ngay_sinh_date).days

tuoi_nam = so_ngay_song // 365
so_ngay_con_lai = so_ngay_song % 365

print(f"Ngày sinh: {ngay_sinh}/{thang_sinh}/{nam_sinh}")
print(f"Hôm nay: {ngay_hien_tai}/{thang_hien_tai}/{nam_hien_tai}")
print(f"Đã sống: {so_ngay_song:,} ngày")
print(f"Tương đương: {tuoi_nam} năm {so_ngay_con_lai} ngày")

print("\n" + "="*50)
print("HOÀN THÀNH BÀI TẬP SỐ HỌC CHI TIẾT!")
print("Bạn đã thực hành:")
print("1. Tất cả phép toán cơ bản")
print("2. Ứng dụng thực tế (BMI, lãi suất, chia tiền)")
print("3. Chuyển đổi đơn vị")
print("4. Toán tử gán")
print("5. Hàm toán học")
print("6. Bài tập thách thức")
print("="*50) 