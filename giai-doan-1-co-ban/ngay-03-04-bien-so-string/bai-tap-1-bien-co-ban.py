# Bài Tập 1: Biến Cơ Bản
# Ngày 3-4: Khai báo và sử dụng biến

print("=== BÀI TẬP 1: BIẾN CƠ BẢN ===")

# Bài 1.1: Tạo thông tin cá nhân
print("\n--- Bài 1.1: Thông tin cá nhân ---")

# Tạo các biến chứa thông tin của bạn
ten_hoc_sinh = "Nguyen Van An"
tuoi = 18
lop = "10A"
truong = "THPT ABC"
diem_trung_binh = 8.5
la_hoc_sinh_gioi = True

# In thông tin
print("THÔNG TIN HỌC SINH")
print("=" * 30)
print(f"Tên: {ten_hoc_sinh}")
print(f"Tuổi: {tuoi}")
print(f"Lớp: {lop}")
print(f"Trường: {truong}")
print(f"Điểm TB: {diem_trung_binh}")
print(f"Học sinh giỏi: {la_hoc_sinh_gioi}")

# Bài 1.2: Kiểm tra kiểu dữ liệu
print("\n--- Bài 1.2: Kiểm tra kiểu dữ liệu ---")

print(f"Kiểu của 'ten_hoc_sinh': {type(ten_hoc_sinh)}")
print(f"Kiểu của 'tuoi': {type(tuoi)}")
print(f"Kiểu của 'diem_trung_binh': {type(diem_trung_binh)}")
print(f"Kiểu của 'la_hoc_sinh_gioi': {type(la_hoc_sinh_gioi)}")

# Bài 1.3: Thay đổi giá trị biến
print("\n--- Bài 1.3: Thay đổi giá trị biến ---")

print(f"Điểm TB ban đầu: {diem_trung_binh}")

# Cập nhật điểm
diem_trung_binh = 9.0
print(f"Điểm TB sau khi cập nhật: {diem_trung_binh}")

# Thay đổi cả kiểu dữ liệu
tuoi_text = str(tuoi)
print(f"Tuổi dạng text: '{tuoi_text}' (kiểu: {type(tuoi_text)})")

# Bài 1.4: Gán nhiều biến
print("\n--- Bài 1.4: Gán nhiều biến ---")

# Gán cùng giá trị
diem_toan = diem_ly = diem_hoa = 8.0
print(f"Điểm Toán: {diem_toan}")
print(f"Điểm Lý: {diem_ly}")
print(f"Điểm Hóa: {diem_hoa}")

# Gán khác giá trị
ten_mon_1, ten_mon_2, ten_mon_3 = "Toán", "Lý", "Hóa"
print(f"Môn 1: {ten_mon_1}")
print(f"Môn 2: {ten_mon_2}")
print(f"Môn 3: {ten_mon_3}")

# Bài 1.5: Hoán đổi giá trị
print("\n--- Bài 1.5: Hoán đổi giá trị ---")

a = 10
b = 20
print(f"Trước khi hoán đổi: a = {a}, b = {b}")

# Hoán đổi bằng Python (elegant way)
a, b = b, a
print(f"Sau khi hoán đổi: a = {a}, b = {b}")

# Bài 1.6: Tính toán với biến
print("\n--- Bài 1.6: Tính toán với biến ---")

# Thông tin hình chữ nhật
chieu_dai = 5.5
chieu_rong = 3.2

# Tính chu vi và diện tích
chu_vi = 2 * (chieu_dai + chieu_rong)
dien_tich = chieu_dai * chieu_rong

print(f"Chiều dài: {chieu_dai} m")
print(f"Chiều rộng: {chieu_rong} m")
print(f"Chu vi: {chu_vi} m")
print(f"Diện tích: {dien_tich} m²")

# Bài 1.7: Quy tắc đặt tên biến
print("\n--- Bài 1.7: Quy tắc đặt tên biến ---")

# Tên biến đúng
ten_day_du = "Nguyen Van An"
so_dien_thoai = "0123456789"
nam_sinh_2005 = 2005
_bien_rieng_tu = "private"

print("Các biến đặt tên đúng quy tắc:")
print(f"- ten_day_du: {ten_day_du}")
print(f"- so_dien_thoai: {so_dien_thoai}")
print(f"- nam_sinh_2005: {nam_sinh_2005}")
print(f"- _bien_rieng_tu: {_bien_rieng_tu}")

# Ví dụ tên biến sai (comment để không lỗi)
# 2ten = "An"           # Sai: bắt đầu bằng số
# ten-hoc-sinh = "An"   # Sai: dấu gạch ngang
# class = "10A"         # Sai: từ khóa Python

print("\nCác tên biến SAI:")
print("- 2ten (bắt đầu bằng số)")
print("- ten-hoc-sinh (có dấu gạch ngang)")
print("- class (từ khóa Python)")

# Bài 1.8: Hằng số (constants)
print("\n--- Bài 1.8: Hằng số ---")

# Hằng số thường viết HOA
PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458  # m/s

print("Các hằng số:")
print(f"- PI = {PI}")
print(f"- Gia tốc trọng trường = {GRAVITY} m/s²")
print(f"- Tốc độ ánh sáng = {SPEED_OF_LIGHT:,} m/s")

# Bài 1.9: Thực hành với input
print("\n--- Bài 1.9: Thực hành với input ---")

# Nhận thông tin từ user (uncomment để test)
# print("Hãy nhập thông tin của bạn:")
# ten_user = input("Tên: ")
# tuoi_user = int(input("Tuổi: "))
# mon_yeu_thich = input("Môn học yêu thích: ")

# print(f"\nXin chào {ten_user}!")
# print(f"Bạn {tuoi_user} tuổi và thích môn {mon_yeu_thich}")

print("(Code nhận input đã được comment)")
print("Uncomment để test với input thực tế")

print("\n" + "=" * 50)
print("HOÀN THÀNH BÀI TẬP 1: BIẾN CƠ BẢN")
print("Bạn đã học được:")
print("1. Tạo và sử dụng biến")
print("2. Các kiểu dữ liệu cơ bản")
print("3. Quy tắc đặt tên biến")
print("4. Gán và hoán đổi giá trị")
print("5. Tính toán với biến")
print("=" * 50) 