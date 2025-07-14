# ===============================================
# NGÀY 5-6: DỰ ÁN THỰC HÀNH NÂNG CAO
# Hệ thống quản lý bán hàng thông minh
# ===============================================

print("=== HỆ THỐNG QUẢN LÝ BÁN HÀNG THÔNG MINH ===")
print("Dự án tổng hợp tất cả kiến thức if/else đã học!")
print()

# ===============================================
# DATABASE SẢN PHẨM VÀ KHÁCH HÀNG
# ===============================================

# Cơ sở dữ liệu sản phẩm
san_pham = {
    "SP001": {
        "ten": "iPhone 15 Pro",
        "gia": 25000000,
        "loai": "dien_thoai",
        "so_luong": 50,
        "giam_gia": 5,  # %
        "rating": 4.8,
        "thuong_hieu": "Apple"
    },
    "SP002": {
        "ten": "MacBook Air M2",
        "gia": 35000000,
        "loai": "laptop",
        "so_luong": 20,
        "giam_gia": 8,
        "rating": 4.9,
        "thuong_hieu": "Apple"
    },
    "SP003": {
        "ten": "Samsung Galaxy S24",
        "gia": 22000000,
        "loai": "dien_thoai",
        "so_luong": 30,
        "giam_gia": 10,
        "rating": 4.7,
        "thuong_hieu": "Samsung"
    },
    "SP004": {
        "ten": "Dell XPS 13",
        "gia": 28000000,
        "loai": "laptop",
        "so_luong": 15,
        "giam_gia": 0,
        "rating": 4.6,
        "thuong_hieu": "Dell"
    },
    "SP005": {
        "ten": "AirPods Pro 2",
        "gia": 6000000,
        "loai": "phu_kien",
        "so_luong": 100,
        "giam_gia": 15,
        "rating": 4.5,
        "thuong_hieu": "Apple"
    }
}

# Cơ sở dữ liệu khách hàng
khach_hang = {
    "KH001": {
        "ten": "Nguyễn Văn An",
        "loai": "vip",  # thuong, vip, premium
        "so_lan_mua": 25,
        "tong_chi_tieu": 150000000,
        "diem_tich_luy": 1500,
        "ngay_sinh": "15/03/1990"
    },
    "KH002": {
        "ten": "Trần Thị Bình",
        "loai": "premium",
        "so_lan_mua": 50,
        "tong_chi_tieu": 300000000,
        "diem_tich_luy": 3000,
        "ngay_sinh": "22/07/1985"
    },
    "KH003": {
        "ten": "Lê Văn Cường",
        "loai": "thuong",
        "so_lan_mua": 5,
        "tong_chi_tieu": 15000000,
        "diem_tich_luy": 150,
        "ngay_sinh": "08/12/1995"
    }
}

# ===============================================
# HÀM HIỂN THỊ MENU VÀ SẢN PHẨM
# ===============================================

def hien_thi_menu():
    print("\n" + "="*50)
    print("         MENU HỆ THỐNG BÁN HÀNG")
    print("="*50)
    print("1. Xem danh sách sản phẩm")
    print("2. Tìm kiếm sản phẩm")
    print("3. Thêm vào giỏ hàng")
    print("4. Xem giỏ hàng")
    print("5. Thanh toán")
    print("6. Quản lý khách hàng")
    print("7. Báo cáo bán hàng")
    print("0. Thoát")
    print("="*50)

def hien_thi_san_pham():
    print("\n" + "="*80)
    print("                        DANH SÁCH SẢN PHẨM")
    print("="*80)
    print(f"{'Mã':<8} {'Tên':<20} {'Giá':<15} {'Loại':<12} {'SL':<5} {'Rating':<8} {'Giảm giá'}")
    print("-"*80)
    
    for ma, sp in san_pham.items():
        gia_format = f"{sp['gia']:,}đ"
        giam_gia_text = f"{sp['giam_gia']}%" if sp['giam_gia'] > 0 else "Không"
        
        # Highlight sản phẩm hot
        if sp['rating'] >= 4.8 or sp['giam_gia'] >= 10:
            hot_mark = "🔥"
        else:
            hot_mark = "  "
            
        print(f"{ma:<8} {sp['ten']:<20} {gia_format:<15} {sp['loai']:<12} {sp['so_luong']:<5} {sp['rating']:<8} {giam_gia_text} {hot_mark}")
    
    print("="*80)

# ===============================================
# HÀM TÌM KIẾM THÔNG MINH
# ===============================================

def tim_kiem_san_pham():
    print("\n=== TÌM KIẾM SẢN PHẨM ===")
    print("1. Tìm theo tên")
    print("2. Tìm theo giá")
    print("3. Tìm theo loại")
    print("4. Tìm theo thương hiệu")
    print("5. Tìm sản phẩm hot")
    
    lua_chon = input("\nChọn cách tìm kiếm: ")
    
    if lua_chon == "1":
        tu_khoa = input("Nhập tên sản phẩm: ").lower()
        ket_qua = []
        for ma, sp in san_pham.items():
            if tu_khoa in sp['ten'].lower():
                ket_qua.append((ma, sp))
        
        if ket_qua:
            print(f"\nTìm thấy {len(ket_qua)} sản phẩm:")
            for ma, sp in ket_qua:
                print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ")
        else:
            print("Không tìm thấy sản phẩm nào!")
            
    elif lua_chon == "2":
        try:
            gia_min = int(input("Giá tối thiểu: "))
            gia_max = int(input("Giá tối đa: "))
            
            ket_qua = []
            for ma, sp in san_pham.items():
                if gia_min <= sp['gia'] <= gia_max:
                    ket_qua.append((ma, sp))
            
            if ket_qua:
                print(f"\nTìm thấy {len(ket_qua)} sản phẩm trong khoảng giá:")
                # Sắp xếp theo giá
                ket_qua.sort(key=lambda x: x[1]['gia'])
                for ma, sp in ket_qua:
                    print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ")
            else:
                print("Không có sản phẩm nào trong khoảng giá này!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
            
    elif lua_chon == "3":
        print("Loại sản phẩm: dien_thoai, laptop, phu_kien")
        loai = input("Nhập loại sản phẩm: ").lower()
        
        ket_qua = [(ma, sp) for ma, sp in san_pham.items() if sp['loai'] == loai]
        
        if ket_qua:
            print(f"\nSản phẩm loại '{loai}':")
            for ma, sp in ket_qua:
                print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ")
        else:
            print("Không có sản phẩm loại này!")
            
    elif lua_chon == "4":
        thuong_hieu = input("Nhập thương hiệu: ")
        
        ket_qua = [(ma, sp) for ma, sp in san_pham.items() 
                  if sp['thuong_hieu'].lower() == thuong_hieu.lower()]
        
        if ket_qua:
            print(f"\nSản phẩm thương hiệu '{thuong_hieu}':")
            for ma, sp in ket_qua:
                print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ")
        else:
            print("Không có sản phẩm thương hiệu này!")
            
    elif lua_chon == "5":
        print("\n🔥 SẢN PHẨM HOT:")
        for ma, sp in san_pham.items():
            if sp['rating'] >= 4.8 or sp['giam_gia'] >= 10:
                ly_do = []
                if sp['rating'] >= 4.8:
                    ly_do.append(f"Rating {sp['rating']}")
                if sp['giam_gia'] >= 10:
                    ly_do.append(f"Giảm {sp['giam_gia']}%")
                
                print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ ({', '.join(ly_do)})")

# ===============================================
# HỆ THỐNG GIỎ HÀNG THÔNG MINH
# ===============================================

gio_hang = {}  # {ma_sp: so_luong}

def them_vao_gio_hang():
    hien_thi_san_pham()
    ma_sp = input("\nNhập mã sản phẩm: ").upper()
    
    if ma_sp not in san_pham:
        print("Mã sản phẩm không tồn tại!")
        return
    
    sp = san_pham[ma_sp]
    
    # Kiểm tra tồn kho
    if sp['so_luong'] == 0:
        print(f"Sản phẩm '{sp['ten']}' đã hết hàng!")
        return
    
    try:
        so_luong = int(input(f"Nhập số lượng (còn {sp['so_luong']}): "))
        
        if so_luong <= 0:
            print("Số lượng phải > 0!")
            return
            
        # Kiểm tra số lượng trong giỏ + số lượng muốn thêm
        so_luong_trong_gio = gio_hang.get(ma_sp, 0)
        tong_so_luong = so_luong_trong_gio + so_luong
        
        if tong_so_luong > sp['so_luong']:
            print(f"Không đủ hàng! Tối đa có thể thêm {sp['so_luong'] - so_luong_trong_gio}")
            return
        
        # Thêm vào giỏ hàng
        gio_hang[ma_sp] = tong_so_luong
        print(f"✅ Đã thêm {so_luong} {sp['ten']} vào giỏ hàng!")
        
        # Gợi ý sản phẩm liên quan
        goi_y_san_pham_lien_quan(ma_sp)
        
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

def goi_y_san_pham_lien_quan(ma_sp_goc):
    sp_goc = san_pham[ma_sp_goc]
    print(f"\n💡 Sản phẩm liên quan đến '{sp_goc['ten']}':")
    
    dem = 0
    for ma, sp in san_pham.items():
        if ma != ma_sp_goc and dem < 3:
            # Gợi ý theo loại hoặc thương hiệu
            if (sp['loai'] == sp_goc['loai'] or 
                sp['thuong_hieu'] == sp_goc['thuong_hieu']):
                print(f"- {ma}: {sp['ten']} - {sp['gia']:,}đ")
                dem += 1

def xem_gio_hang():
    if not gio_hang:
        print("\n🛒 Giỏ hàng trống!")
        return
    
    print("\n" + "="*70)
    print("                        GIỎ HÀNG CỦA BẠN")
    print("="*70)
    print(f"{'Mã':<8} {'Tên':<25} {'SL':<5} {'Đơn giá':<15} {'Thành tiền'}")
    print("-"*70)
    
    tong_tien = 0
    
    for ma_sp, so_luong in gio_hang.items():
        sp = san_pham[ma_sp]
        don_gia = sp['gia']
        
        # Áp dụng giảm giá
        if sp['giam_gia'] > 0:
            don_gia = don_gia * (100 - sp['giam_gia']) / 100
        
        thanh_tien = don_gia * so_luong
        tong_tien += thanh_tien
        
        gia_format = f"{don_gia:,.0f}đ"
        thanh_tien_format = f"{thanh_tien:,.0f}đ"
        
        print(f"{ma_sp:<8} {sp['ten']:<25} {so_luong:<5} {gia_format:<15} {thanh_tien_format}")
    
    print("-"*70)
    print(f"{'TỔNG CỘNG:':<43} {tong_tien:,.0f}đ")
    print("="*70)
    
    return tong_tien

# ===============================================
# HỆ THỐNG THANH TOÁN NÂNG CAO
# ===============================================

def thanh_toan():
    if not gio_hang:
        print("Giỏ hàng trống! Không thể thanh toán.")
        return
    
    print("\n=== THANH TOÁN ===")
    
    # Hiển thị giỏ hàng
    tong_tien_hang = xem_gio_hang()
    
    # Nhập thông tin khách hàng
    print("\nThông tin khách hàng:")
    ma_kh = input("Mã khách hàng (Enter nếu khách lẻ): ").upper()
    
    # Xác định loại khách hàng
    if ma_kh and ma_kh in khach_hang:
        kh = khach_hang[ma_kh]
        loai_kh = kh['loai']
        diem_hien_tai = kh['diem_tich_luy']
        print(f"Chào {kh['ten']} - Khách hàng {loai_kh.upper()}")
        print(f"Điểm tích lũy hiện tại: {diem_hien_tai}")
    else:
        loai_kh = "le"
        diem_hien_tai = 0
        print("Khách hàng lẻ")
    
    # Tính toán giảm giá
    giam_gia_kh = tinh_giam_gia_khach_hang(loai_kh, tong_tien_hang)
    giam_gia_combo = tinh_giam_gia_combo()
    giam_gia_diem = 0
    
    # Sử dụng điểm tích lũy
    if diem_hien_tai > 0:
        su_dung_diem = input(f"Sử dụng điểm tích lũy? (y/n): ").lower()
        if su_dung_diem == 'y':
            max_diem = min(diem_hien_tai, int(tong_tien_hang / 1000))  # 1 điểm = 1k
            diem_su_dung = int(input(f"Sử dụng bao nhiêu điểm (tối đa {max_diem}): "))
            if 0 <= diem_su_dung <= max_diem:
                giam_gia_diem = diem_su_dung * 1000
            else:
                print("Số điểm không hợp lệ!")
                diem_su_dung = 0
        else:
            diem_su_dung = 0
    else:
        diem_su_dung = 0
    
    # Tính phí vận chuyển
    phi_van_chuyen = tinh_phi_van_chuyen(tong_tien_hang, loai_kh)
    
    # Tính tổng thanh toán
    tong_giam_gia = giam_gia_kh + giam_gia_combo + giam_gia_diem
    tong_thanh_toan = tong_tien_hang - tong_giam_gia + phi_van_chuyen
    
    # In hóa đơn
    in_hoa_don(tong_tien_hang, giam_gia_kh, giam_gia_combo, 
               giam_gia_diem, phi_van_chuyen, tong_thanh_toan)
    
    # Xác nhận thanh toán
    xac_nhan = input("\nXác nhận thanh toán? (y/n): ").lower()
    if xac_nhan == 'y':
        xu_ly_thanh_toan(ma_kh, diem_su_dung, tong_thanh_toan)
        print("✅ Thanh toán thành công!")
        gio_hang.clear()
    else:
        print("❌ Đã hủy thanh toán!")

def tinh_giam_gia_khach_hang(loai_kh, tong_tien):
    if loai_kh == "premium":
        return min(tong_tien * 0.15, 5000000)  # 15%, tối đa 5tr
    elif loai_kh == "vip":
        return min(tong_tien * 0.10, 3000000)  # 10%, tối đa 3tr
    else:
        return 0

def tinh_giam_gia_combo():
    # Kiểm tra combo Apple (iPhone + MacBook + AirPods)
    co_iphone = any(san_pham[ma]['thuong_hieu'] == 'Apple' and 
                   san_pham[ma]['loai'] == 'dien_thoai' 
                   for ma in gio_hang.keys())
    co_macbook = any(san_pham[ma]['thuong_hieu'] == 'Apple' and 
                    san_pham[ma]['loai'] == 'laptop' 
                    for ma in gio_hang.keys())
    co_airpods = any(san_pham[ma]['ten'] == 'AirPods Pro 2' 
                    for ma in gio_hang.keys())
    
    if co_iphone and co_macbook and co_airpods:
        print("🎉 COMBO APPLE: Giảm 2 triệu!")
        return 2000000
    elif co_iphone and co_airpods:
        print("🎉 COMBO MINI: Giảm 500k!")
        return 500000
    else:
        return 0

def tinh_phi_van_chuyen(tong_tien, loai_kh):
    if tong_tien >= 5000000:  # Đơn hàng >= 5tr
        return 0
    elif loai_kh in ["vip", "premium"]:
        return 30000  # Giảm 50% cho VIP
    else:
        return 60000  # Phí chuẩn

def in_hoa_don(tong_hang, giam_gia_kh, giam_gia_combo, 
               giam_gia_diem, phi_ship, tong_thanh_toan):
    print("\n" + "="*50)
    print("                   HÓA ĐƠN")
    print("="*50)
    print(f"Tổng tiền hàng:        {tong_hang:>15,}đ")
    
    if giam_gia_kh > 0:
        print(f"Giảm giá khách hàng:   -{giam_gia_kh:>14,}đ")
    if giam_gia_combo > 0:
        print(f"Giảm giá combo:        -{giam_gia_combo:>14,}đ")
    if giam_gia_diem > 0:
        print(f"Sử dụng điểm:          -{giam_gia_diem:>14,}đ")
    
    print(f"Phí vận chuyển:        +{phi_ship:>14,}đ")
    print("-"*50)
    print(f"TỔNG THANH TOÁN:       {tong_thanh_toan:>15,}đ")
    print("="*50)

def xu_ly_thanh_toan(ma_kh, diem_su_dung, tong_thanh_toan):
    # Cập nhật tồn kho
    for ma_sp, so_luong in gio_hang.items():
        san_pham[ma_sp]['so_luong'] -= so_luong
    
    # Cập nhật thông tin khách hàng
    if ma_kh and ma_kh in khach_hang:
        kh = khach_hang[ma_kh]
        kh['so_lan_mua'] += 1
        kh['tong_chi_tieu'] += tong_thanh_toan
        kh['diem_tich_luy'] -= diem_su_dung
        kh['diem_tich_luy'] += int(tong_thanh_toan / 100000)  # 1 điểm/100k
        
        # Nâng cấp hạng khách hàng
        nang_cap_hang_khach_hang(ma_kh)

def nang_cap_hang_khach_hang(ma_kh):
    kh = khach_hang[ma_kh]
    hang_cu = kh['loai']
    
    if kh['tong_chi_tieu'] >= 200000000 and kh['so_lan_mua'] >= 30:
        kh['loai'] = 'premium'
    elif kh['tong_chi_tieu'] >= 50000000 and kh['so_lan_mua'] >= 10:
        kh['loai'] = 'vip'
    else:
        kh['loai'] = 'thuong'
    
    if kh['loai'] != hang_cu:
        print(f"🎉 Chúc mừng! Bạn đã được nâng cấp lên {kh['loai'].upper()}!")

# ===============================================
# CHƯƠNG TRÌNH CHÍNH
# ===============================================

def chuong_trinh_chinh():
    print("Chào mừng đến với Hệ thống Bán hàng Thông minh!")
    print("Được phát triển bằng Python với if/else statements")
    
    while True:
        hien_thi_menu()
        lua_chon = input("\nChọn chức năng: ")
        
        if lua_chon == "1":
            hien_thi_san_pham()
            
        elif lua_chon == "2":
            tim_kiem_san_pham()
            
        elif lua_chon == "3":
            them_vao_gio_hang()
            
        elif lua_chon == "4":
            xem_gio_hang()
            
        elif lua_chon == "5":
            thanh_toan()
            
        elif lua_chon == "6":
            quan_ly_khach_hang()
            
        elif lua_chon == "7":
            bao_cao_ban_hang()
            
        elif lua_chon == "0":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

def quan_ly_khach_hang():
    print("\n=== QUẢN LÝ KHÁCH HÀNG ===")
    print("1. Xem danh sách khách hàng")
    print("2. Thêm khách hàng mới")
    print("3. Tìm kiếm khách hàng")
    
    lua_chon = input("Chọn chức năng: ")
    
    if lua_chon == "1":
        print("\n" + "="*80)
        print("                           DANH SÁCH KHÁCH HÀNG")
        print("="*80)
        print(f"{'Mã':<8} {'Tên':<20} {'Loại':<10} {'Lần mua':<10} {'Chi tiêu':<15} {'Điểm'}")
        print("-"*80)
        
        for ma, kh in khach_hang.items():
            chi_tieu_format = f"{kh['tong_chi_tieu']:,}đ"
            print(f"{ma:<8} {kh['ten']:<20} {kh['loai']:<10} {kh['so_lan_mua']:<10} {chi_tieu_format:<15} {kh['diem_tich_luy']}")
        print("="*80)

def bao_cao_ban_hang():
    print("\n=== BÁO CÁO BÁN HÀNG ===")
    
    # Thống kê sản phẩm
    print("1. SẢN PHẨM BÁN CHẠY:")
    san_pham_ban_chay = sorted(san_pham.items(), 
                              key=lambda x: (100 - x[1]['so_luong']), 
                              reverse=True)[:3]
    
    for i, (ma, sp) in enumerate(san_pham_ban_chay, 1):
        da_ban = 100 - sp['so_luong']  # Giả sử ban đầu mỗi sản phẩm có 100
        print(f"   {i}. {sp['ten']}: {da_ban} sản phẩm")
    
    # Thống kê khách hàng
    print("\n2. KHÁCH HÀNG VIP:")
    kh_vip = [(ma, kh) for ma, kh in khach_hang.items() 
              if kh['loai'] in ['vip', 'premium']]
    
    for ma, kh in kh_vip:
        print(f"   - {kh['ten']} ({kh['loai']}): {kh['tong_chi_tieu']:,}đ")
    
    # Thống kê doanh thu
    tong_doanh_thu = sum(kh['tong_chi_tieu'] for kh in khach_hang.values())
    print(f"\n3. TỔNG DOANH THU: {tong_doanh_thu:,}đ")

# ===============================================
# CHẠY CHƯƠNG TRÌNH
# ===============================================

if __name__ == "__main__":
    print("=== HỆ THỐNG DEMO - NGÀY 5-6 ===")
    print("Dự án này tổng hợp tất cả kiến thức if/else:")
    print("✓ Điều kiện đơn giản và phức tạp")
    print("✓ Nested if và elif chains")
    print("✓ Toán tử logic (and, or, not)")
    print("✓ Input validation và error handling")
    print("✓ Dictionary và list operations")
    print("✓ String processing và formatting")
    print("✓ Business logic thực tế")
    print()
    
    demo = input("Chạy demo? (y/n): ").lower()
    if demo == 'y':
        chuong_trinh_chinh()
    else:
        print("Hãy đọc code để hiểu cách implement!")
        print("Đây là ví dụ tuyệt vời về if/else trong thực tế!")

print("\n" + "="*60)
print("TỔNG KẾT DỰ ÁN")
print("="*60)
print("Bạn đã thấy cách sử dụng if/else trong:")
print("✓ Validation dữ liệu đầu vào")
print("✓ Business logic phức tạp")
print("✓ Hệ thống giảm giá và khuyến mãi")
print("✓ Quản lý trạng thái và workflow")
print("✓ Xử lý nhiều điều kiện đồng thời")
print("✓ Optimization và performance")
print()
print("Đây là foundation để build các ứng dụng lớn hơn!")
print("Hãy tự build thêm các features khác:")
print("- Quản lý nhân viên")
print("- Báo cáo chi tiết")
print("- API integration")
print("- Database connection")
print("=" * 60) 