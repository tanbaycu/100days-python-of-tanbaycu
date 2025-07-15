#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BÀI TẬP 3: METHODS VÀ OPERATIONS CHO LISTS, TUPLES, SETS
Ngày 9-10: Làm việc với các phương thức và thao tác nâng cao

Mục tiêu học tập:
- Nắm vững các methods quan trọng của Lists, Tuples, Sets
- Hiểu rõ hiệu suất và cách sử dụng phù hợp
- Thực hành với List Comprehensions và Set Operations
- Xử lý dữ liệu phức tạp và tối ưu hóa code

Tác giả: Python Learning Journey
Cấp độ: Intermediate đến Advanced
"""

# ============================================================================
# PHẦN 1: LIST METHODS - CÁC PHƯƠNG THỨC CỦA LISTS (20 BÀI TẬP)
# ============================================================================

print("=" * 60)
print("PHẦN 1: LIST METHODS - CÁC PHƯƠNG THỨC CỦA LISTS")
print("=" * 60)

# Bài 1.1: Thêm và xóa phần tử
print("\n--- Bài 1.1: Thêm và xóa phần tử ---")

# Tạo danh sách shopping list và thực hiện các thao tác
shopping_list = ["táo", "chuối", "cam"]
print(f"Danh sách ban đầu: {shopping_list}")

# Thêm phần tử cuối danh sách
shopping_list.append("xoài")
print(f"Sau khi append 'xoài': {shopping_list}")

# Thêm phần tử vào vị trí cụ thể
shopping_list.insert(1, "nho")
print(f"Sau khi insert 'nho' ở vị trí 1: {shopping_list}")

# Thêm nhiều phần tử
shopping_list.extend(["dưa hấu", "đu đủ"])
print(f"Sau khi extend: {shopping_list}")

# Xóa phần tử đầu tiên tìm thấy
shopping_list.remove("chuối")
print(f"Sau khi remove 'chuối': {shopping_list}")

# Xóa và trả về phần tử cuối
last_item = shopping_list.pop()
print(f"Pop ra: {last_item}, danh sách còn: {shopping_list}")

# Xóa phần tử tại vị trí cụ thể
second_item = shopping_list.pop(1)
print(f"Pop vị trí 1: {second_item}, danh sách còn: {shopping_list}")

# Bài 1.2: Tìm kiếm và đếm
print("\n--- Bài 1.2: Tìm kiếm và đếm ---")

numbers = [1, 3, 5, 3, 7, 3, 9, 1, 5]
print(f"Danh sách số: {numbers}")

# Đếm số lần xuất hiện
count_3 = numbers.count(3)
count_1 = numbers.count(1)
print(f"Số 3 xuất hiện {count_3} lần")
print(f"Số 1 xuất hiện {count_1} lần")

# Tìm vị trí đầu tiên
index_5 = numbers.index(5)
print(f"Vị trí đầu tiên của số 5: {index_5}")

# Tìm vị trí với start và end
index_3_after_2 = numbers.index(3, 2)  # Tìm từ vị trí 2
print(f"Vị trí của số 3 kể từ index 2: {index_3_after_2}")

# Bài 1.3: Sắp xếp và đảo ngược
print("\n--- Bài 1.3: Sắp xếp và đảo ngược ---")

# Danh sách điểm số học sinh
scores = [85, 92, 78, 96, 88, 73, 90]
print(f"Điểm gốc: {scores}")

# Sắp xếp tăng dần (thay đổi list gốc)
scores_copy = scores.copy()
scores_copy.sort()
print(f"Sắp xếp tăng dần: {scores_copy}")

# Sắp xếp giảm dần
scores_copy.sort(reverse=True)
print(f"Sắp xếp giảm dần: {scores_copy}")

# Sắp xếp mà không thay đổi list gốc
sorted_scores = sorted(scores)
print(f"Sorted() tăng dần: {sorted_scores}")
print(f"List gốc không đổi: {scores}")

# Đảo ngược list
scores.reverse()
print(f"Sau reverse(): {scores}")

# Bài 1.4: Sao chép list
print("\n--- Bài 1.4: Sao chép list ---")

original = [1, [2, 3], 4]
print(f"List gốc: {original}")

# Shallow copy
shallow = original.copy()
shallow[0] = 999
shallow[1][0] = 888
print(f"Sau shallow copy và thay đổi: {original}")
print(f"Shallow copy: {shallow}")

# Deep copy
import copy
original2 = [1, [2, 3], 4]
deep = copy.deepcopy(original2)
deep[1][0] = 777
print(f"Sau deep copy và thay đổi - gốc: {original2}")
print(f"Deep copy: {deep}")

# Bài 1.5: Xóa toàn bộ
print("\n--- Bài 1.5: Xóa toàn bộ ---")

test_list = ["a", "b", "c", "d"]
print(f"Trước khi clear: {test_list}")
test_list.clear()
print(f"Sau khi clear: {test_list}")

# ============================================================================
# PHẦN 2: LIST COMPREHENSIONS - BIỂU THỨC DANH SÁCH (15 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 2: LIST COMPREHENSIONS - BIỂU THỨC DANH SÁCH")
print("=" * 60)

# Bài 2.1: List comprehension cơ bản
print("\n--- Bài 2.1: List comprehension cơ bản ---")

# Tạo danh sách bình phương
squares = [x**2 for x in range(1, 11)]
print(f"Bình phương từ 1-10: {squares}")

# So sánh với cách truyền thống
squares_traditional = []
for x in range(1, 11):
    squares_traditional.append(x**2)
print(f"Cách truyền thống: {squares_traditional}")

# Tạo danh sách số chẵn
evens = [x for x in range(20) if x % 2 == 0]
print(f"Số chẵn từ 0-19: {evens}")

# Bài 2.2: Xử lý chuỗi với list comprehension
print("\n--- Bài 2.2: Xử lý chuỗi ---")

words = ["python", "java", "javascript", "c++", "go"]
print(f"Danh sách ngôn ngữ: {words}")

# Chuyển thành chữ hoa
upper_words = [word.upper() for word in words]
print(f"Chữ hoa: {upper_words}")

# Lấy độ dài của mỗi từ
word_lengths = [len(word) for word in words]
print(f"Độ dài: {word_lengths}")

# Lọc từ có độ dài > 4
long_words = [word for word in words if len(word) > 4]
print(f"Từ dài hơn 4 ký tự: {long_words}")

# Bài 2.3: Nested list comprehension
print("\n--- Bài 2.3: Nested list comprehension ---")

# Tạo ma trận 3x3
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print("Ma trận 3x3:")
for row in matrix:
    print(row)

# Chuyển vị ma trận
transposed = [[row[i] for row in matrix] for i in range(3)]
print("Ma trận chuyển vị:")
for row in transposed:
    print(row)

# Làm phẳng ma trận
flattened = [num for row in matrix for num in row]
print(f"Ma trận làm phẳng: {flattened}")

# Bài 2.4: Conditional expressions trong list comprehension
print("\n--- Bài 2.4: Conditional expressions ---")

numbers = range(-5, 6)
print(f"Số từ -5 đến 5: {list(numbers)}")

# Thay số âm bằng 0, giữ nguyên số dương
positive_or_zero = [x if x >= 0 else 0 for x in numbers]
print(f"Thay số âm bằng 0: {positive_or_zero}")

# Phân loại chẵn/lẻ
even_odd = ["chẵn" if x % 2 == 0 else "lẻ" for x in range(10)]
print(f"Phân loại chẵn/lẻ: {even_odd}")

# Bài 2.5: Performance comparison
print("\n--- Bài 2.5: So sánh hiệu suất ---")

import time

# Test với 100000 phần tử
n = 100000

# List comprehension
start = time.time()
squares_lc = [x**2 for x in range(n)]
lc_time = time.time() - start

# For loop truyền thống
start = time.time()
squares_loop = []
for x in range(n):
    squares_loop.append(x**2)
loop_time = time.time() - start

# Map function
start = time.time()
squares_map = list(map(lambda x: x**2, range(n)))
map_time = time.time() - start

print(f"List comprehension: {lc_time:.4f}s")
print(f"For loop: {loop_time:.4f}s") 
print(f"Map function: {map_time:.4f}s")

# ============================================================================
# PHẦN 3: TUPLE METHODS VÀ OPERATIONS (10 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 3: TUPLE METHODS VÀ OPERATIONS")
print("=" * 60)

# Bài 3.1: Tuple methods cơ bản
print("\n--- Bài 3.1: Tuple methods cơ bản ---")

# Tuple với dữ liệu trùng lặp
grades = (85, 90, 85, 88, 90, 85, 92)
print(f"Điểm số: {grades}")

# Đếm số lần xuất hiện
count_85 = grades.count(85)
count_90 = grades.count(90)
print(f"Điểm 85 xuất hiện {count_85} lần")
print(f"Điểm 90 xuất hiện {count_90} lần")

# Tìm vị trí đầu tiên
index_88 = grades.index(88)
print(f"Vị trí đầu tiên của điểm 88: {index_88}")

# Bài 3.2: Unpacking và packing nâng cao
print("\n--- Bài 3.2: Unpacking và packing nâng cao ---")

# Multiple assignment
person = ("Nguyễn Văn A", 25, "Hà Nội", "Kỹ sư")
name, age, city, job = person
print(f"Tên: {name}, Tuổi: {age}, Thành phố: {city}, Nghề: {job}")

# Unpacking với *
numbers = (1, 2, 3, 4, 5, 6)
first, second, *middle, last = numbers
print(f"Đầu: {first}, Thứ hai: {second}")
print(f"Giữa: {middle}, Cuối: {last}")

# Swapping variables
a, b = 10, 20
print(f"Trước swap: a={a}, b={b}")
a, b = b, a
print(f"Sau swap: a={a}, b={b}")

# Bài 3.3: Tuple làm key trong dictionary
print("\n--- Bài 3.3: Tuple làm key trong dictionary ---")

# Lưu trữ tọa độ và thông tin
coordinates = {
    (0, 0): "Gốc tọa độ",
    (1, 0): "Trục X",
    (0, 1): "Trục Y", 
    (1, 1): "Góc phần tư 1"
}

for coord, description in coordinates.items():
    print(f"Tọa độ {coord}: {description}")

# Bài 3.4: Named tuples
print("\n--- Bài 3.4: Named tuples ---")

from collections import namedtuple

# Tạo named tuple cho sinh viên
Student = namedtuple('Student', ['name', 'age', 'grade', 'major'])

# Tạo instances
student1 = Student("Trần Thị B", 20, 8.5, "Tin học")
student2 = Student("Lê Văn C", 21, 7.8, "Toán học")

print(f"Sinh viên 1: {student1}")
print(f"Tên: {student1.name}, Điểm: {student1.grade}")

# Convert to dict
student_dict = student1._asdict()
print(f"Chuyển thành dict: {student_dict}")

# ============================================================================
# PHẦN 4: SET OPERATIONS - CÁC PHÉP TOÁN TẬP HỢP (15 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 4: SET OPERATIONS - CÁC PHÉP TOÁN TẬP HỢP")
print("=" * 60)

# Bài 4.1: Các phép toán cơ bản
print("\n--- Bài 4.1: Các phép toán cơ bản ---")

# Tạo các tập hợp
python_students = {"An", "Bình", "Châu", "Dũng", "Em"}
java_students = {"Bình", "Châu", "Phúc", "Giang", "Hải"}

print(f"Học Python: {python_students}")
print(f"Học Java: {java_students}")

# Hợp (Union) - Học ít nhất 1 môn
all_students = python_students | java_students
print(f"Học ít nhất 1 môn: {all_students}")

# Giao (Intersection) - Học cả 2 môn  
both_languages = python_students & java_students
print(f"Học cả 2 môn: {both_languages}")

# Hiệu (Difference) - Chỉ học Python
only_python = python_students - java_students
print(f"Chỉ học Python: {only_python}")

# Hiệu đối xứng (Symmetric difference) - Học đúng 1 môn
exactly_one = python_students ^ java_students
print(f"Học đúng 1 môn: {exactly_one}")

# Bài 4.2: Set methods cho thêm/xóa
print("\n--- Bài 4.2: Set methods cho thêm/xóa ---")

colors = {"đỏ", "xanh", "vàng"}
print(f"Màu ban đầu: {colors}")

# Thêm một phần tử
colors.add("tím")
print(f"Sau khi add 'tím': {colors}")

# Thêm nhiều phần tử
colors.update(["hồng", "cam", "nâu"])
print(f"Sau khi update: {colors}")

# Xóa phần tử (raise error nếu không tồn tại)
colors.remove("vàng")
print(f"Sau khi remove 'vàng': {colors}")

# Xóa phần tử (không error nếu không tồn tại)
colors.discard("trắng")  # không có 'trắng' nhưng không lỗi
colors.discard("đỏ")     # có 'đỏ' và sẽ xóa
print(f"Sau khi discard: {colors}")

# Xóa và trả về phần tử ngẫu nhiên
random_color = colors.pop()
print(f"Pop ra: {random_color}, còn lại: {colors}")

# Bài 4.3: Kiểm tra quan hệ tập hợp
print("\n--- Bài 4.3: Kiểm tra quan hệ tập hợp ---")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {6, 7, 8}
set_d = {1, 2}

print(f"A = {set_a}")
print(f"B = {set_b}")
print(f"C = {set_c}")
print(f"D = {set_d}")

# Kiểm tra tập con
print(f"A là tập con của B: {set_a.issubset(set_b)}")
print(f"D là tập con của A: {set_d.issubset(set_a)}")

# Kiểm tra tập cha
print(f"B là tập cha của A: {set_b.issuperset(set_a)}")
print(f"A là tập cha của D: {set_a.issuperset(set_d)}")

# Kiểm tra rời nhau
print(f"A và C rời nhau: {set_a.isdisjoint(set_c)}")
print(f"A và B rời nhau: {set_a.isdisjoint(set_b)}")

# ============================================================================
# PHẦN 5: SET COMPREHENSIONS (10 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 5: SET COMPREHENSIONS")
print("=" * 60)

# Bài 5.1: Set comprehension cơ bản
print("\n--- Bài 5.1: Set comprehension cơ bản ---")

# Tạo set các số chính phương
squares_set = {x**2 for x in range(10)}
print(f"Số chính phương từ 0-9: {squares_set}")

# Tạo set các ký tự trong chuỗi
text = "Hello World"
unique_chars = {char.lower() for char in text if char.isalpha()}
print(f"Ký tự duy nhất trong '{text}': {unique_chars}")

# Bài 5.2: Set comprehension với điều kiện
print("\n--- Bài 5.2: Set comprehension với điều kiện ---")

# Số chia hết cho 3 hoặc 5
divisible = {x for x in range(30) if x % 3 == 0 or x % 5 == 0}
print(f"Số chia hết cho 3 hoặc 5 (0-29): {divisible}")

# Từ có độ dài chẵn
words = ["python", "java", "c", "javascript", "go", "rust"]
even_length_words = {word for word in words if len(word) % 2 == 0}
print(f"Từ có độ dài chẵn: {even_length_words}")

# ============================================================================
# PHẦN 6: PERFORMANCE VÀ MEMORY OPTIMIZATION (8 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 6: PERFORMANCE VÀ MEMORY OPTIMIZATION")
print("=" * 60)

# Bài 6.1: So sánh hiệu suất lookup
print("\n--- Bài 6.1: So sánh hiệu suất lookup ---")

import time

# Tạo dữ liệu test
large_list = list(range(10000))
large_set = set(range(10000))
target = 9999

# Test lookup trong list
start = time.time()
found_in_list = target in large_list
list_time = time.time() - start

# Test lookup trong set
start = time.time()
found_in_set = target in large_set
set_time = time.time() - start

print(f"Lookup trong list: {list_time:.6f}s")
print(f"Lookup trong set: {set_time:.6f}s")
print(f"Set nhanh hơn list: {list_time/set_time:.2f} lần")

# Bài 6.2: Memory usage comparison
print("\n--- Bài 6.2: Memory usage comparison ---")

import sys

sample_list = [i for i in range(1000)]
sample_tuple = tuple(range(1000))
sample_set = {i for i in range(1000)}

print(f"Memory usage của list: {sys.getsizeof(sample_list)} bytes")
print(f"Memory usage của tuple: {sys.getsizeof(sample_tuple)} bytes")
print(f"Memory usage của set: {sys.getsizeof(sample_set)} bytes")

# ============================================================================
# PHẦN 7: ADVANCED OPERATIONS VÀ ALGORITHMS (12 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 7: ADVANCED OPERATIONS VÀ ALGORITHMS")
print("=" * 60)

# Bài 7.1: Tìm phần tử phổ biến nhất
print("\n--- Bài 7.1: Tìm phần tử phổ biến nhất ---")

from collections import Counter

votes = ["Python", "Java", "Python", "C++", "Python", "Java", "JavaScript"]
vote_counts = Counter(votes)
print(f"Kết quả bỏ phiếu: {vote_counts}")

most_popular = vote_counts.most_common(1)[0]
print(f"Ngôn ngữ phổ biến nhất: {most_popular[0]} với {most_popular[1]} vote")

# Bài 7.2: Loại bỏ duplicates giữ thứ tự
print("\n--- Bài 7.2: Loại bỏ duplicates giữ thứ tự ---")

def remove_duplicates_preserve_order(items):
    """Loại bỏ duplicates nhưng giữ thứ tự xuất hiện đầu tiên"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers_with_dups = [1, 3, 5, 3, 7, 1, 9, 5, 2]
unique_numbers = remove_duplicates_preserve_order(numbers_with_dups)
print(f"Có duplicates: {numbers_with_dups}")
print(f"Không duplicates (giữ thứ tự): {unique_numbers}")

# So sánh với set (không giữ thứ tự)
unique_set = list(set(numbers_with_dups))
print(f"Dùng set (không giữ thứ tự): {unique_set}")

# Bài 7.3: Merge và sort multiple lists
print("\n--- Bài 7.3: Merge và sort multiple lists ---")

list1 = [1, 5, 9, 13]
list2 = [2, 6, 10]
list3 = [3, 7, 11, 15, 17]

# Merge tất cả
merged = list1 + list2 + list3
merged.sort()
print(f"Merged và sorted: {merged}")

# Sử dụng heapq để merge efficiently (khi lists đã sorted)
import heapq
list1_sorted = [1, 5, 9, 13]
list2_sorted = [2, 6, 10, 14]
list3_sorted = [3, 7, 11, 15]

merged_efficient = list(heapq.merge(list1_sorted, list2_sorted, list3_sorted))
print(f"Merge hiệu quả với heapq: {merged_efficient}")

# ============================================================================
# PHẦN 8: REAL-WORLD APPLICATIONS (10 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 8: REAL-WORLD APPLICATIONS")
print("=" * 60)

# Bài 8.1: Phân tích dữ liệu text
print("\n--- Bài 8.1: Phân tích dữ liệu text ---")

def analyze_text(text):
    """Phân tích văn bản và trả về thống kê"""
    words = text.lower().split()
    
    # Tính toán các metrics
    word_count = len(words)
    unique_words = set(words)
    unique_count = len(unique_words)
    
    # Tìm từ xuất hiện nhiều nhất
    word_freq = Counter(words)
    most_common = word_freq.most_common(3)
    
    # Độ dài từ trung bình
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        'total_words': word_count,
        'unique_words': unique_count,
        'diversity_ratio': unique_count / word_count if word_count > 0 else 0,
        'most_common': most_common,
        'avg_word_length': avg_length
    }

sample_text = """
Python là một ngôn ngữ lập trình cấp cao, được thiết kế với triết lý 
mã nguồn rõ ràng và cú pháp cho phép lập trình viên có thể diễn đạt 
khái niệm bằng ít dòng code hơn so với các ngôn ngữ như C++ hay Java.
Python hỗ trợ nhiều mô hình lập trình khác nhau.
"""

analysis = analyze_text(sample_text)
print("Phân tích văn bản:")
for key, value in analysis.items():
    print(f"  {key}: {value}")

# Bài 8.2: Hệ thống tag và category
print("\n--- Bài 8.2: Hệ thống tag và category ---")

class ContentManager:
    """Quản lý nội dung với tags và categories"""
    
    def __init__(self):
        self.contents = {}  # id -> {title, tags, category}
        self.tag_index = {}  # tag -> set of content ids
        self.category_index = {}  # category -> set of content ids
    
    def add_content(self, content_id, title, tags, category):
        """Thêm nội dung mới"""
        self.contents[content_id] = {
            'title': title,
            'tags': set(tags),
            'category': category
        }
        
        # Update indices
        for tag in tags:
            if tag not in self.tag_index:
                self.tag_index[tag] = set()
            self.tag_index[tag].add(content_id)
        
        if category not in self.category_index:
            self.category_index[category] = set()
        self.category_index[category].add(content_id)
    
    def find_by_tags(self, tags):
        """Tìm nội dung có chứa các tags"""
        if not tags:
            return set()
        
        result = self.tag_index.get(tags[0], set()).copy()
        for tag in tags[1:]:
            result &= self.tag_index.get(tag, set())
        return result
    
    def find_similar_content(self, content_id):
        """Tìm nội dung tương tự dựa trên tags chung"""
        if content_id not in self.contents:
            return set()
        
        content_tags = self.contents[content_id]['tags']
        similar = set()
        
        for tag in content_tags:
            similar |= self.tag_index.get(tag, set())
        
        similar.discard(content_id)  # Loại bỏ chính nó
        return similar

# Test content manager
cm = ContentManager()

# Thêm một số nội dung
cm.add_content(1, "Học Python cơ bản", ["python", "programming", "beginner"], "education")
cm.add_content(2, "Advanced Python", ["python", "programming", "advanced"], "education")
cm.add_content(3, "Python for AI", ["python", "ai", "machine-learning"], "technology")
cm.add_content(4, "Java Tutorial", ["java", "programming", "beginner"], "education")

# Test tìm kiếm
python_content = cm.find_by_tags(["python"])
print(f"Nội dung về Python: {python_content}")

programming_beginner = cm.find_by_tags(["programming", "beginner"])
print(f"Nội dung programming cho beginner: {programming_beginner}")

similar_to_1 = cm.find_similar_content(1)
print(f"Nội dung tương tự với ID 1: {similar_to_1}")

# ============================================================================
# PHẦN 9: ERROR HANDLING VÀ BEST PRACTICES (8 BÀI TẬP)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 9: ERROR HANDLING VÀ BEST PRACTICES")
print("=" * 60)

# Bài 9.1: Safe operations với try-except
print("\n--- Bài 9.1: Safe operations với try-except ---")

def safe_list_operations(lst, index=None, value=None, operation="get"):
    """Thực hiện các thao tác list một cách an toàn"""
    try:
        if operation == "get":
            return lst[index] if index is not None else None
        elif operation == "remove":
            lst.remove(value)
            return f"Đã xóa {value}"
        elif operation == "index":
            return lst.index(value)
        elif operation == "pop":
            return lst.pop(index) if index is not None else lst.pop()
    except IndexError:
        return f"Lỗi: Index {index} nằm ngoài phạm vi của list"
    except ValueError:
        return f"Lỗi: Giá trị {value} không có trong list"
    except Exception as e:
        return f"Lỗi không xác định: {e}"

# Test safe operations
test_list = [1, 2, 3, 4, 5]
print(f"Test list: {test_list}")

print(safe_list_operations(test_list, index=2, operation="get"))
print(safe_list_operations(test_list, index=10, operation="get"))
print(safe_list_operations(test_list, value=3, operation="remove"))
print(safe_list_operations(test_list, value=10, operation="remove"))

# Bài 9.2: Input validation
print("\n--- Bài 9.2: Input validation ---")

def validate_and_process_data(data):
    """Validate và xử lý dữ liệu đầu vào"""
    # Kiểm tra type
    if not isinstance(data, (list, tuple, set)):
        return None, "Dữ liệu phải là list, tuple hoặc set"
    
    # Convert to list để xử lý
    data_list = list(data)
    
    # Kiểm tra empty
    if not data_list:
        return None, "Dữ liệu không được rỗng"
    
    # Kiểm tra type của elements
    if not all(isinstance(x, (int, float)) for x in data_list):
        return None, "Tất cả phần tử phải là số"
    
    # Xử lý dữ liệu
    result = {
        'original': data,
        'type': type(data).__name__,
        'length': len(data_list),
        'sum': sum(data_list),
        'average': sum(data_list) / len(data_list),
        'min': min(data_list),
        'max': max(data_list),
        'unique_count': len(set(data_list))
    }
    
    return result, "Thành công"

# Test validation
test_cases = [
    [1, 2, 3, 4, 5],
    (1.5, 2.5, 3.5),
    {1, 2, 3, 3, 4},
    [],
    [1, 2, "3", 4],
    "not a list",
    None
]

for i, case in enumerate(test_cases):
    result, message = validate_and_process_data(case)
    print(f"Test {i+1}: {message}")
    if result:
        print(f"  Kết quả: Average = {result['average']:.2f}, Unique = {result['unique_count']}")

# ============================================================================
# PHẦN 10: THỰC HÀNH TỔNG HỢP (5 DỰ ÁN NHỎ)
# ============================================================================

print("\n" + "=" * 60)
print("PHẦN 10: THỰC HÀNH TỔNG HỢP - 5 DỰ ÁN NHỎ")
print("=" * 60)

# Dự án 1: Phân tích điểm thi
print("\n--- DỰ ÁN 1: Phân tích điểm thi ---")

class GradeAnalyzer:
    """Hệ thống phân tích điểm thi"""
    
    def __init__(self):
        self.grades = []
        self.subjects = set()
        self.students = {}
    
    def add_grade(self, student_name, subject, score):
        """Thêm điểm cho học sinh"""
        if not (0 <= score <= 10):
            raise ValueError("Điểm phải từ 0 đến 10")
        
        grade_record = {
            'student': student_name,
            'subject': subject,
            'score': score
        }
        
        self.grades.append(grade_record)
        self.subjects.add(subject)
        
        if student_name not in self.students:
            self.students[student_name] = []
        self.students[student_name].append(grade_record)
    
    def get_statistics(self):
        """Lấy thống kê tổng quan"""
        if not self.grades:
            return {}
        
        all_scores = [grade['score'] for grade in self.grades]
        
        return {
            'total_records': len(self.grades),
            'total_students': len(self.students),
            'total_subjects': len(self.subjects),
            'average_score': sum(all_scores) / len(all_scores),
            'highest_score': max(all_scores),
            'lowest_score': min(all_scores),
            'pass_rate': len([s for s in all_scores if s >= 5]) / len(all_scores) * 100
        }
    
    def get_top_students(self, n=3):
        """Lấy top học sinh giỏi nhất"""
        student_averages = {}
        for student, grades in self.students.items():
            avg = sum(g['score'] for g in grades) / len(grades)
            student_averages[student] = avg
        
        sorted_students = sorted(student_averages.items(), 
                               key=lambda x: x[1], reverse=True)
        return sorted_students[:n]

# Test grade analyzer
analyzer = GradeAnalyzer()

# Thêm dữ liệu mẫu
sample_data = [
    ("Nguyễn Văn A", "Toán", 8.5),
    ("Nguyễn Văn A", "Lý", 7.0),
    ("Nguyễn Văn A", "Hóa", 8.0),
    ("Trần Thị B", "Toán", 9.0),
    ("Trần Thị B", "Lý", 8.5),
    ("Trần Thị B", "Hóa", 9.5),
    ("Lê Văn C", "Toán", 6.0),
    ("Lê Văn C", "Lý", 5.5),
    ("Lê Văn C", "Hóa", 6.5),
]

for student, subject, score in sample_data:
    analyzer.add_grade(student, subject, score)

# Hiển thị thống kê
stats = analyzer.get_statistics()
print("Thống kê điểm thi:")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# Top học sinh
top_students = analyzer.get_top_students()
print("\nTop 3 học sinh:")
for i, (student, avg) in enumerate(top_students, 1):
    print(f"  {i}. {student}: {avg:.2f}")

# Dự án 2: Quản lý playlist nhạc
print("\n--- DỰ ÁN 2: Quản lý playlist nhạc ---")

class MusicPlaylist:
    """Hệ thống quản lý playlist nhạc"""
    
    def __init__(self, name):
        self.name = name
        self.songs = []  # Ordered list to maintain sequence
        self.song_set = set()  # For fast lookup
        self.current_index = 0
        self.history = []  # Recently played songs
    
    def add_song(self, title, artist, duration):
        """Thêm bài hát vào playlist"""
        song_id = f"{title}_{artist}".lower()
        
        if song_id in self.song_set:
            print(f"Bài hát '{title}' của {artist} đã có trong playlist")
            return False
        
        song = {
            'id': song_id,
            'title': title,
            'artist': artist,
            'duration': duration  # in seconds
        }
        
        self.songs.append(song)
        self.song_set.add(song_id)
        print(f"Đã thêm: {title} - {artist}")
        return True
    
    def remove_song(self, title, artist):
        """Xóa bài hát khỏi playlist"""
        song_id = f"{title}_{artist}".lower()
        
        if song_id not in self.song_set:
            print(f"Không tìm thấy bài hát '{title}' của {artist}")
            return False
        
        # Remove from both structures
        self.songs = [s for s in self.songs if s['id'] != song_id]
        self.song_set.remove(song_id)
        
        # Adjust current index if necessary
        if self.current_index >= len(self.songs):
            self.current_index = 0
        
        print(f"Đã xóa: {title} - {artist}")
        return True
    
    def shuffle(self):
        """Trộn ngẫu nhiên playlist"""
        import random
        random.shuffle(self.songs)
        self.current_index = 0
        print("Đã trộn playlist")
    
    def get_current_song(self):
        """Lấy bài hát hiện tại"""
        if not self.songs:
            return None
        return self.songs[self.current_index]
    
    def next_song(self):
        """Chuyển đến bài hát tiếp theo"""
        if not self.songs:
            return None
        
        # Add current to history
        current = self.get_current_song()
        if current:
            self.history.append(current['id'])
            if len(self.history) > 10:  # Keep only last 10
                self.history.pop(0)
        
        self.current_index = (self.current_index + 1) % len(self.songs)
        return self.get_current_song()
    
    def find_songs_by_artist(self, artist):
        """Tìm bài hát theo nghệ sĩ"""
        return [song for song in self.songs 
                if artist.lower() in song['artist'].lower()]
    
    def get_total_duration(self):
        """Tính tổng thời lượng playlist"""
        total_seconds = sum(song['duration'] for song in self.songs)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Test music playlist
playlist = MusicPlaylist("My Favorites")

# Thêm bài hát
songs_to_add = [
    ("Shape of You", "Ed Sheeran", 234),
    ("Blinding Lights", "The Weeknd", 200),
    ("Bohemian Rhapsody", "Queen", 355),
    ("Hotel California", "Eagles", 391),
    ("Imagine", "John Lennon", 183),
]

for title, artist, duration in songs_to_add:
    playlist.add_song(title, artist, duration)

print(f"\nPlaylist '{playlist.name}':")
print(f"Số bài hát: {len(playlist.songs)}")
print(f"Tổng thời lượng: {playlist.get_total_duration()}")

# Test các chức năng
print(f"\nBài hát hiện tại: {playlist.get_current_song()['title']}")
next_song = playlist.next_song()
print(f"Bài hát tiếp theo: {next_song['title']}")

# Tìm bài hát
ed_songs = playlist.find_songs_by_artist("Ed Sheeran")
print(f"\nBài hát của Ed Sheeran: {[s['title'] for s in ed_songs]}")

print("\n" + "="*60)
print("HOÀN THÀNH BÀI TẬP 3: METHODS VÀ OPERATIONS")
print("Bạn đã thực hành:")
print("✓ Tất cả methods của Lists, Tuples, Sets")
print("✓ List comprehensions và Set comprehensions") 
print("✓ Performance optimization")
print("✓ Error handling và best practices")
print("✓ Các dự án thực tế")
print("="*60) 