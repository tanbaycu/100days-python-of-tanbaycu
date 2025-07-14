# Quiz Tổng Hợp Ngày 3-4
# Biến, Số Học, String và Type Conversion

print("=== QUIZ TỔNG HỢP NGÀY 3-4 ===")
print("Biến - Số Học - String - Type Conversion")
print("=" * 50)

import random

# PHẦN 1: TRẮC NGHIỆM (50 CÂU)
print("\nPHẦN 1: TRẮC NGHIỆM (50 CÂU)")
print("=" * 50)

# Nhóm câu hỏi về BIẾN
print("\n📝 NHÓM A: BIẾN VÀ KIỂU DỮ LIỆU (Câu 1-12)")

questions = []
correct_answers = []

# Câu 1
print("\nCâu 1: Tên biến nào sau đây KHÔNG hợp lệ?")
print("A) ten_hoc_sinh    B) 2name    C) _private    D) TenHocSinh")
questions.append("B")
correct_answers.append("B")

# Câu 2
print("\nCâu 2: type(3.14) trả về gì?")
print("A) <class 'int'>    B) <class 'float'>    C) <class 'str'>    D) <class 'decimal'>")
questions.append("B")
correct_answers.append("B")

# Câu 3
a, b = 5, 3
print(f"\nCâu 3: Cho a = {a}, b = {b}. Sau lệnh a, b = b, a thì a = ?")
print(f"A) {a}    B) {b}    C) 8    D) 0")
questions.append("B")
correct_answers.append("B")

# Câu 4
print("\nCâu 4: Hằng số trong Python thường được viết như thế nào?")
print("A) pi = 3.14    B) PI = 3.14    C) Pi = 3.14    D) pI = 3.14")
questions.append("B")
correct_answers.append("B")

# Nhóm câu hỏi về SỐ HỌC
print("\n🔢 NHÓM B: SỐ HỌC VÀ PHÉP TOÁN (Câu 5-20)")

# Câu 5
result = 2 + 3 * 4
print(f"\nCâu 5: 2 + 3 * 4 = ?")
print(f"A) 20    B) {result}    C) 24    D) 11")
questions.append("B")
correct_answers.append("B")

# Câu 6
result = 17 // 5
print(f"\nCâu 6: 17 // 5 = ?")
print(f"A) 3.4    B) {result}    C) 4    D) 2")
questions.append("B")
correct_answers.append("B")

# Câu 7
result = 17 % 5
print(f"\nCâu 7: 17 % 5 = ?")
print(f"A) 3    B) {result}    C) 12    D) 5")
questions.append("B")
correct_answers.append("B")

# Câu 8
result = 2 ** 3
print(f"\nCâu 8: 2 ** 3 = ?")
print(f"A) 6    B) {result}    C) 9    D) 23")
questions.append("B")
correct_answers.append("B")

# Câu 9
result = abs(-7)
print(f"\nCâu 9: abs(-7) = ?")
print(f"A) -7    B) {result}    C) 0    D) 14")
questions.append("B")
correct_answers.append("B")

# Câu 10
result = round(3.7)
print(f"\nCâu 10: round(3.7) = ?")
print(f"A) 3    B) {result}    C) 3.7    D) 3.0")
questions.append("B")
correct_answers.append("B")

# Nhóm câu hỏi về STRING
print("\n📝 NHÓM C: STRING (Câu 11-30)")

# Câu 11
text = "Python"
print(f"\nCâu 11: len('Python') = ?")
print(f"A) 5    B) {len(text)}    C) 7    D) 8")
questions.append("B")
correct_answers.append("B")

# Câu 12
print(f"\nCâu 12: 'Python'[0] = ?")
print(f"A) 'P'    B) '{text[0]}'    C) 'y'    D) 0")
questions.append("B")
correct_answers.append("B")

# Câu 13
print(f"\nCâu 13: 'Python'[-1] = ?")
print(f"A) 'P'    B) '{text[-1]}'    C) -1    D) 'o'")
questions.append("B")
correct_answers.append("B")

# Câu 14
result = text.upper()
print(f"\nCâu 14: 'Python'.upper() = ?")
print(f"A) 'python'    B) '{result}'    C) 'Python'    D) 'pYTHON'")
questions.append("B")
correct_answers.append("B")

# Câu 15
result = text.find('t')
print(f"\nCâu 15: 'Python'.find('t') = ?")
print(f"A) 1    B) {result}    C) 3    D) -1")
questions.append("B")
correct_answers.append("B")

# Câu 16
result = text.count('y')
print(f"\nCâu 16: 'Python'.count('y') = ?")
print(f"A) 0    B) {result}    C) 2    D) 3")
questions.append("B")
correct_answers.append("B")

# Câu 17
result = "hello world".split()
print(f"\nCâu 17: 'hello world'.split() trả về gì?")
print(f"A) 'hello world'    B) {result}    C) ['hello', 'world']    D) 'hello', 'world'")
questions.append("B")
correct_answers.append("B")

# Câu 18
result = "-".join(['a', 'b', 'c'])
print(f"\nCâu 18: '-'.join(['a', 'b', 'c']) = ?")
print(f"A) 'abc'    B) '{result}'    C) ['a-b-c']    D) 'a b c'")
questions.append("B")
correct_answers.append("B")

# Nhóm câu hỏi về TYPE CONVERSION
print("\n🔄 NHÓM D: CHUYỂN ĐỔI KIỂU (Câu 19-30)")

# Câu 19
result = int("123")
print(f"\nCâu 19: int('123') = ?")
print(f"A) '123'    B) {result}    C) 123.0    D) Lỗi")
questions.append("B")
correct_answers.append("B")

# Câu 20
result = float("3.14")
print(f"\nCâu 20: float('3.14') = ?")
print(f"A) 3    B) {result}    C) '3.14'    D) 3.14.0")
questions.append("B")
correct_answers.append("B")

# Câu 21
result = str(42)
print(f"\nCâu 21: str(42) = ?")
print(f"A) 42    B) '{result}'    C) 42.0    D) [42]")
questions.append("B")
correct_answers.append("B")

# Câu 22
result = int(7.9)
print(f"\nCâu 22: int(7.9) = ?")
print(f"A) 8    B) {result}    C) 7.9    D) Lỗi")
questions.append("B")
correct_answers.append("B")

# Câu 23
result = bool("")
print(f"\nCâu 23: bool('') = ?")
print(f"A) True    B) {result}    C) ''    D) Lỗi")
questions.append("B")
correct_answers.append("B")

# Câu 24
result = bool("hello")
print(f"\nCâu 24: bool('hello') = ?")
print(f"A) False    B) {result}    C) 'hello'    D) Lỗi")
questions.append("B")
correct_answers.append("B")

# CÂU HỎI NÂNG CAO
print("\n🚀 NHÓM E: CÂU HỎI NÂNG CAO (Câu 25-30)")

# Câu 25
name = "Nguyen Van An"
initials = "".join([word[0] for word in name.split()])
print(f"\nCâu 25: Code sau tạo ra gì từ 'Nguyen Van An'?")
print("name.split() → [word[0] for word in ...] → ''.join(...)")
print(f"A) 'Nguyen'    B) '{initials}'    C) ['N', 'V', 'A']    D) 'An'")
questions.append("B")
correct_answers.append("B")

# Câu 26
x = 10
x += 5
x *= 2
print(f"\nCâu 26: Cho x = 10. Sau x += 5 và x *= 2 thì x = ?")
print(f"A) 25    B) {x}    C) 20    D) 100")
questions.append("B")
correct_answers.append("B")

# Câu 27
text = "Programming"
result = text[2:7]
print(f"\nCâu 27: 'Programming'[2:7] = ?")
print(f"A) 'ogram'    B) '{result}'    C) 'ramm'    D) 'gram'")
questions.append("B")
correct_answers.append("B")

# Câu 28
text = "hello"
result = text[::-1]
print(f"\nCâu 28: 'hello'[::-1] = ?")
print(f"A) 'hello'    B) '{result}'    C) 'h'    D) 'o'")
questions.append("B")
correct_answers.append("B")

# Câu 29
price = 1234567
formatted = f"{price:,}"
print(f"\nCâu 29: f'{price:,}' tạo ra string nào?")
print(f"A) '1234567'    B) '{formatted}'    C) '1.234.567'    D) '1_234_567'")
questions.append("B")
correct_answers.append("B")

# Câu 30
result = "Python" in "I love Python programming"
print(f"\nCâu 30: 'Python' in 'I love Python programming' = ?")
print(f"A) False    B) {result}    C) 'Python'    D) 6")
questions.append("B")
correct_answers.append("B")

# PHẦN 2: TỰ LUẬN
print("\n" + "="*50)
print("PHẦN 2: CÂU HỎI TỰ LUẬN")
print("="*50)

print("\n📝 Bài 1: Viết code tính BMI")
print("Yêu cầu:")
print("- Khai báo biến cân nặng và chiều cao")
print("- Tính BMI = cân nặng / (chiều cao^2)")
print("- In kết quả với 2 chữ số thập phân")
print("\nLời giải mẫu:")
print("```python")
print("can_nang = 65  # kg")
print("chieu_cao = 1.70  # m")
print("bmi = can_nang / (chieu_cao ** 2)")
print("print(f'BMI: {bmi:.2f}')")
print("```")

print("\n📝 Bài 2: Xử lý chuỗi họ tên")
print("Yêu cầu:")
print("- Cho string: '  nGuYeN    vAn     aN  '")
print("- Chuẩn hóa thành 'Nguyen Van An'")
print("- Tạo chữ cái đầu 'NVA'")
print("\nLời giải mẫu:")
print("```python")
print("ten_tho = '  nGuYeN    vAn     aN  '")
print("ten_chuan = ' '.join(ten_tho.strip().split()).title()")
print("chu_cai_dau = ''.join([word[0] for word in ten_chuan.split()])")
print("print(f'Tên chuẩn: {ten_chuan}')")
print("print(f'Chữ cái đầu: {chu_cai_dau}')")
print("```")

print("\n📝 Bài 3: Chuyển đổi nhiệt độ")
print("Yêu cầu:")
print("- Nhận nhiệt độ Celsius từ string")
print("- Chuyển sang Fahrenheit và Kelvin")
print("- Xử lý lỗi nếu input không hợp lệ")
print("\nLời giải mẫu:")
print("```python")
print("celsius_str = '25'")
print("try:")
print("    celsius = float(celsius_str)")
print("    fahrenheit = celsius * 9/5 + 32")
print("    kelvin = celsius + 273.15")
print("    print(f'{celsius}°C = {fahrenheit}°F = {kelvin}K')")
print("except ValueError:")
print("    print('Nhiệt độ không hợp lệ')")
print("```")

print("\n📝 Bài 4: Tính tiền mua hàng")
print("Yêu cầu:")
print("- Áo: 250,000 VND x 2 cái")
print("- Quần: 180,000 VND x 1 cái") 
print("- Giảm giá 15%")
print("- Tính tổng tiền phải trả")
print("\nLời giải mẫu:")
print("```python")
print("gia_ao, so_luong_ao = 250000, 2")
print("gia_quan, so_luong_quan = 180000, 1")
print("giam_gia = 15  # %")
print("")
print("tong_tien = (gia_ao * so_luong_ao) + (gia_quan * so_luong_quan)")
print("tien_giam = tong_tien * giam_gia / 100")
print("phai_tra = tong_tien - tien_giam")
print("")
print("print(f'Tổng tiền: {tong_tien:,} VND')")
print("print(f'Giảm {giam_gia}%: -{tien_giam:,} VND')")
print("print(f'Phải trả: {phai_tra:,} VND')")
print("```")

print("\n📝 Bài 5: Phân tích văn bản")
print("Yêu cầu:")
print("- Cho string: 'Python is awesome. Python is easy!'")
print("- Đếm số từ, số ký tự (không tính space)")
print("- Tìm từ 'Python' xuất hiện bao nhiêu lần")
print("\nLời giải mẫu:")
print("```python")
print("text = 'Python is awesome. Python is easy!'")
print("words = text.split()")
print("so_tu = len(words)")
print("so_ky_tu = len(text.replace(' ', ''))")
print("so_lan_python = text.count('Python')")
print("")
print("print(f'Số từ: {so_tu}')")
print("print(f'Số ký tự: {so_ky_tu}')")
print("print(f'Python xuất hiện: {so_lan_python} lần')")
print("```")

# PHẦN 3: THÁCH THỨC
print("\n" + "="*50)
print("PHẦN 3: BÀI TẬP THÁCH THỨC")
print("="*50)

print("\n🏆 Thách thức 1: Tạo mật khẩu thông minh")
print("Yêu cầu:")
print("- Input: Họ tên, năm sinh, sở thích")
print("- Output: Mật khẩu format: [Chữ cái đầu][Năm][3 ký tự đầu sở thích]!")
print("- VD: 'Nguyen Van An', 2005, 'Python' → 'NVA2005Pyt!'")

print("\n🏆 Thách thức 2: Validation dữ liệu học sinh")
print("Yêu cầu:")
print("- Input: 'Tên,Tuổi,Điểm'")
print("- Kiểm tra tuổi (15-25), điểm (0-10)")
print("- Chuẩn hóa tên (Title case)")
print("- Báo lỗi nếu dữ liệu không hợp lệ")

print("\n🏆 Thách thức 3: Máy tính string")
print("Yêu cầu:")
print("- Input: '10 + 5' (dạng string)")
print("- Parse và tính toán")
print("- Hỗ trợ +, -, *, /")
print("- Xử lý lỗi và edge cases")

# BẢNG ĐÁP ÁN
print("\n" + "="*50)
print("BẢNG ĐÁP ÁN TRẮC NGHIỆM")
print("="*50)

print("\nĐáp án các câu trắc nghiệm:")
for i in range(1, min(31, len(correct_answers) + 1)):
    if i <= len(correct_answers):
        print(f"Câu {i}: {correct_answers[i-1]}")

# THỐNG KÊ KIẾN THỨC
print("\n" + "="*50)
print("TỔNG KẾT KIẾN THỨC NGÀY 3-4")
print("="*50)

print("\n✅ BẠN ĐÃ HỌC ĐƯỢC:")
print("1. BIẾN:")
print("   - Khai báo, gán, đổi tên")
print("   - Kiểu dữ liệu: int, float, str, bool")
print("   - Quy tắc đặt tên")

print("\n2. SỐ HỌC:")
print("   - Tất cả phép toán: +, -, *, /, //, %, **")
print("   - Thứ tự ưu tiên")
print("   - Hàm toán học: abs(), round(), min(), max()")

print("\n3. STRING:")
print("   - Tạo, nối, format (f-string)")
print("   - Methods: upper(), lower(), find(), count(), split(), join()")
print("   - Slicing: [start:end:step]")

print("\n4. TYPE CONVERSION:")
print("   - int(), float(), str(), bool()")
print("   - Xử lý lỗi ValueError")
print("   - Validation an toàn")

print("\n📊 ĐIỂM ĐÁNH GIÁ:")
print("- Cơ bản (0-15 câu đúng): Cần ôn lại")
print("- Khá (16-22 câu đúng): Tốt, tiếp tục")
print("- Giỏi (23-27 câu đúng): Rất tốt")
print("- Xuất sắc (28-30 câu đúng): Hoàn hảo!")

print("\n🎯 CHUẨN BỊ CHO NGÀY 5-6:")
print("- Ôn lại boolean (True/False)")
print("- Tìm hiểu so sánh (==, !=, <, >)")
print("- Thực hành logic (and, or, not)")

print("\n" + "="*50)
print("CHÚC BẠN HỌC TẬP TỐT!")
print("="*50) 