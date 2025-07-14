# ===============================================
# NGÀY 5-6: QUIZ TƯƠNG TÁC VỀ ĐIỀU KIỆN IF/ELSE
# Mục tiêu: Kiểm tra kiến thức với trải nghiệm tương tác
# ===============================================

try:
    from colorama import init, Fore, Back, Style
    init()  # Khởi tạo colorama
    COLORAMA_AVAILABLE = True
except ImportError:
    # Nếu không có colorama, tạo các hằng số rỗng
    COLORAMA_AVAILABLE = False
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = Back = Style = DummyColor()

import random
import time
import sys

# ===============================================
# HỆTHỐNG QUẢN LÝ QUIZ
# ===============================================

class QuizManager:
    def __init__(self):
        self.diem_so = 0
        self.tong_cau = 0
        self.dap_an_dung = []
        self.dap_an_sai = []
        self.thoi_gian_bat_dau = time.time()
        
    def hien_thi_header(self):
        if COLORAMA_AVAILABLE:
            print(Fore.CYAN + "=" * 60)
            print(Fore.YELLOW + "🎯 QUIZ TƯƠNG TÁC VỀ ĐIỀU KIỆN IF/ELSE 🎯")
            print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        else:
            print("=" * 60)
            print("QUIZ TUONG TAC VE DIEU KIEN IF/ELSE")
            print("=" * 60)
        
        print("📚 Kiểm tra kiến thức từ cơ bản đến nâng cao!")
        print("⏰ Không giới hạn thời gian - tập trung vào chất lượng")
        print("🎮 Trải nghiệm tương tác từng câu hỏi")
        print()
    
    def hien_thi_tien_do(self):
        if COLORAMA_AVAILABLE:
            print(Fore.MAGENTA + f"📊 Điểm hiện tại: {self.diem_so}/{self.tong_cau}" + Style.RESET_ALL)
        else:
            print(f"Diem hien tai: {self.diem_so}/{self.tong_cau}")
        
        if self.tong_cau > 0:
            ty_le = (self.diem_so / self.tong_cau) * 100
            if ty_le >= 80:
                mau = Fore.GREEN if COLORAMA_AVAILABLE else ""
                bieu_tuong = "🌟"
            elif ty_le >= 60:
                mau = Fore.YELLOW if COLORAMA_AVAILABLE else ""
                bieu_tuong = "👍"
            else:
                mau = Fore.RED if COLORAMA_AVAILABLE else ""
                bieu_tuong = "💪"
            
            reset = Style.RESET_ALL if COLORAMA_AVAILABLE else ""
            print(f"{mau}📈 Tỷ lệ đúng: {ty_le:.1f}% {bieu_tuong}{reset}")
        print()
    
    def kiem_tra_dap_an(self, dap_an_user, dap_an_dung, giai_thich=""):
        self.tong_cau += 1
        
        if dap_an_user.upper() == dap_an_dung.upper():
            self.diem_so += 1
            self.dap_an_dung.append(self.tong_cau)
            
            if COLORAMA_AVAILABLE:
                print(Fore.GREEN + "✅ ĐÚNG! Tuyệt vời!" + Style.RESET_ALL)
            else:
                print("DUNG! Tuyet voi!")
            
            if giai_thich:
                if COLORAMA_AVAILABLE:
                    print(Fore.CYAN + f"💡 Giải thích: {giai_thich}" + Style.RESET_ALL)
                else:
                    print(f"Giai thich: {giai_thich}")
        else:
            self.dap_an_sai.append(self.tong_cau)
            
            if COLORAMA_AVAILABLE:
                print(Fore.RED + f"❌ SAI! Đáp án đúng là: {dap_an_dung}" + Style.RESET_ALL)
            else:
                print(f"SAI! Dap an dung la: {dap_an_dung}")
            
            if giai_thich:
                if COLORAMA_AVAILABLE:
                    print(Fore.YELLOW + f"📖 Giải thích: {giai_thich}" + Style.RESET_ALL)
                else:
                    print(f"Giai thich: {giai_thich}")
        
        print()
        time.sleep(1)  # Pause ngắn để đọc feedback
    
    def hien_thi_ket_qua_cuoi(self):
        thoi_gian_lam_bai = int(time.time() - self.thoi_gian_bat_dau)
        phut = thoi_gian_lam_bai // 60
        giay = thoi_gian_lam_bai % 60
        
        if COLORAMA_AVAILABLE:
            print(Fore.CYAN + "=" * 60)
            print(Fore.YELLOW + "🏆 KẾT QUẢ CUỐI CÙNG 🏆")
            print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        else:
            print("=" * 60)
            print("KET QUA CUOI CUNG")
            print("=" * 60)
        
        ty_le = (self.diem_so / self.tong_cau) * 100 if self.tong_cau > 0 else 0
        
        print(f"📊 Tổng câu hỏi: {self.tong_cau}")
        print(f"✅ Trả lời đúng: {self.diem_so}")
        print(f"❌ Trả lời sai: {self.tong_cau - self.diem_so}")
        print(f"⏰ Thời gian: {phut} phút {giay} giây")
        
        # Xếp loại
        if ty_le >= 90:
            xep_loai = "XUẤT SẮC 🌟"
            mau = Fore.GREEN if COLORAMA_AVAILABLE else ""
            nhan_xet = "Bạn đã thành thạo if/else! Sẵn sàng cho level tiếp theo!"
        elif ty_le >= 80:
            xep_loai = "GIỎI 👏"
            mau = Fore.CYAN if COLORAMA_AVAILABLE else ""
            nhan_xet = "Rất tốt! Chỉ cần ôn lại một vài điểm."
        elif ty_le >= 70:
            xep_loai = "KHÁ 👍"
            mau = Fore.YELLOW if COLORAMA_AVAILABLE else ""
            nhan_xet = "Tốt! Hãy practice thêm với các bài tập khó."
        elif ty_le >= 60:
            xep_loai = "TRUNG BÌNH 📚"
            mau = Fore.MAGENTA if COLORAMA_AVAILABLE else ""
            nhan_xet = "Cần ôn lại lý thuyết và làm thêm bài tập."
        else:
            xep_loai = "CẦN CỐ GẮNG 💪"
            mau = Fore.RED if COLORAMA_AVAILABLE else ""
            nhan_xet = "Hãy đọc lại lý thuyết và practice từ đầu."
        
        reset = Style.RESET_ALL if COLORAMA_AVAILABLE else ""
        print(f"{mau}🎯 Tỷ lệ đúng: {ty_le:.1f}%")
        print(f"🏅 Xếp loại: {xep_loai}{reset}")
        print(f"💬 Nhận xét: {nhan_xet}")
        
        # Gợi ý cải thiện
        if self.dap_an_sai:
            print(f"\n📝 Các câu cần ôn lại: {', '.join(map(str, self.dap_an_sai))}")
            
        print("\n🚀 Tiếp tục học tập và coding!")
        print("=" * 60)

# ===============================================
# CÂU HỎI TRẮC NGHIỆM
# ===============================================

def tao_danh_sach_cau_hoi():
    """Tạo danh sách tất cả câu hỏi trắc nghiệm"""
    
    cau_hoi = [
        # PHẦN CƠ BẢN (10 câu)
        {
            "id": 1,
            "phan": "Cơ bản",
            "noi_dung": "Kết quả của đoạn code sau là gì?\nx = 5\nif x > 3:\n    print('A')\nelse:\n    print('B')",
            "lua_chon": {"A": "A", "B": "B", "C": "Lỗi", "D": "Không in gì"},
            "dap_an": "A",
            "giai_thich": "x = 5 > 3 nên điều kiện đúng, in 'A'"
        },
        {
            "id": 2,
            "phan": "Cơ bản", 
            "noi_dung": "Cú pháp nào đúng để kiểm tra x bằng 10?",
            "lua_chon": {"A": "if x = 10:", "B": "if x == 10:", "C": "if x === 10:", "D": "if x is 10:"},
            "dap_an": "B",
            "giai_thich": "Dùng == để so sánh, = để gán giá trị"
        },
        {
            "id": 3,
            "phan": "Cơ bản",
            "noi_dung": "Toán tử nào dùng để kiểm tra 'không bằng'?",
            "lua_chon": {"A": "<>", "B": "!=", "C": "not=", "D": "!=="},
            "dap_an": "B", 
            "giai_thich": "!= là toán tử 'không bằng' trong Python"
        },
        {
            "id": 4,
            "phan": "Cơ bản",
            "noi_dung": "Kết quả của: 5 > 3 and 2 < 1",
            "lua_chon": {"A": "True", "B": "False", "C": "Lỗi", "D": "None"},
            "dap_an": "B",
            "giai_thich": "True and False = False (cả hai phải đúng)"
        },
        {
            "id": 5,
            "phan": "Cơ bản",
            "noi_dung": "Kết quả của: not True",
            "lua_chon": {"A": "True", "B": "False", "C": "1", "D": "0"},
            "dap_an": "B",
            "giai_thich": "not True = False"
        },
        {
            "id": 6,
            "phan": "Cơ bản",
            "noi_dung": "Trong Python, giá trị nào được coi là False?",
            "lua_chon": {"A": "0", "B": "''", "C": "[]", "D": "Tất cả đều đúng"},
            "dap_an": "D",
            "giai_thich": "0, chuỗi rỗng, list rỗng đều là False"
        },
        {
            "id": 7,
            "phan": "Cơ bản",
            "noi_dung": "Kết quả của: 'Python' in ['Java', 'Python', 'C++']",
            "lua_chon": {"A": "True", "B": "False", "C": "Lỗi", "D": "1"},
            "dap_an": "A",
            "giai_thich": "'Python' có trong list nên trả về True"
        },
        {
            "id": 8,
            "phan": "Cơ bản",
            "noi_dung": "Thứ tự ưu tiên của toán tử logic?",
            "lua_chon": {"A": "and > or > not", "B": "not > and > or", "C": "or > and > not", "D": "Không có thứ tự"},
            "dap_an": "B",
            "giai_thich": "not có ưu tiên cao nhất, sau đó and, cuối cùng or"
        },
        {
            "id": 9,
            "phan": "Cơ bản",
            "noi_dung": "Cách viết nào tương đương với: if not x == 5:",
            "lua_chon": {"A": "if x != 5:", "B": "if x <> 5:", "C": "if x not 5:", "D": "if x is not 5:"},
            "dap_an": "A",
            "giai_thich": "not x == 5 tương đương x != 5"
        },
        {
            "id": 10,
            "phan": "Cơ bản",
            "noi_dung": "Kết quả của: 10 % 3 == 1",
            "lua_chon": {"A": "True", "B": "False", "C": "1", "D": "3.33"},
            "dap_an": "A",
            "giai_thich": "10 chia 3 dư 1, nên 10 % 3 = 1"
        },
        
        # PHẦN NÂNG CAO (10 câu)
        {
            "id": 11,
            "phan": "Nâng cao",
            "noi_dung": "Kết quả của đoạn code?\nx = 0\nif x:\n    print('A')\nelif not x:\n    print('B')\nelse:\n    print('C')",
            "lua_chon": {"A": "A", "B": "B", "C": "C", "D": "Lỗi"},
            "dap_an": "B",
            "giai_thich": "x = 0 là False, not 0 là True nên chạy elif"
        },
        {
            "id": 12,
            "phan": "Nâng cao",
            "noi_dung": "Kết quả của: [] or [1, 2] or [3]",
            "lua_chon": {"A": "[]", "B": "[1, 2]", "C": "[3]", "D": "True"},
            "dap_an": "B",
            "giai_thich": "or trả về giá trị đầu tiên True, [] là False, [1,2] là True"
        },
        {
            "id": 13,
            "phan": "Nâng cao",
            "noi_dung": "Đoạn code nào kiểm tra x trong khoảng 10-20?",
            "lua_chon": {"A": "if 10 < x < 20:", "B": "if x > 10 and x < 20:", "C": "if (x > 10) and (x < 20):", "D": "Tất cả đều đúng"},
            "dap_an": "D",
            "giai_thich": "Cả 3 cách đều đúng, Python hỗ trợ chained comparison"
        },
        {
            "id": 14,
            "phan": "Nâng cao",
            "noi_dung": "Kết quả của: bool('False')",
            "lua_chon": {"A": "True", "B": "False", "C": "'False'", "D": "Lỗi"},
            "dap_an": "A",
            "giai_thich": "Chuỗi không rỗng luôn là True, kể cả 'False'"
        },
        {
            "id": 15,
            "phan": "Nâng cao",
            "noi_dung": "Đoạn code nào có thể gây lỗi?",
            "lua_chon": {"A": "if True: pass", "B": "if 1/0 > 0: print('OK')", "C": "if False: print('Never')", "D": "if None: print('None')"},
            "dap_an": "B",
            "giai_thich": "1/0 gây ZeroDivisionError"
        },
        {
            "id": 16,
            "phan": "Nâng cao",
            "noi_dung": "Kết quả của: 'a' < 'b' < 'c'",
            "lua_chon": {"A": "True", "B": "False", "C": "Lỗi", "D": "'abc'"},
            "dap_an": "A",
            "giai_thich": "So sánh chuỗi theo thứ tự alphabet"
        },
        {
            "id": 17,
            "phan": "Nâng cao",
            "noi_dung": "Cách nào hiệu quả nhất để kiểm tra x trong nhiều giá trị?",
            "lua_chon": {"A": "if x == 1 or x == 2 or x == 3:", "B": "if x in [1, 2, 3]:", "C": "if x in {1, 2, 3}:", "D": "B và C đều tốt"},
            "dap_an": "C",
            "giai_thich": "Set {1,2,3} nhanh hơn list [1,2,3] cho lookup"
        },
        {
            "id": 18,
            "phan": "Nâng cao",
            "noi_dung": "Kết quả của: True + True",
            "lua_chon": {"A": "2", "B": "True", "C": "False", "D": "Lỗi"},
            "dap_an": "A",
            "giai_thich": "True = 1 trong phép toán, 1 + 1 = 2"
        },
        {
            "id": 19,
            "phan": "Nâng cao",
            "noi_dung": "Đoạn code nào kiểm tra s là chuỗi rỗng?",
            "lua_chon": {"A": "if s == '':", "B": "if not s:", "C": "if len(s) == 0:", "D": "Tất cả đều đúng"},
            "dap_an": "D",
            "giai_thich": "Cả 3 cách đều kiểm tra chuỗi rỗng"
        },
        {
            "id": 20,
            "phan": "Nâng cao",
            "noi_dung": "Short-circuit evaluation nghĩa là gì?",
            "lua_chon": {"A": "Tính toán nhanh", "B": "Dừng sớm khi đã biết kết quả", "C": "Tối ưu hóa code", "D": "Kiểm tra lỗi"},
            "dap_an": "B",
            "giai_thich": "and/or dừng sớm khi đã xác định được kết quả"
        }
    ]
    
    return cau_hoi

# ===============================================
# CHỨC NĂNG QUIZ TƯƠNG TÁC
# ===============================================

def hien_thi_cau_hoi(cau_hoi, so_thu_tu, tong_so):
    """Hiển thị một câu hỏi với format đẹp"""
    
    if COLORAMA_AVAILABLE:
        print(Fore.BLUE + f"{'='*60}")
        print(Fore.YELLOW + f"📝 CÂU HỎI {so_thu_tu}/{tong_so} - PHẦN {cau_hoi['phan'].upper()}")
        print(Fore.BLUE + f"{'='*60}" + Style.RESET_ALL)
    else:
        print("="*60)
        print(f"CAU HOI {so_thu_tu}/{tong_so} - PHAN {cau_hoi['phan'].upper()}")
        print("="*60)
    
    print()
    print(f"❓ {cau_hoi['noi_dung']}")
    print()
    
    # Hiển thị các lựa chọn
    for key, value in cau_hoi['lua_chon'].items():
        if COLORAMA_AVAILABLE:
            print(Fore.WHITE + f"   {key}. {value}" + Style.RESET_ALL)
        else:
            print(f"   {key}. {value}")
    
    print()

def nhap_dap_an():
    """Nhập đáp án từ người dùng với validation"""
    
    while True:
        if COLORAMA_AVAILABLE:
            dap_an = input(Fore.GREEN + "🎯 Nhập đáp án của bạn (A/B/C/D): " + Style.RESET_ALL).strip().upper()
        else:
            dap_an = input("Nhap dap an cua ban (A/B/C/D): ").strip().upper()
        
        if dap_an in ['A', 'B', 'C', 'D']:
            return dap_an
        else:
            if COLORAMA_AVAILABLE:
                print(Fore.RED + "❌ Vui lòng nhập A, B, C hoặc D!" + Style.RESET_ALL)
            else:
                print("Vui long nhap A, B, C hoac D!")

def choi_quiz_trac_nghiem():
    """Chức năng chính chơi quiz trắc nghiệm"""
    
    quiz = QuizManager()
    quiz.hien_thi_header()
    
    # Hỏi người dùng có muốn chơi không
    if COLORAMA_AVAILABLE:
        bat_dau = input(Fore.CYAN + "🚀 Bạn có sẵn sàng bắt đầu quiz không? (y/n): " + Style.RESET_ALL).lower()
    else:
        bat_dau = input("Ban co san sang bat dau quiz khong? (y/n): ").lower()
    
    if bat_dau != 'y':
        print("👋 Hẹn gặp lại! Chúc bạn học tốt!")
        return
    
    # Lấy danh sách câu hỏi
    danh_sach_cau_hoi = tao_danh_sach_cau_hoi()
    
    # Hỏi số lượng câu muốn làm
    print("\n📊 Chọn số lượng câu hỏi:")
    print("1. Làm 10 câu (Quick test)")
    print("2. Làm 20 câu (Full test)")  
    print("3. Làm tất cả câu (Complete)")
    
    while True:
        try:
            lua_chon = int(input("🎯 Chọn mode (1/2/3): "))
            if lua_chon == 1:
                so_cau = 10
                break
            elif lua_chon == 2:
                so_cau = 20
                break
            elif lua_chon == 3:
                so_cau = len(danh_sach_cau_hoi)
                break
            else:
                print("❌ Vui lòng chọn 1, 2 hoặc 3!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    # Random hoặc theo thứ tự
    if COLORAMA_AVAILABLE:
        random_order = input(Fore.MAGENTA + "🎲 Bạn có muốn random câu hỏi không? (y/n): " + Style.RESET_ALL).lower()
    else:
        random_order = input("Ban co muon random cau hoi khong? (y/n): ").lower()
    
    if random_order == 'y':
        cau_hoi_chon = random.sample(danh_sach_cau_hoi, min(so_cau, len(danh_sach_cau_hoi)))
    else:
        cau_hoi_chon = danh_sach_cau_hoi[:so_cau]
    
    print(f"\n🎮 Bắt đầu quiz với {len(cau_hoi_chon)} câu hỏi!")
    time.sleep(2)
    
    # Bắt đầu quiz
    for i, cau_hoi in enumerate(cau_hoi_chon, 1):
        # Clear screen effect
        print("\n" * 2)
        
        # Hiển thị tiến độ
        quiz.hien_thi_tien_do()
        
        # Hiển thị câu hỏi
        hien_thi_cau_hoi(cau_hoi, i, len(cau_hoi_chon))
        
        # Nhập đáp án
        dap_an_user = nhap_dap_an()
        
        # Kiểm tra đáp án
        quiz.kiem_tra_dap_an(dap_an_user, cau_hoi['dap_an'], cau_hoi['giai_thich'])
        
        # Pause giữa các câu (trừ câu cuối)
        if i < len(cau_hoi_chon):
            if COLORAMA_AVAILABLE:
                input(Fore.CYAN + "👆 Nhấn Enter để tiếp tục..." + Style.RESET_ALL)
            else:
                input("Nhan Enter de tiep tuc...")
    
    # Hiển thị kết quả cuối
    quiz.hien_thi_ket_qua_cuoi()
    
    # Hỏi có muốn làm lại
    if COLORAMA_AVAILABLE:
        lam_lai = input(Fore.YELLOW + "\n🔄 Bạn có muốn làm quiz khác không? (y/n): " + Style.RESET_ALL).lower()
    else:
        lam_lai = input("\nBan co muon lam quiz khac khong? (y/n): ").lower()
    
    if lam_lai == 'y':
        choi_quiz_trac_nghiem()

# ===============================================
# BÀI TẬP TỰ LUẬN TƯƠNG TÁC
# ===============================================

def tao_bai_tap_tu_luan():
    """Tạo danh sách bài tập tự luận"""
    
    bai_tap = [
        {
            "id": 1,
            "tieu_de": "Phân loại học sinh",
            "mo_ta": "Viết chương trình nhập điểm 3 môn, phân loại học sinh",
            "yeu_cau": [
                "Nhập và validate điểm (0-10)",
                "Tính điểm trung bình", 
                "Phân loại: Giỏi/Khá/TB/Yếu",
                "Đưa ra lời khuyên"
            ],
            "goi_y": "Dùng nested if để kiểm tra điều kiện phức tạp"
        },
        {
            "id": 2,
            "tieu_de": "Máy tính thuế thu nhập",
            "mo_ta": "Tính thuế thu nhập cá nhân theo bậc thuế lũy tiến",
            "yeu_cau": [
                "Nhập thu nhập năm",
                "Tính theo bậc thuế VN",
                "Hiển thị thuế phải nộp",
                "Thu nhập sau thuế"
            ],
            "goi_y": "Sử dụng elif chain cho các bậc thuế"
        },
        {
            "id": 3,
            "tieu_de": "Game đoán số nâng cao", 
            "mo_ta": "Tạo game đoán số với nhiều tính năng",
            "yeu_cau": [
                "Random số từ 1-100",
                "Giới hạn số lần đoán",
                "Gợi ý thông minh",
                "Xử lý input lỗi"
            ],
            "goi_y": "Dùng while loop kết hợp if/else"
        }
    ]
    
    return bai_tap

def hien_thi_bai_tap_tu_luan():
    """Hiển thị menu bài tập tự luận"""
    
    if COLORAMA_AVAILABLE:
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + "📝 BÀI TẬP TỰ LUẬN")
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    else:
        print("=" * 60)
        print("BAI TAP TU LUAN")
        print("=" * 60)
    
    bai_tap = tao_bai_tap_tu_luan()
    
    for bai in bai_tap:
        if COLORAMA_AVAILABLE:
            print(Fore.YELLOW + f"\n🎯 Bài {bai['id']}: {bai['tieu_de']}" + Style.RESET_ALL)
        else:
            print(f"\nBai {bai['id']}: {bai['tieu_de']}")
        
        print(f"📖 Mô tả: {bai['mo_ta']}")
        print("📋 Yêu cầu:")
        for yc in bai['yeu_cau']:
            print(f"   • {yc}")
        
        if COLORAMA_AVAILABLE:
            print(Fore.GREEN + f"💡 Gợi ý: {bai['goi_y']}" + Style.RESET_ALL)
        else:
            print(f"Goi y: {bai['goi_y']}")
    
    print(f"\n{Fore.MAGENTA if COLORAMA_AVAILABLE else ''}📚 Hãy chọn 1-2 bài để thực hành!{Style.RESET_ALL if COLORAMA_AVAILABLE else ''}")
    print("🎯 Tập trung vào logic if/else và xử lý input")

# ===============================================
# MENU CHÍNH
# ===============================================

def hien_thi_menu_chinh():
    """Hiển thị menu chính của ứng dụng"""
    
    if COLORAMA_AVAILABLE:
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + "🎮 HỆ THỐNG QUIZ IF/ELSE TƯƠNG TÁC 🎮")
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    else:
        print("=" * 60)
        print("HE THONG QUIZ IF/ELSE TUONG TAC")
        print("=" * 60)
    
    print("\n📚 Chọn chế độ học tập:")
    print("1. 🎯 Quiz trắc nghiệm tương tác")
    print("2. 📝 Xem bài tập tự luận")
    print("3. 📖 Hướng dẫn sử dụng")
    print("4. 🚪 Thoát")
    print()

def hien_thi_huong_dan():
    """Hiển thị hướng dẫn sử dụng"""
    
    if COLORAMA_AVAILABLE:
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + "📖 HƯỚNG DẪN SỬ DỤNG")
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    else:
        print("=" * 60)
        print("HUONG DAN SU DUNG")
        print("=" * 60)
    
    print("""
🎯 QUIZ TRẮC NGHIỆM:
   • 20 câu hỏi từ cơ bản đến nâng cao
   • Tương tác từng câu với feedback ngay lập tức
   • Chọn số lượng câu và thứ tự random
   • Xem kết quả chi tiết và xếp loại
   
📝 BÀI TẬP TỰ LUẬN:
   • 3 bài tập thực hành coding
   • Yêu cầu chi tiết và gợi ý
   • Tập trung vào if/else logic
   
🌈 TÍNH NĂNG:
   • Colorama cho trải nghiệm đẹp mắt
   • Validation input đầy đủ
   • Tracking điểm số real-time
   • Tips và nhận xét cá nhân hóa
   
💡 LỜI KHUYÊN:
   • Đọc kỹ đề bài trước khi trả lời
   • Suy nghĩ từng bước logic
   • Không ngại làm lại để cải thiện
   • Practice coding thường xuyên
    """)
    
    if COLORAMA_AVAILABLE:
        input(Fore.CYAN + "\n👆 Nhấn Enter để quay lại menu..." + Style.RESET_ALL)
    else:
        input("\nNhan Enter de quay lai menu...")

def main():
    """Hàm chính điều khiển ứng dụng"""
    
    # Kiểm tra colorama
    if not COLORAMA_AVAILABLE:
        print("⚠️  Colorama chưa được cài đặt. Chạy: pip install colorama")
        print("Ứng dụng sẽ chạy ở chế độ text thường.\n")
    
    while True:
        # Clear screen effect
        print("\n" * 2)
        
        hien_thi_menu_chinh()
        
        try:
            lua_chon = int(input("🎯 Chọn chức năng (1-4): "))
            
            if lua_chon == 1:
                choi_quiz_trac_nghiem()
            elif lua_chon == 2:
                hien_thi_bai_tap_tu_luan()
                input("\nNhấn Enter để quay lại...")
            elif lua_chon == 3:
                hien_thi_huong_dan()
            elif lua_chon == 4:
                if COLORAMA_AVAILABLE:
                    print(Fore.GREEN + "👋 Cảm ơn bạn đã sử dụng! Chúc bạn học tốt!" + Style.RESET_ALL)
                else:
                    print("Cam on ban da su dung! Chuc ban hoc tot!")
                break
            else:
                if COLORAMA_AVAILABLE:
                    print(Fore.RED + "❌ Vui lòng chọn từ 1 đến 4!" + Style.RESET_ALL)
                else:
                    print("Vui long chon tu 1 den 4!")
                time.sleep(1)
                
        except ValueError:
            if COLORAMA_AVAILABLE:
                print(Fore.RED + "❌ Vui lòng nhập số!" + Style.RESET_ALL)
            else:
                print("Vui long nhap so!")
            time.sleep(1)
        except KeyboardInterrupt:
            if COLORAMA_AVAILABLE:
                print(Fore.YELLOW + "\n\n👋 Tạm biệt! Hẹn gặp lại!" + Style.RESET_ALL)
            else:
                print("\n\nTam biet! Hen gap lai!")
            break

# ===============================================
# CHẠY CHƯƠNG TRÌNH
# ===============================================

if __name__ == "__main__":
    main() 