# 📝 LÝ THUYẾT: METHODS VÀ OPERATIONS NÂNG CAO

## 🎯 MỤC TIÊU CHƯƠNG NÀY
- Thành thạo tất cả List methods quan trọng
- Hiểu rõ khi nào sử dụng method nào
- Nắm vững List comprehensions cơ bản
- Làm chủ Set operations phức tạp
- Áp dụng vào các bài toán thực tế

---

## 📚 PHẦN 1: LIST METHODS CHI TIẾT

### 🔧 1. THÊM PHẦN TỬ VÀO LIST

#### 1. **append() - Thêm một phần tử vào cuối**
```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# Append list vào list (tạo nested list)
fruits.append(["grape", "mango"])
print(fruits)  # ['apple', 'banana', 'orange', ['grape', 'mango']]
```

#### 2. **insert() - Thêm phần tử tại vị trí cụ thể**
```python
numbers = [1, 3, 5]
numbers.insert(1, 2)  # Chèn 2 vào index 1
print(numbers)  # [1, 2, 3, 5]

# Insert vào đầu list
numbers.insert(0, 0)
print(numbers)  # [0, 1, 2, 3, 5]

# Insert vào cuối (giống append)
numbers.insert(len(numbers), 6)
print(numbers)  # [0, 1, 2, 3, 5, 6]
```

#### 3. **extend() - Thêm nhiều phần tử từ iterable**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# extend() vs append()
list1.extend(list2)  # Thêm từng phần tử
print(list1)  # [1, 2, 3, 4, 5, 6]

# So sánh với append()
list3 = [1, 2, 3]
list3.append(list2)  # Thêm toàn bộ list như một phần tử
print(list3)  # [1, 2, 3, [4, 5, 6]]

# extend() với string
chars = ['a', 'b']
chars.extend("cde")
print(chars)  # ['a', 'b', 'c', 'd', 'e']
```

---

### 🗑️ 2. XÓA PHẦN TỬ KHỎI LIST

#### 1. **remove() - Xóa phần tử đầu tiên có giá trị cụ thể**
```python
fruits = ["apple", "banana", "apple", "orange"]
fruits.remove("apple")  # Xóa "apple" đầu tiên
print(fruits)  # ['banana', 'apple', 'orange']

# Lỗi nếu phần tử không tồn tại
try:
    fruits.remove("grape")
except ValueError:
    print("Không tìm thấy 'grape' trong list")
```

#### 2. **pop() - Xóa và trả về phần tử tại index**
```python
numbers = [1, 2, 3, 4, 5]

# pop() không có tham số - xóa phần tử cuối
last = numbers.pop()
print(f"Xóa: {last}, List: {numbers}")  # Xóa: 5, List: [1, 2, 3, 4]

# pop() với index
second = numbers.pop(1)
print(f"Xóa: {second}, List: {numbers}")  # Xóa: 2, List: [1, 3, 4]

# Sử dụng pop() để implement stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())  # 3
print(stack.pop())  # 2
```

#### 3. **clear() - Xóa tất cả phần tử**
```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []

# Tương đương với
numbers = [1, 2, 3, 4, 5]
numbers[:] = []
print(numbers)  # []
```

#### 4. **del statement - Xóa phần tử hoặc slice**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Xóa một phần tử
del numbers[0]
print(numbers)  # [2, 3, 4, 5, 6, 7, 8, 9]

# Xóa một slice
del numbers[1:4]
print(numbers)  # [2, 6, 7, 8, 9]

# Xóa mỗi phần tử thứ 2
del numbers[::2]
print(numbers)  # [6, 8]

# Xóa toàn bộ list
del numbers
# print(numbers)  # Lỗi! NameError
```

---

### 🔍 3. TÌM KIẾM VÀ ĐẾM

#### 1. **index() - Tìm vị trí đầu tiên của phần tử**
```python
fruits = ["apple", "banana", "orange", "banana"]

# Tìm index đầu tiên
pos = fruits.index("banana")
print(pos)  # 1

# Tìm với start và end
pos2 = fruits.index("banana", 2)  # Tìm từ index 2
print(pos2)  # 3

# Tìm trong range
try:
    pos3 = fruits.index("banana", 0, 2)  # Tìm từ 0 đến 2 (không bao gồm 2)
    print(pos3)  # 1
except ValueError:
    print("Không tìm thấy")
```

#### 2. **count() - Đếm số lần xuất hiện**
```python
numbers = [1, 2, 3, 2, 4, 2, 5]
count_2 = numbers.count(2)
print(f"Số 2 xuất hiện {count_2} lần")  # 3

# Đếm trong list phức tạp
data = [1, "hello", [1, 2], "hello", 1]
print(f"'hello' xuất hiện: {data.count('hello')} lần")  # 2
print(f"[1, 2] xuất hiện: {data.count([1, 2])} lần")   # 1
```

---

### 🔄 4. SẮP XẾP VÀ ĐẢO NGƯỢC

#### 1. **sort() - Sắp xếp list tại chỗ**
```python
# Sort số
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort ngược (descending)
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort string
fruits = ["banana", "apple", "orange", "grape"]
fruits.sort()
print(fruits)  # ['apple', 'banana', 'grape', 'orange']

# Sort theo độ dài
fruits.sort(key=len)
print(fruits)  # ['apple', 'grape', 'banana', 'orange']

# Sort phức tạp
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students.sort(key=lambda x: x[1])  # Sort theo điểm
print(students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]
```

#### 2. **sorted() - Tạo list mới đã sắp xếp**
```python
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")     # [3, 1, 4, 1, 5]
print(f"Sorted: {sorted_list}")   # [1, 1, 3, 4, 5]

# Với key function
words = ["python", "java", "go", "javascript"]
by_length = sorted(words, key=len)
print(by_length)  # ['go', 'java', 'python', 'javascript']
```

#### 3. **reverse() - Đảo ngược list tại chỗ**
```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# So sánh với slicing
original = [1, 2, 3, 4, 5]
reversed_copy = original[::-1]
print(f"Original: {original}")        # [1, 2, 3, 4, 5]
print(f"Reversed copy: {reversed_copy}")  # [5, 4, 3, 2, 1]
```

---

### 📋 5. COPY VÀ REFERENCE

#### 1. **copy() - Tạo shallow copy**
```python
original = [1, 2, [3, 4], 5]
shallow_copy = original.copy()

# Thay đổi phần tử đơn giản
shallow_copy[0] = 10
print(f"Original: {original}")      # [1, 2, [3, 4], 5]
print(f"Copy: {shallow_copy}")      # [10, 2, [3, 4], 5]

# Thay đổi nested object
shallow_copy[2][0] = 30
print(f"Original: {original}")      # [1, 2, [30, 4], 5] - Bị ảnh hưởng!
print(f"Copy: {shallow_copy}")      # [10, 2, [30, 4], 5]
```

#### 2. **Deep copy cho nested structures**
```python
import copy

original = [1, 2, [3, 4], 5]
deep_copy = copy.deepcopy(original)

# Thay đổi nested object
deep_copy[2][0] = 30
print(f"Original: {original}")      # [1, 2, [3, 4], 5] - Không bị ảnh hưởng
print(f"Deep copy: {deep_copy}")    # [1, 2, [30, 4], 5]
```

---

## 📚 PHẦN 2: LIST COMPREHENSIONS

### 🚀 1. CÚ PHÁP CƠ BẢN

#### 1. **Basic List Comprehension**
```python
# Cách truyền thống
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Với strings
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]
```

#### 2. **List Comprehension với điều kiện**
```python
# Chỉ lấy số chẵn
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Lọc và transform
words = ["apple", "banana", "orange", "grape"]
long_words = [word.upper() for word in words if len(word) > 5]
print(long_words)  # ['BANANA', 'ORANGE']

# Điều kiện phức tạp
numbers = range(-10, 11)
positive_squares = [x**2 for x in numbers if x > 0 and x % 2 == 1]
print(positive_squares)  # [1, 9, 25, 49, 81]
```

#### 3. **Nested List Comprehensions**
```python
# Tạo ma trận
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional nested
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)  # [2, 4, 6, 8]
```

---

## 📚 PHẦN 3: SET OPERATIONS NÂNG CAO

### 🔄 1. UPDATE OPERATIONS

#### 1. **update() và các variants**
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# update() - union và assign
set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5}

# intersection_update()
set1 = {1, 2, 3, 4, 5}
set1.intersection_update({3, 4, 5, 6, 7})
print(set1)  # {3, 4, 5}

# difference_update()
set1 = {1, 2, 3, 4, 5}
set1.difference_update({3, 4})
print(set1)  # {1, 2, 5}

# symmetric_difference_update()
set1 = {1, 2, 3}
set1.symmetric_difference_update({3, 4, 5})
print(set1)  # {1, 2, 4, 5}
```

### 🧮 2. COMPLEX SET OPERATIONS

#### 1. **Multiple Set Operations**
```python
# Làm việc với nhiều sets
math_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
physics_students = {"Bob", "Charlie", "Frank", "Grace"}
chemistry_students = {"Charlie", "David", "Grace", "Henry"}

# Sinh viên học cả 3 môn
all_three = math_students & physics_students & chemistry_students
print(f"Học cả 3 môn: {all_three}")  # {'Charlie'}

# Sinh viên học ít nhất 1 môn
at_least_one = math_students | physics_students | chemistry_students
print(f"Học ít nhất 1 môn: {at_least_one}")

# Sinh viên chỉ học math
only_math = math_students - physics_students - chemistry_students
print(f"Chỉ học math: {only_math}")  # {'Alice'}

# Sinh viên học đúng 2 môn
math_physics = (math_students & physics_students) - chemistry_students
math_chemistry = (math_students & chemistry_students) - physics_students
physics_chemistry = (physics_students & chemistry_students) - math_students
exactly_two = math_physics | math_chemistry | physics_chemistry
print(f"Học đúng 2 môn: {exactly_two}")
```

#### 2. **Set Comprehensions**
```python
# Basic set comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Với điều kiện
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Từ string
text = "hello world"
unique_chars = {char.upper() for char in text if char.isalpha()}
print(unique_chars)  # {'H', 'E', 'L', 'O', 'W', 'R', 'D'}

# Phức tạp hơn
words = ["apple", "banana", "orange", "grape"]
first_letters = {word[0].upper() for word in words if len(word) > 4}
print(first_letters)  # {'A', 'B', 'O', 'G'}
```

---

## 📚 PHẦN 4: TUPLE OPERATIONS NÂNG CAO

### 🔍 1. ADVANCED UNPACKING

#### 1. **Nested Tuple Unpacking**
```python
# Nested tuples
data = (("Alice", 25), ("Bob", 30), ("Charlie", 35))
(name1, age1), (name2, age2), (name3, age3) = data
print(f"{name1}: {age1}, {name2}: {age2}, {name3}: {age3}")

# Mixed unpacking
person = ("John", (25, "Engineer"), ("123 Main St", "New York"))
name, (age, job), (street, city) = person
print(f"{name}, {age}, {job}, {street}, {city}")
```

#### 2. **Advanced * unpacking**
```python
# Multiple * in unpacking
data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, *middle, last = data
print(f"First: {first}")    # 1
print(f"Middle: {middle}")  # [2, 3, 4, 5, 6, 7, 8, 9]
print(f"Last: {last}")      # 10

# Specific patterns
first, second, *rest, last = data
print(f"First: {first}, Second: {second}")  # 1, 2
print(f"Rest: {rest}")                      # [3, 4, 5, 6, 7, 8, 9]
print(f"Last: {last}")                      # 10
```

### 🔧 2. TUPLE METHODS VÀ PERFORMANCE

#### 1. **Tuple Performance Characteristics**
```python
import time

# So sánh performance: tuple vs list
def time_access(container, iterations=1000000):
    start = time.time()
    for _ in range(iterations):
        _ = container[0]
        _ = container[-1]
    return time.time() - start

# Test data
test_tuple = tuple(range(100))
test_list = list(range(100))

tuple_time = time_access(test_tuple)
list_time = time_access(test_list)

print(f"Tuple access time: {tuple_time:.4f}s")
print(f"List access time: {list_time:.4f}s")
print(f"Tuple is {list_time/tuple_time:.2f}x faster")
```

---

## 🎯 PHẦN 5: VÍ DỤ THỰC TẾ TỔNG HỢP

### 📊 1. Data Processing Pipeline
```python
# Xử lý dữ liệu sinh viên
raw_data = [
    "Alice,85,90,78",
    "Bob,92,88,95",
    "Charlie,78,85,82",
    "David,95,92,90",
    "Eve,88,86,84"
]

# Parse và xử lý dữ liệu
students = []
for line in raw_data:
    parts = line.split(',')
    name = parts[0]
    scores = [int(x) for x in parts[1:]]
    average = sum(scores) / len(scores)
    students.append((name, tuple(scores), average))

# Sort theo điểm trung bình
students.sort(key=lambda x: x[2], reverse=True)

# Phân loại học sinh
excellent = [s for s in students if s[2] >= 90]
good = [s for s in students if 80 <= s[2] < 90]
average = [s for s in students if s[2] < 80]

print("🏆 XUẤT SẮC:")
for name, scores, avg in excellent:
    print(f"  {name}: {scores} (TB: {avg:.1f})")

print("\n👍 GIỎI:")
for name, scores, avg in good:
    print(f"  {name}: {scores} (TB: {avg:.1f})")

print("\n📚 TRUNG BÌNH:")
for name, scores, avg in average:
    print(f"  {name}: {scores} (TB: {avg:.1f})")
```

### 🏪 2. Inventory Management System
```python
# Hệ thống quản lý kho
class InventoryManager:
    def __init__(self):
        self.products = {}  # product_id: (name, price, quantity, categories)
        self.categories = set()
        
    def add_product(self, product_id, name, price, quantity, categories):
        self.products[product_id] = (name, price, quantity, set(categories))
        self.categories.update(categories)
        
    def get_products_by_category(self, category):
        return [
            (pid, data[0], data[1], data[2]) 
            for pid, data in self.products.items() 
            if category in data[3]
        ]
    
    def low_stock_alert(self, threshold=5):
        return [
            (pid, data[0], data[2])
            for pid, data in self.products.items()
            if data[2] <= threshold
        ]
    
    def price_range_products(self, min_price, max_price):
        return [
            (pid, data[0], data[1])
            for pid, data in self.products.items()
            if min_price <= data[1] <= max_price
        ]
    
    def get_statistics(self):
        if not self.products:
            return {}
            
        prices = [data[1] for data in self.products.values()]
        quantities = [data[2] for data in self.products.values()]
        
        return {
            'total_products': len(self.products),
            'total_categories': len(self.categories),
            'avg_price': sum(prices) / len(prices),
            'total_inventory_value': sum(p[1] * p[2] for p in self.products.values()),
            'low_stock_count': len(self.low_stock_alert())
        }

# Sử dụng system
inventory = InventoryManager()

# Thêm sản phẩm
inventory.add_product("P001", "Laptop Dell", 999.99, 10, ["Electronics", "Computers"])
inventory.add_product("P002", "Mouse Logitech", 29.99, 50, ["Electronics", "Accessories"])
inventory.add_product("P003", "Python Book", 49.99, 3, ["Books", "Programming"])
inventory.add_product("P004", "Coffee Mug", 12.99, 25, ["Kitchen", "Accessories"])

# Truy vấn dữ liệu
print("📱 ELECTRONICS:")
for pid, name, price, qty in inventory.get_products_by_category("Electronics"):
    print(f"  {pid}: {name} - ${price} (Qty: {qty})")

print("\n⚠️ LOW STOCK ALERT:")
for pid, name, qty in inventory.low_stock_alert():
    print(f"  {pid}: {name} (Only {qty} left)")

print("\n📊 STATISTICS:")
stats = inventory.get_statistics()
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")
```

### 🎮 3. Game State Management
```python
# Quản lý trạng thái game với các data structures
class GameState:
    def __init__(self):
        self.players = {}  # player_id: (name, position, inventory, stats)
        self.active_sessions = set()
        self.game_events = []  # List of (timestamp, event_type, data)
        
    def add_player(self, player_id, name, starting_position=(0, 0)):
        self.players[player_id] = (
            name, 
            starting_position, 
            set(),  # inventory (unique items)
            {"health": 100, "score": 0, "level": 1}
        )
        self.active_sessions.add(player_id)
        self.log_event("player_joined", {"player_id": player_id, "name": name})
    
    def move_player(self, player_id, new_position):
        if player_id in self.players:
            name, old_pos, inventory, stats = self.players[player_id]
            self.players[player_id] = (name, new_position, inventory, stats)
            self.log_event("player_moved", {
                "player_id": player_id,
                "from": old_pos,
                "to": new_position
            })
    
    def add_item_to_inventory(self, player_id, item):
        if player_id in self.players:
            name, pos, inventory, stats = self.players[player_id]
            inventory.add(item)
            self.log_event("item_collected", {
                "player_id": player_id,
                "item": item
            })
    
    def get_players_in_area(self, area_bounds):
        x1, y1, x2, y2 = area_bounds
        return [
            (pid, data[0], data[1])
            for pid, data in self.players.items()
            if x1 <= data[1][0] <= x2 and y1 <= data[1][1] <= y2
        ]
    
    def get_shared_items(self, player1_id, player2_id):
        if player1_id in self.players and player2_id in self.players:
            inv1 = self.players[player1_id][2]
            inv2 = self.players[player2_id][2]
            return inv1 & inv2  # Intersection
        return set()
    
    def log_event(self, event_type, data):
        import time
        self.game_events.append((time.time(), event_type, data))
        # Keep only last 100 events
        if len(self.game_events) > 100:
            self.game_events = self.game_events[-100:]
    
    def get_leaderboard(self):
        return sorted(
            [(pid, data[0], data[3]["score"]) for pid, data in self.players.items()],
            key=lambda x: x[2],
            reverse=True
        )

# Demo game
game = GameState()

# Thêm players
game.add_player("p1", "Alice", (10, 20))
game.add_player("p2", "Bob", (15, 25))
game.add_player("p3", "Charlie", (5, 30))

# Game actions
game.add_item_to_inventory("p1", "sword")
game.add_item_to_inventory("p1", "shield")
game.add_item_to_inventory("p2", "sword")
game.add_item_to_inventory("p2", "potion")

game.move_player("p1", (12, 22))
game.move_player("p2", (18, 27))

# Queries
print("🎮 PLAYERS IN AREA (10,20,20,30):")
for pid, name, pos in game.get_players_in_area((10, 20, 20, 30)):
    print(f"  {name} at {pos}")

print("\n⚔️ SHARED ITEMS (Alice & Bob):")
shared = game.get_shared_items("p1", "p2")
print(f"  {shared}")

print("\n📊 LEADERBOARD:")
for rank, (pid, name, score) in enumerate(game.get_leaderboard(), 1):
    print(f"  {rank}. {name}: {score} points")
```

---

## 📝 TÓM TẮT KIẾN THỨC

### ✅ List Methods quan trọng:
- **Thêm**: `append()`, `insert()`, `extend()`
- **Xóa**: `remove()`, `pop()`, `clear()`, `del`
- **Tìm kiếm**: `index()`, `count()`, `in/not in`
- **Sắp xếp**: `sort()`, `sorted()`, `reverse()`
- **Copy**: `copy()`, `deepcopy()`

### ✅ List Comprehensions:
```python
# Pattern: [expression for item in iterable if condition]
result = [x**2 for x in range(10) if x % 2 == 0]
```

### ✅ Set Operations:
- **Basic**: `add()`, `remove()`, `discard()`, `update()`
- **Mathematical**: `|`, `&`, `-`, `^`
- **Relations**: `issubset()`, `issuperset()`, `isdisjoint()`

### ✅ Tuple Features:
- **Immutable** nhưng có thể chứa mutable objects
- **Unpacking** mạnh mẽ với `*` operator
- **Performance** tốt hơn lists cho read-only data

### 🎯 Best Practices:
1. **List comprehensions** cho simple operations
2. **Sets** cho unique data và fast lookup
3. **Tuples** cho immutable data và multiple returns
4. **Appropriate methods** cho từng use case

---

*💪 "Mastering methods và operations là chìa khóa để viết Python code hiệu quả và elegant!"* 