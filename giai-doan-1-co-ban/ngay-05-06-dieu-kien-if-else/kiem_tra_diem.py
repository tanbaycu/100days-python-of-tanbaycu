# kiem_tra_diem.py - Hệ thống phân loại điểm
# File cần nộp cho ngày 5-6

print("HỆ THỐNG PHÂN LOẠI ĐIỂM")
print("=" * 40)

# Nhận thông tin từ học sinh
print("Nhập thông tin học sinh:")
ten_hoc_sinh = input("Tên học sinh: ").strip()
lop = input("Lớp: ").strip()

# Validation tên không rỗng
if not ten_hoc_sinh:
    ten_hoc_sinh = "Học sinh"
if not lop:
    lop = "Chưa rõ"

print(f"\nThông tin: {ten_hoc_sinh} - Lớp {lop}")
print("-" * 40)

# Nhập điểm các môn
print("Nhập điểm các môn học (thang điểm 10):")

try:
    diem_toan = float(input("Điểm Toán: "))
    diem_ly = float(input("Điểm Lý: "))
    diem_hoa = float(input("Điểm Hóa: "))
    diem_van = float(input("Điểm Văn: "))
    diem_anh = float(input("Điểm Anh: "))
    
    # Kiểm tra điểm hợp lệ (0-10)
    danh_sach_diem = [diem_toan, diem_ly, diem_hoa, diem_van, diem_anh]
    ten_mon = ["Toán", "Lý", "Hóa", "Văn", "Anh"]
    
    diem_hop_le = True
    for i, diem in enumerate(danh_sach_diem):
        if not (0 <= diem <= 10):
            print(f"Lỗi: Điểm {ten_mon[i]} không hợp lệ ({diem}). Phải từ 0-10.")
            diem_hop_le = False
    
    if not diem_hop_le:
        print("Vui lòng chạy lại chương trình với điểm hợp lệ!")
    else:
        # Tính điểm trung bình
        diem_trung_binh = sum(danh_sach_diem) / len(danh_sach_diem)
        
        print("\n" + "=" * 40)
        print("KẾT QUẢ HỌC TẬP")
        print("=" * 40)
        
        # Hiển thị điểm từng môn với phân loại
        for i, diem in enumerate(danh_sach_diem):
            if diem >= 8.5:
                xep_loai = "Giỏi"
            elif diem >= 7.0:
                xep_loai = "Khá"
            elif diem >= 5.0:
                xep_loai = "Trung bình"
            elif diem >= 3.5:
                xep_loai = "Yếu"
            else:
                xep_loai = "Kém"
            
            print(f"{ten_mon[i]}: {diem}/10 - {xep_loai}")
        
        print("-" * 40)
        print(f"Điểm trung bình: {diem_trung_binh:.2f}/10")
        
        # Xếp loại tổng kết
        if diem_trung_binh >= 8.5:
            xep_loai_chung = "GIỎI"
            nhan_xet = "Xuất sắc! Hãy tiếp tục phát huy!"
        elif diem_trung_binh >= 7.0:
            xep_loai_chung = "KHÁ"
            nhan_xet = "Tốt! Cố gắng thêm một chút nữa!"
        elif diem_trung_binh >= 5.0:
            xep_loai_chung = "TRUNG BÌNH"
            nhan_xet = "Cần cố gắng hơn nữa!"
        elif diem_trung_binh >= 3.5:
            xep_loai_chung = "YẾU"
            nhan_xet = "Cần học tập chăm chỉ hơn!"
        else:
            xep_loai_chung = "KÉM"
            nhan_xet = "Cần có kế hoạch học tập mới!"
        
        print(f"Xếp loại: {xep_loai_chung}")
        print(f"Nhận xét: {nhan_xet}")
        
        # Phân tích chi tiết
        print("\n" + "-" * 40)
        print("PHÂN TÍCH CHI TIẾT")
        print("-" * 40)
        
        # Đếm số môn từng loại
        so_mon_gioi = sum(1 for diem in danh_sach_diem if diem >= 8.5)
        so_mon_kha = sum(1 for diem in danh_sach_diem if 7.0 <= diem < 8.5)
        so_mon_tb = sum(1 for diem in danh_sach_diem if 5.0 <= diem < 7.0)
        so_mon_yeu = sum(1 for diem in danh_sach_diem if 3.5 <= diem < 5.0)
        so_mon_kem = sum(1 for diem in danh_sach_diem if diem < 3.5)
        
        print(f"Số môn Giỏi: {so_mon_gioi}")
        print(f"Số môn Khá: {so_mon_kha}")
        print(f"Số môn Trung bình: {so_mon_tb}")
        print(f"Số môn Yếu: {so_mon_yeu}")
        print(f"Số môn Kém: {so_mon_kem}")
        
        # Tìm môn cao nhất và thấp nhất
        diem_cao_nhat = max(danh_sach_diem)
        diem_thap_nhat = min(danh_sach_diem)
        
        mon_cao_nhat = [ten_mon[i] for i, diem in enumerate(danh_sach_diem) if diem == diem_cao_nhat]
        mon_thap_nhat = [ten_mon[i] for i, diem in enumerate(danh_sach_diem) if diem == diem_thap_nhat]
        
        print(f"Môn điểm cao nhất: {', '.join(mon_cao_nhat)} ({diem_cao_nhat})")
        print(f"Môn điểm thấp nhất: {', '.join(mon_thap_nhat)} ({diem_thap_nhat})")
        
        # Đánh giá khả năng học tập
        print("\n" + "-" * 40)
        print("ĐÁNH GIÁ VÀ KHUYẾN NGHỊ")
        print("-" * 40)
        
        if so_mon_kem > 0:
            print("⚠️ Cảnh báo: Có môn điểm kém, cần cải thiện ngay!")
        elif so_mon_yeu > 2:
            print("📢 Lưu ý: Có nhiều môn yếu, cần tăng cường học tập!")
        elif so_mon_gioi >= 3:
            print("🌟 Tuyệt vời! Học lực rất tốt, hãy duy trì!")
        else:
            print("👍 Học lực ổn định, cố gắng cải thiện thêm!")
        
        # Khuyến nghị cụ thể
        if diem_toan < 5.0:
            print("- Nên tăng cường học Toán (môn cơ bản quan trọng)")
        if diem_van < 5.0:
            print("- Cần cải thiện kỹ năng Văn (đọc hiểu, viết)")
        if diem_anh < 5.0:
            print("- Nên luyện tập Tiếng Anh thường xuyên hơn")
        
        # Kiểm tra điều kiện lên lớp
        print("\n" + "-" * 40)
        print("ĐIỀU KIỆN LÊN LỚP")
        print("-" * 40)
        
        if diem_trung_binh >= 5.0 and so_mon_kem == 0 and so_mon_yeu <= 2:
            print("✅ ĐẠT điều kiện lên lớp")
            if diem_trung_binh >= 8.0 and so_mon_gioi >= 3:
                print("🏆 Đủ điều kiện xét học sinh giỏi")
            elif diem_trung_binh >= 6.5 and so_mon_kha >= 2:
                print("🎖️ Đủ điều kiện xét học sinh khá")
        else:
            print("❌ CHƯA ĐẠT điều kiện lên lớp")
            print("Cần:")
            if diem_trung_binh < 5.0:
                print("- Điểm trung bình ≥ 5.0")
            if so_mon_kem > 0:
                print("- Không có môn điểm kém")
            if so_mon_yeu > 2:
                print("- Tối đa 2 môn điểm yếu")

except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ cho điểm!")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

print("\n" + "=" * 40)
print("CẢM ƠN BẠN ĐÃ SỬ DỤNG HỆ THỐNG!")
print("Chúc bạn học tập tốt!")
print("=" * 40) 