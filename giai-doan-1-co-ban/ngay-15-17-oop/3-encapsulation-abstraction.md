# Lý Thuyết 3: Encapsulation & Abstraction - Đóng Gói & Trừu Tượng

## Mục Tiêu Học Tập

Sau bài học này, bạn sẽ:
- Nắm vững khái niệm Encapsulation và cách implement
- Hiểu rõ Access Modifiers trong Python
- Thành thạo Properties và Descriptors
- Sử dụng Abstraction để thiết kế hệ thống
- Áp dụng Design Patterns nâng cao

---

## 1. Encapsulation - Đóng Gói

### 1.1 Khái Niệm Encapsulation

**Encapsulation** là việc gói gọn dữ liệu (attributes) và methods thao tác với dữ liệu đó trong một đơn vị (class), đồng thời kiểm soát quyền truy cập.

**Lợi ích:**
- **Data Protection**: Bảo vệ dữ liệu khỏi truy cập trái phép
- **Controlled Access**: Kiểm soát cách dữ liệu được truy cập và thay đổi
- **Maintainability**: Dễ bảo trì và thay đổi implementation
- **Modularity**: Tách biệt interface và implementation

### 1.2 Access Modifiers trong Python

Python sử dụng naming conventions để biểu thị access levels:

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        # Public attribute - truy cập được từ bên ngoài
        self.account_number = account_number
        
        # Protected attribute - chỉ nên truy cập từ class và subclass
        self._balance = initial_balance
        
        # Private attribute - chỉ truy cập từ trong class
        self.__pin = "1234"
        
        # Private method
        self.__validate_pin = lambda pin: pin == self.__pin
    
    # Public method
    def get_balance(self):
        """Public method để lấy balance"""
        return self._balance
    
    # Protected method
    def _update_balance(self, amount):
        """Protected method để update balance"""
        self._balance += amount
    
    # Private method
    def __encrypt_data(self, data):
        """Private method để mã hóa dữ liệu"""
        return f"encrypted_{data}"
    
    def withdraw(self, amount, pin):
        """Public method với validation"""
        if not self.__validate_pin(pin):
            raise ValueError("PIN không đúng")
        
        if amount > self._balance:
            raise ValueError("Số dư không đủ")
        
        self._update_balance(-amount)
        return f"Rút thành công {amount:,} VND"
    
    def deposit(self, amount):
        """Public method để nạp tiền"""
        if amount <= 0:
            raise ValueError("Số tiền phải dương")
        
        self._update_balance(amount)
        return f"Nạp thành công {amount:,} VND"

# Sử dụng
account = BankAccount("123456", 1000000)

# Public access - OK
print(f"Số tài khoản: {account.account_number}")
print(f"Số dư: {account.get_balance():,} VND")

# Protected access - Không nên làm nhưng có thể
print(f"Protected balance: {account._balance}")

# Private access - Sẽ gây lỗi
try:
    print(account.__pin)  # AttributeError
except AttributeError as e:
    print(f"Lỗi: {e}")

# Name mangling - Python thay đổi tên private attributes
print(f"Actual private attribute: {account._BankAccount__pin}")
```

### 1.3 Properties - Elegant Encapsulation

Properties cho phép tạo "computed attributes" với getter, setter, và deleter:

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter cho celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter cho celsius với validation"""
        if value < -273.15:
            raise ValueError("Nhiệt độ không thể thấp hơn -273.15°C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property cho fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter cho fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Computed property cho kelvin"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Setter cho kelvin"""
        self.celsius = value - 273.15
    
    def __str__(self):
        return f"{self._celsius}°C = {self.fahrenheit}°F = {self.kelvin}K"

# Sử dụng properties
temp = Temperature(25)
print(temp)  # 25°C = 77.0°F = 298.15K

# Thay đổi qua different units
temp.fahrenheit = 100
print(temp)  # 37.77777777777778°C = 100°F = 310.9277777777778K

temp.kelvin = 300
print(temp)  # 26.850000000000023°C = 80.33000000000004°F = 300K

# Validation hoạt động
try:
    temp.celsius = -300  # ValueError
except ValueError as e:
    print(f"Lỗi: {e}")
```

### 1.4 Descriptors - Advanced Encapsulation

Descriptors cho phép tùy chỉnh cách attributes được truy cập:

```python
class ValidatedAttribute:
    """Descriptor cho validated attributes"""
    
    def __init__(self, validator=None, default=None):
        self.validator = validator
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)
    
    def __set__(self, instance, value):
        if self.validator:
            self.validator(value)
        setattr(instance, self.name, value)

class PositiveNumber:
    """Validator cho số dương"""
    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Phải là số")
        if value <= 0:
            raise ValueError("Phải là số dương")

class NonEmptyString:
    """Validator cho string không rỗng"""
    def __call__(self, value):
        if not isinstance(value, str):
            raise TypeError("Phải là chuỗi")
        if not value.strip():
            raise ValueError("Chuỗi không được rỗng")

class Product:
    """Class sử dụng descriptors"""
    
    name = ValidatedAttribute(NonEmptyString())
    price = ValidatedAttribute(PositiveNumber())
    quantity = ValidatedAttribute(PositiveNumber())
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @property
    def total_value(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name}: {self.price:,} VND x {self.quantity} = {self.total_value:,} VND"

# Sử dụng descriptors
try:
    product = Product("Laptop", 15000000, 5)
    print(product)
    
    # Validation tự động
    product.price = -1000  # ValueError
except ValueError as e:
    print(f"Lỗi: {e}")

try:
    product.name = ""  # ValueError
except ValueError as e:
    print(f"Lỗi: {e}")
```

---

## 2. Abstraction - Trừu Tượng

### 2.1 Khái Niệm Abstraction

**Abstraction** là việc ẩn đi các chi tiết implementation phức tạp và chỉ expose những interface cần thiết.

**Lợi ích:**
- **Simplicity**: Đơn giản hóa interface
- **Flexibility**: Dễ thay đổi implementation
- **Reusability**: Tái sử dụng code
- **Maintainability**: Dễ bảo trì

### 2.2 Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod, abstractproperty
from typing import List, Optional

class DatabaseConnection(ABC):
    """Abstract base class cho database connections"""
    
    @abstractmethod
    def connect(self):
        """Kết nối đến database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Ngắt kết nối database"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str, params: Optional[tuple] = None):
        """Thực thi query"""
        pass
    
    @abstractmethod
    def execute_many(self, query: str, params_list: List[tuple]):
        """Thực thi nhiều queries"""
        pass
    
    @abstractproperty
    def is_connected(self):
        """Kiểm tra trạng thái kết nối"""
        pass
    
    # Concrete method có thể được override
    def execute_transaction(self, queries: List[tuple]):
        """Thực thi transaction"""
        try:
            self.begin_transaction()
            for query, params in queries:
                self.execute_query(query, params)
            self.commit_transaction()
        except Exception as e:
            self.rollback_transaction()
            raise e
    
    def begin_transaction(self):
        """Bắt đầu transaction"""
        self.execute_query("BEGIN")
    
    def commit_transaction(self):
        """Commit transaction"""
        self.execute_query("COMMIT")
    
    def rollback_transaction(self):
        """Rollback transaction"""
        self.execute_query("ROLLBACK")

class MySQLConnection(DatabaseConnection):
    """MySQL implementation"""
    
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self._connection = None
        self._connected = False
    
    def connect(self):
        """Implement MySQL connection"""
        print(f"Connecting to MySQL: {self.host}/{self.database}")
        # Giả lập kết nối
        self._connected = True
        print("MySQL connected successfully")
    
    def disconnect(self):
        """Implement MySQL disconnection"""
        if self._connected:
            print("Disconnecting from MySQL")
            self._connected = False
    
    def execute_query(self, query: str, params: Optional[tuple] = None):
        """Implement MySQL query execution"""
        if not self._connected:
            raise RuntimeError("Not connected to database")
        
        formatted_query = query
        if params:
            formatted_query = query % params
        
        print(f"MySQL Query: {formatted_query}")
        return f"MySQL Result for: {formatted_query}"
    
    def execute_many(self, query: str, params_list: List[tuple]):
        """Implement MySQL batch execution"""
        results = []
        for params in params_list:
            result = self.execute_query(query, params)
            results.append(result)
        return results
    
    @property
    def is_connected(self):
        return self._connected

class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL implementation"""
    
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self._connected = False
    
    def connect(self):
        print(f"Connecting to PostgreSQL: {self.host}/{self.database}")
        self._connected = True
        print("PostgreSQL connected successfully")
    
    def disconnect(self):
        if self._connected:
            print("Disconnecting from PostgreSQL")
            self._connected = False
    
    def execute_query(self, query: str, params: Optional[tuple] = None):
        if not self._connected:
            raise RuntimeError("Not connected to database")
        
        formatted_query = query
        if params:
            formatted_query = query.replace('?', '%s') % params
        
        print(f"PostgreSQL Query: {formatted_query}")
        return f"PostgreSQL Result for: {formatted_query}"
    
    def execute_many(self, query: str, params_list: List[tuple]):
        results = []
        for params in params_list:
            result = self.execute_query(query, params)
            results.append(result)
        return results
    
    @property
    def is_connected(self):
        return self._connected

# Database Manager sử dụng abstraction
class DatabaseManager:
    """High-level database manager"""
    
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
    
    def setup_database(self):
        """Setup database connection"""
        if not self.connection.is_connected:
            self.connection.connect()
    
    def cleanup_database(self):
        """Cleanup database connection"""
        if self.connection.is_connected:
            self.connection.disconnect()
    
    def create_user(self, username: str, email: str):
        """Create user - abstracted from specific database"""
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        return self.connection.execute_query(query, (username, email))
    
    def get_user(self, user_id: int):
        """Get user by ID"""
        query = "SELECT * FROM users WHERE id = ?"
        return self.connection.execute_query(query, (user_id,))
    
    def create_users_batch(self, users: List[tuple]):
        """Create multiple users"""
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        return self.connection.execute_many(query, users)

# Sử dụng abstraction - code giống nhau cho different databases
def test_database_operations(db_manager: DatabaseManager):
    """Test function works with any database"""
    db_manager.setup_database()
    
    # Create single user
    db_manager.create_user("john_doe", "john@example.com")
    
    # Get user
    db_manager.get_user(1)
    
    # Create batch users
    users = [
        ("alice", "alice@example.com"),
        ("bob", "bob@example.com"),
        ("charlie", "charlie@example.com")
    ]
    db_manager.create_users_batch(users)
    
    db_manager.cleanup_database()

# Test với different databases
print("=== Testing with MySQL ===")
mysql_conn = MySQLConnection("localhost", "myapp", "user", "pass")
mysql_manager = DatabaseManager(mysql_conn)
test_database_operations(mysql_manager)

print("\n=== Testing with PostgreSQL ===")
postgres_conn = PostgreSQLConnection("localhost", "myapp", "user", "pass")
postgres_manager = DatabaseManager(postgres_conn)
test_database_operations(postgres_manager)
```

### 2.3 Interface Segregation

```python
from abc import ABC, abstractmethod

# Bad - Fat interface
class BadWorker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

# Good - Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class Robot(Workable):
    def work(self):
        print("Robot working")
    
    # Robot không cần eat() và sleep()

# Factory pattern với abstraction
class WorkerFactory:
    @staticmethod
    def create_worker(worker_type: str):
        if worker_type == "human":
            return Human()
        elif worker_type == "robot":
            return Robot()
        else:
            raise ValueError(f"Unknown worker type: {worker_type}")

# Polymorphism với abstraction
def assign_work(worker: Workable):
    worker.work()

# Sử dụng
workers = [
    WorkerFactory.create_worker("human"),
    WorkerFactory.create_worker("robot")
]

for worker in workers:
    assign_work(worker)
```

---

## 3. Design Patterns Nâng Cao

### 3.1 Singleton Pattern

```python
class DatabaseConnectionPool:
    """Singleton pattern cho connection pool"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.connections = []
            self.max_connections = 10
            self.current_connections = 0
            self._initialized = True
    
    def get_connection(self):
        if self.current_connections < self.max_connections:
            connection = f"Connection_{self.current_connections}"
            self.connections.append(connection)
            self.current_connections += 1
            print(f"Created new connection: {connection}")
            return connection
        else:
            print("Max connections reached, reusing existing connection")
            return self.connections[0]
    
    def release_connection(self, connection):
        if connection in self.connections:
            print(f"Released connection: {connection}")
        else:
            print("Connection not found in pool")
    
    def get_stats(self):
        return {
            'total_connections': len(self.connections),
            'max_connections': self.max_connections,
            'current_connections': self.current_connections
        }

# Test Singleton
pool1 = DatabaseConnectionPool()
pool2 = DatabaseConnectionPool()

print(f"Same instance: {pool1 is pool2}")  # True

conn1 = pool1.get_connection()
conn2 = pool2.get_connection()

print(pool1.get_stats())
```

### 3.2 Factory Pattern

```python
from abc import ABC, abstractmethod
from enum import Enum

class NotificationType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    SLACK = "slack"

class Notification(ABC):
    """Abstract notification interface"""
    
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass
    
    @abstractmethod
    def get_delivery_status(self, notification_id: str):
        pass

class EmailNotification(Notification):
    def __init__(self, smtp_server: str, port: int):
        self.smtp_server = smtp_server
        self.port = port
    
    def send(self, recipient: str, message: str):
        notification_id = f"email_{hash(recipient + message)}"
        print(f"Sending email to {recipient} via {self.smtp_server}:{self.port}")
        print(f"Message: {message}")
        print(f"Notification ID: {notification_id}")
        return notification_id
    
    def get_delivery_status(self, notification_id: str):
        return f"Email {notification_id}: Delivered"

class SMSNotification(Notification):
    def __init__(self, api_key: str, provider: str):
        self.api_key = api_key
        self.provider = provider
    
    def send(self, recipient: str, message: str):
        notification_id = f"sms_{hash(recipient + message)}"
        print(f"Sending SMS to {recipient} via {self.provider}")
        print(f"Message: {message}")
        print(f"Notification ID: {notification_id}")
        return notification_id
    
    def get_delivery_status(self, notification_id: str):
        return f"SMS {notification_id}: Delivered"

class PushNotification(Notification):
    def __init__(self, app_id: str, api_key: str):
        self.app_id = app_id
        self.api_key = api_key
    
    def send(self, recipient: str, message: str):
        notification_id = f"push_{hash(recipient + message)}"
        print(f"Sending push notification to {recipient} for app {self.app_id}")
        print(f"Message: {message}")
        print(f"Notification ID: {notification_id}")
        return notification_id
    
    def get_delivery_status(self, notification_id: str):
        return f"Push {notification_id}: Delivered"

class SlackNotification(Notification):
    def __init__(self, webhook_url: str, channel: str):
        self.webhook_url = webhook_url
        self.channel = channel
    
    def send(self, recipient: str, message: str):
        notification_id = f"slack_{hash(recipient + message)}"
        print(f"Sending Slack message to {self.channel}")
        print(f"Message: {message}")
        print(f"Notification ID: {notification_id}")
        return notification_id
    
    def get_delivery_status(self, notification_id: str):
        return f"Slack {notification_id}: Delivered"

class NotificationFactory:
    """Factory for creating notifications"""
    
    @staticmethod
    def create_notification(notification_type: NotificationType, **config) -> Notification:
        if notification_type == NotificationType.EMAIL:
            return EmailNotification(
                smtp_server=config.get('smtp_server', 'localhost'),
                port=config.get('port', 587)
            )
        elif notification_type == NotificationType.SMS:
            return SMSNotification(
                api_key=config.get('api_key', 'default_key'),
                provider=config.get('provider', 'default_provider')
            )
        elif notification_type == NotificationType.PUSH:
            return PushNotification(
                app_id=config.get('app_id', 'default_app'),
                api_key=config.get('api_key', 'default_key')
            )
        elif notification_type == NotificationType.SLACK:
            return SlackNotification(
                webhook_url=config.get('webhook_url', 'default_webhook'),
                channel=config.get('channel', '#general')
            )
        else:
            raise ValueError(f"Unsupported notification type: {notification_type}")

class NotificationService:
    """Service sử dụng factory pattern"""
    
    def __init__(self):
        self.notifications = {}
    
    def register_notification(self, name: str, notification_type: NotificationType, **config):
        """Register a notification channel"""
        notification = NotificationFactory.create_notification(notification_type, **config)
        self.notifications[name] = notification
        print(f"Registered {notification_type.value} notification as '{name}'")
    
    def send_notification(self, channel_name: str, recipient: str, message: str):
        """Send notification through specified channel"""
        if channel_name not in self.notifications:
            raise ValueError(f"Notification channel '{channel_name}' not found")
        
        notification = self.notifications[channel_name]
        return notification.send(recipient, message)
    
    def broadcast_message(self, message: str, recipients: dict):
        """Broadcast message to multiple channels"""
        results = {}
        for channel_name, recipient in recipients.items():
            if channel_name in self.notifications:
                notification_id = self.send_notification(channel_name, recipient, message)
                results[channel_name] = notification_id
        return results

# Sử dụng Factory Pattern
service = NotificationService()

# Register different notification channels
service.register_notification("primary_email", NotificationType.EMAIL, 
                             smtp_server="smtp.gmail.com", port=587)
service.register_notification("alert_sms", NotificationType.SMS, 
                             api_key="sms_key_123", provider="Twilio")
service.register_notification("mobile_push", NotificationType.PUSH, 
                             app_id="myapp_123", api_key="push_key_456")
service.register_notification("team_slack", NotificationType.SLACK, 
                             webhook_url="https://hooks.slack.com/...", channel="#alerts")

# Send notifications
message = "System maintenance scheduled for tonight"
recipients = {
    "primary_email": "admin@company.com",
    "alert_sms": "+1234567890",
    "mobile_push": "user_device_123",
    "team_slack": "#alerts"
}

results = service.broadcast_message(message, recipients)
print(f"\nBroadcast results: {results}")
```

### 3.3 Observer Pattern

```python
from abc import ABC, abstractmethod
from typing import List, Any
from datetime import datetime

class Observer(ABC):
    """Abstract observer interface"""
    
    @abstractmethod
    def update(self, subject: 'Subject', event_type: str, data: Any):
        pass

class Subject(ABC):
    """Abstract subject interface"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """Attach an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_type: str, data: Any = None):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self, event_type, data)

class StockPrice(Subject):
    """Stock price subject"""
    
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self.symbol = symbol
        self._price = price
        self.history = [(datetime.now(), price)]
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        if new_price != self._price:
            old_price = self._price
            self._price = new_price
            self.history.append((datetime.now(), new_price))
            
            # Notify observers
            self.notify("price_change", {
                'symbol': self.symbol,
                'old_price': old_price,
                'new_price': new_price,
                'change': new_price - old_price,
                'change_percent': ((new_price - old_price) / old_price) * 100
            })

class EmailAlert(Observer):
    """Email alert observer"""
    
    def __init__(self, email: str, threshold_percent: float = 5.0):
        self.email = email
        self.threshold_percent = threshold_percent
    
    def update(self, subject: Subject, event_type: str, data: Any):
        if event_type == "price_change":
            change_percent = abs(data['change_percent'])
            if change_percent >= self.threshold_percent:
                direction = "increased" if data['change'] > 0 else "decreased"
                print(f"📧 EMAIL ALERT to {self.email}:")
                print(f"   {data['symbol']} {direction} by {change_percent:.2f}%")
                print(f"   Price: ${data['old_price']:.2f} → ${data['new_price']:.2f}")

class SMSAlert(Observer):
    """SMS alert observer"""
    
    def __init__(self, phone: str, threshold_percent: float = 10.0):
        self.phone = phone
        self.threshold_percent = threshold_percent
    
    def update(self, subject: Subject, event_type: str, data: Any):
        if event_type == "price_change":
            change_percent = abs(data['change_percent'])
            if change_percent >= self.threshold_percent:
                direction = "📈" if data['change'] > 0 else "📉"
                print(f"📱 SMS ALERT to {self.phone}:")
                print(f"   {direction} {data['symbol']}: ${data['new_price']:.2f} ({data['change_percent']:+.1f}%)")

class TradingBot(Observer):
    """Trading bot observer"""
    
    def __init__(self, name: str, buy_threshold: float = -5.0, sell_threshold: float = 5.0):
        self.name = name
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.positions = {}
    
    def update(self, subject: Subject, event_type: str, data: Any):
        if event_type == "price_change":
            symbol = data['symbol']
            change_percent = data['change_percent']
            price = data['new_price']
            
            if change_percent <= self.buy_threshold:
                # Buy signal
                if symbol not in self.positions:
                    self.positions[symbol] = {'quantity': 100, 'avg_price': price}
                    print(f"🤖 {self.name} BOT: BUY 100 shares of {symbol} at ${price:.2f}")
                else:
                    # Add to position
                    current_qty = self.positions[symbol]['quantity']
                    current_avg = self.positions[symbol]['avg_price']
                    new_qty = current_qty + 100
                    new_avg = ((current_avg * current_qty) + (price * 100)) / new_qty
                    
                    self.positions[symbol] = {'quantity': new_qty, 'avg_price': new_avg}
                    print(f"🤖 {self.name} BOT: ADD 100 shares of {symbol} at ${price:.2f}")
            
            elif change_percent >= self.sell_threshold:
                # Sell signal
                if symbol in self.positions and self.positions[symbol]['quantity'] > 0:
                    qty_to_sell = min(100, self.positions[symbol]['quantity'])
                    self.positions[symbol]['quantity'] -= qty_to_sell
                    
                    if self.positions[symbol]['quantity'] == 0:
                        del self.positions[symbol]
                    
                    print(f"🤖 {self.name} BOT: SELL {qty_to_sell} shares of {symbol} at ${price:.2f}")

class PriceLogger(Observer):
    """Price logger observer"""
    
    def __init__(self, log_file: str = "price_log.txt"):
        self.log_file = log_file
    
    def update(self, subject: Subject, event_type: str, data: Any):
        if event_type == "price_change":
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {data['symbol']}: ${data['new_price']:.2f} ({data['change_percent']:+.2f}%)"
            print(f"📝 LOGGED: {log_entry}")

# Sử dụng Observer Pattern
# Tạo stock price subject
apple_stock = StockPrice("AAPL", 150.00)

# Tạo observers
email_alert = EmailAlert("investor@email.com", threshold_percent=3.0)
sms_alert = SMSAlert("+1234567890", threshold_percent=7.0)
trading_bot = TradingBot("AlgoBot", buy_threshold=-4.0, sell_threshold=6.0)
price_logger = PriceLogger()

# Attach observers
apple_stock.attach(email_alert)
apple_stock.attach(sms_alert)
apple_stock.attach(trading_bot)
apple_stock.attach(price_logger)

print("=== Stock Price Monitoring Started ===")

# Simulate price changes
price_changes = [145.00, 142.50, 148.00, 159.00, 155.50, 162.00]

for new_price in price_changes:
    print(f"\n--- Price Update: ${new_price:.2f} ---")
    apple_stock.price = new_price
    print(f"Current bot positions: {trading_bot.positions}")
```

---

## 4. Ví Dụ Thực Tế: Enterprise Security System

```python
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from enum import Enum
import hashlib
import secrets

class Permission(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"

class Role(Enum):
    GUEST = "guest"
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"

class SecurityLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class AuthenticationResult:
    def __init__(self, success: bool, user_id: Optional[str] = None, 
                 token: Optional[str] = None, message: str = ""):
        self.success = success
        self.user_id = user_id
        self.token = token
        self.message = message
        self.timestamp = datetime.now()

class AuthorizationResult:
    def __init__(self, allowed: bool, reason: str = ""):
        self.allowed = allowed
        self.reason = reason
        self.timestamp = datetime.now()

class SecureData:
    """Encapsulated secure data with controlled access"""
    
    def __init__(self, data: str, security_level: SecurityLevel):
        self.__data = data
        self.__security_level = security_level
        self.__access_log = []
        self.__created_at = datetime.now()
        self.__last_accessed = None
    
    def access_data(self, user_id: str, required_permission: Permission) -> Optional[str]:
        """Controlled access to data"""
        access_record = {
            'user_id': user_id,
            'permission': required_permission,
            'timestamp': datetime.now(),
            'success': False
        }
        
        # Log access attempt
        self.__access_log.append(access_record)
        
        # Check if access is allowed (simplified)
        if self.__security_level == SecurityLevel.CRITICAL and required_permission != Permission.ADMIN:
            access_record['reason'] = "Critical data requires admin permission"
            return None
        
        # Grant access
        access_record['success'] = True
        self.__last_accessed = datetime.now()
        return self.__data
    
    @property
    def security_level(self) -> SecurityLevel:
        return self.__security_level
    
    @property
    def access_log(self) -> List[Dict]:
        return self.__access_log.copy()
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at

class User:
    """Encapsulated user with secure password handling"""
    
    def __init__(self, user_id: str, username: str, email: str, role: Role):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role
        self.__password_hash = None
        self.__salt = None
        self.__created_at = datetime.now()
        self.__last_login = None
        self.__failed_login_attempts = 0
        self.__locked_until = None
    
    def set_password(self, password: str):
        """Secure password setting"""
        self.__salt = secrets.token_hex(32)
        self.__password_hash = self.__hash_password(password, self.__salt)
    
    def verify_password(self, password: str) -> bool:
        """Secure password verification"""
        if self.__password_hash is None:
            return False
        
        if self.is_locked():
            return False
        
        is_valid = self.__password_hash == self.__hash_password(password, self.__salt)
        
        if is_valid:
            self.__failed_login_attempts = 0
            self.__last_login = datetime.now()
        else:
            self.__failed_login_attempts += 1
            if self.__failed_login_attempts >= 3:
                self.__locked_until = datetime.now() + timedelta(minutes=15)
        
        return is_valid
    
    def is_locked(self) -> bool:
        """Check if account is locked"""
        if self.__locked_until is None:
            return False
        return datetime.now() < self.__locked_until
    
    def unlock_account(self):
        """Unlock account (admin function)"""
        self.__locked_until = None
        self.__failed_login_attempts = 0
    
    def get_permissions(self) -> Set[Permission]:
        """Get user permissions based on role"""
        role_permissions = {
            Role.GUEST: {Permission.READ},
            Role.USER: {Permission.READ, Permission.WRITE},
            Role.MODERATOR: {Permission.READ, Permission.WRITE, Permission.DELETE},
            Role.ADMIN: {Permission.READ, Permission.WRITE, Permission.DELETE, Permission.ADMIN}
        }
        return role_permissions.get(self.role, set())
    
    @staticmethod
    def __hash_password(password: str, salt: str) -> str:
        """Private method for password hashing"""
        return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()
    
    @property
    def last_login(self) -> Optional[datetime]:
        return self.__last_login
    
    @property
    def failed_attempts(self) -> int:
        return self.__failed_login_attempts

class SessionManager:
    """Secure session management"""
    
    def __init__(self, session_timeout: int = 3600):  # 1 hour default
        self.__sessions: Dict[str, Dict] = {}
        self.__session_timeout = session_timeout
    
    def create_session(self, user_id: str) -> str:
        """Create secure session"""
        token = secrets.token_urlsafe(32)
        self.__sessions[token] = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'last_activity': datetime.now()
        }
        return token
    
    def validate_session(self, token: str) -> Optional[str]:
        """Validate session and return user_id"""
        if token not in self.__sessions:
            return None
        
        session = self.__sessions[token]
        now = datetime.now()
        
        # Check timeout
        if (now - session['last_activity']).seconds > self.__session_timeout:
            self.destroy_session(token)
            return None
        
        # Update last activity
        session['last_activity'] = now
        return session['user_id']
    
    def destroy_session(self, token: str):
        """Destroy session"""
        if token in self.__sessions:
            del self.__sessions[token]
    
    def get_active_sessions(self) -> int:
        """Get number of active sessions"""
        return len(self.__sessions)

class SecurityAuditLog:
    """Secure audit logging"""
    
    def __init__(self):
        self.__logs: List[Dict] = []
    
    def log_event(self, event_type: str, user_id: str, details: Dict):
        """Log security event"""
        log_entry = {
            'timestamp': datetime.now(),
            'event_type': event_type,
            'user_id': user_id,
            'details': details.copy(),
            'log_id': secrets.token_hex(16)
        }
        self.__logs.append(log_entry)
    
    def get_logs(self, user_id: Optional[str] = None, 
                 event_type: Optional[str] = None) -> List[Dict]:
        """Get filtered logs"""
        filtered_logs = self.__logs
        
        if user_id:
            filtered_logs = [log for log in filtered_logs if log['user_id'] == user_id]
        
        if event_type:
            filtered_logs = [log for log in filtered_logs if log['event_type'] == event_type]
        
        return filtered_logs.copy()

class SecurityManager:
    """Main security manager - facade pattern"""
    
    def __init__(self):
        self.__users: Dict[str, User] = {}
        self.__session_manager = SessionManager()
        self.__audit_log = SecurityAuditLog()
        self.__secure_data: Dict[str, SecureData] = {}
    
    def register_user(self, username: str, email: str, password: str, role: Role = Role.USER) -> str:
        """Register new user"""
        user_id = secrets.token_hex(16)
        
        # Check if username already exists
        for user in self.__users.values():
            if user.username == username:
                raise ValueError("Username already exists")
        
        user = User(user_id, username, email, role)
        user.set_password(password)
        self.__users[user_id] = user
        
        self.__audit_log.log_event("USER_REGISTERED", user_id, {
            'username': username,
            'email': email,
            'role': role.value
        })
        
        return user_id
    
    def authenticate(self, username: str, password: str) -> AuthenticationResult:
        """Authenticate user"""
        # Find user by username
        user = None
        for u in self.__users.values():
            if u.username == username:
                user = u
                break
        
        if not user:
            self.__audit_log.log_event("AUTH_FAILED", "unknown", {
                'username': username,
                'reason': 'User not found'
            })
            return AuthenticationResult(False, message="Invalid credentials")
        
        if user.is_locked():
            self.__audit_log.log_event("AUTH_FAILED", user.user_id, {
                'username': username,
                'reason': 'Account locked'
            })
            return AuthenticationResult(False, message="Account locked")
        
        if not user.verify_password(password):
            self.__audit_log.log_event("AUTH_FAILED", user.user_id, {
                'username': username,
                'reason': 'Invalid password'
            })
            return AuthenticationResult(False, message="Invalid credentials")
        
        # Create session
        token = self.__session_manager.create_session(user.user_id)
        
        self.__audit_log.log_event("AUTH_SUCCESS", user.user_id, {
            'username': username,
            'token': token[:8] + "..."  # Log partial token
        })
        
        return AuthenticationResult(True, user.user_id, token, "Authentication successful")
    
    def authorize(self, token: str, required_permission: Permission) -> AuthorizationResult:
        """Authorize user action"""
        user_id = self.__session_manager.validate_session(token)
        
        if not user_id:
            self.__audit_log.log_event("AUTHZ_FAILED", "unknown", {
                'token': token[:8] + "...",
                'reason': 'Invalid session'
            })
            return AuthorizationResult(False, "Invalid session")
        
        user = self.__users[user_id]
        user_permissions = user.get_permissions()
        
        if required_permission not in user_permissions:
            self.__audit_log.log_event("AUTHZ_FAILED", user_id, {
                'required_permission': required_permission.value,
                'user_permissions': [p.value for p in user_permissions]
            })
            return AuthorizationResult(False, "Insufficient permissions")
        
        self.__audit_log.log_event("AUTHZ_SUCCESS", user_id, {
            'permission': required_permission.value
        })
        
        return AuthorizationResult(True, "Authorization successful")
    
    def store_secure_data(self, data: str, security_level: SecurityLevel) -> str:
        """Store secure data"""
        data_id = secrets.token_hex(16)
        secure_data = SecureData(data, security_level)
        self.__secure_data[data_id] = secure_data
        return data_id
    
    def access_secure_data(self, token: str, data_id: str, 
                          required_permission: Permission) -> Optional[str]:
        """Access secure data"""
        # Validate session
        user_id = self.__session_manager.validate_session(token)
        if not user_id:
            return None
        
        # Check authorization
        auth_result = self.authorize(token, required_permission)
        if not auth_result.allowed:
            return None
        
        # Access data
        if data_id not in self.__secure_data:
            return None
        
        secure_data = self.__secure_data[data_id]
        data = secure_data.access_data(user_id, required_permission)
        
        if data:
            self.__audit_log.log_event("DATA_ACCESS", user_id, {
                'data_id': data_id,
                'permission': required_permission.value,
                'success': True
            })
        
        return data
    
    def logout(self, token: str):
        """Logout user"""
        user_id = self.__session_manager.validate_session(token)
        if user_id:
            self.__audit_log.log_event("LOGOUT", user_id, {
                'token': token[:8] + "..."
            })
        
        self.__session_manager.destroy_session(token)
    
    def get_user_info(self, token: str) -> Optional[Dict]:
        """Get user information"""
        user_id = self.__session_manager.validate_session(token)
        if not user_id:
            return None
        
        user = self.__users[user_id]
        return {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'role': user.role.value,
            'last_login': user.last_login,
            'is_locked': user.is_locked()
        }
    
    def get_security_stats(self) -> Dict:
        """Get security statistics"""
        return {
            'total_users': len(self.__users),
            'active_sessions': self.__session_manager.get_active_sessions(),
            'total_audit_logs': len(self.__audit_log.get_logs()),
            'secure_data_items': len(self.__secure_data)
        }

# Sử dụng Enterprise Security System
print("=== Enterprise Security System Demo ===")

# Initialize security manager
security = SecurityManager()

# Register users
admin_id = security.register_user("admin", "admin@company.com", "admin123", Role.ADMIN)
user_id = security.register_user("john_doe", "john@company.com", "user123", Role.USER)
guest_id = security.register_user("guest", "guest@company.com", "guest123", Role.GUEST)

print(f"Registered users: Admin({admin_id[:8]}...), User({user_id[:8]}...), Guest({guest_id[:8]}...)")

# Authenticate users
admin_auth = security.authenticate("admin", "admin123")
user_auth = security.authenticate("john_doe", "user123")
guest_auth = security.authenticate("guest", "guest123")

print(f"Admin auth: {admin_auth.success}")
print(f"User auth: {user_auth.success}")
print(f"Guest auth: {guest_auth.success}")

# Store secure data
data_id_1 = security.store_secure_data("Public information", SecurityLevel.LOW)
data_id_2 = security.store_secure_data("Confidential data", SecurityLevel.HIGH)
data_id_3 = security.store_secure_data("Top secret", SecurityLevel.CRITICAL)

print(f"Stored secure data: {data_id_1[:8]}..., {data_id_2[:8]}..., {data_id_3[:8]}...")

# Test access control
print("\n=== Access Control Tests ===")

# Admin can access everything
admin_token = admin_auth.token
print(f"Admin accessing public data: {security.access_secure_data(admin_token, data_id_1, Permission.READ) is not None}")
print(f"Admin accessing confidential data: {security.access_secure_data(admin_token, data_id_2, Permission.READ) is not None}")
print(f"Admin accessing top secret data: {security.access_secure_data(admin_token, data_id_3, Permission.ADMIN) is not None}")

# User has limited access
user_token = user_auth.token
print(f"User accessing public data: {security.access_secure_data(user_token, data_id_1, Permission.READ) is not None}")
print(f"User accessing confidential data: {security.access_secure_data(user_token, data_id_2, Permission.READ) is not None}")
print(f"User accessing top secret data: {security.access_secure_data(user_token, data_id_3, Permission.READ) is not None}")

# Guest has very limited access
guest_token = guest_auth.token
print(f"Guest accessing public data: {security.access_secure_data(guest_token, data_id_1, Permission.READ) is not None}")
print(f"Guest accessing confidential data: {security.access_secure_data(guest_token, data_id_2, Permission.READ) is not None}")

# Security statistics
print(f"\n=== Security Statistics ===")
stats = security.get_security_stats()
for key, value in stats.items():
    print(f"{key}: {value}")

# Logout users
security.logout(admin_token)
security.logout(user_token)
security.logout(guest_token)

print("\nAll users logged out successfully")
```

---

## 5. Best Practices

### 5.1 Encapsulation Best Practices

```python
class BankAccount:
    """Example of proper encapsulation"""
    
    def __init__(self, account_number: str, initial_balance: float = 0):
        # Public attributes
        self.account_number = account_number
        self.created_date = datetime.now()
        
        # Protected attributes (for inheritance)
        self._balance = initial_balance
        self._transaction_history = []
        
        # Private attributes (internal use only)
        self.__encryption_key = secrets.token_hex(32)
        self.__is_frozen = False
    
    @property
    def balance(self) -> float:
        """Public interface for balance"""
        return self._balance
    
    @property
    def is_frozen(self) -> bool:
        """Check if account is frozen"""
        return self.__is_frozen
    
    def deposit(self, amount: float, description: str = ""):
        """Public method with validation"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if self.__is_frozen:
            raise RuntimeError("Account is frozen")
        
        self._balance += amount
        self._record_transaction("DEPOSIT", amount, description)
    
    def withdraw(self, amount: float, description: str = ""):
        """Public method with business logic"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if self.__is_frozen:
            raise RuntimeError("Account is frozen")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount, description)
    
    def freeze_account(self):
        """Admin function to freeze account"""
        self.__is_frozen = True
        self._record_transaction("FREEZE", 0, "Account frozen")
    
    def unfreeze_account(self):
        """Admin function to unfreeze account"""
        self.__is_frozen = False
        self._record_transaction("UNFREEZE", 0, "Account unfrozen")
    
    def _record_transaction(self, transaction_type: str, amount: float, description: str):
        """Protected method for inheritance"""
        transaction = {
            'timestamp': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'description': description,
            'balance_after': self._balance
        }
        self._transaction_history.append(transaction)
    
    def get_transaction_history(self, limit: int = 10) -> List[Dict]:
        """Public method to get transaction history"""
        return self._transaction_history[-limit:].copy()
```

### 5.2 Abstraction Best Practices

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Abstract base class demonstrating good abstraction"""
    
    def process_data(self, data):
        """Template method - public interface"""
        try:
            # Validate input
            validated_data = self._validate_data(data)
            
            # Process data (abstract)
            processed_data = self._process_data_impl(validated_data)
            
            # Post-process (hook method)
            result = self._post_process(processed_data)
            
            # Log success
            self._log_success(result)
            
            return result
            
        except Exception as e:
            self._log_error(e)
            raise
    
    def _validate_data(self, data):
        """Protected method with default implementation"""
        if not data:
            raise ValueError("Data cannot be empty")
        return data
    
    @abstractmethod
    def _process_data_impl(self, data):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def _post_process(self, data):
        """Hook method - can be overridden"""
        return data
    
    def _log_success(self, result):
        """Protected method for logging"""
        print(f"Processing successful: {len(str(result))} bytes processed")
    
    def _log_error(self, error):
        """Protected method for error logging"""
        print(f"Processing failed: {error}")

class JSONProcessor(DataProcessor):
    """Concrete implementation"""
    
    def _process_data_impl(self, data):
        import json
        return json.dumps(data)
    
    def _post_process(self, data):
        # Add JSON-specific post-processing
        return data.replace('\n', '').replace(' ', '')

class XMLProcessor(DataProcessor):
    """Another concrete implementation"""
    
    def _process_data_impl(self, data):
        return f"<data>{data}</data>"
    
    def _validate_data(self, data):
        # Override validation for XML-specific rules
        data = super()._validate_data(data)
        if '<' in str(data) or '>' in str(data):
            raise ValueError("Data contains invalid XML characters")
        return data
```

---

## 6. Tổng Kết

Encapsulation và Abstraction là hai nguyên lý quan trọng nhất của OOP:

### Encapsulation:
- **Mục đích**: Bảo vệ và kiểm soát quyền truy cập dữ liệu
- **Công cụ**: Access modifiers, Properties, Descriptors
- **Lợi ích**: Security, Maintainability, Modularity

### Abstraction:
- **Mục đích**: Ẩn complexity, expose simple interface
- **Công cụ**: Abstract classes, Interfaces, Design patterns
- **Lợi ích**: Simplicity, Flexibility, Reusability

### Design Patterns:
- **Singleton**: Đảm bảo chỉ có một instance
- **Factory**: Tạo objects mà không expose creation logic
- **Observer**: Thông báo thay đổi state

### Best Practices:
- **Favor composition over inheritance**
- **Program to interfaces, not implementations**
- **Principle of least privilege**
- **Separation of concerns**

**"Encapsulation is about bundling data and methods, Abstraction is about hiding complexity and exposing simplicity."** 