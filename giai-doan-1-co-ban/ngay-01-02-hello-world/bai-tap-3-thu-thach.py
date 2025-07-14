# Bài Tập 3: Thử Thách
# Ngày 1-2: Ứng dụng print() và input()

print("=== BÀI TẬP 3: THỬ THÁCH ===")

# Thử thách 3.1: Máy tính cơ bản
print("\n--- Thử thách 3.1: Máy tính cơ bản ---")
print("=== MÁY TÍNH CƠ BẢN ===")
so_thu_nhat = input("Nhập số thứ nhất: ")
so_thu_hai = input("Nhập số thứ hai: ")

# Chuyển đổi string thành số
so_1 = int(so_thu_nhat)
so_2 = int(so_thu_hai)

tong = so_1 + so_2

print(f"{so_1} + {so_2} = {tong}")

# Thử thách 3.2: Thông tin sinh viên
print("\n--- Thử thách 3.2: Thẻ sinh viên ---")
print("ĐĂNG KÝ THÔNG TIN SINH VIÊN")
print("-" * 40)

ho_ten = input("Họ và tên: ")
ma_sv = input("Mã sinh viên: ")
lop = input("Lớp: ")
khoa = input("Khoa: ")
diem_tb = input("Điểm trung bình: ")

print("\n" + "=" * 40)
print("           THẺ SINH VIÊN")
print("=" * 40)
print(f"│ Họ tên: {ho_ten:<28}│")
print(f"│ MSSV: {ma_sv:<30}│")
print(f"│ Lớp: {lop:<31}│")
print(f"│ Khoa: {khoa:<30}│")
print(f"│ Điểm TB: {diem_tb:<27}│")
print("=" * 40)

# Thử thách 3.3: Game đoán tuổi
print("\n--- Thử thách 3.3: Game đoán tuổi ---")
print("GAME ĐOÁN TUỔI")
ten = input("Tên của bạn: ")
nam_sinh = input("Năm sinh của bạn: ")

# Tính tuổi (giả sử hiện tại là 2024)
nam_hien_tai = 2024
tuoi = nam_hien_tai - int(nam_sinh)

print(f"\nXin chào {ten}!")
print(f"Năm {nam_hien_tai}, bạn {tuoi} tuổi")

if tuoi < 18:
    print("Bạn còn nhỏ, học hành chăm chỉ nhé!")
elif tuoi < 25:
    print("Tuổi học tập, cố gắng lên!")
else:
    print("Đã trưởng thành, chúc thành công!")

print("\nHoàn thành tất cả thử thách!")
print("Bạn đã thành thạo print() và input()!") 