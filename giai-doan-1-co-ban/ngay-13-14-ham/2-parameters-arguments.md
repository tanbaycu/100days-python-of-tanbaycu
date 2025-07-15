# 📚 LÝ THUYẾT 2: PARAMETERS & ARGUMENTS - ĐI SÂU VÀO THAM SỐ HÀM

## 🎯 MỤC TIÊU HỌC TẬP
- Hiểu rõ các loại tham số (parameters) và đối số (arguments)
- Thành thạo positional, keyword, default, *args, **kwargs
- Xử lý edge cases, validate input, tránh lỗi thường gặp
- Ứng dụng vào nhiều tình huống thực tế

---

## I. KHÁI NIỆM CƠ BẢN

### 1. Parameter vs Argument
- **Parameter (tham số)**: Biến được định nghĩa trong phần khai báo hàm
- **Argument (đối số)**: Giá trị thực tế được truyền vào khi gọi hàm

```python
def greet(name):  # name là parameter
    print(f"Xin chào {name}!")

greet("An")  # "An" là argument
```

---

## II. CÁC LOẠI THAM SỐ HÀM

### 1. Positional Parameters (Tham số vị trí)

```python
def add(a, b):
    return a + b

add(3, 5)  # a=3, b=5
```

- Đối số được gán theo thứ tự vị trí
- Phải truyền đủ số lượng

### 2. Keyword Parameters (Tham số từ khóa)

```python
def introduce(name, age, city):
    print(f"Tôi là {name}, {age} tuổi, sống ở {city}")

introduce(age=25, name="Minh", city="Hà Nội")
```

- Truyền theo tên, không cần đúng thứ tự
- Có thể kết hợp positional + keyword (positional phải trước)

### 3. Default Parameters (Tham số mặc định)

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9 (exponent=2 mặc định)
print(power(2, 5))   # 32
```

- Nếu không truyền, dùng giá trị mặc định
- Default phải đứng sau non-default

```python
def foo(a, b=2, c=3): pass  # OK
def bar(a=1, b): pass        # ❌ Error
```

### 4. *args - Variable Positional Arguments

```python
def sum_all(*args):
    print(args)  # args là tuple
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
```

- Cho phép truyền số lượng đối số không giới hạn
- Được gom thành tuple

### 5. **kwargs - Variable Keyword Arguments

```python
def print_info(**kwargs):
    print(kwargs)  # kwargs là dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="An", age=20, city="Hà Nội")
```

- Cho phép truyền nhiều cặp key=value
- Được gom thành dictionary

### 6. Kết hợp *args và **kwargs

```python
def demo(a, *args, b=10, **kwargs):
    print(f"a={a}, args={args}, b={b}, kwargs={kwargs}")

demo(1, 2, 3, 4, b=20, x=100, y=200)
# a=1, args=(2,3,4), b=20, kwargs={'x':100,'y':200}
```

---

## III. EDGE CASES & LỖI THƯỜNG GẶP

### 1. Mutable Default Arguments

```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))  # [1]
print(append_item(2))  # [1,2] ❌
```

- **Lỗi:** Default mutable chỉ tạo 1 lần, bị "dính" giữa các lần gọi
- **Giải pháp:**

```python
def append_item_safe(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 2. Truyền thiếu/thừa đối số

```python
def foo(a, b): pass
foo(1)        # ❌ TypeError: missing 1 required positional argument
foo(1,2,3)    # ❌ TypeError: takes 2 positional arguments but 3 were given
```

### 3. Trùng tên giữa positional và keyword

```python
def bar(x, y): pass
bar(1, x=2)   # ❌ TypeError: multiple values for argument 'x'
```

### 4. Sử dụng *args, **kwargs sai thứ tự

```python
def bad(a, *args, b, **kwargs): pass  # OK từ Python 3
# def bad(a, **kwargs, *args): pass  # ❌ SyntaxError
```

---

## IV. VALIDATION & BEST PRACTICES

### 1. Kiểm tra input

```python
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a và b phải là số")
    if b == 0:
        raise ValueError("Không chia cho 0")
    return a / b
```

### 2. Sử dụng *args, **kwargs hợp lý
- Chỉ dùng khi thực sự cần flexibility
- Ghi rõ docstring về kiểu dữ liệu mong đợi
- Không lạm dụng, tránh code khó đọc

### 3. Đặt tên parameters rõ ràng
- Dễ hiểu, có ý nghĩa
- Tránh viết tắt, generic (a, b, x, y)

### 4. Sắp xếp thứ tự parameters
- Thứ tự nên là: required, *args, default, **kwargs

```python
def example(a, b, *args, c=10, **kwargs): pass
```

---

## V. TÌNH HUỐNG THỰC TẾ & ỨNG DỤNG

### 1. Hàm xử lý dữ liệu linh hoạt

```python
def process_data(data, *transforms, **options):
    """Áp dụng nhiều hàm biến đổi lên data"""
    for func in transforms:
        data = func(data)
    if options.get('reverse'):
        data = data[::-1]
    return data

# Ví dụ sử dụng
result = process_data(
    [1,2,3,4],
    lambda x: [i*2 for i in x],
    lambda x: [i+1 for i in x],
    reverse=True
)
print(result)  # [9,7,5,3]
```

### 2. Hàm API với **kwargs

```python
def api_request(endpoint, **params):
    url = f"https://api.example.com/{endpoint}?"
    query = "&".join(f"{k}={v}" for k,v in params.items())
    return url + query

print(api_request("search", q="python", page=2, sort="desc"))
# https://api.example.com/search?q=python&page=2&sort=desc
```

### 3. Hàm validate dữ liệu động

```python
def validate_fields(data, *required_fields, **validators):
    for field in required_fields:
        if field not in data:
            return False, f"Thiếu trường {field}"
    for field, func in validators.items():
        if field in data and not func(data[field]):
            return False, f"Trường {field} không hợp lệ"
    return True, "Hợp lệ"

# Sử dụng
user = {'name':'An','age':20,'email':'an@gmail.com'}
result = validate_fields(
    user,
    'name','age','email',
    age=lambda x: x>=18,
    email=lambda x: '@' in x
)
print(result)
```

---

## VI. BÀI TẬP THỰC HÀNH

1. Viết hàm nhận vào nhiều số bất kỳ, trả về tổng các số lẻ
2. Viết hàm nhận vào list và nhiều hàm xử lý, áp dụng lần lượt các hàm đó lên list
3. Viết hàm nhận vào **kwargs, trả về dict chỉ chứa các key có giá trị là số chẵn
4. Viết hàm validate form với các trường động và điều kiện kiểm tra
5. Viết hàm nhận vào n số, trả về tuple (min, max, average)

---

## VII. KẾT LUẬN
- Parameters & Arguments là nền tảng để viết hàm linh hoạt, mạnh mẽ
- Hiểu rõ các loại tham số giúp tránh lỗi, tối ưu code
- Ứng dụng vào nhiều tình huống thực tế, từ xử lý dữ liệu đến xây dựng API

**Tiếp theo:** Học về advanced concepts: scope, lambda, decorators... 