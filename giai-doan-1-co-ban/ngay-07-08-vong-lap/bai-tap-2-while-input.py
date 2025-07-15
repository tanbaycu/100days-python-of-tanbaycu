"""
BÀI TẬP 2: VÒNG LẶP WHILE VÀ USER INPUT
======================================

Bài tập này tập trung vào while loops kết hợp với input() và validation.
Gồm 10 phần từ cơ bản đến nâng cao.

Yêu cầu:
- Hiểu rõ cách hoạt động của while
- Biết cách tránh infinite loops
- Thành thạo input validation
- Xây dựng được menu systems

Thời gian ước tính: 120-150 phút
"""

print("🎯 BÀI TẬP 2: VÒNG LẶP WHILE & USER INPUT")
print("=" * 50)

# =============================================================================
# PHẦN A: WHILE CƠ BẢN VỚI COUNTERS
# =============================================================================

print("\n📖 PHẦN A: WHILE CƠ BẢN VỚI COUNTERS")
print("-" * 40)

# A.1. Ví dụ: While với counter tăng dần
print("A.1. Ví dụ: Đếm từ 1 đến 5")
count = 1
while count <= 5:
    print(f"Đếm: {count}")
    count += 1  # QUAN TRỌNG: Phải tăng counter
print("Kết thúc đếm!")

# A.2. Ví dụ: While với counter giảm dần
print("\nA.2. Ví dụ: Đếm ngược từ 5 về 1")
countdown = 5
while countdown >= 1:
    print(f"Còn: {countdown}")
    countdown -= 1
print("🚀 Hết giờ!")

# A.3. Ví dụ: While với điều kiện phức tạp
print("\nA.3. Ví dụ: Tính tổng đến khi > 100")
total = 0
current = 1
while total <= 100:
    total += current
    print(f"Cộng {current}, tổng = {total}")
    current += 1
print(f"Kết quả: Tổng = {total}")

# A.4. Ví dụ: While với boolean flag
print("\nA.4. Ví dụ: Sử dụng boolean flag")
running = True
step = 0
while running:
    step += 1
    print(f"Bước {step}")
    if step >= 3:
        running = False  # Thay đổi flag để thoát
print("Hoàn thành!")

print("\n🏃‍♂️ BÀI TẬP PHẦN A:")
print("1. Đếm từ 10 đến 20 bằng while")
print("2. Đếm ngược từ 25 về 15")
print("3. Tính tổng các số từ 1 đến 50")
print("4. In các số chẵn từ 2 đến 20")
print("5. Tính 2^10 bằng while loop")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN A ---")

# Bài 1: Đếm từ 10 đến 20


# Bài 2: Đếm ngược từ 25 về 15


# Bài 3: Tính tổng từ 1 đến 50


# Bài 4: In số chẵn từ 2 đến 20


# Bài 5: Tính 2^10


# =============================================================================
# PHẦN B: INPUT VALIDATION CƠ BẢN
# =============================================================================

print("\n📖 PHẦN B: INPUT VALIDATION CƠ BẢN")
print("-" * 40)

# B.1. Ví dụ: Validation số nguyên
print("B.1. Ví dụ: Nhập số nguyên hợp lệ")
while True:
    try:
        number = int(input("Nhập một số nguyên: "))
        print(f"✅ Bạn đã nhập: {number}")
        break  # Thoát loop khi input hợp lệ
    except ValueError:
        print("❌ Lỗi! Vui lòng nhập số nguyên!")

# B.2. Ví dụ: Validation số dương
print("\nB.2. Ví dụ: Nhập số dương")
while True:
    try:
        positive_num = float(input("Nhập số dương: "))
        if positive_num > 0:
            print(f"✅ Số dương hợp lệ: {positive_num}")
            break
        else:
            print("❌ Số phải lớn hơn 0!")
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")

# B.3. Ví dụ: Validation yes/no
print("\nB.3. Ví dụ: Validation yes/no")
while True:
    answer = input("Bạn có muốn tiếp tục? (yes/no): ").lower()
    if answer in ['yes', 'y', 'có']:
        print("✅ Tiếp tục...")
        break
    elif answer in ['no', 'n', 'không']:
        print("✅ Dừng lại...")
        break
    else:
        print("❌ Vui lòng nhập 'yes' hoặc 'no'!")

print("\n🏃‍♂️ BÀI TẬP PHẦN B:")
print("1. Nhập tuổi (1-120)")
print("2. Nhập điểm số (0-10)")
print("3. Nhập tên (không được rỗng)")
print("4. Nhập email (phải có @ và .)")
print("5. Nhập mật khẩu (ít nhất 6 ký tự)")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN B ---")

# Bài 1: Nhập tuổi hợp lệ (1-120)


# Bài 2: Nhập điểm số (0-10)


# Bài 3: Nhập tên không rỗng


# Bài 4: Nhập email có @ và .


# Bài 5: Nhập mật khẩu ít nhất 6 ký tự


# =============================================================================
# PHẦN C: MENU SYSTEMS
# =============================================================================

print("\n📖 PHẦN C: MENU SYSTEMS")
print("-" * 40)

# C.1. Ví dụ: Menu đơn giản
print("C.1. Ví dụ: Menu Calculator đơn giản")
while True:
    print("\n=== CALCULATOR ===")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Thoát")
    
    choice = input("Chọn (1-3): ")
    
    if choice == '1':
        try:
            a = float(input("Số thứ nhất: "))
            b = float(input("Số thứ hai: "))
            print(f"Kết quả: {a} + {b} = {a + b}")
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập số!")
    elif choice == '2':
        try:
            a = float(input("Số thứ nhất: "))
            b = float(input("Số thứ hai: "))
            print(f"Kết quả: {a} - {b} = {a - b}")
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập số!")
    elif choice == '3':
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")

# C.2. Ví dụ: Menu với counter
print("\nC.2. Ví dụ: Menu với đếm lựa chọn")
total_operations = 0
while True:
    print(f"\n=== MENU (Đã thực hiện: {total_operations} lần) ===")
    print("1. In thông báo")
    print("2. Tính bình phương")
    print("3. Xem thống kê")
    print("4. Thoát")
    
    option = input("Chọn: ")
    
    if option == '1':
        message = input("Nhập thông báo: ")
        print(f"📢 {message}")
        total_operations += 1
    elif option == '2':
        try:
            num = float(input("Nhập số: "))
            print(f"{num}² = {num**2}")
            total_operations += 1
        except ValueError:
            print("❌ Số không hợp lệ!")
    elif option == '3':
        print(f"📊 Bạn đã thực hiện {total_operations} thao tác")
    elif option == '4':
        print(f"Cảm ơn! Tổng cộng {total_operations} thao tác")
        break
    else:
        print("❌ Không hợp lệ!")

print("\n🏃‍♂️ BÀI TẬP PHẦN C:")
print("1. Tạo menu quản lý sinh viên (thêm, xem, thoát)")
print("2. Menu tính toán nâng cao (4 phép tính)")
print("3. Menu game đơn giản (play, score, quit)")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN C ---")

# Bài 1: Menu quản lý sinh viên


# Bài 2: Menu calculator nâng cao


# Bài 3: Menu game


# =============================================================================
# PHẦN D: GAMES VỚI WHILE
# =============================================================================

print("\n📖 PHẦN D: GAMES VỚI WHILE")
print("-" * 40)

# D.1. Ví dụ: Game đoán số đơn giản
import random

print("D.1. Ví dụ: Game đoán số")
secret = random.randint(1, 10)
attempts = 0
max_attempts = 3

print(f"🎯 Đoán số từ 1-10! Bạn có {max_attempts} lần thử.")

while attempts < max_attempts:
    try:
        guess = int(input(f"Lần {attempts + 1}: "))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 Đúng! Số là {secret}")
            break
        elif guess < secret:
            print("📈 Số cần tìm lớn hơn!")
        else:
            print("📉 Số cần tìm nhỏ hơn!")
            
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Còn {remaining} lần thử!")
    except ValueError:
        print("❌ Vui lòng nhập số!")
        attempts -= 1
else:
    print(f"💀 Hết lượt! Số đúng là {secret}")

# D.2. Ví dụ: Rock Paper Scissors
print("\nD.2. Ví dụ: Kéo Búa Bao mini")
choices = ['kéo', 'búa', 'bao']
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"\nTỷ số: Bạn {player_wins} - {computer_wins} Máy")
    player_choice = input("Chọn (kéo/búa/bao): ").lower()
    
    if player_choice not in choices:
        print("❌ Lựa chọn không hợp lệ!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Máy chọn: {computer_choice}")
    
    if player_choice == computer_choice:
        print("🤝 Hòa!")
    elif (player_choice == 'kéo' and computer_choice == 'bao') or \
         (player_choice == 'búa' and computer_choice == 'kéo') or \
         (player_choice == 'bao' and computer_choice == 'búa'):
        print("🎉 Bạn thắng!")
        player_wins += 1
    else:
        print("💻 Máy thắng!")
        computer_wins += 1

if player_wins == 2:
    print("🏆 Bạn chiến thắng!")
else:
    print("🤖 Máy chiến thắng!")

print("\n🏃‍♂️ BÀI TẬP PHẦN D:")
print("1. Game đoán số 1-100 với hints")
print("2. Quiz trắc nghiệm đơn giản")
print("3. Game đếm ngược với random stops")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN D ---")

# Bài 1: Game đoán số 1-100


# Bài 2: Quiz trắc nghiệm


# Bài 3: Game đếm ngược random


# =============================================================================
# PHẦN E: DATA COLLECTION VÀ PROCESSING
# =============================================================================

print("\n📖 PHẦN E: DATA COLLECTION & PROCESSING")
print("-" * 50)

# E.1. Ví dụ: Thu thập và xử lý điểm số
print("E.1. Ví dụ: Thu thập điểm học sinh")
scores = []
student_count = 0

while True:
    student_input = input(f"Điểm học sinh {student_count + 1} (hoặc 'done'): ")
    
    if student_input.lower() == 'done':
        break
    
    try:
        score = float(student_input)
        if 0 <= score <= 10:
            scores.append(score)
            student_count += 1
            print(f"✅ Đã thêm điểm {score}")
        else:
            print("❌ Điểm phải từ 0-10!")
    except ValueError:
        print("❌ Vui lòng nhập số!")

if scores:
    average = sum(scores) / len(scores)
    print(f"\n📊 Thống kê {student_count} học sinh:")
    print(f"Điểm trung bình: {average:.2f}")
    print(f"Điểm cao nhất: {max(scores)}")
    print(f"Điểm thấp nhất: {min(scores)}")

# E.2. Ví dụ: Shopping cart đơn giản
print("\nE.2. Ví dụ: Shopping cart")
cart = []
total_price = 0

while True:
    print(f"\n🛒 Giỏ hàng (Tổng: {total_price}đ)")
    print("1. Thêm sản phẩm")
    print("2. Xem giỏ hàng")
    print("3. Thanh toán")
    
    choice = input("Chọn: ")
    
    if choice == '1':
        item = input("Tên sản phẩm: ")
        try:
            price = float(input("Giá: "))
            if price > 0:
                cart.append((item, price))
                total_price += price
                print(f"✅ Đã thêm {item} - {price}đ")
            else:
                print("❌ Giá phải > 0!")
        except ValueError:
            print("❌ Giá không hợp lệ!")
    elif choice == '2':
        if cart:
            print("📦 Giỏ hàng:")
            for i, (item, price) in enumerate(cart, 1):
                print(f"{i}. {item}: {price}đ")
        else:
            print("Giỏ hàng trống!")
    elif choice == '3':
        print(f"💰 Thanh toán: {total_price}đ")
        break
    else:
        print("❌ Không hợp lệ!")

print("\n🏃‍♂️ BÀI TẬP PHẦN E:")
print("1. Thu thập thông tin nhân viên")
print("2. Quản lý sách thư viện")
print("3. Tracking chi tiêu hàng ngày")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN E ---")

# Bài 1: Thu thập thông tin nhân viên


# Bài 2: Quản lý sách


# Bài 3: Tracking chi tiêu


# =============================================================================
# PHẦN F: PASSWORD VÀ SECURITY
# =============================================================================

print("\n📖 PHẦN F: PASSWORD & SECURITY")
print("-" * 40)

# F.1. Ví dụ: Password validation với attempts
print("F.1. Ví dụ: Hệ thống đăng nhập")
correct_password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Nhập mật khẩu: ")
    
    if password == correct_password:
        print("✅ Đăng nhập thành công!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Sai mật khẩu! Còn {remaining} lần thử.")
        else:
            print("🚫 Hết lượt thử! Tài khoản bị khóa.")

# F.2. Ví dụ: Password strength checker
print("\nF.2. Ví dụ: Kiểm tra độ mạnh mật khẩu")
while True:
    new_password = input("Tạo mật khẩu mới: ")
    
    # Kiểm tra các tiêu chí
    length_ok = len(new_password) >= 8
    has_upper = any(c.isupper() for c in new_password)
    has_lower = any(c.islower() for c in new_password)
    has_digit = any(c.isdigit() for c in new_password)
    
    print("🔒 Kiểm tra mật khẩu:")
    print(f"Độ dài ≥ 8: {'✅' if length_ok else '❌'}")
    print(f"Có chữ hoa: {'✅' if has_upper else '❌'}")
    print(f"Có chữ thường: {'✅' if has_lower else '❌'}")
    print(f"Có số: {'✅' if has_digit else '❌'}")
    
    if all([length_ok, has_upper, has_lower, has_digit]):
        print("🔐 Mật khẩu mạnh! Đã chấp nhận.")
        break
    else:
        print("⚠️ Mật khẩu yếu! Vui lòng thử lại.")

print("\n🏃‍♂️ BÀI TẬP PHẦN F:")
print("1. Hệ thống đăng nhập với username")
print("2. Tạo PIN 4 số với validation")
print("3. Password generator đơn giản")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN F ---")

# Bài 1: Đăng nhập với username + password


# Bài 2: Tạo PIN 4 số


# Bài 3: Password generator


# =============================================================================
# PHẦN G: ATM SIMULATION
# =============================================================================

print("\n📖 PHẦN G: ATM SIMULATION")
print("-" * 40)

# G.1. Ví dụ: ATM đơn giản
print("G.1. Ví dụ: Máy ATM đơn giản")
balance = 1000000  # Số dư ban đầu
pin = "1234"

# Xác thực PIN
attempts = 0
while attempts < 3:
    entered_pin = input("Nhập PIN: ")
    if entered_pin == pin:
        print("✅ PIN chính xác!")
        break
    else:
        attempts += 1
        if attempts < 3:
            print(f"❌ PIN sai! Còn {3-attempts} lần thử.")
        else:
            print("🚫 Thẻ bị khóa!")
            exit()

# Menu ATM
while True:
    print(f"\n💳 ATM MENU (Số dư: {balance:,}đ)")
    print("1. Kiểm tra số dư")
    print("2. Rút tiền")
    print("3. Nạp tiền")
    print("4. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == '1':
        print(f"💰 Số dư hiện tại: {balance:,}đ")
    elif choice == '2':
        try:
            amount = int(input("Số tiền cần rút: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"✅ Rút {amount:,}đ thành công!")
                    print(f"Số dư còn lại: {balance:,}đ")
                else:
                    print("❌ Số dư không đủ!")
            else:
                print("❌ Số tiền phải > 0!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    elif choice == '3':
        try:
            amount = int(input("Số tiền nạp: "))
            if amount > 0:
                balance += amount
                print(f"✅ Nạp {amount:,}đ thành công!")
                print(f"Số dư mới: {balance:,}đ")
            else:
                print("❌ Số tiền phải > 0!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    elif choice == '4':
        print("👋 Cảm ơn bạn đã sử dụng ATM!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")

print("\n🏃‍♂️ BÀI TẬP PHẦN G:")
print("1. ATM với lịch sử giao dịch")
print("2. ATM với nhiều loại thẻ")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN G ---")

# Bài 1: ATM với lịch sử


# Bài 2: ATM nhiều thẻ


# =============================================================================
# TỔNG KẾT VÀ ĐÁNH GIÁ
# =============================================================================

print("\n" + "="*50)
print("🏆 TỔNG KẾT BÀI TẬP 2")
print("="*50)

print("""
KIẾN THỨC ĐÃ HỌC:
✅ While loops với counters
✅ Input validation techniques
✅ Menu systems development
✅ Game programming basics
✅ Data collection & processing
✅ Security & password handling
✅ ATM simulation

ĐIỂM ĐÁNH GIÁ BẢN THÂN:
- Phần A (While cơ bản): ___/5
- Phần B (Input validation): ___/5
- Phần C (Menu systems): ___/3
- Phần D (Games): ___/3
- Phần E (Data processing): ___/3
- Phần F (Security): ___/3
- Phần G (ATM): ___/2

TỔNG ĐIỂM: ___/24

CHUẨN ĐÁNH GIÁ:
🥇 21-24 điểm: Xuất sắc!
🥈 17-20 điểm: Giỏi!
🥉 13-16 điểm: Khá
📚 9-12 điểm: Cần ôn lại
💪 <9 điểm: Học lại từ đầu

SKILLS ĐÃ PHÁT TRIỂN:
□ Tư duy logic với while loops
□ Input validation & error handling
□ User interface design (menu)
□ Game development basics
□ Data management
□ Security awareness

GHI CHÚ PHẢN HỒI:
- Phần khó nhất: ________________
- Phần thú vị nhất: ______________
- Kỹ năng cần cải thiện: __________
- Ứng dụng thực tế nghĩ ra: _______
""")

print("🔥 Sẵn sàng cho Bài Tập 3: Break, Continue & Nested Loops!")

# =============================================================================
# BONUS: PROJECTS TÍCH HỢP (TUỲ CHỌN)
# =============================================================================

print("\n🌟 BONUS - PROJECTS TÍCH HỢP:")
print("Chỉ làm khi đã thành thạo tất cả phần trên!")
print("-" * 50)

print("1. 🏪 Mini Store Management System")
print("2. 🎮 Adventure Game với nhiều rooms")
print("3. 📚 Library Book Lending System")
print("4. 💰 Personal Finance Tracker")
print("5. 🎯 Complete Quiz System với scoring")

# Bonus projects (advanced):
print("\n--- BONUS PROJECT CODE ---")

# Chọn 1 project để thực hiện:


print("\n🎊 XIN CHÚC MỪNG! BẠN ĐÃ THÀNH THẠO WHILE LOOPS!") 