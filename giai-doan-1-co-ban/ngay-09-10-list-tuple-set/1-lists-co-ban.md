# 📝 LÝ THUYẾT: LISTS CƠ BẢN - CẤU TRÚC DỮ LIỆU QUAN TRỌNG NHẤT

## 🎯 MỤC TIÊU CHƯƠNG NÀY
- Hiểu khái niệm và đặc điểm của Lists
- Nắm vững cách tạo và khởi tạo Lists
- Thành thạo indexing và slicing
- Thao tác cơ bản với Lists

---

## 📚 1. KHÁI NIỆM VÀ ĐẶC ĐIỂM LISTS

### 🔍 Lists là gì?
Lists trong Python là một **collection** (tập hợp) các items được sắp xếp theo thứ tự. Đây là cấu trúc dữ liệu quan trọng và sử dụng nhiều nhất trong Python.

### ⭐ Đặc điểm chính của Lists:

#### 1. **Mutable (Có thể thay đổi)**
```python
# Lists có thể thay đổi sau khi tạo
my_list = [1, 2, 3]
my_list[0] = 10  # Thay đổi phần tử đầu tiên
print(my_list)   # [10, 2, 3]
```

#### 2. **Ordered (Có thứ tự)**
```python
# Thứ tự các phần tử được duy trì
list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(list1 == list2)  # False - thứ tự khác nhau
```

#### 3. **Allow Duplicates (Cho phép trùng lặp)**
```python
# Lists có thể chứa các phần tử giống nhau
numbers = [1, 2, 2, 3, 2, 4]
print(numbers)  # [1, 2, 2, 3, 2, 4]
```

#### 4. **Heterogeneous (Đa dạng kiểu dữ liệu)**
```python
# Lists có thể chứa nhiều kiểu dữ liệu khác nhau
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(mixed_list)
```

---

## 🛠️ 2. TẠO VÀ KHỞI TẠO LISTS

### 📝 Các cách tạo Lists:

#### 1. **Empty List (List rỗng)**
```python
# Cách 1: Sử dụng square brackets
empty_list1 = []

# Cách 2: Sử dụng list() constructor
empty_list2 = list()

print(type(empty_list1))  # <class 'list'>
```

#### 2. **List với phần tử**
```python
# List số nguyên
numbers = [1, 2, 3, 4, 5]

# List strings
fruits = ["apple", "banana", "orange"]

# List boolean
flags = [True, False, True]

# List mixed
mixed = [1, "hello", 3.14, True]
```

#### 3. **Tạo từ range()**
```python
# Tạo list từ range
numbers = list(range(10))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
odds = list(range(1, 10, 2))   # [1, 3, 5, 7, 9]
```

#### 4. **List Repetition**
```python
# Lặp lại phần tử
zeros = [0] * 5        # [0, 0, 0, 0, 0]
hellos = ["hello"] * 3 # ["hello", "hello", "hello"]
```

#### 5. **Nested Lists (Lists lồng nhau)**
```python
# 2D List (Matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Mixed nested
complex_list = [1, [2, 3], ["a", "b"], [True, False]]
```

---

## 🔍 3. INDEXING - TRUY CẬP PHẦN TỬ

### 📍 Positive Indexing (Index dương)
```python
fruits = ["apple", "banana", "orange", "grape"]

# Truy cập từng phần tử
print(fruits[0])   # "apple"   - phần tử đầu tiên
print(fruits[1])   # "banana"  - phần tử thứ hai
print(fruits[2])   # "orange"  - phần tử thứ ba
print(fruits[3])   # "grape"   - phần tử thứ tư

# Index bắt đầu từ 0!
```

### 📍 Negative Indexing (Index âm)
```python
fruits = ["apple", "banana", "orange", "grape"]

# Truy cập từ cuối về đầu
print(fruits[-1])  # "grape"   - phần tử cuối cùng
print(fruits[-2])  # "orange"  - phần tử áp cuối
print(fruits[-3])  # "banana"  - phần tử thứ ba từ cuối
print(fruits[-4])  # "apple"   - phần tử đầu tiên

# Negative index bắt đầu từ -1!
```

### 🎯 Ví dụ thực tế:
```python
scores = [85, 92, 78, 96, 88]

# Lấy điểm cao nhất (cuối cùng sau khi sort)
scores.sort()
highest = scores[-1]  # 96

# Lấy điểm thấp nhất
lowest = scores[0]    # 78

print(f"Cao nhất: {highest}, Thấp nhất: {lowest}")
```

---

## ✂️ 4. SLICING - CẮT LIST

### 📐 Cú pháp Slicing:
```python
list[start:stop:step]
```
- **start**: Index bắt đầu (bao gồm)
- **stop**: Index kết thúc (không bao gồm)
- **step**: Bước nhảy (mặc định = 1)

### 🔧 Các ví dụ Slicing:

#### 1. **Basic Slicing**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lấy từ index 2 đến 5 (không bao gồm 5)
print(numbers[2:5])    # [2, 3, 4]

# Lấy từ đầu đến index 4
print(numbers[:5])     # [0, 1, 2, 3, 4]

# Lấy từ index 5 đến cuối
print(numbers[5:])     # [5, 6, 7, 8, 9]

# Lấy toàn bộ list
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 2. **Step Slicing**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lấy mỗi phần tử thứ 2
print(numbers[::2])    # [0, 2, 4, 6, 8]

# Lấy mỗi phần tử thứ 3 từ index 1
print(numbers[1::3])   # [1, 4, 7]

# Lấy từ index 1 đến 8, mỗi phần tử thứ 2
print(numbers[1:8:2])  # [1, 3, 5, 7]
```

#### 3. **Reverse Slicing**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Đảo ngược toàn bộ list
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Lấy từ cuối về, mỗi phần tử thứ 2
print(numbers[::-2])   # [9, 7, 5, 3, 1]

# Đảo ngược một phần
print(numbers[7:2:-1]) # [7, 6, 5, 4, 3]
```

#### 4. **Practical Examples**
```python
# Lấy 3 phần tử đầu
first_three = numbers[:3]      # [0, 1, 2]

# Lấy 3 phần tử cuối
last_three = numbers[-3:]     # [7, 8, 9]

# Lấy phần tử ở giữa (bỏ đầu và cuối)
middle = numbers[1:-1]        # [1, 2, 3, 4, 5, 6, 7, 8]

# Tạo copy của list
list_copy = numbers[:]        # Copy toàn bộ list
```

---

## 🔎 5. MEMBERSHIP TESTING

### ✅ Kiểm tra phần tử có tồn tại không:
```python
fruits = ["apple", "banana", "orange"]

# Sử dụng 'in' operator
print("apple" in fruits)      # True
print("grape" in fruits)      # False

# Sử dụng 'not in' operator
print("grape" not in fruits)  # True
print("apple" not in fruits)  # False
```

### 🎯 Ví dụ thực tế:
```python
valid_grades = ['A', 'B', 'C', 'D', 'F']
student_grade = input("Nhập điểm của bạn: ")

if student_grade in valid_grades:
    print("Điểm hợp lệ!")
else:
    print("Điểm không hợp lệ!")
```

---

## 📏 6. LẤY THÔNG TIN VỀ LIST

### 📊 Các hàm thông tin cơ bản:
```python
numbers = [1, 3, 5, 2, 8, 1, 9]

# Độ dài của list
length = len(numbers)         # 7

# Giá trị lớn nhất
maximum = max(numbers)        # 9

# Giá trị nhỏ nhất
minimum = min(numbers)        # 1

# Tổng các phần tử
total = sum(numbers)          # 29

print(f"Độ dài: {length}")
print(f"Max: {maximum}, Min: {minimum}")
print(f"Tổng: {total}")
```

### 🔍 Tìm index của phần tử:
```python
fruits = ["apple", "banana", "orange", "banana"]

# Tìm index đầu tiên của "banana"
index = fruits.index("banana")  # 1

# Đếm số lần xuất hiện
count = fruits.count("banana")  # 2

print(f"Index của banana: {index}")
print(f"Banana xuất hiện {count} lần")
```

---

## 💡 7. THAO TÁC CƠ BẢN VỚI LISTS

### ➕ Nối Lists (Concatenation):
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Sử dụng + operator
result1 = list1 + list2       # [1, 2, 3, 4, 5, 6]

# Sử dụng += operator
list1 += list2               # list1 trở thành [1, 2, 3, 4, 5, 6]
```

### ✖️ Lặp lại Lists (Repetition):
```python
original = [1, 2]
repeated = original * 3       # [1, 2, 1, 2, 1, 2]

# Lặp và gán
original *= 2                 # original trở thành [1, 2, 1, 2]
```

### 🔄 So sánh Lists:
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2)        # True
print(list1 == list3)        # False
print(list1 < [1, 2, 4])     # True (lexicographic comparison)
```

---

## 🎯 8. VÍ DỤ THỰC TẾ TỔNG HỢP

### 📊 Quản lý điểm số học sinh:
```python
# Tạo danh sách điểm
scores = [85, 92, 78, 96, 88, 91, 84]

# Phân tích dữ liệu
total_students = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)

# Lấy top 3 điểm cao nhất
scores_copy = scores[:]  # Tạo copy để không ảnh hưởng original
scores_copy.sort(reverse=True)
top_3 = scores_copy[:3]

# Đếm số học sinh điểm A (>=90)
a_grades = 0
for score in scores:
    if score >= 90:
        a_grades += 1

# In kết quả
print(f"Tổng số học sinh: {total_students}")
print(f"Điểm cao nhất: {highest_score}")
print(f"Điểm thấp nhất: {lowest_score}")
print(f"Điểm trung bình: {average_score:.2f}")
print(f"Top 3 điểm cao nhất: {top_3}")
print(f"Số học sinh đạt điểm A: {a_grades}")
```

### 🛒 Quản lý giỏ hàng:
```python
# Giỏ hàng với tên sản phẩm
shopping_cart = ["apple", "banana", "milk", "bread"]

# Hiển thị giỏ hàng
print("Giỏ hàng hiện tại:")
for i, item in enumerate(shopping_cart, 1):
    print(f"{i}. {item}")

# Kiểm tra sản phẩm
product = input("Nhập tên sản phẩm cần kiểm tra: ")
if product in shopping_cart:
    position = shopping_cart.index(product) + 1
    print(f"{product} có trong giỏ hàng ở vị trí {position}")
else:
    print(f"{product} không có trong giỏ hàng")

# Thông tin tổng quan
print(f"Tổng số sản phẩm: {len(shopping_cart)}")
```

---

## 📝 9. TÓM TẮT KIẾN THỨC

### ✅ Điểm quan trọng cần nhớ:
1. **Lists là mutable** - có thể thay đổi sau khi tạo
2. **Index bắt đầu từ 0** - phần tử đầu tiên có index 0
3. **Negative index** - truy cập từ cuối về đầu (-1, -2, -3...)
4. **Slicing syntax**: `list[start:stop:step]`
5. **Membership testing**: sử dụng `in` và `not in`

### 🎯 Best Practices:
- Luôn kiểm tra bounds trước khi truy cập index
- Sử dụng meaningful variable names
- Tận dụng slicing thay vì loops khi có thể
- Hiểu rõ sự khác biệt giữa copy và reference

### ⚠️ Lỗi thường gặp:
- `IndexError`: Truy cập index ngoài phạm vi
- Nhầm lẫn giữa `=` (assignment) và `==` (comparison)
- Quên rằng slicing stop index không được bao gồm
- Modify list trong khi iterate

---

## 🚀 CHUẨN BỊ CHO PHẦN TIẾP THEO

Trong phần tiếp theo, chúng ta sẽ học:
- **Tuples**: Immutable sequences
- **Sets**: Unique collections
- **List Methods**: append(), remove(), sort(), etc.
- **List Comprehensions**: Cách tạo lists một cách elegant

---

*💪 "Lists là nền tảng của data manipulation trong Python. Hiểu rõ Lists sẽ giúp bạn giải quyết 80% các bài toán về cấu trúc dữ liệu!"* 