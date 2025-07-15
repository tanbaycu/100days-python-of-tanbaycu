"""
BÀI TẬP 4: ỨNG DỤNG THỰC TẾ VỚI VÒNG LẶP
=========================================

6 ứng dụng thực tế hoàn chỉnh sử dụng for/while loops:
1. Hệ thống ATM
2. Game Quiz 
3. Quản lý học sinh
4. Weather tracker
5. Shopping cart
6. Password generator

Mỗi ứng dụng có đầy đủ features và error handling.
Thời gian ước tính: 150-200 phút
"""

import random
import string
from datetime import datetime

print("🎯 BÀI TẬP 4: ỨNG DỤNG THỰC TẾ VỚI VÒNG LẶP")
print("=" * 50)

# =============================================================================
# ỨNG DỤNG 1: HỆ THỐNG ATM NÂNG CAO
# =============================================================================

def atm_system():
    """Hệ thống ATM với nhiều tính năng"""
    print("\n🏦 ỨNG DỤNG 1: HỆ THỐNG ATM NÂNG CAO")
    print("=" * 40)
    
    # Dữ liệu tài khoản
    accounts = {
        "1234": {"name": "Nguyễn Văn An", "balance": 1000000, "pin": "1234"},
        "5678": {"name": "Trần Thị Bình", "balance": 2500000, "pin": "5678"},
        "9999": {"name": "Lê Hoàng Chi", "balance": 500000, "pin": "9999"}
    }
    
    transaction_history = []
    current_account = None
    
    def login():
        """Xác thực đăng nhập"""
        nonlocal current_account
        
        print("\n🔐 ĐĂNG NHẬP ATM")
        for attempt in range(3):
            card_number = input("Số thẻ: ")
            pin = input("PIN: ")
            
            if card_number in accounts and accounts[card_number]["pin"] == pin:
                current_account = card_number
                print(f"✅ Chào mừng {accounts[card_number]['name']}!")
                return True
            else:
                remaining = 2 - attempt
                if remaining > 0:
                    print(f"❌ Thông tin không đúng! Còn {remaining} lần thử.")
                else:
                    print("🚫 Thẻ bị khóa! Liên hệ ngân hàng.")
                    return False
        return False
    
    def check_balance():
        """Kiểm tra số dư"""
        balance = accounts[current_account]["balance"]
        print(f"💰 Số dư hiện tại: {balance:,}đ")
        return balance
    
    def withdraw_money():
        """Rút tiền"""
        balance = accounts[current_account]["balance"]
        print(f"💰 Số dư hiện tại: {balance:,}đ")
        
        while True:
            try:
                amount = int(input("Số tiền cần rút: "))
                
                if amount <= 0:
                    print("❌ Số tiền phải lớn hơn 0!")
                    continue
                elif amount > balance:
                    print("❌ Số dư không đủ!")
                    continue
                elif amount % 50000 != 0:
                    print("❌ Chỉ có thể rút bội số của 50,000đ!")
                    continue
                else:
                    accounts[current_account]["balance"] -= amount
                    transaction_history.append({
                        "type": "Rút tiền",
                        "amount": amount,
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "account": current_account
                    })
                    print(f"✅ Rút {amount:,}đ thành công!")
                    print(f"Số dư còn lại: {accounts[current_account]['balance']:,}đ")
                    break
            except ValueError:
                print("❌ Vui lòng nhập số hợp lệ!")
    
    def deposit_money():
        """Nạp tiền"""
        while True:
            try:
                amount = int(input("Số tiền nạp: "))
                
                if amount <= 0:
                    print("❌ Số tiền phải lớn hơn 0!")
                    continue
                else:
                    accounts[current_account]["balance"] += amount
                    transaction_history.append({
                        "type": "Nạp tiền",
                        "amount": amount,
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "account": current_account
                    })
                    print(f"✅ Nạp {amount:,}đ thành công!")
                    print(f"Số dư mới: {accounts[current_account]['balance']:,}đ")
                    break
            except ValueError:
                print("❌ Vui lòng nhập số hợp lệ!")
    
    def transfer_money():
        """Chuyển tiền"""
        print("\n💸 CHUYỂN TIỀN")
        
        # Hiển thị danh sách tài khoản
        print("Danh sách tài khoản:")
        for acc_num, info in accounts.items():
            if acc_num != current_account:
                print(f"- {acc_num}: {info['name']}")
        
        target_account = input("Số tài khoản đích: ")
        
        if target_account == current_account:
            print("❌ Không thể chuyển cho chính mình!")
            return
        elif target_account not in accounts:
            print("❌ Tài khoản không tồn tại!")
            return
        
        while True:
            try:
                amount = int(input("Số tiền chuyển: "))
                
                if amount <= 0:
                    print("❌ Số tiền phải lớn hơn 0!")
                    continue
                elif amount > accounts[current_account]["balance"]:
                    print("❌ Số dư không đủ!")
                    continue
                else:
                    # Thực hiện chuyển tiền
                    accounts[current_account]["balance"] -= amount
                    accounts[target_account]["balance"] += amount
                    
                    transaction_history.append({
                        "type": f"Chuyển tiền đến {target_account}",
                        "amount": amount,
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "account": current_account
                    })
                    
                    print(f"✅ Chuyển {amount:,}đ đến {accounts[target_account]['name']} thành công!")
                    print(f"Số dư còn lại: {accounts[current_account]['balance']:,}đ")
                    break
            except ValueError:
                print("❌ Vui lòng nhập số hợp lệ!")
    
    def view_history():
        """Xem lịch sử giao dịch"""
        print("\n📜 LỊCH SỬ GIAO DỊCH")
        user_transactions = [t for t in transaction_history if t["account"] == current_account]
        
        if not user_transactions:
            print("Chưa có giao dịch nào!")
            return
        
        for i, trans in enumerate(user_transactions, 1):
            print(f"{i}. {trans['time']} - {trans['type']}: {trans['amount']:,}đ")
    
    # Main ATM menu
    if not login():
        return
    
    while True:
        print(f"\n💳 ATM MENU - {accounts[current_account]['name']}")
        print("1. Kiểm tra số dư")
        print("2. Rút tiền")
        print("3. Nạp tiền")
        print("4. Chuyển tiền")
        print("5. Lịch sử giao dịch")
        print("6. Thoát")
        
        choice = input("Chọn (1-6): ")
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            transfer_money()
        elif choice == '5':
            view_history()
        elif choice == '6':
            print("👋 Cảm ơn bạn đã sử dụng ATM!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# ỨNG DỤNG 2: GAME QUIZ TƯƠNG TÁC
# =============================================================================

def quiz_game():
    """Game quiz với nhiều chủ đề và scoring"""
    print("\n🧠 ỨNG DỤNG 2: GAME QUIZ TƯƠNG TÁC")
    print("=" * 40)
    
    # Database câu hỏi
    questions_db = {
        "python": [
            {"q": "Python được tạo bởi ai?", "a": ["Guido van Rossum", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"], "correct": 0},
            {"q": "Cú pháp nào đúng để in Hello World?", "a": ["print('Hello World')", "echo('Hello World')", "console.log('Hello World')", "printf('Hello World')"], "correct": 0},
            {"q": "Python là ngôn ngữ gì?", "a": ["Compiled", "Interpreted", "Assembly", "Machine"], "correct": 1},
            {"q": "Phần mở rộng file Python là gì?", "a": [".txt", ".py", ".python", ".code"], "correct": 1},
            {"q": "Từ khóa nào dùng để tạo function?", "a": ["function", "def", "func", "define"], "correct": 1}
        ],
        "math": [
            {"q": "2 + 2 = ?", "a": ["3", "4", "5", "6"], "correct": 1},
            {"q": "Căn bậc 2 của 16 là?", "a": ["2", "4", "6", "8"], "correct": 1},
            {"q": "π (pi) xấp xỉ bằng?", "a": ["3.14", "2.71", "1.41", "1.73"], "correct": 0},
            {"q": "10! (10 giai thừa) = ?", "a": ["100", "1000", "3628800", "10000"], "correct": 2},
            {"q": "Sin(90°) = ?", "a": ["0", "1", "0.5", "-1"], "correct": 1}
        ],
        "general": [
            {"q": "Thủ đô của Việt Nam?", "a": ["Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Cần Thơ"], "correct": 1},
            {"q": "Hành tinh nào gần Mặt Trời nhất?", "a": ["Sao Kim", "Trái Đất", "Sao Thủy", "Sao Hỏa"], "correct": 2},
            {"q": "Ai viết Romeo và Juliet?", "a": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "correct": 1},
            {"q": "1 km = ? m", "a": ["100", "1000", "10000", "10"], "correct": 1},
            {"q": "Nguyên tố hóa học của nước?", "a": ["H2O", "CO2", "O2", "H2"], "correct": 0}
        ]
    }
    
    player_stats = {
        "name": "",
        "total_questions": 0,
        "correct_answers": 0,
        "topics_played": set(),
        "high_score": 0
    }
    
    def get_player_info():
        """Lấy thông tin người chơi"""
        while True:
            name = input("Tên của bạn: ").strip()
            if name:
                player_stats["name"] = name
                print(f"Chào mừng {name} đến với Quiz Game! 🎮")
                break
            else:
                print("❌ Vui lòng nhập tên!")
    
    def choose_topic():
        """Chọn chủ đề"""
        print("\n📚 CHỌN CHỦ ĐỀ:")
        topics = list(questions_db.keys())
        
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic.title()}")
        print(f"{len(topics) + 1}. Random Mix")
        
        while True:
            try:
                choice = int(input("Chọn chủ đề: ")) - 1
                
                if 0 <= choice < len(topics):
                    return topics[choice]
                elif choice == len(topics):
                    return "random"
                else:
                    print("❌ Lựa chọn không hợp lệ!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
    
    def play_quiz(topic):
        """Chơi quiz"""
        if topic == "random":
            # Mix questions from all topics
            all_questions = []
            for topic_questions in questions_db.values():
                all_questions.extend(topic_questions)
            questions = random.sample(all_questions, min(10, len(all_questions)))
            topic_name = "Random Mix"
        else:
            questions = questions_db[topic].copy()
            random.shuffle(questions)
            topic_name = topic.title()
        
        score = 0
        question_count = len(questions)
        
        print(f"\n🎯 QUIZ: {topic_name}")
        print(f"Có {question_count} câu hỏi. Mỗi câu đúng = 10 điểm")
        print("-" * 40)
        
        for i, q_data in enumerate(questions, 1):
            print(f"\nCâu {i}/{question_count}: {q_data['q']}")
            
            # Hiển thị đáp án
            for j, answer in enumerate(q_data['a']):
                print(f"{j + 1}. {answer}")
            
            # Nhận đáp án từ user
            while True:
                try:
                    user_answer = int(input("Đáp án của bạn (1-4): ")) - 1
                    
                    if 0 <= user_answer <= 3:
                        break
                    else:
                        print("❌ Vui lòng chọn 1-4!")
                except ValueError:
                    print("❌ Vui lòng nhập số!")
            
            # Kiểm tra đáp án
            if user_answer == q_data['correct']:
                print("✅ Chính xác! +10 điểm")
                score += 10
                player_stats["correct_answers"] += 1
            else:
                correct_answer = q_data['a'][q_data['correct']]
                print(f"❌ Sai! Đáp án đúng: {correct_answer}")
            
            player_stats["total_questions"] += 1
            print(f"Điểm hiện tại: {score}")
        
        # Kết quả cuối game
        percentage = (score / (question_count * 10)) * 100
        print(f"\n🏆 KẾT QUẢ QUIZ {topic_name}")
        print(f"Điểm số: {score}/{question_count * 10}")
        print(f"Tỷ lệ đúng: {percentage:.1f}%")
        
        # Đánh giá
        if percentage >= 90:
            print("🌟 Xuất sắc! Bạn là thiên tài!")
        elif percentage >= 70:
            print("👏 Giỏi lắm! Kiến thức tốt!")
        elif percentage >= 50:
            print("👍 Không tệ! Cần cố gắng thêm!")
        else:
            print("💪 Cần học thêm nhé!")
        
        # Cập nhật high score
        if score > player_stats["high_score"]:
            player_stats["high_score"] = score
            print("🎉 HIGH SCORE MỚI!")
        
        player_stats["topics_played"].add(topic_name)
        return score
    
    def view_stats():
        """Xem thống kê"""
        print(f"\n📊 THỐNG KÊ GAME - {player_stats['name']}")
        print("-" * 30)
        print(f"Tổng câu hỏi: {player_stats['total_questions']}")
        print(f"Câu trả lời đúng: {player_stats['correct_answers']}")
        
        if player_stats['total_questions'] > 0:
            accuracy = (player_stats['correct_answers'] / player_stats['total_questions']) * 100
            print(f"Độ chính xác: {accuracy:.1f}%")
        
        print(f"High Score: {player_stats['high_score']}")
        print(f"Chủ đề đã chơi: {', '.join(player_stats['topics_played'])}")
    
    # Main quiz menu
    get_player_info()
    
    while True:
        print(f"\n🎮 QUIZ GAME MENU - {player_stats['name']}")
        print("1. Chơi Quiz")
        print("2. Xem thống kê")
        print("3. Luật chơi")
        print("4. Thoát")
        
        choice = input("Chọn (1-4): ")
        
        if choice == '1':
            topic = choose_topic()
            play_quiz(topic)
        elif choice == '2':
            view_stats()
        elif choice == '3':
            print("\n📋 LUẬT CHƠI:")
            print("- Chọn chủ đề yêu thích")
            print("- Trả lời câu hỏi bằng cách chọn 1-4")
            print("- Mỗi câu đúng = 10 điểm")
            print("- Cố gắng đạt high score!")
        elif choice == '4':
            print(f"👋 Tạm biệt {player_stats['name']}! Cảm ơn bạn đã chơi!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# ỨNG DỤNG 3: QUẢN LÝ HỌC SINH
# =============================================================================

def student_management():
    """Hệ thống quản lý học sinh"""
    print("\n🎓 ỨNG DỤNG 3: QUẢN LÝ HỌC SINH")
    print("=" * 40)
    
    students = []  # Database học sinh
    
    def add_student():
        """Thêm học sinh mới"""
        print("\n➕ THÊM HỌC SINH MỚI")
        
        # Nhập thông tin
        while True:
            name = input("Họ tên: ").strip()
            if name:
                break
            print("❌ Tên không được rỗng!")
        
        while True:
            try:
                age = int(input("Tuổi: "))
                if 6 <= age <= 25:
                    break
                print("❌ Tuổi phải từ 6-25!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Nhập điểm các môn
        subjects = ["Toán", "Lý", "Hóa", "Văn", "Anh"]
        scores = {}
        
        print("Nhập điểm các môn (0-10):")
        for subject in subjects:
            while True:
                try:
                    score = float(input(f"{subject}: "))
                    if 0 <= score <= 10:
                        scores[subject] = score
                        break
                    print("❌ Điểm phải từ 0-10!")
                except ValueError:
                    print("❌ Vui lòng nhập số!")
        
        # Tính điểm trung bình
        average = sum(scores.values()) / len(scores)
        
        # Xếp loại
        if average >= 9:
            rank = "Xuất sắc"
        elif average >= 8:
            rank = "Giỏi"
        elif average >= 6.5:
            rank = "Khá"
        elif average >= 5:
            rank = "Trung bình"
        else:
            rank = "Yếu"
        
        # Tạo student ID
        student_id = f"SV{len(students) + 1:03d}"
        
        # Thêm vào database
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "scores": scores,
            "average": average,
            "rank": rank
        }
        
        students.append(student)
        print(f"✅ Đã thêm học sinh {name} với ID: {student_id}")
        print(f"Điểm TB: {average:.2f} - Xếp loại: {rank}")
    
    def view_students():
        """Xem danh sách học sinh"""
        if not students:
            print("📝 Danh sách trống!")
            return
        
        print(f"\n📋 DANH SÁCH HỌC SINH ({len(students)} người)")
        print("-" * 70)
        print(f"{'ID':<6} {'Họ tên':<20} {'Tuổi':<5} {'ĐTB':<6} {'Xếp loại':<15}")
        print("-" * 70)
        
        for student in students:
            print(f"{student['id']:<6} {student['name']:<20} {student['age']:<5} "
                  f"{student['average']:<6.2f} {student['rank']:<15}")
    
    def search_student():
        """Tìm kiếm học sinh"""
        if not students:
            print("📝 Danh sách trống!")
            return
        
        print("\n🔍 TÌM KIẾM HỌC SINH")
        print("1. Tìm theo ID")
        print("2. Tìm theo tên")
        print("3. Tìm theo xếp loại")
        
        choice = input("Chọn (1-3): ")
        found_students = []
        
        if choice == '1':
            search_id = input("Nhập ID: ").upper()
            found_students = [s for s in students if s['id'] == search_id]
        elif choice == '2':
            search_name = input("Nhập tên (có thể là một phần): ").lower()
            found_students = [s for s in students if search_name in s['name'].lower()]
        elif choice == '3':
            print("Xếp loại: Xuất sắc, Giỏi, Khá, Trung bình, Yếu")
            search_rank = input("Nhập xếp loại: ")
            found_students = [s for s in students if s['rank'].lower() == search_rank.lower()]
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return
        
        if found_students:
            print(f"\n🎯 TÌM THẤY {len(found_students)} KẾT QUẢ:")
            for student in found_students:
                print(f"\nID: {student['id']} - {student['name']} ({student['age']} tuổi)")
                print(f"Điểm các môn: {student['scores']}")
                print(f"ĐTB: {student['average']:.2f} - Xếp loại: {student['rank']}")
        else:
            print("❌ Không tìm thấy kết quả!")
    
    def statistics():
        """Thống kê"""
        if not students:
            print("📝 Không có dữ liệu để thống kê!")
            return
        
        print("\n📊 THỐNG KÊ HỌC SINH")
        print("-" * 30)
        
        # Thống kê theo xếp loại
        ranks = {}
        total_average = 0
        ages = []
        
        for student in students:
            rank = student['rank']
            ranks[rank] = ranks.get(rank, 0) + 1
            total_average += student['average']
            ages.append(student['age'])
        
        print("Thống kê theo xếp loại:")
        for rank, count in ranks.items():
            percentage = (count / len(students)) * 100
            print(f"- {rank}: {count} người ({percentage:.1f}%)")
        
        print(f"\nĐiểm trung bình chung: {total_average / len(students):.2f}")
        print(f"Tuổi trung bình: {sum(ages) / len(ages):.1f}")
        print(f"Tuổi nhỏ nhất: {min(ages)}")
        print(f"Tuổi lớn nhất: {max(ages)}")
        
        # Top học sinh
        top_students = sorted(students, key=lambda x: x['average'], reverse=True)[:3]
        print(f"\n🏆 TOP 3 HỌC SINH:")
        for i, student in enumerate(top_students, 1):
            print(f"{i}. {student['name']} - ĐTB: {student['average']:.2f}")
    
    def update_student():
        """Cập nhật thông tin học sinh"""
        if not students:
            print("📝 Danh sách trống!")
            return
        
        print("\n✏️ CẬP NHẬT HỌC SINH")
        view_students()
        
        student_id = input("\nNhập ID học sinh cần cập nhật: ").upper()
        student = None
        
        for s in students:
            if s['id'] == student_id:
                student = s
                break
        
        if not student:
            print("❌ Không tìm thấy học sinh!")
            return
        
        print(f"\nThông tin hiện tại: {student['name']}")
        print("Chọn thông tin cần cập nhật:")
        print("1. Tên")
        print("2. Tuổi") 
        print("3. Điểm môn học")
        
        choice = input("Chọn (1-3): ")
        
        if choice == '1':
            new_name = input("Tên mới: ").strip()
            if new_name:
                student['name'] = new_name
                print("✅ Đã cập nhật tên!")
        elif choice == '2':
            try:
                new_age = int(input("Tuổi mới: "))
                if 6 <= new_age <= 25:
                    student['age'] = new_age
                    print("✅ Đã cập nhật tuổi!")
                else:
                    print("❌ Tuổi phải từ 6-25!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        elif choice == '3':
            print("Điểm hiện tại:", student['scores'])
            subject = input("Môn cần cập nhật: ")
            if subject in student['scores']:
                try:
                    new_score = float(input(f"Điểm {subject} mới: "))
                    if 0 <= new_score <= 10:
                        student['scores'][subject] = new_score
                        
                        # Tính lại điểm TB và xếp loại
                        student['average'] = sum(student['scores'].values()) / len(student['scores'])
                        
                        if student['average'] >= 9:
                            student['rank'] = "Xuất sắc"
                        elif student['average'] >= 8:
                            student['rank'] = "Giỏi"
                        elif student['average'] >= 6.5:
                            student['rank'] = "Khá"
                        elif student['average'] >= 5:
                            student['rank'] = "Trung bình"
                        else:
                            student['rank'] = "Yếu"
                        
                        print("✅ Đã cập nhật điểm và xếp loại!")
                    else:
                        print("❌ Điểm phải từ 0-10!")
                except ValueError:
                    print("❌ Vui lòng nhập số!")
            else:
                print("❌ Môn học không tồn tại!")
    
    def delete_student():
        """Xóa học sinh"""
        if not students:
            print("📝 Danh sách trống!")
            return
        
        print("\n🗑️ XÓA HỌC SINH")
        view_students()
        
        student_id = input("\nNhập ID học sinh cần xóa: ").upper()
        
        for i, student in enumerate(students):
            if student['id'] == student_id:
                confirm = input(f"Xác nhận xóa {student['name']}? (yes/no): ").lower()
                if confirm in ['yes', 'y', 'có']:
                    removed = students.pop(i)
                    print(f"✅ Đã xóa học sinh {removed['name']}")
                else:
                    print("❌ Đã hủy xóa!")
                return
        
        print("❌ Không tìm thấy học sinh!")
    
    # Main menu
    while True:
        print(f"\n🎓 QUẢN LÝ HỌC SINH - Tổng: {len(students)} người")
        print("1. Thêm học sinh")
        print("2. Xem danh sách")
        print("3. Tìm kiếm")
        print("4. Thống kê")
        print("5. Cập nhật")
        print("6. Xóa")
        print("7. Thoát")
        
        choice = input("Chọn (1-7): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            statistics()
        elif choice == '5':
            update_student()
        elif choice == '6':
            delete_student()
        elif choice == '7':
            print("👋 Tạm biệt! Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# ỨNG DỤNG 4: WEATHER TRACKER
# =============================================================================

def weather_tracker():
    """Ứng dụng theo dõi thời tiết"""
    print("\n🌤️ ỨNG DỤNG 4: WEATHER TRACKER")
    print("=" * 40)
    
    weather_data = []
    
    def add_weather_data():
        """Thêm dữ liệu thời tiết"""
        print("\n📊 THÊM DỮ LIỆU THỜI TIẾT")
        
        # Nhập ngày
        while True:
            date = input("Ngày (dd/mm/yyyy): ")
            if len(date) == 10 and date[2] == '/' and date[5] == '/':
                break
            print("❌ Format ngày: dd/mm/yyyy")
        
        # Nhiệt độ
        while True:
            try:
                temp = float(input("Nhiệt độ (°C): "))
                if -50 <= temp <= 60:
                    break
                print("❌ Nhiệt độ phải từ -50°C đến 60°C")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Độ ẩm
        while True:
            try:
                humidity = int(input("Độ ẩm (%): "))
                if 0 <= humidity <= 100:
                    break
                print("❌ Độ ẩm phải từ 0-100%")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Thời tiết
        weather_conditions = ["Nắng", "Mây", "Mưa", "Bão", "Sương mù"]
        print("Tình trạng thời tiết:")
        for i, condition in enumerate(weather_conditions, 1):
            print(f"{i}. {condition}")
        
        while True:
            try:
                choice = int(input("Chọn (1-5): ")) - 1
                if 0 <= choice < len(weather_conditions):
                    condition = weather_conditions[choice]
                    break
                print("❌ Chọn từ 1-5!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Ghi chú
        notes = input("Ghi chú (tùy chọn): ")
        
        # Thêm vào database
        weather_entry = {
            "date": date,
            "temperature": temp,
            "humidity": humidity,
            "condition": condition,
            "notes": notes
        }
        
        weather_data.append(weather_entry)
        print(f"✅ Đã thêm dữ liệu thời tiết ngày {date}")
    
    def view_weather_data():
        """Xem dữ liệu thời tiết"""
        if not weather_data:
            print("📝 Chưa có dữ liệu thời tiết!")
            return
        
        print(f"\n🌡️ DỮ LIỆU THỜI TIẾT ({len(weather_data)} ngày)")
        print("-" * 80)
        print(f"{'Ngày':<12} {'Nhiệt độ':<10} {'Độ ẩm':<8} {'Thời tiết':<12} {'Ghi chú':<20}")
        print("-" * 80)
        
        for entry in weather_data:
            notes_short = entry['notes'][:17] + "..." if len(entry['notes']) > 20 else entry['notes']
            print(f"{entry['date']:<12} {entry['temperature']:>6.1f}°C  {entry['humidity']:>5}%   "
                  f"{entry['condition']:<12} {notes_short:<20}")
    
    def weather_statistics():
        """Thống kê thời tiết"""
        if not weather_data:
            print("📝 Không có dữ liệu để thống kê!")
            return
        
        print("\n📈 THỐNG KÊ THỜI TIẾT")
        print("-" * 30)
        
        # Thống kê nhiệt độ
        temperatures = [entry['temperature'] for entry in weather_data]
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        
        print(f"Nhiệt độ trung bình: {avg_temp:.1f}°C")
        print(f"Nhiệt độ cao nhất: {max_temp:.1f}°C")
        print(f"Nhiệt độ thấp nhất: {min_temp:.1f}°C")
        
        # Thống kê độ ẩm
        humidities = [entry['humidity'] for entry in weather_data]
        avg_humidity = sum(humidities) / len(humidities)
        
        print(f"Độ ẩm trung bình: {avg_humidity:.1f}%")
        
        # Thống kê thời tiết
        conditions = {}
        for entry in weather_data:
            condition = entry['condition']
            conditions[condition] = conditions.get(condition, 0) + 1
        
        print("\nThống kê thời tiết:")
        for condition, count in conditions.items():
            percentage = (count / len(weather_data)) * 100
            print(f"- {condition}: {count} ngày ({percentage:.1f}%)")
        
        # Ngày đặc biệt
        hot_days = [e for e in weather_data if e['temperature'] > 35]
        cold_days = [e for e in weather_data if e['temperature'] < 15]
        rainy_days = [e for e in weather_data if e['condition'] == 'Mưa']
        
        print(f"\nNgày nóng (>35°C): {len(hot_days)}")
        print(f"Ngày lạnh (<15°C): {len(cold_days)}")
        print(f"Ngày mưa: {len(rainy_days)}")
    
    def search_weather():
        """Tìm kiếm dữ liệu thời tiết"""
        if not weather_data:
            print("📝 Chưa có dữ liệu!")
            return
        
        print("\n🔍 TÌM KIẾM THỜI TIẾT")
        print("1. Tìm theo ngày")
        print("2. Tìm theo nhiệt độ")
        print("3. Tìm theo thời tiết")
        
        choice = input("Chọn (1-3): ")
        found_entries = []
        
        if choice == '1':
            search_date = input("Nhập ngày (dd/mm/yyyy): ")
            found_entries = [e for e in weather_data if e['date'] == search_date]
        elif choice == '2':
            try:
                min_temp = float(input("Nhiệt độ từ: "))
                max_temp = float(input("Nhiệt độ đến: "))
                found_entries = [e for e in weather_data 
                               if min_temp <= e['temperature'] <= max_temp]
            except ValueError:
                print("❌ Vui lòng nhập số!")
                return
        elif choice == '3':
            search_condition = input("Thời tiết (Nắng/Mây/Mưa/Bão/Sương mù): ")
            found_entries = [e for e in weather_data 
                           if e['condition'].lower() == search_condition.lower()]
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return
        
        if found_entries:
            print(f"\n🎯 TÌM THẤY {len(found_entries)} KẾT QUẢ:")
            for entry in found_entries:
                print(f"\n📅 {entry['date']}")
                print(f"🌡️ Nhiệt độ: {entry['temperature']:.1f}°C")
                print(f"💧 Độ ẩm: {entry['humidity']}%")
                print(f"🌤️ Thời tiết: {entry['condition']}")
                if entry['notes']:
                    print(f"📝 Ghi chú: {entry['notes']}")
        else:
            print("❌ Không tìm thấy kết quả!")
    
    def weather_trends():
        """Phân tích xu hướng thời tiết"""
        if len(weather_data) < 2:
            print("📝 Cần ít nhất 2 ngày dữ liệu để phân tích xu hướng!")
            return
        
        print("\n📊 XU HƯỚNG THỜI TIẾT")
        print("-" * 30)
        
        # Xu hướng nhiệt độ
        recent_temps = [e['temperature'] for e in weather_data[-7:]]  # 7 ngày gần nhất
        if len(recent_temps) >= 2:
            temp_trend = recent_temps[-1] - recent_temps[0]
            if temp_trend > 1:
                print("🔥 Xu hướng: Nhiệt độ đang tăng")
            elif temp_trend < -1:
                print("❄️ Xu hướng: Nhiệt độ đang giảm")
            else:
                print("➡️ Xu hướng: Nhiệt độ ổn định")
        
        # Dự đoán đơn giản
        avg_recent_temp = sum(recent_temps) / len(recent_temps)
        print(f"Nhiệt độ dự kiến ngày mai: {avg_recent_temp:.1f}°C")
        
        # Thời tiết phổ biến gần đây
        recent_conditions = [e['condition'] for e in weather_data[-5:]]
        most_common = max(set(recent_conditions), key=recent_conditions.count)
        print(f"Thời tiết phổ biến gần đây: {most_common}")
    
    # Main menu
    while True:
        print(f"\n🌤️ WEATHER TRACKER - {len(weather_data)} ngày dữ liệu")
        print("1. Thêm dữ liệu")
        print("2. Xem dữ liệu")
        print("3. Thống kê")
        print("4. Tìm kiếm")
        print("5. Xu hướng")
        print("6. Thoát")
        
        choice = input("Chọn (1-6): ")
        
        if choice == '1':
            add_weather_data()
        elif choice == '2':
            view_weather_data()
        elif choice == '3':
            weather_statistics()
        elif choice == '4':
            search_weather()
        elif choice == '5':
            weather_trends()
        elif choice == '6':
            print("👋 Tạm biệt! Cảm ơn bạn đã sử dụng Weather Tracker!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# ỨNG DỤNG 5: SHOPPING CART SYSTEM
# =============================================================================

def shopping_cart():
    """Hệ thống giỏ hàng mua sắm"""
    print("\n🛒 ỨNG DỤNG 5: SHOPPING CART SYSTEM")
    print("=" * 40)
    
    # Database sản phẩm
    products = {
        "SP001": {"name": "iPhone 15", "price": 25000000, "stock": 10, "category": "Điện thoại"},
        "SP002": {"name": "Samsung Galaxy S24", "price": 22000000, "stock": 8, "category": "Điện thoại"},
        "SP003": {"name": "MacBook Pro", "price": 45000000, "stock": 5, "category": "Laptop"},
        "SP004": {"name": "Dell XPS 13", "price": 30000000, "stock": 7, "category": "Laptop"},
        "SP005": {"name": "iPad Air", "price": 18000000, "stock": 12, "category": "Tablet"},
        "SP006": {"name": "AirPods Pro", "price": 6000000, "stock": 20, "category": "Phụ kiện"},
        "SP007": {"name": "Apple Watch", "price": 12000000, "stock": 15, "category": "Phụ kiện"},
        "SP008": {"name": "Gaming Mouse", "price": 2000000, "stock": 25, "category": "Phụ kiện"},
    }
    
    cart = []  # Giỏ hàng
    customer_info = {}
    
    def display_products():
        """Hiển thị danh sách sản phẩm"""
        print("\n🏪 DANH SÁCH SẢN PHẨM")
        print("-" * 80)
        print(f"{'Mã SP':<8} {'Tên sản phẩm':<20} {'Giá':<15} {'Kho':<6} {'Danh mục':<12}")
        print("-" * 80)
        
        for code, info in products.items():
            price_str = f"{info['price']:,}đ"
            stock_status = f"{info['stock']}" if info['stock'] > 0 else "Hết hàng"
            print(f"{code:<8} {info['name']:<20} {price_str:<15} {stock_status:<6} {info['category']:<12}")
    
    def add_to_cart():
        """Thêm sản phẩm vào giỏ hàng"""
        display_products()
        
        while True:
            product_code = input("\nNhập mã sản phẩm (hoặc 'back' để quay lại): ").upper()
            
            if product_code == 'BACK':
                return
            
            if product_code not in products:
                print("❌ Mã sản phẩm không tồn tại!")
                continue
            
            product = products[product_code]
            
            if product['stock'] == 0:
                print("❌ Sản phẩm đã hết hàng!")
                continue
            
            while True:
                try:
                    quantity = int(input(f"Số lượng (có sẵn: {product['stock']}): "))
                    
                    if quantity <= 0:
                        print("❌ Số lượng phải lớn hơn 0!")
                        continue
                    elif quantity > product['stock']:
                        print(f"❌ Chỉ còn {product['stock']} sản phẩm!")
                        continue
                    else:
                        # Kiểm tra sản phẩm đã có trong giỏ chưa
                        existing_item = None
                        for item in cart:
                            if item['code'] == product_code:
                                existing_item = item
                                break
                        
                        if existing_item:
                            new_quantity = existing_item['quantity'] + quantity
                            if new_quantity <= product['stock']:
                                existing_item['quantity'] = new_quantity
                                existing_item['total'] = new_quantity * product['price']
                                print(f"✅ Đã cập nhật số lượng {product['name']} thành {new_quantity}")
                            else:
                                print(f"❌ Tổng số lượng vượt quá kho ({product['stock']})!")
                                continue
                        else:
                            cart_item = {
                                'code': product_code,
                                'name': product['name'],
                                'price': product['price'],
                                'quantity': quantity,
                                'total': quantity * product['price']
                            }
                            cart.append(cart_item)
                            print(f"✅ Đã thêm {quantity} {product['name']} vào giỏ hàng")
                        
                        break
                except ValueError:
                    print("❌ Vui lòng nhập số!")
            
            add_more = input("Thêm sản phẩm khác? (y/n): ").lower()
            if add_more not in ['y', 'yes', 'có']:
                break
    
    def view_cart():
        """Xem giỏ hàng"""
        if not cart:
            print("🛒 Giỏ hàng trống!")
            return
        
        print(f"\n🛒 GIỎ HÀNG ({len(cart)} loại sản phẩm)")
        print("-" * 70)
        print(f"{'STT':<4} {'Tên sản phẩm':<20} {'Giá':<12} {'SL':<4} {'Thành tiền':<15}")
        print("-" * 70)
        
        total_amount = 0
        for i, item in enumerate(cart, 1):
            price_str = f"{item['price']:,}đ"
            total_str = f"{item['total']:,}đ"
            print(f"{i:<4} {item['name']:<20} {price_str:<12} {item['quantity']:<4} {total_str:<15}")
            total_amount += item['total']
        
        print("-" * 70)
        print(f"{'TỔNG TIỀN:':<41} {total_amount:,}đ")
        
        return total_amount
    
    def update_cart():
        """Cập nhật giỏ hàng"""
        if not cart:
            print("🛒 Giỏ hàng trống!")
            return
        
        view_cart()
        
        try:
            item_index = int(input("\nChọn sản phẩm cần cập nhật (STT): ")) - 1
            
            if 0 <= item_index < len(cart):
                item = cart[item_index]
                product = products[item['code']]
                
                print(f"\nCập nhật: {item['name']}")
                print("1. Thay đổi số lượng")
                print("2. Xóa khỏi giỏ hàng")
                
                choice = input("Chọn (1-2): ")
                
                if choice == '1':
                    new_quantity = int(input(f"Số lượng mới (hiện tại: {item['quantity']}, kho: {product['stock']}): "))
                    
                    if new_quantity <= 0:
                        cart.pop(item_index)
                        print("✅ Đã xóa sản phẩm khỏi giỏ hàng")
                    elif new_quantity <= product['stock']:
                        item['quantity'] = new_quantity
                        item['total'] = new_quantity * item['price']
                        print(f"✅ Đã cập nhật số lượng thành {new_quantity}")
                    else:
                        print(f"❌ Vượt quá số lượng kho ({product['stock']})!")
                elif choice == '2':
                    removed_item = cart.pop(item_index)
                    print(f"✅ Đã xóa {removed_item['name']} khỏi giỏ hàng")
            else:
                print("❌ STT không hợp lệ!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    def apply_discount(total):
        """Áp dụng giảm giá"""
        print(f"\n💰 TỔNG TIỀN: {total:,}đ")
        print("\n🎫 ÁP DỤNG GIẢM GIÁ:")
        print("1. Khách hàng thân thiết (-10%)")
        print("2. Sinh viên (-15%)")
        print("3. Mua trên 50 triệu (-20%)")
        print("4. Không áp dụng")
        
        choice = input("Chọn loại giảm giá (1-4): ")
        discount = 0
        discount_name = ""
        
        if choice == '1':
            discount = 0.10
            discount_name = "Khách hàng thân thiết"
        elif choice == '2':
            discount = 0.15
            discount_name = "Sinh viên"
        elif choice == '3':
            if total >= 50000000:
                discount = 0.20
                discount_name = "Mua trên 50 triệu"
            else:
                print("❌ Không đủ điều kiện giảm giá này!")
                return total, 0, ""
        elif choice == '4':
            return total, 0, ""
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return total, 0, ""
        
        discount_amount = total * discount
        final_total = total - discount_amount
        
        print(f"🎫 Giảm giá {discount_name}: -{discount_amount:,}đ ({discount*100:.0f}%)")
        print(f"💳 Thành tiền: {final_total:,}đ")
        
        return final_total, discount_amount, discount_name
    
    def checkout():
        """Thanh toán"""
        if not cart:
            print("🛒 Giỏ hàng trống! Không thể thanh toán.")
            return
        
        print("\n💳 THANH TOÁN")
        total = view_cart()
        
        # Áp dụng giảm giá
        final_total, discount_amount, discount_name = apply_discount(total)
        
        # Nhập thông tin khách hàng
        print("\n👤 THÔNG TIN KHÁCH HÀNG:")
        customer_info['name'] = input("Họ tên: ")
        customer_info['phone'] = input("Số điện thoại: ")
        customer_info['address'] = input("Địa chỉ: ")
        
        # Chọn phương thức thanh toán
        print("\n💳 PHƯƠNG THỨC THANH TOÁN:")
        print("1. Tiền mặt")
        print("2. Thẻ tín dụng")
        print("3. Chuyển khoản")
        
        payment_methods = ["Tiền mặt", "Thẻ tín dụng", "Chuyển khoản"]
        while True:
            try:
                payment_choice = int(input("Chọn (1-3): ")) - 1
                if 0 <= payment_choice < 3:
                    payment_method = payment_methods[payment_choice]
                    break
                print("❌ Chọn từ 1-3!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Xác nhận thanh toán
        print(f"\n📋 XÁC NHẬN ĐỊA ĐƠN HÀNG")
        print("-" * 40)
        print(f"Khách hàng: {customer_info['name']}")
        print(f"Điện thoại: {customer_info['phone']}")
        print(f"Địa chỉ: {customer_info['address']}")
        print(f"Tổng tiền hàng: {total:,}đ")
        if discount_amount > 0:
            print(f"Giảm giá: -{discount_amount:,}đ ({discount_name})")
        print(f"Thành tiền: {final_total:,}đ")
        print(f"Thanh toán: {payment_method}")
        
        confirm = input("\nXác nhận đặt hàng? (yes/no): ").lower()
        
        if confirm in ['yes', 'y', 'có']:
            # Cập nhật kho
            for item in cart:
                products[item['code']]['stock'] -= item['quantity']
            
            # Tạo mã đơn hàng
            order_id = f"DH{random.randint(10000, 99999)}"
            
            print(f"\n✅ ĐẶT HÀNG THÀNH CÔNG!")
            print(f"🆔 Mã đơn hàng: {order_id}")
            print(f"💰 Tổng tiền: {final_total:,}đ")
            print(f"🚚 Đơn hàng sẽ được giao trong 2-3 ngày!")
            
            # Xóa giỏ hàng
            cart.clear()
        else:
            print("❌ Đã hủy đơn hàng!")
    
    def search_products():
        """Tìm kiếm sản phẩm"""
        print("\n🔍 TÌM KIẾM SẢN PHẨM")
        print("1. Tìm theo tên")
        print("2. Tìm theo danh mục")
        print("3. Tìm theo khoảng giá")
        
        choice = input("Chọn (1-3): ")
        found_products = {}
        
        if choice == '1':
            search_name = input("Nhập tên sản phẩm: ").lower()
            found_products = {code: info for code, info in products.items() 
                            if search_name in info['name'].lower()}
        elif choice == '2':
            search_category = input("Nhập danh mục: ").lower()
            found_products = {code: info for code, info in products.items() 
                            if search_category in info['category'].lower()}
        elif choice == '3':
            try:
                min_price = int(input("Giá từ: "))
                max_price = int(input("Giá đến: "))
                found_products = {code: info for code, info in products.items() 
                                if min_price <= info['price'] <= max_price}
            except ValueError:
                print("❌ Vui lòng nhập số!")
                return
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return
        
        if found_products:
            print(f"\n🎯 TÌM THẤY {len(found_products)} SẢN PHẨM:")
            print("-" * 80)
            print(f"{'Mã SP':<8} {'Tên sản phẩm':<20} {'Giá':<15} {'Kho':<6} {'Danh mục':<12}")
            print("-" * 80)
            
            for code, info in found_products.items():
                price_str = f"{info['price']:,}đ"
                stock_status = f"{info['stock']}" if info['stock'] > 0 else "Hết hàng"
                print(f"{code:<8} {info['name']:<20} {price_str:<15} {stock_status:<6} {info['category']:<12}")
        else:
            print("❌ Không tìm thấy sản phẩm nào!")
    
    # Main menu
    while True:
        total_items = sum(item['quantity'] for item in cart)
        print(f"\n🛒 SHOPPING CART - Giỏ hàng: {total_items} sản phẩm")
        print("1. Xem sản phẩm")
        print("2. Tìm kiếm sản phẩm")
        print("3. Thêm vào giỏ hàng")
        print("4. Xem giỏ hàng")
        print("5. Cập nhật giỏ hàng")
        print("6. Thanh toán")
        print("7. Thoát")
        
        choice = input("Chọn (1-7): ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            search_products()
        elif choice == '3':
            add_to_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            update_cart()
        elif choice == '6':
            checkout()
        elif choice == '7':
            if cart:
                save_cart = input("Bạn có muốn lưu giỏ hàng? (y/n): ").lower()
                if save_cart in ['y', 'yes', 'có']:
                    print("💾 Giỏ hàng đã được lưu!")
            print("👋 Cảm ơn bạn đã mua sắm!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# ỨNG DỤNG 6: PASSWORD GENERATOR
# =============================================================================

def password_generator():
    """Trình tạo mật khẩu an toàn"""
    print("\n🔐 ỨNG DỤNG 6: PASSWORD GENERATOR")
    print("=" * 40)
    
    password_history = []
    
    def generate_password():
        """Tạo mật khẩu theo yêu cầu"""
        print("\n🔑 TẠO MẬT KHẨU MỚI")
        
        # Cấu hình mật khẩu
        while True:
            try:
                length = int(input("Độ dài mật khẩu (8-128): "))
                if 8 <= length <= 128:
                    break
                print("❌ Độ dài phải từ 8-128 ký tự!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
        
        # Tùy chọn ký tự
        print("\nTùy chọn ký tự (chọn ít nhất 1):")
        
        include_upper = input("Bao gồm chữ HOA (A-Z)? (y/n): ").lower() in ['y', 'yes', 'có']
        include_lower = input("Bao gồm chữ thường (a-z)? (y/n): ").lower() in ['y', 'yes', 'có']
        include_numbers = input("Bao gồm số (0-9)? (y/n): ").lower() in ['y', 'yes', 'có']
        include_symbols = input("Bao gồm ký tự đặc biệt (!@#$%^&*)? (y/n): ").lower() in ['y', 'yes', 'có']
        
        if not any([include_upper, include_lower, include_numbers, include_symbols]):
            print("❌ Phải chọn ít nhất 1 loại ký tự!")
            return
        
        # Tạo bộ ký tự
        charset = ""
        if include_upper:
            charset += string.ascii_uppercase
        if include_lower:
            charset += string.ascii_lowercase
        if include_numbers:
            charset += string.digits
        if include_symbols:
            charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Tạo mật khẩu
        password = ''.join(random.choice(charset) for _ in range(length))
        
        # Đảm bảo có ít nhất 1 ký tự từ mỗi loại được chọn
        if include_upper and not any(c.isupper() for c in password):
            password = password[:-1] + random.choice(string.ascii_uppercase)
        if include_lower and not any(c.islower() for c in password):
            password = password[:-1] + random.choice(string.ascii_lowercase)
        if include_numbers and not any(c.isdigit() for c in password):
            password = password[:-1] + random.choice(string.digits)
        if include_symbols and not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            password = password[:-1] + random.choice("!@#$%^&*")
        
        # Trộn lại mật khẩu
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        print(f"\n✅ MẬT KHẨU ĐÃ TẠO:")
        print(f"🔑 {password}")
        
        # Đánh giá độ mạnh
        strength = check_password_strength(password)
        print(f"💪 Độ mạnh: {strength}")
        
        # Lưu vào lịch sử
        password_entry = {
            "password": password,
            "length": length,
            "strength": strength,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        password_history.append(password_entry)
        
        # Tùy chọn lưu
        save_choice = input("\nLưu mật khẩu này? (y/n): ").lower()
        if save_choice in ['y', 'yes', 'có']:
            purpose = input("Mục đích sử dụng (tùy chọn): ")
            password_entry["purpose"] = purpose
            print("💾 Đã lưu mật khẩu!")
        
        return password
    
    def check_password_strength(password):
        """Kiểm tra độ mạnh mật khẩu"""
        score = 0
        feedback = []
        
        # Độ dài
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Quá ngắn")
        
        # Ký tự hoa
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Thiếu chữ hoa")
        
        # Ký tự thường
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Thiếu chữ thường")
        
        # Số
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Thiếu số")
        
        # Ký tự đặc biệt
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
        else:
            feedback.append("Thiếu ký tự đặc biệt")
        
        # Không có pattern đơn giản
        if not any(password[i:i+3].isdigit() for i in range(len(password)-2)):
            score += 1
        
        # Đánh giá
        if score >= 6:
            return "Rất mạnh 💪"
        elif score >= 4:
            return "Mạnh 👍"
        elif score >= 3:
            return "Trung bình ⚠️"
        else:
            return f"Yếu ❌ ({', '.join(feedback)})"
    
    def validate_existing_password():
        """Kiểm tra mật khẩu hiện có"""
        print("\n🔍 KIỂM TRA MẬT KHẨU HIỆN CÓ")
        
        password = input("Nhập mật khẩu cần kiểm tra: ")
        
        if not password:
            print("❌ Vui lòng nhập mật khẩu!")
            return
        
        print(f"\n📊 PHÂN TÍCH MẬT KHẨU: {password}")
        print("-" * 40)
        
        # Thông tin cơ bản
        print(f"Độ dài: {len(password)} ký tự")
        print(f"Độ mạnh: {check_password_strength(password)}")
        
        # Chi tiết
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        print(f"Chữ hoa: {'✅' if has_upper else '❌'}")
        print(f"Chữ thường: {'✅' if has_lower else '❌'}")
        print(f"Số: {'✅' if has_digit else '❌'}")
        print(f"Ký tự đặc biệt: {'✅' if has_symbol else '❌'}")
        
        # Cảnh báo
        warnings = []
        if "123" in password or "abc" in password.lower():
            warnings.append("Chứa chuỗi ký tự liên tiếp")
        if password.lower() in ["password", "123456", "qwerty"]:
            warnings.append("Là mật khẩu phổ biến")
        if len(set(password)) < len(password) * 0.7:
            warnings.append("Nhiều ký tự lặp lại")
        
        if warnings:
            print("\n⚠️ CẢNH BÁO:")
            for warning in warnings:
                print(f"- {warning}")
        
        # Gợi ý cải thiện
        suggestions = []
        if len(password) < 12:
            suggestions.append("Tăng độ dài lên ít nhất 12 ký tự")
        if not has_upper:
            suggestions.append("Thêm chữ hoa")
        if not has_lower:
            suggestions.append("Thêm chữ thường")
        if not has_digit:
            suggestions.append("Thêm số")
        if not has_symbol:
            suggestions.append("Thêm ký tự đặc biệt")
        
        if suggestions:
            print("\n💡 GỢI Ý CẢI THIỆN:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
    
    def view_password_history():
        """Xem lịch sử mật khẩu"""
        if not password_history:
            print("📝 Chưa có mật khẩu nào được tạo!")
            return
        
        print(f"\n📚 LỊCH SỬ MẬT KHẨU ({len(password_history)} mật khẩu)")
        print("-" * 80)
        
        for i, entry in enumerate(password_history, 1):
            print(f"\n{i}. Tạo lúc: {entry['created']}")
            print(f"   Mật khẩu: {entry['password']}")
            print(f"   Độ dài: {entry['length']} ký tự")
            print(f"   Độ mạnh: {entry['strength']}")
            if 'purpose' in entry and entry['purpose']:
                print(f"   Mục đích: {entry['purpose']}")
    
    def password_tips():
        """Mẹo về mật khẩu an toàn"""
        print("\n💡 MẸO TẠO MẬT KHẨU AN TOÀN")
        print("-" * 40)
        
        tips = [
            "Sử dụng ít nhất 12 ký tự",
            "Kết hợp chữ hoa, chữ thường, số và ký tự đặc biệt",
            "Tránh thông tin cá nhân (tên, ngày sinh, số điện thoại)",
            "Không sử dụng từ trong từ điển",
            "Mỗi tài khoản nên có mật khẩu riêng",
            "Thay đổi mật khẩu định kỳ (3-6 tháng)",
            "Sử dụng trình quản lý mật khẩu",
            "Bật xác thực 2 yếu tố khi có thể",
            "Không chia sẻ mật khẩu với ai",
            "Kiểm tra định kỳ xem tài khoản có bị hack không"
        ]
        
        for i, tip in enumerate(tips, 1):
            print(f"{i:2}. {tip}")
        
        print("\n🚨 DẤU HIỆU MẬT KHẨU YẾU:")
        weak_signs = [
            "Ngắn hơn 8 ký tự",
            "Chỉ chứa chữ cái hoặc chỉ chứa số",
            "Là thông tin cá nhân",
            "Là từ trong từ điển",
            "Có pattern đơn giản (123456, abcdef)",
            "Được sử dụng cho nhiều tài khoản"
        ]
        
        for sign in weak_signs:
            print(f"❌ {sign}")
    
    def generate_passphrase():
        """Tạo passphrase (cụm từ mật khẩu)"""
        print("\n📝 TẠO PASSPHRASE")
        
        word_lists = {
            "animals": ["cat", "dog", "elephant", "tiger", "lion", "bear", "wolf", "fox"],
            "colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black"],
            "objects": ["house", "car", "book", "tree", "mountain", "river", "star", "moon"],
            "actions": ["run", "jump", "fly", "swim", "dance", "sing", "write", "read"]
        }
        
        try:
            num_words = int(input("Số từ trong passphrase (3-6): "))
            if not 3 <= num_words <= 6:
                print("❌ Số từ phải từ 3-6!")
                return
        except ValueError:
            print("❌ Vui lòng nhập số!")
            return
        
        # Tạo passphrase
        words = []
        for _ in range(num_words):
            category = random.choice(list(word_lists.keys()))
            word = random.choice(word_lists[category])
            words.append(word.capitalize())
        
        # Thêm số và ký tự đặc biệt
        separator = random.choice(["-", "_", ".", "!"])
        number = random.randint(10, 99)
        
        passphrase = separator.join(words) + str(number)
        
        print(f"\n✅ PASSPHRASE ĐÃ TẠO:")
        print(f"🔑 {passphrase}")
        print(f"📏 Độ dài: {len(passphrase)} ký tự")
        print(f"💪 Dễ nhớ và an toàn!")
        
        # Lưu vào lịch sử
        password_entry = {
            "password": passphrase,
            "length": len(passphrase),
            "strength": "Mạnh (Passphrase)",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "passphrase"
        }
        password_history.append(password_entry)
    
    # Main menu
    while True:
        print(f"\n🔐 PASSWORD GENERATOR - {len(password_history)} mật khẩu đã tạo")
        print("1. Tạo mật khẩu ngẫu nhiên")
        print("2. Tạo passphrase")
        print("3. Kiểm tra mật khẩu hiện có")
        print("4. Xem lịch sử")
        print("5. Mẹo bảo mật")
        print("6. Thoát")
        
        choice = input("Chọn (1-6): ")
        
        if choice == '1':
            generate_password()
        elif choice == '2':
            generate_passphrase()
        elif choice == '3':
            validate_existing_password()
        elif choice == '4':
            view_password_history()
        elif choice == '5':
            password_tips()
        elif choice == '6':
            print("🔒 Cảm ơn bạn đã sử dụng Password Generator!")
            print("💡 Nhớ lưu mật khẩu ở nơi an toàn!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# MENU CHÍNH - CHỌN ỨNG DỤNG
# =============================================================================

def main_menu():
    """Menu chính để chọn ứng dụng"""
    while True:
        print("\n🎯 CHỌN ỨNG DỤNG THỰC TẾ")
        print("=" * 40)
        print("1. 🏦 Hệ thống ATM")
        print("2. 🧠 Game Quiz")
        print("3. 🎓 Quản lý học sinh")
        print("4. 🌤️ Weather Tracker")
        print("5. 🛒 Shopping Cart")
        print("6. 🔐 Password Generator")
        print("7. 🚪 Thoát")
        
        choice = input("Chọn ứng dụng (1-7): ")
        
        if choice == '1':
            atm_system()
        elif choice == '2':
            quiz_game()
        elif choice == '3':
            student_management()
        elif choice == '4':
            weather_tracker()
        elif choice == '5':
            shopping_cart()
        elif choice == '6':
            password_generator()
        elif choice == '7':
            print("👋 Cảm ơn bạn đã sử dụng các ứng dụng!")
            print("🎉 Chúc mừng bạn đã hoàn thành Bài Tập 4!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================================================================
# CHẠY CHƯƠNG TRÌNH
# =============================================================================

if __name__ == "__main__":
    print("🔥 CHÀO MỪNG ĐẾN VỚI BÀI TẬP 4!")
    print("6 ứng dụng thực tế hoàn chỉnh với vòng lặp")
    print("Mỗi ứng dụng minh họa cách sử dụng for/while loops")
    print("trong các tình huống thực tế khác nhau.")
    
    main_menu()
    
    print("\n🏆 TỔNG KẾT BÀI TẬP 4")
    print("=" * 30)
    print("KIẾN THỨC ĐÃ ỨNG DỤNG:")
    print("✅ While loops với menu systems")
    print("✅ For loops với data processing")
    print("✅ Input validation và error handling")
    print("✅ Nested loops cho algorithms")
    print("✅ Break/continue trong business logic")
    print("✅ Data structures với loops")
    print("✅ User interface design")
    print("✅ Real-world problem solving")
    
    print("\n🌟 SKILLS PHÁT TRIỂN:")
    print("□ System design thinking")
    print("□ User experience awareness")  
    print("□ Data management")
    print("□ Security mindset")
    print("□ Code organization")
    print("□ Testing và debugging")
    
    print("\n🎯 BẠN ĐÃ SẴN SÀNG CHO:")
    print("- Xây dựng ứng dụng hoàn chỉnh")
    print("- Làm việc với dữ liệu phức tạp")
    print("- Thiết kế user interfaces")
    print("- Giải quyết bài toán thực tế")
    
    print("\n🚀 TIẾP THEO: DỰ ÁN LỚN VÀ QUIZ TỔNG HỢP!") 