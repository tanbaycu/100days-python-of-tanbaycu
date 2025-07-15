"""
BÀI TẬP 3: BREAK, CONTINUE & NESTED LOOPS
=========================================

Bài tập này tập trung vào break, continue và vòng lặp lồng nhau.
Gồm 8 phần từ cơ bản đến nâng cao.

Yêu cầu:
- Hiểu rõ khi nào dùng break vs continue
- Thành thạo nested loops
- Biết cách debug complex loops
- Xây dựng patterns và algorithms

Thời gian ước tính: 100-130 phút
"""

print("🎯 BÀI TẬP 3: BREAK, CONTINUE & NESTED LOOPS")
print("=" * 50)

# =============================================================================
# PHẦN A: BREAK STATEMENT CƠ BẢN
# =============================================================================

print("\n📖 PHẦN A: BREAK STATEMENT CƠ BẢN")
print("-" * 40)

# A.1. Ví dụ: Break trong for loop
print("A.1. Ví dụ: Tìm số đầu tiên chia hết cho 7")
for i in range(1, 50):
    print(f"Kiểm tra: {i}")
    if i % 7 == 0:
        print(f"🎯 Tìm thấy: {i}")
        break  # Dừng ngay khi tìm thấy
print("Kết thúc tìm kiếm!")

# A.2. Ví dụ: Break trong while loop
print("\nA.2. Ví dụ: Nhập số đến khi gặp số âm")
count = 0
total = 0
while True:
    try:
        number = float(input(f"Nhập số thứ {count + 1}: "))
        if number < 0:
            print("🛑 Gặp số âm - Dừng nhập!")
            break
        count += 1
        total += number
        print(f"✅ Đã thêm {number}, tổng = {total}")
    except ValueError:
        print("❌ Vui lòng nhập số!")
        
if count > 0:
    print(f"📊 Kết quả: {count} số, tổng = {total}, TB = {total/count:.2f}")

# A.3. Ví dụ: Break với search
print("\nA.3. Ví dụ: Tìm kiếm trong danh sách")
students = ["An", "Bình", "Chi", "Dũng", "Lan"]
search_name = "Chi"

print(f"🔍 Tìm '{search_name}' trong {students}")
for i, student in enumerate(students):
    print(f"Kiểm tra vị trí {i}: {student}")
    if student == search_name:
        print(f"✅ Tìm thấy '{search_name}' tại vị trí {i}!")
        break
else:
    print(f"❌ Không tìm thấy '{search_name}'")

print("\n🏃‍♂️ BÀI TẬP PHẦN A:")
print("1. Tìm số nguyên tố đầu tiên > 20")
print("2. Tìm số hoàn hảo đầu tiên (1-100)")
print("3. Game đoán số với break khi đúng")
print("4. Tìm từ dài nhất trong list")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN A ---")

# Bài 1: Tìm số nguyên tố đầu tiên > 20


# Bài 2: Tìm số hoàn hảo đầu tiên


# Bài 3: Game đoán số với break


# Bài 4: Tìm từ dài nhất


# =============================================================================
# PHẦN B: CONTINUE STATEMENT CƠ BẢN
# =============================================================================

print("\n📖 PHẦN B: CONTINUE STATEMENT CƠ BẢN")
print("-" * 40)

# B.1. Ví dụ: Continue bỏ qua số chẵn
print("B.1. Ví dụ: In các số lẻ từ 1-10")
for i in range(1, 11):
    if i % 2 == 0:  # Nếu chẵn
        continue    # Bỏ qua, không in
    print(f"Số lẻ: {i}")

# B.2. Ví dụ: Continue với validation
print("\nB.2. Ví dụ: Xử lý danh sách điểm, bỏ qua điểm âm")
scores = [8.5, -1, 9.0, 7.5, -2, 6.8, 10]
valid_scores = []
total_valid = 0

for score in scores:
    if score < 0:
        print(f"⚠️ Bỏ qua điểm âm: {score}")
        continue  # Bỏ qua điểm âm
    
    valid_scores.append(score)
    total_valid += score
    print(f"✅ Điểm hợp lệ: {score}")

print(f"📊 Kết quả: {len(valid_scores)} điểm hợp lệ, TB = {total_valid/len(valid_scores):.2f}")

# B.3. Ví dụ: Continue với string processing
print("\nB.3. Ví dụ: Đếm chỉ chữ cái trong chuỗi")
text = "Hello World 123!"
letter_count = 0
digit_count = 0

for char in text:
    if char.isspace():  # Bỏ qua khoảng trắng
        continue
    elif char.isdigit():
        digit_count += 1
        continue
    elif char.isalpha():
        letter_count += 1
        print(f"Chữ cái: '{char}'")
    else:
        print(f"Ký tự đặc biệt: '{char}'")

print(f"📊 Chữ cái: {letter_count}, Số: {digit_count}")

print("\n🏃‍♂️ BÀI TẬP PHẦN B:")
print("1. In các số không chia hết cho 3 (1-30)")
print("2. Xử lý email list, bỏ qua email không hợp lệ")
print("3. Đếm nguyên âm, bỏ qua consonants")
print("4. Tính tổng số dương, bỏ qua số âm và 0")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN B ---")

# Bài 1: Số không chia hết cho 3


# Bài 2: Xử lý email list


# Bài 3: Đếm nguyên âm


# Bài 4: Tổng số dương


# =============================================================================
# PHẦN C: BREAK VS CONTINUE - SO SÁNH
# =============================================================================

print("\n📖 PHẦN C: BREAK VS CONTINUE COMPARISON")
print("-" * 40)

# C.1. Demo khác biệt break vs continue
print("C.1. Demo: Break vs Continue")

print("\n🛑 VỚI BREAK:")
for i in range(1, 6):
    if i == 3:
        print(f"BREAK tại {i} - DỪNG TOÀN BỘ LOOP")
        break
    print(f"Số: {i}")
print("Sau loop với break\n")

print("⏩ VỚI CONTINUE:")
for i in range(1, 6):
    if i == 3:
        print(f"CONTINUE tại {i} - BỎ QUA ITERATION NÀY")
        continue
    print(f"Số: {i}")
print("Sau loop với continue")

# C.2. Ví dụ: Input processing với break/continue
print("\nC.2. Ví dụ: Xử lý input commands")
commands = ["start", "invalid", "process", "stop", "end"]

for command in commands:
    print(f"\nXử lý command: '{command}'")
    
    if command == "invalid":
        print("⏩ CONTINUE: Bỏ qua command không hợp lệ")
        continue
    
    if command == "stop":
        print("🛑 BREAK: Dừng xử lý tất cả commands")
        break
    
    # Xử lý command hợp lệ
    print(f"✅ Thực thi: {command}")

print("\n🏃‍♂️ BÀI TẬP PHẦN C:")
print("1. Menu với continue cho invalid input, break cho quit")
print("2. Password attempts với continue cho wrong, break cho correct")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN C ---")

# Bài 1: Menu với continue/break


# Bài 2: Password với continue/break


# =============================================================================
# PHẦN D: NESTED LOOPS CƠ BẢN
# =============================================================================

print("\n📖 PHẦN D: NESTED LOOPS CƠ BẢN")
print("-" * 40)

# D.1. Ví dụ: Nested for loops
print("D.1. Ví dụ: Bảng nhân 2D")
for i in range(1, 4):
    print(f"\nBảng nhân {i}:")
    for j in range(1, 6):
        result = i * j
        print(f"{i} x {j} = {result:2}", end="  ")
    print()  # Xuống dòng

# D.2. Ví dụ: Matrix processing
print("\nD.2. Ví dụ: Xử lý ma trận")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Ma trận:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:3}", end="")
    print()

# Tính tổng
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print(f"Tổng tất cả phần tử: {total_sum}")

# D.3. Ví dụ: Nested while loops
print("\nD.3. Ví dụ: Nested while với coordinates")
x = 0
while x < 3:
    y = 0
    while y < 3:
        print(f"({x},{y})", end=" ")
        y += 1
    print()  # Xuống dòng
    x += 1

print("\n🏃‍♂️ BÀI TẬP PHẦN D:")
print("1. In bảng cửu chương từ 2-5")
print("2. Tạo ma trận identity 4x4")
print("3. In tọa độ của bàn cờ 8x8")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN D ---")

# Bài 1: Bảng cửu chương 2-5


# Bài 2: Ma trận identity


# Bài 3: Tọa độ bàn cờ


# =============================================================================
# PHẦN E: PATTERNS VỚI NESTED LOOPS
# =============================================================================

print("\n📖 PHẦN E: PATTERNS VỚI NESTED LOOPS")
print("-" * 40)

# E.1. Ví dụ: Tam giác số
print("E.1. Ví dụ: Tam giác số")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# E.2. Ví dụ: Tam giác sao căn giữa
print("\nE.2. Ví dụ: Tam giác sao căn giữa")
height = 5
for i in range(1, height + 1):
    # In spaces
    for j in range(height - i):
        print(" ", end="")
    # In stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# E.3. Ví dụ: Pattern chữ cái
print("\nE.3. Ví dụ: Pattern chữ cái")
for i in range(4):
    for j in range(i + 1):
        char = chr(ord('A') + j)
        print(char, end=" ")
    print()

# E.4. Ví dụ: Chessboard pattern
print("\nE.4. Ví dụ: Pattern bàn cờ")
size = 4
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

print("\n🏃‍♂️ BÀI TẬP PHẦN E:")
print("1. Tạo kim cương sao 5 tầng")
print("2. Pattern số theo dạng Pascal triangle")
print("3. Tạo pattern spiral numbers")
print("4. In bảng ASCII characters")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN E ---")

# Bài 1: Kim cương sao


# Bài 2: Pascal triangle


# Bài 3: Spiral numbers


# Bài 4: ASCII characters


# =============================================================================
# PHẦN F: BREAK/CONTINUE TRONG NESTED LOOPS
# =============================================================================

print("\n📖 PHẦN F: BREAK/CONTINUE TRONG NESTED LOOPS")
print("-" * 50)

# F.1. Ví dụ: Break chỉ inner loop
print("F.1. Ví dụ: Break inner loop")
for i in range(1, 4):
    print(f"Outer loop i={i}")
    for j in range(1, 6):
        if j == 3:
            print(f"  Break inner tại j={j}")
            break  # Chỉ thoát inner loop
        print(f"  Inner loop j={j}")
    print(f"Tiếp tục outer i={i}")

# F.2. Ví dụ: Break outer loop với flag
print("\nF.2. Ví dụ: Break outer loop với flag")
found = False
target = 15

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}")
        if product == target:
            print(f"🎯 Tìm thấy {target}!")
            found = True
            break
    if found:
        print("Thoát outer loop!")
        break

# F.3. Ví dụ: Continue trong nested
print("\nF.3. Ví dụ: Continue trong nested loops")
for i in range(1, 4):
    print(f"Row {i}:")
    for j in range(1, 6):
        if j % 2 == 0:  # Bỏ qua số chẵn
            continue
        print(f"  Column {j} (odd)")

# F.4. Ví dụ: Search trong 2D array
print("\nF.4. Ví dụ: Tìm kiếm trong ma trận")
matrix_2d = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
search_value = 9
found_position = None

for i in range(len(matrix_2d)):
    for j in range(len(matrix_2d[i])):
        print(f"Kiểm tra [{i}][{j}] = {matrix_2d[i][j]}")
        if matrix_2d[i][j] == search_value:
            found_position = (i, j)
            print(f"✅ Tìm thấy {search_value} tại ({i}, {j})")
            break
    if found_position:
        break

print("\n🏃‍♂️ BÀI TẬP PHẦN F:")
print("1. Tìm cặp số có tích = 24 trong range(1,10)")
print("2. Tìm tất cả điểm có tổng tọa độ = 5")
print("3. Matrix search với break khi tìm thấy")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN F ---")

# Bài 1: Tìm cặp số có tích = 24


# Bài 2: Điểm có tổng tọa độ = 5


# Bài 3: Matrix search


# =============================================================================
# PHẦN G: ALGORITHMS VỚI NESTED LOOPS
# =============================================================================

print("\n📖 PHẦN G: ALGORITHMS VỚI NESTED LOOPS")
print("-" * 40)

# G.1. Ví dụ: Bubble sort đơn giản
print("G.1. Ví dụ: Bubble Sort")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Mảng ban đầu: {numbers}")

n = len(numbers)
for i in range(n):
    print(f"\nLượt {i + 1}:")
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            print(f"  Swap {numbers[j+1]} và {numbers[j]}: {numbers}")
        else:
            print(f"  Không swap {numbers[j]} và {numbers[j+1]}")

print(f"Mảng đã sắp xếp: {numbers}")

# G.2. Ví dụ: Finding all pairs
print("\nG.2. Ví dụ: Tìm tất cả cặp số có tổng = 10")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
pairs = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):  # Tránh lặp lại
        if arr[i] + arr[j] == target_sum:
            pair = (arr[i], arr[j])
            pairs.append(pair)
            print(f"Tìm thấy cặp: {arr[i]} + {arr[j]} = {target_sum}")

print(f"Tất cả cặp: {pairs}")

# G.3. Ví dụ: Multiplication table generator
print("\nG.3. Ví dụ: Tạo bảng nhân hoàn chỉnh")
size = 5
print("   ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print()

for i in range(1, size + 1):
    print(f"{i:2}:", end="")
    for j in range(1, size + 1):
        print(f"{i*j:4}", end="")
    print()

print("\n🏃‍♂️ BÀI TẬP PHẦN G:")
print("1. Implement Selection Sort")
print("2. Tìm tất cả triplets có tổng = 15")
print("3. Tạo bảng truth table cho AND/OR")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN G ---")

# Bài 1: Selection Sort


# Bài 2: Triplets tổng = 15


# Bài 3: Truth table


# =============================================================================
# PHẦN H: THỰC HÀNH TỔNG HỢP
# =============================================================================

print("\n📖 PHẦN H: THỰC HÀNH TỔNG HỢP")
print("-" * 40)

# H.1. Ví dụ: Tic-tac-toe board checker
print("H.1. Ví dụ: Kiểm tra Tic-tac-toe")
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

print("Bàn cờ:")
for row in board:
    for cell in row:
        print(cell, end=" ")
    print()

# Kiểm tra hàng ngang
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != ' ':
        print(f"Thắng hàng {i}: {board[i][0]}")

# Kiểm tra cột dọc
for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] != ' ':
        print(f"Thắng cột {j}: {board[0][j]}")

# H.2. Ví dụ: Password brute force (educational)
print("\nH.2. Ví dụ: Password cracking simulation")
correct_password = "AB"
charset = "ABCD"
found = False

print(f"Thử tất cả combination 2 ký tự từ '{charset}':")
for char1 in charset:
    if found:
        break
    for char2 in charset:
        attempt = char1 + char2
        print(f"Thử: {attempt}")
        if attempt == correct_password:
            print(f"✅ Tìm thấy password: {attempt}")
            found = True
            break

print("\n🏃‍♂️ BÀI TẬP PHẦN H:")
print("1. Sudoku row/column validator")
print("2. Conway's Game of Life (1 generation)")
print("3. Matrix multiplication")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN H ---")

# Bài 1: Sudoku validator


# Bài 2: Game of Life


# Bài 3: Matrix multiplication


# =============================================================================
# TỔNG KẾT VÀ ĐÁNH GIÁ
# =============================================================================

print("\n" + "="*50)
print("🏆 TỔNG KẾT BÀI TẬP 3")
print("="*50)

print("""
KIẾN THỨC ĐÃ HỌC:
✅ Break statement và cách sử dụng
✅ Continue statement và ứng dụng
✅ So sánh break vs continue
✅ Nested loops cơ bản
✅ Patterns với nested loops
✅ Break/continue trong nested loops
✅ Algorithms với nested loops
✅ Complex problem solving

ĐIỂM ĐÁNH GIÁ BẢN THÂN:
- Phần A (Break cơ bản): ___/4
- Phần B (Continue cơ bản): ___/4
- Phần C (Break vs Continue): ___/2
- Phần D (Nested loops): ___/3
- Phần E (Patterns): ___/4
- Phần F (Break/Continue nested): ___/3
- Phần G (Algorithms): ___/3
- Phần H (Tổng hợp): ___/3

TỔNG ĐIỂM: ___/26

CHUẨN ĐÁNH GIÁ:
🥇 23-26 điểm: Xuất sắc! Master level
🥈 19-22 điểm: Giỏi! Advanced level
🥉 15-18 điểm: Khá - Intermediate level
📚 11-14 điểm: Cần ôn lại
💪 <11 điểm: Học lại từ đầu

SKILLS CHUYÊN MÔN PHÁT TRIỂN:
□ Loop control flow mastery
□ Pattern recognition & creation
□ Algorithm thinking
□ Code optimization awareness
□ Debugging complex loops
□ Problem decomposition

FEEDBACK VÀ REFLECTION:
- Concept khó nhất: ________________
- Algorithm thú vị nhất: ____________
- Pattern ấn tượng nhất: ____________
- Ứng dụng thực tế nghĩ ra: _________
- Kỹ năng cần cải thiện: ____________

NEXT LEVEL GOALS:
□ Tối ưu hóa algorithms
□ Xử lý big data với loops
□ Advanced pattern generation
□ Game development
□ Data structures implementation
""")

print("🔥 Sẵn sàng cho Bài Tập 4: Ứng Dụng Thực Tế!")

# =============================================================================
# BONUS: ADVANCED CHALLENGES (TUỲ CHỌN)
# =============================================================================

print("\n🌟 BONUS - ADVANCED CHALLENGES:")
print("Chỉ thử thách khi đã thành thạo tất cả!")
print("-" * 50)

print("1. 🧩 Fractal Patterns Generator")
print("2. 🎯 Prime Number Sieve")
print("3. 🔄 Palindrome Pyramid")
print("4. 🎲 Dice Roll Statistics")
print("5. 🏗️ ASCII Art Generator")

# Advanced challenges:
print("\n--- ADVANCED CHALLENGE CODE ---")

# Chọn 1-2 challenges để thực hiện:


print("\n🎆 CHÚC MỪNG! BẠN ĐÃ MASTER BREAK/CONTINUE & NESTED LOOPS!") 