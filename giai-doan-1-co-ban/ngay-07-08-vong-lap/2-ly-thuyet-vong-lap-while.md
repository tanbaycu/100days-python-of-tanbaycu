# Lý Thuyết: Vòng Lặp While - Chi Tiết Toàn Diện

## 🎯 Mục Tiêu Chương

Sau khi học xong chương này, bạn sẽ:
- ✅ Hiểu hoàn toàn về vòng lặp while
- ✅ Biết cách tạo và kiểm soát điều kiện lặp
- ✅ Tránh được infinite loops
- ✅ Kết hợp while với input() và validation
- ✅ Sử dụng while để tạo menu systems

---

## 📖 1. VÒNG LẶP WHILE LÀ GÌ?

### Định Nghĩa
**Vòng lặp while** lặp lại code miễn là điều kiện (condition) còn là `True`.

### Cú Pháp Cơ Bản
```python
while condition:
    # Code block sẽ được lặp lại
    statements
    # Phải có code để thay đổi condition
```

### Ví Dụ Đơn Giản
```python
# Đếm từ 1 đến 5
count = 1
while count <= 5:
    print(f"Đếm: {count}")
    count += 1  # QUAN TRỌNG: Phải thay đổi biến điều kiện

# Output:
# Đếm: 1
# Đếm: 2
# Đếm: 3
# Đếm: 4
# Đếm: 5
```

---

## ⚠️ 2. ĐIỀU KIỆN VÀ INFINITE LOOPS

### 2.1. Điều Kiện Hợp Lệ
```python
# Điều kiện với số
x = 0
while x < 3:
    print(x)
    x += 1

# Điều kiện với boolean
running = True
while running:
    user_input = input("Tiếp tục? (y/n): ")
    if user_input.lower() == 'n':
        running = False
```

### 2.2. NGUY HIỂM: Infinite Loops
```python
# SAI: Infinite loop - không có cách thoát
count = 1
while count <= 5:
    print(count)
    # Quên tăng count - loop vô tận!

# ĐÚNG: Có cách thay đổi điều kiện
count = 1
while count <= 5:
    print(count)
    count += 1  # Tăng count để thoát loop
```

### 2.3. Cách Phát Hiện Infinite Loop
```python
# Dấu hiệu: Code cứ chạy mãi không dừng
# Giải pháp: Ctrl+C để dừng program
# Prevention: Luôn đảm bảo có cách thay đổi condition
```

---

## 🔢 3. WHILE VỚI COUNTERS

### 3.1. Counter Tăng Dần
```python
# In số chẵn từ 0 đến 10
num = 0
while num <= 10:
    if num % 2 == 0:
        print(f"Số chẵn: {num}")
    num += 1
```

### 3.2. Counter Giảm Dần
```python
# Đếm ngược từ 10 về 0
countdown = 10
while countdown >= 0:
    if countdown == 0:
        print("🚀 Phóng!")
    else:
        print(f"Đếm ngược: {countdown}")
    countdown -= 1
```

### 3.3. Counter Với Step Khác
```python
# Tăng theo bước nhảy 2
value = 1
while value <= 20:
    print(value)
    value += 2  # Tăng 2 đơn vị mỗi lần

# Output: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
```

---

## 💬 4. WHILE VỚI USER INPUT

### 4.1. Input Validation Loop
```python
# Yêu cầu user nhập số dương
while True:
    try:
        number = int(input("Nhập một số dương: "))
        if number > 0:
            print(f"Bạn đã nhập: {number}")
            break  # Thoát loop khi input hợp lệ
        else:
            print("Vui lòng nhập số dương!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
```

### 4.2. Password Verification
```python
# Xác thực password với 3 lần thử
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Nhập password: ")
    
    if password == correct_password:
        print("✅ Đăng nhập thành công!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Sai password! Còn {remaining} lần thử.")
        else:
            print("🚫 Hết lượt thử! Tài khoản bị khóa.")
```

### 4.3. Menu Selection
```python
# Menu lựa chọn đơn giản
while True:
    print("\n=== MENU ===")
    print("1. Chào hỏi")
    print("2. Tính toán")
    print("3. Thoát")
    
    choice = input("Chọn (1-3): ")
    
    if choice == '1':
        name = input("Tên bạn là gì? ")
        print(f"Xin chào {name}!")
    elif choice == '2':
        try:
            a = float(input("Số thứ nhất: "))
            b = float(input("Số thứ hai: "))
            print(f"Tổng: {a + b}")
        except ValueError:
            print("Lỗi: Vui lòng nhập số!")
    elif choice == '3':
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
```

---

## 🎮 5. WHILE TRONG GAMES

### 5.1. Game Đoán Số Đơn Giản
```python
import random

# Game đoán số
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("🎯 GAME ĐOÁN SỐ (1-100)")
print(f"Bạn có {max_attempts} lần đoán!")

while attempts < max_attempts:
    try:
        guess = int(input(f"Lần {attempts + 1}: Đoán số? "))
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 CHÍNH XÁC! Số là {secret_number}")
            print(f"Bạn đoán đúng trong {attempts} lần!")
            break
        elif guess < secret_number:
            print("📈 Số cần tìm LỚN HỚN!")
        else:
            print("📉 Số cần tìm NHỎ HỚN!")
            
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Còn {remaining} lần đoán!")
        
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")
        attempts -= 1  # Không tính lần nhập sai

else:
    print(f"💀 HẾT LƯỢT! Số đúng là {secret_number}")
```

### 5.2. Rock Paper Scissors
```python
import random

# Game Kéo Búa Bao
choices = ['kéo', 'búa', 'bao']
player_score = 0
computer_score = 0

print("🎮 GAME KÉO BÚA BAO")
print("Chơi đến khi ai đó đạt 3 điểm!")

while player_score < 3 and computer_score < 3:
    print(f"\nTỷ số: Bạn {player_score} - {computer_score} Máy")
    print("Lựa chọn: kéo, búa, bao (hoặc 'quit' để thoát)")
    
    player_choice = input("Bạn chọn: ").lower()
    
    if player_choice == 'quit':
        break
    
    if player_choice not in choices:
        print("❌ Lựa chọn không hợp lệ!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Máy chọn: {computer_choice}")
    
    if player_choice == computer_choice:
        print("🤝 HÒA!")
    elif (player_choice == 'kéo' and computer_choice == 'bao') or \
         (player_choice == 'búa' and computer_choice == 'kéo') or \
         (player_choice == 'bao' and computer_choice == 'búa'):
        print("🎉 BẠN THẮNG!")
        player_score += 1
    else:
        print("💻 MÁY THẮNG!")
        computer_score += 1

# Kết quả cuối game
if player_score == 3:
    print("🏆 BẠN CHIẾN THẮNG!")
elif computer_score == 3:
    print("🤖 MÁY CHIẾN THẮNG!")
else:
    print("👋 Cảm ơn bạn đã chơi!")
```

---

## 📊 6. WHILE VỚI DATA PROCESSING

### 6.1. Thu Thập Và Xử Lý Nhiều Dữ Liệu
```python
# Thu thập điểm số của học sinh
scores = []
total_students = 0

print("📊 NHẬP ĐIỂM HỌC SINH")
print("Nhập 'done' để kết thúc")

while True:
    score_input = input(f"Điểm học sinh {total_students + 1}: ")
    
    if score_input.lower() == 'done':
        break
    
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            scores.append(score)
            total_students += 1
            print(f"✅ Đã thêm điểm {score}")
        else:
            print("❌ Điểm phải từ 0 đến 10!")
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")

# Xử lý dữ liệu
if scores:
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    
    print(f"\n📈 THỐNG KÊ:")
    print(f"Tổng số học sinh: {total_students}")
    print(f"Điểm trung bình: {average:.2f}")
    print(f"Điểm cao nhất: {highest}")
    print(f"Điểm thấp nhất: {lowest}")
else:
    print("Không có dữ liệu để xử lý!")
```

### 6.2. Tìm Kiếm Trong Dữ Liệu
```python
# Tìm kiếm tên trong danh sách
students = ["An", "Bình", "Chi", "Dũng", "Lan"]

print("🔍 TÌM KIẾM HỌC SINH")
print("Danh sách học sinh:", ", ".join(students))

while True:
    search_name = input("\nTìm kiếm tên (hoặc 'quit' để thoát): ").strip()
    
    if search_name.lower() == 'quit':
        break
    
    if not search_name:
        print("❌ Vui lòng nhập tên!")
        continue
    
    # Tìm kiếm không phân biệt hoa thường
    found = False
    for i, student in enumerate(students):
        if student.lower() == search_name.lower():
            print(f"✅ Tìm thấy '{student}' ở vị trí {i + 1}")
            found = True
            break
    
    if not found:
        print(f"❌ Không tìm thấy '{search_name}'")
```

---

## 🔄 7. WHILE VS FOR - KHI NÀO DÙNG GÌ?

### 7.1. Khi Nào Dùng While
```python
# ✅ Dùng while khi:
# 1. Không biết trước số lần lặp
while user_input != 'quit':
    user_input = input("Command: ")

# 2. Lặp đến khi điều kiện nào đó thỏa mãn
while not found:
    # search logic
    pass

# 3. User input validation
while True:
    try:
        age = int(input("Age: "))
        if age > 0:
            break
    except ValueError:
        print("Invalid!")
```

### 7.2. Khi Nào Dùng For
```python
# ✅ Dùng for khi:
# 1. Biết trước số lần lặp
for i in range(10):
    print(i)

# 2. Lặp qua collection
for item in my_list:
    print(item)

# 3. Tạo patterns
for i in range(5):
    print("*" * (i + 1))
```

---

## 🚫 8. LỖI THƯỜNG GẶP VỚI WHILE

### 8.1. Quên Update Counter
```python
# ❌ SAI: Infinite loop
count = 0
while count < 5:
    print(count)
    # Quên: count += 1

# ✅ ĐÚNG:
count = 0
while count < 5:
    print(count)
    count += 1  # Phải có!
```

### 8.2. Điều Kiện Sai Logic
```python
# ❌ SAI: Điều kiện không bao giờ False
x = 10
while x > 0:
    print(x)
    x += 1  # x càng lúc càng lớn, không bao giờ <= 0

# ✅ ĐÚNG:
x = 10
while x > 0:
    print(x)
    x -= 1  # Giảm x để thoát loop
```

### 8.3. Off-by-One Error
```python
# ❌ SAI: Lặp không đúng số lần
i = 1
while i <= 5:  # Muốn lặp 5 lần
    print(i)
    i += 1     # Nhưng lặp từ 1->5 (đúng 5 lần)

# Nếu muốn lặp từ 0-4:
i = 0
while i < 5:   # 0, 1, 2, 3, 4 (đúng 5 lần)
    print(i)
    i += 1
```

---

## 💡 9. TIPS VÀ BEST PRACTICES

### 9.1. Sử Dụng Flags
```python
# Flag để kiểm soát loop
running = True
error_occurred = False

while running and not error_occurred:
    try:
        # Main logic here
        user_input = input("Command: ")
        if user_input == 'quit':
            running = False
    except Exception as e:
        print(f"Error: {e}")
        error_occurred = True
```

### 9.2. Combine With Else
```python
# else chạy khi while kết thúc bình thường (không break)
count = 0
while count < 5:
    print(count)
    if count == 10:  # Không bao giờ True
        break
    count += 1
else:
    print("Loop completed normally!")
```

### 9.3. Nested While Loops
```python
# While lồng nhau - cẩn thận với logic
outer = 1
while outer <= 3:
    print(f"Outer loop: {outer}")
    
    inner = 1
    while inner <= 2:
        print(f"  Inner loop: {inner}")
        inner += 1
    
    outer += 1

# Output:
# Outer loop: 1
#   Inner loop: 1
#   Inner loop: 2
# Outer loop: 2
#   Inner loop: 1
#   Inner loop: 2
# Outer loop: 3
#   Inner loop: 1
#   Inner loop: 2
```

---

## 🏃‍♂️ 10. BÀI TẬP THỰC HÀNH

### Bài 1: Cơ Bản
```python
# 1. Viết while loop in số từ 1 đến 10
# 2. Tính tổng các số từ 1 đến 100 bằng while
# 3. In bảng cửu chương 7 bằng while
```

### Bài 2: User Input
```python
# 1. Tạo calculator đơn giản với menu while
# 2. Password validation với giới hạn 3 lần thử
# 3. Nhập và tính trung bình của n số (user định)
```

### Bài 3: Games
```python
# 1. Cải tiến game đoán số với levels khó
# 2. Simple ATM simulation
# 3. Word guessing game
```

### Bài 4: Data Processing
```python
# 1. Inventory management system
# 2. Grade calculator với multiple students
# 3. Simple banking system
```

---

## 📚 TÓM TẮT CHƯƠNG

### Key Points
1. **While loop** lặp khi điều kiện còn True
2. **Luôn phải có cách thay đổi điều kiện** để tránh infinite loop
3. **While tốt cho user input** và validation
4. **Combine với try/except** cho error handling
5. **Flags và counters** giúp kiểm soát flow

### Syntax Patterns
```python
# Basic while
while condition:
    # code
    # update condition

# With counter
count = start
while count < end:
    # code
    count += step

# Input validation
while True:
    user_input = input("...")
    if valid(user_input):
        break

# Menu system
while True:
    display_menu()
    choice = input("...")
    if choice == 'quit':
        break
    process_choice(choice)
```

### Debug Checklist
- ✅ Có cách thay đổi condition?
- ✅ Điều kiện logic đúng?
- ✅ Không có infinite loop?
- ✅ Handle exceptions properly?
- ✅ Clear exit conditions?

---

**🔥 Tiếp theo: Break, Continue và Nested Loops!** 