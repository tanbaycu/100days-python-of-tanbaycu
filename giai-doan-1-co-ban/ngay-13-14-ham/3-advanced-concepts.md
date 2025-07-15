# Lý Thuyết 3: Advanced Concepts - Kiến Trúc Hàm Nâng Cao

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Nắm vững khái niệm Scope và LEGB Rule
- Sử dụng thành thạo Lambda functions
- Hiểu và áp dụng Higher-order functions
- Làm việc với Decorators và Closures
- Sử dụng Generators và Iterators
- Thành thạo Recursion và các thuật toán đệ quy

## 1. Scope và LEGB Rule

### 1.1 Các Loại Scope

#### Local Scope
```python
def function_test():
    x = 10  # Local variable
    print(f"Trong function: {x}")

function_test()
# print(x)  # NameError: name 'x' is not defined
```

#### Enclosing Scope
```python
def outer_function():
    x = 20  # Enclosing scope
    
    def inner_function():
        print(f"Trong inner function: {x}")  # Truy cập enclosing scope
    
    inner_function()
    return inner_function

func = outer_function()
func()  # Vẫn có thể truy cập x = 20
```

#### Global Scope
```python
x = 30  # Global variable

def test_global():
    print(f"Global x: {x}")

def modify_global():
    global x
    x = 40
    print(f"Modified global x: {x}")

test_global()     # Global x: 30
modify_global()   # Modified global x: 40
test_global()     # Global x: 40
```

#### Built-in Scope
```python
# Built-in functions như len, print, type luôn có sẵn
def test_builtin():
    print(len([1, 2, 3]))  # len là built-in function
    print(type("hello"))   # type là built-in function

test_builtin()
```

### 1.2 LEGB Rule
Python tìm kiếm biến theo thứ tự: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"Inner function: {x}")  # local
    
    inner()
    print(f"Outer function: {x}")     # enclosing

outer()
print(f"Global: {x}")                 # global
```

### 1.3 Nonlocal Keyword
```python
def outer():
    count = 0
    
    def increment():
        nonlocal count  # Thay đổi biến enclosing scope
        count += 1
        return count
    
    return increment

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## 2. Lambda Functions

### 2.1 Cú Pháp Lambda
```python
# Cú pháp: lambda arguments: expression

# Function thường
def binh_phuong(x):
    return x ** 2

# Lambda function
binh_phuong_lambda = lambda x: x ** 2

print(binh_phuong(5))        # 25
print(binh_phuong_lambda(5)) # 25
```

### 2.2 Lambda Với Nhiều Tham Số
```python
# Cộng hai số
cong = lambda x, y: x + y
print(cong(10, 20))  # 30

# Tính diện tích hình chữ nhật
dien_tich = lambda dai, rong: dai * rong
print(dien_tich(5, 3))  # 15

# Tìm số lớn nhất trong ba số
max_ba_so = lambda a, b, c: max(a, max(b, c))
print(max_ba_so(10, 20, 15))  # 20
```

### 2.3 Lambda Với Conditional Expression
```python
# Tìm giá trị tuyệt đối
abs_value = lambda x: x if x >= 0 else -x
print(abs_value(-5))   # 5
print(abs_value(3))    # 3

# Phân loại tuổi
phan_loai_tuoi = lambda tuoi: "Trẻ em" if tuoi < 18 else "Người lớn"
print(phan_loai_tuoi(15))  # Trẻ em
print(phan_loai_tuoi(25))  # Người lớn

# Tính giá sau giảm giá
gia_sau_giam = lambda gia, giam_gia: gia * (1 - giam_gia/100) if giam_gia > 0 else gia
print(gia_sau_giam(100000, 10))  # 90000.0
```

## 3. Higher-Order Functions

### 3.1 Map Function
```python
# Áp dụng function cho mỗi phần tử trong iterable
so_list = [1, 2, 3, 4, 5]

# Sử dụng lambda với map
binh_phuong_list = list(map(lambda x: x**2, so_list))
print(binh_phuong_list)  # [1, 4, 9, 16, 25]

# Chuyển đổi nhiệt độ
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 86.0, 104.0]

# Xử lý chuỗi
ten_list = ["nguyễn văn an", "trần thị bình", "lê văn cường"]
ten_chuan = list(map(lambda ten: ten.title(), ten_list))
print(ten_chuan)  # ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Văn Cường']
```

### 3.2 Filter Function
```python
# Lọc phần tử thỏa mãn điều kiện
so_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc số chẵn
so_chan = list(filter(lambda x: x % 2 == 0, so_list))
print(so_chan)  # [2, 4, 6, 8, 10]

# Lọc số lớn hơn 5
so_lon = list(filter(lambda x: x > 5, so_list))
print(so_lon)  # [6, 7, 8, 9, 10]

# Lọc chuỗi có độ dài > 5
tu_list = ["python", "java", "javascript", "c++", "go"]
tu_dai = list(filter(lambda tu: len(tu) > 5, tu_list))
print(tu_dai)  # ['python', 'javascript']
```

### 3.3 Reduce Function
```python
from functools import reduce

# Tính tổng
so_list = [1, 2, 3, 4, 5]
tong = reduce(lambda x, y: x + y, so_list)
print(tong)  # 15

# Tìm số lớn nhất
max_value = reduce(lambda x, y: x if x > y else y, so_list)
print(max_value)  # 5

# Tính giai thừa
n = 5
giai_thua = reduce(lambda x, y: x * y, range(1, n + 1))
print(giai_thua)  # 120
```

### 3.4 Sorted Function với Key
```python
# Sắp xếp theo key tùy chỉnh
hoc_sinh = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 7.0},
    {"ten": "Cường", "diem": 9.0},
    {"ten": "Dung", "diem": 6.5}
]

# Sắp xếp theo điểm
sap_xep_diem = sorted(hoc_sinh, key=lambda hs: hs["diem"], reverse=True)
print(sap_xep_diem)

# Sắp xếp theo tên
sap_xep_ten = sorted(hoc_sinh, key=lambda hs: hs["ten"])
print(sap_xep_ten)

# Sắp xếp chuỗi theo độ dài
tu_list = ["python", "java", "c", "javascript", "go"]
sap_xep_do_dai = sorted(tu_list, key=lambda tu: len(tu))
print(sap_xep_do_dai)  # ['c', 'go', 'java', 'python', 'javascript']
```

## 4. Decorators

### 4.1 Decorator Cơ Bản
```python
def my_decorator(func):
    def wrapper():
        print("Trước khi gọi function")
        func()
        print("Sau khi gọi function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Trước khi gọi function
# Hello!
# Sau khi gọi function
```

### 4.2 Decorator Với Arguments
```python
def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} thực thi trong {end_time - start_time:.4f} giây")
        return result
    return wrapper

@timing_decorator
def tinh_tong(n):
    return sum(range(n))

@timing_decorator
def tinh_giai_thua(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(tinh_tong(1000000))
print(tinh_giai_thua(1000))
```

### 4.3 Decorator Với Parameters
```python
def retry_decorator(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Lần thử {attempt + 1} thất bại: {e}")
            return None
        return wrapper
    return decorator

@retry_decorator(max_attempts=3)
def chia_so(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b

# Test
try:
    print(chia_so(10, 2))  # 5.0
    print(chia_so(10, 0))  # Sẽ thử 3 lần rồi raise exception
except ValueError as e:
    print(f"Lỗi cuối cùng: {e}")
```

### 4.4 Class-based Decorators
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} đã được gọi {self.count} lần")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("An")    # say_hello đã được gọi 1 lần
say_hello("Bình")  # say_hello đã được gọi 2 lần
```

## 5. Closures

### 5.1 Closure Cơ Bản
```python
def outer_function(x):
    def inner_function(y):
        return x + y  # x được "nhớ" từ outer function
    return inner_function

# Tạo closure
add_10 = outer_function(10)
add_20 = outer_function(20)

print(add_10(5))  # 15
print(add_20(5))  # 25
```

### 5.2 Closure Với State
```python
def make_counter(start=0):
    count = start
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    def reset():
        nonlocal count
        count = start
    
    def get_count():
        return count
    
    # Trả về dictionary chứa các functions
    return {
        'next': counter,
        'reset': reset,
        'current': get_count
    }

# Sử dụng
counter1 = make_counter(0)
counter2 = make_counter(100)

print(counter1['next']())     # 1
print(counter1['next']())     # 2
print(counter2['next']())     # 101
print(counter1['current']())  # 2
counter1['reset']()
print(counter1['current']())  # 0
```

### 5.3 Closure Factory Pattern
```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

def make_validator(min_value, max_value):
    def validator(value):
        return min_value <= value <= max_value
    return validator

# Sử dụng
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Validator
age_validator = make_validator(0, 120)
score_validator = make_validator(0, 10)

print(age_validator(25))   # True
print(age_validator(150))  # False
print(score_validator(8))  # True
```

## 6. Generators

### 6.1 Generator Functions
```python
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

# Sử dụng generator
counter = count_up_to(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5

# Generator chỉ có thể duyệt một lần
for num in counter:
    print(num)  # Không in gì (generator đã exhausted)
```

### 6.2 Generator Expressions
```python
# List comprehension
squares_list = [x**2 for x in range(10)]
print(type(squares_list))  # <class 'list'>

# Generator expression
squares_gen = (x**2 for x in range(10))
print(type(squares_gen))   # <class 'generator'>

# Sử dụng generator
for square in squares_gen:
    print(square)
```

### 6.3 Fibonacci Generator
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Sử dụng
fib = fibonacci()
for i in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 6.4 Generator Với File Processing
```python
def read_large_file(file_path):
    """Generator để đọc file lớn từng dòng"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def process_numbers(numbers):
    """Generator xử lý số từ iterable"""
    for num in numbers:
        if num % 2 == 0:
            yield num * 2
        else:
            yield num * 3

# Chain generators
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = process_numbers(numbers)
for result in processed:
    print(result)
```

## 7. Recursion

### 7.1 Recursion Cơ Bản
```python
def factorial(n):
    """Tính giai thừa bằng đệ quy"""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(0))  # 1
```

### 7.2 Fibonacci Recursion
```python
def fibonacci_recursive(n):
    """Tính số Fibonacci bằng đệ quy"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Tối ưu với memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_recursive(10))  # 55 (chậm)
print(fibonacci_memo(10))       # 55 (nhanh)
```

### 7.3 Tree Traversal
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def traverse_tree(node, depth=0):
    """Duyệt cây bằng đệ quy"""
    print("  " * depth + str(node.value))
    for child in node.children:
        traverse_tree(child, depth + 1)

# Tạo cây
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
grandchild1 = TreeNode("Grandchild 1")
grandchild2 = TreeNode("Grandchild 2")

root.add_child(child1)
root.add_child(child2)
child1.add_child(grandchild1)
child1.add_child(grandchild2)

traverse_tree(root)
```

### 7.4 Directory Traversal
```python
import os

def list_files_recursive(directory, extension=None):
    """Liệt kê file trong thư mục và thư mục con"""
    items = []
    
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            if os.path.isfile(item_path):
                if extension is None or item.endswith(extension):
                    items.append(item_path)
            elif os.path.isdir(item_path):
                # Đệ quy vào thư mục con
                items.extend(list_files_recursive(item_path, extension))
    except PermissionError:
        pass
    
    return items

# Sử dụng
python_files = list_files_recursive(".", ".py")
for file in python_files:
    print(file)
```

## 8. Functional Programming Patterns

### 8.1 Function Composition
```python
def compose(f, g):
    """Kết hợp hai functions"""
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

# Composition
add_then_multiply = compose(multiply_by_two, add_one)
print(add_then_multiply(5))  # (5 + 1) * 2 = 12

multiply_then_add = compose(add_one, multiply_by_two)
print(multiply_then_add(5))  # (5 * 2) + 1 = 11
```

### 8.2 Partial Application
```python
from functools import partial

def multiply(x, y, z):
    return x * y * z

# Partial application
multiply_by_2 = partial(multiply, 2)
multiply_by_2_and_3 = partial(multiply, 2, 3)

print(multiply_by_2(3, 4))      # 2 * 3 * 4 = 24
print(multiply_by_2_and_3(4))   # 2 * 3 * 4 = 24
```

### 8.3 Currying
```python
def curry_add(x):
    def add_x(y):
        def add_xy(z):
            return x + y + z
        return add_xy
    return add_x

# Sử dụng
add_1 = curry_add(1)
add_1_2 = add_1(2)
result = add_1_2(3)  # 1 + 2 + 3 = 6
print(result)

# Hoặc viết gọn
result = curry_add(1)(2)(3)  # 6
print(result)
```

## 9. Ví Dụ Thực Tế

### 9.1 Hệ Thống Cache Với Decorator
```python
from functools import wraps
import time

def cache_decorator(expiry_time=60):
    def decorator(func):
        cache = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Tạo key từ arguments
            key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            # Kiểm tra cache
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < expiry_time:
                    print(f"Cache hit for {func.__name__}")
                    return result
            
            # Tính toán và lưu cache
            print(f"Computing {func.__name__}")
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        
        return wrapper
    return decorator

@cache_decorator(expiry_time=30)
def expensive_calculation(n):
    time.sleep(2)  # Giả lập tính toán phức tạp
    return sum(i**2 for i in range(n))

# Test
print(expensive_calculation(1000))  # Computing (chậm)
print(expensive_calculation(1000))  # Cache hit (nhanh)
```

### 9.2 Event System Với Closures
```python
def create_event_system():
    """Tạo hệ thống event với closures"""
    events = {}
    
    def register_event(event_name, callback):
        if event_name not in events:
            events[event_name] = []
        events[event_name].append(callback)
    
    def trigger_event(event_name, *args, **kwargs):
        if event_name in events:
            for callback in events[event_name]:
                callback(*args, **kwargs)
    
    def remove_event(event_name):
        if event_name in events:
            del events[event_name]
    
    return {
        'register': register_event,
        'trigger': trigger_event,
        'remove': remove_event
    }

# Sử dụng
event_system = create_event_system()

# Đăng ký event handlers
def on_user_login(username):
    print(f"User {username} đã đăng nhập")

def on_user_logout(username):
    print(f"User {username} đã đăng xuất")

def log_activity(action, username):
    print(f"LOG: {action} - {username}")

event_system['register']('user_login', on_user_login)
event_system['register']('user_login', lambda u: log_activity('LOGIN', u))
event_system['register']('user_logout', on_user_logout)

# Trigger events
event_system['trigger']('user_login', 'john_doe')
event_system['trigger']('user_logout', 'john_doe')
```

### 9.3 Data Pipeline Với Generators
```python
def read_data():
    """Generator đọc dữ liệu"""
    data = [
        {'name': 'An', 'age': 25, 'salary': 10000000},
        {'name': 'Bình', 'age': 30, 'salary': 15000000},
        {'name': 'Cường', 'age': 35, 'salary': 20000000},
        {'name': 'Dung', 'age': 28, 'salary': 12000000},
        {'name': 'Em', 'age': 22, 'salary': 8000000}
    ]
    for item in data:
        yield item

def filter_by_age(data_stream, min_age):
    """Filter theo tuổi"""
    for item in data_stream:
        if item['age'] >= min_age:
            yield item

def calculate_tax(data_stream):
    """Tính thuế"""
    for item in data_stream:
        item = item.copy()
        if item['salary'] > 11000000:
            item['tax'] = (item['salary'] - 11000000) * 0.1
        else:
            item['tax'] = 0
        item['net_salary'] = item['salary'] - item['tax']
        yield item

def format_output(data_stream):
    """Format output"""
    for item in data_stream:
        yield f"{item['name']}: {item['net_salary']:,} VND (thuế: {item['tax']:,})"

# Tạo pipeline
pipeline = format_output(
    calculate_tax(
        filter_by_age(
            read_data(),
            min_age=25
        )
    )
)

# Xử lý dữ liệu
for result in pipeline:
    print(result)
```

## 10. Best Practices

### 10.1 Khi Nào Sử Dụng Lambda
```python
# Tốt - Lambda đơn giản
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# Không tốt - Lambda phức tạp
complex_lambda = lambda x: x**2 if x > 0 else abs(x) * 2 if x < -10 else 0

# Tốt - Sử dụng function thường cho logic phức tạp
def complex_calculation(x):
    if x > 0:
        return x**2
    elif x < -10:
        return abs(x) * 2
    else:
        return 0
```

### 10.2 Recursion vs Iteration
```python
# Recursion - Tốt cho cấu trúc dữ liệu phân cấp
def traverse_nested_dict(d, prefix=""):
    for key, value in d.items():
        if isinstance(value, dict):
            traverse_nested_dict(value, f"{prefix}{key}.")
        else:
            print(f"{prefix}{key}: {value}")

# Iteration - Tốt cho tính toán đơn giản
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### 10.3 Generator vs List
```python
# Generator - Tốt cho dữ liệu lớn
def read_large_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# List - Tốt cho dữ liệu nhỏ cần truy cập nhiều lần
def process_small_data():
    data = [1, 2, 3, 4, 5]
    return [x * 2 for x in data]
```

## 11. Tổng Kết

Advanced Function Concepts mở ra sức mạnh thực sự của Python:

### Điểm Quan Trọng:
1. **Scope và LEGB** - Hiểu cách Python tìm kiếm biến
2. **Lambda Functions** - Sử dụng cho logic đơn giản
3. **Higher-order Functions** - Map, Filter, Reduce
4. **Decorators** - Mở rộng chức năng functions
5. **Generators** - Xử lý dữ liệu lớn hiệu quả
6. **Recursion** - Giải quyết bài toán phân cấp

### Khi Nào Sử dụng:
- **Lambda**: Logic đơn giản, một dòng
- **Decorators**: Logging, caching, validation
- **Generators**: Xử lý dữ liệu lớn, streaming
- **Recursion**: Cấu trúc dữ liệu phân cấp
- **Closures**: State management, factory patterns

### Lộ Trình Học Tiếp:
- **Thực hành**: Áp dụng vào dự án thực tế
- **Nâng cao**: Metaclasses, Descriptors
- **Frameworks**: Django, Flask, FastAPI 