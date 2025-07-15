# Lý Thuyết: Vòng Lặp For và Range() - Chi Tiết

## 🎯 Mục Tiêu Chương

Sau khi học xong chương này, bạn sẽ:
- ✅ Hiểu hoàn toàn về vòng lặp for
- ✅ Thành thạo function range() với tất cả tham số
- ✅ Biết cách lặp qua strings, lists, và các iterable objects
- ✅ Sử dụng for loop trong tính toán và xử lý dữ liệu

---

## 📖 1. VÒNG LẶP FOR LÀ GÌ?

### Định Nghĩa
**Vòng lặp for** là cấu trúc lặp lại code nhiều lần dựa trên một tập hợp (collection) hoặc dải số (range).

### Cú Pháp Cơ Bản
```python
for variable in sequence:
    # Code block sẽ được lặp lại
    statements
```

### Ví Dụ Đơn Giản
```python
# In số từ 0 đến 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## 🔢 2. FUNCTION RANGE() - CHI TIẾT

Range() là function quan trọng nhất khi làm việc với for loops.

### 2.1. range(stop) - Một Tham Số
```python
# range(n) tạo ra dãy số từ 0 đến n-1
for i in range(5):
    print(f"Số: {i}")

# Output: 0, 1, 2, 3, 4
```

### 2.2. range(start, stop) - Hai Tham Số  
```python
# range(start, stop) tạo ra dãy từ start đến stop-1
for i in range(3, 8):
    print(f"Số: {i}")

# Output: 3, 4, 5, 6, 7
```

### 2.3. range(start, stop, step) - Ba Tham Số
```python
# range(start, stop, step) với bước nhảy
for i in range(0, 10, 2):
    print(f"Số chẵn: {i}")

# Output: 0, 2, 4, 6, 8
```

### 2.4. Range Với Số Âm
```python
# Đếm ngược
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

---

## 📝 3. FOR LOOP VỚI STRINGS

### 3.1. Lặp Qua Từng Ký Tự
```python
name = "Python"
for char in name:
    print(f"Ký tự: {char}")

# Output: P, y, t, h, o, n
```

### 3.2. Lặp Với Index
```python
word = "Hello"
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

# Output:
# Index 0: H
# Index 1: e
# Index 2: l
# Index 3: l
# Index 4: o
```

### 3.3. Enumerate() - Cả Index Và Value
```python
text = "ABC"
for index, char in enumerate(text):
    print(f"Vị trí {index}: {char}")

# Output:
# Vị trí 0: A
# Vị trí 1: B
# Vị trí 2: C
```

---

## 📊 4. FOR LOOP VỚI LISTS

### 4.1. Lặp Qua Elements
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Tôi thích {fruit}")

# Output:
# Tôi thích apple
# Tôi thích banana
# Tôi thích orange
```

### 4.2. Lặp Với Index
```python
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"Màu {i+1}: {colors[i]}")

# Output:
# Màu 1: red
# Màu 2: green
# Màu 3: blue
```

---

## 🧮 5. FOR LOOP TRONG TÍNH TOÁN

### 5.1. Tính Tổng
```python
# Tính tổng từ 1 đến 100
total = 0
for i in range(1, 101):
    total += i
print(f"Tổng từ 1 đến 100: {total}")

# Output: Tổng từ 1 đến 100: 5050
```

### 5.2. Tính Giai Thừa
```python
# Tính 5! (5 factorial)
factorial = 1
for i in range(1, 6):
    factorial *= i
print(f"5! = {factorial}")

# Output: 5! = 120
```

### 5.3. Tìm Số Chẵn/Lẻ
```python
# Đếm số chẵn và lẻ từ 1 đến 20
even_count = 0
odd_count = 0

for i in range(1, 21):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Số chẵn: {even_count}, Số lẻ: {odd_count}")
# Output: Số chẵn: 10, Số lẻ: 10
```

---

## 🔍 6. PATTERNS VỚI FOR LOOPS

### 6.1. In Ra Patterns Số
```python
# Pattern tam giác số
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()  # Xuống dòng

# Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
```

### 6.2. Pattern Sao
```python
# Pattern tam giác sao
for i in range(1, 6):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****
```

---

## ⚡ 7. CÁC VÍ DỤ THỰC TẾ

### 7.1. Bảng Cửu Chương
```python
# In bảng cửu chương số 7
number = 7
print(f"Bảng cửu chương {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

### 7.2. Kiểm Tra Số Nguyên Tố
```python
# Kiểm tra số 17 có phải số nguyên tố không
num = 17
is_prime = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print(f"{num} là số nguyên tố")
else:
    print(f"{num} không là số nguyên tố")
```

### 7.3. Tìm Ước Số
```python
# Tìm tất cả ước số của 24
number = 24
print(f"Các ước số của {number}:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
print()  # Xuống dòng

# Output: 1 2 3 4 6 8 12 24
```

---

## 🚫 8. LỖI THƯỜNG GẶP

### 8.1. Off-by-One Error
```python
# SAI: Muốn in từ 1 đến 10
for i in range(10):  # Sai vì chỉ in từ 0 đến 9
    print(i)

# ĐÚNG:
for i in range(1, 11):  # Đúng: in từ 1 đến 10
    print(i)
```

### 8.2. Confusing range() Parameters
```python
# SAI: Hiểu sai về range()
for i in range(5, 1):  # Không có gì được in vì start > stop
    print(i)

# ĐÚNG: Phải dùng step âm
for i in range(5, 1, -1):  # In 5, 4, 3, 2
    print(i)
```

### 8.3. Modifying List While Iterating
```python
# SAI: Thay đổi list trong khi lặp
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Nguy hiểm!

# ĐÚNG: Lặp ngược hoặc tạo list mới
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
```

---

## 💡 9. TIPS VÀ TRICKS

### 9.1. Sử Dụng Else Với For
```python
# else chạy khi loop kết thúc bình thường (không break)
for i in range(5):
    if i == 10:  # Điều kiện không bao giờ đúng
        break
    print(i)
else:
    print("Loop hoàn thành!")

# Output: 0, 1, 2, 3, 4, Loop hoàn thành!
```

### 9.2. Multiple Variables
```python
# Lặp với nhiều biến
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")

# Output:
# x=1, y=2
# x=3, y=4
# x=5, y=6
```

### 9.3. Nested For Loops
```python
# Vòng lặp lồng nhau
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()  # Xuống dòng

# Output:
# (0,0) (0,1) (0,2) 
# (1,0) (1,1) (1,2) 
# (2,0) (2,1) (2,2) 
```

---

## 🏃‍♂️ 10. BÀI TẬP THỰC HÀNH

### Bài 1: Cơ Bản
```python
# 1. In số từ 10 đến 1 (đếm ngược)
# 2. In tất cả số lẻ từ 1 đến 20
# 3. Tính tổng của tất cả số từ 1 đến 50
```

### Bài 2: Trung Bình
```python
# 1. In bảng cửu chương từ 1 đến 9
# 2. Đếm có bao nhiêu ký tự 'a' trong string "banana"
# 3. Tìm số lớn nhất trong list [3, 7, 2, 9, 1, 8]
```

### Bài 3: Nâng Cao
```python
# 1. Tạo pattern kim cương bằng dấu *
# 2. Kiểm tra string có phải palindrome không (đọc xuôi = đọc ngược)
# 3. Tìm tất cả số Armstrong từ 1 đến 1000
```

---

## 📚 TÓM TẮT CHƯƠNG

### Key Points
1. **For loop** lặp qua sequences (string, list, range)
2. **range()** tạo sequences số với start, stop, step
3. **enumerate()** cho cả index và value
4. For loops tuyệt vời cho tính toán và patterns
5. Cẩn thận với off-by-one errors

### Syntax Patterns
```python
# Cơ bản
for i in range(n):
    # code

# Với start/stop
for i in range(start, stop):
    # code

# Với step
for i in range(start, stop, step):
    # code

# Với strings/lists
for item in collection:
    # code
```

### Best Practices
- Sử dụng meaningful variable names
- Comment cho nested loops phức tạp
- Test boundary conditions
- Cẩn thận với infinite loops trong while (sẽ học tiếp)

---

**🔥 Sẵn sàng cho phần tiếp theo: While Loops!** 