# 📚 LÝ THUYẾT 3: ADVANCED CONCEPTS - FUNCTION SÂU & RỘNG

## 🎯 MỤC TIÊU HỌC TẬP
- Hiểu sâu về scope, namespace, LEGB rule
- Thành thạo lambda, higher-order functions, decorators, generators, recursion
- Ứng dụng functional programming patterns
- Tránh lỗi thường gặp, áp dụng best practices

---

## I. SCOPE, NAMESPACE & LEGB RULE

### 1. Scope là gì?
- **Scope**: Vùng mà biến có thể truy cập được
- **Namespace**: Không gian đặt tên cho các biến, hàm, class

### 2. LEGB Rule
- **L**ocal: Bên trong function
- **E**nclosing: Function bao ngoài (nested)
- **G**lobal: Module hiện tại
- **B**uilt-in: Python built-in

```python
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)  # local
    inner()
    print(x)      # enclosing

x = 'global'
outer()
print(x)          # global
```

### 3. Nonlocal & global

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c())  # 1
print(c())  # 2

# global
x = 10
def foo():
    global x
    x += 5
foo()
print(x)  # 15
```

---

## II. LAMBDA FUNCTIONS & HIGHER-ORDER FUNCTIONS

### 1. Lambda là gì?
- Hàm ẩn danh, ngắn gọn, dùng cho các thao tác đơn giản

```python
f = lambda x, y: x + y
print(f(2, 3))  # 5
```

### 2. Sử dụng lambda với map, filter, reduce

```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120
```

### 3. Higher-order functions
- Hàm nhận hàm khác làm đối số hoặc trả về hàm

```python
def apply_func(f, x):
    return f(x)

def square(n):
    return n * n

print(apply_func(square, 5))  # 25
```

---

## III. DECORATORS - TRANG TRÍ HÀM

### 1. Decorator là gì?
- Hàm nhận vào 1 hàm, trả về 1 hàm mới (bọc thêm logic)

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Bắt đầu...")
        result = func(*args, **kwargs)
        print("Kết thúc!")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Xin chào {name}!")

say_hello("An")
# Output:
# Bắt đầu...
# Xin chào An!
# Kết thúc!
```

### 2. Decorator thực tế: Logging, timing, validate

```python
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Thời gian chạy: {end-start:.4f}s")
        return result
    return wrapper

@timing
def slow_func():
    time.sleep(1)
    print("Done!")

slow_func()
```

---

## IV. GENERATORS & YIELD

### 1. Generator là gì?
- Hàm trả về iterator, sinh giá trị từng bước với `yield`

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```

### 2. So sánh return vs yield
- `return`: Kết thúc hàm, trả về 1 giá trị
- `yield`: Tạm dừng, giữ trạng thái, tiếp tục lần sau

### 3. Generator expressions

```python
gen = (x**2 for x in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
```

---

## V. RECURSION - ĐỆ QUY

### 1. Đệ quy là gì?
- Hàm tự gọi lại chính nó
- Cần điều kiện dừng (base case)

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
```

### 2. Ứng dụng đệ quy: Fibonacci, duyệt cây, backtracking

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(7)])  # [0,1,1,2,3,5,8]
```

---

## VI. FUNCTIONAL PROGRAMMING PATTERNS

### 1. map, filter, reduce
- `map(func, iterable)`: Áp dụng func cho từng phần tử
- `filter(func, iterable)`: Lọc theo điều kiện
- `reduce(func, iterable)`: Tích lũy kết quả

### 2. Closures
- Hàm lồng nhau, nhớ giá trị biến enclosing

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
print(double(5))  # 10
```

---

## VII. BEST PRACTICES & LỖI THƯỜNG GẶP

### 1. Best practices
- Đặt tên rõ ràng, mô tả đúng chức năng
- Sử dụng docstring cho mọi hàm
- Tránh lồng hàm quá sâu, tránh đệ quy không có base case
- Decorator nên dùng functools.wraps để giữ metadata

```python
from functools import wraps

def log_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Gọi hàm {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### 2. Lỗi thường gặp
- Quên return trong recursion
- Sử dụng biến ngoài scope không đúng
- Lạm dụng lambda, decorator gây khó đọc
- Quên yield trong generator

---

## VIII. ỨNG DỤNG THỰC TẾ

### 1. Decorator kiểm tra quyền truy cập

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_admin'):
            print("Truy cập bị từ chối!")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user, user_id):
    print(f"Xóa user {user_id}")

admin = {'name':'An','is_admin':True}
user = {'name':'Bình','is_admin':False}
delete_user(admin, 123)  # OK
delete_user(user, 456)   # Truy cập bị từ chối!
```

### 2. Generator đọc file lớn

```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# for line in read_large_file('big.txt'):
#     process(line)
```

### 3. Functional pipeline

```python
def pipeline(data, *funcs):
    for f in funcs:
        data = f(data)
    return data

result = pipeline(
    [1,2,3,4],
    lambda x: [i*2 for i in x],
    lambda x: [i+1 for i in x],
    sum
)
print(result)  # 22
```

---

## IX. BÀI TẬP THỰC HÀNH

1. Viết decorator log thời gian chạy của hàm
2. Viết generator sinh dãy số nguyên tố vô hạn
3. Viết hàm đệ quy tính tổng các số trong list lồng nhau
4. Viết closure tạo bộ đếm tăng dần
5. Viết hàm sử dụng map/filter/reduce để xử lý list số

---

## X. KẾT LUẬN
- Advanced function concepts giúp code mạnh mẽ, tối ưu, chuyên nghiệp
- Ứng dụng vào automation, data processing, web, AI...
- Tiếp theo: Thực hành bài tập và dự án thực tế! 