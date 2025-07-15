"""
🎯 BÀI TẬP 2: DICTIONARY METHODS & OPERATIONS - INTERACTIVE WORKSHOP
📚 Ngày 11-12: Phương pháp Workshop - Học qua thực hành nhóm

🌟 PHƯƠNG PHÁP WORKSHOP MỚI:
- 🛠️ Hands-on Workshop: Thực hành trực tiếp
- 👥 Collaborative Learning: Học cùng nhau
- 🎯 Problem-Based Learning: Giải quyết vấn đề thực tế
- 🔄 Iterative Practice: Lặp lại và cải tiến
- 📊 Performance Analysis: Phân tích hiệu suất

Tác giả: Tanbaycu
Cập nhật: 2024
"""

import time
import json
import random
from collections import defaultdict, Counter, OrderedDict, ChainMap
from typing import Dict, List, Any, Tuple
import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# 🎪 PHẦN 1: WORKSHOP SETUP - KHỞI TẠO WORKSHOP
# =============================================================================

class DictionaryWorkshop:
    """Lớp quản lý workshop Dictionary"""
    
    def __init__(self):
        self.participants = {}
        self.exercises_completed = {}
        self.performance_data = {}
        self.workshop_data = {}
        
    def register_participant(self, name: str):
        """Đăng ký thành viên workshop"""
        participant_id = f"user_{len(self.participants) + 1}"
        self.participants[participant_id] = {
            "name": name,
            "join_time": time.time(),
            "level": "Beginner",
            "points": 0,
            "exercises_completed": [],
            "badges": []
        }
        print(f"✅ Chào mừng {name} tham gia workshop!")
        return participant_id
    
    def show_leaderboard(self):
        """Hiển thị bảng xếp hạng"""
        print("\n🏆 BẢNG XẾP HẠNG WORKSHOP")
        print("="*50)
        
        sorted_participants = sorted(
            self.participants.items(),
            key=lambda x: x[1]["points"],
            reverse=True
        )
        
        for i, (pid, data) in enumerate(sorted_participants, 1):
            print(f"{i}. {data['name']} - {data['points']} điểm - Level: {data['level']}")

# =============================================================================
# 🔧 PHẦN 2: DICTIONARY METHODS WORKSHOP
# =============================================================================

def workshop_basic_methods():
    """
    🛠️ WORKSHOP: Dictionary Methods cơ bản
    🎯 Thực hành các methods: keys(), values(), items(), get(), pop()
    """
    print("\n" + "="*60)
    print("🔧 WORKSHOP: DICTIONARY METHODS CỞ BẢN")
    print("="*60)
    
    print("""
    🎯 Mục tiêu Workshop:
    - Thành thạo 8 methods cơ bản của Dictionary
    - Hiểu rõ cách sử dụng trong thực tế
    - Phân tích performance của từng method
    - Áp dụng vào project thực tế
    """)
    
    # Tạo sample data cho workshop
    student_database = {
        "SV001": {"name": "Nguyễn Văn A", "age": 20, "major": "CNTT", "gpa": 3.5},
        "SV002": {"name": "Trần Thị B", "age": 19, "major": "Kinh tế", "gpa": 3.8},
        "SV003": {"name": "Lê Văn C", "age": 21, "major": "CNTT", "gpa": 3.2},
        "SV004": {"name": "Phạm Thị D", "age": 20, "major": "Văn học", "gpa": 3.9},
        "SV005": {"name": "Hoàng Văn E", "age": 22, "major": "CNTT", "gpa": 3.6}
    }
    
    print(f"\n📊 Database mẫu: {len(student_database)} sinh viên")
    
    # Workshop Session 1: .keys()
    print("\n🔥 SESSION 1: .keys() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .keys() trả về tất cả keys trong dictionary")
    print("🎯 Thực hành:")
    
    # Đo performance
    start_time = time.time()
    all_keys = list(student_database.keys())
    end_time = time.time()
    
    print(f"   Code: list(student_database.keys())")
    print(f"   Kết quả: {all_keys}")
    print(f"   ⏱️ Thời gian: {(end_time - start_time)*1000:.4f}ms")
    
    # Ứng dụng thực tế
    print("\n🚀 Ứng dụng thực tế:")
    print("   - Lấy danh sách tất cả mã sinh viên")
    print("   - Kiểm tra số lượng sinh viên")
    print("   - Tạo dropdown list cho form")
    
    # Interactive Exercise
    print("\n🎮 THỰC HÀNH TƯƠNG TÁC:")
    user_input = input("Viết code để lấy tất cả keys: ")
    if ".keys()" in user_input:
        print("✅ Chính xác! +10 điểm")
    else:
        print("❌ Thử lại! Gợi ý: sử dụng .keys()")
    
    # Workshop Session 2: .values()
    print("\n🔥 SESSION 2: .values() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .values() trả về tất cả values trong dictionary")
    print("🎯 Thực hành:")
    
    start_time = time.time()
    all_values = list(student_database.values())
    end_time = time.time()
    
    print(f"   Code: list(student_database.values())")
    print(f"   Kết quả: {len(all_values)} records")
    print(f"   ⏱️ Thời gian: {(end_time - start_time)*1000:.4f}ms")
    
    # Phân tích dữ liệu
    print("\n📊 PHÂN TÍCH DỮ LIỆU:")
    ages = [student["age"] for student in all_values]
    gpas = [student["gpa"] for student in all_values]
    
    print(f"   📈 Tuổi trung bình: {sum(ages)/len(ages):.1f}")
    print(f"   📈 GPA trung bình: {sum(gpas)/len(gpas):.2f}")
    print(f"   📈 Tuổi cao nhất: {max(ages)}")
    print(f"   📈 GPA cao nhất: {max(gpas)}")
    
    # Workshop Session 3: .items()
    print("\n🔥 SESSION 3: .items() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .items() trả về cặp (key, value)")
    print("🎯 Thực hành:")
    
    print("   Duyệt qua tất cả sinh viên:")
    for student_id, student_info in student_database.items():
        print(f"   {student_id}: {student_info['name']} - GPA: {student_info['gpa']}")
    
    # Workshop Session 4: .get()
    print("\n🔥 SESSION 4: .get() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .get() lấy value an toàn, có thể set default")
    print("🎯 Thực hành:")
    
    # So sánh cách truy cập
    print("   Cách 1 (không an toàn):")
    try:
        result = student_database["SV999"]
        print(f"   Kết quả: {result}")
    except KeyError:
        print("   ❌ KeyError: Không tìm thấy key!")
    
    print("   Cách 2 (an toàn với .get()):")
    result = student_database.get("SV999", "Không tìm thấy sinh viên")
    print(f"   Kết quả: {result}")
    
    # Workshop Session 5: .pop()
    print("\n🔥 SESSION 5: .pop() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .pop() xóa và trả về value")
    print("🎯 Thực hành:")
    
    # Tạo copy để demo
    demo_db = student_database.copy()
    print(f"   Trước khi pop: {len(demo_db)} sinh viên")
    
    removed_student = demo_db.pop("SV005", "Không tìm thấy")
    print(f"   Sinh viên đã xóa: {removed_student}")
    print(f"   Sau khi pop: {len(demo_db)} sinh viên")
    
    # Workshop Session 6: .update()
    print("\n🔥 SESSION 6: .update() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .update() cập nhật dictionary với dict khác")
    print("🎯 Thực hành:")
    
    new_students = {
        "SV006": {"name": "Đỗ Văn F", "age": 19, "major": "Toán", "gpa": 3.7},
        "SV007": {"name": "Vũ Thị G", "age": 20, "major": "Lý", "gpa": 3.4}
    }
    
    print(f"   Trước update: {len(student_database)} sinh viên")
    student_database.update(new_students)
    print(f"   Sau update: {len(student_database)} sinh viên")
    
    # Workshop Session 7: .setdefault()
    print("\n🔥 SESSION 7: .setdefault() METHOD")
    print("-" * 30)
    
    print("💡 Lý thuyết: .setdefault() lấy value hoặc set default nếu không tồn tại")
    print("🎯 Thực hành:")
    
    # Tạo counter cho majors
    major_counter = {}
    for student in student_database.values():
        major = student["major"]
        major_counter.setdefault(major, 0)
        major_counter[major] += 1
    
    print(f"   Thống kê ngành học: {major_counter}")
    
    # Workshop Session 8: .clear() và .copy()
    print("\n🔥 SESSION 8: .clear() và .copy() METHODS")
    print("-" * 30)
    
    print("💡 Lý thuyết: .clear() xóa tất cả, .copy() tạo bản sao")
    print("🎯 Thực hành:")
    
    # Demo copy
    backup_db = student_database.copy()
    print(f"   Backup tạo: {len(backup_db)} records")
    
    # Demo clear
    temp_db = {"test": "data"}
    print(f"   Trước clear: {temp_db}")
    temp_db.clear()
    print(f"   Sau clear: {temp_db}")
    
    return student_database

# =============================================================================
# 🏗️ PHẦN 3: COLLECTIONS MODULE WORKSHOP
# =============================================================================

def workshop_collections_module():
    """
    🏗️ WORKSHOP: Collections Module
    🎯 Thực hành defaultdict, Counter, OrderedDict, ChainMap
    """
    print("\n" + "="*60)
    print("🏗️ WORKSHOP: COLLECTIONS MODULE")
    print("="*60)
    
    print("""
    🎯 Mục tiêu Workshop:
    - Thành thạo 4 collections chính
    - Hiểu khi nào sử dụng từng loại
    - So sánh performance
    - Ứng dụng trong project thực tế
    """)
    
    # Workshop Session 1: defaultdict
    print("\n🔥 SESSION 1: defaultdict")
    print("-" * 30)
    
    print("💡 Lý thuyết: defaultdict tự động tạo default value")
    print("🎯 Thực hành:")
    
    # Tạo word counter
    text = "python is great python is powerful python is fun"
    words = text.split()
    
    # Cách thường
    word_count_normal = {}
    for word in words:
        if word in word_count_normal:
            word_count_normal[word] += 1
        else:
            word_count_normal[word] = 1
    
    # Cách dùng defaultdict
    word_count_default = defaultdict(int)
    for word in words:
        word_count_default[word] += 1
    
    print(f"   Cách thường: {dict(word_count_normal)}")
    print(f"   Với defaultdict: {dict(word_count_default)}")
    
    # Ứng dụng thực tế: Group students by major
    students = [
        {"name": "A", "major": "CNTT"},
        {"name": "B", "major": "Kinh tế"},
        {"name": "C", "major": "CNTT"},
        {"name": "D", "major": "Văn học"},
        {"name": "E", "major": "CNTT"}
    ]
    
    students_by_major = defaultdict(list)
    for student in students:
        students_by_major[student["major"]].append(student["name"])
    
    print(f"   Sinh viên theo ngành: {dict(students_by_major)}")
    
    # Workshop Session 2: Counter
    print("\n🔥 SESSION 2: Counter")
    print("-" * 30)
    
    print("💡 Lý thuyết: Counter đếm elements tự động")
    print("🎯 Thực hành:")
    
    # Đếm từ trong text
    word_counter = Counter(words)
    print(f"   Word count: {word_counter}")
    print(f"   Top 2 words: {word_counter.most_common(2)}")
    
    # Đếm grades
    grades = ["A", "B", "A", "C", "B", "A", "D", "B", "A"]
    grade_counter = Counter(grades)
    print(f"   Grade distribution: {grade_counter}")
    
    # Counter operations
    counter1 = Counter("hello")
    counter2 = Counter("world")
    print(f"   Counter 1: {counter1}")
    print(f"   Counter 2: {counter2}")
    print(f"   Combined: {counter1 + counter2}")
    print(f"   Subtract: {counter1 - counter2}")
    
    # Workshop Session 3: OrderedDict
    print("\n🔥 SESSION 3: OrderedDict")
    print("-" * 30)
    
    print("💡 Lý thuyết: OrderedDict giữ thứ tự insertion")
    print("🎯 Thực hành:")
    
    # So sánh với dict thường (Python 3.7+ dict cũng ordered)
    normal_dict = {}
    ordered_dict = OrderedDict()
    
    items = [("first", 1), ("second", 2), ("third", 3)]
    
    for key, value in items:
        normal_dict[key] = value
        ordered_dict[key] = value
    
    print(f"   Normal dict: {normal_dict}")
    print(f"   OrderedDict: {ordered_dict}")
    
    # Move to end
    ordered_dict.move_to_end("first")
    print(f"   After move_to_end: {ordered_dict}")
    
    # Workshop Session 4: ChainMap
    print("\n🔥 SESSION 4: ChainMap")
    print("-" * 30)
    
    print("💡 Lý thuyết: ChainMap kết hợp nhiều dict")
    print("🎯 Thực hành:")
    
    # Tạo config system
    default_config = {"theme": "light", "lang": "en", "debug": False}
    user_config = {"theme": "dark", "lang": "vi"}
    project_config = {"debug": True}
    
    # Kết hợp configs (priority: project > user > default)
    config = ChainMap(project_config, user_config, default_config)
    
    print(f"   Default config: {default_config}")
    print(f"   User config: {user_config}")
    print(f"   Project config: {project_config}")
    print(f"   Final config: {dict(config)}")
    
    # Thay đổi config
    config["new_feature"] = True
    print(f"   After adding new_feature: {dict(config)}")
    
    return {
        "defaultdict_example": dict(students_by_major),
        "counter_example": dict(word_counter),
        "ordered_dict_example": dict(ordered_dict),
        "chainmap_example": dict(config)
    }

# =============================================================================
# 🎯 PHẦN 4: PERFORMANCE WORKSHOP
# =============================================================================

def workshop_performance_analysis():
    """
    🎯 WORKSHOP: Performance Analysis
    🎯 So sánh hiệu suất các operations
    """
    print("\n" + "="*60)
    print("🎯 WORKSHOP: PERFORMANCE ANALYSIS")
    print("="*60)
    
    print("""
    🎯 Mục tiêu Workshop:
    - Đo lường performance các operations
    - So sánh dict vs list
    - Tối ưu hóa code
    - Best practices
    """)
    
    # Tạo test data
    test_sizes = [1000, 10000, 100000]
    results = {}
    
    for size in test_sizes:
        print(f"\n📊 Testing với {size:,} elements:")
        
        # Tạo data
        test_dict = {f"key_{i}": f"value_{i}" for i in range(size)}
        test_list = [(f"key_{i}", f"value_{i}") for i in range(size)]
        
        # Test 1: Lookup performance
        search_key = f"key_{size//2}"
        
        # Dict lookup
        start_time = time.time()
        result = test_dict.get(search_key)
        dict_time = time.time() - start_time
        
        # List lookup
        start_time = time.time()
        result = next((value for key, value in test_list if key == search_key), None)
        list_time = time.time() - start_time
        
        print(f"   🔍 Lookup performance:")
        print(f"      Dict: {dict_time*1000:.4f}ms")
        print(f"      List: {list_time*1000:.4f}ms")
        print(f"      Dict nhanh hơn: {list_time/dict_time:.0f}x")
        
        # Test 2: Insertion performance
        start_time = time.time()
        test_dict[f"new_key_{size}"] = f"new_value_{size}"
        dict_insert_time = time.time() - start_time
        
        start_time = time.time()
        test_list.append((f"new_key_{size}", f"new_value_{size}"))
        list_insert_time = time.time() - start_time
        
        print(f"   ➕ Insertion performance:")
        print(f"      Dict: {dict_insert_time*1000:.4f}ms")
        print(f"      List: {list_insert_time*1000:.4f}ms")
        
        # Test 3: Iteration performance
        start_time = time.time()
        for key, value in test_dict.items():
            pass
        dict_iter_time = time.time() - start_time
        
        start_time = time.time()
        for key, value in test_list:
            pass
        list_iter_time = time.time() - start_time
        
        print(f"   🔄 Iteration performance:")
        print(f"      Dict: {dict_iter_time*1000:.4f}ms")
        print(f"      List: {list_iter_time*1000:.4f}ms")
        
        results[size] = {
            "dict_lookup": dict_time,
            "list_lookup": list_time,
            "dict_insert": dict_insert_time,
            "list_insert": list_insert_time,
            "dict_iter": dict_iter_time,
            "list_iter": list_iter_time
        }
    
    # Phân tích kết quả
    print("\n📈 PHÂN TÍCH TỔNG HỢP:")
    print("="*40)
    
    for operation in ["lookup", "insert", "iter"]:
        print(f"\n🔍 {operation.upper()} PERFORMANCE:")
        for size in test_sizes:
            dict_time = results[size][f"dict_{operation}"]
            list_time = results[size][f"list_{operation}"]
            speedup = list_time / dict_time if dict_time > 0 else 0
            print(f"   {size:,} elements: Dict nhanh hơn {speedup:.1f}x")
    
    # Best practices
    print("\n💡 BEST PRACTICES:")
    print("="*40)
    practices = [
        "✅ Sử dụng dict cho lookup nhanh (O(1) vs O(n))",
        "✅ Sử dụng .get() thay vì [] để tránh KeyError",
        "✅ Sử dụng defaultdict cho grouping",
        "✅ Sử dụng Counter cho counting",
        "✅ Tránh tạo dict trong vòng lặp nếu có thể",
        "✅ Sử dụng dict comprehension cho performance tốt hơn"
    ]
    
    for practice in practices:
        print(f"   {practice}")
    
    return results

# =============================================================================
# 🎮 PHẦN 5: INTERACTIVE CODING CHALLENGES
# =============================================================================

def interactive_coding_challenges():
    """
    🎮 WORKSHOP: Interactive Coding Challenges
    🎯 Thách thức coding với Dictionary
    """
    print("\n" + "="*60)
    print("🎮 WORKSHOP: INTERACTIVE CODING CHALLENGES")
    print("="*60)
    
    challenges = [
        {
            "title": "🏪 Inventory Management",
            "description": "Quản lý kho hàng với nhiều operations",
            "difficulty": "Medium",
            "points": 30
        },
        {
            "title": "📊 Data Aggregation",
            "description": "Tổng hợp dữ liệu từ nhiều sources",
            "difficulty": "Hard",
            "points": 50
        },
        {
            "title": "🔍 Search Engine",
            "description": "Xây dựng search engine mini",
            "difficulty": "Expert",
            "points": 70
        }
    ]
    
    print("📋 Danh sách thách thức:")
    for i, challenge in enumerate(challenges, 1):
        print(f"{i}. {challenge['title']} - {challenge['description']} ({challenge['difficulty']}) - {challenge['points']} điểm")
    
    choice = int(input("\nChọn thách thức (1-3): "))
    
    if choice == 1:
        return inventory_management_challenge()
    elif choice == 2:
        return data_aggregation_challenge()
    elif choice == 3:
        return search_engine_challenge()

def inventory_management_challenge():
    """🏪 Thách thức quản lý kho hàng"""
    print("\n🏪 THÁCH THỨC: INVENTORY MANAGEMENT")
    print("="*50)
    
    print("""
    📋 Nhiệm vụ:
    1. Tạo hệ thống quản lý kho hàng
    2. Thêm/xóa/cập nhật sản phẩm
    3. Tính toán thống kê
    4. Xử lý báo cáo
    """)
    
    # Khởi tạo inventory
    inventory = {}
    
    def add_product(name, quantity, price, category):
        """Thêm sản phẩm vào kho"""
        product_id = f"P{len(inventory) + 1:03d}"
        inventory[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category,
            "added_date": time.strftime("%Y-%m-%d")
        }
        return product_id
    
    def update_stock(product_id, quantity_change):
        """Cập nhật số lượng tồn kho"""
        if product_id in inventory:
            inventory[product_id]["quantity"] += quantity_change
            return True
        return False
    
    def get_low_stock_products(threshold=10):
        """Lấy sản phẩm sắp hết hàng"""
        return {pid: product for pid, product in inventory.items() 
                if product["quantity"] < threshold}
    
    def calculate_total_value():
        """Tính tổng giá trị kho hàng"""
        return sum(product["quantity"] * product["price"] 
                  for product in inventory.values())
    
    def get_category_report():
        """Báo cáo theo danh mục"""
        category_stats = defaultdict(lambda: {"count": 0, "total_value": 0})
        
        for product in inventory.values():
            category = product["category"]
            category_stats[category]["count"] += product["quantity"]
            category_stats[category]["total_value"] += product["quantity"] * product["price"]
        
        return dict(category_stats)
    
    # Interactive demo
    print("\n🎮 THỰC HÀNH TƯƠNG TÁC:")
    
    # Thêm sản phẩm mẫu
    sample_products = [
        ("Laptop Dell", 50, 15000000, "Electronics"),
        ("iPhone 15", 30, 25000000, "Electronics"),
        ("Áo thun", 200, 150000, "Fashion"),
        ("Quần jean", 100, 300000, "Fashion"),
        ("Sách Python", 80, 200000, "Books")
    ]
    
    print("1️⃣ Thêm sản phẩm mẫu:")
    for name, qty, price, cat in sample_products:
        pid = add_product(name, qty, price, cat)
        print(f"   ✅ {pid}: {name} - {qty} cái - {price:,} VND")
    
    print(f"\n📊 Tổng số sản phẩm: {len(inventory)}")
    print(f"💰 Tổng giá trị kho: {calculate_total_value():,} VND")
    
    # Cập nhật stock
    print("\n2️⃣ Cập nhật tồn kho:")
    update_stock("P001", -5)  # Bán 5 laptop
    update_stock("P002", -10) # Bán 10 iPhone
    print("   ✅ Đã cập nhật sau khi bán hàng")
    
    # Kiểm tra sản phẩm sắp hết
    print("\n3️⃣ Sản phẩm sắp hết hàng:")
    low_stock = get_low_stock_products(50)
    for pid, product in low_stock.items():
        print(f"   ⚠️ {pid}: {product['name']} - còn {product['quantity']} cái")
    
    # Báo cáo theo danh mục
    print("\n4️⃣ Báo cáo theo danh mục:")
    category_report = get_category_report()
    for category, stats in category_report.items():
        print(f"   📦 {category}: {stats['count']} sản phẩm - {stats['total_value']:,} VND")
    
    # Challenge questions
    print("\n❓ THÁCH THỨC:")
    questions = [
        "Tìm sản phẩm có giá trị cao nhất trong kho",
        "Tính tỷ lệ phần trăm từng danh mục",
        "Tìm sản phẩm được thêm gần đây nhất",
        "Tạo function tìm kiếm sản phẩm theo tên"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
    
    # Giải thách thức 1
    print("\n💡 GIẢI THÁCH THỨC 1:")
    most_valuable = max(inventory.items(), 
                       key=lambda x: x[1]["quantity"] * x[1]["price"])
    print(f"   Sản phẩm có giá trị cao nhất: {most_valuable[0]} - {most_valuable[1]['name']}")
    print(f"   Giá trị: {most_valuable[1]['quantity'] * most_valuable[1]['price']:,} VND")
    
    return inventory

def data_aggregation_challenge():
    """📊 Thách thức tổng hợp dữ liệu"""
    print("\n📊 THÁCH THỨC: DATA AGGREGATION")
    print("="*50)
    
    print("""
    📋 Nhiệm vụ:
    1. Tổng hợp dữ liệu từ nhiều nguồn
    2. Xử lý missing data
    3. Tạo báo cáo tổng hợp
    4. Phân tích xu hướng
    """)
    
    # Tạo sample data từ nhiều nguồn
    sales_data = {
        "2024-01": {"revenue": 1000000, "orders": 150, "customers": 120},
        "2024-02": {"revenue": 1200000, "orders": 180, "customers": 140},
        "2024-03": {"revenue": 1100000, "orders": 165, "customers": 130}
    }
    
    customer_data = {
        "new_customers": {"2024-01": 20, "2024-02": 25, "2024-03": 15},
        "returning_customers": {"2024-01": 100, "2024-02": 115, "2024-03": 115},
        "churn_rate": {"2024-01": 0.05, "2024-02": 0.04, "2024-03": 0.06}
    }
    
    product_data = {
        "categories": {
            "Electronics": {"2024-01": 600000, "2024-02": 720000, "2024-03": 660000},
            "Fashion": {"2024-01": 300000, "2024-02": 360000, "2024-03": 330000},
            "Books": {"2024-01": 100000, "2024-02": 120000, "2024-03": 110000}
        }
    }
    
    # Aggregation functions
    def aggregate_monthly_data():
        """Tổng hợp dữ liệu theo tháng"""
        aggregated = {}
        
        for month in sales_data.keys():
            aggregated[month] = {
                "revenue": sales_data[month]["revenue"],
                "orders": sales_data[month]["orders"],
                "customers": sales_data[month]["customers"],
                "avg_order_value": sales_data[month]["revenue"] / sales_data[month]["orders"],
                "new_customers": customer_data["new_customers"].get(month, 0),
                "returning_customers": customer_data["returning_customers"].get(month, 0),
                "churn_rate": customer_data["churn_rate"].get(month, 0)
            }
        
        return aggregated
    
    def calculate_growth_rates(data):
        """Tính tỷ lệ tăng trưởng"""
        months = sorted(data.keys())
        growth_rates = {}
        
        for i in range(1, len(months)):
            prev_month = months[i-1]
            curr_month = months[i]
            
            growth_rates[curr_month] = {}
            for metric in ["revenue", "orders", "customers"]:
                prev_value = data[prev_month][metric]
                curr_value = data[curr_month][metric]
                growth_rate = ((curr_value - prev_value) / prev_value) * 100
                growth_rates[curr_month][metric] = growth_rate
        
        return growth_rates
    
    def analyze_category_performance():
        """Phân tích hiệu suất theo danh mục"""
        category_analysis = {}
        
        for category, monthly_data in product_data["categories"].items():
            total_revenue = sum(monthly_data.values())
            avg_monthly = total_revenue / len(monthly_data)
            
            # Tính trend
            months = sorted(monthly_data.keys())
            trend = "increasing" if monthly_data[months[-1]] > monthly_data[months[0]] else "decreasing"
            
            category_analysis[category] = {
                "total_revenue": total_revenue,
                "avg_monthly_revenue": avg_monthly,
                "trend": trend,
                "market_share": (total_revenue / sum(sum(cat.values()) for cat in product_data["categories"].values())) * 100
            }
        
        return category_analysis
    
    # Thực hiện aggregation
    print("\n🔥 THỰC HIỆN AGGREGATION:")
    
    print("1️⃣ Tổng hợp dữ liệu theo tháng:")
    monthly_aggregated = aggregate_monthly_data()
    for month, data in monthly_aggregated.items():
        print(f"   {month}: Revenue {data['revenue']:,} - AOV {data['avg_order_value']:,.0f}")
    
    print("\n2️⃣ Tính tỷ lệ tăng trưởng:")
    growth_rates = calculate_growth_rates(monthly_aggregated)
    for month, rates in growth_rates.items():
        print(f"   {month}: Revenue {rates['revenue']:+.1f}% - Orders {rates['orders']:+.1f}%")
    
    print("\n3️⃣ Phân tích danh mục:")
    category_analysis = analyze_category_performance()
    for category, analysis in category_analysis.items():
        print(f"   {category}: {analysis['market_share']:.1f}% market share - {analysis['trend']}")
    
    # Advanced aggregation với ChainMap
    print("\n4️⃣ Advanced Aggregation với ChainMap:")
    
    # Kết hợp tất cả data sources
    combined_data = ChainMap(
        {"sales": sales_data},
        {"customers": customer_data},
        {"products": product_data}
    )
    
    print(f"   Tổng số data sources: {len(combined_data)}")
    print(f"   Available keys: {list(combined_data.keys())}")
    
    # Tạo dashboard data
    dashboard_data = {
        "summary": {
            "total_revenue": sum(month["revenue"] for month in sales_data.values()),
            "total_orders": sum(month["orders"] for month in sales_data.values()),
            "total_customers": sum(month["customers"] for month in sales_data.values()),
            "avg_churn_rate": sum(customer_data["churn_rate"].values()) / len(customer_data["churn_rate"])
        },
        "trends": growth_rates,
        "categories": category_analysis
    }
    
    print(f"\n📊 DASHBOARD SUMMARY:")
    print(f"   💰 Total Revenue: {dashboard_data['summary']['total_revenue']:,} VND")
    print(f"   📦 Total Orders: {dashboard_data['summary']['total_orders']:,}")
    print(f"   👥 Total Customers: {dashboard_data['summary']['total_customers']:,}")
    print(f"   📉 Avg Churn Rate: {dashboard_data['summary']['avg_churn_rate']:.2%}")
    
    return dashboard_data

def search_engine_challenge():
    """🔍 Thách thức xây dựng search engine"""
    print("\n🔍 THÁCH THỨC: SEARCH ENGINE")
    print("="*50)
    
    print("""
    📋 Nhiệm vụ:
    1. Xây dựng inverted index
    2. Implement search algorithm
    3. Ranking và scoring
    4. Fuzzy search
    """)
    
    # Sample documents
    documents = {
        "doc1": "Python is a powerful programming language for data science and web development",
        "doc2": "Machine learning with Python is becoming increasingly popular",
        "doc3": "Web development using Django and Flask frameworks in Python",
        "doc4": "Data analysis and visualization with Python pandas and matplotlib",
        "doc5": "Python programming best practices and design patterns"
    }
    
    class SimpleSearchEngine:
        def __init__(self):
            self.documents = {}
            self.inverted_index = defaultdict(set)
            self.word_freq = defaultdict(lambda: defaultdict(int))
        
        def add_document(self, doc_id, content):
            """Thêm document vào search engine"""
            self.documents[doc_id] = content
            words = content.lower().split()
            
            # Tạo inverted index
            for word in words:
                self.inverted_index[word].add(doc_id)
                self.word_freq[doc_id][word] += 1
        
        def search(self, query):
            """Tìm kiếm cơ bản"""
            query_words = query.lower().split()
            
            if not query_words:
                return []
            
            # Tìm documents chứa từ đầu tiên
            result_docs = self.inverted_index.get(query_words[0], set())
            
            # Intersection với các từ khác
            for word in query_words[1:]:
                result_docs = result_docs.intersection(
                    self.inverted_index.get(word, set())
                )
            
            return list(result_docs)
        
        def search_or(self, query):
            """Tìm kiếm OR (chứa ít nhất 1 từ)"""
            query_words = query.lower().split()
            result_docs = set()
            
            for word in query_words:
                result_docs = result_docs.union(
                    self.inverted_index.get(word, set())
                )
            
            return list(result_docs)
        
        def calculate_tf_idf_score(self, doc_id, query):
            """Tính TF-IDF score"""
            query_words = query.lower().split()
            score = 0
            
            for word in query_words:
                # Term Frequency
                tf = self.word_freq[doc_id].get(word, 0)
                
                # Inverse Document Frequency
                docs_with_word = len(self.inverted_index.get(word, set()))
                if docs_with_word > 0:
                    idf = len(self.documents) / docs_with_word
                    score += tf * idf
            
            return score
        
        def ranked_search(self, query, top_k=5):
            """Tìm kiếm có ranking"""
            # Tìm tất cả documents có chứa ít nhất 1 từ
            candidate_docs = self.search_or(query)
            
            # Tính score cho từng document
            scored_docs = []
            for doc_id in candidate_docs:
                score = self.calculate_tf_idf_score(doc_id, query)
                scored_docs.append((doc_id, score))
            
            # Sắp xếp theo score
            scored_docs.sort(key=lambda x: x[1], reverse=True)
            
            return scored_docs[:top_k]
        
        def fuzzy_search(self, query, max_distance=1):
            """Tìm kiếm fuzzy (cho phép lỗi chính tả)"""
            def levenshtein_distance(s1, s2):
                if len(s1) < len(s2):
                    return levenshtein_distance(s2, s1)
                
                if len(s2) == 0:
                    return len(s1)
                
                previous_row = range(len(s2) + 1)
                for i, c1 in enumerate(s1):
                    current_row = [i + 1]
                    for j, c2 in enumerate(s2):
                        insertions = previous_row[j + 1] + 1
                        deletions = current_row[j] + 1
                        substitutions = previous_row[j] + (c1 != c2)
                        current_row.append(min(insertions, deletions, substitutions))
                    previous_row = current_row
                
                return previous_row[-1]
            
            query_words = query.lower().split()
            fuzzy_results = set()
            
            for query_word in query_words:
                for indexed_word in self.inverted_index.keys():
                    if levenshtein_distance(query_word, indexed_word) <= max_distance:
                        fuzzy_results.update(self.inverted_index[indexed_word])
            
            return list(fuzzy_results)
    
    # Khởi tạo search engine
    search_engine = SimpleSearchEngine()
    
    print("\n🔥 KHỞI TẠO SEARCH ENGINE:")
    
    # Thêm documents
    for doc_id, content in documents.items():
        search_engine.add_document(doc_id, content)
    
    print(f"   ✅ Đã index {len(documents)} documents")
    print(f"   📚 Tổng số từ unique: {len(search_engine.inverted_index)}")
    
    # Test searches
    test_queries = [
        "Python programming",
        "web development",
        "machine learning",
        "data science",
        "Django Flask"
    ]
    
    print("\n🔍 TEST SEARCHES:")
    
    for query in test_queries:
        print(f"\n   Query: '{query}'")
        
        # Basic search (AND)
        basic_results = search_engine.search(query)
        print(f"   Basic (AND): {basic_results}")
        
        # OR search
        or_results = search_engine.search_or(query)
        print(f"   OR search: {or_results}")
        
        # Ranked search
        ranked_results = search_engine.ranked_search(query, top_k=3)
        print(f"   Ranked: {[(doc_id, f'{score:.2f}') for doc_id, score in ranked_results]}")
    
    # Fuzzy search demo
    print("\n🔍 FUZZY SEARCH DEMO:")
    fuzzy_queries = ["Pythn", "machne learning", "web developmnt"]
    
    for query in fuzzy_queries:
        fuzzy_results = search_engine.fuzzy_search(query)
        print(f"   '{query}' -> {fuzzy_results}")
    
    # Interactive search
    print("\n🎮 INTERACTIVE SEARCH:")
    while True:
        user_query = input("   Nhập query (hoặc 'quit' để thoát): ")
        if user_query.lower() == 'quit':
            break
        
        ranked_results = search_engine.ranked_search(user_query, top_k=3)
        
        if ranked_results:
            print("   Kết quả:")
            for i, (doc_id, score) in enumerate(ranked_results, 1):
                print(f"   {i}. {doc_id} (score: {score:.2f})")
                print(f"      {documents[doc_id][:100]}...")
        else:
            print("   Không tìm thấy kết quả!")
    
    return search_engine

# =============================================================================
# 🎊 PHẦN 6: WORKSHOP SUMMARY & GRADUATION
# =============================================================================

def workshop_graduation():
    """
    🎊 WORKSHOP: Graduation Ceremony
    🎯 Tổng kết và cấp chứng chỉ
    """
    print("\n" + "="*60)
    print("🎊 WORKSHOP GRADUATION CEREMONY")
    print("="*60)
    
    print("""
    🎉 Chúc mừng! Bạn đã hoàn thành Dictionary Methods & Operations Workshop!
    
    📋 Nội dung đã học:
    ✅ 8 Dictionary methods cơ bản
    ✅ Collections module (defaultdict, Counter, OrderedDict, ChainMap)
    ✅ Performance analysis và optimization
    ✅ 3 coding challenges thực tế
    ✅ Best practices và design patterns
    """)
    
    # Tạo certificate
    student_name = input("👤 Tên của bạn để in chứng chỉ: ")
    
    certificate = f"""
    
    🏆 CHỨNG CHỈ HOÀN THÀNH WORKSHOP 🏆
    
    ════════════════════════════════════════════════════════════════
    
                    DICTIONARY METHODS & OPERATIONS
                           INTERACTIVE WORKSHOP
    
    ════════════════════════════════════════════════════════════════
    
    Chứng nhận rằng:
    
                        {student_name.upper()}
    
    Đã hoàn thành xuất sắc workshop về Dictionary Methods & Operations
    với các thành tích:
    
    ✅ Thành thạo 8 Dictionary methods cơ bản
    ✅ Sử dụng thành thạo Collections module
    ✅ Phân tích và tối ưu performance
    ✅ Hoàn thành 3 coding challenges
    ✅ Áp dụng best practices
    
    Cấp ngày: {time.strftime("%d/%m/%Y")}
    Nơi cấp: Dictionary Workshop Academy
    
    ════════════════════════════════════════════════════════════════
    
    🎯 Level đạt được: DICTIONARY EXPERT
    ⭐ Điểm số: 95/100
    🏅 Xếp hạng: XUẤT SẮC
    
    """
    
    print(certificate)
    
    # Lưu certificate
    with open(f"certificate_{student_name.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
        f.write(certificate)
    
    print(f"✅ Chứng chỉ đã được lưu vào file: certificate_{student_name.replace(' ', '_')}.txt")
    
    # Next steps
    print("\n🚀 BƯỚC TIẾP THEO:")
    next_steps = [
        "📚 Học Dictionary nâng cao (Nested, Complex operations)",
        "🔧 Ứng dụng vào các project thực tế",
        "📊 Học về Data Structures khác (Set, List comprehension)",
        "🎯 Tham gia các workshops khác trong khóa học",
        "💼 Áp dụng kiến thức vào công việc/dự án cá nhân"
    ]
    
    for step in next_steps:
        print(f"   {step}")
    
    print("\n🎉 Cảm ơn bạn đã tham gia workshop! Chúc bạn thành công!")

# =============================================================================
# 🎮 MAIN PROGRAM - CHƯƠNG TRÌNH CHÍNH
# =============================================================================

def main():
    """Chương trình chính - Workshop orchestrator"""
    
    print("🎓 DICTIONARY METHODS & OPERATIONS WORKSHOP")
    print("📚 Phương pháp: Interactive Workshop + Hands-on Practice")
    print("🎯 Mục tiêu: Thành thạo Dictionary Methods trong 1 ngày")
    
    # Khởi tạo workshop
    workshop = DictionaryWorkshop()
    
    # Đăng ký participant
    participant_name = input("\n👤 Tên của bạn: ")
    participant_id = workshop.register_participant(participant_name)
    
    # Menu workshop
    while True:
        print("\n" + "="*60)
        print("🎯 WORKSHOP MENU")
        print("="*60)
        
        menu_options = [
            "1. 🔧 Dictionary Methods Workshop",
            "2. 🏗️ Collections Module Workshop", 
            "3. 🎯 Performance Analysis Workshop",
            "4. 🎮 Interactive Coding Challenges",
            "5. 🏆 Leaderboard",
            "6. 🎊 Graduation Ceremony",
            "7. 🚪 Exit"
        ]
        
        for option in menu_options:
            print(option)
        
        choice = input("\nChọn workshop (1-7): ")
        
        if choice == "1":
            print("\n🔧 Bắt đầu Dictionary Methods Workshop...")
            result = workshop_basic_methods()
            workshop.participants[participant_id]["points"] += 30
            workshop.participants[participant_id]["exercises_completed"].append("basic_methods")
            
        elif choice == "2":
            print("\n🏗️ Bắt đầu Collections Module Workshop...")
            result = workshop_collections_module()
            workshop.participants[participant_id]["points"] += 40
            workshop.participants[participant_id]["exercises_completed"].append("collections")
            
        elif choice == "3":
            print("\n🎯 Bắt đầu Performance Analysis Workshop...")
            result = workshop_performance_analysis()
            workshop.participants[participant_id]["points"] += 35
            workshop.participants[participant_id]["exercises_completed"].append("performance")
            
        elif choice == "4":
            print("\n🎮 Bắt đầu Interactive Coding Challenges...")
            result = interactive_coding_challenges()
            workshop.participants[participant_id]["points"] += 50
            workshop.participants[participant_id]["exercises_completed"].append("challenges")
            
        elif choice == "5":
            workshop.show_leaderboard()
            
        elif choice == "6":
            if len(workshop.participants[participant_id]["exercises_completed"]) >= 3:
                workshop_graduation()
            else:
                print("❌ Bạn cần hoàn thành ít nhất 3 workshop để tốt nghiệp!")
            
        elif choice == "7":
            print("\n🎉 Cảm ơn bạn đã tham gia workshop!")
            print(f"🏆 Điểm cuối cùng: {workshop.participants[participant_id]['points']}")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        # Cập nhật level
        points = workshop.participants[participant_id]["points"]
        if points >= 150:
            workshop.participants[participant_id]["level"] = "Expert"
        elif points >= 100:
            workshop.participants[participant_id]["level"] = "Advanced"
        elif points >= 50:
            workshop.participants[participant_id]["level"] = "Intermediate"
        
        input("\nNhấn Enter để tiếp tục...")

# =============================================================================
# 🚀 KHỞI CHẠY WORKSHOP
# =============================================================================

if __name__ == "__main__":
    print("🎓 DICTIONARY METHODS & OPERATIONS WORKSHOP - VERSION 2.0")
    print("📚 Phương pháp mới: Interactive Workshop + Collaborative Learning")
    print("🎯 Mục tiêu: Thành thạo Dictionary Methods & Operations")
    print("\n" + "🚀 WORKSHOP STARTING..." + "\n")
    
    main()

"""
🎯 TỔNG KẾT BÀI TẬP 2:

✅ PHƯƠNG PHÁP WORKSHOP MỚI:
- Interactive Workshop: Thực hành trực tiếp với instructor
- Hands-on Practice: Làm ngay, không lý thuyết dài
- Collaborative Learning: Học cùng nhau, chia sẻ kinh nghiệm
- Performance-focused: Tập trung vào hiệu suất và optimization

🏆 NỘI DUNG CHÍNH:
1. Dictionary Methods Workshop (8 methods cơ bản)
2. Collections Module Workshop (defaultdict, Counter, OrderedDict, ChainMap)
3. Performance Analysis Workshop (so sánh hiệu suất)
4. Interactive Coding Challenges (3 thách thức thực tế)
5. Leaderboard System (theo dõi tiến độ)
6. Graduation Ceremony (cấp chứng chỉ)

🎮 TÍNH NĂNG ĐẶC BIỆT:
- Workshop management system
- Real-time performance analysis
- Interactive coding challenges
- Leaderboard và competition
- Certificate generation
- Hands-on practice với real data

📊 KẾT QUẢ MONG ĐỢI:
- Thành thạo 8 Dictionary methods
- Sử dụng thành thạo Collections module
- Hiểu rõ performance implications
- Giải quyết được các bài toán thực tế
- Có chứng chỉ hoàn thành workshop
""" 