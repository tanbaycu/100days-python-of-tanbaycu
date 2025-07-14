# ===============================================
# NGÀY 5-6: ỨNG DỤNG THỰC TẾ VỚI IF/ELSE
# Mục tiêu: Áp dụng if/else vào các tình huống thực tế
# ===============================================

print("=== ỨNG DỤNG THỰC TẾ VỚI IF/ELSE ===")
print("Học lập trình qua các tình huống đời sống!")
print()

# ===============================================
# PHẦN A: HỆ THỐNG MUA SẮM ONLINE
# ===============================================
print("--- PHẦN A: HỆ THỐNG MUA SẮM ONLINE ---")
print()

# A1. Tính phí ship theo khu vực
print("A1. Tính phí ship theo khu vực:")
print("Code mẫu:")
print('''
gia_don_hang = 500000
khu_vuc = "noi_thanh"  # noi_thanh, ngoai_thanh, tinh_khac

if khu_vuc == "noi_thanh":
    phi_ship = 30000
    if gia_don_hang >= 200000:
        phi_ship = 0  # Miễn phí ship
        print("Miễn phí ship cho đơn >= 200k trong nội thành")
elif khu_vuc == "ngoai_thanh":
    phi_ship = 50000
    if gia_don_hang >= 500000:
        phi_ship = 25000  # Giảm 50%
        print("Giảm 50% phí ship cho đơn >= 500k ngoại thành")
else:  # tinh_khac
    phi_ship = 80000
    if gia_don_hang >= 1000000:
        phi_ship = 40000  # Giảm 50%
        print("Giảm 50% phí ship cho đơn >= 1tr tỉnh khác")

tong_tien = gia_don_hang + phi_ship
print(f"Giá đơn hàng: {gia_don_hang:,}đ")
print(f"Phí ship: {phi_ship:,}đ")
print(f"Tổng cộng: {tong_tien:,}đ")
''')
print()

# A2. Hệ thống giảm giá thông minh
print("A2. Hệ thống giảm giá thông minh:")
print("Code mẫu:")
print('''
gia_goc = 1500000
la_thanh_vien = True
so_lan_mua = 15  # Lần mua trước đó
la_sinh_nhat = False

giam_gia = 0

# Giảm giá theo thành viên
if la_thanh_vien:
    if so_lan_mua >= 20:
        giam_gia += 20  # VIP: 20%
    elif so_lan_mua >= 10:
        giam_gia += 15  # Thân thiết: 15%
    else:
        giam_gia += 10  # Thành viên mới: 10%

# Giảm giá sinh nhật
if la_sinh_nhat:
    giam_gia += 5
    print("Chúc mừng sinh nhật! Tặng thêm 5% giảm giá!")

# Giảm giá theo giá trị đơn hàng
if gia_goc >= 2000000:
    giam_gia += 10
    print("Đơn hàng >= 2tr: Tặng thêm 10%!")
elif gia_goc >= 1000000:
    giam_gia += 5
    print("Đơn hàng >= 1tr: Tặng thêm 5%!")

# Giới hạn giảm giá tối đa
if giam_gia > 30:
    giam_gia = 30
    print("Giảm giá tối đa 30%")

so_tien_giam = gia_goc * giam_gia / 100
gia_cuoi = gia_goc - so_tien_giam

print(f"\\nThông tin đơn hàng:")
print(f"Giá gốc: {gia_goc:,}đ")
print(f"Giảm giá: {giam_gia}% (-{so_tien_giam:,}đ)")
print(f"Thành tiền: {gia_cuoi:,}đ")
''')
print()

# BÀI TẬP TỰ LÀM A:
print("*** BÀI TẬP TỰ LÀM A ***")
print("1. Tạo hệ thống tích điểm: mỗi 100k = 1 điểm, VIP x2 điểm")
print("2. Tính thuế VAT: thực phẩm 5%, hàng hóa 10%, dịch vụ 10%")
print("3. Hệ thống đổi trả: < 7 ngày miễn phí, 7-30 ngày phí 50k")
print()

# ===============================================
# PHẦN B: HỆ THỐNG NGÂN HÀNG
# ===============================================
print("--- PHẦN B: HỆ THỐNG NGÂN HÀNG ---")
print()

# B1. Tính lãi suất tiết kiệm
print("B1. Tính lãi suất tiết kiệm:")
print("Code mẫu:")
print('''
so_tien_gui = 100000000  # 100 triệu
thoi_gian_gui = 12  # tháng
loai_khach = "vip"  # thuong, vip, premium

# Lãi suất cơ bản theo thời gian
if thoi_gian_gui >= 36:
    lai_suat = 7.5
elif thoi_gian_gui >= 24:
    lai_suat = 7.0
elif thoi_gian_gui >= 12:
    lai_suat = 6.5
elif thoi_gian_gui >= 6:
    lai_suat = 6.0
else:
    lai_suat = 5.5

# Thưởng theo loại khách hàng
if loai_khach == "premium":
    lai_suat += 0.5
    print("Khách hàng Premium: Thưởng +0.5% lãi suất")
elif loai_khach == "vip":
    lai_suat += 0.3
    print("Khách hàng VIP: Thưởng +0.3% lãi suất")

# Thưởng theo số tiền gửi
if so_tien_gui >= 500000000:  # >= 500 triệu
    lai_suat += 0.2
    print("Số tiền lớn (>= 500tr): Thưởng +0.2% lãi suất")
elif so_tien_gui >= 100000000:  # >= 100 triệu
    lai_suat += 0.1
    print("Số tiền khá (>= 100tr): Thưởng +0.1% lãi suất")

# Tính lãi
lai_thang = so_tien_gui * lai_suat / 100 / 12
tong_lai = lai_thang * thoi_gian_gui
so_tien_nhan = so_tien_gui + tong_lai

print(f"\\n=== THÔNG TIN TIẾT KIỆM ===")
print(f"Số tiền gửi: {so_tien_gui:,}đ")
print(f"Thời gian: {thoi_gian_gui} tháng")
print(f"Lãi suất: {lai_suat}%/năm")
print(f"Lãi/tháng: {lai_thang:,.0f}đ")
print(f"Tổng lãi: {tong_lai:,.0f}đ")
print(f"Tổng nhận: {so_tien_nhan:,.0f}đ")
''')
print()

# B2. Đánh giá khả năng vay vốn
print("B2. Đánh giá khả năng vay vốn:")
print("Code mẫu:")
print('''
thu_nhap_thang = 25000000
so_tien_vay = 500000000
thoi_gian_vay = 60  # tháng
co_bds = True  # Có bất động sản thế chấp
diem_tin_dung = 720  # Điểm tín dụng (300-850)

# Kiểm tra thu nhập tối thiểu
thu_nhap_toi_thieu = so_tien_vay / 20  # 1/20 số tiền vay
if thu_nhap_thang < thu_nhap_toi_thieu:
    print("❌ Không đủ điều kiện vay (thu nhập thấp)")
    exit()

# Tính lãi suất dựa trên điểm tín dụng
if diem_tin_dung >= 750:
    lai_suat_nam = 8.0
    muc_do_rui_ro = "Thấp"
elif diem_tin_dung >= 650:
    lai_suat_nam = 10.0
    muc_do_rui_ro = "Trung bình"
elif diem_tin_dung >= 550:
    lai_suat_nam = 12.0
    muc_do_rui_ro = "Cao"
else:
    print("❌ Điểm tín dụng quá thấp")
    exit()

# Điều chỉnh lãi suất theo tài sản thế chấp
if co_bds:
    lai_suat_nam -= 1.0
    print("Có BĐS thế chấp: Giảm 1% lãi suất")

# Tính khoản vay
lai_suat_thang = lai_suat_nam / 100 / 12
tra_hang_thang = (so_tien_vay * lai_suat_thang * (1 + lai_suat_thang)**thoi_gian_vay) / ((1 + lai_suat_thang)**thoi_gian_vay - 1)
tong_tra = tra_hang_thang * thoi_gian_vay
tong_lai = tong_tra - so_tien_vay

# Kiểm tra khả năng thanh toán
ty_le_thu_nhap = (tra_hang_thang / thu_nhap_thang) * 100

if ty_le_thu_nhap <= 30:
    ket_qua = "✅ DUYỆT VAY"
    loi_khuyen = "Tỷ lệ nợ/thu nhập hợp lý"
elif ty_le_thu_nhap <= 50:
    ket_qua = "⚠️ CÂN NHẮC"
    loi_khuyen = "Nên giảm số tiền vay hoặc tăng thời gian"
else:
    ket_qua = "❌ TỪ CHỐI"
    loi_khuyen = "Tỷ lệ nợ/thu nhập quá cao"

print(f"\\n=== ĐÁNH GIÁ VAY VỐN ===")
print(f"Số tiền vay: {so_tien_vay:,}đ")
print(f"Thời gian: {thoi_gian_vay} tháng")
print(f"Lãi suất: {lai_suat_nam}%/năm")
print(f"Trả hàng tháng: {tra_hang_thang:,.0f}đ")
print(f"Tổng trả: {tong_tra:,.0f}đ")
print(f"Tổng lãi: {tong_lai:,.0f}đ")
print(f"Tỷ lệ nợ/thu nhập: {ty_le_thu_nhap:.1f}%")
print(f"Mức độ rủi ro: {muc_do_rui_ro}")
print(f"Kết quả: {ket_qua}")
print(f"Lời khuyên: {loi_khuyen}")
''')
print()

# BÀI TẬP TỰ LÀM B:
print("*** BÀI TẬP TỰ LÀM B ***")
print("1. Hệ thống phí chuyển khoản: nội địa, quốc tế, priority")
print("2. Tính phí duy trì tài khoản theo số dư và loại tài khoản")
print("3. Đánh giá hạn mức thẻ tín dụng theo thu nhập và lịch sử")
print()

# ===============================================
# PHẦN C: HỆ THỐNG Y TẾ
# ===============================================
print("--- PHẦN C: HỆ THỐNG Y TẾ ---")
print()

# C1. Đánh giá sức khỏe BMI nâng cao
print("C1. Đánh giá sức khỏe BMI nâng cao:")
print("Code mẫu:")
print('''
can_nang = 70  # kg
chieu_cao = 175  # cm
tuoi = 30
gioi_tinh = "nam"  # nam, nu
co_benh_nen = False

# Chuyển đổi chiều cao sang mét
chieu_cao_m = chieu_cao / 100
bmi = can_nang / (chieu_cao_m ** 2)

# Phân loại BMI cơ bản
if bmi < 16:
    phan_loai = "Suy dinh dưỡng nặng"
    muc_do_rui_ro = "Rất cao"
elif bmi < 17:
    phan_loai = "Suy dinh dưỡng vừa"
    muc_do_rui_ro = "Cao"
elif bmi < 18.5:
    phan_loai = "Suy dinh dưỡng nhẹ"
    muc_do_rui_ro = "Thấp"
elif bmi < 25:
    phan_loai = "Bình thường"
    muc_do_rui_ro = "Thấp"
elif bmi < 30:
    phan_loai = "Thừa cân"
    muc_do_rui_ro = "Trung bình"
elif bmi < 35:
    phan_loai = "Béo phì độ I"
    muc_do_rui_ro = "Cao"
elif bmi < 40:
    phan_loai = "Béo phì độ II"
    muc_do_rui_ro = "Rất cao"
else:
    phan_loai = "Béo phì độ III"
    muc_do_rui_ro = "Cực cao"

# Điều chỉnh theo tuổi và giới tính
if tuoi >= 65:
    if bmi >= 23 and bmi <= 30:
        phan_loai += " (Phù hợp người cao tuổi)"
        muc_do_rui_ro = "Thấp"

# Tính cân nặng lý tưởng
if gioi_tinh == "nam":
    can_nang_ly_tuong_min = 22 * (chieu_cao_m ** 2)
    can_nang_ly_tuong_max = 24.9 * (chieu_cao_m ** 2)
else:
    can_nang_ly_tuong_min = 20 * (chieu_cao_m ** 2)
    can_nang_ly_tuong_max = 24 * (chieu_cao_m ** 2)

# Đưa ra lời khuyên
if bmi < 18.5:
    loi_khuyen = f"Nên tăng {can_nang_ly_tuong_min - can_nang:.1f}kg. Ăn nhiều protein, tập gym."
elif bmi > 25:
    loi_khuyen = f"Nên giảm {can_nang - can_nang_ly_tuong_max:.1f}kg. Ăn ít, tập cardio."
else:
    loi_khuyen = "Duy trì cân nặng hiện tại. Tập thể dục đều đặn."

# Cảnh báo bệnh lý
if co_benh_nen and (bmi < 18.5 or bmi > 30):
    canh_bao = "⚠️ CẢNH BÁO: BMI bất thường có thể ảnh hưởng bệnh nền!"
else:
    canh_bao = ""

print(f"=== ĐÁNH GIÁ SỨC KHỎE BMI ===")
print(f"Chiều cao: {chieu_cao}cm")
print(f"Cân nặng: {can_nang}kg")
print(f"BMI: {bmi:.1f}")
print(f"Phân loại: {phan_loai}")
print(f"Mức độ rủi ro: {muc_do_rui_ro}")
print(f"Cân nặng lý tưởng: {can_nang_ly_tuong_min:.1f} - {can_nang_ly_tuong_max:.1f}kg")
print(f"Lời khuyên: {loi_khuyen}")
if canh_bao:
    print(canh_bao)
''')
print()

# C2. Hệ thống tư vấn sức khỏe
print("C2. Hệ thống tư vấn sức khỏe:")
print("Code mẫu:")
print('''
# Nhập triệu chứng
trieu_chung = ["đau đầu", "sốt", "ho", "mệt mỏi"]
muc_do_dau = 7  # Thang điểm 1-10
thoi_gian_dau = 3  # ngày
co_tien_su_benh = True

print("=== HỆ THỐNG TƯ VẤN SỨC KHỎE ===")
print(f"Triệu chứng: {', '.join(trieu_chung)}")
print(f"Mức độ đau: {muc_do_dau}/10")
print(f"Thời gian: {thoi_gian_dau} ngày")

# Đánh giá mức độ nghiêm trọng
diem_rui_ro = 0

# Điểm theo triệu chứng
if "sốt" in trieu_chung:
    diem_rui_ro += 3
if "đau ngực" in trieu_chung:
    diem_rui_ro += 5
if "khó thở" in trieu_chung:
    diem_rui_ro += 4
if "đau đầu" in trieu_chung:
    diem_rui_ro += 2
if "ho" in trieu_chung:
    diem_rui_ro += 1

# Điểm theo mức độ đau
if muc_do_dau >= 8:
    diem_rui_ro += 3
elif muc_do_dau >= 6:
    diem_rui_ro += 2
elif muc_do_dau >= 4:
    diem_rui_ro += 1

# Điểm theo thời gian
if thoi_gian_dau >= 7:
    diem_rui_ro += 2
elif thoi_gian_dau >= 3:
    diem_rui_ro += 1

# Điểm tiền sử bệnh
if co_tien_su_benh:
    diem_rui_ro += 2

# Đưa ra khuyến nghị
if diem_rui_ro >= 10:
    uu_tien = "🚨 KHẨN CẤP"
    khuyen_nghi = "Đi bệnh viện NGAY LẬP TỨC!"
    thoi_gian = "Trong 1 giờ"
elif diem_rui_ro >= 7:
    uu_tien = "⚠️ NGHIÊM TRỌNG"
    khuyen_nghi = "Đến bệnh viện trong ngày hôm nay"
    thoi_gian = "Trong 4-6 giờ"
elif diem_rui_ro >= 4:
    uu_tien = "🟡 CẦN KHÁM"
    khuyen_nghi = "Đặt lịch khám trong tuần"
    thoi_gian = "1-3 ngày"
else:
    uu_tien = "🟢 THEO DÕI"
    khuyen_nghi = "Tự theo dõi, nghỉ ngơi"
    thoi_gian = "Nếu không giảm sau 3-5 ngày"

# Gợi ý sơ cứu
if "sốt" in trieu_chung:
    so_cuu = "Hạ sốt bằng paracetamol, chườm ấm"
elif "ho" in trieu_chung:
    so_cuu = "Uống nước ấm, mật ong, tránh khói bụi"
elif "đau đầu" in trieu_chung:
    so_cuu = "Nghỉ ngơi, massage thái dương, giảm ánh sáng"
else:
    so_cuu = "Nghỉ ngơi đầy đủ, uống nhiều nước"

print(f"\\nĐánh giá rủi ro: {diem_rui_ro} điểm")
print(f"Mức độ ưu tiên: {uu_tien}")
print(f"Khuyến nghị: {khuyen_nghi}")
print(f"Thời gian: {thoi_gian}")
print(f"Sơ cứu tại nhà: {so_cuu}")
print("\\n⚠️ Lưu ý: Đây chỉ là tư vấn sơ bộ, không thay thế bác sĩ!")
''')
print()

# BÀI TẬP TỰ LÀM C:
print("*** BÀI TẬP TỰ LÀM C ***")
print("1. Tính liều thuốc theo cân nặng và tuổi")
print("2. Đánh giá nguy cơ tim mạch theo các yếu tố")
print("3. Hệ thống nhắc uống thuốc theo đơn bác sĩ")
print()

# ===============================================
# PHẦN D: HỆ THỐNG GIÁO DỤC
# ===============================================
print("--- PHẦN D: HỆ THỐNG GIÁO DỤC ---")
print()

# D1. Hệ thống xếp lớp thông minh
print("D1. Hệ thống xếp lớp thông minh:")
print("Code mẫu:")
print('''
diem_toan = 8.5
diem_van = 7.0
diem_anh = 9.0
hanh_kiem = "tốt"  # tot, kha, tb, yeu
so_buoi_nghi = 5
co_khen_thuong = True
co_vi_pham = False

# Tính điểm trung bình
diem_tb = (diem_toan + diem_van + diem_anh) / 3

# Xếp loại học lực
if diem_tb >= 8.5 and min(diem_toan, diem_van, diem_anh) >= 8.0:
    hoc_luc = "Giỏi"
elif diem_tb >= 7.0 and min(diem_toan, diem_van, diem_anh) >= 6.5:
    hoc_luc = "Khá"
elif diem_tb >= 5.0 and min(diem_toan, diem_van, diem_anh) >= 4.0:
    hoc_luc = "Trung bình"
else:
    hoc_luc = "Yếu"

# Điều chỉnh theo hạnh kiểm và chuyên cần
if so_buoi_nghi > 10:
    hoc_luc = "Yếu"  # Quá nhiều buổi nghỉ
    ly_do = "Nghỉ học quá nhiều"
elif hanh_kiem == "yeu":
    if hoc_luc == "Giỏi":
        hoc_luc = "Khá"
    elif hoc_luc == "Khá":
        hoc_luc = "Trung bình"
    ly_do = "Hạnh kiểm yếu"

# Xét học sinh xuất sắc
if hoc_luc == "Giỏi" and hanh_kiem == "tốt" and co_khen_thuong and not co_vi_pham:
    danh_hieu = "Học sinh xuất sắc"
elif hoc_luc in ["Giỏi", "Khá"] and hanh_kiem in ["tốt", "khá"]:
    danh_hieu = "Học sinh tiên tiến"
else:
    danh_hieu = "Không"

# Xét điều kiện lên lớp
mon_duoi_5 = sum([1 for diem in [diem_toan, diem_van, diem_anh] if diem < 5])

if mon_duoi_5 == 0:
    len_lop = "Lên lớp"
elif mon_duoi_5 <= 1 and diem_tb >= 5.0:
    len_lop = "Lên lớp (có điều kiện)"
else:
    len_lop = "Ở lại lớp"

# Gợi ý cải thiện
goi_y = []
if diem_toan < 6:
    goi_y.append("Cần cải thiện Toán")
if diem_van < 6:
    goi_y.append("Cần cải thiện Văn")
if diem_anh < 6:
    goi_y.append("Cần cải thiện Anh")
if so_buoi_nghi > 5:
    goi_y.append("Cần cải thiện chuyên cần")
if hanh_kiem != "tốt":
    goi_y.append("Cần cải thiện hạnh kiểm")

print(f"=== KẾT QUẢ HỌC TẬP ===")
print(f"Điểm TB: {diem_tb:.2f}")
print(f"Học lực: {hoc_luc}")
print(f"Hạnh kiểm: {hanh_kiem}")
print(f"Chuyên cần: {40 - so_buoi_nghi}/40 buổi")
print(f"Danh hiệu: {danh_hieu}")
print(f"Kết quả: {len_lop}")
if goi_y:
    print(f"Gợi ý cải thiện: {', '.join(goi_y)}")
''')
print()

# D2. Hệ thống tư vấn ngành nghề
print("D2. Hệ thống tư vấn ngành nghề:")
print("Code mẫu:")
print('''
# Điểm các khối
diem_A = 24.5  # Toán, Lý, Hóa
diem_B = 22.0  # Toán, Hóa, Sinh
diem_C = 23.5  # Văn, Sử, Địa
diem_D = 25.0  # Toán, Văn, Anh

# Sở thích và năng lực
so_thich = ["công nghệ", "toán học", "nghiên cứu"]
tinh_cach = "hướng nội"  # hướng nội, hướng ngoại
kha_nang_dac_biet = ["lập trình", "phân tích"]

# Điều kiện gia đình
tinh_hinh_kinh_te = "khá"  # khó khăn, bình thường, khá, giàu
mong_muon_gia_dinh = "ổn định"  # ổn định, phát triển, thành công

print("=== TƯ VẤN NGÀNH NGHỀ ===")

# Phân tích điểm số
diem_cao_nhat = max(diem_A, diem_B, diem_C, diem_D)
if diem_cao_nhat == diem_A:
    khoi_manh = "A (Toán, Lý, Hóa)"
    nganh_phu_hop = ["Kỹ thuật", "Công nghệ thông tin", "Y dược", "Kiến trúc"]
elif diem_cao_nhat == diem_B:
    khoi_manh = "B (Toán, Hóa, Sinh)"
    nganh_phu_hop = ["Y học", "Sinh học", "Nông nghiệp", "Môi trường"]
elif diem_cao_nhat == diem_C:
    khoi_manh = "C (Văn, Sử, Địa)"
    nganh_phu_hop = ["Luật", "Báo chí", "Du lịch", "Ngoại ngữ"]
else:
    khoi_manh = "D (Toán, Văn, Anh)"
    nganh_phu_hop = ["Kinh tế", "Quản trị", "Tài chính", "Marketing"]

# Phân tích sở thích
nganh_theo_so_thich = []
if "công nghệ" in so_thich:
    nganh_theo_so_thich.extend(["Công nghệ thông tin", "Kỹ thuật điện tử"])
if "nghiên cứu" in so_thich:
    nganh_theo_so_thich.extend(["Khoa học cơ bản", "R&D"])
if "kinh doanh" in so_thich:
    nganh_theo_so_thich.extend(["Kinh doanh", "Marketing"])

# Phân tích tính cách
if tinh_cach == "hướng nội":
    nghe_phu_hop_tinh_cach = ["Lập trình viên", "Kế toán", "Nghiên cứu viên", "Thiết kế"]
else:
    nghe_phu_hop_tinh_cach = ["Kinh doanh", "Giáo viên", "Luật sư", "Bác sĩ"]

# Gợi ý ngành học cụ thể
goi_y_cuoi = []
for nganh in nganh_phu_hop:
    if nganh in nganh_theo_so_thich:
        goi_y_cuoi.append(f"{nganh} (⭐ Rất phù hợp)")
    else:
        goi_y_cuoi.append(f"{nganh} (Phù hợp)")

# Tư vấn tài chính
if tinh_hinh_kinh_te == "khó khăn":
    tu_van_tai_chinh = "Nên chọn ngành dễ có việc làm, học phí thấp"
elif tinh_hinh_kinh_te == "giàu":
    tu_van_tai_chinh = "Có thể chọn ngành yêu thích, du học"
else:
    tu_van_tai_chinh = "Cân bằng giữa đam mê và thực tế"

print(f"Khối mạnh nhất: {khoi_manh} ({diem_cao_nhat} điểm)")
print(f"Ngành phù hợp theo điểm:")
for goi_y in goi_y_cuoi:
    print(f"  - {goi_y}")
print(f"\\nNghề phù hợp tính cách: {', '.join(nghe_phu_hop_tinh_cach[:3])}")
print(f"Tư vấn tài chính: {tu_van_tai_chinh}")
''')
print()

# BÀI TẬP TỰ LÀM D:
print("*** BÀI TẬP TỰ LÀM D ***")
print("1. Hệ thống đăng ký môn học theo điều kiện tiên quyết")
print("2. Tính học phí theo tín chỉ và chương trình học")
print("3. Xếp lịch thi tránh trùng và hợp lý cho sinh viên")
print()

# ===============================================
# PHẦN E: ỨNG DỤNG GIẢI TRÍ
# ===============================================
print("--- PHẦN E: ỨNG DỤNG GIẢI TRÍ ---")
print()

# E1. Game RPG Character Builder
print("E1. Game RPG Character Builder:")
print("Code mẫu:")
print('''
print("=== TẠO NHÂN VẬT RPG ===")

# Chọn class nhân vật
character_class = "warrior"  # warrior, mage, archer, thief

# Chọn race
race = "human"  # human, elf, dwarf, orc

# Stats cơ bản
base_hp = 100
base_mp = 50
base_attack = 20
base_defense = 15
base_speed = 10

# Điều chỉnh theo class
if character_class == "warrior":
    hp_bonus = 50
    attack_bonus = 15
    defense_bonus = 20
    speed_bonus = -5
    mp_bonus = 0
    special_skill = "Berserker Rage"
    weapon = "Sword & Shield"
    
elif character_class == "mage":
    hp_bonus = -20
    attack_bonus = 5
    defense_bonus = -10
    speed_bonus = 5
    mp_bonus = 100
    special_skill = "Fireball"
    weapon = "Magic Staff"
    
elif character_class == "archer":
    hp_bonus = 0
    attack_bonus = 25
    defense_bonus = 0
    speed_bonus = 20
    mp_bonus = 20
    special_skill = "Arrow Rain"
    weapon = "Longbow"
    
else:  # thief
    hp_bonus = -10
    attack_bonus = 10
    defense_bonus = -5
    speed_bonus = 30
    mp_bonus = 30
    special_skill = "Stealth Attack"
    weapon = "Twin Daggers"

# Điều chỉnh theo race
if race == "elf":
    hp_bonus -= 10
    mp_bonus += 30
    speed_bonus += 10
    trait = "Magic Resistance"
    
elif race == "dwarf":
    hp_bonus += 20
    defense_bonus += 15
    speed_bonus -= 10
    trait = "Tough Skin"
    
elif race == "orc":
    hp_bonus += 30
    attack_bonus += 10
    defense_bonus += 5
    speed_bonus -= 15
    trait = "Berserker Blood"
    
else:  # human
    # Balanced - no bonuses but gets extra skill point
    trait = "Adaptable"

# Tính stats cuối cùng
final_hp = base_hp + hp_bonus
final_mp = base_mp + mp_bonus
final_attack = base_attack + attack_bonus
final_defense = base_defense + defense_bonus
final_speed = base_speed + speed_bonus

# Tính combat rating
combat_rating = (final_hp + final_attack + final_defense + final_speed + final_mp) // 10

# Xếp hạng nhân vật
if combat_rating >= 35:
    rank = "S-Rank (Legendary)"
elif combat_rating >= 30:
    rank = "A-Rank (Epic)"
elif combat_rating >= 25:
    rank = "B-Rank (Rare)"
elif combat_rating >= 20:
    rank = "C-Rank (Common)"
else:
    rank = "D-Rank (Novice)"

print(f"\\n{'='*40}")
print(f"      {race.upper()} {character_class.upper()}")
print(f"{'='*40}")
print(f"HP      : {final_hp:>3}")
print(f"MP      : {final_mp:>3}")
print(f"Attack  : {final_attack:>3}")
print(f"Defense : {final_defense:>3}")
print(f"Speed   : {final_speed:>3}")
print(f"Weapon  : {weapon}")
print(f"Special : {special_skill}")
print(f"Trait   : {trait}")
print(f"Rating  : {combat_rating} ({rank})")
print(f"{'='*40}")
''')
print()

# E2. Hệ thống tính toán tỷ số trận đấu
print("E2. Hệ thống tính toán tỷ số trận đấu:")
print("Code mẫu:")
print('''
print("=== DỰ ĐOÁN TRẬN ĐẤU BÓNG ĐÁ ===")

# Thông tin đội
team_a = "Manchester United"
team_b = "Liverpool"

# Chỉ số sức mạnh (0-100)
attack_a = 85
defense_a = 75
midfield_a = 80
form_a = 70  # Phong độ gần đây

attack_b = 90
defense_b = 80
midfield_b = 85
form_b = 85

# Yếu tố khác
home_advantage = True  # Đội A đá sân nhà
weather = "sunny"  # sunny, rainy, windy
importance = "normal"  # friendly, normal, important, final

# Tính điểm tổng thể
total_a = (attack_a + defense_a + midfield_a + form_a) / 4
total_b = (attack_b + defense_b + midfield_b + form_b) / 4

# Điều chỉnh theo sân nhà
if home_advantage:
    total_a += 5
    print(f"{team_a} được +5 điểm (sân nhà)")

# Điều chỉnh theo thời tiết
if weather == "rainy":
    # Thời tiết xấu ảnh hưởng đội kỹ thuật cao
    if attack_a > attack_b:
        total_a -= 3
    else:
        total_b -= 3
    print("Thời tiết mưa: -3 điểm cho đội kỹ thuật cao")

# Điều chỉnh theo tầm quan trọng
if importance == "final":
    # Chung kết: phong độ quan trọng hơn
    total_a = total_a * 0.7 + form_a * 0.3
    total_b = total_b * 0.7 + form_b * 0.3
    print("Trận chung kết: Phong độ được tính trọng số cao hơn")

# Tính xác suất
diff = total_a - total_b
if diff > 10:
    prob_a_win = 75
    prob_draw = 15
    prob_b_win = 10
elif diff > 5:
    prob_a_win = 60
    prob_draw = 25
    prob_b_win = 15
elif diff > -5:
    prob_a_win = 45
    prob_draw = 30
    prob_b_win = 25
elif diff > -10:
    prob_a_win = 25
    prob_draw = 25
    prob_b_win = 50
else:
    prob_a_win = 15
    prob_draw = 20
    prob_b_win = 65

# Dự đoán tỷ số
if prob_a_win > 50:
    if attack_a > 80:
        predicted_score = "3-1"
    else:
        predicted_score = "2-0"
    result = f"{team_a} thắng"
elif prob_b_win > 50:
    if attack_b > 80:
        predicted_score = "1-3"
    else:
        predicted_score = "0-2"
    result = f"{team_b} thắng"
else:
    if (attack_a + attack_b) / 2 > 75:
        predicted_score = "2-2"
    else:
        predicted_score = "1-1"
    result = "Hòa"

print(f"\\n{'='*50}")
print(f"        {team_a} vs {team_b}")
print(f"{'='*50}")
print(f"Chỉ số {team_a}: {total_a:.1f}")
print(f"Chỉ số {team_b}: {total_b:.1f}")
print(f"\\nXác suất:")
print(f"  {team_a} thắng: {prob_a_win}%")
print(f"  Hòa          : {prob_draw}%")
print(f"  {team_b} thắng: {prob_b_win}%")
print(f"\\nDự đoán: {result}")
print(f"Tỷ số dự kiến: {predicted_score}")
print(f"{'='*50}")
''')
print()

# BÀI TẬP TỰ LÀM E:
print("*** BÀI TẬP TỰ LÀM E ***")
print("1. Game đoán từ với gợi ý thông minh")
print("2. Hệ thống ranking chess/game theo ELO")
print("3. Máy tính tử vi/cung hoàng đạo vui")
print()

# ===============================================
# TỔNG KẾT VÀ THÁCH THỨC
# ===============================================
print("=== TỔNG KẾT PHẦN ỨNG DỤNG THỰC TẾ ===")
print()
print("Bạn đã học cách áp dụng if/else vào:")
print("✓ Hệ thống thương mại điện tử")
print("✓ Ứng dụng ngân hàng tài chính")
print("✓ Hệ thống y tế sức khỏe")
print("✓ Phần mềm giáo dục")
print("✓ Game và giải trí")
print()
print("THÁCH THỨC CUỐI CÙNG:")
print("Chọn 1 lĩnh vực yêu thích và tạo ứng dụng hoàn chỉnh")
print("với đầy đủ: input validation, xử lý lỗi, output đẹp!")
print()
print("=" * 60) 