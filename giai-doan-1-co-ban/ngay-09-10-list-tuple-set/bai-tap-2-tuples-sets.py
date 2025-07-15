"""
=== BÀI TẬP 2: TUPLES VÀ SETS ===
Ngày 9-10: Lists, Tuples, Sets
Chủ đề: Tuple operations, unpacking/packing, Set operations, mathematical operations

Bài tập này gồm 8 sections:
1. Tuple creation và basic operations
2. Tuple indexing và slicing
3. Tuple unpacking và packing
4. Advanced tuple unpacking với *
5. Set creation và basic operations
6. Set mathematical operations
7. Set methods và advanced operations
8. Practical applications với tuples và sets

Mỗi section có 5-6 bài tập từ easy đến hard.
"""

print("🐍 BÀI TẬP 2: TUPLES VÀ SETS")
print("=" * 50)

# =============================================================================
# SECTION 1: TUPLE CREATION VÀ BASIC OPERATIONS
# =============================================================================

print("\n📝 SECTION 1: TUPLE CREATION VÀ BASIC OPERATIONS")
print("-" * 40)

# Bài 1.1: Tạo tuples khác nhau
print("Bài 1.1: Tạo tuples")
empty_tuple = ()
single_tuple = (42,)  # Chú ý dấu phẩy!
coordinates = (10, 20)
rgb_color = (255, 128, 0)
student_info = ("Alice", 20, "Computer Science", 3.8)
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])

print(f"Empty tuple: {empty_tuple} (type: {type(empty_tuple)})")
print(f"Single tuple: {single_tuple} (type: {type(single_tuple)})")
print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Student info: {student_info}")
print(f"Mixed tuple: {mixed_tuple}")

# Bài 1.2: Tuple từ other iterables
print("\nBài 1.2: Tuple từ iterables khác")
from_list = tuple([1, 2, 3, 4, 5])
from_string = tuple("hello")
from_range = tuple(range(5, 10))
from_set = tuple({3, 1, 4, 1, 5})  # Chú ý: set sẽ remove duplicates

print(f"From list: {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")
print(f"From set: {from_set}")

# Bài 1.3: Nested tuples
print("\nBài 1.3: Nested tuples")
point_2d = (10, 20)
point_3d = (10, 20, 30)
line_segment = ((0, 0), (10, 10))
triangle = ((0, 0), (0, 5), (5, 0))
matrix_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(f"2D point: {point_2d}")
print(f"3D point: {point_3d}")
print(f"Line segment: {line_segment}")
print(f"Triangle: {triangle}")
print(f"Matrix as tuple: {matrix_tuple}")

# Bài 1.4: Tuple operations
print("\nBài 1.4: Tuple operations")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
concatenated = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {concatenated}")

# Repetition
repeated = tuple1 * 3
print(f"Repetition: {tuple1} * 3 = {repeated}")

# Length và membership
print(f"Length of tuple1: {len(tuple1)}")
print(f"2 in tuple1: {2 in tuple1}")
print(f"7 not in tuple1: {7 not in tuple1}")

# Bài 1.5: Tuple comparison
print("\nBài 1.5: Tuple comparison")
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
tuple_d = (1, 2)

print(f"tuple_a: {tuple_a}")
print(f"tuple_b: {tuple_b}")
print(f"tuple_c: {tuple_c}")
print(f"tuple_d: {tuple_d}")

print(f"tuple_a == tuple_b: {tuple_a == tuple_b}")
print(f"tuple_a < tuple_c: {tuple_a < tuple_c}")
print(f"tuple_a > tuple_d: {tuple_a > tuple_d}")

# Thực hành Section 1
print("\n🎯 THỰC HÀNH SECTION 1:")

# Bài tập 1.1
print("1. Tạo database records với tuples")
employees = [
    ("E001", "Alice Johnson", "Engineering", 75000),
    ("E002", "Bob Smith", "Marketing", 65000),
    ("E003", "Charlie Brown", "Engineering", 80000),
    ("E004", "Diana Prince", "HR", 70000)
]

print("Employee Database:")
for emp_id, name, dept, salary in employees:
    print(f"  {emp_id}: {name} - {dept} (${salary:,})")

# Bài tập 1.2
print("\n2. Coordinates system")
cities = [
    ("New York", (40.7128, -74.0060)),
    ("London", (51.5074, -0.1278)),
    ("Tokyo", (35.6762, 139.6503)),
    ("Sydney", (-33.8688, 151.2093))
]

print("World Cities Coordinates:")
for city, (lat, lon) in cities:
    hemisphere_ns = "N" if lat >= 0 else "S"
    hemisphere_ew = "E" if lon >= 0 else "W"
    print(f"  {city}: {abs(lat):.2f}°{hemisphere_ns}, {abs(lon):.2f}°{hemisphere_ew}")

# =============================================================================
# SECTION 2: TUPLE INDEXING VÀ SLICING
# =============================================================================

print("\n📝 SECTION 2: TUPLE INDEXING VÀ SLICING")
print("-" * 40)

# Bài 2.1: Basic indexing
print("Bài 2.1: Basic indexing")
grades = (85, 92, 78, 96, 88, 91, 84)
print(f"Grades: {grades}")
print(f"First grade: {grades[0]}")
print(f"Last grade: {grades[-1]}")
print(f"Middle grade: {grades[len(grades)//2]}")
print(f"Second highest: {sorted(grades, reverse=True)[1]}")

# Bài 2.2: Nested tuple indexing
print("\nBài 2.2: Nested tuple indexing")
students = (
    ("Alice", (85, 90, 78)),
    ("Bob", (92, 88, 95)),
    ("Charlie", (78, 85, 82))
)

print(f"Students data: {students}")
print(f"Alice's name: {students[0][0]}")
print(f"Alice's first grade: {students[0][1][0]}")
print(f"Bob's grades: {students[1][1]}")
print(f"Charlie's last grade: {students[2][1][-1]}")

# Bài 2.3: Tuple slicing
print("\nBài 2.3: Tuple slicing")
alphabet = tuple('abcdefghijklmnopqrstuvwxyz')
print(f"Alphabet: {alphabet[:10]}...")  # Show first 10

# Various slicing operations
first_five = alphabet[:5]
last_five = alphabet[-5:]
every_third = alphabet[::3]
reverse = alphabet[::-1]
middle_section = alphabet[10:16]

print(f"First 5: {first_five}")
print(f"Last 5: {last_five}")
print(f"Every 3rd: {every_third[:10]}...")  # Show first 10
print(f"Reverse first 5: {reverse[:5]}")
print(f"Middle section: {middle_section}")

# Bài 2.4: Slicing với computed indices
print("\nBài 2.4: Computed indices slicing")
data = tuple(range(1, 21))  # 1 to 20
print(f"Data: {data}")

n = len(data)
quarter = n // 4
half = n // 2
three_quarter = 3 * n // 4

first_quarter = data[:quarter]
second_quarter = data[quarter:half]
third_quarter = data[half:three_quarter]
fourth_quarter = data[three_quarter:]

print(f"Q1: {first_quarter}")
print(f"Q2: {second_quarter}")
print(f"Q3: {third_quarter}")
print(f"Q4: {fourth_quarter}")

# Bài 2.5: Advanced slicing patterns
print("\nBài 2.5: Advanced slicing patterns")
sequence = tuple(range(1, 31))  # 1 to 30
print(f"Sequence: {sequence[:10]}...")  # Show first 10

# Extract patterns
odd_positions = sequence[::2]      # 1st, 3rd, 5th...
even_positions = sequence[1::2]    # 2nd, 4th, 6th...
every_fifth = sequence[4::5]       # 5th, 10th, 15th...
backward_evens = sequence[::-2]    # Last, 2nd last, 4th last...

print(f"Odd positions (first 10): {odd_positions[:10]}")
print(f"Even positions (first 10): {even_positions[:10]}")
print(f"Every 5th: {every_fifth}")
print(f"Backward evens (first 10): {backward_evens[:10]}")

# Thực hành Section 2
print("\n🎯 THỰC HÀNH SECTION 2:")

# Bài tập 2.1
print("1. Phân tích dữ liệu thời tiết")
weather_data = (
    ("Monday", 25, 60, "Sunny"),
    ("Tuesday", 22, 70, "Cloudy"),
    ("Wednesday", 18, 85, "Rainy"),
    ("Thursday", 20, 75, "Cloudy"),
    ("Friday", 26, 55, "Sunny"),
    ("Saturday", 28, 50, "Sunny"),
    ("Sunday", 24, 65, "Partly Cloudy")
)

print("Weather Analysis:")
temperatures = tuple(day[1] for day in weather_data)
avg_temp = sum(temperatures) / len(temperatures)
max_temp_day = max(weather_data, key=lambda x: x[1])
min_temp_day = min(weather_data, key=lambda x: x[1])

print(f"  Average temperature: {avg_temp:.1f}°C")
print(f"  Hottest day: {max_temp_day[0]} ({max_temp_day[1]}°C)")
print(f"  Coolest day: {min_temp_day[0]} ({min_temp_day[1]}°C)")

# Bài tập 2.2
print("\n2. RGB color analysis")
colors = (
    ("Red", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Blue", (0, 0, 255)),
    ("Yellow", (255, 255, 0)),
    ("Magenta", (255, 0, 255)),
    ("Cyan", (0, 255, 255)),
    ("White", (255, 255, 255)),
    ("Black", (0, 0, 0))
)

print("Color brightness analysis:")
for name, (r, g, b) in colors:
    brightness = (r + g + b) / 3
    print(f"  {name}: brightness = {brightness:.1f}")

# =============================================================================
# SECTION 3: TUPLE UNPACKING VÀ PACKING
# =============================================================================

print("\n📝 SECTION 3: TUPLE UNPACKING VÀ PACKING")
print("-" * 40)

# Bài 3.1: Basic unpacking
print("Bài 3.1: Basic unpacking")
point = (10, 20)
x, y = point
print(f"Point: {point}")
print(f"x = {x}, y = {y}")

# Multiple assignment
person = ("John", 25, "Engineer")
name, age, job = person
print(f"Person: {person}")
print(f"Name: {name}, Age: {age}, Job: {job}")

# Bài 3.2: Tuple packing
print("\nBài 3.2: Tuple packing")
# Automatic packing
coordinates = 100, 200  # Creates tuple automatically
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")

# Function returning multiple values
def get_statistics(numbers):
    return len(numbers), sum(numbers), min(numbers), max(numbers)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = get_statistics(data)  # Packed into tuple
count, total, minimum, maximum = stats  # Unpacked
print(f"Statistics: {stats}")
print(f"Count: {count}, Total: {total}, Min: {minimum}, Max: {maximum}")

# Bài 3.3: Swapping values
print("\nBài 3.3: Swapping values")
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

# Elegant swapping với tuple unpacking
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Multiple swapping
x, y, z = 1, 2, 3
print(f"Before: x={x}, y={y}, z={z}")
x, y, z = z, x, y  # Rotate values
print(f"After rotation: x={x}, y={y}, z={z}")

# Bài 3.4: Unpacking trong loops
print("\nBài 3.4: Unpacking trong loops")
student_grades = [
    ("Alice", 85, 90, 78),
    ("Bob", 92, 88, 95),
    ("Charlie", 78, 85, 82)
]

print("Student Grade Analysis:")
for name, math, science, english in student_grades:
    average = (math + science + english) / 3
    print(f"  {name}: Math={math}, Science={science}, English={english}, Avg={average:.1f}")

# Unpacking với enumerate
print("\nStudent ranking:")
for rank, (name, math, science, english) in enumerate(student_grades, 1):
    total = math + science + english
    print(f"  #{rank}: {name} (Total: {total})")

# Bài 3.5: Nested unpacking
print("\nBài 3.5: Nested unpacking")
companies = [
    ("TechCorp", ("Alice", "CEO"), ("New York", "USA")),
    ("DataInc", ("Bob", "CTO"), ("London", "UK")),
    ("CodeLab", ("Charlie", "Founder"), ("Tokyo", "Japan"))
]

print("Company Information:")
for company, (ceo_name, ceo_title), (city, country) in companies:
    print(f"  {company}: {ceo_title} {ceo_name} in {city}, {country}")

# Thực hành Section 3
print("\n🎯 THỰC HÀNH SECTION 3:")

# Bài tập 3.1
print("1. Processing coordinates")
locations = [
    ("Home", (0, 0)),
    ("School", (5, 3)),
    ("Store", (-2, 4)),
    ("Park", (3, -1)),
    ("Office", (7, 2))
]

print("Distance from Home:")
for place, (x, y) in locations:
    distance = (x**2 + y**2)**0.5  # Euclidean distance
    print(f"  {place}: {distance:.2f} units")

# Bài tập 3.2
print("\n2. File processing simulation")
files = [
    ("document.txt", 1024, "2023-01-15"),
    ("image.jpg", 2048000, "2023-02-20"),
    ("video.mp4", 50000000, "2023-03-10"),
    ("music.mp3", 5120000, "2023-04-05")
]

print("File Analysis:")
total_size = 0
for filename, size, date in files:
    size_mb = size / (1024 * 1024)
    total_size += size
    print(f"  {filename}: {size_mb:.2f} MB (Created: {date})")

print(f"Total size: {total_size / (1024 * 1024):.2f} MB")

# =============================================================================
# SECTION 4: ADVANCED TUPLE UNPACKING VỚI *
# =============================================================================

print("\n📝 SECTION 4: ADVANCED TUPLE UNPACKING VỚI *")
print("-" * 40)

# Bài 4.1: Star unpacking basics
print("Bài 4.1: Star unpacking basics")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# First, rest
first, *rest = numbers
print(f"First: {first}")
print(f"Rest: {rest}")

# First, middle, last
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle[:3]}..., Last: {last}")

# First, second, rest
first, second, *rest = numbers
print(f"First: {first}, Second: {second}, Rest: {rest[:3]}...")

# Bài 4.2: Advanced patterns
print("\nBài 4.2: Advanced patterns")
grades = (95, 87, 92, 78, 85, 90, 88)

# Get top 2 và rest
sorted_grades = tuple(sorted(grades, reverse=True))
top1, top2, *others = sorted_grades
print(f"Grades: {grades}")
print(f"Top 1: {top1}, Top 2: {top2}")
print(f"Others: {others}")

# Get first, last và middle
first, *middle, last = grades
middle_avg = sum(middle) / len(middle) if middle else 0
print(f"First: {first}, Last: {last}, Middle avg: {middle_avg:.1f}")

# Bài 4.3: Unpacking với different lengths
print("\nBài 4.3: Variable length unpacking")
def process_scores(*scores):
    if not scores:
        return "No scores provided"
    
    first, *rest = scores
    if not rest:
        return f"Single score: {first}"
    
    last = rest[-1]
    middle = rest[:-1] if len(rest) > 1 else []
    
    return {
        "first": first,
        "last": last,
        "middle": middle,
        "count": len(scores),
        "average": sum(scores) / len(scores)
    }

# Test với different lengths
test_cases = [
    (85,),
    (85, 92),
    (85, 92, 78),
    (85, 92, 78, 96, 88)
]

for i, scores in enumerate(test_cases, 1):
    result = process_scores(*scores)
    print(f"Test {i} {scores}: {result}")

# Bài 4.4: Nested star unpacking
print("\nBài 4.4: Nested unpacking")
teams = [
    ("Team A", 95, 87, 92, 78, 85),
    ("Team B", 88, 91, 84, 89),
    ("Team C", 92, 85, 88, 91, 87, 90)
]

print("Team Performance Analysis:")
for team_name, *scores in teams:
    if len(scores) >= 3:
        top_score, *middle_scores, worst_score = sorted(scores, reverse=True)
        avg_middle = sum(middle_scores) / len(middle_scores) if middle_scores else 0
        
        print(f"  {team_name}:")
        print(f"    Best: {top_score}, Worst: {worst_score}")
        print(f"    Middle avg: {avg_middle:.1f}, Total games: {len(scores)}")
    else:
        print(f"  {team_name}: Insufficient data ({len(scores)} games)")

# Bài 4.5: Practical star unpacking
print("\nBài 4.5: Practical applications")
def analyze_sales_data(month, *daily_sales):
    if not daily_sales:
        return f"{month}: No sales data"
    
    total = sum(daily_sales)
    average = total / len(daily_sales)
    best_day, *_, worst_day = sorted(daily_sales, reverse=True)
    
    # Find streak of good days (above average)
    good_days = [day for day in daily_sales if day > average]
    
    return {
        "month": month,
        "total_sales": total,
        "average_daily": average,
        "best_day": best_day,
        "worst_day": worst_day,
        "good_days_count": len(good_days),
        "days_tracked": len(daily_sales)
    }

# Sales data for different months
sales_data = [
    ("January", 1200, 1350, 980, 1100, 1450, 1200, 1380),
    ("February", 1100, 1250, 1400),
    ("March", 1500, 1200, 1350, 1600, 1100, 1250, 1480, 1320, 1400, 1550)
]

for month_data in sales_data:
    analysis = analyze_sales_data(*month_data)
    print(f"{analysis['month']} Analysis:")
    print(f"  Total: ${analysis['total_sales']:,}")
    print(f"  Daily average: ${analysis['average_daily']:.0f}")
    print(f"  Best day: ${analysis['best_day']}, Worst day: ${analysis['worst_day']}")
    print(f"  Good days: {analysis['good_days_count']}/{analysis['days_tracked']}")

# Thực hành Section 4
print("\n🎯 THỰC HÀNH SECTION 4:")

# Bài tập 4.1
print("1. Tournament bracket system")
players = ("Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry")

# First round: first vs last, second vs second-last, etc.
first, *middle, last = players
print(f"Championship match: {first} vs {last}")

if len(middle) >= 2:
    second, *inner, second_last = middle
    print(f"Semi-final 1: {second} vs {second_last}")
    
    if len(inner) >= 2:
        third, *center, third_last = inner
        print(f"Quarter-final 1: {third} vs {third_last}")
        
        if center:
            print(f"Remaining players: {center}")

# =============================================================================
# SECTION 5: SET CREATION VÀ BASIC OPERATIONS
# =============================================================================

print("\n📝 SECTION 5: SET CREATION VÀ BASIC OPERATIONS")
print("-" * 40)

# Bài 5.1: Creating sets
print("Bài 5.1: Creating sets")
# Empty set (chú ý: {} tạo dict, không phải set!)
empty_set = set()
print(f"Empty set: {empty_set} (type: {type(empty_set)})")

# Set from literals
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
mixed = {1, "hello", 3.14, True}

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Bài 5.2: Set from iterables
print("\nBài 5.2: Set from iterables")
# Remove duplicates from list
numbers_list = [1, 2, 2, 3, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"List with duplicates: {numbers_list}")
print(f"Unique numbers: {unique_numbers}")

# Set from string
text = "hello world"
unique_chars = set(text)
print(f"Text: '{text}'")
print(f"Unique characters: {unique_chars}")

# Set from range
range_set = set(range(1, 11, 2))  # Odd numbers 1-9
print(f"Odd numbers 1-9: {range_set}")

# Bài 5.3: Set properties
print("\nBài 5.3: Set properties")
test_set = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(f"Original input: {{3, 1, 4, 1, 5, 9, 2, 6, 5}}")
print(f"Actual set: {test_set}")  # Duplicates removed, order may vary
print(f"Length: {len(test_set)}")
print(f"3 in set: {3 in test_set}")
print(f"7 in set: {7 in test_set}")

# Bài 5.4: Adding và removing elements
print("\nBài 5.4: Adding và removing elements")
colors = {"red", "green", "blue"}
print(f"Original colors: {colors}")

# Add single element
colors.add("yellow")
print(f"After adding yellow: {colors}")

# Add multiple elements
colors.update(["purple", "orange", "pink"])
print(f"After adding multiple: {colors}")

# Remove elements
colors.remove("green")  # Raises error if not found
print(f"After removing green: {colors}")

colors.discard("brown")  # No error if not found
print(f"After discarding brown (not present): {colors}")

# Pop random element
removed = colors.pop()
print(f"Popped element: {removed}")
print(f"After pop: {colors}")

# Bài 5.5: Set comprehensions
print("\nBài 5.5: Set comprehensions")
# Basic set comprehension
squares = {x**2 for x in range(1, 11)}
print(f"Squares 1-100: {squares}")

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string processing
text = "Hello World Python"
vowels = {char.lower() for char in text if char.lower() in 'aeiou'}
print(f"Unique vowels in '{text}': {vowels}")

# Complex comprehension
words = ["apple", "banana", "cherry", "date", "elderberry"]
first_letters = {word[0].upper() for word in words if len(word) > 4}
print(f"First letters of long words: {first_letters}")

# Thực hành Section 5
print("\n🎯 THỰC HÀNH SECTION 5:")

# Bài tập 5.1
print("1. Student enrollment system")
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Charlie", "Eve", "Frank"}
english_students = {"Alice", "Charlie", "Frank", "Grace"}

all_students = math_students | science_students | english_students
print(f"All students: {all_students}")
print(f"Total unique students: {len(all_students)}")

# Bài tập 5.2
print("\n2. Data cleaning - remove duplicates")
survey_responses = [
    "Yes", "No", "Yes", "Maybe", "Yes", "No", "Maybe", "Yes", "No", "Yes"
]
unique_responses = set(survey_responses)
print(f"Survey responses: {survey_responses}")
print(f"Unique responses: {unique_responses}")
print(f"Response counts:")
for response in unique_responses:
    count = survey_responses.count(response)
    print(f"  {response}: {count} times")

# =============================================================================
# SECTION 6: SET MATHEMATICAL OPERATIONS
# =============================================================================

print("\n📝 SECTION 6: SET MATHEMATICAL OPERATIONS")
print("-" * 40)

# Bài 6.1: Union operations
print("Bài 6.1: Union operations")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")

# Union với | operator
union_ab = set_a | set_b
print(f"A ∪ B: {union_ab}")

# Union với method
union_method = set_a.union(set_b)
print(f"A.union(B): {union_method}")

# Multiple union
union_all = set_a | set_b | set_c
print(f"A ∪ B ∪ C: {union_all}")

# Bài 6.2: Intersection operations
print("\nBài 6.2: Intersection operations")
# Intersection với & operator
intersection_ab = set_a & set_b
print(f"A ∩ B: {intersection_ab}")

# Intersection với method
intersection_method = set_a.intersection(set_b)
print(f"A.intersection(B): {intersection_method}")

# Multiple intersection
intersection_all = set_a & set_b & set_c
print(f"A ∩ B ∩ C: {intersection_all}")

# No intersection
set_d = {10, 11, 12}
no_intersection = set_a & set_d
print(f"A ∩ {{10,11,12}}: {no_intersection}")

# Bài 6.3: Difference operations
print("\nBài 6.3: Difference operations")
# Difference với - operator
diff_ab = set_a - set_b
print(f"A - B: {diff_ab}")

# Reverse difference
diff_ba = set_b - set_a
print(f"B - A: {diff_ba}")

# Difference với method
diff_method = set_a.difference(set_b)
print(f"A.difference(B): {diff_method}")

# Multiple difference
diff_multiple = set_a - set_b - {1}
print(f"A - B - {{1}}: {diff_multiple}")

# Bài 6.4: Symmetric difference
print("\nBài 6.4: Symmetric difference")
# Symmetric difference với ^ operator
sym_diff_ab = set_a ^ set_b
print(f"A △ B: {sym_diff_ab}")

# Symmetric difference với method
sym_diff_method = set_a.symmetric_difference(set_b)
print(f"A.symmetric_difference(B): {sym_diff_method}")

# Verify: (A-B) ∪ (B-A) = A△B
manual_sym_diff = (set_a - set_b) | (set_b - set_a)
print(f"(A-B) ∪ (B-A): {manual_sym_diff}")
print(f"Same as A△B: {sym_diff_ab == manual_sym_diff}")

# Bài 6.5: Set relations
print("\nBài 6.5: Set relations")
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {5, 6}
set4 = {1, 2, 3, 4}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Set3: {set3}")
print(f"Set4: {set4}")

# Subset relations
print(f"Set1 ⊆ Set2: {set1.issubset(set2)} or {set1 <= set2}")
print(f"Set2 ⊆ Set1: {set2.issubset(set1)} or {set2 <= set1}")

# Superset relations
print(f"Set2 ⊇ Set1: {set2.issuperset(set1)} or {set2 >= set1}")

# Equality
print(f"Set2 = Set4: {set2 == set4}")

# Disjoint sets
print(f"Set1 and Set3 disjoint: {set1.isdisjoint(set3)}")
print(f"Set1 and Set2 disjoint: {set1.isdisjoint(set2)}")

# Thực hành Section 6
print("\n🎯 THỰC HÀNH SECTION 6:")

# Bài tập 6.1
print("1. Course enrollment analysis")
courses = {
    "Math": {"Alice", "Bob", "Charlie", "Diana", "Eve"},
    "Physics": {"Bob", "Charlie", "Frank", "Grace"},
    "Chemistry": {"Alice", "Charlie", "Eve", "Frank", "Henry"},
    "Biology": {"Diana", "Eve", "Grace", "Henry", "Ivy"}
}

print("Course Enrollment Analysis:")
for course, students in courses.items():
    print(f"  {course}: {len(students)} students")

# Students taking both Math and Physics
math_physics = courses["Math"] & courses["Physics"]
print(f"\nStudents in both Math and Physics: {math_physics}")

# Students in Science courses (Physics, Chemistry, Biology)
science_students = courses["Physics"] | courses["Chemistry"] | courses["Biology"]
print(f"Students in any Science course: {science_students}")

# Students only in Math
math_only = courses["Math"] - science_students
print(f"Students only in Math: {math_only}")

# Bài tập 6.2
print("\n2. Website visitor analysis")
yesterday_visitors = {"user1", "user2", "user3", "user4", "user5"}
today_visitors = {"user3", "user4", "user5", "user6", "user7", "user8"}

# New visitors today
new_visitors = today_visitors - yesterday_visitors
print(f"New visitors today: {new_visitors}")

# Returning visitors
returning_visitors = yesterday_visitors & today_visitors
print(f"Returning visitors: {returning_visitors}")

# Visitors who didn't return
lost_visitors = yesterday_visitors - today_visitors
print(f"Lost visitors: {lost_visitors}")

# Total unique visitors across 2 days
total_unique = yesterday_visitors | today_visitors
print(f"Total unique visitors: {len(total_unique)}")

# =============================================================================
# SECTION 7: SET METHODS VÀ ADVANCED OPERATIONS
# =============================================================================

print("\n📝 SECTION 7: SET METHODS VÀ ADVANCED OPERATIONS")
print("-" * 40)

# Bài 7.1: Update operations
print("Bài 7.1: Update operations")
base_set = {1, 2, 3}
print(f"Base set: {base_set}")

# update() - union and assign
update_set = base_set.copy()
update_set.update({4, 5, 6})
print(f"After update({4, 5, 6}): {update_set}")

# intersection_update()
intersect_set = {1, 2, 3, 4, 5}
intersect_set.intersection_update({3, 4, 5, 6, 7})
print(f"After intersection_update: {intersect_set}")

# difference_update()
diff_set = {1, 2, 3, 4, 5}
diff_set.difference_update({3, 4})
print(f"After difference_update: {diff_set}")

# symmetric_difference_update()
sym_set = {1, 2, 3}
sym_set.symmetric_difference_update({3, 4, 5})
print(f"After symmetric_difference_update: {sym_set}")

# Bài 7.2: Set copying và identity
print("\nBài 7.2: Set copying")
original = {1, 2, 3, 4, 5}
shallow_copy = original.copy()
reference = original

print(f"Original: {original}")
print(f"Copy: {shallow_copy}")
print(f"Reference: {reference}")

# Modify original
original.add(6)
print(f"After adding 6 to original:")
print(f"  Original: {original}")
print(f"  Copy: {shallow_copy}")
print(f"  Reference: {reference}")

# Identity check
print(f"original is reference: {original is reference}")
print(f"original is copy: {original is shallow_copy}")

# Bài 7.3: Advanced set operations
print("\nBài 7.3: Advanced operations")
def analyze_sets(*sets):
    """Analyze relationships between multiple sets"""
    if len(sets) < 2:
        return "Need at least 2 sets"
    
    # Universal set (union of all)
    universal = set()
    for s in sets:
        universal.update(s)
    
    # Common elements (intersection of all)
    common = sets[0].copy()
    for s in sets[1:]:
        common.intersection_update(s)
    
    # Unique to each set
    unique_elements = []
    for i, s in enumerate(sets):
        others = set()
        for j, other in enumerate(sets):
            if i != j:
                others.update(other)
        unique_to_set = s - others
        unique_elements.append(unique_to_set)
    
    return {
        "universal": universal,
        "common": common,
        "unique_to_each": unique_elements,
        "total_unique": len(universal),
        "common_count": len(common)
    }

# Test với multiple sets
test_sets = [
    {"apple", "banana", "orange", "grape"},
    {"banana", "orange", "kiwi", "mango"},
    {"orange", "grape", "strawberry", "blueberry"}
]

analysis = analyze_sets(*test_sets)
print("Set Analysis:")
print(f"  Universal set: {analysis['universal']}")
print(f"  Common elements: {analysis['common']}")
print(f"  Unique to each set:")
for i, unique in enumerate(analysis['unique_to_each']):
    print(f"    Set {i+1}: {unique}")

# Bài 7.4: Set performance analysis
print("\nBài 7.4: Performance comparison")
import time

# Create large datasets
large_list = list(range(10000))
large_set = set(range(10000))

# Test membership
test_values = [5000, 7500, 9999]

# List membership test
start_time = time.time()
for _ in range(1000):
    for val in test_values:
        result = val in large_list
list_time = time.time() - start_time

# Set membership test
start_time = time.time()
for _ in range(1000):
    for val in test_values:
        result = val in large_set
set_time = time.time() - start_time

print(f"List membership test: {list_time:.6f}s")
print(f"Set membership test: {set_time:.6f}s")
print(f"Set is {list_time/set_time:.1f}x faster")

# Bài 7.5: Practical set applications
print("\nBài 7.5: Practical applications")

# Email domain analysis
emails = [
    "user1@gmail.com", "user2@yahoo.com", "user3@gmail.com",
    "user4@hotmail.com", "user5@gmail.com", "user6@company.com",
    "user7@yahoo.com", "user8@outlook.com", "user9@gmail.com"
]

domains = {email.split('@')[1] for email in emails}
print(f"Email domains found: {domains}")

# Count by domain
domain_counts = {}
for email in emails:
    domain = email.split('@')[1]
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

print("Domain distribution:")
for domain, count in sorted(domain_counts.items()):
    print(f"  {domain}: {count} users")

# Thực hành Section 7
print("\n🎯 THỰC HÀNH SECTION 7:")

# Bài tập 7.1
print("1. Social media follower analysis")
followers = {
    "Alice": {"Bob", "Charlie", "Diana", "Eve"},
    "Bob": {"Alice", "Charlie", "Frank"},
    "Charlie": {"Alice", "Bob", "Diana", "Grace"},
    "Diana": {"Alice", "Charlie", "Eve", "Frank"}
}

print("Social Media Analysis:")
for person, following in followers.items():
    print(f"  {person} follows: {following}")

# Mutual followers
alice_bob_mutual = followers["Alice"] & followers["Bob"]
print(f"\nMutual connections (Alice & Bob): {alice_bob_mutual}")

# Most connected person
most_connected = max(followers.items(), key=lambda x: len(x[1]))
print(f"Most connected: {most_connected[0]} with {len(most_connected[1])} connections")

# =============================================================================
# SECTION 8: PRACTICAL APPLICATIONS
# =============================================================================

print("\n📝 SECTION 8: PRACTICAL APPLICATIONS")
print("-" * 40)

# Bài 8.1: Inventory management với tuples
print("Bài 8.1: Inventory management")
class SimpleInventory:
    def __init__(self):
        self.items = []  # List of tuples: (id, name, price, quantity)
    
    def add_item(self, item_id, name, price, quantity):
        item = (item_id, name, price, quantity)
        self.items.append(item)
        return f"Added: {name}"
    
    def find_item(self, item_id):
        for item in self.items:
            if item[0] == item_id:
                return item
        return None
    
    def low_stock_items(self, threshold=5):
        return [item for item in self.items if item[3] <= threshold]
    
    def total_value(self):
        return sum(price * quantity for _, _, price, quantity in self.items)
    
    def items_by_price_range(self, min_price, max_price):
        return [item for item in self.items 
                if min_price <= item[2] <= max_price]

# Demo inventory
inventory = SimpleInventory()
inventory.add_item("I001", "Laptop", 999.99, 5)
inventory.add_item("I002", "Mouse", 29.99, 50)
inventory.add_item("I003", "Keyboard", 79.99, 3)
inventory.add_item("I004", "Monitor", 299.99, 8)

print("Inventory Summary:")
for item_id, name, price, qty in inventory.items:
    print(f"  {item_id}: {name} - ${price} (Stock: {qty})")

print(f"\nTotal inventory value: ${inventory.total_value():,.2f}")

low_stock = inventory.low_stock_items()
if low_stock:
    print("⚠️ Low stock alerts:")
    for item_id, name, price, qty in low_stock:
        print(f"  {name}: only {qty} left")

# Bài 8.2: Student course management
print("\nBài 8.2: Student course management")
class CourseManager:
    def __init__(self):
        self.students = {}  # student_id: (name, enrolled_courses_set)
        self.courses = {}   # course_id: (name, enrolled_students_set)
    
    def add_student(self, student_id, name):
        self.students[student_id] = (name, set())
    
    def add_course(self, course_id, name):
        self.courses[course_id] = (name, set())
    
    def enroll_student(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            # Add course to student's set
            name, courses = self.students[student_id]
            courses.add(course_id)
            
            # Add student to course's set
            course_name, students = self.courses[course_id]
            students.add(student_id)
            return True
        return False
    
    def get_common_courses(self, student1_id, student2_id):
        if student1_id in self.students and student2_id in self.students:
            courses1 = self.students[student1_id][1]
            courses2 = self.students[student2_id][1]
            return courses1 & courses2
        return set()
    
    def get_course_overlap(self, course1_id, course2_id):
        if course1_id in self.courses and course2_id in self.courses:
            students1 = self.courses[course1_id][1]
            students2 = self.courses[course2_id][1]
            return students1 & students2
        return set()

# Demo course management
cm = CourseManager()

# Add students
cm.add_student("S001", "Alice")
cm.add_student("S002", "Bob")
cm.add_student("S003", "Charlie")

# Add courses
cm.add_course("C001", "Math")
cm.add_course("C002", "Physics")
cm.add_course("C003", "Chemistry")

# Enroll students
enrollments = [
    ("S001", "C001"), ("S001", "C002"),
    ("S002", "C001"), ("S002", "C003"),
    ("S003", "C002"), ("S003", "C003")
]

for student_id, course_id in enrollments:
    cm.enroll_student(student_id, course_id)

print("Course Management System:")
for student_id, (name, courses) in cm.students.items():
    course_names = [cm.courses[cid][0] for cid in courses]
    print(f"  {name}: {course_names}")

# Common courses between students
common = cm.get_common_courses("S001", "S002")
if common:
    common_names = [cm.courses[cid][0] for cid in common]
    print(f"\nAlice and Bob share: {common_names}")

# Bài 8.3: Text processing và analysis
print("\nBài 8.3: Text processing")
def analyze_text_advanced(text):
    # Split into words and clean
    words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    # Word statistics với tuples
    word_stats = []
    unique_words = set(words)
    
    for word in unique_words:
        count = words.count(word)
        length = len(word)
        word_stats.append((word, count, length))
    
    # Sort by frequency
    word_stats.sort(key=lambda x: x[1], reverse=True)
    
    # Character analysis với sets
    all_chars = set(text.lower())
    letters = {c for c in all_chars if c.isalpha()}
    vowels = {c for c in letters if c in 'aeiou'}
    consonants = letters - vowels
    
    return {
        "total_words": len(words),
        "unique_words": len(unique_words),
        "word_stats": word_stats[:5],  # Top 5
        "unique_letters": len(letters),
        "vowels": vowels,
        "consonants": consonants,
        "avg_word_length": sum(len(w) for w in words) / len(words)
    }

sample_text = """
Python is a powerful programming language. Python is easy to learn and
Python is versatile. Many developers love Python because Python makes
programming fun and productive.
"""

analysis = analyze_text_advanced(sample_text)
print("Advanced Text Analysis:")
print(f"  Total words: {analysis['total_words']}")
print(f"  Unique words: {analysis['unique_words']}")
print(f"  Average word length: {analysis['avg_word_length']:.1f}")
print(f"  Unique letters: {analysis['unique_letters']}")
print(f"  Vowels used: {analysis['vowels']}")
print("  Most frequent words:")
for word, count, length in analysis['word_stats']:
    print(f"    '{word}': {count} times (length: {length})")

# Bài 8.4: Game achievement system
print("\nBài 8.4: Game achievement system")
class AchievementSystem:
    def __init__(self):
        self.players = {}  # player_id: (name, achievements_set)
        self.achievements = {
            "first_kill": "First Kill",
            "speed_demon": "Speed Demon", 
            "collector": "Collector",
            "explorer": "Explorer",
            "master": "Master Player"
        }
    
    def add_player(self, player_id, name):
        self.players[player_id] = (name, set())
    
    def award_achievement(self, player_id, achievement_id):
        if player_id in self.players and achievement_id in self.achievements:
            name, achievements = self.players[player_id]
            achievements.add(achievement_id)
            return f"{name} earned: {self.achievements[achievement_id]}"
        return "Invalid player or achievement"
    
    def get_player_achievements(self, player_id):
        if player_id in self.players:
            name, achievements = self.players[player_id]
            return [(aid, self.achievements[aid]) for aid in achievements]
        return []
    
    def get_common_achievements(self, player1_id, player2_id):
        if player1_id in self.players and player2_id in self.players:
            ach1 = self.players[player1_id][1]
            ach2 = self.players[player2_id][1]
            common = ach1 & ach2
            return [(aid, self.achievements[aid]) for aid in common]
        return []
    
    def leaderboard(self):
        player_scores = []
        for player_id, (name, achievements) in self.players.items():
            player_scores.append((name, len(achievements), achievements))
        return sorted(player_scores, key=lambda x: x[1], reverse=True)

# Demo achievement system
game = AchievementSystem()

# Add players
game.add_player("P001", "Alice")
game.add_player("P002", "Bob") 
game.add_player("P003", "Charlie")

# Award achievements
awards = [
    ("P001", "first_kill"), ("P001", "speed_demon"), ("P001", "collector"),
    ("P002", "first_kill"), ("P002", "explorer"),
    ("P003", "first_kill"), ("P003", "speed_demon"), ("P003", "master")
]

print("Achievement System:")
for player_id, achievement_id in awards:
    result = game.award_achievement(player_id, achievement_id)
    print(f"  {result}")

print("\n🏆 Leaderboard:")
for rank, (name, count, achievements) in enumerate(game.leaderboard(), 1):
    print(f"  #{rank}: {name} - {count} achievements")

# Common achievements
common = game.get_common_achievements("P001", "P003")
if common:
    print(f"\nAlice and Charlie both have:")
    for aid, name in common:
        print(f"  - {name}")

# Bài 8.5: Advanced data processing
print("\nBài 8.5: Advanced data processing")
def process_survey_data(responses):
    """Process survey responses using tuples and sets"""
    
    # responses: list of tuples (respondent_id, age_group, preferences_set)
    age_groups = set()
    all_preferences = set()
    age_group_data = {}
    
    for resp_id, age_group, preferences in responses:
        age_groups.add(age_group)
        all_preferences.update(preferences)
        
        if age_group not in age_group_data:
            age_group_data[age_group] = []
        age_group_data[age_group].append((resp_id, preferences))
    
    # Analysis
    results = {}
    for age_group in age_groups:
        group_responses = age_group_data[age_group]
        group_preferences = set()
        
        for resp_id, preferences in group_responses:
            group_preferences.update(preferences)
        
        # Common preferences in this age group
        if len(group_responses) > 1:
            common_prefs = group_responses[0][1].copy()
            for resp_id, preferences in group_responses[1:]:
                common_prefs &= preferences
        else:
            common_prefs = group_responses[0][1] if group_responses else set()
        
        results[age_group] = {
            "count": len(group_responses),
            "unique_preferences": group_preferences,
            "common_preferences": common_prefs,
            "diversity": len(group_preferences)
        }
    
    return results, all_preferences

# Sample survey data
survey_responses = [
    ("R001", "18-25", {"gaming", "music", "sports", "travel"}),
    ("R002", "18-25", {"gaming", "movies", "music", "reading"}),
    ("R003", "26-35", {"travel", "cooking", "fitness", "music"}),
    ("R004", "26-35", {"reading", "cooking", "gardening", "music"}),
    ("R005", "36-45", {"gardening", "cooking", "reading", "wine"}),
    ("R006", "36-45", {"fitness", "travel", "cooking", "photography"})
]

analysis, all_prefs = process_survey_data(survey_responses)

print("Survey Analysis Results:")
print(f"All preferences mentioned: {all_prefs}")

for age_group, data in analysis.items():
    print(f"\nAge Group {age_group}:")
    print(f"  Respondents: {data['count']}")
    print(f"  Preference diversity: {data['diversity']}")
    print(f"  Common preferences: {data['common_preferences']}")
    print(f"  All preferences: {data['unique_preferences']}")

print("\n" + "=" * 50)
print("🎉 HOÀN THÀNH BÀI TẬP 2: TUPLES VÀ SETS!")
print("✅ Đã thực hành: Tuple operations, unpacking/packing")
print("✅ Đã làm quen: Set operations, mathematical operations")
print("✅ Đã áp dụng: Practical applications với tuples và sets")
print("🚀 Tiếp theo: Bài tập 3 - Methods và Operations!")
print("=" * 50) 