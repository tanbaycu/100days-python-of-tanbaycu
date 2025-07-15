# DICTIONARY CỞ BẢN - NGÀY 11 📚

## 🎯 MỤC TIÊU BÀI HỌC

Sau bài học này, bạn sẽ nắm vững:
- **Khái niệm Dictionary** và cách hoạt động
- **Tạo và khởi tạo Dictionary** bằng nhiều cách
- **Truy cập và cập nhật dữ liệu** hiệu quả
- **Xử lý lỗi** và edge cases
- **So sánh Dictionary** với các cấu trúc khác

---

## 📖 1. KHÁI NIỆM VÀ ĐẶC ĐIỂM

### 🔑 Dictionary là gì?

**Dictionary** (từ điển) là cấu trúc dữ liệu lưu trữ các cặp **key-value** (khóa-giá trị):

```python
# Ví dụ dictionary đơn giản
student = {
    "name": "Nguyễn Văn An",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}
```

### ✨ Đặc điểm chính

#### 1. **Key-Value Structure**
```python
# Cú pháp: {key1: value1, key2: value2, ...}
person = {
    "tên": "Minh",           # key: "tên", value: "Minh"
    "tuổi": 25,              # key: "tuổi", value: 25
    "thành_phố": "Hà Nội"    # key: "thành_phố", value: "Hà Nội"
}

print(person["tên"])         # Truy cập value qua key
# Output: Minh
```

#### 2. **Mutable (Có thể thay đổi)**
```python
student = {"name": "An", "grade": "B"}

# Thay đổi value
student["grade"] = "A"
print(student)  # {'name': 'An', 'grade': 'A'}

# Thêm key-value mới
student["age"] = 20
print(student)  # {'name': 'An', 'grade': 'A', 'age': 20}
```

#### 3. **Keys phải là Hashable**
```python
# ✅ Keys hợp lệ (hashable)
valid_dict = {
    "string": "value1",      # String
    42: "value2",            # Integer
    3.14: "value3",          # Float
    (1, 2): "value4",        # Tuple
    True: "value5"           # Boolean
}

# ❌ Keys không hợp lệ (unhashable)
try:
    invalid_dict = {
        [1, 2, 3]: "value"   # List không thể làm key
    }
except TypeError as e:
    print(f"Lỗi: {e}")
    # Output: Lỗi: unhashable type: 'list'
```

#### 4. **Ordered (Python 3.7+)**
```python
# Từ Python 3.7+, dictionary giữ thứ tự insertion
order_dict = {}
order_dict["first"] = 1
order_dict["second"] = 2
order_dict["third"] = 3

print(list(order_dict.keys()))
# Output: ['first', 'second', 'third']
```

#### 5. **Fast Lookup - O(1)**
```python
# Dictionary sử dụng hash table → truy cập nhanh
large_dict = {i: f"value_{i}" for i in range(1000000)}

# Truy cập rất nhanh dù dictionary rất lớn
value = large_dict[999999]  # O(1) average case
```

---

## 🛠️ 2. TẠO DICTIONARY

### Phương pháp 1: Literal Syntax
```python
# Cách phổ biến nhất
empty_dict = {}
student = {
    "id": "SV001",
    "name": "Trần Thị Bình",
    "major": "Computer Science",
    "gpa": 3.8
}

# Dictionary lồng nhau
company = {
    "name": "Tech Corp",
    "address": {
        "street": "123 Main St",
        "city": "Hanoi",
        "country": "Vietnam"
    },
    "employees": 150
}
```

### Phương pháp 2: Constructor dict()
```python
# Từ keyword arguments
person = dict(name="John", age=30, city="NYC")
print(person)  # {'name': 'John', 'age': 30, 'city': 'NYC'}

# Từ list of tuples
pairs = [("apple", 5), ("banana", 3), ("orange", 7)]
fruits = dict(pairs)
print(fruits)  # {'apple': 5, 'banana': 3, 'orange': 7}

# Từ zip của hai lists
keys = ["name", "age", "job"]
values = ["Alice", 28, "Engineer"]
profile = dict(zip(keys, values))
print(profile)  # {'name': 'Alice', 'age': 28, 'job': 'Engineer'}
```

### Phương pháp 3: Dictionary Comprehension
```python
# Tạo dictionary từ range
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Với điều kiện
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Từ string
char_count = {char: word.count(char) for word in ["hello"] for char in word}
print(char_count)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Phương pháp 4: Từ JSON
```python
import json

# Từ JSON string
json_string = '{"name": "David", "age": 35, "married": true}'
person = json.loads(json_string)
print(person)  # {'name': 'David', 'age': 35, 'married': True}

# Từ file JSON (simulation)
json_data = {
    "users": [
        {"id": 1, "name": "User1"},
        {"id": 2, "name": "User2"}
    ],
    "settings": {"theme": "dark", "language": "en"}
}
```

---

## 🔍 3. TRUY CẬP DỮ LIỆU

### Square Bracket Notation
```python
student = {
    "name": "Nguyễn Văn Cường",
    "age": 22,
    "grades": {"math": 9, "physics": 8.5}
}

# Truy cập direct
print(student["name"])     # Nguyễn Văn Cường
print(student["age"])      # 22

# Truy cập nested dictionary
print(student["grades"]["math"])  # 9

# ❌ KeyError nếu key không tồn tại
try:
    print(student["phone"])
except KeyError:
    print("Key 'phone' không tồn tại!")
```

### Phương thức .get()
```python
student = {"name": "An", "age": 20}

# Sử dụng .get() - an toàn hơn
name = student.get("name")          # "An"
phone = student.get("phone")        # None (không lỗi)
email = student.get("email", "N/A") # "N/A" (default value)

print(f"Name: {name}")    # Name: An
print(f"Phone: {phone}")  # Phone: None  
print(f"Email: {email}")  # Email: N/A

# So sánh với square bracket
try:
    phone_direct = student["phone"]  # KeyError!
except KeyError:
    phone_direct = "N/A"

# .get() ngắn gọn và an toàn hơn
phone_safe = student.get("phone", "N/A")
```

### Kiểm tra sự tồn tại của Key
```python
inventory = {"apple": 50, "banana": 30, "orange": 25}

# Sử dụng 'in' operator
if "apple" in inventory:
    print(f"Có {inventory['apple']} táo")

if "grape" not in inventory:
    print("Không có nho trong kho")

# Kiểm tra multiple keys
required_items = ["apple", "banana", "grape"]
missing_items = [item for item in required_items if item not in inventory]
print(f"Thiếu: {missing_items}")  # Thiếu: ['grape']

# haskey() method (deprecated, dùng 'in' instead)
# if inventory.haskey("apple"):  # ❌ Không còn sử dụng
```

---

## ✏️ 4. CẬP NHẬT DICTIONARY

### Thêm và sửa từng key
```python
student = {"name": "Lan", "age": 19}

# Thêm key mới
student["major"] = "Mathematics"
student["gpa"] = 3.7

# Sửa giá trị hiện có
student["age"] = 20

print(student)
# {'name': 'Lan', 'age': 20, 'major': 'Mathematics', 'gpa': 3.7}
```

### Phương thức .update()
```python
student = {"name": "Minh", "age": 21}

# Update với dictionary khác
additional_info = {"major": "Physics", "year": 3}
student.update(additional_info)

# Update với keyword arguments
student.update(gpa=3.5, scholarship=True)

# Update với list of tuples
new_data = [("phone", "0123456789"), ("email", "minh@email.com")]
student.update(new_data)

print(student)
# {'name': 'Minh', 'age': 21, 'major': 'Physics', 'year': 3, 
#  'gpa': 3.5, 'scholarship': True, 'phone': '0123456789', 'email': 'minh@email.com'}
```

### Merge Dictionaries (Python 3.9+)
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # 'b' trùng với dict1

# Union operator |
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update operator |=
dict1 |= dict2
print(dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Merge với conflict resolution
all_merged = dict1 | dict2 | dict3
print(all_merged)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}
# Note: dict3["b"] ghi đè dict1["b"]
```

### Conditional Updates
```python
config = {"debug": False, "port": 8000}

# Chỉ update nếu key chưa tồn tại
if "host" not in config:
    config["host"] = "localhost"

# Hoặc sử dụng setdefault (sẽ học ở bài sau)
config.setdefault("timeout", 30)

print(config)
# {'debug': False, 'port': 8000, 'host': 'localhost', 'timeout': 30}
```

---

## 🔄 5. SO SÁNH VỚI CÁC CẤU TRÚC KHÁC

### Dictionary vs List
```python
# List - truy cập bằng index (integer)
students_list = ["An", "Bình", "Cường"]
print(students_list[0])  # "An" - truy cập bằng vị trí

# Dictionary - truy cập bằng key (flexible)
students_dict = {
    "SV001": "An",
    "SV002": "Bình", 
    "SV003": "Cường"
}
print(students_dict["SV001"])  # "An" - truy cập bằng ý nghĩa

# Performance comparison
import time

# Large dataset
large_list = list(range(100000))
large_dict = {i: i for i in range(100000)}

# Tìm kiếm trong list - O(n)
start = time.time()
result = 99999 in large_list
list_time = time.time() - start

# Tìm kiếm trong dict - O(1)
start = time.time()
result = 99999 in large_dict
dict_time = time.time() - start

print(f"List search time: {list_time:.6f}s")
print(f"Dict search time: {dict_time:.6f}s")
print(f"Dict is {list_time/dict_time:.0f}x faster!")
```

### Dictionary vs Tuple
```python
# Tuple - immutable, ordered, accessed by index
person_tuple = ("John", 30, "Engineer")
name = person_tuple[0]  # Phải nhớ vị trí

# Dictionary - mutable, meaningful keys
person_dict = {"name": "John", "age": 30, "job": "Engineer"}
name = person_dict["name"]  # Tự mô tả

# Named Tuple - compromise solution
from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "job"])
person_named = Person("John", 30, "Engineer")
name = person_named.name  # Có tên field nhưng immutable
```

### Dictionary vs Set
```python
# Set - unique values, no key-value pairs
unique_ages = {20, 21, 22, 20, 21}  # {20, 21, 22}

# Dictionary - key-value mapping
age_names = {20: ["An"], 21: ["Bình", "Cường"], 22: ["Dung"]}

# Sử dụng set làm value trong dict
students_by_grade = {
    "A": {"An", "Bình"},
    "B": {"Cường", "Dung"},
    "C": {"Em"}
}
```

---

## 🎯 6. CÁC PATTERNS THƯỜNG DÙNG

### 1. Counting Pattern
```python
# Đếm frequency
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Viết ngắn gọn hơn với .get()
char_count_v2 = {}
for char in text:
    char_count_v2[char] = char_count_v2.get(char, 0) + 1
```

### 2. Grouping Pattern
```python
# Nhóm students theo grade
students = [
    {"name": "An", "grade": "A"},
    {"name": "Bình", "grade": "B"},
    {"name": "Cường", "grade": "A"},
    {"name": "Dung", "grade": "C"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])

print(grouped)
# {'A': ['An', 'Cường'], 'B': ['Bình'], 'C': ['Dung']}
```

### 3. Lookup Table Pattern
```python
# Bảng chuyển đổi
grade_points = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

def calculate_gpa(grades):
    total_points = sum(grade_points[grade] for grade in grades)
    return total_points / len(grades)

student_grades = ["A", "B", "A", "C"]
gpa = calculate_gpa(student_grades)
print(f"GPA: {gpa:.2f}")  # GPA: 3.25
```

### 4. Configuration Pattern
```python
# Cấu hình ứng dụng
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "api": {
        "rate_limit": 1000,
        "timeout": 30
    },
    "features": {
        "logging": True,
        "debug_mode": False
    }
}

# Truy cập nested config
db_host = app_config["database"]["host"]
is_debug = app_config["features"]["debug_mode"]
```

---

## ⚠️ 7. LỖI THƯỜNG GẶP VÀ CÁCH TRÁNH

### 1. KeyError
```python
# ❌ Lỗi thường gặp
student = {"name": "An", "age": 20}
try:
    phone = student["phone"]  # KeyError!
except KeyError as e:
    print(f"Lỗi: Key {e} không tồn tại")

# ✅ Cách tránh
phone = student.get("phone", "Chưa có")  # An toàn
# hoặc
if "phone" in student:
    phone = student["phone"]
else:
    phone = "Chưa có"
```

### 2. Unhashable Keys
```python
# ❌ Sử dụng list làm key
try:
    bad_dict = {[1, 2, 3]: "value"}
except TypeError:
    print("List không thể làm key!")

# ✅ Sử dụng tuple thay thế
good_dict = {(1, 2, 3): "value"}  # OK

# ✅ Chuyển list thành string
coordinates = {}
point_list = [1, 2, 3]
coordinates[str(point_list)] = "point A"  # "[1, 2, 3]" làm key
```

### 3. Modification During Iteration
```python
scores = {"An": 85, "Bình": 92, "Cường": 78}

# ❌ Không được modify dict khi đang iterate
# for name in scores:
#     if scores[name] < 80:
#         del scores[name]  # RuntimeError!

# ✅ Iterate trên copy của keys
for name in list(scores.keys()):
    if scores[name] < 80:
        del scores[name]

print(scores)  # {'Bình': 92}
```

### 4. Reference vs Copy Issues
```python
# ❌ Shallow reference
original = {"data": [1, 2, 3]}
reference = original
reference["data"].append(4)
print(original)  # {'data': [1, 2, 3, 4]} - bị thay đổi!

# ✅ Shallow copy
import copy
original = {"data": [1, 2, 3]}
shallow = original.copy()
shallow["new_key"] = "new_value"  # OK, không ảnh hưởng original
# Nhưng:
shallow["data"].append(4)  # Vẫn ảnh hưởng original!

# ✅ Deep copy cho nested structures
deep = copy.deepcopy(original)
deep["data"].append(5)  # Không ảnh hưởng original
```

---

## 🧠 8. MEMORY VÀ PERFORMANCE

### Memory Efficiency
```python
import sys

# Dictionary vs List cho lookup
data_list = list(range(1000))
data_dict = {i: i for i in range(1000)}

print(f"List memory: {sys.getsizeof(data_list)} bytes")
print(f"Dict memory: {sys.getsizeof(data_dict)} bytes")

# Dict dùng nhiều memory hơn nhưng lookup nhanh hơn
```

### Time Complexity
```python
# Dictionary operations complexity:
d = {"a": 1, "b": 2, "c": 3}

# O(1) average case:
value = d["a"]          # Get
d["d"] = 4             # Set  
del d["b"]             # Delete
result = "a" in d      # Membership test

# O(n) operations:
keys = list(d.keys())      # Get all keys
values = list(d.values())  # Get all values
items = list(d.items())    # Get all items
```

---

## 💡 9. BEST PRACTICES

### 1. Meaningful Keys
```python
# ❌ Không rõ ràng
data = {0: "John", 1: 30, 2: "Engineer"}

# ✅ Rõ ràng, self-documenting
person = {"name": "John", "age": 30, "job": "Engineer"}
```

### 2. Consistent Key Types
```python
# ❌ Mixed key types gây confusion
mixed = {"name": "John", 1: "age", True: "active"}

# ✅ Consistent key types
user = {"name": "John", "age": 30, "active": True}
```

### 3. Use .get() for Optional Values
```python
config = {"debug": True}

# ❌ Cumbersome
if "timeout" in config:
    timeout = config["timeout"]
else:
    timeout = 30

# ✅ Clean and concise
timeout = config.get("timeout", 30)
```

### 4. Document Complex Structures
```python
# ✅ Well-documented nested structure
user_profile = {
    "personal": {
        "name": str,        # Full name
        "age": int,         # Age in years
        "email": str        # Primary email
    },
    "preferences": {
        "theme": str,       # UI theme: "light" or "dark"
        "language": str,    # Language code: "en", "vi", etc.
        "notifications": bool  # Enable notifications
    },
    "stats": {
        "login_count": int,     # Total logins
        "last_login": str       # ISO datetime string
    }
}
```

---

## 🎯 TÓM TẮT

**Dictionary** là cấu trúc dữ liệu mạnh mẽ trong Python với các đặc điểm chính:

✅ **Key-Value mapping** - Truy cập dữ liệu bằng ý nghĩa thay vì vị trí  
✅ **Mutable** - Có thể thay đổi sau khi tạo  
✅ **Fast lookup** - O(1) average case performance  
✅ **Flexible keys** - Bất kỳ hashable type nào  
✅ **Ordered** - Giữ thứ tự insertion (Python 3.7+)  

**Khi nào sử dụng Dictionary:**
- Cần lookup nhanh bằng key có ý nghĩa
- Modeling real-world entities với properties
- Counting và grouping data
- Configuration management
- Caching và memoization

**Tiếp theo:** Học về các methods nâng cao và operations với Dictionary! 🚀 