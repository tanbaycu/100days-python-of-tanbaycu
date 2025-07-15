"""
🎯 BÀI TẬP 4: ỨNG DỤNG FUNCTIONS VÀO DỰ ÁN THỰC TẾ
Ngày 13-14: Mini-projects thực tế, code sạch, test case, giải thích
Tác giả: Tanbaycu
"""

# 1. Quản lý thư viện sách đơn giản

def them_sach(library, ten, tac_gia, nam):
    """Thêm sách vào thư viện"""
    library.append({'ten':ten, 'tac_gia':tac_gia, 'nam':nam})
    return library

def tim_sach(library, keyword):
    """Tìm sách theo tên hoặc tác giả"""
    return [s for s in library if keyword.lower() in s['ten'].lower() or keyword.lower() in s['tac_gia'].lower()]

# Test
lib = []
them_sach(lib, "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 1941)
them_sach(lib, "Tuổi Thơ Dữ Dội", "Phùng Quán", 1988)
assert len(tim_sach(lib, "Dế")) == 1
assert len(tim_sach(lib, "Phùng")) == 1

# 2. Phân tích điểm học sinh

def tinh_trung_binh(diem):
    return sum(diem)/len(diem) if diem else 0

def phan_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def bao_cao_hoc_sinh(ds):
    """Trả về báo cáo điểm trung bình và phân loại cho từng học sinh"""
    return [{
        'ten': hs['ten'],
        'trung_binh': tinh_trung_binh(hs['diem']),
        'phan_loai': phan_loai(tinh_trung_binh(hs['diem']))
    } for hs in ds]

# Test
students = [
    {'ten':'An','diem':[8,9,7]},
    {'ten':'Bình','diem':[6,7,6]},
    {'ten':'Cường','diem':[4,5,5]}
]
report = bao_cao_hoc_sinh(students)
assert report[0]['phan_loai'] == "Giỏi"
assert report[1]['phan_loai'] == "Khá"
assert report[2]['phan_loai'] == "Yếu"

# 3. Xử lý văn bản: đếm tần suất từ

def dem_tan_suat_tu(text):
    """Đếm tần suất xuất hiện của từng từ"""
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0)+1
    return freq

# Test
text = "python code python ai code"
assert dem_tan_suat_tu(text)["python"] == 2
assert dem_tan_suat_tu(text)["code"] == 2

# 4. Quản lý đơn hàng e-commerce

def tinh_tong_don_hang(items):
    """Tính tổng tiền đơn hàng"""
    return sum(item['gia']*item['so_luong'] for item in items)

def ap_dung_coupon(total, coupon):
    """Áp dụng mã giảm giá"""
    if coupon == "SAVE10":
        return total*0.9
    elif coupon == "SAVE20":
        return total*0.8
    return total

# Test
order = [
    {'ten':'Laptop','gia':1000,'so_luong':1},
    {'ten':'Mouse','gia':50,'so_luong':2}
]
assert tinh_tong_don_hang(order) == 1100
assert ap_dung_coupon(1000, "SAVE10") == 900

# 5. Hệ thống tính lương nhân viên

def tinh_luong_cb(ngay, luong_ngay):
    return ngay*luong_ngay

def tinh_luong_tong(ngay, luong_ngay, thuong=0, phat=0):
    return tinh_luong_cb(ngay, luong_ngay) + thuong - phat

# Test
assert tinh_luong_tong(22, 300, 500, 0) == 7100
assert tinh_luong_tong(20, 250, 0, 200) == 4800

print("✅ Đã kiểm tra xong 5 mini-projects ứng dụng Functions!") 