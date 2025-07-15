# NESTED DICTIONARIES VÀ ADVANCED CONCEPTS - NGÀY 12 🏗️

## 🎯 MỤC TIÊU BÀI HỌC

Sau bài học này, bạn sẽ làm chủ:
- **Nested dictionaries** và multilevel structures
- **Safe navigation** trong complex data
- **Performance optimization** techniques  
- **Advanced applications** trong real-world projects
- **Hash table internals** và best practices

---

## 🏗️ 1. NESTED DICTIONARIES

### Khái niệm và Cấu trúc

```python
# Simple nested structure
company = {
    "name": "Tech Corp",
    "founded": 2020,
    "headquarters": {
        "country": "Vietnam",
        "city": "Ho Chi Minh",
        "address": {
            "street": "123 Nguyen Hue",
            "district": "District 1",
            "postal_code": "700000"
        }
    },
    "departments": {
        "engineering": {
            "head": "John Doe",
            "employees": 25,
            "budget": 500000
        },
        "marketing": {
            "head": "Jane Smith", 
            "employees": 12,
            "budget": 200000
        }
    }
}

# Accessing nested data
print(company["name"])  # Tech Corp
print(company["headquarters"]["city"])  # Ho Chi Minh
print(company["headquarters"]["address"]["street"])  # 123 Nguyen Hue
print(company["departments"]["engineering"]["employees"])  # 25
```

### Creating Nested Structures

```python
# Method 1: Direct construction
user_profile = {
    "personal": {
        "name": "Nguyen Van A",
        "age": 28,
        "contact": {
            "email": "nguyenvana@email.com",
            "phone": "+84-123-456-789"
        }
    },
    "professional": {
        "job_title": "Software Engineer",
        "company": "Tech Startup",
        "skills": ["Python", "JavaScript", "React"],
        "experience": {
            "years": 5,
            "previous_roles": [
                {"title": "Junior Developer", "duration": "2 years"},
                {"title": "Developer", "duration": "3 years"}
            ]
        }
    },
    "preferences": {
        "notifications": True,
        "privacy": {
            "profile_visibility": "public",
            "contact_visibility": "friends_only"
        }
    }
}

# Method 2: Programmatic construction
def create_student_record(name, subjects_grades):
    """Create nested student record"""
    record = {
        "info": {
            "name": name,
            "enrollment_date": "2024-01-15",
            "status": "active"
        },
        "academics": {
            "subjects": {},
            "gpa": 0.0,
            "credits": 0
        },
        "activities": {
            "clubs": [],
            "sports": [],
            "achievements": []
        }
    }
    
    # Add subjects and calculate GPA
    total_points = 0
    total_subjects = len(subjects_grades)
    
    for subject, grade in subjects_grades.items():
        record["academics"]["subjects"][subject] = {
            "grade": grade,
            "credits": 3,  # Default 3 credits
            "semester": "Fall 2024"
        }
        total_points += grade
        record["academics"]["credits"] += 3
    
    record["academics"]["gpa"] = total_points / total_subjects if total_subjects > 0 else 0
    
    return record

# Usage
student = create_student_record("Tran Thi B", {
    "Mathematics": 8.5,
    "Physics": 9.0,
    "Chemistry": 7.5,
    "English": 8.0
})

print(f"Student GPA: {student['academics']['gpa']:.2f}")
```

### Dynamic Nested Updates

```python
def deep_update(base_dict, update_dict):
    """
    Recursively update nested dictionary
    """
    for key, value in update_dict.items():
        if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
            deep_update(base_dict[key], value)
        else:
            base_dict[key] = value
    return base_dict

# Example usage
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "default123"
        }
    },
    "api": {
        "rate_limit": 1000,
        "timeout": 30
    }
}

# Update with new configuration
updates = {
    "database": {
        "host": "production-server",
        "credentials": {
            "password": "secure456"  # Only update password, keep username
        },
        "ssl": True  # Add new field
    },
    "logging": {  # Add completely new section
        "level": "INFO",
        "file": "/var/log/app.log"
    }
}

deep_update(config, updates)
print(config)
# Result: database.host and database.credentials.password updated,
# database.credentials.username preserved, new fields added
```

---

## 🛡️ 2. SAFE NAVIGATION

### Handling Missing Keys

```python
# Sample complex data structure
api_response = {
    "status": "success",
    "data": {
        "user": {
            "id": 123,
            "profile": {
                "name": "John Doe",
                "settings": {
                    "notifications": {
                        "email": True,
                        "push": False
                    }
                }
            }
        }
    }
}

# ❌ Dangerous direct access
try:
    email_notifications = api_response["data"]["user"]["profile"]["settings"]["notifications"]["email"]
    print(email_notifications)  # Works fine
    
    # But this will fail:
    sms_notifications = api_response["data"]["user"]["profile"]["settings"]["notifications"]["sms"]
except KeyError as e:
    print(f"Key not found: {e}")

# ✅ Safe navigation function
def safe_get(dictionary, keys, default=None):
    """
    Safely navigate nested dictionary with list of keys
    """
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

# Usage examples
email_notif = safe_get(api_response, ["data", "user", "profile", "settings", "notifications", "email"])
print(f"Email notifications: {email_notif}")  # True

sms_notif = safe_get(api_response, ["data", "user", "profile", "settings", "notifications", "sms"], False)
print(f"SMS notifications: {sms_notif}")  # False (default)

user_name = safe_get(api_response, ["data", "user", "profile", "name"])
print(f"User name: {user_name}")  # John Doe

missing_field = safe_get(api_response, ["data", "user", "missing", "field"], "Not found")
print(f"Missing field: {missing_field}")  # Not found
```

### Chain of Gets Pattern

```python
def chain_get(obj, *keys, default=None):
    """
    Chain multiple .get() calls safely
    """
    current = obj
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return default
        else:
            return default
    return current

# Alternative implementation with try-except
def safe_chain_access(obj, *keys, default=None):
    """
    Safe chained access with exception handling
    """
    try:
        current = obj
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

# Test both approaches
data = {
    "level1": {
        "level2": {
            "level3": {
                "value": "found it!"
            }
        }
    }
}

# Both return "found it!"
result1 = chain_get(data, "level1", "level2", "level3", "value")
result2 = safe_chain_access(data, "level1", "level2", "level3", "value")

# Both return default for missing path
missing1 = chain_get(data, "level1", "missing", "value", default="not found")
missing2 = safe_chain_access(data, "level1", "missing", "value", default="not found")

print(f"Found: {result1}")      # found it!
print(f"Missing: {missing1}")   # not found
```

### Flattening Nested Dictionaries

```python
def flatten_dict(nested_dict, separator=".", prefix=""):
    """
    Flatten nested dictionary into single level
    """
    flattened = {}
    
    for key, value in nested_dict.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key
        
        if isinstance(value, dict):
            # Recursively flatten nested dictionaries
            flattened.update(flatten_dict(value, separator, new_key))
        else:
            flattened[new_key] = value
    
    return flattened

# Example usage
complex_config = {
    "database": {
        "primary": {
            "host": "db1.example.com",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret"
            }
        },
        "replica": {
            "host": "db2.example.com",
            "port": 5433
        }
    },
    "cache": {
        "redis": {
            "host": "cache.example.com",
            "port": 6379
        }
    },
    "debug": True
}

flattened = flatten_dict(complex_config)
for key, value in flattened.items():
    print(f"{key}: {value}")

# Output:
# database.primary.host: db1.example.com
# database.primary.port: 5432
# database.primary.credentials.username: admin
# database.primary.credentials.password: secret
# database.replica.host: db2.example.com
# database.replica.port: 5433
# cache.redis.host: cache.example.com
# cache.redis.port: 6379
# debug: True

def unflatten_dict(flattened_dict, separator="."):
    """
    Convert flattened dictionary back to nested structure
    """
    nested = {}
    
    for key, value in flattened_dict.items():
        keys = key.split(separator)
        current = nested
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    return nested

# Test round-trip
original = {"a": {"b": {"c": 1}}}
flat = flatten_dict(original)
restored = unflatten_dict(flat)
print(f"Original: {original}")
print(f"Restored: {restored}")
print(f"Equal: {original == restored}")  # True
```

---

## ⚡ 3. PERFORMANCE OPTIMIZATION

### Hash Table Internals

```python
import sys
import time

class HashAnalysis:
    """Analyze hash behavior and performance"""
    
    @staticmethod
    def analyze_hash_distribution(keys):
        """Analyze how keys hash and distribute"""
        hash_values = [hash(key) for key in keys]
        
        print(f"Keys analyzed: {len(keys)}")
        print(f"Unique hashes: {len(set(hash_values))}")
        print(f"Hash collisions: {len(keys) - len(set(hash_values))}")
        
        # Show some hash values
        for i, key in enumerate(keys[:5]):
            print(f"hash('{key}') = {hash(key)}")
    
    @staticmethod
    def measure_performance(dict_size, operation="lookup"):
        """Measure dictionary operation performance"""
        # Create test dictionary
        test_dict = {f"key_{i}": f"value_{i}" for i in range(dict_size)}
        
        # Warm up
        for _ in range(1000):
            _ = "key_500" in test_dict
        
        # Measure lookup time
        start_time = time.time()
        for _ in range(10000):
            _ = "key_500" in test_dict  # Middle key
        lookup_time = time.time() - start_time
        
        print(f"Dict size: {dict_size:,}")
        print(f"10,000 lookups took: {lookup_time:.6f} seconds")
        print(f"Average per lookup: {lookup_time/10000*1_000_000:.3f} microseconds")
        
        return lookup_time

# Test hash distribution
test_keys = ["user_123", "user_456", "user_789", "product_abc", "order_xyz"]
HashAnalysis.analyze_hash_distribution(test_keys)

# Performance comparison across sizes
print("\nPerformance scaling:")
for size in [1000, 10000, 100000, 1000000]:
    HashAnalysis.measure_performance(size)
    print("-" * 40)
```

### Key Design Best Practices

```python
# ✅ Good key design
class OptimalKeys:
    """Examples of well-designed dictionary keys"""
    
    # 1. Use immutable types
    GOOD_KEYS = {
        "string_key": "Simple and readable",
        42: "Integer keys are fast",
        (1, 2, 3): "Tuples work great as composite keys",
        frozenset([1, 2, 3]): "Frozen sets are hashable"
    }
    
    # 2. Consistent naming convention
    USER_DATA = {
        "user_id_123": {"name": "John", "active": True},
        "user_id_456": {"name": "Jane", "active": False},
        "user_id_789": {"name": "Bob", "active": True}
    }
    
    # 3. Composite keys for relationships
    RELATIONSHIPS = {
        ("user_123", "user_456"): "friends",
        ("user_123", "user_789"): "colleagues",
        ("user_456", "user_789"): "siblings"
    }

# ❌ Poor key design
class ProblematicKeys:
    """Examples of problematic dictionary keys"""
    
    # 1. Inconsistent types
    MIXED_TYPES = {
        "string_key": "value1",
        123: "value2",           # Different type
        True: "value3"           # Boolean (careful: True == 1)
    }
    
    # 2. Non-descriptive keys
    UNCLEAR = {
        "a": "What does 'a' represent?",
        "x1": "Unclear meaning",
        "temp": "Temporary what?"
    }
    
    # 3. Very long keys (less efficient)
    VERBOSE = {
        "this_is_an_extremely_long_and_verbose_key_name_that_should_probably_be_shorter": "value"
    }

# Custom hashable class
class CustomKey:
    """Example of custom hashable key class"""
    
    def __init__(self, category, identifier):
        self.category = category
        self.identifier = identifier
    
    def __hash__(self):
        return hash((self.category, self.identifier))
    
    def __eq__(self, other):
        if not isinstance(other, CustomKey):
            return False
        return self.category == other.category and self.identifier == other.identifier
    
    def __repr__(self):
        return f"CustomKey({self.category}, {self.identifier})"

# Usage example
custom_dict = {
    CustomKey("user", 123): {"name": "Alice"},
    CustomKey("product", 456): {"title": "Laptop"},
    CustomKey("order", 789): {"amount": 1500}
}

key = CustomKey("user", 123)
print(custom_dict[key])  # {'name': 'Alice'}
```

### Memory Usage Patterns

```python
import sys
from collections import defaultdict

def analyze_memory_usage():
    """Compare memory usage of different dictionary approaches"""
    
    # Test data
    n = 1000
    
    # 1. Regular dict
    regular_dict = {}
    for i in range(n):
        regular_dict[f"key_{i}"] = f"value_{i}"
    
    # 2. defaultdict
    default_dict = defaultdict(str)
    for i in range(n):
        default_dict[f"key_{i}"] = f"value_{i}"
    
    # 3. Dict with pre-allocated size (Python doesn't directly support this,
    # but we can show the concept)
    pre_allocated = {}
    # In practice, creating all at once can be more memory efficient
    data = {f"key_{i}": f"value_{i}" for i in range(n)}
    
    # 4. Nested structure
    nested = {}
    for i in range(n//10):  # Less items but nested
        nested[f"group_{i}"] = {f"item_{j}": f"value_{i}_{j}" for j in range(10)}
    
    # Memory analysis
    print("Memory Usage Analysis:")
    print(f"Regular dict ({n} items): {sys.getsizeof(regular_dict):,} bytes")
    print(f"defaultdict ({n} items): {sys.getsizeof(default_dict):,} bytes")
    print(f"Pre-allocated dict: {sys.getsizeof(data):,} bytes")
    print(f"Nested structure: {sys.getsizeof(nested):,} bytes")
    
    # Calculate total nested size
    nested_total = sys.getsizeof(nested)
    for key, sub_dict in nested.items():
        nested_total += sys.getsizeof(sub_dict)
        nested_total += sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in sub_dict.items())
    
    print(f"Nested total (including sub-dicts): {nested_total:,} bytes")

analyze_memory_usage()

# Memory-efficient patterns
def memory_efficient_grouping(items):
    """Group items efficiently by avoiding unnecessary intermediate structures"""
    
    # ❌ Memory inefficient - creates many intermediate lists
    def inefficient_grouping(items):
        groups = {}
        for item in items:
            category = item.get("category", "unknown")
            if category not in groups:
                groups[category] = []
            groups[category].append(item)
        return groups
    
    # ✅ More memory efficient - use generator when possible
    def efficient_grouping(items):
        groups = defaultdict(list)
        for item in items:
            groups[item.get("category", "unknown")].append(item)
        return dict(groups)
    
    return efficient_grouping(items)

# Test data
test_items = [
    {"name": "item1", "category": "A"},
    {"name": "item2", "category": "B"},
    {"name": "item3", "category": "A"},
    {"name": "item4", "category": "C"}
]

grouped = memory_efficient_grouping(test_items)
print("\nGrouped items:", grouped)
```

---

## 🚀 4. ADVANCED APPLICATIONS

### Caching and Memoization

```python
import functools
import time
from collections import OrderedDict

class LRUCache:
    """Least Recently Used cache implementation using OrderedDict"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # Move to end (mark as recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def display(self):
        return list(self.cache.items())

# Usage example
lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print("After adding a,b,c:", lru.display())  # [('a', 1), ('b', 2), ('c', 3)]

lru.get("a")  # Access 'a'
print("After accessing 'a':", lru.display())  # [('b', 2), ('c', 3), ('a', 1)]

lru.put("d", 4)  # This will evict 'b'
print("After adding 'd':", lru.display())  # [('c', 3), ('a', 1), ('d', 4)]

# Advanced memoization with expiry
class TimedCache:
    """Cache with time-based expiry"""
    
    def __init__(self, ttl_seconds=300):  # 5 minutes default
        self.ttl = ttl_seconds
        self.cache = {}
        self.timestamps = {}
    
    def is_expired(self, key):
        if key not in self.timestamps:
            return True
        return time.time() - self.timestamps[key] > self.ttl
    
    def get(self, key):
        if key in self.cache and not self.is_expired(key):
            return self.cache[key]
        
        # Clean up expired entry
        if key in self.cache:
            del self.cache[key]
            del self.timestamps[key]
        
        return None
    
    def put(self, key, value):
        self.cache[key] = value
        self.timestamps[key] = time.time()
    
    def cleanup_expired(self):
        """Remove all expired entries"""
        expired_keys = [
            key for key in self.cache 
            if self.is_expired(key)
        ]
        
        for key in expired_keys:
            del self.cache[key]
            del self.timestamps[key]
        
        return len(expired_keys)

# Function memoization decorator
def memoize_with_ttl(ttl_seconds=300):
    """Decorator for function memoization with TTL"""
    def decorator(func):
        cache = TimedCache(ttl_seconds)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from arguments
            key = str(args) + str(sorted(kwargs.items()))
            
            # Check cache first
            result = cache.get(key)
            if result is not None:
                return result
            
            # Compute and cache result
            result = func(*args, **kwargs)
            cache.put(key, result)
            return result
        
        wrapper.cache = cache  # Expose cache for inspection
        return wrapper
    return decorator

@memoize_with_ttl(ttl_seconds=60)  # 1 minute TTL
def expensive_computation(x, y):
    """Simulate expensive computation"""
    time.sleep(1)  # Simulate work
    return x ** y + x * y

# Test memoization
print("First call (will be slow):")
start = time.time()
result1 = expensive_computation(5, 3)
print(f"Result: {result1}, Time: {time.time() - start:.2f}s")

print("Second call (should be instant):")
start = time.time()
result2 = expensive_computation(5, 3)
print(f"Result: {result2}, Time: {time.time() - start:.2f}s")
```

### Database-like Operations

```python
class DictDatabase:
    """Simple in-memory database using dictionaries"""
    
    def __init__(self):
        self.tables = {}
        self.indexes = {}
    
    def create_table(self, table_name, primary_key="id"):
        """Create a new table"""
        self.tables[table_name] = {}
        self.indexes[table_name] = {
            "primary": {},  # primary_key -> record
            "secondary": {}  # field -> {value -> [primary_keys]}
        }
        self.primary_keys = {table_name: primary_key}
    
    def insert(self, table_name, record):
        """Insert record into table"""
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")
        
        primary_key = self.primary_keys[table_name]
        if primary_key not in record:
            raise ValueError(f"Record must have primary key '{primary_key}'")
        
        pk_value = record[primary_key]
        
        # Store in main table
        self.tables[table_name][pk_value] = record.copy()
        
        # Update primary index
        self.indexes[table_name]["primary"][pk_value] = record
        
        # Update secondary indexes
        for field, value in record.items():
            if field != primary_key:
                if field not in self.indexes[table_name]["secondary"]:
                    self.indexes[table_name]["secondary"][field] = defaultdict(list)
                self.indexes[table_name]["secondary"][field][value].append(pk_value)
    
    def select(self, table_name, where=None, order_by=None, limit=None):
        """Select records with optional filtering and ordering"""
        if table_name not in self.tables:
            return []
        
        records = list(self.tables[table_name].values())
        
        # Apply WHERE clause
        if where:
            filtered_records = []
            for record in records:
                if self._evaluate_where(record, where):
                    filtered_records.append(record)
            records = filtered_records
        
        # Apply ORDER BY
        if order_by:
            field, direction = order_by
            reverse = direction.lower() == "desc"
            records.sort(key=lambda r: r.get(field, ""), reverse=reverse)
        
        # Apply LIMIT
        if limit:
            records = records[:limit]
        
        return records
    
    def _evaluate_where(self, record, conditions):
        """Evaluate WHERE conditions"""
        for field, operator, value in conditions:
            record_value = record.get(field)
            
            if operator == "=":
                if record_value != value:
                    return False
            elif operator == ">":
                if not (record_value and record_value > value):
                    return False
            elif operator == "<":
                if not (record_value and record_value < value):
                    return False
            elif operator == ">=":
                if not (record_value and record_value >= value):
                    return False
            elif operator == "<=":
                if not (record_value and record_value <= value):
                    return False
            elif operator == "in":
                if record_value not in value:
                    return False
        
        return True
    
    def update(self, table_name, where, updates):
        """Update records matching conditions"""
        records_to_update = self.select(table_name, where)
        updated_count = 0
        
        for record in records_to_update:
            pk_value = record[self.primary_keys[table_name]]
            
            # Update the record
            for field, new_value in updates.items():
                old_value = record.get(field)
                record[field] = new_value
                
                # Update secondary indexes
                if field in self.indexes[table_name]["secondary"]:
                    # Remove from old value list
                    if old_value is not None:
                        old_list = self.indexes[table_name]["secondary"][field][old_value]
                        if pk_value in old_list:
                            old_list.remove(pk_value)
                    
                    # Add to new value list
                    self.indexes[table_name]["secondary"][field][new_value].append(pk_value)
            
            updated_count += 1
        
        return updated_count
    
    def delete(self, table_name, where):
        """Delete records matching conditions"""
        records_to_delete = self.select(table_name, where)
        deleted_count = 0
        
        for record in records_to_delete:
            pk_value = record[self.primary_keys[table_name]]
            
            # Remove from main table
            del self.tables[table_name][pk_value]
            
            # Remove from primary index
            del self.indexes[table_name]["primary"][pk_value]
            
            # Remove from secondary indexes
            for field, value in record.items():
                if field in self.indexes[table_name]["secondary"]:
                    value_list = self.indexes[table_name]["secondary"][field][value]
                    if pk_value in value_list:
                        value_list.remove(pk_value)
            
            deleted_count += 1
        
        return deleted_count

# Usage example
db = DictDatabase()

# Create users table
db.create_table("users", primary_key="user_id")

# Insert users
users_data = [
    {"user_id": 1, "name": "Alice", "age": 25, "department": "Engineering"},
    {"user_id": 2, "name": "Bob", "age": 30, "department": "Marketing"},
    {"user_id": 3, "name": "Charlie", "age": 28, "department": "Engineering"},
    {"user_id": 4, "name": "Diana", "age": 26, "department": "Sales"}
]

for user in users_data:
    db.insert("users", user)

# Query examples
print("All users:")
all_users = db.select("users")
for user in all_users:
    print(f"  {user}")

print("\nEngineering department:")
engineers = db.select("users", where=[("department", "=", "Engineering")])
for engineer in engineers:
    print(f"  {engineer}")

print("\nUsers over 26, ordered by age:")
older_users = db.select(
    "users", 
    where=[("age", ">", 26)],
    order_by=("age", "asc")
)
for user in older_users:
    print(f"  {user}")

# Update example
print(f"\nUpdated {db.update('users', [('name', '=', 'Alice')], {'age': 26})} records")

# Delete example
print(f"Deleted {db.delete('users', [('department', '=', 'Sales')])} records")

print("\nFinal users:")
final_users = db.select("users")
for user in final_users:
    print(f"  {user}")
```

### Configuration Management

```python
import json
import os
from pathlib import Path

class ConfigManager:
    """Advanced configuration management with nested dictionaries"""
    
    def __init__(self, config_dir="./config"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        self.configs = {}
        self.watchers = {}  # Field -> callback functions
        
        # Default configuration
        self.defaults = {
            "app": {
                "name": "MyApp",
                "version": "1.0.0",
                "debug": False
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp_db",
                "pool_size": 10
            },
            "api": {
                "rate_limit": 1000,
                "timeout": 30,
                "cors": {
                    "enabled": True,
                    "origins": ["*"]
                }
            }
        }
    
    def load_config(self, environment="development"):
        """Load configuration for specific environment"""
        # Start with defaults
        config = self._deep_copy(self.defaults)
        
        # Load environment-specific overrides
        env_file = self.config_dir / f"{environment}.json"
        if env_file.exists():
            with open(env_file, 'r') as f:
                env_config = json.load(f)
                self._deep_merge(config, env_config)
        
        # Load local overrides (not committed to version control)
        local_file = self.config_dir / "local.json"
        if local_file.exists():
            with open(local_file, 'r') as f:
                local_config = json.load(f)
                self._deep_merge(config, local_config)
        
        # Apply environment variables
        self._apply_env_variables(config)
        
        self.configs[environment] = config
        return config
    
    def _deep_copy(self, obj):
        """Deep copy dictionary"""
        if isinstance(obj, dict):
            return {key: self._deep_copy(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._deep_copy(item) for item in obj]
        else:
            return obj
    
    def _deep_merge(self, base, override):
        """Deep merge two dictionaries"""
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value
    
    def _apply_env_variables(self, config):
        """Apply environment variables with prefix"""
        prefix = "MYAPP_"
        
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                keys = config_key.split("_")
                
                # Navigate to nested location
                current = config
                for k in keys[:-1]:
                    if k not in current:
                        current[k] = {}
                    current = current[k]
                
                # Set value with type conversion
                current[keys[-1]] = self._convert_env_value(value)
    
    def _convert_env_value(self, value):
        """Convert environment variable string to appropriate type"""
        if value.lower() in ("true", "false"):
            return value.lower() == "true"
        
        try:
            if "." in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value
    
    def get(self, path, environment="development", default=None):
        """Get configuration value by path (e.g., 'database.host')"""
        if environment not in self.configs:
            self.load_config(environment)
        
        config = self.configs[environment]
        keys = path.split(".")
        
        current = config
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        
        return current
    
    def set(self, path, value, environment="development"):
        """Set configuration value by path"""
        if environment not in self.configs:
            self.load_config(environment)
        
        config = self.configs[environment]
        keys = path.split(".")
        
        current = config
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        old_value = current.get(keys[-1])
        current[keys[-1]] = value
        
        # Trigger watchers
        if path in self.watchers:
            for callback in self.watchers[path]:
                callback(old_value, value)
    
    def watch(self, path, callback):
        """Watch for changes to configuration values"""
        if path not in self.watchers:
            self.watchers[path] = []
        self.watchers[path].append(callback)
    
    def save_config(self, environment="development"):
        """Save current configuration to file"""
        if environment in self.configs:
            env_file = self.config_dir / f"{environment}.json"
            with open(env_file, 'w') as f:
                json.dump(self.configs[environment], f, indent=2)

# Usage example
config_manager = ConfigManager()

# Load configuration
config = config_manager.load_config("production")

# Get values
db_host = config_manager.get("database.host", "production")
api_timeout = config_manager.get("api.timeout", "production")
cors_origins = config_manager.get("api.cors.origins", "production")

print(f"Database host: {db_host}")
print(f"API timeout: {api_timeout}")
print(f"CORS origins: {cors_origins}")

# Set up watcher
def on_debug_change(old_value, new_value):
    print(f"Debug mode changed from {old_value} to {new_value}")

config_manager.watch("app.debug", on_debug_change)

# Change value (will trigger watcher)
config_manager.set("app.debug", True, "production")

# Save configuration
config_manager.save_config("production")
```

---

## 🎯 TÓM TẮT

**Nested Dictionaries và Advanced Concepts** cung cấp powerful tools để:

✅ **Complex data structures**: Multilevel nested dictionaries  
✅ **Safe navigation**: Avoiding KeyError trong deep structures  
✅ **Performance optimization**: Hash design và memory efficiency  
✅ **Advanced applications**: Caching, database operations, configuration  
✅ **Real-world patterns**: LRU cache, timed cache, config management  

**Key Takeaways:**
- Safe navigation prevents crashes với missing keys
- Hash table understanding giúp optimize performance  
- Nested structures mạnh mẽ nhưng cần careful design
- Advanced patterns như caching và database operations rất useful
- Configuration management với nested dicts là industry standard

**Tiếp theo:** Thực hành với bài tập Dictionary phức tạp! 🚀 