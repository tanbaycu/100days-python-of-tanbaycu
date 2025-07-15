"""
BÀI TẬP 1: VÒNG LẶP FOR CỞ BẢN
=============================

Bài tập này gồm 12 phần từ cơ bản đến nâng cao về for loops.
Mỗi phần có ví dụ minh họa và bài tập thực hành.

Yêu cầu:
- Đọc kỹ từng phần
- Chạy code ví dụ để hiểu
- Làm bài tập ở cuối mỗi phần
- Không xóa code ví dụ, viết bài tập bên dưới

Thời gian ước tính: 90-120 phút
"""

print("🎯 BÀI TẬP 1: VÒNG LẶP FOR CỞ BẢN")
print("=" * 50)

# =============================================================================
# PHẦN A: FOR VỚI RANGE() CƠ BẢN
# =============================================================================

print("\n📖 PHẦN A: FOR VỚI RANGE() CƠ BẢN")
print("-" * 30)

# A.1. Ví dụ: range(n) - từ 0 đến n-1
print("A.1. Ví dụ range(5):")
for i in range(5):
    print(f"Số: {i}")

# A.2. Ví dụ: range(start, stop) 
print("\nA.2. Ví dụ range(3, 8):")
for i in range(3, 8):
    print(f"Từ 3 đến 7: {i}")

# A.3. Ví dụ: range(start, stop, step)
print("\nA.3. Ví dụ range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"Số chẵn: {i}")

# A.4. Ví dụ: range ngược
print("\nA.4. Ví dụ range(10, 0, -1):")
for i in range(10, 0, -1):
    print(f"Đếm ngược: {i}")

print("\n🏃‍♂️ BÀI TẬP PHẦN A:")
print("1. In các số từ 1 đến 15")
print("2. In các số từ 20 đến 30")
print("3. In các số lẻ từ 1 đến 20")
print("4. Đếm ngược từ 50 về 40")
print("5. In các số chia hết cho 5 từ 0 đến 100")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN A ---")

# Bài 1: In các số từ 1 đến 15


# Bài 2: In các số từ 20 đến 30


# Bài 3: In các số lẻ từ 1 đến 20


# Bài 4: Đếm ngược từ 50 về 40


# Bài 5: In các số chia hết cho 5 từ 0 đến 100


# =============================================================================
# PHẦN B: FOR VỚI STRINGS
# =============================================================================

print("\n📖 PHẦN B: FOR VỚI STRINGS")
print("-" * 30)

# B.1. Ví dụ: Lặp qua từng ký tự
text = "Python"
print(f"B.1. Lặp qua '{text}':")
for char in text:
    print(f"Ký tự: '{char}'")

# B.2. Ví dụ: Lặp với index
word = "Hello"
print(f"\nB.2. Lặp '{word}' với index:")
for i in range(len(word)):
    print(f"Index {i}: '{word[i]}'")

# B.3. Ví dụ: Enumerate() 
greeting = "Hi"
print(f"\nB.3. Enumerate '{greeting}':")
for index, char in enumerate(greeting):
    print(f"Vị trí {index}: '{char}'")

# B.4. Ví dụ: Đếm ký tự cụ thể
sentence = "Hello World"
count_l = 0
print(f"\nB.4. Đếm chữ 'l' trong '{sentence}':")
for char in sentence:
    if char.lower() == 'l':
        count_l += 1
        print(f"Tìm thấy 'l' tại: '{char}'")
print(f"Tổng số 'l': {count_l}")

print("\n🏃‍♂️ BÀI TẬP PHẦN B:")
print("1. In từng ký tự của tên bạn")
print("2. Đếm số nguyên âm trong 'Education'")
print("3. In vị trí của tất cả chữ 'a' trong 'banana'")
print("4. Kiểm tra chuỗi 'level' có phải palindrome")
print("5. Tạo chuỗi ngược của 'Programming'")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN B ---")

# Bài 1: In từng ký tự của tên bạn
my_name = "Tên của bạn"  # Thay bằng tên thật


# Bài 2: Đếm số nguyên âm trong 'Education'
word_education = "Education"
vowels = "aeiouAEIOU"


# Bài 3: In vị trí của tất cả chữ 'a' trong 'banana'
banana_word = "banana"


# Bài 4: Kiểm tra chuỗi 'level' có phải palindrome
check_word = "level"


# Bài 5: Tạo chuỗi ngược của 'Programming'
programming_word = "Programming"


# =============================================================================
# PHẦN C: FOR VỚI LISTS
# =============================================================================

print("\n📖 PHẦN C: FOR VỚI LISTS")
print("-" * 30)

# C.1. Ví dụ: Lặp qua elements
fruits = ["apple", "banana", "orange", "grape"]
print("C.1. Lặp qua danh sách trái cây:")
for fruit in fruits:
    print(f"Tôi thích {fruit}")

# C.2. Ví dụ: Lặp với index
colors = ["red", "green", "blue"]
print(f"\nC.2. Lặp qua màu sắc với index:")
for i in range(len(colors)):
    print(f"Màu thứ {i+1}: {colors[i]}")

# C.3. Ví dụ: Enumerate với list
numbers = [10, 20, 30]
print(f"\nC.3. Enumerate với list số:")
for index, value in enumerate(numbers):
    print(f"Index {index}: Value {value}")

# C.4. Ví dụ: Tính tổng list
scores = [85, 92, 78, 96, 88]
total = 0
print(f"\nC.4. Tính tổng điểm {scores}:")
for score in scores:
    total += score
    print(f"Cộng {score}, tổng hiện tại: {total}")
print(f"Tổng cuối cùng: {total}")

print("\n🏃‍♂️ BÀI TẬP PHẦN C:")
print("1. Tìm số lớn nhất trong [3, 7, 2, 9, 1, 8]")
print("2. Đếm số chẵn trong [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("3. Tạo list bình phương của [1, 2, 3, 4, 5]")
print("4. Tìm tất cả tên có độ dài > 5 trong danh sách")
print("5. Tính trung bình của [4.5, 3.2, 8.7, 6.1, 9.0]")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN C ---")

# Bài 1: Tìm số lớn nhất trong [3, 7, 2, 9, 1, 8]
numbers_list = [3, 7, 2, 9, 1, 8]


# Bài 2: Đếm số chẵn trong [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_1_to_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Bài 3: Tạo list bình phương của [1, 2, 3, 4, 5]
original_numbers = [1, 2, 3, 4, 5]


# Bài 4: Tìm tên có độ dài > 5
names = ["An", "Bình", "Christopher", "Dũng", "Elizabeth", "Phong"]


# Bài 5: Tính trung bình của [4.5, 3.2, 8.7, 6.1, 9.0]
grades = [4.5, 3.2, 8.7, 6.1, 9.0]


# =============================================================================
# PHẦN D: TÍNH TOÁN VỚI FOR
# =============================================================================

print("\n📖 PHẦN D: TÍNH TOÁN VỚI FOR")
print("-" * 30)

# D.1. Ví dụ: Tính tổng 1 đến n
n = 10
total_sum = 0
print(f"D.1. Tính tổng từ 1 đến {n}:")
for i in range(1, n + 1):
    total_sum += i
    print(f"i={i}, tổng={total_sum}")
print(f"Tổng cuối cùng: {total_sum}")

# D.2. Ví dụ: Tính giai thừa
factorial_n = 5
factorial = 1
print(f"\nD.2. Tính {factorial_n}! (giai thừa):")
for i in range(1, factorial_n + 1):
    factorial *= i
    print(f"i={i}, giai thừa={factorial}")
print(f"{factorial_n}! = {factorial}")

# D.3. Ví dụ: Lũy thừa
base = 2
power = 4
result = 1
print(f"\nD.3. Tính {base}^{power}:")
for i in range(power):
    result *= base
    print(f"Lần {i+1}: {result}")
print(f"{base}^{power} = {result}")

print("\n🏃‍♂️ BÀI TẬP PHẦN D:")
print("1. Tính tổng các số chẵn từ 2 đến 20")
print("2. Tính 8! (8 giai thừa)")  
print("3. Tính 3^6 (3 mũ 6)")
print("4. Tính tổng bình phương từ 1^2 đến 10^2")
print("5. Tìm tổng các số chia hết cho 3 từ 1 đến 30")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN D ---")

# Bài 1: Tính tổng các số chẵn từ 2 đến 20


# Bài 2: Tính 8! (8 giai thừa)


# Bài 3: Tính 3^6 (3 mũ 6)


# Bài 4: Tính tổng bình phương từ 1^2 đến 10^2


# Bài 5: Tìm tổng các số chia hết cho 3 từ 1 đến 30


# =============================================================================
# PHẦN E: PATTERNS VỚI FOR
# =============================================================================

print("\n📖 PHẦN E: PATTERNS VỚI FOR")
print("-" * 30)

# E.1. Ví dụ: Tam giác sao
print("E.1. Tam giác sao:")
for i in range(1, 6):
    print("*" * i)

# E.2. Ví dụ: Tam giác số
print("\nE.2. Tam giác số:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Xuống dòng

# E.3. Ví dụ: Pattern chữ cái
print("\nE.3. Pattern chữ cái:")
for i in range(1, 5):
    for j in range(i):
        char = chr(ord('A') + j)  # A, B, C, D...
        print(char, end=" ")
    print()

print("\n🏃‍♂️ BÀI TẬP PHẦN E:")
print("1. Tạo tam giác sao ngược (5 dòng giảm dần)")
print("2. Tạo pattern số theo hàng (1, 22, 333, 4444)")
print("3. Tạo tam giác vuông cân bằng số")
print("4. In pattern chữ cái theo alphabet")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN E ---")

# Bài 1: Tam giác sao ngược


# Bài 2: Pattern số theo hàng


# Bài 3: Tam giác vuông cân


# Bài 4: Pattern chữ cái alphabet


# =============================================================================
# PHẦN F: BÀI TOÁN THỰC TẾ
# =============================================================================

print("\n📖 PHẦN F: BÀI TOÁN THỰC TẾ")
print("-" * 30)

# F.1. Ví dụ: Bảng cửu chương
table_number = 7
print(f"F.1. Bảng cửu chương {table_number}:")
for i in range(1, 11):
    result = table_number * i
    print(f"{table_number} x {i:2} = {result:2}")

# F.2. Ví dụ: Kiểm tra số nguyên tố
def is_prime_demo(num):
    if num < 2:
        return False
    
    print(f"F.2. Kiểm tra {num} có phải số nguyên tố:")
    for i in range(2, int(num**0.5) + 1):
        print(f"Kiểm tra {num} % {i} = {num % i}")
        if num % i == 0:
            print(f"{num} chia hết cho {i} → Không phải số nguyên tố")
            return False
    print(f"{num} là số nguyên tố!")
    return True

is_prime_demo(17)

# F.3. Ví dụ: Tìm ước số
number = 12
print(f"\nF.3. Tìm ước số của {number}:")
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
        print(f"{i} là ước số của {number}")
print(f"Các ước số: {divisors}")

print("\n🏃‍♂️ BÀI TẬP PHẦN F:")
print("1. In bảng cửu chương của số 9")
print("2. Kiểm tra 29 có phải số nguyên tố không")
print("3. Tìm tất cả ước số của 24")
print("4. Tính tổng các chữ số của 12345")
print("5. Đếm số lần xuất hiện chữ số 3 trong 3333377")

# Viết code bài tập ở đây:
print("\n--- BÀI LÀM PHẦN F ---")

# Bài 1: Bảng cửu chương số 9


# Bài 2: Kiểm tra 29 có phải số nguyên tố


# Bài 3: Tìm ước số của 24


# Bài 4: Tính tổng chữ số của 12345


# Bài 5: Đếm chữ số 3 trong 3333377


# =============================================================================
# TỔNG KẾT VÀ ĐÁNH GIÁ
# =============================================================================

print("\n" + "="*50)
print("🏆 TỔNG KẾT BÀI TẬP 1")
print("="*50)

print("""
KIẾN THỨC ĐÃ HỌC:
✅ range() với 1, 2, 3 tham số
✅ For loop với strings
✅ For loop với lists  
✅ Tính toán với for loops
✅ Tạo patterns đơn giản
✅ Giải quyết bài toán thực tế

ĐIỂM ĐÁNH GIÁ BẢN THÂN:
- Phần A (range cơ bản): ___/5
- Phần B (strings): ___/5  
- Phần C (lists): ___/5
- Phần D (tính toán): ___/5
- Phần E (patterns): ___/4
- Phần F (thực tế): ___/5

TỔNG ĐIỂM: ___/29

CHUẨN ĐÁNH GIÁ:
🥇 25-29 điểm: Xuất sắc! 
🥈 20-24 điểm: Giỏi!
🥉 15-19 điểm: Khá
📚 10-14 điểm: Cần ôn lại
💪 <10 điểm: Học lại từ đầu

GHI CHÚ CẢM NHẬN:
- Phần nào khó nhất? ________________
- Phần nào thú vị nhất? ______________  
- Cần cải thiện gì? __________________
""")

print("🔥 Sẵn sàng cho Bài Tập 2: While Loops!")

# =============================================================================
# BONUS: THÁCH THỨC NÂNG CAO (TUỲ CHỌN)
# =============================================================================

print("\n🌟 BONUS - THÁCH THỨC NÂNG CAO:")
print("Chỉ làm nếu bạn đã hoàn thành tất cả bài tập trên!")
print("-" * 50)

print("1. Tạo pattern kim cương sao (5 tầng)")
print("2. Tìm tất cả số hoàn hảo từ 1 đến 1000")  
print("3. In bảng ASCII từ A đến Z")
print("4. Tạo password ngẫu nhiên 8 ký tự")
print("5. Viết chương trình vẽ hình chữ nhật bằng sao")

# Bonus code ở đây (nếu muốn thử thách):
print("\n--- BONUS CODE ---")

# Bonus 1: Kim cương sao


# Bonus 2: Số hoàn hảo


# Bonus 3: Bảng ASCII


# Bonus 4: Password generator


# Bonus 5: Hình chữ nhật sao


print("\n🎉 CHÚC MỪNG! BẠN ĐÃ HOÀN THÀNH BÀI TẬP 1!") 