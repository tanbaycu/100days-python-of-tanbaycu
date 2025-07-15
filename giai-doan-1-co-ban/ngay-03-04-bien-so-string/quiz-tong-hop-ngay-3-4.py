"""
=== QUIZ TỔNG HỢP NGÀY 3-4: BIẾN, SỐ HỌC, STRING ===
Quiz tương tác với giao diện màu sắc và theo dõi điểm số real-time

Chủ đề: Variables, Arithmetic, String Manipulation, Type Conversion
Level: Beginner to Intermediate
"""

import random
import os
from colorama import Fore, Back, Style, init

# Khởi tạo colorama
init(autoreset=True)

class QuizManager:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.current_question = 0
        
    def clear_screen(self):
        """Clear màn hình cho cả Windows và Unix"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Hiển thị header đẹp mắt"""
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + Style.BRIGHT + "   🐍 QUIZ TỔNG HỢP NGÀY 3-4: BIẾN, SỐ HỌC, STRING   ")
        print(Fore.CYAN + "=" * 60)
        print(Fore.WHITE + f"Câu hỏi: {self.current_question}/{self.total_questions} | " + 
              Fore.GREEN + f"Điểm số: {self.score}")
        print(Fore.CYAN + "-" * 60)
    
    def ask_question(self, question, options, correct_answer, explanation=""):
        """Hỏi một câu trắc nghiệm"""
        self.clear_screen()
        self.current_question += 1
        self.display_header()
        
        print(Fore.WHITE + Style.BRIGHT + f"Câu {self.current_question}: {question}\n")
        
        # Hiển thị các lựa chọn
        for i, option in enumerate(options, 1):
            print(Fore.CYAN + f"{i}. {option}")
        
        # Lấy input từ user
        while True:
            try:
                print()
                user_input = input(Fore.YELLOW + "Chọn đáp án (1-4): ").strip()
                choice = int(user_input)
                if 1 <= choice <= 4:
                    break
                else:
                    print(Fore.RED + "Vui lòng chọn số từ 1-4!")
            except ValueError:
                print(Fore.RED + "Vui lòng nhập số!")
        
        # Kiểm tra đáp án
        is_correct = choice == correct_answer
        if is_correct:
            self.score += 1
            print(Fore.GREEN + Style.BRIGHT + "\n✓ CHÍNH XÁC!")
        else:
            print(Fore.RED + Style.BRIGHT + f"\n✗ SAI RỒI! Đáp án đúng là: {correct_answer}")
        
        if explanation:
            print(Fore.MAGENTA + f"💡 Giải thích: {explanation}")
        
        input(Fore.YELLOW + "\nNhấn Enter để tiếp tục...")
    
    def show_final_score(self):
        """Hiển thị kết quả cuối cùng"""
        self.clear_screen()
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + Style.BRIGHT + "           🎉 KẾT QUẢ CUỐI CÙNG 🎉")
        print(Fore.CYAN + "=" * 60)
        
        percentage = (self.score / self.total_questions) * 100
        print(Fore.WHITE + f"Tổng câu hỏi: {self.total_questions}")
        print(Fore.GREEN + f"Số câu đúng: {self.score}")
        print(Fore.RED + f"Số câu sai: {self.total_questions - self.score}")
        print(Fore.YELLOW + f"Phần trăm: {percentage:.1f}%")
        
        # Xếp loại
        if percentage >= 90:
            grade = "XUẤT SẮC 🏆"
            color = Fore.YELLOW
        elif percentage >= 80:
            grade = "GIỎI 🥇"
            color = Fore.GREEN
        elif percentage >= 70:
            grade = "KHÁ 🥈"
            color = Fore.CYAN
        elif percentage >= 60:
            grade = "TRUNG BÌNH 🥉"
            color = Fore.BLUE
        else:
            grade = "CẦN CỐ GẮNG 📚"
            color = Fore.RED
        
        print(color + Style.BRIGHT + f"\nXếp loại: {grade}")
        
        # Gợi ý cải thiện
        if percentage < 70:
            print(Fore.MAGENTA + "\n💡 Gợi ý cải thiện:")
            print("- Ôn lại lý thuyết về biến và kiểu dữ liệu")
            print("- Thực hành thêm các phép toán số học")
            print("- Làm quen với các method của string")
            print("- Luyện tập type conversion an toàn")

# Tạo quiz manager
quiz = QuizManager()

# BANK CÂU HỎI TRẮC NGHIỆM
questions_bank = [
    # PHẦN 1: BIẾN VÀ KIỂU DỮ LIỆU
    {
        "question": "Cách nào sau đây là ĐÚNG để khai báo biến trong Python?",
        "options": [
            "var name = 'John'",
            "name = 'John'", 
            "String name = 'John'",
            "declare name = 'John'"
        ],
        "answer": 2,
        "explanation": "Python không cần từ khóa khai báo biến, chỉ cần gán giá trị trực tiếp"
    },
    {
        "question": "Kiểu dữ liệu nào sẽ được trả về bởi type(3.14)?",
        "options": ["int", "float", "double", "decimal"],
        "answer": 2,
        "explanation": "Số thập phân trong Python có kiểu dữ liệu float"
    },
    {
        "question": "Biến nào sau đây có tên HỢP LỆ trong Python?",
        "options": ["2name", "_private_var", "class", "my-variable"],
        "answer": 2,
        "explanation": "_private_var hợp lệ vì bắt đầu bằng underscore và chỉ chứa ký tự cho phép"
    },
    {
        "question": "Kết quả của bool('') là gì?",
        "options": ["True", "False", "None", "Error"],
        "answer": 2,
        "explanation": "String rỗng được coi là False trong Python"
    },
    {
        "question": "Cách nào để kiểm tra kiểu dữ liệu của biến x?",
        "options": ["typeof(x)", "type(x)", "x.type()", "datatype(x)"],
        "answer": 2,
        "explanation": "type(x) là hàm built-in để kiểm tra kiểu dữ liệu"
    },
    
    # PHẦN 2: SỐ HỌC VÀ TOÁN TỬ
    {
        "question": "Kết quả của 17 // 5 là gì?",
        "options": ["3.4", "3", "4", "3.0"],
        "answer": 2,
        "explanation": "// là phép chia lấy nguyên, 17 chia 5 được 3 dư 2"
    },
    {
        "question": "Toán tử ** trong Python dùng để làm gì?",
        "options": ["Nhân đôi", "Lũy thừa", "Nhân", "Chia"],
        "answer": 2,
        "explanation": "** là toán tử lũy thừa, ví dụ 2**3 = 8"
    },
    {
        "question": "Kết quả của 10 % 3 là gì?",
        "options": ["3", "1", "0", "3.33"],
        "answer": 2,
        "explanation": "% là phép chia lấy dư, 10 chia 3 được 3 dư 1"
    },
    {
        "question": "Thứ tự ưu tiên của các phép toán: 2 + 3 * 4",
        "options": ["20", "14", "10", "Error"],
        "answer": 2,
        "explanation": "Nhân có ưu tiên cao hơn cộng: 2 + (3 * 4) = 2 + 12 = 14"
    },
    {
        "question": "Kết quả của round(4.567, 2) là gì?",
        "options": ["4.56", "4.57", "5", "4.6"],
        "answer": 2,
        "explanation": "round(4.567, 2) làm tròn đến 2 chữ số thập phân: 4.57"
    },
    
    # PHẦN 3: XỬ LÝ STRING
    {
        "question": "Cách nào để lấy ký tự đầu tiên của string 'Python'?",
        "options": ["'Python'[1]", "'Python'[0]", "'Python'.first()", "'Python'[-1]"],
        "answer": 2,
        "explanation": "Index trong Python bắt đầu từ 0, nên [0] là ký tự đầu tiên"
    },
    {
        "question": "Kết quả của 'Hello' + ' ' + 'World' là gì?",
        "options": ["Hello World", "HelloWorld", "Hello+World", "Error"],
        "answer": 1,
        "explanation": "Toán tử + nối các string lại với nhau"
    },
    {
        "question": "Method nào để chuyển string thành chữ HOA?",
        "options": ["capitalize()", "upper()", "title()", "swapcase()"],
        "answer": 2,
        "explanation": "upper() chuyển tất cả ký tự thành chữ HOA"
    },
    {
        "question": "Kết quả của len('Python') là gì?",
        "options": ["5", "6", "7", "4"],
        "answer": 2,
        "explanation": "Python có 6 ký tự: P-y-t-h-o-n"
    },
    {
        "question": "'Python'[1:4] sẽ trả về gì?",
        "options": ["Pyt", "yth", "ytho", "tho"],
        "answer": 2,
        "explanation": "Slicing [1:4] lấy từ index 1 đến 3 (không bao gồm 4): 'yth'"
    },
    
    # PHẦN 4: TYPE CONVERSION
    {
        "question": "Cách nào để chuyển string '123' thành integer?",
        "options": ["integer('123')", "int('123')", "to_int('123')", "'123'.int()"],
        "answer": 2,
        "explanation": "int() là hàm built-in để chuyển đổi sang kiểu integer"
    },
    {
        "question": "Kết quả của str(42) là gì?",
        "options": ["42", "'42'", "42.0", "Error"],
        "answer": 2,
        "explanation": "str(42) chuyển số 42 thành string '42'"
    },
    {
        "question": "float('3.14') sẽ trả về gì?",
        "options": ["3.14", "'3.14'", "3", "Error"],
        "answer": 1,
        "explanation": "float() chuyển string số thành kiểu float"
    },
    {
        "question": "Điều gì xảy ra khi int('hello')?",
        "options": ["0", "None", "ValueError", "'hello'"],
        "answer": 3,
        "explanation": "Không thể chuyển string không phải số thành int, sẽ raise ValueError"
    },
    {
        "question": "Kết quả của bool(0) là gì?",
        "options": ["True", "False", "0", "None"],
        "answer": 2,
        "explanation": "Số 0 được coi là False trong Python"
    },
    
    # PHẦN 5: ỨNG DỤNG TỔNG HỢP
    {
        "question": "Code nào tính BMI đúng cách? (BMI = weight / height²)",
        "options": [
            "bmi = weight / height * 2",
            "bmi = weight / (height ** 2)",
            "bmi = weight * height ** 2", 
            "bmi = (weight / height) ** 2"
        ],
        "answer": 2,
        "explanation": "BMI = cân nặng chia cho bình phương chiều cao"
    },
    {
        "question": "Cách nào để lấy 3 ký tự cuối của string?",
        "options": ["text[3:]", "text[-3:]", "text[:3]", "text[:-3]"],
        "answer": 2,
        "explanation": "[-3:] lấy từ ký tự thứ 3 từ cuối đến hết"
    },
    {
        "question": "Input validation an toàn cho việc nhập tuổi:",
        "options": [
            "age = int(input())",
            "age = input().int()",
            "try: age = int(input()) except: age = 0",
            "age = input() if input().isdigit() else 0"
        ],
        "answer": 3,
        "explanation": "Try-except bắt được exception khi input không hợp lệ"
    },
    {
        "question": "Cách format string với f-string:",
        "options": [
            "f'Tên: name, tuổi: age'",
            "f'Tên: {name}, tuổi: {age}'",
            "'Tên: {name}, tuổi: {age}'.format()",
            "format('Tên: name, tuổi: age')"
        ],
        "answer": 2,
        "explanation": "F-string cần dấu {} để chèn biến vào chuỗi"
    },
    {
        "question": "Method nào kiểm tra string chỉ chứa số?",
        "options": ["isnumber()", "isdigit()", "isnumeric()", "Cả B và C"],
        "answer": 4,
        "explanation": "Cả isdigit() và isnumeric() đều kiểm tra string chỉ chứa số"
    },
    
    # PHẦN 6: THÁCH THỨC NÂNG CAO
    {
        "question": "Kết quả của '5' * 3 là gì?",
        "options": ["15", "'555'", "Error", "'5' + '5' + '5'"],
        "answer": 2,
        "explanation": "Toán tử * với string tạo ra string lặp lại: '5' * 3 = '555'"
    },
    {
        "question": "Cách tối ưu để đảo ngược string?",
        "options": ["reverse(text)", "text.reverse()", "text[::-1]", "text[-1:0]"],
        "answer": 3,
        "explanation": "Slicing [::-1] là cách pythonic để đảo ngược string"
    },
    {
        "question": "Expression nào kiểm tra số chẵn?",
        "options": ["x % 2", "x % 2 == 0", "x / 2 == int(x/2)", "even(x)"],
        "answer": 2,
        "explanation": "Số chẵn khi chia 2 có số dư bằng 0"
    },
    {
        "question": "Cách an toàn nhất để ghép nhiều string?",
        "options": [
            "s1 + s2 + s3 + s4",
            "''.join([s1, s2, s3, s4])",
            "format(s1, s2, s3, s4)",
            "s1.append(s2, s3, s4)"
        ],
        "answer": 2,
        "explanation": "join() hiệu quả hơn khi ghép nhiều string"
    },
    {
        "question": "Escape sequence nào tạo xuống dòng?",
        "options": ["\\t", "\\n", "\\r", "\\b"],
        "answer": 2,
        "explanation": "\\n (newline) tạo xuống dòng mới"
    }
]

def main_menu():
    """Menu chính của quiz"""
    quiz.clear_screen()
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "   🐍 QUIZ TỔNG HỢP NGÀY 3-4: BIẾN, SỐ HỌC, STRING   ")
    print(Fore.CYAN + "=" * 60)
    print(Fore.WHITE + "\nChọn chế độ quiz:")
    print(Fore.GREEN + "1. Quiz nhanh (10 câu ngẫu nhiên)")
    print(Fore.YELLOW + "2. Quiz đầy đủ (20 câu ngẫu nhiên)")
    print(Fore.RED + "3. Quiz hoàn chỉnh (tất cả 30 câu)")
    print(Fore.CYAN + "4. Quiz theo chủ đề")
    print(Fore.MAGENTA + "0. Thoát")
    
    while True:
        try:
            choice = input(Fore.YELLOW + "\nChọn (0-4): ").strip()
            if choice in ['0', '1', '2', '3', '4']:
                return choice
            else:
                print(Fore.RED + "Vui lòng chọn từ 0-4!")
        except:
            print(Fore.RED + "Input không hợp lệ!")

def run_quiz(num_questions=None, topic_filter=None):
    """Chạy quiz với số câu hỏi xác định"""
    available_questions = questions_bank.copy()
    
    if topic_filter:
        # Lọc theo chủ đề nếu cần
        pass
    
    if num_questions:
        if num_questions > len(available_questions):
            num_questions = len(available_questions)
        selected_questions = random.sample(available_questions, num_questions)
    else:
        selected_questions = available_questions
    
    quiz.total_questions = len(selected_questions)
    quiz.score = 0
    quiz.current_question = 0
    
    # Bắt đầu quiz
    for q in selected_questions:
        quiz.ask_question(
            q["question"],
            q["options"], 
            q["answer"],
            q.get("explanation", "")
        )
    
    # Hiển thị kết quả
    quiz.show_final_score()

def topic_menu():
    """Menu chọn chủ đề"""
    quiz.clear_screen()
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "           CHỌN CHỦ ĐỀ QUIZ")
    print(Fore.CYAN + "=" * 60)
    print(Fore.WHITE + "\nCác chủ đề có sẵn:")
    print(Fore.GREEN + "1. Biến và kiểu dữ liệu (5 câu)")
    print(Fore.YELLOW + "2. Số học và toán tử (5 câu)")
    print(Fore.CYAN + "3. Xử lý string (5 câu)")
    print(Fore.MAGENTA + "4. Type conversion (5 câu)")
    print(Fore.BLUE + "5. Ứng dụng tổng hợp (5 câu)")
    print(Fore.RED + "6. Thách thức nâng cao (5 câu)")
    print(Fore.WHITE + "0. Quay lại menu chính")
    
    while True:
        try:
            choice = input(Fore.YELLOW + "\nChọn chủ đề (0-6): ").strip()
            if choice == '0':
                return None
            elif choice in ['1', '2', '3', '4', '5', '6']:
                # Lấy 5 câu đầu của mỗi chủ đề
                start_idx = (int(choice) - 1) * 5
                end_idx = start_idx + 5
                topic_questions = questions_bank[start_idx:end_idx]
                
                quiz.total_questions = len(topic_questions)
                quiz.score = 0
                quiz.current_question = 0
                
                for q in topic_questions:
                    quiz.ask_question(
                        q["question"],
                        q["options"],
                        q["answer"], 
                        q.get("explanation", "")
                    )
                
                quiz.show_final_score()
                return True
            else:
                print(Fore.RED + "Vui lòng chọn từ 0-6!")
        except:
            print(Fore.RED + "Input không hợp lệ!")

def main():
    """Hàm main điều khiển chương trình"""
    print(Fore.GREEN + "Khởi tạo quiz system...")
    print(Fore.YELLOW + "Đang tải ngân hàng câu hỏi...")
    
    while True:
        choice = main_menu()
        
        if choice == '0':
            quiz.clear_screen()
            print(Fore.GREEN + Style.BRIGHT + "Cảm ơn bạn đã học Python! 🐍")
            print(Fore.CYAN + "Hẹn gặp lại trong những bài học tiếp theo!")
            break
        elif choice == '1':
            run_quiz(10)
        elif choice == '2':
            run_quiz(20)
        elif choice == '3':
            run_quiz()  # Tất cả câu hỏi
        elif choice == '4':
            result = topic_menu()
            if result is None:
                continue
        
        # Hỏi có muốn tiếp tục không
        print()
        continue_choice = input(Fore.YELLOW + "Bạn có muốn làm quiz khác không? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes', 'có', 'c']:
            quiz.clear_screen()
            print(Fore.GREEN + Style.BRIGHT + "Cảm ơn bạn đã học Python! 🐍")
            print(Fore.CYAN + "Hẹn gặp lại trong những bài học tiếp theo!")
            break

if __name__ == "__main__":
    main() 