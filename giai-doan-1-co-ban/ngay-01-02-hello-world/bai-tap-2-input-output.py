# Bài Tập 2: Input và Output
# Ngày 1-2: Tương tác với người dùng

print("=== BÀI TẬP 2: INPUT VÀ OUTPUT ===")

# Bài 2.1: Chào hỏi đơn giản
print("\n--- Bài 2.1: Chào hỏi đơn giản ---")
ten = input("Nhập tên của bạn: ")
print("Xin chào " + ten + "!")
print(f"Rất vui được gặp bạn, {ten}!")

# Bài 2.2: Thông tin chi tiết
print("\n--- Bài 2.2: Form đăng ký ---")
print("=== FORM ĐĂNG KÝ ===")
ho_ten = input("Họ và tên: ")
tuoi = input("Tuổi: ")
noi_song = input("Nơi sống: ")
so_thich = input("Sở thích: ")

print("\n" + "="*25)
print("THÔNG TIN CỦA BẠN")
print("="*25)
print(f"Họ tên: {ho_ten}")
print(f"Tuổi: {tuoi}")
print(f"Nơi sống: {noi_song}")
print(f"Sở thích: {so_thich}")
print("="*25)

# Bài 2.3: Lời chào tùy chỉnh
print("\n--- Bài 2.3: Lời chào theo thời gian ---")
ten_2 = input("Tên của bạn: ")
buoi = input("Bây giờ là buổi gì? (sáng/chiều/tối): ")

if buoi == "sáng":
    print(f"Chào buổi sáng {ten_2}! Hôm nay học Python nhé!")
elif buoi == "chiều":
    print(f"Chào buổi chiều {ten_2}! Tiếp tục coding thôi!")
else:
    print(f"Chào buổi tối {ten_2}! Học Python buổi tối rất tập trung!")

print("\nHoàn thành bài tập 2!")
print("Tiếp tục với bài tập thử thách!") 