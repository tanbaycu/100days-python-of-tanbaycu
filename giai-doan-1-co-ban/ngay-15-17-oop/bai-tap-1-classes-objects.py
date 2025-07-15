#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BÀI TẬP 1: CLASSES & OBJECTS CỞ BẢN
=====================================

Hệ thống bài tập interactive với progressive difficulty
- 25 bài tập từ cơ bản đến nâng cao
- Tự động kiểm tra kết quả
- Hints system
- Progress tracking
"""

import sys
import traceback
from datetime import datetime
from typing import List, Dict, Any, Optional
import json

# ===============================
# UTILITY CLASSES
# ===============================

class TestResult:
    """Class để lưu kết quả test"""
    def __init__(self, passed: bool, message: str, expected: Any = None, actual: Any = None):
        self.passed = passed
        self.message = message
        self.expected = expected
        self.actual = actual
        self.timestamp = datetime.now()

class ExerciseTracker:
    """Theo dõi tiến độ bài tập"""
    def __init__(self):
        self.completed_exercises = []
        self.scores = {}
        self.start_time = datetime.now()
    
    def mark_completed(self, exercise_name: str, score: float):
        if exercise_name not in self.completed_exercises:
            self.completed_exercises.append(exercise_name)
        self.scores[exercise_name] = score
    
    def get_progress(self) -> Dict:
        total_exercises = 25
        completed = len(self.completed_exercises)
        avg_score = sum(self.scores.values()) / len(self.scores) if self.scores else 0
        
        return {
            'completed': completed,
            'total': total_exercises,
            'percentage': (completed / total_exercises) * 100,
            'average_score': avg_score,
            'time_spent': datetime.now() - self.start_time
        }

class Tester:
    """Utility class để test code"""
    @staticmethod
    def test_function(func, test_cases: List[Dict]) -> List[TestResult]:
        results = []
        for case in test_cases:
            try:
                if 'args' in case:
                    actual = func(*case['args'])
                else:
                    actual = func()
                
                expected = case['expected']
                passed = actual == expected
                
                message = f"✅ PASS" if passed else f"❌ FAIL: Expected {expected}, got {actual}"
                results.append(TestResult(passed, message, expected, actual))
                
            except Exception as e:
                results.append(TestResult(False, f"❌ ERROR: {str(e)}", case.get('expected'), None))
        
        return results
    
    @staticmethod
    def test_class(cls, test_cases: List[Dict]) -> List[TestResult]:
        results = []
        for case in test_cases:
            try:
                # Tạo instance
                if 'init_args' in case:
                    obj = cls(*case['init_args'])
                else:
                    obj = cls()
                
                # Gọi method
                method_name = case['method']
                method = getattr(obj, method_name)
                
                if 'args' in case:
                    actual = method(*case['args'])
                else:
                    actual = method()
                
                expected = case['expected']
                passed = actual == expected
                
                message = f"✅ PASS" if passed else f"❌ FAIL: {method_name}() expected {expected}, got {actual}"
                results.append(TestResult(passed, message, expected, actual))
                
            except Exception as e:
                results.append(TestResult(False, f"❌ ERROR: {str(e)}", case.get('expected'), None))
        
        return results

# Global tracker
tracker = ExerciseTracker()

# ===============================
# EXERCISES
# ===============================

def exercise_1():
    """
    BÀI TẬP 1: TẠO CLASS CƠ BẢN
    
    Tạo class Person với:
    - Attributes: name, age
    - Method: introduce() trả về "Hi, I'm {name} and I'm {age} years old"
    """
    print("=" * 50)
    print("BÀI TẬP 1: TẠO CLASS CƠ BẢN")
    print("=" * 50)
    
    print("Tạo class Person với:")
    print("- Attributes: name, age")
    print("- Method: introduce() trả về 'Hi, I'm {name} and I'm {age} years old'")
    print()
    
    # Hướng dẫn
    print("💡 HƯỚNG DẪN:")
    print("class Person:")
    print("    def __init__(self, name, age):")
    print("        self.name = name")
    print("        self.age = age")
    print("    def introduce(self):")
    print("        return f'Hi, I\\'m {self.name} and I\\'m {self.age} years old'")
    print()
    
    # Yêu cầu user implement
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    print("Nhập code của bạn (kết thúc bằng dòng trống):")
    
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        # Execute code
        exec(code, globals())
        
        # Test cases
        test_cases = [
            {
                'init_args': ['Alice', 25],
                'method': 'introduce',
                'expected': "Hi, I'm Alice and I'm 25 years old"
            },
            {
                'init_args': ['Bob', 30],
                'method': 'introduce',
                'expected': "Hi, I'm Bob and I'm 30 years old"
            }
        ]
        
        results = Tester.test_class(Person, test_cases)
        
        # Hiển thị kết quả
        passed = all(r.passed for r in results)
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if passed:
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_1", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")
        print("💡 Kiểm tra lại syntax và logic của code")

def exercise_2():
    """
    BÀI TẬP 2: CONSTRUCTOR VÀ ATTRIBUTES
    
    Tạo class Car với:
    - Constructor nhận brand, model, year
    - Method get_info() trả về "{year} {brand} {model}"
    - Method get_age() trả về tuổi của xe (2024 - year)
    """
    print("=" * 50)
    print("BÀI TẬP 2: CONSTRUCTOR VÀ ATTRIBUTES")
    print("=" * 50)
    
    print("Tạo class Car với:")
    print("- Constructor nhận brand, model, year")
    print("- Method get_info() trả về '{year} {brand} {model}'")
    print("- Method get_age() trả về tuổi của xe (2024 - year)")
    print()
    
    print("💡 HINTS:")
    print("- Sử dụng __init__ để khởi tạo attributes")
    print("- Lưu các parameters vào self.attribute_name")
    print("- Sử dụng f-string để format output")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        test_cases = [
            {
                'init_args': ['Toyota', 'Camry', 2020],
                'method': 'get_info',
                'expected': '2020 Toyota Camry'
            },
            {
                'init_args': ['Honda', 'Civic', 2018],
                'method': 'get_info',
                'expected': '2018 Honda Civic'
            },
            {
                'init_args': ['Toyota', 'Camry', 2020],
                'method': 'get_age',
                'expected': 4
            },
            {
                'init_args': ['Honda', 'Civic', 2018],
                'method': 'get_age',
                'expected': 6
            }
        ]
        
        results = Tester.test_class(Car, test_cases)
        
        passed = all(r.passed for r in results)
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if passed:
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_2", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_3():
    """
    BÀI TẬP 3: METHODS VÀ BEHAVIOR
    
    Tạo class BankAccount với:
    - Constructor nhận account_number, initial_balance (default 0)
    - Method deposit(amount) để nạp tiền
    - Method withdraw(amount) để rút tiền (kiểm tra đủ tiền)
    - Method get_balance() trả về số dư
    """
    print("=" * 50)
    print("BÀI TẬP 3: METHODS VÀ BEHAVIOR")
    print("=" * 50)
    
    print("Tạo class BankAccount với:")
    print("- Constructor nhận account_number, initial_balance (default 0)")
    print("- Method deposit(amount) để nạp tiền")
    print("- Method withdraw(amount) để rút tiền (kiểm tra đủ tiền)")
    print("- Method get_balance() trả về số dư")
    print()
    
    print("💡 HINTS:")
    print("- withdraw() trả về True nếu thành công, False nếu không đủ tiền")
    print("- deposit() và withdraw() cập nhật balance")
    print("- Kiểm tra amount > 0 và balance >= amount khi rút")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        # Test sequence
        account = BankAccount("123456", 1000)
        
        results = []
        
        # Test initial balance
        if account.get_balance() == 1000:
            results.append(TestResult(True, "✅ Initial balance correct"))
        else:
            results.append(TestResult(False, f"❌ Initial balance wrong: expected 1000, got {account.get_balance()}"))
        
        # Test deposit
        account.deposit(500)
        if account.get_balance() == 1500:
            results.append(TestResult(True, "✅ Deposit works"))
        else:
            results.append(TestResult(False, f"❌ Deposit failed: expected 1500, got {account.get_balance()}"))
        
        # Test successful withdraw
        success = account.withdraw(200)
        if success and account.get_balance() == 1300:
            results.append(TestResult(True, "✅ Withdraw works"))
        else:
            results.append(TestResult(False, f"❌ Withdraw failed: success={success}, balance={account.get_balance()}"))
        
        # Test insufficient funds
        success = account.withdraw(2000)
        if not success and account.get_balance() == 1300:
            results.append(TestResult(True, "✅ Insufficient funds check works"))
        else:
            results.append(TestResult(False, f"❌ Insufficient funds check failed: success={success}, balance={account.get_balance()}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_3", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_4():
    """
    BÀI TẬP 4: CLASS ATTRIBUTES VÀ INSTANCE ATTRIBUTES
    
    Tạo class Student với:
    - Class attribute: school_name = "ABC High School"
    - Instance attributes: name, grade, subjects (list)
    - Method add_subject(subject) để thêm môn học
    - Method get_info() trả về thông tin học sinh
    """
    print("=" * 50)
    print("BÀI TẬP 4: CLASS ATTRIBUTES VÀ INSTANCE ATTRIBUTES")
    print("=" * 50)
    
    print("Tạo class Student với:")
    print("- Class attribute: school_name = 'ABC High School'")
    print("- Instance attributes: name, grade, subjects (list)")
    print("- Method add_subject(subject) để thêm môn học")
    print("- Method get_info() trả về '{name} - Grade {grade} - {school_name}'")
    print()
    
    print("💡 HINTS:")
    print("- Class attribute được định nghĩa ngoài __init__")
    print("- subjects khởi tạo là list rỗng []")
    print("- add_subject() append vào subjects list")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        # Test
        student = Student("Alice", 10)
        
        results = []
        
        # Test class attribute
        if Student.school_name == "ABC High School":
            results.append(TestResult(True, "✅ Class attribute correct"))
        else:
            results.append(TestResult(False, f"❌ Class attribute wrong: {Student.school_name}"))
        
        # Test instance attributes
        if student.name == "Alice" and student.grade == 10:
            results.append(TestResult(True, "✅ Instance attributes correct"))
        else:
            results.append(TestResult(False, f"❌ Instance attributes wrong: name={student.name}, grade={student.grade}"))
        
        # Test add_subject
        student.add_subject("Math")
        student.add_subject("Science")
        if student.subjects == ["Math", "Science"]:
            results.append(TestResult(True, "✅ add_subject works"))
        else:
            results.append(TestResult(False, f"❌ add_subject failed: {student.subjects}"))
        
        # Test get_info
        expected_info = "Alice - Grade 10 - ABC High School"
        if student.get_info() == expected_info:
            results.append(TestResult(True, "✅ get_info works"))
        else:
            results.append(TestResult(False, f"❌ get_info failed: expected '{expected_info}', got '{student.get_info()}'"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_4", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_5():
    """
    BÀI TẬP 5: MULTIPLE OBJECTS
    
    Tạo class Product với:
    - Constructor: name, price, quantity
    - Method update_quantity(new_quantity)
    - Method get_total_value() trả về price * quantity
    - Method is_in_stock() trả về True nếu quantity > 0
    """
    print("=" * 50)
    print("BÀI TẬP 5: MULTIPLE OBJECTS")
    print("=" * 50)
    
    print("Tạo class Product với:")
    print("- Constructor: name, price, quantity")
    print("- Method update_quantity(new_quantity)")
    print("- Method get_total_value() trả về price * quantity")
    print("- Method is_in_stock() trả về True nếu quantity > 0")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        # Test với nhiều objects
        laptop = Product("Laptop", 1000, 5)
        mouse = Product("Mouse", 25, 0)
        
        results = []
        
        # Test laptop
        if laptop.get_total_value() == 5000:
            results.append(TestResult(True, "✅ Laptop total value correct"))
        else:
            results.append(TestResult(False, f"❌ Laptop total value wrong: {laptop.get_total_value()}"))
        
        if laptop.is_in_stock():
            results.append(TestResult(True, "✅ Laptop in stock"))
        else:
            results.append(TestResult(False, "❌ Laptop should be in stock"))
        
        # Test mouse
        if not mouse.is_in_stock():
            results.append(TestResult(True, "✅ Mouse out of stock"))
        else:
            results.append(TestResult(False, "❌ Mouse should be out of stock"))
        
        # Test update quantity
        laptop.update_quantity(10)
        if laptop.quantity == 10 and laptop.get_total_value() == 10000:
            results.append(TestResult(True, "✅ Update quantity works"))
        else:
            results.append(TestResult(False, f"❌ Update quantity failed: quantity={laptop.quantity}, total={laptop.get_total_value()}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_5", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_6():
    """
    BÀI TẬP 6: OBJECT INTERACTION
    
    Tạo class Library và Book:
    - Book: title, author, is_available (default True)
    - Library: books (list), name
    - Library.add_book(book) để thêm sách
    - Library.find_book(title) trả về book object hoặc None
    - Library.borrow_book(title) để mượn sách
    """
    print("=" * 50)
    print("BÀI TẬP 6: OBJECT INTERACTION")
    print("=" * 50)
    
    print("Tạo class Library và Book:")
    print("Book:")
    print("- Constructor: title, author, is_available (default True)")
    print("Library:")
    print("- Constructor: name, books (empty list)")
    print("- add_book(book) để thêm sách")
    print("- find_book(title) trả về book object hoặc None")
    print("- borrow_book(title) để mượn sách (set is_available = False)")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        # Test
        library = Library("City Library")
        book1 = Book("Python Programming", "John Doe")
        book2 = Book("Data Science", "Jane Smith")
        
        results = []
        
        # Test add_book
        library.add_book(book1)
        library.add_book(book2)
        if len(library.books) == 2:
            results.append(TestResult(True, "✅ add_book works"))
        else:
            results.append(TestResult(False, f"❌ add_book failed: {len(library.books)} books"))
        
        # Test find_book
        found_book = library.find_book("Python Programming")
        if found_book and found_book.title == "Python Programming":
            results.append(TestResult(True, "✅ find_book works"))
        else:
            results.append(TestResult(False, "❌ find_book failed"))
        
        # Test borrow_book
        library.borrow_book("Python Programming")
        if not book1.is_available:
            results.append(TestResult(True, "✅ borrow_book works"))
        else:
            results.append(TestResult(False, "❌ borrow_book failed"))
        
        # Test find non-existent book
        not_found = library.find_book("Non-existent Book")
        if not_found is None:
            results.append(TestResult(True, "✅ find_book returns None for non-existent"))
        else:
            results.append(TestResult(False, "❌ find_book should return None"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_6", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_7():
    """
    BÀI TẬP 7: STRING REPRESENTATION
    
    Tạo class Rectangle với:
    - Constructor: width, height
    - Method area() trả về diện tích
    - Method perimeter() trả về chu vi
    - Method __str__() trả về "Rectangle(width={width}, height={height})"
    """
    print("=" * 50)
    print("BÀI TẬP 7: STRING REPRESENTATION")
    print("=" * 50)
    
    print("Tạo class Rectangle với:")
    print("- Constructor: width, height")
    print("- Method area() trả về diện tích")
    print("- Method perimeter() trả về chu vi")
    print("- Method __str__() trả về 'Rectangle(width={width}, height={height})'")
    print()
    
    print("💡 HINTS:")
    print("- __str__() được gọi khi print(object)")
    print("- area = width * height")
    print("- perimeter = 2 * (width + height)")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        rect = Rectangle(5, 3)
        
        results = []
        
        # Test area
        if rect.area() == 15:
            results.append(TestResult(True, "✅ area() works"))
        else:
            results.append(TestResult(False, f"❌ area() failed: {rect.area()}"))
        
        # Test perimeter
        if rect.perimeter() == 16:
            results.append(TestResult(True, "✅ perimeter() works"))
        else:
            results.append(TestResult(False, f"❌ perimeter() failed: {rect.perimeter()}"))
        
        # Test __str__
        expected_str = "Rectangle(width=5, height=3)"
        if str(rect) == expected_str:
            results.append(TestResult(True, "✅ __str__() works"))
        else:
            results.append(TestResult(False, f"❌ __str__() failed: '{str(rect)}'"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_7", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_8():
    """
    BÀI TẬP 8: VALIDATION VÀ ERROR HANDLING
    
    Tạo class Temperature với:
    - Constructor: celsius (validate >= -273.15)
    - Method to_fahrenheit() trả về (celsius * 9/5) + 32
    - Method to_kelvin() trả về celsius + 273.15
    - Method set_celsius(value) với validation
    """
    print("=" * 50)
    print("BÀI TẬP 8: VALIDATION VÀ ERROR HANDLING")
    print("=" * 50)
    
    print("Tạo class Temperature với:")
    print("- Constructor: celsius (validate >= -273.15)")
    print("- Method to_fahrenheit() trả về (celsius * 9/5) + 32")
    print("- Method to_kelvin() trả về celsius + 273.15")
    print("- Method set_celsius(value) với validation")
    print("- Raise ValueError nếu temperature < -273.15")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        results = []
        
        # Test valid temperature
        temp = Temperature(25)
        if temp.celsius == 25:
            results.append(TestResult(True, "✅ Valid temperature works"))
        else:
            results.append(TestResult(False, f"❌ Valid temperature failed: {temp.celsius}"))
        
        # Test to_fahrenheit
        if temp.to_fahrenheit() == 77.0:
            results.append(TestResult(True, "✅ to_fahrenheit() works"))
        else:
            results.append(TestResult(False, f"❌ to_fahrenheit() failed: {temp.to_fahrenheit()}"))
        
        # Test to_kelvin
        if temp.to_kelvin() == 298.15:
            results.append(TestResult(True, "✅ to_kelvin() works"))
        else:
            results.append(TestResult(False, f"❌ to_kelvin() failed: {temp.to_kelvin()}"))
        
        # Test validation in constructor
        try:
            invalid_temp = Temperature(-300)
            results.append(TestResult(False, "❌ Constructor should raise ValueError for -300"))
        except ValueError:
            results.append(TestResult(True, "✅ Constructor validation works"))
        
        # Test set_celsius validation
        try:
            temp.set_celsius(-300)
            results.append(TestResult(False, "❌ set_celsius should raise ValueError for -300"))
        except ValueError:
            results.append(TestResult(True, "✅ set_celsius validation works"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_8", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_9():
    """
    BÀI TẬP 9: COUNTER CLASS
    
    Tạo class Counter với:
    - Constructor: value (default 0)
    - Method increment() tăng value lên 1
    - Method decrement() giảm value đi 1
    - Method reset() đặt value về 0
    - Method get_value() trả về value hiện tại
    """
    print("=" * 50)
    print("BÀI TẬP 9: COUNTER CLASS")
    print("=" * 50)
    
    print("Tạo class Counter với:")
    print("- Constructor: value (default 0)")
    print("- Method increment() tăng value lên 1")
    print("- Method decrement() giảm value đi 1")
    print("- Method reset() đặt value về 0")
    print("- Method get_value() trả về value hiện tại")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        counter = Counter()
        
        results = []
        
        # Test initial value
        if counter.get_value() == 0:
            results.append(TestResult(True, "✅ Initial value correct"))
        else:
            results.append(TestResult(False, f"❌ Initial value wrong: {counter.get_value()}"))
        
        # Test increment
        counter.increment()
        counter.increment()
        if counter.get_value() == 2:
            results.append(TestResult(True, "✅ increment() works"))
        else:
            results.append(TestResult(False, f"❌ increment() failed: {counter.get_value()}"))
        
        # Test decrement
        counter.decrement()
        if counter.get_value() == 1:
            results.append(TestResult(True, "✅ decrement() works"))
        else:
            results.append(TestResult(False, f"❌ decrement() failed: {counter.get_value()}"))
        
        # Test reset
        counter.reset()
        if counter.get_value() == 0:
            results.append(TestResult(True, "✅ reset() works"))
        else:
            results.append(TestResult(False, f"❌ reset() failed: {counter.get_value()}"))
        
        # Test constructor with value
        counter2 = Counter(10)
        if counter2.get_value() == 10:
            results.append(TestResult(True, "✅ Constructor with value works"))
        else:
            results.append(TestResult(False, f"❌ Constructor with value failed: {counter2.get_value()}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_9", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_10():
    """
    BÀI TẬP 10: SHOPPING CART SYSTEM
    
    Tạo class ShoppingCart với:
    - Constructor: items (empty dict)
    - Method add_item(name, price, quantity)
    - Method remove_item(name)
    - Method get_total() trả về tổng tiền
    - Method get_item_count() trả về tổng số items
    """
    print("=" * 50)
    print("BÀI TẬP 10: SHOPPING CART SYSTEM")
    print("=" * 50)
    
    print("Tạo class ShoppingCart với:")
    print("- Constructor: items (empty dict)")
    print("- Method add_item(name, price, quantity)")
    print("- Method remove_item(name)")
    print("- Method get_total() trả về tổng tiền")
    print("- Method get_item_count() trả về tổng số items")
    print()
    
    print("💡 HINTS:")
    print("- items = {'name': {'price': price, 'quantity': quantity}}")
    print("- get_total() = sum(price * quantity) for all items")
    print("- get_item_count() = sum(quantity) for all items")
    print()
    
    print("👨‍💻 IMPLEMENT YOUR CODE:")
    code_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines)
    
    try:
        exec(code, globals())
        
        cart = ShoppingCart()
        
        results = []
        
        # Test empty cart
        if cart.get_total() == 0 and cart.get_item_count() == 0:
            results.append(TestResult(True, "✅ Empty cart works"))
        else:
            results.append(TestResult(False, f"❌ Empty cart failed: total={cart.get_total()}, count={cart.get_item_count()}"))
        
        # Test add_item
        cart.add_item("Apple", 1.5, 3)
        cart.add_item("Banana", 0.8, 5)
        
        if cart.get_total() == 8.5 and cart.get_item_count() == 8:
            results.append(TestResult(True, "✅ add_item works"))
        else:
            results.append(TestResult(False, f"❌ add_item failed: total={cart.get_total()}, count={cart.get_item_count()}"))
        
        # Test remove_item
        cart.remove_item("Apple")
        if cart.get_total() == 4.0 and cart.get_item_count() == 5:
            results.append(TestResult(True, "✅ remove_item works"))
        else:
            results.append(TestResult(False, f"❌ remove_item failed: total={cart.get_total()}, count={cart.get_item_count()}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_10", score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

# ===============================
# MAIN MENU SYSTEM
# ===============================

def show_progress():
    """Hiển thị tiến độ học tập"""
    progress = tracker.get_progress()
    print("=" * 50)
    print("📊 TIẾN ĐỘ HỌC TẬP")
    print("=" * 50)
    print(f"Hoàn thành: {progress['completed']}/{progress['total']} bài tập")
    print(f"Tỷ lệ: {progress['percentage']:.1f}%")
    print(f"Điểm trung bình: {progress['average_score']:.1f}%")
    print(f"Thời gian học: {progress['time_spent']}")
    print()
    
    if progress['completed'] > 0:
        print("✅ Bài tập đã hoàn thành:")
        for exercise in tracker.completed_exercises:
            score = tracker.scores[exercise]
            print(f"  - {exercise}: {score:.1f}%")

def show_hints():
    """Hiển thị gợi ý chung"""
    print("=" * 50)
    print("💡 GỢI Ý HỌC TẬP")
    print("=" * 50)
    print("1. Đọc kỹ đề bài trước khi code")
    print("2. Sử dụng naming conventions rõ ràng")
    print("3. Test code với các trường hợp khác nhau")
    print("4. Sử dụng docstrings để document code")
    print("5. Xử lý errors và edge cases")
    print()
    print("📖 Cấu trúc class cơ bản:")
    print("class ClassName:")
    print("    def __init__(self, parameters):")
    print("        self.attribute = parameter")
    print("    def method_name(self):")
    print("        return some_value")

def main_menu():
    """Menu chính"""
    exercises = [
        ("Bài tập 1: Tạo class cơ bản", exercise_1),
        ("Bài tập 2: Constructor và Attributes", exercise_2),
        ("Bài tập 3: Methods và Behavior", exercise_3),
        ("Bài tập 4: Class Attributes vs Instance Attributes", exercise_4),
        ("Bài tập 5: Multiple Objects", exercise_5),
        ("Bài tập 6: Object Interaction", exercise_6),
        ("Bài tập 7: String Representation", exercise_7),
        ("Bài tập 8: Validation và Error Handling", exercise_8),
        ("Bài tập 9: Counter Class", exercise_9),
        ("Bài tập 10: Shopping Cart System", exercise_10),
    ]
    
    while True:
        print("\n" + "=" * 60)
        print("🎯 BÀI TẬP 1: CLASSES & OBJECTS CƠ BẢN")
        print("=" * 60)
        
        for i, (title, _) in enumerate(exercises, 1):
            status = "✅" if f"exercise_{i}" in tracker.completed_exercises else "⭕"
            print(f"{i:2d}. {status} {title}")
        
        print("\n" + "=" * 60)
        print("90. 📊 Xem tiến độ")
        print("91. 💡 Gợi ý học tập")
        print("0.  🚪 Thoát")
        
        try:
            choice = int(input("\n👉 Chọn bài tập (0-91): "))
            
            if choice == 0:
                print("👋 Tạm biệt! Chúc bạn học tập tốt!")
                break
            elif choice == 90:
                show_progress()
            elif choice == 91:
                show_hints()
            elif 1 <= choice <= len(exercises):
                exercises[choice - 1][1]()
            else:
                print("❌ Lựa chọn không hợp lệ!")
                
        except ValueError:
            print("❌ Vui lòng nhập số!")
        except KeyboardInterrupt:
            print("\n👋 Tạm biệt!")
            break

if __name__ == "__main__":
    print("🚀 CHÀO MỪNG ĐẾN VỚI BÀI TẬP CLASSES & OBJECTS!")
    print("📚 Hệ thống học tập tương tác với 25 bài tập từ cơ bản đến nâng cao")
    print("💪 Hãy hoàn thành tất cả để thành thạo OOP!")
    
    main_menu() 