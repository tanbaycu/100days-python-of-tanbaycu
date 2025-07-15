# Lý Thuyết: Break, Continue & Nested Loops - Nâng Cao

## 🎯 Mục Tiêu Chương

Sau khi học xong chương này, bạn sẽ:
- ✅ Thành thạo break và continue statements
- ✅ Hiểu cách hoạt động của nested loops
- ✅ Biết khi nào sử dụng break/continue hiệu quả
- ✅ Xây dựng được patterns phức tạp với nested loops
- ✅ Debug được lỗi trong multi-level loops

---

## 🛑 1. BREAK STATEMENT

### 1.1. Break Là Gì?
**Break** dừng hoàn toàn vòng lặp hiện tại và chuyển control ra ngoài loop.

### 1.2. Break Trong For Loop
```python
# Tìm số đầu tiên chia hết cho 7
print("Tìm số đầu tiên chia hết cho 7:")
for i in range(1, 50):
    if i % 7 == 0:
        print(f"Tìm thấy: {i}")
        break  # Dừng loop ngay lập tức
    print(f"Kiểm tra: {i}")

# Output:
# Kiểm tra: 1
# Kiểm tra: 2
# Kiểm tra: 3
# Kiểm tra: 4
# Kiểm tra: 5
# Kiểm tra: 6
# Tìm thấy: 7
```

### 1.3. Break Trong While Loop
```python
# Menu system với break
print("🎮 SIMPLE GAME MENU")
while True:  # Infinite loop
    print("\n=== MENU ===")
    print("1. Play Game")
    print("2. View Score")
    print("3. Quit")
    
    choice = input("Choose (1-3): ")
    
    if choice == '1':
        print("🎮 Starting game...")
    elif choice == '2':
        print("📊 Your score: 100")
    elif choice == '3':
        print("👋 Goodbye!")
        break  # Thoát khỏi while loop
    else:
        print("❌ Invalid choice!")

print("Game ended.")
```

### 1.4. Break Với Search Operations
```python
# Tìm kiếm trong list
students = ["An", "Bình", "Chi", "Dũng", "Lan"]
search_name = "Chi"
found_index = -1

print(f"🔍 Tìm kiếm '{search_name}':")
for i in range(len(students)):
    print(f"Kiểm tra vị trí {i}: {students[i]}")
    if students[i] == search_name:
        found_index = i
        print(f"✅ Tìm thấy tại index {i}!")
        break
else:
    print(f"❌ Không tìm thấy '{search_name}'")

if found_index != -1:
    print(f"Kết quả: {search_name} ở vị trí {found_index}")
```

---

## ⏩ 2. CONTINUE STATEMENT

### 2.1. Continue Là Gì?
**Continue** bỏ qua phần còn lại của iteration hiện tại và chuyển đến iteration tiếp theo.

### 2.2. Continue Trong For Loop
```python
# In các số lẻ từ 1 đến 10
print("Các số lẻ từ 1 đến 10:")
for i in range(1, 11):
    if i % 2 == 0:  # Nếu là số chẵn
        continue    # Bỏ qua, chuyển sang số tiếp theo
    print(f"Số lẻ: {i}")

# Output:
# Số lẻ: 1
# Số lẻ: 3
# Số lẻ: 5
# Số lẻ: 7
# Số lẻ: 9
```

### 2.3. Continue Trong While Loop
```python
# Nhập và xử lý nhiều số, bỏ qua số âm
count = 0
positive_sum = 0

print("📊 NHẬP CÁC SỐ DƯƠNG (nhập 0 để kết thúc)")
while True:
    try:
        number = float(input(f"Số thứ {count + 1}: "))
        
        if number == 0:
            break  # Kết thúc chương trình
        
        if number < 0:
            print("⚠️ Bỏ qua số âm!")
            continue  # Bỏ qua số âm, không tăng count
        
        # Chỉ xử lý số dương
        count += 1
        positive_sum += number
        print(f"✅ Đã thêm số {number}")
        
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")
        continue  # Bỏ qua input không hợp lệ

print(f"\n📈 KẾT QUẢ:")
print(f"Số lượng số dương: {count}")
print(f"Tổng các số dương: {positive_sum}")
if count > 0:
    print(f"Trung bình: {positive_sum / count:.2f}")
```

### 2.4. Continue Với String Processing
```python
# Đếm chỉ các ký tự là chữ cái
text = "Hello World 123!"
letter_count = 0

print(f"Phân tích chuỗi: '{text}'")
for char in text:
    if not char.isalpha():  # Nếu không phải chữ cái
        print(f"Bỏ qua: '{char}'")
        continue
    
    letter_count += 1
    print(f"Ký tự thứ {letter_count}: '{char}'")

print(f"Tổng số chữ cái: {letter_count}")

# Output:
# Bỏ qua: ' '
# Bỏ qua: ' '
# Bỏ qua: '1'
# Bỏ qua: '2'
# Bỏ qua: '3'
# Bỏ qua: '!'
# Tổng số chữ cái: 10
```

---

## 🔄 3. BREAK VS CONTINUE - SO SÁNH

### 3.1. Khác Biệt Cơ Bản
```python
print("=== DEMO BREAK vs CONTINUE ===")

# Với BREAK
print("\n🛑 VỚI BREAK:")
for i in range(1, 6):
    if i == 3:
        print(f"Break tại {i} - DỪNG LOOP")
        break
    print(f"Số: {i}")

# Output: 1, 2, Break tại 3 - DỪNG LOOP

# Với CONTINUE  
print("\n⏩ VỚI CONTINUE:")
for i in range(1, 6):
    if i == 3:
        print(f"Continue tại {i} - BỎ QUA")
        continue
    print(f"Số: {i}")

# Output: 1, 2, Continue tại 3 - BỎ QUA, 4, 5
```

### 3.2. Khi Nào Dùng Gì?
```python
# ✅ Dùng BREAK khi:
# - Tìm thấy kết quả và muốn dừng
# - Gặp lỗi nghiêm trọng
# - User muốn thoát

# ✅ Dùng CONTINUE khi:
# - Bỏ qua dữ liệu không hợp lệ
# - Lọc dữ liệu theo điều kiện
# - Xử lý exceptions cục bộ
```

---

## 🏗️ 4. NESTED LOOPS (VÒNG LẶP LỒNG NHAU)

### 4.1. Cơ Bản Về Nested Loops
```python
# Nested for loops đơn giản
print("📊 BẢNG NHÂN:")
for i in range(1, 4):      # Outer loop
    for j in range(1, 4):  # Inner loop
        result = i * j
        print(f"{i} x {j} = {result}")
    print("---")  # Phân cách các nhóm

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ---
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ---
```

### 4.2. Tạo Patterns Với Nested Loops
```python
# Pattern tam giác sao
print("⭐ TAM GIÁC SAO:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # Xuống dòng

# Output:
# *
# **
# ***
# ****
# *****

# Pattern số
print("\n🔢 PATTERN SỐ:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
```

### 4.3. Matrix Processing
```python
# Xử lý ma trận 2D
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("🔢 MA TRẬN:")
# In ma trận
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:3}", end="")
    print()  # Xuống dòng

# Tính tổng tất cả elements
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print(f"\nTổng tất cả phần tử: {total_sum}")

# Tìm phần tử lớn nhất
max_value = matrix[0][0]
max_position = (0, 0)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_position = (i, j)

print(f"Giá trị lớn nhất: {max_value} tại vị trí {max_position}")
```

---

## 🚫🔄 5. BREAK/CONTINUE TRONG NESTED LOOPS

### 5.1. Break Trong Nested Loops
```python
# Break chỉ thoát inner loop
print("🛑 BREAK TRONG NESTED LOOPS:")
for i in range(1, 4):
    print(f"Outer loop: {i}")
    for j in range(1, 6):
        if j == 3:
            print(f"  Break inner loop tại j={j}")
            break  # Chỉ thoát inner loop
        print(f"  Inner loop: {j}")
    print(f"Tiếp tục outer loop {i}")

# Output:
# Outer loop: 1
#   Inner loop: 1
#   Inner loop: 2
#   Break inner loop tại j=3
# Tiếp tục outer loop 1
# (tương tự cho i=2, i=3)
```

### 5.2. Break Outer Loop Với Flag
```python
# Sử dụng flag để break outer loop
print("🚩 BREAK OUTER LOOP VỚI FLAG:")
found = False

for i in range(1, 4):
    for j in range(1, 6):
        print(f"Checking ({i}, {j})")
        if i == 2 and j == 3:
            print("🎯 Tìm thấy target!")
            found = True
            break  # Break inner loop
    
    if found:
        break  # Break outer loop

print("Hoàn thành tìm kiếm!")
```

### 5.3. Continue Trong Nested Loops
```python
# Continue trong nested loops
print("⏩ CONTINUE TRONG NESTED:")
for i in range(1, 4):
    print(f"Outer: {i}")
    for j in range(1, 6):
        if j % 2 == 0:  # Bỏ qua số chẵn
            continue
        print(f"  Inner (odd only): {j}")

# Output:
# Outer: 1
#   Inner (odd only): 1
#   Inner (odd only): 3
#   Inner (odd only): 5
# (tương tự cho outer 2, 3)
```

---

## 🎨 6. PATTERNS NÂNG CAO VỚI NESTED LOOPS

### 6.1. Kim Cương Sao
```python
# Tạo pattern kim cương
def print_diamond(size):
    print("💎 KIM CƯƠNG SAO:")
    
    # Nửa trên (bao gồm giữa)
    for i in range(size):
        # In spaces
        for j in range(size - i - 1):
            print(" ", end="")
        # In stars
        for k in range(2 * i + 1):
            print("*", end="")
        print()
    
    # Nửa dưới
    for i in range(size - 2, -1, -1):
        # In spaces
        for j in range(size - i - 1):
            print(" ", end="")
        # In stars
        for k in range(2 * i + 1):
            print("*", end="")
        print()

print_diamond(5)

# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
```

### 6.2. Bảng Cửu Chương Hoàn Chỉnh
```python
# Bảng cửu chương từ 1-9
print("📚 BẢNG CỬU CHƯƠNG HOÀN CHỈNH")
print("=" * 50)

for i in range(1, 10):
    print(f"\nBảng nhân {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j:2} = {result:2}", end="  ")
        if j % 5 == 0:  # Xuống dòng sau mỗi 5 phép tính
            print()
```

### 6.3. Spiral Pattern
```python
# Tạo pattern xoắn ốc số
def print_spiral(n):
    # Tạo matrix rỗng
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    
    row, col = 0, 0
    
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        
        # Calculate next position
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        # Check if need to turn
        if (next_row < 0 or next_row >= n or 
            next_col < 0 or next_col >= n or 
            matrix[next_row][next_col] != 0):
            current_dir = (current_dir + 1) % 4
            next_row = row + directions[current_dir][0]
            next_col = col + directions[current_dir][1]
        
        row, col = next_row, next_col
    
    # In matrix
    print("🌀 SPIRAL PATTERN:")
    for row in matrix:
        for num in row:
            print(f"{num:3}", end="")
        print()

print_spiral(4)

# Output:
#   1  2  3  4
#  12 13 14  5
#  11 16 15  6
#  10  9  8  7
```

---

## 🐛 7. DEBUG NESTED LOOPS

### 7.1. Common Issues
```python
# ❌ LỖI THƯỜNG GẶP: Nhầm lẫn indices
# SAI:
for i in range(3):
    for j in range(3):
        print(f"({i}, {i})")  # Sai! Dùng i thay vì j

# ĐÚNG:
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")  # Đúng!
```

### 7.2. Debug Techniques
```python
# Technique 1: Print debug info
print("🐛 DEBUG NESTED LOOPS:")
for i in range(2):
    print(f"DEBUG: Outer loop i={i}")
    for j in range(3):
        print(f"DEBUG: Inner loop j={j}")
        # Your main logic here
        result = i * j
        print(f"RESULT: {i} * {j} = {result}")

# Technique 2: Use step-by-step execution
def debug_nested_example():
    outer_count = 0
    inner_count = 0
    
    for i in range(2):
        outer_count += 1
        print(f"Outer iteration #{outer_count}, i={i}")
        
        for j in range(3):
            inner_count += 1
            print(f"  Inner iteration #{inner_count}, j={j}")
    
    print(f"Total outer: {outer_count}, Total inner: {inner_count}")

debug_nested_example()
```

---

## 💡 8. BEST PRACTICES

### 8.1. Code Organization
```python
# ✅ GOOD: Clear structure và meaningful names
def process_student_grades():
    students = ["An", "Bình", "Chi"]
    subjects = ["Toán", "Lý", "Hóa"]
    
    for student_index, student_name in enumerate(students):
        print(f"\nHọc sinh: {student_name}")
        
        total_score = 0
        for subject_index, subject_name in enumerate(subjects):
            # Simulate getting grade
            grade = 8.5 + student_index + subject_index * 0.2
            total_score += grade
            print(f"  {subject_name}: {grade:.1f}")
        
        average = total_score / len(subjects)
        print(f"  Trung bình: {average:.1f}")

# ❌ BAD: Unclear và poor naming
def bad_example():
    a = ["An", "Bình", "Chi"]
    b = ["Toán", "Lý", "Hóa"]
    
    for i in range(len(a)):
        for j in range(len(b)):
            # Hard to understand what's happening
            pass
```

### 8.2. Performance Considerations
```python
# ✅ GOOD: Efficient loop termination
def find_target_efficient(matrix, target):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                print(f"Found {target} at ({i}, {j})")
                return True  # Early termination
    return False

# ❌ BAD: Unnecessary continuing after found
def find_target_inefficient(matrix, target):
    found = False
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                found = True
                # Continues checking unnecessarily
    return found
```

---

## 🏃‍♂️ 9. BÀI TẬP THỰC HÀNH

### Bài 1: Break/Continue Cơ Bản
```python
# 1. Tìm số nguyên tố đầu tiên > 100
# 2. Tính tổng các số từ 1-100, bỏ qua số chia hết cho 3
# 3. Nhập danh sách số, dừng khi gặp số âm
```

### Bài 2: Nested Loops Patterns
```python
# 1. Tạo pattern tam giác số ngược
# 2. In bảng ASCII từ A-Z và a-z
# 3. Tạo pattern chessboard với X và O
```

### Bài 3: Real Applications
```python
# 1. Tic-tac-toe board checker
# 2. Find all pairs that sum to target
# 3. Password brute force simulation (educational)
```

### Bài 4: Advanced
```python
# 1. Sudoku validator
# 2. Matrix multiplication
# 3. Conway's Game of Life (1 generation)
```

---

## 📚 TÓM TẮT CHƯƠNG

### Key Points
1. **Break** dừng hoàn toàn loop hiện tại
2. **Continue** bỏ qua iteration hiện tại, tiếp tục loop
3. **Nested loops** cho phép xử lý data 2D/multi-dimensional
4. **Break/continue** chỉ ảnh hưởng inner loop trực tiếp
5. **Use flags** để break outer loops

### Common Patterns
```python
# Search và break
for item in collection:
    if condition:
        break

# Filter với continue  
for item in collection:
    if not valid(item):
        continue
    process(item)

# Nested processing
for i in range(rows):
    for j in range(cols):
        process(matrix[i][j])

# Break outer với flag
found = False
for i in range(...):
    for j in range(...):
        if condition:
            found = True
            break
    if found:
        break
```

### Best Practices
- Sử dụng meaningful variable names
- Comment complex nested logic
- Consider early termination với break
- Validate loop boundaries
- Test edge cases thoroughly

---

**🚀 Sẵn sàng cho Bài Tập Thực Hành!** 