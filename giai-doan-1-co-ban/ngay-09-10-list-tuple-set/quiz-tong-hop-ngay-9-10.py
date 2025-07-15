#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUIZ TỔNG HỢP: LISTS, TUPLES, SETS - NGÀY 9-10
Kiểm tra kiến thức toàn diện về Lists, Tuples, Sets

Mục tiêu:
- Đánh giá hiểu biết về cấu trúc dữ liệu
- Kiểm tra kỹ năng thực hành
- Phân loại trình độ học viên
- Gợi ý hướng học tiếp theo

Tác giả: Python Learning Journey
Cấp độ: All Levels
"""

import random
import time
import json
from datetime import datetime
from collections import Counter

# Cài đặt màu sắc cho giao diện
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    # Fallback nếu không có colorama
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Back:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = BLACK = RESET = ""
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ""

class QuizSystem:
    """Hệ thống quiz tương tác với giao diện đẹp"""
    
    def __init__(self):
        self.questions = self._load_questions()
        self.user_answers = []
        self.correct_answers = 0
        self.start_time = None
        self.end_time = None
        self.difficulty_levels = ['easy', 'medium', 'hard', 'expert']
        
    def _load_questions(self):
        """Tải ngân hàng câu hỏi"""
        return {
            'easy': [
                {
                    'question': 'Cách nào sau đây tạo một list rỗng?',
                    'options': ['A) list = []', 'B) list = {}', 'C) list = ()', 'D) list = set()'],
                    'correct': 'A',
                    'explanation': 'Dấu ngoặc vuông [] được sử dụng để tạo list rỗng.'
                },
                {
                    'question': 'Tuple khác list ở điểm nào?',
                    'options': ['A) Tuple có thể thay đổi', 'B) Tuple không thể thay đổi', 'C) Tuple nhanh hơn', 'D) Cả B và C'],
                    'correct': 'D',
                    'explanation': 'Tuple là immutable (không thể thay đổi) và thường nhanh hơn list trong việc truy cập.'
                },
                {
                    'question': 'Set không chứa được phần tử nào?',
                    'options': ['A) Số nguyên', 'B) Chuỗi', 'C) List', 'D) Boolean'],
                    'correct': 'C',
                    'explanation': 'Set chỉ chứa các phần tử hashable. List là mutable nên không hashable.'
                },
                {
                    'question': 'Kết quả của [1, 2, 3] + [4, 5] là gì?',
                    'options': ['A) [1, 2, 3, 4, 5]', 'B) [5, 7, 3]', 'C) Error', 'D) [1, 2, 3] [4, 5]'],
                    'correct': 'A',
                    'explanation': 'Toán tử + nối hai list lại với nhau.'
                },
                {
                    'question': 'Cách truy cập phần tử cuối cùng của list my_list?',
                    'options': ['A) my_list[len(my_list)]', 'B) my_list[-1]', 'C) my_list[last]', 'D) my_list.last()'],
                    'correct': 'B',
                    'explanation': 'Index -1 luôn trỏ đến phần tử cuối cùng.'
                }
            ],
            'medium': [
                {
                    'question': 'Kết quả của {1, 2, 3} & {2, 3, 4} là gì?',
                    'options': ['A) {1, 2, 3, 4}', 'B) {2, 3}', 'C) {1, 4}', 'D) {1}'],
                    'correct': 'B',
                    'explanation': 'Toán tử & là phép giao (intersection), trả về phần tử chung.'
                },
                {
                    'question': 'List comprehension [x**2 for x in range(3)] tạo ra gì?',
                    'options': ['A) [0, 1, 4]', 'B) [1, 4, 9]', 'C) [0, 1, 2]', 'D) [1, 2, 3]'],
                    'correct': 'A',
                    'explanation': 'range(3) tạo [0,1,2], bình phương lên thành [0,1,4].'
                },
                {
                    'question': 'Phương thức nào xóa và trả về phần tử cuối list?',
                    'options': ['A) remove()', 'B) delete()', 'C) pop()', 'D) clear()'],
                    'correct': 'C',
                    'explanation': 'pop() xóa và trả về phần tử (mặc định là cuối list).'
                },
                {
                    'question': 'Cách unpacking tuple (a, b, c) = (1, 2, 3, 4) sẽ?',
                    'options': ['A) a=1, b=2, c=3', 'B) Lỗi ValueError', 'C) a=1, b=2, c=[3,4]', 'D) a=[1,2], b=3, c=4'],
                    'correct': 'B',
                    'explanation': 'Số biến phải bằng số phần tử trong tuple, nếu không sẽ lỗi ValueError.'
                },
                {
                    'question': 'my_list.extend([4, 5]) khác my_list.append([4, 5]) như thế nào?',
                    'options': ['A) Không khác', 'B) extend() thêm từng phần tử, append() thêm cả list', 'C) extend() nhanh hơn', 'D) append() an toàn hơn'],
                    'correct': 'B',
                    'explanation': 'extend() thêm từng phần tử của iterable, append() thêm cả object như một phần tử.'
                }
            ],
            'hard': [
                {
                    'question': 'Performance tốt nhất để kiểm tra membership (x in collection)?',
                    'options': ['A) List', 'B) Tuple', 'C) Set', 'D) Dictionary'],
                    'correct': 'C',
                    'explanation': 'Set có O(1) average case cho membership test, trong khi list/tuple là O(n).'
                },
                {
                    'question': 'Kết quả của list(zip([1,2], [3,4,5]))?',
                    'options': ['A) [(1,3), (2,4), (5,)]', 'B) [(1,3), (2,4)]', 'C) [1,2,3,4,5]', 'D) Error'],
                    'correct': 'B',
                    'explanation': 'zip() dừng ở iterable ngắn nhất. Phần tử thứ 3 của list thứ 2 bị bỏ qua.'
                },
                {
                    'question': 'List comprehension có điều kiện: [x for x in range(10) if x%2==0 if x>2]',
                    'options': ['A) [0, 2, 4, 6, 8]', 'B) [4, 6, 8]', 'C) [2, 4, 6, 8]', 'D) [0, 4, 6, 8]'],
                    'correct': 'B',
                    'explanation': 'Hai điều kiện if được AND lại: x phải chẵn VÀ lớn hơn 2.'
                },
                {
                    'question': 'Shallow copy vs Deep copy với nested list?',
                    'options': ['A) Shallow copy an toàn hơn', 'B) Deep copy chỉ copy tham chiếu', 'C) Shallow copy không copy nested objects', 'D) Không có sự khác biệt'],
                    'correct': 'C',
                    'explanation': 'Shallow copy chỉ copy tham chiếu đến nested objects, thay đổi nested object ảnh hưởng cả hai.'
                },
                {
                    'question': 'Set comprehension {x**2 for x in [1,-1,2,-2]} kết quả?',
                    'options': ['A) {1, 1, 4, 4}', 'B) {1, 4}', 'C) [1, 1, 4, 4]', 'D) {-1, 1, -4, 4}'],
                    'correct': 'B',
                    'explanation': 'Set tự động loại bỏ duplicates. 1² = (-1)² = 1, 2² = (-2)² = 4.'
                }
            ],
            'expert': [
                {
                    'question': 'Memory efficiency: tuple vs list với 1 triệu số nguyên?',
                    'options': ['A) Tuple ít memory hơn ~20%', 'B) List ít memory hơn', 'C) Bằng nhau', 'D) Tùy thuộc vào số'],
                    'correct': 'A',
                    'explanation': 'Tuple có overhead ít hơn list vì không cần extra space cho dynamic resizing.'
                },
                {
                    'question': 'Nested list comprehension [[j for j in range(i)] for i in range(3)]?',
                    'options': ['A) [[], [0], [0,1]]', 'B) [[0,1,2], [0,1,2], [0,1,2]]', 'C) [0, 0, 1]', 'D) Error'],
                    'correct': 'A',
                    'explanation': 'Outer loop tạo 3 list: range(0)=[], range(1)=[0], range(2)=[0,1].'
                },
                {
                    'question': 'Frozenset vs set trong dictionary key?',
                    'options': ['A) Cả hai đều được', 'B) Chỉ frozenset được', 'C) Chỉ set được', 'D) Cả hai đều không được'],
                    'correct': 'B',
                    'explanation': 'Chỉ frozenset là hashable nên có thể làm dictionary key. Set là mutable nên không hashable.'
                },
                {
                    'question': 'List slicing với step âm: [1,2,3,4,5][::-2]?',
                    'options': ['A) [5,3,1]', 'B) [1,3,5]', 'C) [5,4,3,2,1]', 'D) [2,4]'],
                    'correct': 'A',
                    'explanation': 'Step -2 đi ngược từ cuối, lấy mỗi phần tử thứ 2: index 4,2,0 → [5,3,1].'
                },
                {
                    'question': 'Generator expression vs list comprehension cho big data?',
                    'options': ['A) List comp nhanh hơn', 'B) Generator ít memory hơn', 'C) Kết quả khác nhau', 'D) A và B đều đúng'],
                    'correct': 'B',
                    'explanation': 'Generator expression lazy evaluation, chỉ tạo item khi cần, tiết kiệm memory đáng kể.'
                }
            ]
        }
    
    def print_header(self, title):
        """In header đẹp"""
        if COLORS_AVAILABLE:
            print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}")
            print("=" * 80)
            print(f"{title:^80}")
            print("=" * 80)
            print(f"{Style.RESET_ALL}")
        else:
            print(f"\n{'='*80}")
            print(f"{title:^80}")
            print("="*80)
    
    def print_question(self, question_num, total, question_data):
        """In câu hỏi với format đẹp"""
        if COLORS_AVAILABLE:
            print(f"\n{Fore.CYAN}{Style.BRIGHT}Câu {question_num}/{total}:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}{question_data['question']}{Style.RESET_ALL}")
            print()
            
            for option in question_data['options']:
                print(f"  {Fore.YELLOW}{option}{Style.RESET_ALL}")
        else:
            print(f"\nCâu {question_num}/{total}:")
            print(question_data['question'])
            print()
            for option in question_data['options']:
                print(f"  {option}")
    
    def get_user_input(self, prompt="Nhập đáp án của bạn (A/B/C/D): "):
        """Lấy input từ user với validation"""
        while True:
            if COLORS_AVAILABLE:
                answer = input(f"{Fore.GREEN}{prompt}{Style.RESET_ALL}").upper().strip()
            else:
                answer = input(prompt).upper().strip()
                
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                if COLORS_AVAILABLE:
                    print(f"{Fore.RED}❌ Vui lòng chỉ nhập A, B, C hoặc D{Style.RESET_ALL}")
                else:
                    print("❌ Vui lòng chỉ nhập A, B, C hoặc D")
    
    def show_result(self, user_answer, correct_answer, explanation):
        """Hiển thị kết quả câu hỏi"""
        if user_answer == correct_answer:
            if COLORS_AVAILABLE:
                print(f"{Fore.GREEN}{Style.BRIGHT}✅ ĐÚNG!{Style.RESET_ALL}")
            else:
                print("✅ ĐÚNG!")
            return True
        else:
            if COLORS_AVAILABLE:
                print(f"{Fore.RED}{Style.BRIGHT}❌ SAI!{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Đáp án đúng: {correct_answer}{Style.RESET_ALL}")
            else:
                print("❌ SAI!")
                print(f"Đáp án đúng: {correct_answer}")
            
        if COLORS_AVAILABLE:
            print(f"{Fore.BLUE}💡 Giải thích: {explanation}{Style.RESET_ALL}")
        else:
            print(f"💡 Giải thích: {explanation}")
        return False
    
    def calculate_level(self, score_percentage):
        """Tính level dựa trên điểm số"""
        if score_percentage >= 90:
            return "XUẤT SẮC 🏆", "Expert level - Bạn đã thành thạo Lists, Tuples, Sets!"
        elif score_percentage >= 80:
            return "GIỎI 🥇", "Advanced level - Kiến thức vững vàng, có thể học các chủ đề nâng cao!"
        elif score_percentage >= 70:
            return "KHÁ 🥈", "Intermediate level - Cần ôn luyện thêm một số khái niệm!"
        elif score_percentage >= 60:
            return "TRUNG BÌNH 🥉", "Basic level - Nắm được cơ bản, cần thực hành nhiều hơn!"
        else:
            return "CẦN CỐ GẮNG 📚", "Beginner level - Hãy ôn lại lý thuyết và làm nhiều bài tập!"
    
    def show_final_results(self):
        """Hiển thị kết quả cuối cùng"""
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        total_questions = len(self.user_answers)
        score_percentage = (self.correct_answers / total_questions) * 100 if total_questions > 0 else 0
        
        level, advice = self.calculate_level(score_percentage)
        
        self.print_header("KẾT QUẢ QUIZ")
        
        if COLORS_AVAILABLE:
            print(f"{Style.BRIGHT}")
            print(f"📊 Tổng câu hỏi: {Fore.WHITE}{total_questions}{Style.RESET_ALL}")
            print(f"✅ Trả lời đúng: {Fore.GREEN}{self.correct_answers}{Style.RESET_ALL}")
            print(f"❌ Trả lời sai: {Fore.RED}{total_questions - self.correct_answers}{Style.RESET_ALL}")
            print(f"📈 Điểm số: {Fore.YELLOW}{score_percentage:.1f}%{Style.RESET_ALL}")
            print(f"⏱️ Thời gian: {Fore.CYAN}{duration/60:.1f} phút{Style.RESET_ALL}")
            print(f"\n🎯 Trình độ: {Fore.MAGENTA}{level}{Style.RESET_ALL}")
            print(f"💭 Đánh giá: {Fore.BLUE}{advice}{Style.RESET_ALL}")
        else:
            print(f"📊 Tổng câu hỏi: {total_questions}")
            print(f"✅ Trả lời đúng: {self.correct_answers}")
            print(f"❌ Trả lời sai: {total_questions - self.correct_answers}")
            print(f"📈 Điểm số: {score_percentage:.1f}%")
            print(f"⏱️ Thời gian: {duration/60:.1f} phút")
            print(f"\n🎯 Trình độ: {level}")
            print(f"💭 Đánh giá: {advice}")
    
    def show_detailed_analysis(self):
        """Hiển thị phân tích chi tiết"""
        if not self.user_answers:
            return
            
        self.print_header("PHÂN TÍCH CHI TIẾT")
        
        # Phân tích theo độ khó
        difficulty_stats = {}
        for answer_data in self.user_answers:
            difficulty = answer_data['difficulty']
            if difficulty not in difficulty_stats:
                difficulty_stats[difficulty] = {'correct': 0, 'total': 0}
            
            difficulty_stats[difficulty]['total'] += 1
            if answer_data['is_correct']:
                difficulty_stats[difficulty]['correct'] += 1
        
        print("📈 Kết quả theo độ khó:")
        for difficulty in self.difficulty_levels:
            if difficulty in difficulty_stats:
                stats = difficulty_stats[difficulty]
                percentage = (stats['correct'] / stats['total']) * 100
                if COLORS_AVAILABLE:
                    color = Fore.GREEN if percentage >= 80 else Fore.YELLOW if percentage >= 60 else Fore.RED
                    print(f"  {difficulty.title()}: {color}{stats['correct']}/{stats['total']} ({percentage:.1f}%){Style.RESET_ALL}")
                else:
                    print(f"  {difficulty.title()}: {stats['correct']}/{stats['total']} ({percentage:.1f}%)")
        
        # Gợi ý học tập
        print(f"\n📚 GỢI Ý HỌC TẬP:")
        weak_areas = []
        for difficulty, stats in difficulty_stats.items():
            if stats['total'] > 0:
                percentage = (stats['correct'] / stats['total']) * 100
                if percentage < 70:
                    weak_areas.append(difficulty)
        
        if weak_areas:
            if COLORS_AVAILABLE:
                print(f"{Fore.YELLOW}Cần ôn luyện thêm:{Style.RESET_ALL}")
            else:
                print("Cần ôn luyện thêm:")
            
            suggestions = {
                'easy': "• Ôn lại cú pháp cơ bản của Lists, Tuples, Sets\n• Thực hành các thao tác CRUD cơ bản",
                'medium': "• Học về List Comprehensions\n• Thực hành với các methods quan trọng\n• Hiểu rõ sự khác biệt giữa các cấu trúc",
                'hard': "• Tìm hiểu về performance và memory\n• Thực hành với nested structures\n• Học về shallow vs deep copy",
                'expert': "• Nghiên cứu advanced techniques\n• Thực hành với big data\n• Tối ưu hóa performance cho production"
            }
            
            for area in weak_areas:
                if COLORS_AVAILABLE:
                    print(f"\n{Fore.CYAN}{area.title()}:{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}{suggestions.get(area, 'Thực hành thêm')}{Style.RESET_ALL}")
                else:
                    print(f"\n{area.title()}:")
                    print(suggestions.get(area, 'Thực hành thêm'))
        else:
            if COLORS_AVAILABLE:
                print(f"{Fore.GREEN}🎉 Xuất sắc! Bạn đã nắm vững tất cả các chủ đề!{Style.RESET_ALL}")
                print(f"{Fore.BLUE}Hãy tiếp tục với các chủ đề nâng cao như Functions, OOP!{Style.RESET_ALL}")
            else:
                print("🎉 Xuất sắc! Bạn đã nắm vững tất cả các chủ đề!")
                print("Hãy tiếp tục với các chủ đề nâng cao như Functions, OOP!")
    
    def save_results(self):
        """Lưu kết quả quiz"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_results_{timestamp}.json"
        
        results = {
            'timestamp': timestamp,
            'total_questions': len(self.user_answers),
            'correct_answers': self.correct_answers,
            'score_percentage': (self.correct_answers / len(self.user_answers)) * 100 if self.user_answers else 0,
            'duration_minutes': (self.end_time - self.start_time) / 60 if self.end_time and self.start_time else 0,
            'answers': self.user_answers
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            
            if COLORS_AVAILABLE:
                print(f"\n{Fore.GREEN}💾 Đã lưu kết quả vào file: {filename}{Style.RESET_ALL}")
            else:
                print(f"\n💾 Đã lưu kết quả vào file: {filename}")
        except Exception as e:
            if COLORS_AVAILABLE:
                print(f"\n{Fore.RED}❌ Lỗi khi lưu file: {e}{Style.RESET_ALL}")
            else:
                print(f"\n❌ Lỗi khi lưu file: {e}")
    
    def run_quiz(self, mode='mixed'):
        """Chạy quiz chính"""
        self.print_header("QUIZ TỔNG HỢP: LISTS, TUPLES, SETS")
        
        if COLORS_AVAILABLE:
            print(f"{Fore.CYAN}🎯 Chào mừng đến với Quiz tổng hợp về Lists, Tuples, Sets!{Style.RESET_ALL}")
            print(f"{Fore.WHITE}📝 Quiz bao gồm các câu hỏi từ cơ bản đến nâng cao{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}💡 Mỗi câu hỏi sẽ có giải thích chi tiết{Style.RESET_ALL}")
        else:
            print("🎯 Chào mừng đến với Quiz tổng hợp về Lists, Tuples, Sets!")
            print("📝 Quiz bao gồm các câu hỏi từ cơ bản đến nâng cao")
            print("💡 Mỗi câu hỏi sẽ có giải thích chi tiết")
        
        # Chọn mode
        print(f"\n📋 CHỌN CHẾ ĐỘ QUIZ:")
        print("1. 🎯 Quiz nhanh (10 câu hỏi)")
        print("2. 📚 Quiz đầy đủ (20 câu hỏi)")
        print("3. 🔥 Thử thách chuyên gia (15 câu khó)")
        print("4. 🎨 Tùy chỉnh")
        
        choice = input("\nNhập lựa chọn của bạn (1-4): ").strip()
        
        # Tạo danh sách câu hỏi theo mode
        if choice == '1':
            # Quiz nhanh: 2-3 câu mỗi level
            selected_questions = []
            for level in ['easy', 'medium', 'hard']:
                questions = random.sample(self.questions[level], min(3, len(self.questions[level])))
                for q in questions:
                    q['difficulty'] = level
                selected_questions.extend(questions)
            random.shuffle(selected_questions)
            selected_questions = selected_questions[:10]
            
        elif choice == '2':
            # Quiz đầy đủ: tất cả levels
            selected_questions = []
            for level in self.difficulty_levels:
                questions = self.questions[level][:]
                for q in questions:
                    q['difficulty'] = level
                selected_questions.extend(questions)
            random.shuffle(selected_questions)
            selected_questions = selected_questions[:20]
            
        elif choice == '3':
            # Thử thách chuyên gia: chỉ hard và expert
            selected_questions = []
            for level in ['hard', 'expert']:
                questions = self.questions[level][:]
                for q in questions:
                    q['difficulty'] = level
                selected_questions.extend(questions)
            random.shuffle(selected_questions)
            selected_questions = selected_questions[:15]
            
        else:
            # Tùy chỉnh
            print("\n🎨 TÙY CHỈNH QUIZ:")
            num_questions = int(input("Số câu hỏi (5-30): ") or "15")
            num_questions = max(5, min(30, num_questions))
            
            print("Chọn độ khó:")
            print("1. Chỉ cơ bản (Easy)")
            print("2. Cơ bản + Trung bình (Easy + Medium)")
            print("3. Tất cả levels")
            
            difficulty_choice = input("Nhập lựa chọn (1-3): ").strip()
            
            if difficulty_choice == '1':
                levels = ['easy']
            elif difficulty_choice == '2':
                levels = ['easy', 'medium']
            else:
                levels = self.difficulty_levels
            
            selected_questions = []
            for level in levels:
                questions = self.questions[level][:]
                for q in questions:
                    q['difficulty'] = level
                selected_questions.extend(questions)
            
            random.shuffle(selected_questions)
            selected_questions = selected_questions[:num_questions]
        
        # Bắt đầu quiz
        self.start_time = time.time()
        total_questions = len(selected_questions)
        
        if COLORS_AVAILABLE:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}🚀 BẮT ĐẦU QUIZ - {total_questions} CÂU HỎI{Style.RESET_ALL}")
        else:
            print(f"\n🚀 BẮT ĐẦU QUIZ - {total_questions} CÂU HỎI")
        
        # Thực hiện quiz
        for i, question_data in enumerate(selected_questions, 1):
            self.print_question(i, total_questions, question_data)
            
            user_answer = self.get_user_input()
            is_correct = self.show_result(user_answer, question_data['correct'], question_data['explanation'])
            
            if is_correct:
                self.correct_answers += 1
            
            # Lưu kết quả câu hỏi
            self.user_answers.append({
                'question': question_data['question'],
                'user_answer': user_answer,
                'correct_answer': question_data['correct'],
                'is_correct': is_correct,
                'difficulty': question_data['difficulty'],
                'explanation': question_data['explanation']
            })
            
            # Tạm dừng giữa các câu
            if i < total_questions:
                input(f"\n{Fore.BLUE if COLORS_AVAILABLE else ''}⏳ Nhấn Enter để tiếp tục...{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
        
        # Hiển thị kết quả
        self.show_final_results()
        self.show_detailed_analysis()
        
        # Lưu kết quả
        save_choice = input(f"\n💾 Bạn có muốn lưu kết quả quiz? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes', 'có']:
            self.save_results()
        
        if COLORS_AVAILABLE:
            print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🎉 CẢM ƠN BẠN ĐÃ THAM GIA QUIZ!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}📚 Hãy tiếp tục học tập và thực hành để nâng cao kỹ năng!{Style.RESET_ALL}")
        else:
            print("\n🎉 CẢM ƠN BẠN ĐÃ THAM GIA QUIZ!")
            print("📚 Hãy tiếp tục học tập và thực hành để nâng cao kỹ năng!")

def main():
    """Hàm main chạy quiz"""
    try:
        quiz = QuizSystem()
        quiz.run_quiz()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW if COLORS_AVAILABLE else ''}⚠️ Quiz đã bị dừng bởi người dùng.{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
        print(f"{Fore.BLUE if COLORS_AVAILABLE else ''}👋 Hẹn gặp lại lần sau!{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
    except Exception as e:
        print(f"\n{Fore.RED if COLORS_AVAILABLE else ''}❌ Lỗi không xác định: {e}{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
        print(f"{Fore.BLUE if COLORS_AVAILABLE else ''}🔧 Vui lòng báo cáo lỗi này để được hỗ trợ.{Style.RESET_ALL if COLORS_AVAILABLE else ''}")

if __name__ == "__main__":
    main() 