# DICTIONARY METHODS VÀ OPERATIONS - NGÀY 11 🔧

## 🎯 MỤC TIÊU BÀI HỌC

Sau bài học này, bạn sẽ thành thạo:
- **Essential Methods** của Dictionary
- **Iteration patterns** hiệu quả
- **Advanced techniques** với Collections module
- **Dictionary operations** và filtering
- **Performance optimization** strategies

---

## 📋 1. ESSENTIAL METHODS

### 🔑 .keys() - Lấy tất cả Keys

```python
student = {"name": "An", "age": 20, "grade": "A"}

# Lấy keys
keys = student.keys()
print(keys)         # dict_keys(['name', 'age', 'grade'])
print(type(keys))   # <class 'dict_keys'>

# Convert to list
keys_list = list(keys)
print(keys_list)    # ['name', 'age', 'grade']

# Iteration
for key in student.keys():
    print(f"Key: {key}")
    
# Check membership
if "name" in student.keys():  # Nhưng dùng 'in student' tốt hơn
    print("Name key exists")
```

### 🎯 .values() - Lấy tất cả Values

```python
scores = {"math": 95, "physics": 88, "chemistry": 92}

# Lấy values
values = scores.values()
print(values)       # dict_values([95, 88, 92])

# Convert to list
values_list = list(values)
print(values_list)  # [95, 88, 92]

# Calculations
average = sum(scores.values()) / len(scores)
print(f"Average score: {average}")  # Average score: 91.67

max_score = max(scores.values())
print(f"Highest score: {max_score}")  # Highest score: 95

# Count occurrences
high_scores = [score for score in scores.values() if score >= 90]
print(f"High scores: {high_scores}")  # High scores: [95, 92]
```

### 🔗 .items() - Lấy Key-Value Pairs

```python
person = {"name": "Bình", "age": 25, "city": "Hanoi"}

# Lấy items
items = person.items()
print(items)  # dict_items([('name', 'Bình'), ('age', 25), ('city', 'Hanoi')])

# Convert to list of tuples
items_list = list(items)
print(items_list)  # [('name', 'Bình'), ('age', 25), ('city', 'Hanoi')]

# Unpacking trong iteration
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Bình
# age: 25
# city: Hanoi

# Destructuring với enumeration
for i, (key, value) in enumerate(person.items()):
    print(f"{i+1}. {key} = {value}")
```

---

## 🗑️ 2. REMOVING METHODS

### .pop() - Xóa và trả về Value

```python
config = {"debug": True, "port": 8080, "host": "localhost"}

# Pop with key
debug_mode = config.pop("debug")
print(debug_mode)  # True
print(config)      # {'port': 8080, 'host': 'localhost'}

# Pop with default value
timeout = config.pop("timeout", 30)  # Key không tồn tại
print(timeout)     # 30
print(config)      # {'port': 8080, 'host': 'localhost'} (không thay đổi)

# Pop without default (KeyError if key doesn't exist)
try:
    missing = config.pop("missing_key")
except KeyError:
    print("Key not found!")

# Use case: Extracting specific configs
database_config = {
    "host": "localhost",
    "port": 5432,
    "database": "myapp",
    "username": "admin",
    "password": "secret123"
}

# Extract sensitive data
password = database_config.pop("password")
print("Password extracted safely")
print(database_config)  # Password không còn trong dict
```

### .popitem() - Xóa và trả về cặp Key-Value cuối

```python
shopping_cart = {
    "apple": 3,
    "banana": 2,
    "orange": 5,
    "grape": 1
}

# Pop last inserted item (Python 3.7+)
last_item = shopping_cart.popitem()
print(last_item)       # ('grape', 1)
print(shopping_cart)   # {'apple': 3, 'banana': 2, 'orange': 5}

# Use case: Undo functionality
history = {}
def add_item(cart, item, quantity):
    history[item] = cart.get(item, 0)  # Save previous value
    cart[item] = quantity

def undo_last():
    if history:
        item, prev_quantity = history.popitem()
        if prev_quantity == 0:
            shopping_cart.pop(item, None)
        else:
            shopping_cart[item] = prev_quantity

add_item(shopping_cart, "mango", 4)
print(shopping_cart)  # {'apple': 3, 'banana': 2, 'orange': 5, 'mango': 4}
undo_last()
print(shopping_cart)  # {'apple': 3, 'banana': 2, 'orange': 5}
```

### del statement và .clear()

```python
data = {"a": 1, "b": 2, "c": 3, "d": 4}

# Delete specific key
del data["b"]
print(data)  # {'a': 1, 'c': 3, 'd': 4}

# Delete multiple keys
keys_to_delete = ["a", "c"]
for key in keys_to_delete:
    if key in data:
        del data[key]
print(data)  # {'d': 4}

# Clear all items
data.clear()
print(data)  # {}

# Comparison with reassignment
data = {"x": 1, "y": 2}
original_ref = data

data.clear()          # Clears original dict
print(original_ref)   # {} - original reference affected

data = {"x": 1, "y": 2}
original_ref = data
data = {}             # Creates new dict
print(original_ref)   # {'x': 1, 'y': 2} - original unchanged
```

---

## 🛠️ 3. ADVANCED METHODS

### .setdefault() - Set if Key Doesn't Exist

```python
# Problem: Adding to nested structure
students_by_grade = {}

# ❌ Cumbersome way
grade = "A"
if grade not in students_by_grade:
    students_by_grade[grade] = []
students_by_grade[grade].append("An")

# ✅ Using setdefault
students_by_grade.setdefault("B", []).append("Bình")
students_by_grade.setdefault("A", []).append("Cường")  # Won't overwrite existing

print(students_by_grade)  # {'A': ['An', 'Cường'], 'B': ['Bình']}

# Use case: Counting with grouping
text = "hello world"
char_positions = {}

for i, char in enumerate(text):
    char_positions.setdefault(char, []).append(i)

print(char_positions)
# {'h': [0], 'e': [1], 'l': [2, 3, 9], 'o': [4, 7], ' ': [5], 'w': [6], 'r': [8], 'd': [10]}

# Configuration with defaults
app_config = {"port": 8080}
app_config.setdefault("host", "localhost")
app_config.setdefault("debug", False)
app_config.setdefault("port", 3000)  # Won't change existing port

print(app_config)  # {'port': 8080, 'host': 'localhost', 'debug': False}
```

### .copy() - Shallow Copy

```python
original = {
    "name": "John",
    "hobbies": ["reading", "swimming"],
    "address": {"city": "Hanoi", "district": "Ba Dinh"}
}

# Shallow copy
copied = original.copy()

# Modify top-level key - safe
copied["name"] = "Jane"
print(original["name"])  # "John" - unchanged

# Modify nested list - affects original!
copied["hobbies"].append("coding")
print(original["hobbies"])  # ['reading', 'swimming', 'coding'] - changed!

# Modify nested dict - affects original!
copied["address"]["city"] = "Ho Chi Minh"
print(original["address"]["city"])  # "Ho Chi Minh" - changed!

# Deep copy for complete independence
import copy
deep_copied = copy.deepcopy(original)
deep_copied["hobbies"].append("dancing")
deep_copied["address"]["district"] = "District 1"

print(original["hobbies"])              # ['reading', 'swimming', 'coding']
print(original["address"]["district"])  # "Ba Dinh"
```

---

## 🔄 4. ITERATION PATTERNS

### Basic Iteration

```python
prices = {"apple": 1.2, "banana": 0.8, "orange": 1.5}

# Iterate over keys (default)
for item in prices:
    print(f"{item}: ${prices[item]}")

# Explicit key iteration
for item in prices.keys():
    print(f"Item: {item}")

# Value iteration
for price in prices.values():
    print(f"Price: ${price}")

# Key-value iteration
for item, price in prices.items():
    print(f"{item} costs ${price}")
```

### Advanced Iteration Patterns

```python
inventory = {
    "laptop": {"price": 1000, "stock": 5},
    "mouse": {"price": 25, "stock": 50},
    "keyboard": {"price": 75, "stock": 20},
    "monitor": {"price": 300, "stock": 0}
}

# Filter iteration
print("Available items:")
for item, details in inventory.items():
    if details["stock"] > 0:
        print(f"- {item}: ${details['price']} ({details['stock']} in stock)")

# Sorting during iteration
print("\nItems by price (ascending):")
for item, details in sorted(inventory.items(), key=lambda x: x[1]["price"]):
    print(f"- {item}: ${details['price']}")

# Enumerate with items
print("\nIndexed inventory:")
for i, (item, details) in enumerate(inventory.items(), 1):
    status = "Available" if details["stock"] > 0 else "Out of stock"
    print(f"{i}. {item}: {status}")

# Parallel iteration with zip
items = list(inventory.keys())
prices = [details["price"] for details in inventory.values()]

for item, price in zip(items, prices):
    print(f"{item}: ${price}")
```

### Dictionary Comprehensions with Iteration

```python
products = {
    "laptop": 1000,
    "phone": 600,
    "tablet": 400,
    "watch": 200
}

# Filter expensive items
expensive = {item: price for item, price in products.items() if price > 500}
print(expensive)  # {'laptop': 1000, 'phone': 600}

# Apply discount
discounted = {item: price * 0.9 for item, price in products.items()}
print(discounted)  # {'laptop': 900.0, 'phone': 540.0, 'tablet': 360.0, 'watch': 180.0}

# Transform keys
uppercase_keys = {item.upper(): price for item, price in products.items()}
print(uppercase_keys)  # {'LAPTOP': 1000, 'PHONE': 600, 'TABLET': 400, 'WATCH': 200}

# Conditional transformation
categorized = {
    item: "expensive" if price > 500 else "affordable" 
    for item, price in products.items()
}
print(categorized)  # {'laptop': 'expensive', 'phone': 'expensive', 'tablet': 'affordable', 'watch': 'affordable'}
```

---

## 📊 5. COLLECTIONS MODULE

### defaultdict - Automatic Default Values

```python
from collections import defaultdict

# Regular dict problem
regular_dict = {}
# regular_dict["missing_key"].append("value")  # KeyError!

# defaultdict solution
dd = defaultdict(list)  # Default factory: list
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")

print(dd)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})

# Different default types
int_dict = defaultdict(int)      # Default: 0
set_dict = defaultdict(set)      # Default: empty set
str_dict = defaultdict(str)      # Default: empty string

# Counting example
text = "hello world"
char_count = defaultdict(int)
for char in text:
    char_count[char] += 1

print(dict(char_count))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Grouping example
students = [
    {"name": "An", "grade": "A", "subject": "Math"},
    {"name": "Bình", "grade": "B", "subject": "Math"},
    {"name": "Cường", "grade": "A", "subject": "Physics"}
]

by_grade = defaultdict(list)
for student in students:
    by_grade[student["grade"]].append(student["name"])

print(dict(by_grade))  # {'A': ['An', 'Cường'], 'B': ['Bình']}
```

### Counter - Counting Made Easy

```python
from collections import Counter

# Basic counting
text = "hello world"
char_counter = Counter(text)
print(char_counter)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Most common
print(char_counter.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]

# List counting
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_counter = Counter(fruits)
print(fruit_counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Counter arithmetic
counter1 = Counter({"a": 3, "b": 1})
counter2 = Counter({"a": 1, "b": 2, "c": 1})

print(counter1 + counter2)  # Counter({'a': 4, 'b': 3, 'c': 1})
print(counter1 - counter2)  # Counter({'a': 2})
print(counter1 & counter2)  # Counter({'a': 1, 'b': 1}) - intersection
print(counter1 | counter2)  # Counter({'a': 3, 'b': 2, 'c': 1}) - union

# Update counters
sales = Counter({"laptop": 5, "phone": 8})
sales.update({"laptop": 2, "tablet": 3})  # Add more sales
print(sales)  # Counter({'phone': 8, 'laptop': 7, 'tablet': 3})

# Practical example: Word frequency
def analyze_text(text):
    words = text.lower().split()
    word_count = Counter(words)
    
    return {
        "total_words": sum(word_count.values()),
        "unique_words": len(word_count),
        "most_common": word_count.most_common(5)
    }

sample_text = "python is great python is powerful python is easy"
analysis = analyze_text(sample_text)
print(analysis)
# {'total_words': 9, 'unique_words': 5, 'most_common': [('python', 3), ('is', 3), ('great', 1), ('powerful', 1), ('easy', 1)]}
```

### OrderedDict - Order Preservation (Legacy)

```python
from collections import OrderedDict

# Note: In Python 3.7+, regular dicts maintain order
# OrderedDict still useful for specific behaviors

# Basic usage
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3

print(ordered)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Move to end
ordered.move_to_end("first")
print(ordered)  # OrderedDict([('second', 2), ('third', 3), ('first', 1)])

# Pop from either end
ordered.popitem(last=False)  # Pop from beginning
print(ordered)  # OrderedDict([('third', 3), ('first', 1)])

# Equality comparison (order matters)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)  # True - regular dicts

ordered1 = OrderedDict([("a", 1), ("b", 2)])
ordered2 = OrderedDict([("b", 2), ("a", 1)])
print(ordered1 == ordered2)  # False - order matters
```

### ChainMap - Multiple Dictionaries

```python
from collections import ChainMap

# Combine multiple dictionaries
defaults = {"color": "blue", "size": "medium"}
user_prefs = {"color": "red"}
command_line = {"size": "large"}

# ChainMap searches in order
config = ChainMap(command_line, user_prefs, defaults)
print(config["color"])  # "red" (from user_prefs)
print(config["size"])   # "large" (from command_line)

# View all values
print(dict(config))  # {'size': 'large', 'color': 'red'}

# Add new mapping
session_prefs = {"theme": "dark"}
config = config.new_child(session_prefs)
print(config["theme"])  # "dark"

# Use case: Configuration hierarchy
system_config = {"timeout": 30, "debug": False}
user_config = {"timeout": 60}
session_config = {"debug": True}

final_config = ChainMap(session_config, user_config, system_config)
print(f"Timeout: {final_config['timeout']}")  # 60 (user override)
print(f"Debug: {final_config['debug']}")      # True (session override)
```

---

## 🔍 6. FILTERING VÀ SORTING

### Filtering Dictionaries

```python
students = {
    "An": {"grade": 85, "age": 20},
    "Bình": {"grade": 92, "age": 19},
    "Cường": {"grade": 78, "age": 21},
    "Dung": {"grade": 96, "age": 20}
}

# Filter by condition
high_performers = {
    name: info for name, info in students.items() 
    if info["grade"] >= 90
}
print(high_performers)  # {'Bình': {'grade': 92, 'age': 19}, 'Dung': {'grade': 96, 'age': 20}}

# Multiple conditions
young_high_performers = {
    name: info for name, info in students.items()
    if info["grade"] >= 85 and info["age"] <= 20
}
print(young_high_performers)  # {'An': {'grade': 85, 'age': 20}, 'Bình': {'grade': 92, 'age': 19}, 'Dung': {'grade': 96, 'age': 20}}

# Using filter() function
def is_passing(item):
    name, info = item
    return info["grade"] >= 80

passing_students = dict(filter(is_passing, students.items()))
print(passing_students)
```

### Sorting Dictionaries

```python
products = {
    "laptop": {"price": 1000, "rating": 4.5},
    "phone": {"price": 600, "rating": 4.8},
    "tablet": {"price": 400, "rating": 4.2},
    "watch": {"price": 200, "rating": 4.0}
}

# Sort by key
sorted_by_name = dict(sorted(products.items()))
print(sorted_by_name)

# Sort by price
sorted_by_price = dict(sorted(products.items(), key=lambda x: x[1]["price"]))
print("Sorted by price:", sorted_by_price)

# Sort by rating (descending)
sorted_by_rating = dict(sorted(products.items(), key=lambda x: x[1]["rating"], reverse=True))
print("Sorted by rating:", sorted_by_rating)

# Multiple criteria sorting
def sort_key(item):
    name, info = item
    return (info["rating"], -info["price"])  # Rating ascending, price descending

sorted_multi = dict(sorted(products.items(), key=sort_key, reverse=True))
print("Multi-criteria sort:", sorted_multi)

# Get top N items
top_rated = dict(sorted(products.items(), key=lambda x: x[1]["rating"], reverse=True)[:2])
print("Top 2 rated:", top_rated)
```

---

## ⚡ 7. PERFORMANCE TIPS

### Efficient Operations

```python
import time

# Large dictionary for testing
large_dict = {i: f"value_{i}" for i in range(100000)}

# ✅ Efficient membership testing
start = time.time()
result = 50000 in large_dict
fast_time = time.time() - start

# ❌ Inefficient membership testing
start = time.time()
result = 50000 in large_dict.values()
slow_time = time.time() - start

print(f"Key lookup: {fast_time:.6f}s")
print(f"Value lookup: {slow_time:.6f}s")
print(f"Key lookup is {slow_time/fast_time:.0f}x faster")

# ✅ Efficient iteration
def process_efficiently(d):
    # Direct iteration over items
    for key, value in d.items():
        if key % 2 == 0:
            # Process even keys
            pass

# ❌ Inefficient iteration
def process_inefficiently(d):
    # Accessing dict for each key
    for key in d.keys():
        value = d[key]  # Extra lookup!
        if key % 2 == 0:
            pass
```

### Memory Optimization

```python
import sys

# Regular dict
regular_dict = {f"key_{i}": i for i in range(1000)}

# Dict with __slots__ optimization (advanced)
class SlottedDict:
    __slots__ = ['data']
    
    def __init__(self, data):
        self.data = data

slotted = SlottedDict({f"key_{i}": i for i in range(1000)})

print(f"Regular dict: {sys.getsizeof(regular_dict)} bytes")
print(f"Slotted approach: {sys.getsizeof(slotted) + sys.getsizeof(slotted.data)} bytes")

# Use generators for large transformations
def transform_large_dict(d):
    # ❌ Memory intensive
    # return {k: expensive_transform(v) for k, v in d.items()}
    
    # ✅ Memory efficient generator
    for k, v in d.items():
        yield k, expensive_transform(v)

def expensive_transform(x):
    return x ** 2 + x * 10
```

---

## 🎯 8. PRACTICAL PATTERNS

### Configuration Management

```python
class Config:
    def __init__(self, **kwargs):
        self.config = {
            # Defaults
            "host": "localhost",
            "port": 8080,
            "debug": False,
            "timeout": 30
        }
        self.config.update(kwargs)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
    
    def update_from_file(self, filename):
        # Simulate loading from file
        file_config = {"port": 9000, "debug": True}
        self.config.update(file_config)

# Usage
app_config = Config(host="0.0.0.0", workers=4)
print(app_config.config)
```

### Caching Pattern

```python
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    wrapper.cache = cache  # Expose cache for inspection
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test
print(fibonacci(10))  # 55
print(fibonacci.cache)  # See cached values
```

### Data Transformation Pipeline

```python
def transform_pipeline(data, *transformations):
    """Apply multiple transformations to dictionary data"""
    result = data.copy()
    
    for transform in transformations:
        result = transform(result)
    
    return result

# Transformation functions
def add_full_name(data):
    """Add full_name field from first_name and last_name"""
    return {
        **data,
        "full_name": f"{data.get('first_name', '')} {data.get('last_name', '')}".strip()
    }

def normalize_email(data):
    """Normalize email to lowercase"""
    if "email" in data:
        data = data.copy()
        data["email"] = data["email"].lower()
    return data

def add_age_group(data):
    """Add age group based on age"""
    age = data.get("age", 0)
    group = "child" if age < 18 else "adult" if age < 65 else "senior"
    return {**data, "age_group": group}

# Usage
user_data = {
    "first_name": "Nguyen",
    "last_name": "Van A",
    "email": "NGUYEN.A@EMAIL.COM",
    "age": 25
}

processed = transform_pipeline(
    user_data,
    add_full_name,
    normalize_email,
    add_age_group
)

print(processed)
# {'first_name': 'Nguyen', 'last_name': 'Van A', 'email': 'nguyen.a@email.com', 
#  'age': 25, 'full_name': 'Nguyen Van A', 'age_group': 'adult'}
```

---

## 🎯 TÓM TẮT

**Dictionary Methods và Operations** cung cấp powerful tools để:

✅ **Truy xuất dữ liệu**: `.keys()`, `.values()`, `.items()`  
✅ **Quản lý entries**: `.pop()`, `.popitem()`, `.clear()`  
✅ **Safe operations**: `.get()`, `.setdefault()`  
✅ **Collections support**: `defaultdict`, `Counter`, `ChainMap`  
✅ **Advanced patterns**: Filtering, sorting, caching  

**Key Takeaways:**
- Sử dụng `.get()` thay vì direct access để tránh KeyError
- `defaultdict` và `Counter` giải quyết nhiều use cases phổ biến
- Dictionary comprehensions mạnh mẽ cho filtering và transformation
- Performance matters: key lookup là O(1), value lookup là O(n)

**Tiếp theo:** Nested dictionaries và advanced applications! 🚀 