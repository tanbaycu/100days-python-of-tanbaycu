# may_tinh_nang_cao.py - Máy tính với nhiều phép toán
# File cần nộp cho ngày 3-4

print("MÁY TÍNH NÂNG CAO")
print("=" * 40)

# Nhận input từ người dùng
print("Nhập thông tin để tính toán:")
so_thu_nhat = float(input("Số thứ nhất: "))
so_thu_hai = float(input("Số thứ hai: "))

print(f"\nSố thứ nhất: {so_thu_nhat}")
print(f"Số thứ hai: {so_thu_hai}")

# Thực hiện tất cả phép toán
print("\n" + "=" * 40)
print("KẾT QUẢ CÁC PHÉP TOÁN")
print("=" * 40)

# Phép toán cơ bản
tong = so_thu_nhat + so_thu_hai
hieu = so_thu_nhat - so_thu_hai
tich = so_thu_nhat * so_thu_hai

print(f"Cộng: {so_thu_nhat} + {so_thu_hai} = {tong}")
print(f"Trừ: {so_thu_nhat} - {so_thu_hai} = {hieu}")
print(f"Nhân: {so_thu_nhat} * {so_thu_hai} = {tich}")

# Phép chia (kiểm tra chia cho 0)
if so_thu_hai != 0:
    thuong = so_thu_nhat / so_thu_hai
    chia_nguyen = so_thu_nhat // so_thu_hai
    chia_du = so_thu_nhat % so_thu_hai
    
    print(f"Chia: {so_thu_nhat} / {so_thu_hai} = {thuong}")
    print(f"Chia lấy nguyên: {so_thu_nhat} // {so_thu_hai} = {chia_nguyen}")
    print(f"Chia lấy dư: {so_thu_nhat} % {so_thu_hai} = {chia_du}")
else:
    print("Chia: Không thể chia cho 0!")

# Lũy thừa
luy_thua = so_thu_nhat ** so_thu_hai
print(f"Lũy thừa: {so_thu_nhat} ^ {so_thu_hai} = {luy_thua}")

# Phép toán nâng cao
print("\n" + "-" * 40)
print("PHÉP TOÁN NÂNG CAO")
print("-" * 40)

# Giá trị tuyệt đối
gia_tri_tuyet_doi_1 = abs(so_thu_nhat)
gia_tri_tuyet_doi_2 = abs(so_thu_hai)
print(f"Giá trị tuyệt đối của {so_thu_nhat}: {gia_tri_tuyet_doi_1}")
print(f"Giá trị tuyệt đối của {so_thu_hai}: {gia_tri_tuyet_doi_2}")

# Làm tròn
lam_tron_1 = round(so_thu_nhat, 2)
lam_tron_2 = round(so_thu_hai, 2)
print(f"Làm tròn {so_thu_nhat} (2 chữ số): {lam_tron_1}")
print(f"Làm tròn {so_thu_hai} (2 chữ số): {lam_tron_2}")

# Min, Max
so_nho_nhat = min(so_thu_nhat, so_thu_hai)
so_lon_nhat = max(so_thu_nhat, so_thu_hai)
print(f"Số nhỏ nhất: {so_nho_nhat}")
print(f"Số lớn nhất: {so_lon_nhat}")

# Căn bậc hai (nếu số dương)
if so_thu_nhat >= 0:
    can_bac_hai_1 = so_thu_nhat ** 0.5
    print(f"Căn bậc hai của {so_thu_nhat}: {can_bac_hai_1}")
else:
    print(f"Không thể tính căn bậc hai của số âm: {so_thu_nhat}")

if so_thu_hai >= 0:
    can_bac_hai_2 = so_thu_hai ** 0.5
    print(f"Căn bậc hai của {so_thu_hai}: {can_bac_hai_2}")
else:
    print(f"Không thể tính căn bậc hai của số âm: {so_thu_hai}")

# Thống kê
print("\n" + "-" * 40)
print("THỐNG KÊ")
print("-" * 40)

trung_binh = (so_thu_nhat + so_thu_hai) / 2
print(f"Trung bình cộng: {trung_binh}")

# Phân loại kết quả
if tong > 100:
    loai_tong = "Tổng lớn"
elif tong > 0:
    loai_tong = "Tổng dương"
elif tong == 0:
    loai_tong = "Tổng bằng 0"
else:
    loai_tong = "Tổng âm"

print(f"Phân loại tổng: {loai_tong}")

# Kiểm tra số chẵn/lẻ (nếu là số nguyên)
if so_thu_nhat == int(so_thu_nhat):
    if int(so_thu_nhat) % 2 == 0:
        print(f"{int(so_thu_nhat)} là số chẵn")
    else:
        print(f"{int(so_thu_nhat)} là số lẻ")

if so_thu_hai == int(so_thu_hai):
    if int(so_thu_hai) % 2 == 0:
        print(f"{int(so_thu_hai)} là số chẵn")
    else:
        print(f"{int(so_thu_hai)} là số lẻ")

print("\n" + "=" * 40)
print("CẢM ƠN BẠN ĐÃ SỬ DỤNG MÁY TÍNH!")
print("Máy tính này hỗ trợ:")
print("- Tất cả phép toán cơ bản")
print("- Phép toán nâng cao")
print("- Xử lý lỗi chia cho 0")
print("- Thống kê và phân loại")
print("=" * 40) 