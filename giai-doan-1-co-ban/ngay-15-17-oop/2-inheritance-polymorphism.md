# Lý Thuyết 2: Inheritance & Polymorphism - Kế Thừa & Đa Hình

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Nắm vững khái niệm Inheritance và cách implement
- Hiểu rõ Method Overriding và super()
- Thành thạo Polymorphism và tính ứng dụng
- Sử dụng Abstract Classes và Interfaces
- Áp dụng Design Patterns cơ bản

---

## 1. Inheritance - Kế Thừa

### 1.1 Khái Niệm Inheritance

**Inheritance** cho phép một class (child/subclass) kế thừa attributes và methods từ class khác (parent/superclass).

**Lợi ích:**
- Tái sử dụng code
- Tạo hierarchy logic
- Dễ bảo trì và mở rộng
- Giảm code duplication

### 1.2 Syntax Cơ Bản

```python
# Parent class (Base class)
class Animal:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
        self.loai = "Động vật"
    
    def an(self):
        print(f"{self.ten} đang ăn")
    
    def ngu(self):
        print(f"{self.ten} đang ngủ")
    
    def thong_tin(self):
        return f"{self.ten} - {self.tuoi} tuổi - {self.loai}"

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)  # Gọi constructor của parent
        self.giong = giong
        self.loai = "Chó"  # Override attribute
    
    def sua(self):  # Method riêng của Dog
        print(f"{self.ten} đang sủa: Gâu gâu!")
    
    def thong_tin(self):  # Override method
        return f"Chó {self.ten} - {self.tuoi} tuổi - Giống {self.giong}"

class Cat(Animal):
    def __init__(self, ten, tuoi, mau_long):
        super().__init__(ten, tuoi)
        self.mau_long = mau_long
        self.loai = "Mèo"
    
    def keu(self):
        print(f"{self.ten} đang kêu: Meo meo!")
    
    def thong_tin(self):
        return f"Mèo {self.ten} - {self.tuoi} tuổi - Lông {self.mau_long}"

# Sử dụng
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Trắng")

print(dog.thong_tin())  # Chó Buddy - 3 tuổi - Giống Golden Retriever
print(cat.thong_tin())  # Mèo Whiskers - 2 tuổi - Lông Trắng

# Kế thừa methods từ parent
dog.an()    # Buddy đang ăn
cat.ngu()   # Whiskers đang ngủ

# Methods riêng của child
dog.sua()   # Buddy đang sủa: Gâu gâu!
cat.keu()   # Whiskers đang kêu: Meo meo!
```

### 1.3 Multiple Inheritance

Python hỗ trợ multiple inheritance (kế thừa từ nhiều class):

```python
class Flyable:
    def fly(self):
        print("Đang bay")
    
    def land(self):
        print("Đang hạ cánh")

class Swimmable:
    def swim(self):
        print("Đang bơi")
    
    def dive(self):
        print("Đang lặn")

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, ten, tuoi):
        super().__init__(ten, tuoi)
        self.loai = "Vịt"
    
    def quack(self):
        print(f"{self.ten} đang kêu: Quack quack!")
    
    def thong_tin(self):
        return f"Vịt {self.ten} - {self.tuoi} tuổi"

# Sử dụng
duck = Duck("Donald", 1)
print(duck.thong_tin())  # Vịt Donald - 1 tuổi

# Kế thừa từ Animal
duck.an()

# Kế thừa từ Flyable
duck.fly()
duck.land()

# Kế thừa từ Swimmable
duck.swim()
duck.dive()

# Method riêng
duck.quack()
```

### 1.4 Method Resolution Order (MRO)

Python sử dụng MRO để xác định thứ tự tìm kiếm methods:

```python
class A:
    def method(self):
        print("Method từ A")

class B(A):
    def method(self):
        print("Method từ B")

class C(A):
    def method(self):
        print("Method từ C")

class D(B, C):
    pass

# Kiểm tra MRO
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Method từ B (B đứng trước C trong MRO)
```

---

## 2. Method Overriding và super()

### 2.1 Method Overriding

**Method Overriding** là việc child class định nghĩa lại method của parent class:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
    
    def start(self):
        print(f"{self.brand} {self.model} đang khởi động")
    
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Tăng tốc lên {self.speed} km/h")
    
    def get_info(self):
        return f"{self.brand} {self.model} - Tốc độ: {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.doors = 4
    
    def start(self):  # Override method
        print(f"Xe hơi {self.brand} {self.model} đang khởi động động cơ")
        print("Kiểm tra hệ thống an toàn...")
    
    def accelerate(self, speed_increase):  # Override method
        if self.speed + speed_increase > 200:
            print("Cảnh báo: Tốc độ quá cao!")
            self.speed = 200
        else:
            super().accelerate(speed_increase)  # Gọi method của parent
    
    def get_info(self):  # Override method
        parent_info = super().get_info()
        return f"{parent_info} - Nhiên liệu: {self.fuel_type}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def start(self):  # Override method
        print(f"Xe máy {self.brand} {self.model} đang khởi động")
        print("Kiểm tra phanh...")
    
    def wheelie(self):  # Method riêng
        print("Đang bốc đầu!")

# Sử dụng
car = Car("Toyota", "Camry", "Xăng")
motorcycle = Motorcycle("Honda", "CBR", "600cc")

# Override methods hoạt động khác nhau
car.start()
# Xe hơi Toyota Camry đang khởi động động cơ
# Kiểm tra hệ thống an toàn...

motorcycle.start()
# Xe máy Honda CBR đang khởi động
# Kiểm tra phanh...

# Override accelerate với logic khác nhau
car.accelerate(250)  # Cảnh báo: Tốc độ quá cao!
print(car.get_info())

motorcycle.accelerate(150)
print(motorcycle.get_info())
```

### 2.2 super() Advanced Usage

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_pay(self):
        return self.salary
    
    def get_info(self):
        return f"Nhân viên: {self.name}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.bonus = 0
    
    def set_bonus(self, bonus):
        self.bonus = bonus
    
    def get_pay(self):
        base_pay = super().get_pay()
        return base_pay + self.bonus
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Quản lý bộ phận {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        self.project_bonus = 0
    
    def complete_project(self, bonus):
        self.project_bonus += bonus
        print(f"Hoàn thành dự án, nhận thưởng {bonus:,} VND")
    
    def get_pay(self):
        base_pay = super().get_pay()
        return base_pay + self.project_bonus
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Developer {self.programming_language}"

# Sử dụng
manager = Manager("An", 20000000, "IT")
developer = Developer("Bình", 15000000, "Python")

manager.set_bonus(5000000)
developer.complete_project(2000000)

print(manager.get_info())
print(f"Lương: {manager.get_pay():,} VND")

print(developer.get_info())
print(f"Lương: {developer.get_pay():,} VND")
```

---

## 3. Polymorphism - Đa Hình

### 3.1 Khái Niệm Polymorphism

**Polymorphism** cho phép objects của các classes khác nhau được sử dụng thông qua cùng một interface.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError("Subclass phải implement method này")
    
    def perimeter(self):
        raise NotImplementedError("Subclass phải implement method này")
    
    def info(self):
        return f"{self.name} - Diện tích: {self.area():.2f}, Chu vi: {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Hình chữ nhật")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Hình tròn")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Tam giác")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Sử dụng công thức Heron
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
shapes = [
    Rectangle(5, 4),
    Circle(3),
    Triangle(3, 4, 5)
]

# Cùng một interface, hành vi khác nhau
for shape in shapes:
    print(shape.info())
    print(f"Loại: {type(shape).__name__}")
    print("-" * 40)
```

### 3.2 Duck Typing

Python sử dụng "Duck Typing" - "If it walks like a duck and quacks like a duck, it's a duck":

```python
class Duck:
    def fly(self):
        print("Vịt đang bay")
    
    def quack(self):
        print("Quack quack!")

class Airplane:
    def fly(self):
        print("Máy bay đang bay")
    
    def quack(self):
        print("Tiếng động cơ: Vrooom!")

class Bird:
    def fly(self):
        print("Chim đang bay")
    
    def quack(self):
        print("Tweet tweet!")

def make_it_fly_and_quack(thing):
    """Function không cần biết thing là gì, chỉ cần có fly() và quack()"""
    thing.fly()
    thing.quack()

# Duck typing - không cần inheritance
objects = [Duck(), Airplane(), Bird()]

for obj in objects:
    make_it_fly_and_quack(obj)
    print("-" * 20)
```

### 3.3 Polymorphism với Built-in Functions

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"Học sinh {self.name} - Điểm: {self.grade}"
    
    def __len__(self):
        return len(self.name)
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __eq__(self, other):
        return self.grade == other.grade

# Polymorphism với built-in functions
students = [
    Student("An", 8.5),
    Student("Bình", 7.0),
    Student("Cường", 9.0)
]

# __str__ được gọi bởi print()
for student in students:
    print(student)

# __len__ được gọi bởi len()
print(f"Độ dài tên: {[len(s) for s in students]}")

# __lt__ được gọi bởi sorted()
sorted_students = sorted(students)
print("Sắp xếp theo điểm:")
for student in sorted_students:
    print(student)
```

---

## 4. Abstract Classes và Interfaces

### 4.1 Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class cho payment processors"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Method abstract phải được implement bởi subclass"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id):
        """Method abstract cho refund"""
        pass
    
    def log_transaction(self, transaction_id, amount, status):
        """Concrete method có thể được sử dụng bởi subclasses"""
        print(f"Transaction {transaction_id}: {amount} - {status}")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
    
    def process_payment(self, amount):
        # Implement abstract method
        transaction_id = f"CC_{self.merchant_id}_{amount}"
        print(f"Xử lý thanh toán thẻ tín dụng: {amount:,} VND")
        self.log_transaction(transaction_id, amount, "SUCCESS")
        return transaction_id
    
    def refund_payment(self, transaction_id):
        # Implement abstract method
        print(f"Hoàn tiền giao dịch: {transaction_id}")
        self.log_transaction(transaction_id, 0, "REFUNDED")

class PayPalProcessor(PaymentProcessor):
    def __init__(self, api_key):
        self.api_key = api_key
    
    def process_payment(self, amount):
        transaction_id = f"PP_{self.api_key[:6]}_{amount}"
        print(f"Xử lý thanh toán PayPal: {amount:,} VND")
        self.log_transaction(transaction_id, amount, "SUCCESS")
        return transaction_id
    
    def refund_payment(self, transaction_id):
        print(f"Hoàn tiền PayPal: {transaction_id}")
        self.log_transaction(transaction_id, 0, "REFUNDED")

class BankTransferProcessor(PaymentProcessor):
    def __init__(self, bank_code):
        self.bank_code = bank_code
    
    def process_payment(self, amount):
        transaction_id = f"BT_{self.bank_code}_{amount}"
        print(f"Xử lý chuyển khoản ngân hàng: {amount:,} VND")
        self.log_transaction(transaction_id, amount, "SUCCESS")
        return transaction_id
    
    def refund_payment(self, transaction_id):
        print(f"Hoàn tiền chuyển khoản: {transaction_id}")
        self.log_transaction(transaction_id, 0, "REFUNDED")

# Sử dụng polymorphism với abstract classes
def process_order_payment(processor: PaymentProcessor, amount):
    """Function nhận bất kỳ PaymentProcessor nào"""
    transaction_id = processor.process_payment(amount)
    return transaction_id

# Tạo các processors khác nhau
processors = [
    CreditCardProcessor("MERCHANT123"),
    PayPalProcessor("PAYPAL_API_KEY_123456"),
    BankTransferProcessor("VCB")
]

# Polymorphism - cùng interface, implementation khác nhau
for processor in processors:
    transaction_id = process_order_payment(processor, 1000000)
    print(f"Transaction ID: {transaction_id}")
    print("-" * 40)
```

### 4.2 Interface Pattern

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    """Interface cho objects có thể vẽ được"""
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass

class Movable(ABC):
    """Interface cho objects có thể di chuyển"""
    
    @abstractmethod
    def move(self, x, y):
        pass
    
    @abstractmethod
    def get_position(self):
        pass

class GameObject(Drawable, Movable):
    """Base class cho game objects"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player(GameObject):
    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.name = name
        self.health = 100
    
    def draw(self):
        print(f"Vẽ player {self.name} tại ({self.x}, {self.y})")
    
    def get_area(self):
        return 1  # Player có area = 1
    
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"Player {self.name} di chuyển đến ({self.x}, {self.y})")
    
    def get_position(self):
        return (self.x, self.y)

class Enemy(GameObject):
    def __init__(self, x, y, enemy_type):
        super().__init__(x, y)
        self.enemy_type = enemy_type
        self.health = 50
    
    def draw(self):
        print(f"Vẽ enemy {self.enemy_type} tại ({self.x}, {self.y})")
    
    def get_area(self):
        return 2  # Enemy có area = 2
    
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"Enemy {self.enemy_type} di chuyển đến ({self.x}, {self.y})")
    
    def get_position(self):
        return (self.x, self.y)

class GameEngine:
    def __init__(self):
        self.objects = []
    
    def add_object(self, obj: GameObject):
        self.objects.append(obj)
    
    def render_all(self):
        """Vẽ tất cả objects"""
        for obj in self.objects:
            obj.draw()
    
    def move_all(self, dx, dy):
        """Di chuyển tất cả objects"""
        for obj in self.objects:
            current_x, current_y = obj.get_position()
            obj.move(current_x + dx, current_y + dy)
    
    def get_total_area(self):
        """Tính tổng area của tất cả objects"""
        return sum(obj.get_area() for obj in self.objects)

# Sử dụng
game = GameEngine()

# Thêm objects
player = Player(10, 10, "Hero")
enemy1 = Enemy(20, 20, "Goblin")
enemy2 = Enemy(30, 30, "Orc")

game.add_object(player)
game.add_object(enemy1)
game.add_object(enemy2)

# Polymorphism - tất cả objects đều implement cùng interface
game.render_all()
print(f"Total area: {game.get_total_area()}")

game.move_all(5, 5)
print("After moving:")
game.render_all()
```

---

## 5. Design Patterns với Inheritance

### 5.1 Template Method Pattern

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Template method pattern cho data processing"""
    
    def process_data(self, data):
        """Template method định nghĩa workflow"""
        print("Bắt đầu xử lý dữ liệu...")
        
        # Các bước cố định
        validated_data = self.validate_data(data)
        processed_data = self.transform_data(validated_data)
        result = self.save_data(processed_data)
        
        print("Hoàn thành xử lý dữ liệu")
        return result
    
    def validate_data(self, data):
        """Bước validation chung"""
        print("Validating data...")
        if not data:
            raise ValueError("Data không thể rỗng")
        return data
    
    @abstractmethod
    def transform_data(self, data):
        """Bước transform - phải implement bởi subclass"""
        pass
    
    @abstractmethod
    def save_data(self, data):
        """Bước save - phải implement bởi subclass"""
        pass

class CSVProcessor(DataProcessor):
    def transform_data(self, data):
        print("Chuyển đổi dữ liệu thành CSV format")
        # Giả lập chuyển đổi
        csv_data = ",".join(str(item) for item in data)
        return csv_data
    
    def save_data(self, data):
        print(f"Lưu CSV data: {data}")
        return f"csv_file_{len(data)}.csv"

class JSONProcessor(DataProcessor):
    def transform_data(self, data):
        print("Chuyển đổi dữ liệu thành JSON format")
        import json
        json_data = json.dumps(data)
        return json_data
    
    def save_data(self, data):
        print(f"Lưu JSON data: {data}")
        return f"json_file_{len(data)}.json"

class XMLProcessor(DataProcessor):
    def transform_data(self, data):
        print("Chuyển đổi dữ liệu thành XML format")
        xml_data = f"<data>{data}</data>"
        return xml_data
    
    def save_data(self, data):
        print(f"Lưu XML data: {data}")
        return f"xml_file_{len(data)}.xml"

# Sử dụng Template Method Pattern
processors = [
    CSVProcessor(),
    JSONProcessor(),
    XMLProcessor()
]

sample_data = ["item1", "item2", "item3"]

for processor in processors:
    print(f"\n=== {type(processor).__name__} ===")
    result = processor.process_data(sample_data)
    print(f"Result: {result}")
```

### 5.2 Strategy Pattern với Inheritance

```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    """Strategy interface cho sorting algorithms"""
    
    @abstractmethod
    def sort(self, data):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Sử dụng Bubble Sort")
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def get_name(self):
        return "Bubble Sort"

class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Sử dụng Quick Sort")
        return self._quick_sort(data.copy())
    
    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)
    
    def get_name(self):
        return "Quick Sort"

class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Sử dụng Merge Sort")
        return self._merge_sort(data.copy())
    
    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def get_name(self):
        return "Merge Sort"

class SortingContext:
    """Context class sử dụng strategy"""
    
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        print(f"Sorting với {self.strategy.get_name()}")
        result = self.strategy.sort(data)
        print(f"Kết quả: {result}")
        return result

# Sử dụng Strategy Pattern
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Dữ liệu gốc: {data}")

# Tạo context với different strategies
context = SortingContext(BubbleSort())
context.sort_data(data)

print("-" * 40)
context.set_strategy(QuickSort())
context.sort_data(data)

print("-" * 40)
context.set_strategy(MergeSort())
context.sort_data(data)
```

---

## 6. Ví Dụ Thực Tế: Hệ Thống Banking

```python
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class AccountType(Enum):
    SAVINGS = "Tiết kiệm"
    CHECKING = "Thanh toán"
    BUSINESS = "Doanh nghiệp"

class TransactionType(Enum):
    DEPOSIT = "Nạp tiền"
    WITHDRAWAL = "Rút tiền"
    TRANSFER = "Chuyển khoản"

class Transaction:
    def __init__(self, transaction_type, amount, description=""):
        self.transaction_id = f"TXN_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"{self.transaction_id}: {self.transaction_type.value} {self.amount:,} VND - {self.description}"

class Account(ABC):
    """Abstract base class cho tất cả account types"""
    
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now()
        self.is_active = True
    
    @abstractmethod
    def get_account_type(self):
        """Trả về loại tài khoản"""
        pass
    
    @abstractmethod
    def calculate_interest(self):
        """Tính lãi suất"""
        pass
    
    @abstractmethod
    def get_withdrawal_limit(self):
        """Giới hạn rút tiền"""
        pass
    
    def deposit(self, amount, description=""):
        """Nạp tiền - chung cho tất cả account types"""
        if amount <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0")
        
        self.balance += amount
        transaction = Transaction(TransactionType.DEPOSIT, amount, description)
        self.transactions.append(transaction)
        print(f"Nạp thành công {amount:,} VND. Số dư: {self.balance:,} VND")
        return transaction
    
    def withdraw(self, amount, description=""):
        """Rút tiền - có thể override bởi subclasses"""
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0")
        
        if amount > self.get_withdrawal_limit():
            raise ValueError(f"Vượt quá giới hạn rút tiền: {self.get_withdrawal_limit():,} VND")
        
        if self.balance < amount:
            raise ValueError("Số dư không đủ")
        
        self.balance -= amount
        transaction = Transaction(TransactionType.WITHDRAWAL, amount, description)
        self.transactions.append(transaction)
        print(f"Rút thành công {amount:,} VND. Số dư: {self.balance:,} VND")
        return transaction
    
    def transfer(self, target_account, amount, description=""):
        """Chuyển khoản"""
        if amount <= 0:
            raise ValueError("Số tiền chuyển phải lớn hơn 0")
        
        # Rút tiền từ tài khoản nguồn
        self.withdraw(amount, f"Chuyển đến {target_account.account_number}")
        
        # Nạp tiền vào tài khoản đích
        target_account.deposit(amount, f"Nhận từ {self.account_number}")
        
        # Ghi transaction
        transaction = Transaction(TransactionType.TRANSFER, amount, 
                                f"Chuyển đến {target_account.account_number}: {description}")
        self.transactions.append(transaction)
        
        print(f"Chuyển thành công {amount:,} VND đến {target_account.account_number}")
        return transaction
    
    def get_transaction_history(self, limit=10):
        """Lấy lịch sử giao dịch"""
        return self.transactions[-limit:]
    
    def get_account_info(self):
        """Thông tin tài khoản"""
        return {
            'account_number': self.account_number,
            'customer_name': self.customer_name,
            'account_type': self.get_account_type().value,
            'balance': self.balance,
            'created_date': self.created_date,
            'is_active': self.is_active
        }

class SavingsAccount(Account):
    """Tài khoản tiết kiệm"""
    
    def __init__(self, account_number, customer_name, initial_balance=0):
        super().__init__(account_number, customer_name, initial_balance)
        self.interest_rate = 0.05  # 5% per year
        self.minimum_balance = 50000
    
    def get_account_type(self):
        return AccountType.SAVINGS
    
    def calculate_interest(self):
        """Tính lãi suất hàng tháng"""
        monthly_interest = self.balance * (self.interest_rate / 12)
        return monthly_interest
    
    def get_withdrawal_limit(self):
        return 5000000  # 5 triệu VND per day
    
    def withdraw(self, amount, description=""):
        """Override withdraw để kiểm tra minimum balance"""
        if self.balance - amount < self.minimum_balance:
            raise ValueError(f"Không thể rút. Số dư tối thiểu: {self.minimum_balance:,} VND")
        
        return super().withdraw(amount, description)
    
    def add_monthly_interest(self):
        """Thêm lãi hàng tháng"""
        interest = self.calculate_interest()
        self.deposit(interest, "Lãi suất hàng tháng")
        return interest

class CheckingAccount(Account):
    """Tài khoản thanh toán"""
    
    def __init__(self, account_number, customer_name, initial_balance=0):
        super().__init__(account_number, customer_name, initial_balance)
        self.overdraft_limit = 1000000  # Cho phép thấu chi 1 triệu
        self.monthly_fee = 20000
    
    def get_account_type(self):
        return AccountType.CHECKING
    
    def calculate_interest(self):
        return 0  # Không có lãi suất
    
    def get_withdrawal_limit(self):
        return 10000000  # 10 triệu VND per day
    
    def withdraw(self, amount, description=""):
        """Override withdraw để cho phép overdraft"""
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0")
        
        if amount > self.get_withdrawal_limit():
            raise ValueError(f"Vượt quá giới hạn rút tiền: {self.get_withdrawal_limit():,} VND")
        
        # Cho phép rút âm đến overdraft limit
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError(f"Vượt quá hạn mức thấu chi: {self.overdraft_limit:,} VND")
        
        self.balance -= amount
        transaction = Transaction(TransactionType.WITHDRAWAL, amount, description)
        self.transactions.append(transaction)
        
        status = "Số dư âm" if self.balance < 0 else "Số dư dương"
        print(f"Rút thành công {amount:,} VND. Số dư: {self.balance:,} VND ({status})")
        return transaction
    
    def charge_monthly_fee(self):
        """Tính phí hàng tháng"""
        self.balance -= self.monthly_fee
        transaction = Transaction(TransactionType.WITHDRAWAL, self.monthly_fee, "Phí duy trì tài khoản")
        self.transactions.append(transaction)
        print(f"Đã tính phí hàng tháng: {self.monthly_fee:,} VND")

class BusinessAccount(Account):
    """Tài khoản doanh nghiệp"""
    
    def __init__(self, account_number, customer_name, business_license, initial_balance=0):
        super().__init__(account_number, customer_name, initial_balance)
        self.business_license = business_license
        self.transaction_fee = 5000  # 5k per transaction
        self.interest_rate = 0.02  # 2% per year
    
    def get_account_type(self):
        return AccountType.BUSINESS
    
    def calculate_interest(self):
        monthly_interest = self.balance * (self.interest_rate / 12)
        return monthly_interest
    
    def get_withdrawal_limit(self):
        return 50000000  # 50 triệu VND per day
    
    def withdraw(self, amount, description=""):
        """Override withdraw để tính phí giao dịch"""
        # Rút tiền + phí
        total_amount = amount + self.transaction_fee
        
        if self.balance < total_amount:
            raise ValueError(f"Không đủ số dư (cần {total_amount:,} VND bao gồm phí)")
        
        # Rút tiền
        result = super().withdraw(amount, description)
        
        # Tính phí
        self.balance -= self.transaction_fee
        fee_transaction = Transaction(TransactionType.WITHDRAWAL, self.transaction_fee, "Phí giao dịch")
        self.transactions.append(fee_transaction)
        
        print(f"Phí giao dịch: {self.transaction_fee:,} VND")
        return result

class Bank:
    """Hệ thống ngân hàng"""
    
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.account_counter = 1000
    
    def create_account(self, account_type: AccountType, customer_name, **kwargs):
        """Factory method tạo account"""
        account_number = f"ACC{self.account_counter:06d}"
        self.account_counter += 1
        
        if account_type == AccountType.SAVINGS:
            account = SavingsAccount(account_number, customer_name, 
                                   kwargs.get('initial_balance', 0))
        elif account_type == AccountType.CHECKING:
            account = CheckingAccount(account_number, customer_name, 
                                    kwargs.get('initial_balance', 0))
        elif account_type == AccountType.BUSINESS:
            business_license = kwargs.get('business_license')
            if not business_license:
                raise ValueError("Business account cần business license")
            account = BusinessAccount(account_number, customer_name, business_license,
                                    kwargs.get('initial_balance', 0))
        else:
            raise ValueError(f"Loại tài khoản không hỗ trợ: {account_type}")
        
        self.accounts[account_number] = account
        print(f"Tạo thành công {account_type.value} - {account_number}")
        return account
    
    def get_account(self, account_number):
        """Lấy account theo số"""
        return self.accounts.get(account_number)
    
    def process_monthly_maintenance(self):
        """Xử lý bảo trì hàng tháng"""
        print(f"\n=== BẢO TRÌ HÀNG THÁNG - {self.name} ===")
        
        for account in self.accounts.values():
            print(f"\nXử lý tài khoản {account.account_number}:")
            
            if isinstance(account, SavingsAccount):
                interest = account.add_monthly_interest()
                print(f"Thêm lãi: {interest:,} VND")
            
            elif isinstance(account, CheckingAccount):
                account.charge_monthly_fee()
            
            elif isinstance(account, BusinessAccount):
                interest = account.calculate_interest()
                if interest > 0:
                    account.deposit(interest, "Lãi suất hàng tháng")
    
    def get_bank_summary(self):
        """Tóm tắt ngân hàng"""
        total_accounts = len(self.accounts)
        total_balance = sum(acc.balance for acc in self.accounts.values())
        
        account_types = {}
        for account in self.accounts.values():
            acc_type = account.get_account_type().value
            account_types[acc_type] = account_types.get(acc_type, 0) + 1
        
        print(f"\n=== TÓM TẮT NGÂN HÀNG {self.name} ===")
        print(f"Tổng tài khoản: {total_accounts}")
        print(f"Tổng số dư: {total_balance:,} VND")
        print("Phân loại tài khoản:")
        for acc_type, count in account_types.items():
            print(f"  {acc_type}: {count} tài khoản")

# Sử dụng hệ thống Banking
bank = Bank("Ngân hàng ABC")

# Tạo các loại tài khoản khác nhau
savings = bank.create_account(AccountType.SAVINGS, "Nguyễn Văn An", initial_balance=1000000)
checking = bank.create_account(AccountType.CHECKING, "Trần Thị Bình", initial_balance=500000)
business = bank.create_account(AccountType.BUSINESS, "Công ty XYZ", 
                             business_license="DN123456", initial_balance=5000000)

# Polymorphism - cùng interface, behavior khác nhau
accounts = [savings, checking, business]

print("\n=== THÔNG TIN TÀI KHOẢN ===")
for account in accounts:
    info = account.get_account_info()
    print(f"{info['account_number']}: {info['customer_name']} - {info['account_type']} - {info['balance']:,} VND")

# Test các operations
print("\n=== TEST OPERATIONS ===")
try:
    # Savings account
    savings.deposit(500000, "Nạp tiền lương")
    savings.withdraw(200000, "Rút tiền ATM")
    
    # Checking account (test overdraft)
    checking.withdraw(600000, "Thanh toán hóa đơn")  # Sẽ âm số dư
    
    # Business account (test transaction fee)
    business.withdraw(1000000, "Thanh toán nhà cung cấp")
    
    # Transfer
    savings.transfer(checking, 300000, "Chuyển khoản")
    
except ValueError as e:
    print(f"Lỗi: {e}")

# Monthly maintenance
bank.process_monthly_maintenance()

# Bank summary
bank.get_bank_summary()
```

---

## 7. Best Practices

### 7.1 Khi Nào Sử Dụng Inheritance

```python
# Tốt - Inheritance khi có "is-a" relationship
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):  # Dog IS-A Animal
    def bark(self):
        print("Woof!")

# Không tốt - Inheritance khi chỉ có "has-a" relationship
class Engine:
    def start(self):
        print("Engine starting...")

class Car(Engine):  # Sai! Car HAS-A Engine, không phải IS-A Engine
    pass

# Đúng - Composition thay vì inheritance
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        self.engine.start()
```

### 7.2 Favor Composition Over Inheritance

```python
# Composition approach - linh hoạt hơn
class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class Database:
    def save(self, data):
        print(f"Saving: {data}")

class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")

class UserService:
    def __init__(self):
        self.logger = Logger()
        self.database = Database()
        self.email_service = EmailService()
    
    def create_user(self, user_data):
        self.logger.log(f"Creating user: {user_data['name']}")
        self.database.save(user_data)
        self.email_service.send(f"Welcome {user_data['name']}!")
        self.logger.log("User created successfully")

# Flexible và dễ test
user_service = UserService()
user_service.create_user({"name": "John", "email": "john@example.com"})
```

### 7.3 Proper Use of super()

```python
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor: {name}")
    
    def method(self):
        print(f"Parent method: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Gọi parent constructor
        self.age = age
        print(f"Child constructor: {name}, {age}")
    
    def method(self):
        super().method()  # Gọi parent method trước
        print(f"Child method: {self.name}, {self.age}")

# Sử dụng
child = Child("Alice", 10)
child.method()
```

---

## 8. Tổng Kết

Inheritance và Polymorphism là hai trụ cột quan trọng của OOP:

### Inheritance:
- **Mục đích**: Tái sử dụng code và tạo hierarchy
- **Khi nào dùng**: Quan hệ "is-a"
- **Lưu ý**: Không lạm dụng, favor composition

### Polymorphism:
- **Mục đích**: Cùng interface, behavior khác nhau
- **Lợi ích**: Code linh hoạt, dễ mở rộng
- **Python**: Duck typing hỗ trợ polymorphism tự nhiên

### Method Overriding:
- **super()**: Gọi method của parent class
- **Flexibility**: Mở rộng hoặc thay đổi behavior

### Abstract Classes:
- **Mục đích**: Định nghĩa interface chung
- **Ép buộc**: Subclass phải implement abstract methods

### Design Patterns:
- **Template Method**: Định nghĩa workflow
- **Strategy**: Thay đổi algorithm runtime

**"Inheritance is about reusing code, Polymorphism is about writing flexible code."** 