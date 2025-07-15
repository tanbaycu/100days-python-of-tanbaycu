"""
=== QUIZ TỔNG HỢP NGÀY 7-8: VÒNG LẶP (FOR & WHILE) ===
Quiz tương tác với giao diện màu sắc và theo dõi điểm số real-time

Chủ đề: For loops, While loops, Break, Continue, Nested loops
Level: Beginner to Advanced
"""

import random
import os
import time
from colorama import Fore, Back, Style, init
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

# Khởi tạo colorama và rich
init(autoreset=True)
console = Console()

class LoopQuizManager:
    def __init__(self):
        self.score = 0
        self.total_questions = 60  # 50 trắc nghiệm + 10 coding
        self.current_question = 0
        self.wrong_answers = []
        
    def clear_screen(self):
        """Clear màn hình cho cả Windows và Unix"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Hiển thị header đẹp mắt"""
        print(Fore.CYAN + "=" * 70)
        print(Fore.YELLOW + Style.BRIGHT + "   🔄 QUIZ TỔNG HỢP NGÀY 7-8: VÒNG LẶP (FOR & WHILE)   ")
        print(Fore.CYAN + "=" * 70)
        print(Fore.WHITE + f"Câu hỏi: {self.current_question}/{self.total_questions} | " + 
              Fore.GREEN + f"Điểm số: {self.score}")
        print(Fore.CYAN + "-" * 70)
    
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
                user_choice = int(input(Fore.YELLOW + "Chọn đáp án (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print(Fore.RED + "Vui lòng chọn từ 1-4!")
            except ValueError:
                print(Fore.RED + "Vui lòng nhập số!")
        
        # Kiểm tra đáp án
        if user_choice == correct_answer:
            self.score += 1
            print(Fore.GREEN + Style.BRIGHT + "✓ CHÍNH XÁC!")
        else:
            correct_text = options[correct_answer - 1]
            user_text = options[user_choice - 1]
            print(Fore.RED + Style.BRIGHT + f"✗ SAI! Đáp án đúng là: {correct_answer}. {correct_text}")
            self.wrong_answers.append({
                'question': question,
                'user_answer': user_text,
                'correct_answer': correct_text,
                'explanation': explanation
            })
        
        if explanation:
            print(Fore.CYAN + f"\n💡 Giải thích: {explanation}")
        
        input(Fore.MAGENTA + "\nNhấn Enter để tiếp tục...")
    
    def ask_coding_question(self, question, sample_input, expected_output, explanation=""):
        """Hỏi câu hỏi coding"""
        self.clear_screen()
        self.current_question += 1
        self.display_header()
        
        print(Fore.WHITE + Style.BRIGHT + f"Câu coding {self.current_question}: {question}\n")
        print(Fore.CYAN + f"Input mẫu: {sample_input}")
        print(Fore.CYAN + f"Output mong đợi: {expected_output}\n")
        
        user_code = input(Fore.YELLOW + "Nhập code Python của bạn (một dòng): ")
        
        try:
            # Tạo môi trường an toàn để test code
            test_globals = {"__builtins__": {}}
            exec(user_code, test_globals)
            print(Fore.GREEN + Style.BRIGHT + "✓ Code hợp lệ!")
            self.score += 1
        except:
            print(Fore.RED + Style.BRIGHT + "✗ Code có lỗi hoặc không chính xác!")
            self.wrong_answers.append({
                'question': question,
                'user_answer': user_code,
                'correct_answer': expected_output,
                'explanation': explanation
            })
        
        if explanation:
            print(Fore.CYAN + f"\n💡 Giải thích: {explanation}")
        
        input(Fore.MAGENTA + "\nNhấn Enter để tiếp tục...")
    
    def show_final_results(self):
        """Hiển thị kết quả cuối cùng"""
        self.clear_screen()
        
        percentage = (self.score / self.total_questions) * 100
        
        # Xác định level
        if percentage >= 90:
            level = "XUẤT SẮC"
            color = Fore.GREEN
            emoji = "🏆"
        elif percentage >= 80:
            level = "GIỎI"
            color = Fore.YELLOW
            emoji = "🥇"
        elif percentage >= 70:
            level = "KHÁ"
            color = Fore.CYAN
            emoji = "🥈"
        elif percentage >= 60:
            level = "TRUNG BÌNH"
            color = Fore.BLUE
            emoji = "🥉"
        else:
            level = "CẦN CỐ GẮNG"
            color = Fore.RED
            emoji = "📚"
        
        print(color + "=" * 60)
        print(color + Style.BRIGHT + f"   {emoji} KẾT QUẢ QUIZ VÒNG LẶP   ")
        print(color + "=" * 60)
        print(Fore.WHITE + f"Điểm số: {self.score}/{self.total_questions}")
        print(Fore.WHITE + f"Tỷ lệ: {percentage:.1f}%")
        print(color + Style.BRIGHT + f"Xếp hạng: {level}")
        print(color + "=" * 60)
        
        # Hiển thị câu trả lời sai (nếu có)
        if self.wrong_answers:
            print(Fore.RED + "\n📝 CÁC CÂU TRẢ LỜI SAI:")
            for i, wrong in enumerate(self.wrong_answers, 1):
                print(Fore.YELLOW + f"\n{i}. {wrong['question']}")
                print(Fore.RED + f"   Bạn chọn: {wrong['user_answer']}")
                print(Fore.GREEN + f"   Đáp án đúng: {wrong['correct_answer']}")
                if wrong['explanation']:
                    print(Fore.CYAN + f"   💡 {wrong['explanation']}")
        
        print(Fore.MAGENTA + "\n🎯 Khuyến nghị học tập:")
        if percentage < 60:
            print(Fore.WHITE + "- Xem lại lý thuyết về vòng lặp for và while")
            print(Fore.WHITE + "- Thực hành thêm các bài tập cơ bản")
            print(Fore.WHITE + "- Hiểu rõ cách sử dụng break và continue")
        elif percentage < 80:
            print(Fore.WHITE + "- Luyện tập thêm nested loops")
            print(Fore.WHITE + "- Thực hành các dự án phức tạp hơn")
        else:
            print(Fore.WHITE + "- Xuất sắc! Hãy thử thách với các dự án nâng cao")
            print(Fore.WHITE + "- Chuẩn bị cho chủ đề tiếp theo: Lists và Tuples")

def run_quiz():
    """Chạy toàn bộ quiz"""
    quiz = LoopQuizManager()
    
    # Hiển thị màn hình chào mừng
    quiz.clear_screen()
    console.print(Panel.fit(
        Text("🔄 QUIZ TỔNG HỢP VÒNG LẶP\nNgày 7-8: For & While Loops", 
             style="bold cyan", justify="center"),
        style="cyan"
    ))
    print(Fore.WHITE + "\n📚 Quiz bao gồm:")
    print(Fore.CYAN + "• 50 câu trắc nghiệm về vòng lặp")
    print(Fore.CYAN + "• 10 câu coding thực hành")
    print(Fore.CYAN + "• Giải thích chi tiết cho từng câu")
    
    input(Fore.MAGENTA + "\nNhấn Enter để bắt đầu...")
    
    # PHẦN 1: CÂU HỎI TRẮC NGHIỆM (50 câu)
    
    # For Loop Cơ bản (10 câu)
    quiz.ask_question(
        "Cú pháp đúng của vòng lặp for để lặp từ 0 đến 4 là gì?",
        ["for i in range(5):", "for i in range(0,5):", "for i in 0 to 5:", "Cả A và B đều đúng"],
        4,
        "range(5) và range(0,5) đều tạo ra chuỗi từ 0 đến 4"
    )
    
    quiz.ask_question(
        "Kết quả của range(2, 8, 2) là gì?",
        ["[2, 4, 6]", "[2, 4, 6, 8]", "[2, 3, 4, 5, 6, 7]", "[0, 2, 4, 6]"],
        1,
        "range(start, stop, step) tạo ra: 2, 4, 6 (không bao gồm 8)"
    )
    
    quiz.ask_question(
        "Đoạn code nào in ra các số từ 5 đến 1 (giảm dần)?",
        ["for i in range(5, 0, -1):", "for i in range(5, 1, -1):", "for i in range(1, 5, -1):", "for i in range(1, 6, -1):"],
        1,
        "range(5, 0, -1) tạo ra: 5, 4, 3, 2, 1"
    )
    
    quiz.ask_question(
        "Vòng lặp for dùng để làm gì?",
        ["Lặp qua một chuỗi các phần tử", "Lặp với điều kiện", "Tạo hàm", "Khai báo biến"],
        1,
        "For loop dùng để lặp qua các phần tử trong iterable (list, string, range...)"
    )
    
    quiz.ask_question(
        "Kết quả của đoạn code: for i in 'abc': print(i)",
        ["a b c (trên 3 dòng)", "abc", "0 1 2", "Lỗi"],
        1,
        "For loop có thể lặp qua từng ký tự trong string"
    )
    
    quiz.ask_question(
        "len(range(10)) trả về giá trị nào?",
        ["9", "10", "11", "Lỗi"],
        2,
        "range(10) có 10 phần tử (từ 0 đến 9)"
    )
    
    quiz.ask_question(
        "Cách nào đúng để lặp qua list numbers = [1,2,3]?",
        ["for i in numbers:", "for i in len(numbers):", "for i = 0 to len(numbers):", "for numbers in i:"],
        1,
        "Cú pháp: for item in list_name"
    )
    
    quiz.ask_question(
        "Để lấy cả index và value khi lặp list, ta dùng:",
        ["for i, v in list:", "for i, v in enumerate(list):", "for i in range(list):", "for list[i] in range:"],
        2,
        "enumerate() trả về tuple (index, value)"
    )
    
    quiz.ask_question(
        "range(0) tạo ra gì?",
        ["[0]", "[]", "Lỗi", "0"],
        2,
        "range(0) tạo ra chuỗi rỗng"
    )
    
    quiz.ask_question(
        "Vòng lặp for có thể lặp qua kiểu dữ liệu nào?",
        ["Chỉ numbers", "Chỉ strings", "Tất cả iterable objects", "Chỉ lists"],
        3,
        "For loop hoạt động với bất kỳ iterable nào: string, list, tuple, range..."
    )
    
    # While Loop (10 câu)
    quiz.ask_question(
        "Điều kiện nào cần thiết cho vòng lặp while?",
        ["Phải có biến đếm", "Phải có điều kiện boolean", "Phải có break", "Phải có list"],
        2,
        "While loop cần điều kiện boolean để quyết định tiếp tục hay dừng"
    )
    
    quiz.ask_question(
        "Vòng lặp vô hạn xảy ra khi nào?",
        ["Điều kiện while luôn True", "Quên update biến điều kiện", "Không có break", "Tất cả đáp án trên"],
        4,
        "Infinite loop xảy ra khi điều kiện không bao giờ False"
    )
    
    quiz.ask_question(
        "Đoạn code nào in ra số từ 1 đến 5?",
        ["i=1; while i<=5: print(i)", "i=1; while i<=5: print(i); i+=1", "i=0; while i<5: print(i+1); i+=1", "B và C đều đúng"],
        4,
        "Cần nhớ update biến điều kiện để tránh vòng lặp vô hạn"
    )
    
    quiz.ask_question(
        "While loop thích hợp nhất khi nào?",
        ["Biết trước số lần lặp", "Không biết trước số lần lặp", "Lặp qua list", "Tạo range"],
        2,
        "While loop tốt khi số lần lặp phụ thuộc vào điều kiện động"
    )
    
    quiz.ask_question(
        "Sự khác biệt chính giữa for và while là gì?",
        ["For nhanh hơn while", "While nhanh hơn for", "For có cấu trúc cố định, while linh hoạt hơn", "Không có sự khác biệt"],
        3,
        "For loop có cấu trúc rõ ràng, while loop linh hoạt với điều kiện"
    )
    
    quiz.ask_question(
        "Để đọc input đến khi user nhập 'quit', ta dùng:",
        ["for input in 'quit':", "while input != 'quit':", "while True: if input=='quit': break", "B và C đều có thể"],
        4,
        "Cả hai cách đều đúng, tùy thuộc vào cách implement"
    )
    
    quiz.ask_question(
        "Vòng lặp while có thể thay thế for loop không?",
        ["Không", "Có, nhưng phức tạp hơn", "Chỉ trong một số trường hợp", "While nhanh hơn for"],
        2,
        "While có thể làm mọi thứ for làm được, nhưng code sẽ dài hơn"
    )
    
    quiz.ask_question(
        "Cách nào tốt nhất để validate user input?",
        ["Dùng for loop", "Dùng while loop với try-except", "Không cần validate", "Dùng if-else"],
        2,
        "While loop + try-except là pattern phổ biến cho input validation"
    )
    
    quiz.ask_question(
        "while True: có nghĩa là gì?",
        ["Lặp 1 lần", "Lặp đến khi có lỗi", "Lặp vô hạn cho đến khi gặp break", "Không lặp"],
        3,
        "while True tạo vòng lặp vô hạn, cần break để thoát"
    )
    
    quiz.ask_question(
        "Khi nào nên dùng while thay vì for?",
        ["Khi lặp qua string", "Khi cần input validation", "Khi lặp qua list", "Khi tạo range"],
        2,
        "While tốt cho các tình huống không biết trước số lần lặp"
    )
    
    # Break và Continue (10 câu)
    quiz.ask_question(
        "break statement có tác dụng gì?",
        ["Dừng chương trình", "Thoát khỏi vòng lặp hiện tại", "Bỏ qua iteration hiện tại", "Tạo lỗi"],
        2,
        "break thoát hoàn toàn khỏi vòng lặp"
    )
    
    quiz.ask_question(
        "continue statement có tác dụng gì?",
        ["Thoát khỏi vòng lặp", "Bỏ qua phần còn lại của iteration hiện tại", "Dừng chương trình", "Lặp lại từ đầu"],
        2,
        "continue bỏ qua code phía dưới và chuyển đến iteration tiếp theo"
    )
    
    quiz.ask_question(
        "Trong nested loop, break thoát khỏi vòng lặp nào?",
        ["Tất cả vòng lặp", "Vòng lặp ngoài cùng", "Vòng lặp trong cùng", "Không thoát vòng lặp nào"],
        3,
        "break chỉ thoát khỏi vòng lặp chứa nó trực tiếp"
    )
    
    quiz.ask_question(
        "Đoạn code nào in ra các số chẵn từ 1 đến 10?",
        ["for i in range(1,11): if i%2==0: print(i)", "for i in range(1,11): if i%2!=0: continue; print(i)", "for i in range(2,11,2): print(i)", "Tất cả đều đúng"],
        4,
        "Cả 3 cách đều cho kết quả giống nhau"
    )
    
    quiz.ask_question(
        "else trong vòng lặp for/while chạy khi nào?",
        ["Khi có break", "Khi vòng lặp hoàn thành bình thường (không có break)", "Khi có continue", "Khi có lỗi"],
        2,
        "else chạy khi vòng lặp kết thúc tự nhiên, không qua break"
    )
    
    quiz.ask_question(
        "pass statement dùng để làm gì?",
        ["Thoát vòng lặp", "Placeholder không làm gì", "Bỏ qua iteration", "Tạo lỗi"],
        2,
        "pass là null operation, dùng khi cần placeholder"
    )
    
    quiz.ask_question(
        "Để tìm số đầu tiên lớn hơn 100 trong list, ta dùng:",
        ["for + break", "while + break", "for + continue", "A và B đều được"],
        4,
        "Cả for và while đều có thể dùng với break để tìm và dừng"
    )
    
    quiz.ask_question(
        "continue có thể dùng trong while loop không?",
        ["Không", "Có", "Chỉ trong for loop", "Chỉ trong nested loop"],
        2,
        "continue hoạt động trong cả for và while loop"
    )
    
    quiz.ask_question(
        "Trong vòng lặp đọc file, khi nào dùng continue?",
        ["Để đóng file", "Để bỏ qua dòng trống hoặc comment", "Để đọc dòng tiếp theo", "Để ghi file"],
        2,
        "continue thường dùng để bỏ qua dòng không cần xử lý"
    )
    
    quiz.ask_question(
        "break và return khác nhau như thế nào?",
        ["Không khác", "break thoát vòng lặp, return thoát hàm", "return thoát vòng lặp, break thoát hàm", "Cả hai đều thoát chương trình"],
        2,
        "break chỉ thoát vòng lặp, return thoát cả hàm"
    )
    
    # Nested Loops (10 câu)
    quiz.ask_question(
        "Nested loop là gì?",
        ["Vòng lặp trong vòng lặp", "Vòng lặp song song", "Vòng lặp ngược", "Vòng lặp có điều kiện"],
        1,
        "Nested loop là vòng lặp bên trong vòng lặp khác"
    )
    
    quiz.ask_question(
        "Để in ra bảng cửu chương, ta cần:",
        ["1 vòng lặp", "2 vòng lặp nested", "3 vòng lặp", "Không cần vòng lặp"],
        2,
        "Cần 2 vòng lặp: outer cho số thứ nhất, inner cho số thứ hai"
    )
    
    quiz.ask_question(
        "Complexity của nested loop với n phần tử là:",
        ["O(n)", "O(n²)", "O(2n)", "O(log n)"],
        2,
        "Nested loop có độ phức tạp O(n²) vì mỗi phần tử outer chạy n lần inner"
    )
    
    quiz.ask_question(
        "Để in ra pattern tam giác *, ta dùng:",
        ["1 vòng lặp với range", "2 vòng lặp nested", "While loop đơn", "List comprehension"],
        2,
        "Cần outer loop cho số dòng, inner loop cho số * mỗi dòng"
    )
    
    quiz.ask_question(
        "Trong nested loop, biến của vòng lặp ngoài có accessible trong vòng lặp trong không?",
        ["Không", "Có", "Chỉ khi khai báo global", "Chỉ trong for loop"],
        2,
        "Biến outer loop có thể truy cập trong inner loop (scope rules)"
    )
    
    quiz.ask_question(
        "Để duyệt ma trận 2D, ta cần:",
        ["1 vòng lặp", "2 vòng lặp nested", "3 vòng lặp", "Tùy thuộc kích thước"],
        2,
        "Ma trận 2D cần 2 loops: một cho hàng, một cho cột"
    )
    
    quiz.ask_question(
        "Khi nào nên tránh nested loop?",
        ["Khi data nhỏ", "Khi cần performance cao với data lớn", "Khi làm game", "Không bao giờ"],
        2,
        "Nested loop có độ phức tạp cao, cần cân nhắc với big data"
    )
    
    quiz.ask_question(
        "Để thoát khỏi cả 2 vòng lặp nested, ta có thể:",
        ["Dùng break 2 lần", "Dùng flag variable", "Dùng return trong function", "B và C đều đúng"],
        4,
        "Flag variable hoặc return trong function đều có thể thoát nested loops"
    )
    
    quiz.ask_question(
        "List comprehension có thể thay thế nested loop không?",
        ["Không", "Có, trong nhiều trường hợp", "Chỉ với 2 levels", "Chỉ với for loop"],
        2,
        "List comprehension có thể handle nhiều levels nesting một cách gọn gàng"
    )
    
    quiz.ask_question(
        "Performance của nested loop phụ thuộc vào:",
        ["Chỉ outer loop", "Chỉ inner loop", "Tích của cả hai", "Tổng của cả hai"],
        3,
        "Performance = outer_iterations × inner_iterations"
    )
    
    # Ứng dụng thực tế (10 câu)
    quiz.ask_question(
        "Để validate password với nhiều điều kiện, nên dùng:",
        ["For loop qua từng ký tự", "Multiple if statements", "While loop với flags", "Tất cả đều có thể"],
        4,
        "Tùy approach: for loop check từng char, if statements check rules, while loop retry"
    )
    
    quiz.ask_question(
        "Menu system thường dùng loại loop nào?",
        ["For loop", "While True với break", "Nested loop", "List comprehension"],
        2,
        "while True cho phép menu chạy liên tục đến khi user chọn exit"
    )
    
    quiz.ask_question(
        "Để xử lý file CSV với nhiều dòng, ta dùng:",
        ["For loop qua từng dòng", "While loop đọc đến EOF", "Nested loop cho cells", "A và C kết hợp"],
        4,
        "For loop qua dòng, có thể cần inner loop để xử lý từng cell"
    )
    
    quiz.ask_question(
        "Game loop thường có cấu trúc:",
        ["for i in range(10):", "while game_running:", "if player_win:", "def game():"],
        2,
        "Game loop cần chạy liên tục đến khi game over"
    )
    
    quiz.ask_question(
        "Để tìm kiếm trong danh sách, thuật toán nào dùng loop?",
        ["Linear search", "Binary search", "Bubble sort", "Tất cả đều dùng"],
        4,
        "Hầu hết thuật toán search và sort đều sử dụng loops"
    )
    
    quiz.ask_question(
        "Animation trong game thường dùng:",
        ["For loop với sleep()", "While loop với time control", "Nested loop cho frames", "B và C đều đúng"],
        4,
        "Animation cần time control và có thể cần nested loops cho complex movements"
    )
    
    quiz.ask_question(
        "Để crawl web pages, ta thường dùng:",
        ["For loop qua URLs", "While loop cho pagination", "Nested loop cho links", "Tất cả đều đúng"],
        4,
        "Web crawling có thể cần nhiều loại loops tùy theo structure"
    )
    
    quiz.ask_question(
        "Database queries với nhiều records thường dùng:",
        ["For loop qua results", "While loop với cursor", "Batch processing", "Tất cả đều đúng"],
        4,
        "Database operations có nhiều patterns sử dụng loops"
    )
    
    quiz.ask_question(
        "Machine learning training loop thường có:",
        ["For epochs", "For batches", "While not converged", "Tất cả đều có thể"],
        4,
        "ML training có thể dùng nhiều loại loops tùy theo algorithm"
    )
    
    quiz.ask_question(
        "Để xử lý real-time data stream, ta dùng:",
        ["For loop cố định", "While True với data check", "If-else đơn giản", "Function recursion"],
        2,
        "Real-time processing cần infinite loop để liên tục check data mới"
    )
    
    # PHẦN 2: CÂU HỎI CODING (10 câu)
    
    quiz.ask_coding_question(
        "Viết code in ra tổng các số từ 1 đến 10",
        "1+2+3+...+10",
        "55",
        "Có thể dùng for loop hoặc công thức n*(n+1)/2"
    )
    
    quiz.ask_coding_question(
        "Viết code tìm số lớn nhất trong list [3,7,2,9,1]",
        "[3,7,2,9,1]",
        "9",
        "Dùng max() hoặc loop để so sánh từng phần tử"
    )
    
    quiz.ask_coding_question(
        "Viết code đếm số chữ 'a' trong string 'banana'",
        "string: 'banana'",
        "3",
        "Dùng count() method hoặc loop qua từng ký tự"
    )
    
    quiz.ask_coding_question(
        "Viết code in ra các số chẵn từ 2 đến 20",
        "2, 4, 6, ..., 20",
        "2 4 6 8 10 12 14 16 18 20",
        "Dùng range(2, 21, 2) hoặc if i%2==0"
    )
    
    quiz.ask_coding_question(
        "Viết code tạo list bình phương của các số từ 1 đến 5",
        "[1, 2, 3, 4, 5]",
        "[1, 4, 9, 16, 25]",
        "Dùng list comprehension hoặc loop append"
    )
    
    quiz.ask_coding_question(
        "Viết code đảo ngược string 'python'",
        "string: 'python'",
        "nohtyp",
        "Dùng slicing [::-1] hoặc loop ngược"
    )
    
    quiz.ask_coding_question(
        "Viết code kiểm tra số 17 có phải số nguyên tố",
        "number: 17",
        "True (17 là số nguyên tố)",
        "Check chia hết cho các số từ 2 đến sqrt(n)"
    )
    
    quiz.ask_coding_question(
        "Viết code tìm factorial của 5 (5!)",
        "5! = 5*4*3*2*1",
        "120",
        "Dùng loop nhân dần hoặc recursion"
    )
    
    quiz.ask_coding_question(
        "Viết code tạo pattern: * ** *** (3 dòng)",
        "Triangle pattern",
        "* ** ***",
        "Dùng nested loop: outer cho dòng, inner cho số *"
    )
    
    quiz.ask_coding_question(
        "Viết code tìm chỉ số của 'world' trong 'hello world'",
        "string: 'hello world', find: 'world'",
        "6",
        "Dùng find() method hoặc loop tìm substring"
    )
    
    # Hiển thị kết quả cuối cùng
    quiz.show_final_results()

# Chạy quiz
if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n🚪 Quiz đã được dừng. Hẹn gặp lại!")
    except Exception as e:
        print(Fore.RED + f"\n❌ Có lỗi xảy ra: {e}")
        print(Fore.CYAN + "Vui lòng thử lại!") 