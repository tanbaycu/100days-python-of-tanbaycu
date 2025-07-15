# 📝 LÝ THUYẾT: TUPLES VÀ SETS - IMMUTABLE VÀ UNIQUE COLLECTIONS

## 🎯 MỤC TIÊU CHƯƠNG NÀY
- Hiểu khái niệm và đặc điểm của Tuples
- Nắm vững Tuple operations và unpacking/packing
- Làm quen với Sets và tính chất unique
- Thành thạo Set operations và mathematical operations

---

## 📚 PHẦN 1: TUPLES - IMMUTABLE SEQUENCES

### 🔍 1. TUPLES LÀ GÌ?

Tuples là một **sequence** (chuỗi) các items được sắp xếp theo thứ tự, tương tự như Lists nhưng **không thể thay đổi** (immutable) sau khi đã tạo.

### ⭐ Đặc điểm chính của Tuples:

#### 1. **Immutable (Không thể thay đổi)**
```python
# Tuple không thể thay đổi sau khi tạo
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Lỗi! TypeError

print(my_tuple)  # (1, 2, 3)
```

#### 2. **Ordered (Có thứ tự)**
```python
# Thứ tự các phần tử được duy trì
tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
print(tuple1 == tuple2)  # False - thứ tự khác nhau
```

#### 3. **Allow Duplicates (Cho phép trùng lặp)**
```python
# Tuples có thể chứa các phần tử giống nhau
numbers = (1, 2, 2, 3, 2, 4)
print(numbers)  # (1, 2, 2, 3, 2, 4)
```

#### 4. **Heterogeneous (Đa dạng kiểu dữ liệu)**
```python
# Tuples có thể chứa nhiều kiểu dữ liệu khác nhau
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])
print(mixed_tuple)
```

---

### 🛠️ 2. TẠO VÀ KHỞI TẠO TUPLES

#### 1. **Empty Tuple (Tuple rỗng)**
```python
# Cách 1: Sử dụng parentheses
empty_tuple1 = ()

# Cách 2: Sử dụng tuple() constructor
empty_tuple2 = tuple()

print(type(empty_tuple1))  # <class 'tuple'>
```

#### 2. **Tuple với phần tử**
```python
# Tuple với nhiều phần tử
coordinates = (10, 20)
rgb_color = (255, 128, 0)
student_info = ("Alice", 20, "Computer Science")

# Tuple với một phần tử (chú ý dấu phẩy)
single_tuple = (42,)  # Cần dấu phẩy!
not_tuple = (42)      # Đây chỉ là số trong ngoặc
print(type(single_tuple))  # <class 'tuple'>
print(type(not_tuple))     # <class 'int'>
```

#### 3. **Tạo từ Lists hoặc Strings**
```python
# Từ list
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)  # (1, 2, 3, 4)

# Từ string
text_tuple = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# Từ range
range_tuple = tuple(range(5))  # (0, 1, 2, 3, 4)
```

#### 4. **Nested Tuples**
```python
# Tuple lồng nhau
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
complex_tuple = (1, (2, 3), ("a", "b"), (True, False))
```

---

### 🔍 3. TRUY CẬP VÀ SLICING TUPLES

#### 1. **Indexing**
```python
point = (10, 20, 30)

# Positive indexing
x = point[0]   # 10
y = point[1]   # 20
z = point[2]   # 30

# Negative indexing
last = point[-1]   # 30
second_last = point[-2]  # 20
```

#### 2. **Slicing**
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
first_three = numbers[:3]      # (0, 1, 2)
middle = numbers[3:7]          # (3, 4, 5, 6)
last_three = numbers[-3:]     # (7, 8, 9)

# Step slicing
evens = numbers[::2]           # (0, 2, 4, 6, 8)
reverse = numbers[::-1]        # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

---

### 📦 4. TUPLE UNPACKING VÀ PACKING

#### 1. **Tuple Packing**
```python
# Tự động tạo tuple từ nhiều giá trị
coordinates = 10, 20, 30  # Tạo tuple (10, 20, 30)
print(coordinates)        # (10, 20, 30)
```

#### 2. **Tuple Unpacking**
```python
# Gán từng phần tử của tuple cho các biến
point = (10, 20, 30)
x, y, z = point  # x=10, y=20, z=30

# Ví dụ thực tế
student = ("Alice", 20, "Computer Science")
name, age, major = student
print(f"{name} is {age} years old, majoring in {major}")
```

#### 3. **Partial Unpacking với ***
```python
# Unpacking một phần với *
numbers = (1, 2, 3, 4, 5, 6)

# Lấy first, last và middle
first, *middle, last = numbers
print(f"First: {first}")      # First: 1
print(f"Middle: {middle}")    # Middle: [2, 3, 4, 5]
print(f"Last: {last}")        # Last: 6

# Lấy first và rest
first, *rest = numbers
print(f"First: {first}")      # First: 1
print(f"Rest: {rest}")        # Rest: [2, 3, 4, 5, 6]
```

#### 4. **Multiple Assignment**
```python
# Hoán đổi giá trị
a = 10
b = 20
a, b = b, a  # Hoán đổi qua tuple
print(f"a={a}, b={b}")  # a=20, b=10

# Return multiple values từ function
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
```

---

### 🔧 5. TUPLE METHODS VÀ OPERATIONS

#### 1. **Tuple Methods**
```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - đếm số lần xuất hiện
count_2 = numbers.count(2)  # 3

# index() - tìm index đầu tiên
index_3 = numbers.index(3)  # 2

# index() với start và end
index_2_after_3 = numbers.index(2, 3)  # 5 (tìm 2 từ index 3)

print(f"Số 2 xuất hiện {count_2} lần")
print(f"Số 3 ở index {index_3}")
```

#### 2. **Tuple Operations**
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership testing
print(2 in tuple1)     # True
print(7 not in tuple1) # True

# Length
length = len(tuple1)   # 3
```

---

### 🎯 6. KHI NÀO SỬ DỤNG TUPLES?

#### 1. **Coordinates và Points**
```python
# 2D point
point_2d = (10, 20)

# 3D point
point_3d = (10, 20, 30)

# RGB color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
```

#### 2. **Database Records**
```python
# Student record
student = ("Alice", 25, "Computer Science", 3.8)

# Product record
product = ("Laptop", "Dell XPS 13", 999.99, True)  # name, model, price, in_stock
```

#### 3. **Configuration Settings**
```python
# Window size
window_size = (800, 600)

# Database connection
db_config = ("localhost", 5432, "mydb", "user", "password")
```

#### 4. **Return Multiple Values**
```python
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average  # Return tuple

# Usage
stats = calculate_stats([1, 2, 3, 4, 5])
total, count, avg = stats
```

---

## 📚 PHẦN 2: SETS - UNIQUE COLLECTIONS

### 🔍 1. SETS LÀ GÌ?

Sets là một **collection** các phần tử **unique** (không trùng lặp) và **unordered** (không có thứ tự cố định).

### ⭐ Đặc điểm chính của Sets:

#### 1. **Unique Elements (Phần tử duy nhất)**
```python
# Sets tự động loại bỏ duplicates
my_set = {1, 2, 2, 3, 3, 4}
print(my_set)  # {1, 2, 3, 4}
```

#### 2. **Unordered (Không có thứ tự)**
```python
# Sets không có index
my_set = {3, 1, 4, 2}
print(my_set)  # Có thể in: {1, 2, 3, 4} hoặc thứ tự khác
# print(my_set[0])  # Lỗi! Sets không có indexing
```

#### 3. **Mutable (Có thể thay đổi)**
```python
# Có thể thêm/xóa phần tử
my_set = {1, 2, 3}
my_set.add(4)     # Thêm phần tử
my_set.remove(1)  # Xóa phần tử
print(my_set)     # {2, 3, 4}
```

#### 4. **Fast Membership Testing**
```python
# Kiểm tra membership rất nhanh trong sets
large_set = set(range(1000000))
print(999999 in large_set)  # Rất nhanh!
```

---

### 🛠️ 2. TẠO VÀ KHỞI TẠO SETS

#### 1. **Empty Set**
```python
# Chú ý: {} tạo dictionary, không phải set!
empty_set = set()  # Cách duy nhất tạo empty set
print(type(empty_set))  # <class 'set'>

# {} tạo dictionary
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>
```

#### 2. **Set với phần tử**
```python
# Từ literals
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
mixed = {1, "hello", 3.14, True}
```

#### 3. **Tạo từ Iterables**
```python
# Từ list
my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list)  # {1, 2, 3, 4}

# Từ string
char_set = set("hello")    # {'h', 'e', 'l', 'o'}

# Từ tuple
tuple_set = set((1, 2, 3, 2))  # {1, 2, 3}

# Từ range
range_set = set(range(5))  # {0, 1, 2, 3, 4}
```

---

### 🔧 3. SET METHODS VÀ OPERATIONS

#### 1. **Thêm và Xóa phần tử**
```python
my_set = {1, 2, 3}

# add() - thêm một phần tử
my_set.add(4)        # {1, 2, 3, 4}
my_set.add(2)        # {1, 2, 3, 4} (2 đã có, không thêm)

# update() - thêm nhiều phần tử
my_set.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}
my_set.update("abc")      # Thêm 'a', 'b', 'c'

# remove() - xóa phần tử (raise error nếu không tồn tại)
my_set.remove(1)     # Xóa 1
# my_set.remove(10)  # Lỗi! KeyError

# discard() - xóa phần tử (không error nếu không tồn tại)
my_set.discard(10)   # Không lỗi, không làm gì

# pop() - xóa và return phần tử ngẫu nhiên
removed = my_set.pop()

# clear() - xóa tất cả phần tử
my_set.clear()       # set()
```

#### 2. **Set Information**
```python
my_set = {1, 2, 3, 4, 5}

# Length
length = len(my_set)  # 5

# Membership testing
print(3 in my_set)    # True
print(10 not in my_set)  # True

# Copy
set_copy = my_set.copy()
```

---

### 🧮 4. MATHEMATICAL SET OPERATIONS

#### 1. **Union (Hợp) - |**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union - tất cả phần tử từ cả hai sets
union1 = set1 | set2           # {1, 2, 3, 4, 5}
union2 = set1.union(set2)      # {1, 2, 3, 4, 5}

# Union nhiều sets
set3 = {5, 6, 7}
union_all = set1 | set2 | set3  # {1, 2, 3, 4, 5, 6, 7}
```

#### 2. **Intersection (Giao) - &**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection - phần tử chung
intersection1 = set1 & set2              # {3, 4}
intersection2 = set1.intersection(set2)  # {3, 4}

# Intersection nhiều sets
set3 = {2, 3, 4}
common = set1 & set2 & set3  # {3, 4}
```

#### 3. **Difference (Hiệu) - -**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Difference - phần tử ở set1 nhưng không ở set2
diff1 = set1 - set2              # {1, 2}
diff2 = set1.difference(set2)    # {1, 2}

# Ngược lại
diff3 = set2 - set1              # {5, 6}
```

#### 4. **Symmetric Difference (Hiệu đối xứng) - ^**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Symmetric difference - phần tử ở một trong hai sets, không ở cả hai
sym_diff1 = set1 ^ set2                        # {1, 2, 5, 6}
sym_diff2 = set1.symmetric_difference(set2)    # {1, 2, 5, 6}
```

#### 5. **Set Relations**
```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {5, 6}

# Subset - tập con
print(set1.issubset(set2))    # True - set1 là tập con của set2
print(set1 <= set2)           # True - cú pháp ngắn gọn

# Superset - tập cha
print(set2.issuperset(set1))  # True - set2 chứa set1
print(set2 >= set1)           # True - cú pháp ngắn gọn

# Disjoint - không có phần tử chung
print(set1.isdisjoint(set3))  # True - không có phần tử chung
```

---

### 🎯 5. KHI NÀO SỬ DỤNG SETS?

#### 1. **Loại bỏ Duplicates**
```python
# Loại bỏ phần tử trùng lặp trong list
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]

# Loại bỏ ký tự trùng lặp
text = "hello world"
unique_chars = set(text)  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
```

#### 2. **Fast Membership Testing**
```python
# Kiểm tra membership nhanh
valid_ids = {101, 102, 103, 104, 105}
user_id = 103

if user_id in valid_ids:  # Rất nhanh với sets
    print("Valid user")
```

#### 3. **Mathematical Operations**
```python
# Tìm sinh viên học cả hai môn
math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "Charlie", "Eve", "Frank"}

both_subjects = math_students & physics_students  # {"Bob", "Charlie"}
math_only = math_students - physics_students      # {"Alice", "David"}
all_students = math_students | physics_students   # Tất cả sinh viên
```

#### 4. **Data Analysis**
```python
# Phân tích dữ liệu
yesterday_visitors = {"user1", "user2", "user3", "user4"}
today_visitors = {"user2", "user3", "user5", "user6"}

# Người dùng mới hôm nay
new_visitors = today_visitors - yesterday_visitors  # {"user5", "user6"}

# Người dùng quay lại
returning_visitors = today_visitors & yesterday_visitors  # {"user2", "user3"}

# Tổng số người dùng unique
total_unique = yesterday_visitors | today_visitors
```

---

## 📊 6. SO SÁNH LISTS, TUPLES, VÀ SETS

| Đặc điểm | Lists | Tuples | Sets |
|----------|-------|--------|------|
| Mutable | ✅ Yes | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes | ❌ No |
| Indexed | ✅ Yes | ✅ Yes | ❌ No |
| Duplicates | ✅ Allow | ✅ Allow | ❌ Unique |
| Syntax | `[1,2,3]` | `(1,2,3)` | `{1,2,3}` |
| Use case | General purpose | Immutable data | Unique items |

---

## 🎯 7. VÍ DỤ THỰC TẾ TỔNG HỢP

### 📊 Phân tích dữ liệu khách hàng:
```python
# Dữ liệu khách hàng
customer_data = [
    ("Alice", 25, "Premium"),
    ("Bob", 30, "Standard"),
    ("Charlie", 35, "Premium"),
    ("David", 28, "Basic"),
    ("Eve", 32, "Standard")
]

# Unpacking và phân tích
names = []
ages = []
memberships = set()

for name, age, membership in customer_data:
    names.append(name)
    ages.append(age)
    memberships.add(membership)

# Thống kê
print(f"Tổng khách hàng: {len(names)}")
print(f"Tuổi trung bình: {sum(ages)/len(ages):.1f}")
print(f"Các loại membership: {memberships}")

# Tìm khách hàng Premium
premium_customers = {name for name, age, membership in customer_data 
                    if membership == "Premium"}
print(f"Khách hàng Premium: {premium_customers}")
```

### 🎮 Game Inventory System:
```python
# Player inventory sử dụng sets cho unique items
player1_items = {"sword", "shield", "potion", "key"}
player2_items = {"bow", "arrow", "potion", "map"}

# Shared items
shared_items = player1_items & player2_items
print(f"Shared items: {shared_items}")

# All unique items
all_items = player1_items | player2_items
print(f"All unique items: {all_items}")

# Player 1 exclusive items
p1_exclusive = player1_items - player2_items
print(f"Player 1 exclusive: {p1_exclusive}")

# Trade simulation
def trade_items(p1_inventory, p2_inventory, item1, item2):
    if item1 in p1_inventory and item2 in p2_inventory:
        p1_inventory.remove(item1)
        p1_inventory.add(item2)
        p2_inventory.remove(item2)
        p2_inventory.add(item1)
        return True
    return False

# Trade sword for bow
if trade_items(player1_items, player2_items, "sword", "bow"):
    print("Trade successful!")
    print(f"Player 1 now has: {player1_items}")
    print(f"Player 2 now has: {player2_items}")
```

---

## 📝 8. TÓM TẮT KIẾN THỨC

### ✅ TUPLES:
- **Immutable sequences** - không thể thay đổi
- **Ordered và allow duplicates**
- **Perfect for**: coordinates, database records, function returns
- **Key operations**: indexing, slicing, unpacking/packing

### ✅ SETS:
- **Unique collections** - không có duplicates
- **Unordered và mutable**
- **Perfect for**: removing duplicates, membership testing, mathematical operations
- **Key operations**: union, intersection, difference

### 🎯 Khi nào sử dụng:
- **Lists**: Khi cần mutable, ordered collection
- **Tuples**: Khi cần immutable, ordered data
- **Sets**: Khi cần unique elements và fast lookup

---

## 🚀 CHUẨN BỊ CHO PHẦN TIẾP THEO

Trong phần tiếp theo, chúng ta sẽ học:
- **Advanced List Methods**: sort(), reverse(), extend(), etc.
- **List Comprehensions**: Elegant way to create lists
- **Nested Data Structures**: Complex combinations
- **Performance Considerations**: When to use what

---

*💪 "Tuples và Sets bổ sung hoàn hảo cho Lists, tạo nên bộ ba cấu trúc dữ liệu cơ bản mạnh mẽ trong Python!"* 