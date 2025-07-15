"""
🎯 BÀI TẬP 1: DICTIONARY CƠ BẢN - LEARN BY DOING
📚 Ngày 11-12: Phương pháp học mới - Học qua Thực hành & Câu chuyện

🌟 PHƯƠNG PHÁP HỌC MỚI:
- 📖 Story-Based Learning: Học qua câu chuyện thực tế
- 🎮 Interactive Learning: Tương tác trực tiếp với code
- 🔄 Learn-by-Doing: Thực hành ngay lập tức
- 🎯 Problem-Solving: Giải quyết vấn đề thực tế
- 🏆 Achievement System: Hệ thống thành tích

Tác giả: Tanbaycu
Cập nhật: 2024
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Any

# =============================================================================
# 🎪 PHẦN 1: WELCOME TO THE DICTIONARY WORLD
# =============================================================================

def welcome_message():
    """Chào mừng đến với thế giới Dictionary"""
    print("🎉" * 50)
    print("🌟 CHÀO MỪNG ĐẾN VỚI THẾ GIỚI DICTIONARY! 🌟")
    print("🎉" * 50)
    print("""
    📚 Hôm nay chúng ta sẽ học Dictionary qua những câu chuyện thực tế!
    🎯 Mục tiêu: Thành thạo Dictionary trong 2 ngày
    🚀 Phương pháp: Học qua làm, không học qua đọc!
    
    🏆 Hệ thống thành tích sẽ theo dõi tiến độ của bạn!
    """)
    
    # Tạo profile học viên
    student_profile = {
        "name": input("👤 Tên của bạn: "),
        "level": "Beginner",
        "points": 0,
        "achievements": [],
        "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    print(f"✨ Xin chào {student_profile['name']}! Hãy bắt đầu hành trình học Dictionary!")
    return student_profile

# =============================================================================
# 🏪 PHẦN 2: CÂU CHUYỆN CỬA HÀNG - DICTIONARY BASICS
# =============================================================================

def story_shop_inventory():
    """
    📖 CÂU CHUYỆN: Bạn là chủ cửa hàng tạp hóa
    🎯 Nhiệm vụ: Quản lý kho hàng bằng Dictionary
    """
    print("\n" + "="*60)
    print("🏪 CÂU CHUYỆN: CỬA HÀNG TẠP HÓA CỦA BẠN")
    print("="*60)
    
    print("""
    📖 Tình huống: Bạn vừa mở một cửa hàng tạp hóa nhỏ.
    Bạn cần theo dõi số lượng hàng hóa trong kho.
    
    🤔 Vấn đề: Làm sao để lưu trữ thông tin sản phẩm một cách hiệu quả?
    💡 Giải pháp: Sử dụng Dictionary!
    """)
    
    # Bước 1: Tạo kho hàng trống
    print("\n🔥 THỰC HÀNH NGAY:")
    print("1️⃣ Tạo kho hàng trống:")
    
    inventory = {}
    print(f"   inventory = {inventory}")
    print(f"   📊 Kho hàng hiện tại: {len(inventory)} sản phẩm")
    
    # Bước 2: Thêm sản phẩm đầu tiên
    print("\n2️⃣ Thêm sản phẩm đầu tiên:")
    inventory["bánh mì"] = 50
    inventory["sữa"] = 30
    inventory["trứng"] = 100
    
    print(f"   inventory['bánh mì'] = 50")
    print(f"   inventory['sữa'] = 30") 
    print(f"   inventory['trứng'] = 100")
    print(f"   📊 Kho hàng: {inventory}")
    
    # Bước 3: Kiểm tra hàng hóa
    print("\n3️⃣ Kiểm tra hàng hóa:")
    product = "bánh mì"
    if product in inventory:
        print(f"   ✅ Còn {inventory[product]} {product}")
    else:
        print(f"   ❌ Hết {product}")
    
    # Interactive Exercise
    print("\n🎮 THỰC HÀNH TƯƠNG TÁC:")
    print("Hãy thêm 3 sản phẩm vào kho hàng của bạn!")
    
    for i in range(3):
        product = input(f"Sản phẩm {i+1}: ")
        quantity = int(input(f"Số lượng {product}: "))
        inventory[product] = quantity
        print(f"✅ Đã thêm {quantity} {product}")
    
    print(f"\n🏆 Kho hàng hoàn chỉnh: {inventory}")
    return inventory

# =============================================================================
# 👥 PHẦN 3: CÂU CHUYỆN MẠNG XÃ HỘI - NESTED DICTIONARIES
# =============================================================================

def story_social_network():
    """
    📖 CÂU CHUYỆN: Xây dựng mạng xã hội mini
    🎯 Nhiệm vụ: Quản lý thông tin user bằng Nested Dictionary
    """
    print("\n" + "="*60)
    print("👥 CÂU CHUYỆN: MẠNG XÃ HỘI MINI")
    print("="*60)
    
    print("""
    📖 Tình huống: Bạn đang xây dựng một mạng xã hội nhỏ.
    Mỗi user có nhiều thông tin: tên, tuổi, sở thích, bạn bè...
    
    🤔 Vấn đề: Làm sao lưu trữ thông tin phức tạp này?
    💡 Giải pháp: Nested Dictionary!
    """)
    
    # Tạo database users
    users_db = {}
    
    print("\n🔥 THỰC HÀNH NGAY:")
    print("1️⃣ Tạo profile user đầu tiên:")
    
    # User 1
    users_db["alice"] = {
        "name": "Alice Nguyễn",
        "age": 25,
        "city": "Hà Nội",
        "hobbies": ["đọc sách", "du lịch", "nấu ăn"],
        "friends": ["bob", "charlie"],
        "posts": [
            {"content": "Hôm nay thời tiết đẹp!", "likes": 15, "time": "2024-01-15"},
            {"content": "Vừa đọc xong cuốn sách hay!", "likes": 8, "time": "2024-01-14"}
        ]
    }
    
    print(f"   users_db['alice'] = {json.dumps(users_db['alice'], ensure_ascii=False, indent=2)}")
    
    # Interactive: Tạo user mới
    print("\n🎮 THỰC HÀNH TƯƠNG TÁC:")
    print("Hãy tạo profile cho chính bạn!")
    
    username = input("Username: ")
    name = input("Tên đầy đủ: ")
    age = int(input("Tuổi: "))
    city = input("Thành phố: ")
    
    # Nhập sở thích
    hobbies = []
    print("Nhập 3 sở thích của bạn:")
    for i in range(3):
        hobby = input(f"Sở thích {i+1}: ")
        hobbies.append(hobby)
    
    users_db[username] = {
        "name": name,
        "age": age,
        "city": city,
        "hobbies": hobbies,
        "friends": [],
        "posts": []
    }
    
    print(f"\n✅ Profile của bạn đã được tạo!")
    print(f"📊 Tổng số users: {len(users_db)}")
    
    # Thêm bạn bè
    print("\n2️⃣ Thêm bạn bè:")
    users_db[username]["friends"].append("alice")
    users_db["alice"]["friends"].append(username)
    
    print(f"✅ Bạn và Alice đã trở thành bạn bè!")
    print(f"📊 Bạn bè của {username}: {users_db[username]['friends']}")
    
    return users_db

# =============================================================================
# 🎯 PHẦN 4: GAME QUIZ - DICTIONARY METHODS
# =============================================================================

def interactive_quiz_game():
    """
    🎮 GAME: Quiz tương tác về Dictionary methods
    🎯 Học methods qua game thực tế
    """
    print("\n" + "="*60)
    print("🎯 GAME: DICTIONARY METHODS QUIZ")
    print("="*60)
    
    print("""
    🎮 Luật chơi:
    - Bạn sẽ được cho một dictionary
    - Thực hiện các thao tác được yêu cầu
    - Mỗi câu đúng +10 điểm
    - Có gợi ý nếu cần
    """)
    
    score = 0
    
    # Tạo sample dictionary
    student_grades = {
        "Toán": 8.5,
        "Văn": 7.0,
        "Anh": 9.0,
        "Lý": 6.5,
        "Hóa": 8.0
    }
    
    print(f"\n📊 Dictionary mẫu: {student_grades}")
    
    # Câu hỏi 1: .keys()
    print("\n❓ Câu 1: Lấy tất cả tên môn học")
    print("💡 Gợi ý: Sử dụng method .keys()")
    
    answer = input("Nhập code: ")
    if ".keys()" in answer:
        print("✅ Chính xác!")
        print(f"📊 Kết quả: {list(student_grades.keys())}")
        score += 10
    else:
        print("❌ Sai rồi! Đáp án: student_grades.keys()")
    
    # Câu hỏi 2: .values()
    print("\n❓ Câu 2: Lấy tất cả điểm số")
    print("💡 Gợi ý: Sử dụng method .values()")
    
    answer = input("Nhập code: ")
    if ".values()" in answer:
        print("✅ Chính xác!")
        print(f"📊 Kết quả: {list(student_grades.values())}")
        score += 10
    else:
        print("❌ Sai rồi! Đáp án: student_grades.values()")
    
    # Câu hỏi 3: .items()
    print("\n❓ Câu 3: Lấy cả môn học và điểm")
    print("💡 Gợi ý: Sử dụng method .items()")
    
    answer = input("Nhập code: ")
    if ".items()" in answer:
        print("✅ Chính xác!")
        print(f"📊 Kết quả: {list(student_grades.items())}")
        score += 10
    else:
        print("❌ Sai rồi! Đáp án: student_grades.items()")
    
    # Câu hỏi 4: .get()
    print("\n❓ Câu 4: Lấy điểm Sinh (môn không tồn tại) với giá trị mặc định 0")
    print("💡 Gợi ý: Sử dụng method .get()")
    
    answer = input("Nhập code: ")
    if ".get(" in answer and "0" in answer:
        print("✅ Chính xác!")
        print(f"📊 Kết quả: {student_grades.get('Sinh', 0)}")
        score += 10
    else:
        print("❌ Sai rồi! Đáp án: student_grades.get('Sinh', 0)")
    
    # Câu hỏi 5: .pop()
    print("\n❓ Câu 5: Xóa môn Lý và lấy điểm của nó")
    print("💡 Gợi ý: Sử dụng method .pop()")
    
    answer = input("Nhập code: ")
    if ".pop(" in answer and "Lý" in answer:
        print("✅ Chính xác!")
        removed_score = student_grades.pop("Lý")
        print(f"📊 Điểm Lý đã xóa: {removed_score}")
        print(f"📊 Dictionary còn lại: {student_grades}")
        score += 10
    else:
        print("❌ Sai rồi! Đáp án: student_grades.pop('Lý')")
    
    print(f"\n🏆 Điểm của bạn: {score}/50")
    return score

# =============================================================================
# 🚀 PHẦN 5: DỰ ÁN THỰC TẾ - QUẢN LÝ THÀNH PHỐ
# =============================================================================

def city_management_project():
    """
    🏙️ DỰ ÁN: Hệ thống quản lý thành phố
    🎯 Ứng dụng Dictionary trong bài toán thực tế
    """
    print("\n" + "="*60)
    print("🏙️ DỰ ÁN: HỆ THỐNG QUẢN LÝ THÀNH PHỐ")
    print("="*60)
    
    print("""
    📖 Tình huống: Bạn là quản lý thành phố thông minh
    🎯 Nhiệm vụ: Quản lý dân số, giao thông, dịch vụ
    🛠️ Công cụ: Dictionary với cấu trúc phức tạp
    """)
    
    # Khởi tạo hệ thống thành phố
    city_system = {
        "name": "Smart City",
        "population": 1000000,
        "districts": {},
        "traffic": {
            "lights": {},
            "accidents": [],
            "peak_hours": ["7:00-9:00", "17:00-19:00"]
        },
        "services": {
            "hospitals": {},
            "schools": {},
            "police_stations": {}
        },
        "weather": {
            "temperature": 28,
            "humidity": 70,
            "condition": "sunny"
        }
    }
    
    print("\n🔥 THỰC HÀNH TỪNG BƯỚC:")
    
    # Bước 1: Thêm quận
    print("\n1️⃣ Thêm quận mới:")
    district_name = input("Tên quận: ")
    district_population = int(input("Dân số: "))
    
    city_system["districts"][district_name] = {
        "population": district_population,
        "area": input("Diện tích (km²): "),
        "mayor": input("Chủ tịch quận: "),
        "budget": int(input("Ngân sách (tỷ): ")),
        "projects": []
    }
    
    print(f"✅ Đã thêm quận {district_name}")
    
    # Bước 2: Thêm dịch vụ
    print("\n2️⃣ Thêm bệnh viện:")
    hospital_name = input("Tên bệnh viện: ")
    city_system["services"]["hospitals"][hospital_name] = {
        "address": input("Địa chỉ: "),
        "capacity": int(input("Sức chứa: ")),
        "doctors": int(input("Số bác sĩ: ")),
        "specialties": input("Chuyên khoa (cách nhau bởi dấu phẩy): ").split(",")
    }
    
    print(f"✅ Đã thêm bệnh viện {hospital_name}")
    
    # Bước 3: Cập nhật giao thông
    print("\n3️⃣ Thêm đèn giao thông:")
    intersection = input("Tên ngã tư: ")
    city_system["traffic"]["lights"][intersection] = {
        "status": "green",
        "timer": 30,
        "traffic_flow": random.randint(50, 200)
    }
    
    print(f"✅ Đã thêm đèn giao thông tại {intersection}")
    
    # Bước 4: Báo cáo tổng hợp
    print("\n📊 BÁO CÁO TỔNG HỢP:")
    print(f"🏙️ Thành phố: {city_system['name']}")
    print(f"👥 Dân số: {city_system['population']:,}")
    print(f"🏘️ Số quận: {len(city_system['districts'])}")
    print(f"🏥 Số bệnh viện: {len(city_system['services']['hospitals'])}")
    print(f"🚦 Số đèn giao thông: {len(city_system['traffic']['lights'])}")
    print(f"🌡️ Nhiệt độ: {city_system['weather']['temperature']}°C")
    
    # Tính toán thống kê
    total_district_population = sum(district["population"] for district in city_system["districts"].values())
    total_hospital_capacity = sum(hospital["capacity"] for hospital in city_system["services"]["hospitals"].values())
    
    print(f"\n📈 THỐNG KÊ CHI TIẾT:")
    print(f"👥 Dân số các quận: {total_district_population:,}")
    print(f"🏥 Tổng sức chứa bệnh viện: {total_hospital_capacity:,}")
    print(f"🚦 Lưu lượng giao thông trung bình: {sum(light['traffic_flow'] for light in city_system['traffic']['lights'].values()) // len(city_system['traffic']['lights']) if city_system['traffic']['lights'] else 0}")
    
    return city_system

# =============================================================================
# 🎯 PHẦN 6: CHALLENGE MODES - THÁCH THỨC NÂNG CAO
# =============================================================================

def challenge_mode():
    """
    🏆 CHALLENGE: Thách thức nâng cao với Dictionary
    🎯 Test kỹ năng qua các tình huống phức tạp
    """
    print("\n" + "="*60)
    print("🏆 CHALLENGE MODE: THÁCH THỨC NÂNG CAO")
    print("="*60)
    
    challenges = [
        {
            "name": "🔍 Detective Dictionary",
            "description": "Tìm ra thông tin ẩn trong nested dictionary",
            "difficulty": "Medium"
        },
        {
            "name": "🎲 Random Data Generator",
            "description": "Tạo dữ liệu ngẫu nhiên với Dictionary",
            "difficulty": "Easy"
        },
        {
            "name": "🧮 Data Analyzer",
            "description": "Phân tích dữ liệu phức tạp",
            "difficulty": "Hard"
        }
    ]
    
    print("📋 Danh sách thách thức:")
    for i, challenge in enumerate(challenges, 1):
        print(f"{i}. {challenge['name']} - {challenge['description']} ({challenge['difficulty']})")
    
    choice = int(input("\nChọn thách thức (1-3): "))
    
    if choice == 1:
        return detective_challenge()
    elif choice == 2:
        return random_generator_challenge()
    elif choice == 3:
        return data_analyzer_challenge()

def detective_challenge():
    """🔍 Thách thức thám tử: Tìm thông tin ẩn"""
    print("\n🔍 THÁCH THỨC THÁM TỬ")
    print("="*40)
    
    # Tạo database phức tạp
    crime_database = {
        "cases": {
            "case_001": {
                "title": "Vụ mất tích bí ẩn",
                "suspects": {
                    "john_doe": {
                        "age": 35,
                        "occupation": "Kế toán",
                        "alibi": "Ở nhà xem TV",
                        "evidence": ["fingerprints", "witness_testimony"]
                    },
                    "jane_smith": {
                        "age": 28,
                        "occupation": "Y tá",
                        "alibi": "Làm việc tại bệnh viện",
                        "evidence": ["cctv_footage"]
                    }
                },
                "evidence": {
                    "fingerprints": {"location": "door_handle", "quality": "clear"},
                    "witness_testimony": {"reliability": "high", "details": "Thấy xe màu đỏ"},
                    "cctv_footage": {"timestamp": "22:30", "quality": "poor"}
                }
            }
        }
    }
    
    print("📋 Nhiệm vụ: Tìm ra thông tin sau từ database:")
    print("1. Tuổi của John Doe")
    print("2. Nghề nghiệp của Jane Smith")
    print("3. Chất lượng của CCTV footage")
    print("4. Địa điểm tìm thấy fingerprints")
    
    score = 0
    
    # Câu hỏi 1
    answer = input("\n1. Tuổi của John Doe: ")
    if answer == "35":
        print("✅ Chính xác!")
        score += 25
    else:
        print(f"❌ Sai! Đáp án: {crime_database['cases']['case_001']['suspects']['john_doe']['age']}")
    
    # Câu hỏi 2
    answer = input("2. Nghề nghiệp của Jane Smith: ")
    if answer.lower() in ["y tá", "y ta", "nurse"]:
        print("✅ Chính xác!")
        score += 25
    else:
        print(f"❌ Sai! Đáp án: {crime_database['cases']['case_001']['suspects']['jane_smith']['occupation']}")
    
    # Câu hỏi 3
    answer = input("3. Chất lượng CCTV footage: ")
    if answer.lower() == "poor":
        print("✅ Chính xác!")
        score += 25
    else:
        print(f"❌ Sai! Đáp án: {crime_database['cases']['case_001']['evidence']['cctv_footage']['quality']}")
    
    # Câu hỏi 4
    answer = input("4. Địa điểm fingerprints: ")
    if "door" in answer.lower():
        print("✅ Chính xác!")
        score += 25
    else:
        print(f"❌ Sai! Đáp án: {crime_database['cases']['case_001']['evidence']['fingerprints']['location']}")
    
    print(f"\n🏆 Điểm số: {score}/100")
    return score

def random_generator_challenge():
    """🎲 Thách thức tạo dữ liệu ngẫu nhiên"""
    print("\n🎲 THÁCH THỨC: RANDOM DATA GENERATOR")
    print("="*40)
    
    print("📋 Nhiệm vụ: Tạo dữ liệu ngẫu nhiên cho game RPG")
    
    # Danh sách dữ liệu mẫu
    character_names = ["Warrior", "Mage", "Archer", "Rogue", "Paladin"]
    weapons = ["Sword", "Staff", "Bow", "Dagger", "Hammer"]
    locations = ["Forest", "Castle", "Cave", "Village", "Mountain"]
    
    print("\n🎮 Tạo 5 nhân vật ngẫu nhiên:")
    
    characters = {}
    for i in range(5):
        name = random.choice(character_names)
        character_id = f"char_{i+1}"
        
        characters[character_id] = {
            "name": name,
            "level": random.randint(1, 50),
            "health": random.randint(50, 200),
            "mana": random.randint(20, 100),
            "weapon": random.choice(weapons),
            "location": random.choice(locations),
            "gold": random.randint(0, 1000),
            "skills": random.sample(["Fire", "Ice", "Heal", "Shield", "Speed"], 3)
        }
        
        print(f"✅ {character_id}: {characters[character_id]}")
    
    # Thống kê
    print("\n📊 THỐNG KÊ:")
    avg_level = sum(char["level"] for char in characters.values()) / len(characters)
    total_gold = sum(char["gold"] for char in characters.values())
    
    print(f"🎯 Level trung bình: {avg_level:.1f}")
    print(f"💰 Tổng gold: {total_gold}")
    print(f"⚔️ Weapon phổ biến nhất: {max(set(char['weapon'] for char in characters.values()), key=lambda x: sum(1 for char in characters.values() if char['weapon'] == x))}")
    
    return characters

def data_analyzer_challenge():
    """🧮 Thách thức phân tích dữ liệu"""
    print("\n🧮 THÁCH THỨC: DATA ANALYZER")
    print("="*40)
    
    # Tạo dữ liệu bán hàng
    sales_data = {
        "2024-01": {
            "products": {
                "laptop": {"sold": 150, "revenue": 300000000, "cost": 200000000},
                "phone": {"sold": 300, "revenue": 450000000, "cost": 300000000},
                "tablet": {"sold": 80, "revenue": 120000000, "cost": 80000000}
            },
            "customers": 450,
            "returns": 15
        },
        "2024-02": {
            "products": {
                "laptop": {"sold": 200, "revenue": 400000000, "cost": 260000000},
                "phone": {"sold": 280, "revenue": 420000000, "cost": 280000000},
                "tablet": {"sold": 120, "revenue": 180000000, "cost": 120000000}
            },
            "customers": 520,
            "returns": 12
        }
    }
    
    print("📋 Nhiệm vụ: Phân tích dữ liệu bán hàng và trả lời câu hỏi")
    
    # Câu hỏi phân tích
    questions = [
        "Tháng nào bán được nhiều laptop hơn?",
        "Sản phẩm nào có lợi nhuận cao nhất tháng 1?",
        "Tổng doanh thu 2 tháng là bao nhiêu?",
        "Tỷ lệ trả hàng trung bình là bao nhiêu?"
    ]
    
    score = 0
    
    # Phân tích tự động
    print("\n🔍 PHÂN TÍCH TỰ ĐỘNG:")
    
    # Tháng bán laptop nhiều hơn
    laptop_jan = sales_data["2024-01"]["products"]["laptop"]["sold"]
    laptop_feb = sales_data["2024-02"]["products"]["laptop"]["sold"]
    best_laptop_month = "2024-02" if laptop_feb > laptop_jan else "2024-01"
    
    print(f"1. Tháng bán laptop nhiều nhất: {best_laptop_month} ({max(laptop_jan, laptop_feb)} chiếc)")
    
    # Sản phẩm lợi nhuận cao nhất tháng 1
    jan_profits = {}
    for product, data in sales_data["2024-01"]["products"].items():
        jan_profits[product] = data["revenue"] - data["cost"]
    
    best_profit_product = max(jan_profits, key=jan_profits.get)
    print(f"2. Sản phẩm lợi nhuận cao nhất tháng 1: {best_profit_product} ({jan_profits[best_profit_product]:,} VND)")
    
    # Tổng doanh thu
    total_revenue = 0
    for month_data in sales_data.values():
        for product_data in month_data["products"].values():
            total_revenue += product_data["revenue"]
    
    print(f"3. Tổng doanh thu 2 tháng: {total_revenue:,} VND")
    
    # Tỷ lệ trả hàng
    total_customers = sum(month["customers"] for month in sales_data.values())
    total_returns = sum(month["returns"] for month in sales_data.values())
    return_rate = (total_returns / total_customers) * 100
    
    print(f"4. Tỷ lệ trả hàng trung bình: {return_rate:.2f}%")
    
    # Interactive questions
    print("\n❓ TRẮC NGHIỆM:")
    user_answer = input("Tháng nào bán laptop nhiều hơn? (2024-01/2024-02): ")
    if user_answer == best_laptop_month:
        score += 25
        print("✅ Chính xác!")
    else:
        print(f"❌ Sai! Đáp án: {best_laptop_month}")
    
    print(f"\n🏆 Điểm số: {score}/100")
    return score

# =============================================================================
# 🎊 PHẦN 7: ACHIEVEMENT SYSTEM - HỆ THỐNG THÀNH TÍCH
# =============================================================================

def update_achievements(student_profile: Dict, activity: str, score: int = 0):
    """Cập nhật thành tích của học viên"""
    
    achievements = {
        "first_dictionary": "🥇 Tạo Dictionary đầu tiên",
        "shop_master": "🏪 Chủ cửa hàng giỏi",
        "social_builder": "👥 Kiến trúc sư mạng xã hội",
        "quiz_champion": "🎯 Nhà vô địch Quiz",
        "city_manager": "🏙️ Quản lý thành phố",
        "detective": "🔍 Thám tử tài ba",
        "data_analyst": "📊 Chuyên gia phân tích dữ liệu",
        "perfect_score": "💯 Điểm số hoàn hảo"
    }
    
    # Cập nhật điểm
    student_profile["points"] += score
    
    # Kiểm tra thành tích mới
    if activity not in student_profile["achievements"]:
        student_profile["achievements"].append(activity)
        print(f"\n🎉 THÀNH TÍCH MỚI: {achievements.get(activity, activity)}")
    
    # Cập nhật level
    if student_profile["points"] >= 200:
        student_profile["level"] = "Expert"
    elif student_profile["points"] >= 100:
        student_profile["level"] = "Advanced"
    elif student_profile["points"] >= 50:
        student_profile["level"] = "Intermediate"
    
    return student_profile

def show_progress_report(student_profile: Dict):
    """Hiển thị báo cáo tiến độ học tập"""
    print("\n" + "="*60)
    print("📊 BÁO CÁO TIẾN ĐỘ HỌC TẬP")
    print("="*60)
    
    print(f"👤 Học viên: {student_profile['name']}")
    print(f"🎯 Level: {student_profile['level']}")
    print(f"⭐ Điểm số: {student_profile['points']}")
    print(f"🏆 Thành tích: {len(student_profile['achievements'])}")
    
    print("\n🏅 DANH SÁCH THÀNH TÍCH:")
    for achievement in student_profile['achievements']:
        print(f"  ✅ {achievement}")
    
    # Đánh giá tiến độ
    if student_profile['points'] >= 200:
        print("\n🌟 XUẤT SẮC! Bạn đã thành thạo Dictionary!")
    elif student_profile['points'] >= 100:
        print("\n👍 TỐT! Bạn đã hiểu rõ Dictionary!")
    elif student_profile['points'] >= 50:
        print("\n📈 TIẾN BỘ! Tiếp tục cố gắng!")
    else:
        print("\n💪 BẮT ĐẦU! Hãy thực hành nhiều hơn!")

# =============================================================================
# 🎮 PHẦN 8: MAIN PROGRAM - CHƯƠNG TRÌNH CHÍNH
# =============================================================================

def main():
    """Chương trình chính - Orchestrate toàn bộ bài học"""
    
    # Chào mừng và tạo profile
    student_profile = welcome_message()
    
    # Menu chính
    while True:
        print("\n" + "="*60)
        print("🎯 MENU CHÍNH - DICTIONARY LEARNING JOURNEY")
        print("="*60)
        
        menu_options = [
            "1. 🏪 Câu chuyện cửa hàng (Dictionary Basics)",
            "2. 👥 Mạng xã hội mini (Nested Dictionary)",
            "3. 🎯 Game Quiz (Dictionary Methods)",
            "4. 🏙️ Dự án thành phố (Real Project)",
            "5. 🏆 Challenge Mode (Advanced)",
            "6. 📊 Xem tiến độ học tập",
            "7. 💾 Lưu tiến độ",
            "8. 🚪 Thoát"
        ]
        
        for option in menu_options:
            print(option)
        
        choice = input("\nChọn hoạt động (1-8): ")
        
        if choice == "1":
            print("\n🎬 Bắt đầu câu chuyện cửa hàng...")
            inventory = story_shop_inventory()
            student_profile = update_achievements(student_profile, "shop_master", 20)
            
        elif choice == "2":
            print("\n🎬 Xây dựng mạng xã hội...")
            users_db = story_social_network()
            student_profile = update_achievements(student_profile, "social_builder", 25)
            
        elif choice == "3":
            print("\n🎮 Bắt đầu Quiz Game...")
            score = interactive_quiz_game()
            student_profile = update_achievements(student_profile, "quiz_champion", score)
            if score >= 40:
                student_profile = update_achievements(student_profile, "perfect_score", 10)
            
        elif choice == "4":
            print("\n🏗️ Khởi động dự án thành phố...")
            city_data = city_management_project()
            student_profile = update_achievements(student_profile, "city_manager", 30)
            
        elif choice == "5":
            print("\n⚡ Entering Challenge Mode...")
            challenge_score = challenge_mode()
            student_profile = update_achievements(student_profile, "detective", challenge_score)
            
        elif choice == "6":
            show_progress_report(student_profile)
            
        elif choice == "7":
            # Lưu tiến độ
            with open("student_progress.json", "w", encoding="utf-8") as f:
                json.dump(student_profile, f, ensure_ascii=False, indent=2)
            print("✅ Đã lưu tiến độ học tập!")
            
        elif choice == "8":
            print("\n🎉 Cảm ơn bạn đã học cùng chúng tôi!")
            print(f"🏆 Điểm cuối cùng: {student_profile['points']}")
            print(f"🎯 Level đạt được: {student_profile['level']}")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

# =============================================================================
# 🚀 KHỞI CHẠY CHƯƠNG TRÌNH
# =============================================================================

if __name__ == "__main__":
    print("🎓 DICTIONARY LEARNING SYSTEM - PHIÊN BẢN 2.0")
    print("📚 Phương pháp học mới: Story-Based + Interactive + Gamification")
    print("🎯 Mục tiêu: Thành thạo Dictionary trong 2 ngày")
    print("\n" + "🚀 KHỞI ĐỘNG..." + "\n")
    
    main()

"""
🎯 TỔNG KẾT BÀI TẬP 1:

✅ PHƯƠNG PHÁP HỌC MỚI:
- Story-Based Learning: Học qua câu chuyện thực tế
- Interactive Learning: Tương tác trực tiếp với code
- Gamification: Hệ thống điểm, thành tích, thách thức
- Problem-Solving: Giải quyết vấn đề thực tế

🏆 NỘI DUNG CHÍNH:
1. Dictionary Basics qua câu chuyện cửa hàng
2. Nested Dictionary qua mạng xã hội
3. Dictionary Methods qua game quiz
4. Real Project: Hệ thống quản lý thành phố
5. Challenge Mode: Thách thức nâng cao
6. Achievement System: Theo dõi tiến độ

🎮 TÍNH NĂNG ĐẶC BIỆT:
- Menu tương tác
- Hệ thống điểm số và thành tích
- Lưu tiến độ học tập
- Báo cáo chi tiết
- Thách thức đa cấp độ

📊 KẾT QUẢ MONG ĐỢI:
- Hiểu sâu về Dictionary
- Ứng dụng thực tế
- Tư duy giải quyết vấn đề
- Kỹ năng lập trình nâng cao
""" 