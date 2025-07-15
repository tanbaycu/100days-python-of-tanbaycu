# 📚 LÝ THUYẾT 1: FUNCTIONS CƠ BẢN - TỪ ĐƠN GIẢN ĐẾN NÂNG CAO

## 🎯 MỤC TIÊU HỌC TẬP

Sau bài học này, bạn sẽ:
- ✅ Hiểu rõ khái niệm function và tại sao cần thiết
- ✅ Nắm vững cú pháp và cấu trúc của functions
- ✅ Thành thạo return values và side effects
- ✅ Áp dụng best practices trong việc viết functions
- ✅ Xử lý được các tình huống phức tạp với functions

---

## 🌟 PHẦN I: KHÁI NIỆM VÀ MOTIVATION

### 🤔 Tại Sao Cần Functions?

Hãy tưởng tượng bạn đang viết một chương trình tính toán điểm trung bình của học sinh:

```python
# ❌ Code không sử dụng functions - Lặp lại và khó maintain
student1_scores = [8, 7, 9, 6, 8]
student1_total = 0
for score in student1_scores:
    student1_total += score
student1_average = student1_total / len(student1_scores)
print(f"Học sinh 1: {student1_average}")

student2_scores = [9, 8, 7, 8, 9]
student2_total = 0
for score in student2_scores:
    student2_total += score
student2_average = student2_total / len(student2_scores)
print(f"Học sinh 2: {student2_average}")

# ... và còn 100 học sinh nữa 😱
```

**Vấn đề của code trên:**
- 🔄 **Lặp lại code**: Cùng một logic được viết nhiều lần
- 🐛 **Khó debug**: Nếu có lỗi, phải sửa ở nhiều nơi
- 📈 **Không scalable**: Thêm học sinh mới = thêm code mới
- 🔧 **Khó maintain**: Thay đổi logic = sửa toàn bộ code

```python
# ✅ Code sử dụng functions - Clean và maintainable
def calculate_average(scores):
    """Tính điểm trung bình của một danh sách điểm"""
    if not scores:  # Xử lý edge case
        return 0
    return sum(scores) / len(scores)

# Sử dụng function
student1_average = calculate_average([8, 7, 9, 6, 8])
student2_average = calculate_average([9, 8, 7, 8, 9])
student3_average = calculate_average([7, 8, 9, 7, 8])

print(f"Học sinh 1: {student1_average}")
print(f"Học sinh 2: {student2_average}")
print(f"Học sinh 3: {student3_average}")
```

**Lợi ích của functions:**
- 🔄 **DRY Principle**: Don't Repeat Yourself
- 🧩 **Modularity**: Chia code thành các module nhỏ
- 🔧 **Maintainability**: Dễ sửa đổi và cập nhật
- 🧪 **Testability**: Dễ test từng phần riêng biệt
- 📖 **Readability**: Code dễ đọc và hiểu

### 🏗️ Khái Niệm Function

**Function** là một khối code được đặt tên, có thể:
- Nhận **input** (parameters/arguments)
- Thực hiện **xử lý** (processing)
- Trả về **output** (return value)
- Có **side effects** (tác động bên ngoài)

```python
# Anatomy của một function
def function_name(parameters):
    """Docstring - mô tả function"""
    # Function body - xử lý logic
    return result  # Optional return value
```

---

## 🔧 PHẦN II: CÚ PHÁP VÀ CẤU TRÚC CHI TIẾT

### 1. 📝 Cú Pháp Cơ Bản

```python
def greet():
    """Function đơn giản nhất - không parameter, không return"""
    print("Xin chào!")

# Gọi function
greet()  # Output: Xin chào!
```

**Phân tích cú pháp:**
- `def`: Keyword để định nghĩa function
- `greet`: Tên function (snake_case convention)
- `()`: Dấu ngoặc chứa parameters (rỗng nếu không có)
- `:`: Dấu hai chấm bắt đầu function body
- `"""..."""`: Docstring (optional nhưng recommended)
- Function body: Code thực thi, phải được indent

### 2. 🎯 Function Với Parameters

```python
def greet_person(name):
    """Function với 1 parameter"""
    print(f"Xin chào {name}!")

def greet_person_formal(name, title):
    """Function với nhiều parameters"""
    print(f"Xin chào {title} {name}!")

# Sử dụng
greet_person("An")                    # Output: Xin chào An!
greet_person_formal("Minh", "Anh")    # Output: Xin chào Anh Minh!
```

**Quy tắc đặt tên parameters:**
- Sử dụng `snake_case`: `user_name`, `total_score`
- Tên có ý nghĩa: `age` thay vì `a`, `student_list` thay vì `lst`
- Tránh keywords: không dùng `class`, `def`, `return`

### 3. 🔄 Function Với Return Value

```python
def add_numbers(a, b):
    """Cộng hai số và trả về kết quả"""
    result = a + b
    return result

def multiply_numbers(a, b):
    """Nhân hai số - return trực tiếp"""
    return a * b

# Sử dụng return value
sum_result = add_numbers(5, 3)        # sum_result = 8
product = multiply_numbers(4, 7)      # product = 28
print(f"Tổng: {sum_result}, Tích: {product}")
```

**Quan trọng về return:**
- Function không có `return` sẽ trả về `None`
- `return` dừng execution của function ngay lập tức
- Có thể return nhiều giá trị: `return a, b, c`

### 4. 🎨 Multiple Return Values

```python
def analyze_numbers(numbers):
    """Phân tích danh sách số và trả về nhiều thông tin"""
    if not numbers:
        return 0, 0, 0, 0  # min, max, sum, avg
    
    min_val = min(numbers)
    max_val = max(numbers)
    sum_val = sum(numbers)
    avg_val = sum_val / len(numbers)
    
    return min_val, max_val, sum_val, avg_val

# Sử dụng multiple return values
scores = [85, 92, 78, 96, 88]

# Cách 1: Unpack trực tiếp
min_score, max_score, total_score, avg_score = analyze_numbers(scores)
print(f"Min: {min_score}, Max: {max_score}, Avg: {avg_score}")

# Cách 2: Nhận tuple
result = analyze_numbers(scores)
print(f"Kết quả: {result}")  # (78, 96, 439, 87.8)
```

---

## 🌍 PHẦN III: SCOPE VÀ NAMESPACE CỞ BẢN

### 1. 🏠 Local vs Global Variables

```python
# Global variable
global_message = "Tôi là global variable"

def demo_scope():
    # Local variable
    local_message = "Tôi là local variable"
    print(f"Trong function: {local_message}")
    print(f"Trong function: {global_message}")  # Có thể đọc global

demo_scope()
print(f"Ngoài function: {global_message}")     # OK
# print(f"Ngoài function: {local_message}")    # ❌ Error!
```

**Quy tắc scope:**
- **Local variables**: Chỉ tồn tại trong function
- **Global variables**: Có thể đọc từ function
- **Không thể modify global** từ function (trừ khi dùng `global`)

### 2. 🔄 Modifying Global Variables

```python
counter = 0  # Global variable

def increment_counter():
    global counter  # Khai báo sử dụng global variable
    counter += 1
    print(f"Counter trong function: {counter}")

def get_counter():
    return counter  # Chỉ đọc, không cần global

print(f"Counter ban đầu: {counter}")
increment_counter()  # Counter trong function: 1
print(f"Counter sau khi increment: {counter}")  # 1
```

**Best Practice:**
- 🚫 **Tránh global variables** khi có thể
- ✅ **Sử dụng parameters và return values** thay vì global
- ✅ **Nếu cần global**, khai báo rõ ràng với `global`

### 3. 🎯 Parameter Passing - Call by Value vs Reference

```python
def modify_number(x):
    """Integers là immutable - không thể modify"""
    x = x + 10
    print(f"Trong function: {x}")
    return x

def modify_list(lst):
    """Lists là mutable - có thể modify"""
    lst.append(4)
    print(f"Trong function: {lst}")

# Test với number (immutable)
num = 5
result = modify_number(num)
print(f"Sau function - num: {num}, result: {result}")
# Output: num vẫn là 5, result là 15

# Test với list (mutable)
my_list = [1, 2, 3]
modify_list(my_list)
print(f"Sau function - my_list: {my_list}")
# Output: my_list đã thay đổi thành [1, 2, 3, 4]
```

**Hiểu về parameter passing:**
- **Immutable objects** (int, str, tuple): Không thể modify trong function
- **Mutable objects** (list, dict, set): Có thể modify trong function
- **Best practice**: Tránh modify mutable parameters, return new objects

---

## 📚 PHẦN IV: DOCSTRINGS VÀ DOCUMENTATION

### 1. 📖 Viết Docstring Hiệu Quả

```python
def calculate_bmi(weight, height):
    """
    Tính chỉ số BMI (Body Mass Index).
    
    Args:
        weight (float): Cân nặng tính bằng kg
        height (float): Chiều cao tính bằng mét
    
    Returns:
        float: Chỉ số BMI
    
    Raises:
        ValueError: Khi weight hoặc height <= 0
        
    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """
    Phân loại BMI theo tiêu chuẩn WHO.
    
    Args:
        bmi (float): Chỉ số BMI
    
    Returns:
        str: Phân loại BMI ('Thiếu cân', 'Bình thường', 'Thừa cân', 'Béo phì')
    """
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"

# Sử dụng
try:
    bmi = calculate_bmi(70, 1.75)
    category = categorize_bmi(bmi)
    print(f"BMI: {bmi:.2f} - Phân loại: {category}")
except ValueError as e:
    print(f"Lỗi: {e}")
```

### 2. 🔍 Accessing Docstrings

```python
# Xem docstring
print(calculate_bmi.__doc__)

# Sử dụng help()
help(calculate_bmi)

# Trong IPython/Jupyter
# calculate_bmi?
```

---

## 🎯 PHẦN V: BEST PRACTICES VÀ COMMON PITFALLS

### 1. ✅ Best Practices

#### A. Function Naming Convention

```python
# ✅ Good naming
def calculate_tax(income, tax_rate):
    """Tính thuế thu nhập"""
    return income * tax_rate

def is_valid_email(email):
    """Kiểm tra email hợp lệ"""
    return "@" in email and "." in email

def get_user_by_id(user_id):
    """Lấy thông tin user theo ID"""
    # Implementation here
    pass

# ❌ Bad naming
def calc(x, y):  # Tên không rõ ràng
    return x * y

def func1(data):  # Tên generic
    return data.upper()
```

#### B. Function Length và Complexity

```python
# ✅ Good - Single responsibility
def validate_password(password):
    """Kiểm tra mật khẩu hợp lệ"""
    if len(password) < 8:
        return False, "Mật khẩu phải có ít nhất 8 ký tự"
    if not any(c.isupper() for c in password):
        return False, "Mật khẩu phải có ít nhất 1 chữ hoa"
    if not any(c.islower() for c in password):
        return False, "Mật khẩu phải có ít nhất 1 chữ thường"
    if not any(c.isdigit() for c in password):
        return False, "Mật khẩu phải có ít nhất 1 số"
    return True, "Mật khẩu hợp lệ"

def hash_password(password):
    """Mã hóa mật khẩu"""
    # Implementation here
    pass

def create_user(username, password, email):
    """Tạo user mới"""
    # Validate password
    is_valid, message = validate_password(password)
    if not is_valid:
        return False, message
    
    # Hash password
    hashed_password = hash_password(password)
    
    # Create user
    # Implementation here
    return True, "User created successfully"
```

#### C. Error Handling

```python
def divide_numbers(a, b):
    """
    Chia hai số với error handling.
    
    Args:
        a (float): Số bị chia
        b (float): Số chia
    
    Returns:
        float: Kết quả phép chia
    
    Raises:
        TypeError: Khi a hoặc b không phải số
        ZeroDivisionError: Khi b = 0
    """
    # Type checking
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Cả a và b phải là số")
    
    # Zero division check
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0")
    
    return a / b

# Sử dụng với error handling
try:
    result = divide_numbers(10, 2)
    print(f"Kết quả: {result}")
except (TypeError, ZeroDivisionError) as e:
    print(f"Lỗi: {e}")
```

### 2. ❌ Common Pitfalls

#### A. Mutable Default Arguments

```python
# ❌ Dangerous - Mutable default argument
def add_item(item, target_list=[]):
    """NGUY HIỂM: Default list được share giữa các lần gọi"""
    target_list.append(item)
    return target_list

# Test
list1 = add_item("apple")
list2 = add_item("banana")
print(list1)  # ['apple', 'banana'] - Unexpected!
print(list2)  # ['apple', 'banana'] - Same list!

# ✅ Safe - Immutable default argument
def add_item_safe(item, target_list=None):
    """An toàn: Tạo list mới mỗi lần gọi"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# Test
list1 = add_item_safe("apple")
list2 = add_item_safe("banana")
print(list1)  # ['apple'] - Correct!
print(list2)  # ['banana'] - Correct!
```

#### B. Modifying Global State

```python
# ❌ Bad - Modifying global state
total_score = 0

def add_score(score):
    """Thêm điểm vào tổng điểm global"""
    global total_score
    total_score += score
    return total_score

# ✅ Good - Pure function
def calculate_total_score(current_total, new_score):
    """Tính tổng điểm mới"""
    return current_total + new_score

# Usage
total_score = 0
total_score = calculate_total_score(total_score, 85)
total_score = calculate_total_score(total_score, 92)
```

#### C. Too Many Parameters

```python
# ❌ Bad - Too many parameters
def create_user(first_name, last_name, email, phone, address, city, 
                country, postal_code, age, gender, occupation):
    """Quá nhiều parameters - khó sử dụng"""
    pass

# ✅ Good - Use data structure
def create_user(user_info):
    """Sử dụng dictionary cho user info"""
    required_fields = ['first_name', 'last_name', 'email']
    
    for field in required_fields:
        if field not in user_info:
            raise ValueError(f"Missing required field: {field}")
    
    # Process user creation
    pass

# Usage
user_data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john@example.com',
    'phone': '123-456-7890',
    'address': '123 Main St'
}
create_user(user_data)
```

---

## 🔬 PHẦN VI: TÌNH HUỐNG THỰC TẾ VÀ ỨNG DỤNG

### 1. 🧮 Tình Huống: Hệ Thống Tính Lương

```python
def calculate_base_salary(hours_worked, hourly_rate):
    """Tính lương cơ bản"""
    return hours_worked * hourly_rate

def calculate_overtime_pay(hours_worked, hourly_rate, overtime_threshold=40):
    """Tính lương làm thêm giờ"""
    if hours_worked <= overtime_threshold:
        return 0
    
    overtime_hours = hours_worked - overtime_threshold
    overtime_rate = hourly_rate * 1.5  # 150% lương cơ bản
    return overtime_hours * overtime_rate

def calculate_tax(gross_salary, tax_rate=0.2):
    """Tính thuế thu nhập"""
    return gross_salary * tax_rate

def calculate_net_salary(hours_worked, hourly_rate, tax_rate=0.2):
    """Tính lương thực lĩnh"""
    base_salary = calculate_base_salary(hours_worked, hourly_rate)
    overtime_pay = calculate_overtime_pay(hours_worked, hourly_rate)
    gross_salary = base_salary + overtime_pay
    tax = calculate_tax(gross_salary, tax_rate)
    net_salary = gross_salary - tax
    
    return {
        'base_salary': base_salary,
        'overtime_pay': overtime_pay,
        'gross_salary': gross_salary,
        'tax': tax,
        'net_salary': net_salary
    }

# Sử dụng
salary_info = calculate_net_salary(45, 20)  # 45 giờ, 20$/giờ
print(f"Lương cơ bản: ${salary_info['base_salary']}")
print(f"Lương overtime: ${salary_info['overtime_pay']}")
print(f"Lương gross: ${salary_info['gross_salary']}")
print(f"Thuế: ${salary_info['tax']}")
print(f"Lương net: ${salary_info['net_salary']}")
```

### 2. 📊 Tình Huống: Phân Tích Dữ Liệu Học Sinh

```python
def calculate_grade_statistics(grades):
    """Tính thống kê điểm số"""
    if not grades:
        return None
    
    return {
        'count': len(grades),
        'min': min(grades),
        'max': max(grades),
        'average': sum(grades) / len(grades),
        'median': sorted(grades)[len(grades) // 2]
    }

def categorize_grade(grade):
    """Phân loại điểm số"""
    if grade >= 9:
        return 'Xuất sắc'
    elif grade >= 8:
        return 'Giỏi'
    elif grade >= 6.5:
        return 'Khá'
    elif grade >= 5:
        return 'Trung bình'
    else:
        return 'Yếu'

def generate_grade_report(student_grades):
    """Tạo báo cáo điểm số chi tiết"""
    report = {}
    
    for subject, grades in student_grades.items():
        stats = calculate_grade_statistics(grades)
        if stats:
            report[subject] = {
                'statistics': stats,
                'category': categorize_grade(stats['average']),
                'grade_distribution': {}
            }
            
            # Phân bố điểm
            for grade in grades:
                category = categorize_grade(grade)
                report[subject]['grade_distribution'][category] = \
                    report[subject]['grade_distribution'].get(category, 0) + 1
    
    return report

# Sử dụng
student_data = {
    'Toán': [8.5, 9.0, 7.5, 8.0, 9.5],
    'Văn': [7.0, 8.0, 6.5, 7.5, 8.5],
    'Anh': [9.0, 9.5, 8.5, 9.0, 9.5]
}

report = generate_grade_report(student_data)
for subject, info in report.items():
    print(f"\n{subject}:")
    print(f"  Điểm trung bình: {info['statistics']['average']:.2f}")
    print(f"  Phân loại: {info['category']}")
    print(f"  Phân bố: {info['grade_distribution']}")
```

### 3. 🛒 Tình Huống: Hệ Thống E-commerce

```python
def calculate_item_total(price, quantity, discount_percent=0):
    """Tính tổng tiền cho một item"""
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percent / 100)
    return subtotal - discount_amount

def calculate_shipping_cost(total_amount, weight, shipping_method='standard'):
    """Tính phí vận chuyển"""
    if total_amount >= 100:  # Free shipping cho đơn hàng >= $100
        return 0
    
    shipping_rates = {
        'standard': 5.99,
        'express': 12.99,
        'overnight': 24.99
    }
    
    base_cost = shipping_rates.get(shipping_method, 5.99)
    
    # Thêm phí theo trọng lượng
    if weight > 5:  # kg
        base_cost += (weight - 5) * 2
    
    return base_cost

def apply_coupon(total_amount, coupon_code):
    """Áp dụng mã giảm giá"""
    coupons = {
        'SAVE10': {'type': 'percent', 'value': 10, 'min_amount': 50},
        'SAVE20': {'type': 'percent', 'value': 20, 'min_amount': 100},
        'FLAT15': {'type': 'fixed', 'value': 15, 'min_amount': 75}
    }
    
    if coupon_code not in coupons:
        return 0, "Mã giảm giá không hợp lệ"
    
    coupon = coupons[coupon_code]
    
    if total_amount < coupon['min_amount']:
        return 0, f"Đơn hàng tối thiểu ${coupon['min_amount']} để sử dụng mã này"
    
    if coupon['type'] == 'percent':
        discount = total_amount * (coupon['value'] / 100)
    else:  # fixed
        discount = coupon['value']
    
    return discount, "Mã giảm giá đã được áp dụng"

def calculate_order_total(items, shipping_method='standard', coupon_code=None):
    """Tính tổng đơn hàng"""
    subtotal = 0
    total_weight = 0
    
    # Tính tổng từng item
    for item in items:
        item_total = calculate_item_total(
            item['price'], 
            item['quantity'], 
            item.get('discount', 0)
        )
        subtotal += item_total
        total_weight += item['weight'] * item['quantity']
    
    # Tính phí vận chuyển
    shipping_cost = calculate_shipping_cost(subtotal, total_weight, shipping_method)
    
    # Tính tổng trước giảm giá
    total_before_coupon = subtotal + shipping_cost
    
    # Áp dụng coupon
    coupon_discount = 0
    coupon_message = ""
    if coupon_code:
        coupon_discount, coupon_message = apply_coupon(total_before_coupon, coupon_code)
    
    # Tổng cuối cùng
    final_total = total_before_coupon - coupon_discount
    
    return {
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'coupon_discount': coupon_discount,
        'coupon_message': coupon_message,
        'final_total': final_total,
        'total_weight': total_weight
    }

# Sử dụng
order_items = [
    {'name': 'Laptop', 'price': 999.99, 'quantity': 1, 'weight': 2.5, 'discount': 10},
    {'name': 'Mouse', 'price': 29.99, 'quantity': 2, 'weight': 0.2, 'discount': 0},
    {'name': 'Keyboard', 'price': 79.99, 'quantity': 1, 'weight': 1.0, 'discount': 5}
]

order_summary = calculate_order_total(
    order_items, 
    shipping_method='express', 
    coupon_code='SAVE20'
)

print("=== HÓA ĐƠN ===")
print(f"Tổng tiền hàng: ${order_summary['subtotal']:.2f}")
print(f"Phí vận chuyển: ${order_summary['shipping_cost']:.2f}")
print(f"Giảm giá: -${order_summary['coupon_discount']:.2f}")
print(f"Tổng thanh toán: ${order_summary['final_total']:.2f}")
print(f"Trọng lượng: {order_summary['total_weight']:.1f} kg")
print(f"Coupon: {order_summary['coupon_message']}")
```

---

## 🎯 PHẦN VII: TESTING VÀ DEBUGGING

### 1. 🧪 Testing Functions

```python
def test_calculate_average():
    """Test function calculate_average"""
    
    # Test case 1: Normal case
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    # Test case 2: Single element
    assert calculate_average([10]) == 10.0
    
    # Test case 3: Empty list
    assert calculate_average([]) == 0
    
    # Test case 4: Negative numbers
    assert calculate_average([-1, -2, -3]) == -2.0
    
    # Test case 5: Mixed numbers
    assert calculate_average([-5, 0, 5]) == 0.0
    
    print("✅ Tất cả test cases đều pass!")

# Chạy test
test_calculate_average()
```

### 2. 🐛 Debugging Strategies

```python
def debug_function(data):
    """Function với debugging statements"""
    print(f"DEBUG: Input data = {data}")
    print(f"DEBUG: Type of data = {type(data)}")
    
    if not data:
        print("DEBUG: Data is empty")
        return 0
    
    result = sum(data) / len(data)
    print(f"DEBUG: Calculated result = {result}")
    
    return result

# Sử dụng
result = debug_function([1, 2, 3, 4, 5])
print(f"Final result: {result}")
```

---

## 📝 PHẦN VIII: BÀI TẬP VÀ THỰC HÀNH

### 🎯 Bài Tập Cơ Bản

1. **Viết function tính diện tích hình chữ nhật**
2. **Viết function kiểm tra số nguyên tố**
3. **Viết function đảo ngược chuỗi**
4. **Viết function tìm số lớn nhất trong list**
5. **Viết function chuyển đổi nhiệt độ C sang F**

### 🎯 Bài Tập Nâng Cao

1. **Viết function tính factorial với recursion**
2. **Viết function validate email address**
3. **Viết function tính lương nhân viên phức tạp**
4. **Viết function phân tích văn bản**
5. **Viết function quản lý inventory**

---

## 🎉 KẾT LUẬN

Functions là nền tảng của lập trình Python. Thành thạo functions sẽ giúp bạn:

- ✅ Viết code clean, maintainable
- ✅ Tái sử dụng code hiệu quả
- ✅ Debug và test dễ dàng
- ✅ Xây dựng applications phức tạp
- ✅ Làm việc nhóm hiệu quả

**Bước tiếp theo**: Học về Parameters và Arguments chi tiết trong `2-parameters-arguments.md`

---

*"Code is read more often than it is written. Make your functions readable." - Tanbaycu* 