# may_tinh_don_gian.py - Máy tính cơ bản
# File cần nộp cho ngày 1-2

print("MÁY TÍNH ĐƠN GIẢN")
print("=" * 30)

# Nhập hai số từ người dùng
print("Nhập hai số để thực hiện phép tính:")
so_thu_nhat = input("Số thứ nhất: ")
so_thu_hai = input("Số thứ hai: ")

# Chuyển đổi từ string sang số
so_1 = int(so_thu_nhat)
so_2 = int(so_thu_hai)

# Thực hiện phép tính cộng
tong = so_1 + so_2

# Hiển thị kết quả
print("\n" + "📊" * 20)
print("     KẾT QUẢ TÍNH TOÁN")
print("📊" * 20)
print(f"{so_1} + {so_2} = {tong}")
print("📊" * 20)

# Thêm thông tin bổ sung
if tong > 100:
    print("Wow! Kết quả lớn hơn 100!")
elif tong > 50:
    print("Kết quả khá lớn!")
else:
    print("Kết quả nhỏ gọn!")

print(f"\nCảm ơn bạn đã sử dụng máy tính!")
print("Chúc bạn học Python vui vẻ!") 