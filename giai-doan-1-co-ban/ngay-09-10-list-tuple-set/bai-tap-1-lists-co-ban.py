"""
=== BÀI TẬP 1: LISTS CƠ BẢN ===
Ngày 9-10: Lists, Tuples, Sets
Chủ đề: Lists fundamentals, indexing, slicing, basic operations

Bài tập này gồm 10 sections:
1. Tạo và khởi tạo Lists
2. Indexing và truy cập phần tử
3. Slicing cơ bản
4. Slicing nâng cao
5. Membership testing
6. List concatenation và repetition
7. List information và built-in functions
8. Basic list modification
9. List comparison và sorting
10. Practical applications

Mỗi section có 5-6 bài tập từ easy đến hard.
"""

print("🐍 BÀI TẬP 1: LISTS CƠ BẢN")
print("=" * 50)

# =============================================================================
# SECTION 1: TẠO VÀ KHỞI TẠO LISTS
# =============================================================================

print("\n📝 SECTION 1: TẠO VÀ KHỞI TẠO LISTS")
print("-" * 40)

# Bài 1.1: Tạo các loại lists khác nhau
print("Bài 1.1: Tạo lists")
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Bài 1.2: Tạo list từ range
print("\nBài 1.2: Tạo list từ range")
range_list = list(range(10))
even_range = list(range(0, 20, 2))
odd_range = list(range(1, 20, 2))
reverse_range = list(range(10, 0, -1))
print(f"Range 0-9: {range_list}")
print(f"Even 0-18: {even_range}")
print(f"Odd 1-19: {odd_range}")
print(f"Reverse 10-1: {reverse_range}")

# Bài 1.3: List repetition
print("\nBài 1.3: List repetition")
zeros = [0] * 5
ones = [1] * 10
pattern = [1, 2] * 3
nested_pattern = [[0] * 3] * 2  # Chú ý: shallow copy!
print(f"5 zeros: {zeros}")
print(f"10 ones: {ones}")
print(f"Pattern [1,2]*3: {pattern}")
print(f"Nested pattern: {nested_pattern}")

# Bài 1.4: Nested lists
print("\nBài 1.4: Nested lists")
matrix_2x2 = [[1, 2], [3, 4]]
matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mixed_nested = [1, [2, 3], "hello", [True, False]]
print(f"2x2 matrix: {matrix_2x2}")
print(f"3x3 matrix: {matrix_3x3}")
print(f"Mixed nested: {mixed_nested}")

# Bài 1.5: Tạo list từ string
print("\nBài 1.5: Tạo list từ string")
char_list = list("hello")
word_list = "Python is awesome".split()
csv_data = "apple,banana,orange".split(",")
print(f"Characters: {char_list}")
print(f"Words: {word_list}")
print(f"CSV data: {csv_data}")

# Thực hành Section 1
print("\n🎯 THỰC HÀNH SECTION 1:")

# Bài tập 1.1
print("1. Tạo list chứa bình phương của các số từ 1 đến 10")
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(f"Bình phương 1-10: {squares}")

# Bài tập 1.2
print("2. Tạo list chứa tên các tháng trong năm")
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
print(f"Số tháng: {len(months)}")
print(f"3 tháng đầu: {months[:3]}")

# Bài tập 1.3
print("3. Tạo ma trận đơn vị 3x3")
identity_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity_matrix.append(row)
print(f"Ma trận đơn vị 3x3: {identity_matrix}")

# =============================================================================
# SECTION 2: INDEXING VÀ TRUY CẬP PHẦN TỬ
# =============================================================================

print("\n📝 SECTION 2: INDEXING VÀ TRUY CẬP PHẦN TỬ")
print("-" * 40)

# Bài 2.1: Positive indexing
print("Bài 2.1: Positive indexing")
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Last color: {colors[4]}")
print(f"Middle color: {colors[2]}")

# Bài 2.2: Negative indexing
print("\nBài 2.2: Negative indexing")
print(f"Last color: {colors[-1]}")
print(f"Second last: {colors[-2]}")
print(f"Third last: {colors[-3]}")
print(f"First (negative): {colors[-5]}")

# Bài 2.3: Truy cập nested lists
print("\nBài 2.3: Truy cập nested lists")
student_grades = [
    ["Alice", [85, 90, 78]],
    ["Bob", [92, 88, 95]],
    ["Charlie", [78, 85, 82]]
]
print(f"Student data: {student_grades}")
print(f"First student name: {student_grades[0][0]}")
print(f"Alice's first grade: {student_grades[0][1][0]}")
print(f"Bob's grades: {student_grades[1][1]}")
print(f"Charlie's last grade: {student_grades[2][1][-1]}")

# Bài 2.4: Dynamic indexing
print("\nBài 2.4: Dynamic indexing")
data = [10, 20, 30, 40, 50]
for i in range(len(data)):
    print(f"Index {i}: {data[i]}")

# Bài 2.5: Safe indexing
print("\nBài 2.5: Safe indexing")
numbers = [1, 2, 3]
safe_index = 5

try:
    value = numbers[safe_index]
    print(f"Value at index {safe_index}: {value}")
except IndexError:
    print(f"Index {safe_index} is out of range for list of length {len(numbers)}")

# Thực hành Section 2
print("\n🎯 THỰC HÀNH SECTION 2:")

# Bài tập 2.1
print("1. Truy cập và in ra từng phần tử với index của nó")
animals = ["cat", "dog", "bird", "fish", "rabbit"]
for i in range(len(animals)):
    print(f"  Index {i}: {animals[i]}")

# Bài tập 2.2
print("2. Lấy phần tử đầu, giữa và cuối của list")
scores = [85, 92, 78, 96, 88, 91, 84]
first = scores[0]
middle = scores[len(scores) // 2]
last = scores[-1]
print(f"  Đầu: {first}, Giữa: {middle}, Cuối: {last}")

# Bài tập 2.3
print("3. Truy cập ma trận 2D")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"  Phần tử [1][2]: {matrix[1][2]}")
print(f"  Đường chéo chính: {[matrix[i][i] for i in range(len(matrix))]}")

# =============================================================================
# SECTION 3: SLICING CƠ BẢN
# =============================================================================

print("\n📝 SECTION 3: SLICING CƠ BẢN")
print("-" * 40)

# Bài 3.1: Basic slicing
print("Bài 3.1: Basic slicing")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f"Alphabet: {alphabet}")
print(f"First 3: {alphabet[:3]}")
print(f"Last 3: {alphabet[-3:]}")
print(f"Middle (3-7): {alphabet[3:7]}")
print(f"All: {alphabet[:]}")

# Bài 3.2: Slicing với step
print("\nBài 3.2: Slicing với step")
numbers = list(range(0, 20))
print(f"Numbers: {numbers}")
print(f"Every 2nd: {numbers[::2]}")
print(f"Every 3rd: {numbers[::3]}")
print(f"Reverse: {numbers[::-1]}")
print(f"Every 2nd reverse: {numbers[::-2]}")

# Bài 3.3: Slicing với negative indices
print("\nBài 3.3: Slicing với negative indices")
text = "Hello World"
chars = list(text)
print(f"Characters: {chars}")
print(f"Last 5: {chars[-5:]}")
print(f"All except last 2: {chars[:-2]}")
print(f"From -7 to -2: {chars[-7:-2]}")

# Bài 3.4: Copying với slicing
print("\nBài 3.4: Copying với slicing")
original = [1, 2, 3, 4, 5]
copy1 = original[:]
copy2 = original.copy()
copy3 = list(original)

original[0] = 999
print(f"Original after change: {original}")
print(f"Copy1 (slice): {copy1}")
print(f"Copy2 (method): {copy2}")
print(f"Copy3 (constructor): {copy3}")

# Bài 3.5: Slicing for extraction
print("\nBài 3.5: Slicing for extraction")
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_half = data[:len(data)//2]
second_half = data[len(data)//2:]
odds_positions = data[1::2]  # positions 1, 3, 5, ...
evens_positions = data[::2]  # positions 0, 2, 4, ...

print(f"Data: {data}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")
print(f"Odd positions: {odds_positions}")
print(f"Even positions: {evens_positions}")

# Thực hành Section 3
print("\n🎯 THỰC HÀNH SECTION 3:")

# Bài tập 3.1
print("1. Tách list thành 3 phần bằng nhau")
long_list = list(range(1, 31))  # 1-30
third = len(long_list) // 3
part1 = long_list[:third]
part2 = long_list[third:2*third]
part3 = long_list[2*third:]
print(f"  Part 1: {part1}")
print(f"  Part 2: {part2}")
print(f"  Part 3: {part3}")

# Bài tập 3.2
print("2. Lấy mỗi phần tử thứ n từ list")
source = list(range(1, 21))
every_2nd = source[::2]
every_3rd = source[::3]
every_4th = source[::4]
print(f"  Every 2nd: {every_2nd}")
print(f"  Every 3rd: {every_3rd}")
print(f"  Every 4th: {every_4th}")

# =============================================================================
# SECTION 4: SLICING NÂNG CAO
# =============================================================================

print("\n📝 SECTION 4: SLICING NÂNG CAO")
print("-" * 40)

# Bài 4.1: Complex slicing patterns
print("Bài 4.1: Complex slicing patterns")
data = list(range(1, 21))  # 1-20
print(f"Data: {data}")

# Lấy 3 phần tử đầu và 3 phần tử cuối
head_tail = data[:3] + data[-3:]
print(f"Head + Tail: {head_tail}")

# Lấy phần tử ở index chẵn từ nửa đầu list
first_half_evens = data[:len(data)//2:2]
print(f"First half evens: {first_half_evens}")

# Lấy phần tử từ giữa về hai phía
mid = len(data) // 2
around_middle = data[mid-2:mid+3]
print(f"Around middle: {around_middle}")

# Bài 4.2: Slicing with computed indices
print("\nBài 4.2: Slicing with computed indices")
scores = [85, 92, 78, 96, 88, 91, 84, 79, 93, 87]
n = len(scores)

# Top 30%
top_30_count = int(n * 0.3)
top_30_percent = sorted(scores, reverse=True)[:top_30_count]
print(f"Scores: {scores}")
print(f"Top 30%: {top_30_percent}")

# Bottom 20%
bottom_20_count = int(n * 0.2)
bottom_20_percent = sorted(scores)[:bottom_20_count]
print(f"Bottom 20%: {bottom_20_percent}")

# Bài 4.3: Palindrome checking với slicing
print("\nBài 4.3: Palindrome checking")
def is_palindrome(lst):
    return lst == lst[::-1]

test_lists = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'b', 'a'],
    [1, 2, 2, 1]
]

for test_list in test_lists:
    result = is_palindrome(test_list)
    print(f"  {test_list} is palindrome: {result}")

# Bài 4.4: Matrix operations với slicing
print("\nBài 4.4: Matrix operations")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Lấy cột đầu tiên
first_column = [row[0] for row in matrix]
print(f"First column: {first_column}")

# Lấy đường chéo chính
main_diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Main diagonal: {main_diagonal}")

# Lấy hàng thứ 2
second_row = matrix[1]
print(f"Second row: {second_row}")

# Lấy submatrix 2x2 từ góc trái trên
submatrix = [row[:2] for row in matrix[:2]]
print(f"2x2 submatrix: {submatrix}")

# Bài 4.5: Advanced pattern extraction
print("\nBài 4.5: Advanced pattern extraction")
sequence = list(range(1, 101))  # 1-100

# Lấy số chia hết cho 7
divisible_by_7 = [x for x in sequence if x % 7 == 0]
print(f"Divisible by 7: {divisible_by_7[:5]}...")  # Show first 5

# Lấy số có chữ số cuối là 3 hoặc 7
ending_3_or_7 = [x for x in sequence if x % 10 in [3, 7]]
print(f"Ending in 3 or 7: {ending_3_or_7[:10]}...")  # Show first 10

# Thực hành Section 4
print("\n🎯 THỰC HÀNH SECTION 4:")

# Bài tập 4.1
print("1. Tạo pattern zigzag từ list")
numbers = list(range(1, 21))
# Lấy 2 phần tử đầu, bỏ 1, lấy 2, bỏ 1, ...
zigzag = []
i = 0
while i < len(numbers):
    if i + 1 < len(numbers):
        zigzag.extend([numbers[i], numbers[i+1]])
    else:
        zigzag.append(numbers[i])
    i += 3
print(f"  Zigzag pattern: {zigzag}")

# =============================================================================
# SECTION 5: MEMBERSHIP TESTING
# =============================================================================

print("\n📝 SECTION 5: MEMBERSHIP TESTING")
print("-" * 40)

# Bài 5.1: Basic membership testing
print("Bài 5.1: Basic membership testing")
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"Fruits: {fruits}")

test_fruits = ["apple", "mango", "banana", "pear"]
for fruit in test_fruits:
    if fruit in fruits:
        print(f"  ✓ {fruit} có trong danh sách")
    else:
        print(f"  ✗ {fruit} không có trong danh sách")

# Bài 5.2: Not in operator
print("\nBài 5.2: Not in operator")
valid_grades = ['A', 'B', 'C', 'D', 'F']
student_grades = ['A', 'B', 'X', 'C', 'Y']

invalid_grades = []
for grade in student_grades:
    if grade not in valid_grades:
        invalid_grades.append(grade)

print(f"Valid grades: {valid_grades}")
print(f"Student grades: {student_grades}")
print(f"Invalid grades: {invalid_grades}")

# Bài 5.3: Membership với numbers
print("\nBài 5.3: Membership với numbers")
even_numbers = [x for x in range(2, 21, 2)]
test_numbers = [5, 8, 12, 15, 18, 25]

print(f"Even numbers: {even_numbers}")
for num in test_numbers:
    status = "even" if num in even_numbers else "odd/out of range"
    print(f"  {num} is {status}")

# Bài 5.4: Nested membership testing
print("\nBài 5.4: Nested membership testing")
categories = [
    ["fiction", "mystery", "romance"],
    ["science", "math", "physics"],
    ["history", "biography", "politics"]
]

search_books = ["mystery", "chemistry", "math", "romance", "geography"]

for book in search_books:
    found = False
    for i, category in enumerate(categories):
        if book in category:
            category_names = ["Literature", "Science", "History"]
            print(f"  '{book}' found in {category_names[i]} category")
            found = True
            break
    if not found:
        print(f"  '{book}' not found in any category")

# Bài 5.5: Performance comparison
print("\nBài 5.5: Performance comparison")
import time

# Tạo data lớn
large_list = list(range(10000))
large_set = set(large_list)

search_value = 9999

# Test với list
start_time = time.time()
for _ in range(1000):
    result = search_value in large_list
list_time = time.time() - start_time

# Test với set
start_time = time.time()
for _ in range(1000):
    result = search_value in large_set
set_time = time.time() - start_time

print(f"List search time: {list_time:.6f}s")
print(f"Set search time: {set_time:.6f}s")
print(f"Set is {list_time/set_time:.1f}x faster")

# Thực hành Section 5
print("\n🎯 THỰC HÀNH SECTION 5:")

# Bài tập 5.1
print("1. Kiểm tra email hợp lệ")
valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
emails = ["user@gmail.com", "test@yahoo.com", "admin@company.com", "person@outlook.com"]

for email in emails:
    domain = email.split('@')[1] if '@' in email else ""
    if domain in valid_domains:
        print(f"  ✓ {email} - Valid domain")
    else:
        print(f"  ✗ {email} - Invalid domain")

# Bài tập 5.2
print("2. Tìm phần tử chung giữa các lists")
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [3, 4, 5, 10, 11]

common_elements = []
for item in list1:
    if item in list2 and item in list3:
        common_elements.append(item)

print(f"  Common elements: {common_elements}")

# =============================================================================
# SECTION 6: LIST CONCATENATION VÀ REPETITION
# =============================================================================

print("\n📝 SECTION 6: LIST CONCATENATION VÀ REPETITION")
print("-" * 40)

# Bài 6.1: Basic concatenation
print("Bài 6.1: Basic concatenation")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Sử dụng + operator
combined1 = list1 + list2
print(f"list1 + list2: {combined1}")

# Concatenate nhiều lists
combined2 = list1 + list2 + list3
print(f"list1 + list2 + list3: {combined2}")

# Sử dụng += operator (modify in place)
original = [1, 2, 3]
original += [4, 5, 6]
print(f"After +=: {original}")

# Bài 6.2: Repetition với *
print("\nBài 6.2: Repetition với *")
pattern = [1, 2]
repeated = pattern * 5
print(f"Pattern * 5: {repeated}")

zeros = [0] * 10
print(f"10 zeros: {zeros}")

separator = ['-'] * 20
print(f"Separator: {separator}")

# Bài 6.3: Combining concatenation và repetition
print("\nBài 6.3: Combining operations")
header = ['ID'] + ['Score'] * 3 + ['Grade']
print(f"Table header: {header}")

template = ['Name:', ''] + ['Subject:', ''] * 3
print(f"Form template: {template}")

# Tạo pattern phức tạp
pattern = ([1] * 3 + [0] * 2) * 4
print(f"Complex pattern: {pattern}")

# Bài 6.4: Building sequences
print("\nBài 6.4: Building sequences")
# Tạo chuỗi Fibonacci
fibonacci = [0, 1]
for i in range(8):
    fibonacci = fibonacci + [fibonacci[-1] + fibonacci[-2]]
print(f"Fibonacci: {fibonacci}")

# Tạo pattern pyramid
pyramid = []
for i in range(1, 6):
    level = [i] * i
    pyramid = pyramid + level
print(f"Pyramid: {pyramid}")

# Bài 6.5: List building with conditions
print("\nBài 6.5: Conditional building")
# Tạo list với pattern điều kiện
result = []
for i in range(1, 11):
    if i % 2 == 0:
        result = result + [i] * 2  # Even numbers appear twice
    else:
        result = result + [i]      # Odd numbers appear once
print(f"Conditional pattern: {result}")

# Thực hành Section 6
print("\n🎯 THỰC HÀNH SECTION 6:")

# Bài tập 6.1
print("1. Tạo bảng cửu chương dạng list")
multiplication_table = []
for i in range(1, 10):
    row = []
    for j in range(1, 10):
        row.append(i * j)
    multiplication_table.append(row)

print("  Bảng cửu chương (3 hàng đầu):")
for i in range(3):
    print(f"    {multiplication_table[i]}")

# Bài tập 6.2
print("2. Tạo ma trận chess board")
chess_board = []
for row in range(8):
    board_row = []
    for col in range(8):
        if (row + col) % 2 == 0:
            board_row.append('W')  # White
        else:
            board_row.append('B')  # Black
    chess_board.append(board_row)

print("  Chess board (4 hàng đầu):")
for i in range(4):
    print(f"    {chess_board[i]}")

# =============================================================================
# SECTION 7: LIST INFORMATION VÀ BUILT-IN FUNCTIONS
# =============================================================================

print("\n📝 SECTION 7: LIST INFORMATION VÀ BUILT-IN FUNCTIONS")
print("-" * 40)

# Bài 7.1: Basic list information
print("Bài 7.1: Basic list information")
scores = [85, 92, 78, 96, 88, 91, 84, 79, 93, 87]
print(f"Scores: {scores}")
print(f"Length: {len(scores)}")
print(f"Maximum: {max(scores)}")
print(f"Minimum: {min(scores)}")
print(f"Sum: {sum(scores)}")
print(f"Average: {sum(scores) / len(scores):.2f}")

# Bài 7.2: List methods for information
print("\nBài 7.2: List methods for information")
data = [1, 2, 3, 2, 4, 2, 5, 2]
print(f"Data: {data}")
print(f"Count of 2: {data.count(2)}")
print(f"Index of first 2: {data.index(2)}")
print(f"Index of 2 after position 3: {data.index(2, 4)}")

# Bài 7.3: Working với mixed data types
print("\nBài 7.3: Mixed data types")
mixed_data = [1, 2.5, 3, 4.7, 5]
numbers_only = [x for x in mixed_data if isinstance(x, (int, float))]
integers_only = [x for x in mixed_data if isinstance(x, int)]

print(f"Mixed data: {mixed_data}")
print(f"Numbers only: {numbers_only}")
print(f"Integers only: {integers_only}")
print(f"Sum of numbers: {sum(numbers_only)}")

# Bài 7.4: Statistical analysis
print("\nBài 7.4: Statistical analysis")
grades = [85, 92, 78, 96, 88, 91, 84, 79, 93, 87, 90, 85]
grades_sorted = sorted(grades)

# Calculate median
n = len(grades_sorted)
if n % 2 == 0:
    median = (grades_sorted[n//2 - 1] + grades_sorted[n//2]) / 2
else:
    median = grades_sorted[n//2]

# Calculate mode (most frequent)
grade_counts = {}
for grade in grades:
    grade_counts[grade] = grade_counts.get(grade, 0) + 1
mode = max(grade_counts, key=grade_counts.get)

print(f"Grades: {grades}")
print(f"Mean: {sum(grades) / len(grades):.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {max(grades) - min(grades)}")

# Bài 7.5: List analysis functions
print("\nBài 7.5: List analysis functions")
def analyze_list(lst):
    if not lst:
        return "Empty list"
    
    analysis = {
        'length': len(lst),
        'sum': sum(lst) if all(isinstance(x, (int, float)) for x in lst) else 'N/A',
        'average': sum(lst) / len(lst) if all(isinstance(x, (int, float)) for x in lst) else 'N/A',
        'min': min(lst),
        'max': max(lst),
        'unique_count': len(set(lst)),
        'has_duplicates': len(lst) != len(set(lst))
    }
    return analysis

test_lists = [
    [1, 2, 3, 4, 5],
    [1, 1, 2, 2, 3],
    ['a', 'b', 'c', 'a'],
    []
]

for i, test_list in enumerate(test_lists):
    print(f"List {i+1}: {test_list}")
    result = analyze_list(test_list)
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {result}")

# Thực hành Section 7
print("\n🎯 THỰC HÀNH SECTION 7:")

# Bài tập 7.1
print("1. Phân tích điểm thi")
exam_scores = [95, 87, 92, 78, 85, 90, 88, 76, 94, 89, 82, 91]
total_students = len(exam_scores)
passed = sum(1 for score in exam_scores if score >= 80)
failed = total_students - passed
highest = max(exam_scores)
lowest = min(exam_scores)

print(f"  Total students: {total_students}")
print(f"  Passed (≥80): {passed} ({passed/total_students*100:.1f}%)")
print(f"  Failed (<80): {failed} ({failed/total_students*100:.1f}%)")
print(f"  Highest score: {highest}")
print(f"  Lowest score: {lowest}")
print(f"  Class average: {sum(exam_scores)/len(exam_scores):.1f}")

# =============================================================================
# SECTION 8: BASIC LIST MODIFICATION
# =============================================================================

print("\n📝 SECTION 8: BASIC LIST MODIFICATION")
print("-" * 40)

# Bài 8.1: Modifying elements by index
print("Bài 8.1: Modifying elements by index")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

numbers[0] = 10
numbers[-1] = 50
numbers[2] = numbers[1] * 2
print(f"After modifications: {numbers}")

# Bài 8.2: Modifying multiple elements
print("\nBài 8.2: Modifying multiple elements")
data = [0, 0, 0, 0, 0, 0, 0, 0]
print(f"Original: {data}")

# Modify slice
data[2:5] = [20, 30, 40]
print(f"After slice modification: {data}")

# Replace with different length
data[1:3] = [100, 200, 300, 400]
print(f"After length-changing replacement: {data}")

# Bài 8.3: List modification with conditions
print("\nBài 8.3: Conditional modification")
scores = [75, 85, 65, 95, 55, 88, 72, 91]
print(f"Original scores: {scores}")

# Add bonus points to low scores
for i in range(len(scores)):
    if scores[i] < 70:
        scores[i] += 10  # Bonus points
        
print(f"After bonus: {scores}")

# Cap maximum score at 100
for i in range(len(scores)):
    if scores[i] > 100:
        scores[i] = 100
        
print(f"After capping: {scores}")

# Bài 8.4: Swapping elements
print("\nBài 8.4: Swapping elements")
arrangement = ['A', 'B', 'C', 'D', 'E']
print(f"Original arrangement: {arrangement}")

# Swap first and last
arrangement[0], arrangement[-1] = arrangement[-1], arrangement[0]
print(f"After swapping first and last: {arrangement}")

# Swap adjacent pairs
temp_list = arrangement.copy()
for i in range(0, len(temp_list)-1, 2):
    temp_list[i], temp_list[i+1] = temp_list[i+1], temp_list[i]
print(f"After swapping adjacent pairs: {temp_list}")

# Bài 8.5: Complex modifications
print("\nBài 8.5: Complex modifications")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original matrix:")
for row in matrix:
    print(f"  {row}")

# Modify diagonal elements
for i in range(len(matrix)):
    matrix[i][i] *= 10

print("After modifying diagonal:")
for row in matrix:
    print(f"  {row}")

# Thực hành Section 8
print("\n🎯 THỰC HÀNH SECTION 8:")

# Bài tập 8.1
print("1. Chuẩn hóa dữ liệu")
temperatures = [32, 45, 38, 52, 29, 41, 47]  # Fahrenheit
print(f"  Fahrenheit: {temperatures}")

# Convert to Celsius
for i in range(len(temperatures)):
    temperatures[i] = round((temperatures[i] - 32) * 5/9, 1)
    
print(f"  Celsius: {temperatures}")

# Bài tập 8.2
print("2. Xử lý dữ liệu lỗi")
sensor_data = [23.5, -999, 24.1, 23.8, -999, 24.3, 23.9]  # -999 = lỗi sensor
print(f"  Raw data: {sensor_data}")

# Replace error values with average of valid readings
valid_readings = [x for x in sensor_data if x != -999]
average = sum(valid_readings) / len(valid_readings)

for i in range(len(sensor_data)):
    if sensor_data[i] == -999:
        sensor_data[i] = round(average, 1)
        
print(f"  Cleaned data: {sensor_data}")

# =============================================================================
# SECTION 9: LIST COMPARISON VÀ SORTING
# =============================================================================

print("\n📝 SECTION 9: LIST COMPARISON VÀ SORTING")
print("-" * 40)

# Bài 9.1: List comparison
print("Bài 9.1: List comparison")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
list4 = [1, 2, 3, 4]

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list4: {list4}")

print(f"list1 == list2: {list1 == list2}")
print(f"list1 == list3: {list1 == list3}")
print(f"list1 < list4: {list1 < list4}")
print(f"list1 > list3: {list1 > list3}")

# Bài 9.2: Sorting numbers
print("\nBài 9.2: Sorting numbers")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers}")

# Sort ascending (modify original)
numbers_asc = numbers.copy()
numbers_asc.sort()
print(f"Ascending: {numbers_asc}")

# Sort descending
numbers_desc = numbers.copy()
numbers_desc.sort(reverse=True)
print(f"Descending: {numbers_desc}")

# Using sorted() (creates new list)
numbers_sorted = sorted(numbers)
print(f"Original unchanged: {numbers}")
print(f"Sorted copy: {numbers_sorted}")

# Bài 9.3: Sorting strings
print("\nBài 9.3: Sorting strings")
fruits = ["banana", "apple", "cherry", "date"]
print(f"Original: {fruits}")

# Alphabetical sort
fruits_alpha = sorted(fruits)
print(f"Alphabetical: {fruits_alpha}")

# Sort by length
fruits_length = sorted(fruits, key=len)
print(f"By length: {fruits_length}")

# Case-insensitive sort
mixed_case = ["Banana", "apple", "Cherry", "date"]
case_insensitive = sorted(mixed_case, key=str.lower)
print(f"Case-insensitive: {case_insensitive}")

# Bài 9.4: Custom sorting
print("\nBài 9.4: Custom sorting")
students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 78),
    ("Diana", 92)
]

print(f"Original: {students}")

# Sort by grade
by_grade = sorted(students, key=lambda x: x[1])
print(f"By grade: {by_grade}")

# Sort by name
by_name = sorted(students, key=lambda x: x[0])
print(f"By name: {by_name}")

# Sort by grade descending
by_grade_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"By grade (desc): {by_grade_desc}")

# Bài 9.5: Multiple criteria sorting
print("\nBài 9.5: Multiple criteria sorting")
employees = [
    ("Alice", "Engineering", 75000),
    ("Bob", "Engineering", 80000),
    ("Charlie", "Marketing", 65000),
    ("Diana", "Engineering", 75000),
    ("Eve", "Marketing", 70000)
]

print("Original employees:")
for emp in employees:
    print(f"  {emp}")

# Sort by department first, then by salary
sorted_employees = sorted(employees, key=lambda x: (x[1], x[2]))
print("\nSorted by dept, then salary:")
for emp in sorted_employees:
    print(f"  {emp}")

# Thực hành Section 9
print("\n🎯 THỰC HÀNH SECTION 9:")

# Bài tập 9.1
print("1. Sắp xếp danh sách sách")
books = [
    ("1984", "George Orwell", 1949),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("Pride and Prejudice", "Jane Austen", 1813)
]

# Sort by publication year
by_year = sorted(books, key=lambda x: x[2])
print("  Sorted by year:")
for book in by_year[:2]:  # Show first 2
    print(f"    {book[0]} ({book[2]})")

# =============================================================================
# SECTION 10: PRACTICAL APPLICATIONS
# =============================================================================

print("\n📝 SECTION 10: PRACTICAL APPLICATIONS")
print("-" * 40)

# Bài 10.1: Shopping cart system
print("Bài 10.1: Shopping cart system")
shopping_cart = []

def add_item(cart, item, price, quantity=1):
    cart.append([item, price, quantity])
    return f"Added {quantity}x {item} at ${price} each"

def calculate_total(cart):
    return sum(item[1] * item[2] for item in cart)

def display_cart(cart):
    print("Shopping Cart:")
    for i, (item, price, qty) in enumerate(cart, 1):
        print(f"  {i}. {item}: ${price} x {qty} = ${price * qty}")
    print(f"Total: ${calculate_total(cart)}")

# Demo shopping cart
print(add_item(shopping_cart, "Apple", 1.50, 5))
print(add_item(shopping_cart, "Bread", 2.00, 2))
print(add_item(shopping_cart, "Milk", 3.50, 1))
display_cart(shopping_cart)

# Bài 10.2: Student grade tracker
print("\nBài 10.2: Student grade tracker")
class GradeTracker:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        self.students[name] = []
        
    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].append((subject, grade))
    
    def get_average(self, name):
        if name in self.students and self.students[name]:
            grades = [grade for _, grade in self.students[name]]
            return sum(grades) / len(grades)
        return 0
    
    def get_top_student(self):
        if not self.students:
            return None
        averages = [(name, self.get_average(name)) for name in self.students]
        return max(averages, key=lambda x: x[1])

# Demo grade tracker
tracker = GradeTracker()
tracker.add_student("Alice")
tracker.add_student("Bob")

tracker.add_grade("Alice", "Math", 95)
tracker.add_grade("Alice", "Science", 87)
tracker.add_grade("Bob", "Math", 92)
tracker.add_grade("Bob", "Science", 89)

print(f"Alice's average: {tracker.get_average('Alice'):.1f}")
print(f"Bob's average: {tracker.get_average('Bob'):.1f}")
print(f"Top student: {tracker.get_top_student()}")

# Bài 10.3: Simple inventory system
print("\nBài 10.3: Simple inventory system")
inventory = [
    ["Laptop", 10, 999.99],
    ["Mouse", 50, 29.99],
    ["Keyboard", 30, 79.99],
    ["Monitor", 15, 299.99]
]

def find_item(inventory, item_name):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            return item
    return None

def update_stock(inventory, item_name, quantity_change):
    item = find_item(inventory, item_name)
    if item:
        item[1] += quantity_change
        return f"Updated {item_name}: new stock = {item[1]}"
    return f"Item {item_name} not found"

def low_stock_alert(inventory, threshold=10):
    low_stock = [item for item in inventory if item[1] <= threshold]
    return low_stock

print("Current inventory:")
for item, stock, price in inventory:
    print(f"  {item}: {stock} units at ${price}")

print(f"\n{update_stock(inventory, 'laptop', -2)}")
print(f"{update_stock(inventory, 'mouse', 20)}")

low_stock = low_stock_alert(inventory, 15)
if low_stock:
    print(f"\n⚠️ Low stock alert:")
    for item, stock, price in low_stock:
        print(f"  {item}: only {stock} left")

# Bài 10.4: Text analysis
print("\nBài 10.4: Text analysis")
def analyze_text(text):
    words = text.lower().split()
    
    # Word frequency
    word_count = {}
    for word in words:
        word = word.strip('.,!?";')  # Remove punctuation
        word_count[word] = word_count.get(word, 0) + 1
    
    # Convert to list of tuples and sort
    word_freq = list(word_count.items())
    word_freq.sort(key=lambda x: x[1], reverse=True)
    
    return {
        'total_words': len(words),
        'unique_words': len(word_count),
        'most_common': word_freq[:5],  # Top 5
        'avg_word_length': sum(len(word) for word in words) / len(words)
    }

sample_text = """
Python is a powerful programming language. Python is easy to learn and 
Python is versatile. Many developers love Python because Python is readable.
"""

analysis = analyze_text(sample_text)
print("Text Analysis Results:")
print(f"  Total words: {analysis['total_words']}")
print(f"  Unique words: {analysis['unique_words']}")
print(f"  Average word length: {analysis['avg_word_length']:.1f}")
print("  Most common words:")
for word, count in analysis['most_common']:
    print(f"    '{word}': {count} times")

# Bài 10.5: Simple game leaderboard
print("\nBài 10.5: Game leaderboard")
leaderboard = []

def add_score(leaderboard, player_name, score):
    # Check if player exists
    for entry in leaderboard:
        if entry[0] == player_name:
            if score > entry[1]:  # Update if new high score
                entry[1] = score
                return f"New high score for {player_name}: {score}"
            else:
                return f"Score {score} is not higher than {player_name}'s best: {entry[1]}"
    
    # New player
    leaderboard.append([player_name, score])
    return f"Added new player {player_name} with score {score}"

def display_leaderboard(leaderboard, top_n=5):
    sorted_board = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    print(f"🏆 TOP {min(top_n, len(sorted_board))} LEADERBOARD:")
    for i, (player, score) in enumerate(sorted_board[:top_n], 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        print(f"  {medal} {player}: {score}")

# Demo leaderboard
print(add_score(leaderboard, "Alice", 1500))
print(add_score(leaderboard, "Bob", 1200))
print(add_score(leaderboard, "Charlie", 1800))
print(add_score(leaderboard, "Alice", 1600))
print(add_score(leaderboard, "Diana", 2000))

display_leaderboard(leaderboard)

print("\n" + "=" * 50)
print("🎉 HOÀN THÀNH BÀI TẬP 1: LISTS CƠ BẢN!")
print("✅ Đã thực hành: Tạo lists, indexing, slicing, operations")
print("✅ Đã làm quen: Membership testing, concatenation, sorting")
print("✅ Đã áp dụng: Các ứng dụng thực tế với lists")
print("🚀 Tiếp theo: Bài tập 2 - Tuples và Sets!")
print("=" * 50) 