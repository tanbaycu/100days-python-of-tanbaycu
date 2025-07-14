# thong_tin_ca_nhan.py - Form thông tin cá nhân
# File cần nộp cho ngày 1-2

print("FORM THÔNG TIN CÁ NHÂN")
print("=" * 40)

# Nhập thông tin cá nhân
print("Vui lòng nhập thông tin của bạn:")
print("-" * 40)

ten = input("Tên: ")
tuoi = input("Tuổi: ")
thanh_pho = input("Thành phố: ")

# Hiển thị thông tin đã nhập
print("\n" + "=" * 40)
print("       THÔNG TIN CỦA BẠN")
print("=" * 40)
print(f"Tên: {ten}")
print(f"Tuổi: {tuoi}")
print(f"Thành phố: {thanh_pho}")
print("=" * 40)

# Tạo lời chào tùy chỉnh
print(f"\nXin chào {ten}!")
print(f"Rất vui được biết bạn {tuoi} tuổi và đang sống tại {thanh_pho}.")
print("Chúc bạn học Python vui vẻ!")

print("\nCảm ơn bạn đã chia sẻ thông tin!") 