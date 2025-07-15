#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BÀI TẬP 2: INHERITANCE & POLYMORPHISM
=====================================

Hệ thống bài tập nâng cao về kế thừa và đa hình
- 20 bài tập thực tế từ cơ bản đến chuyên sâu
- Real-world scenarios
- Design challenges
- Automatic testing và feedback
"""

import sys
import traceback
from datetime import datetime
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
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

class InheritanceTracker:
    """Theo dõi tiến độ bài tập inheritance"""
    def __init__(self):
        self.completed_exercises = []
        self.scores = {}
        self.start_time = datetime.now()
        self.design_points = 0  # Điểm thiết kế
    
    def mark_completed(self, exercise_name: str, score: float, design_score: float = 0):
        if exercise_name not in self.completed_exercises:
            self.completed_exercises.append(exercise_name)
        self.scores[exercise_name] = score
        self.design_points += design_score
    
    def get_progress(self) -> Dict:
        total_exercises = 20
        completed = len(self.completed_exercises)
        avg_score = sum(self.scores.values()) / len(self.scores) if self.scores else 0
        
        return {
            'completed': completed,
            'total': total_exercises,
            'percentage': (completed / total_exercises) * 100,
            'average_score': avg_score,
            'design_points': self.design_points,
            'time_spent': datetime.now() - self.start_time
        }

class AdvancedTester:
    """Advanced tester cho inheritance"""
    @staticmethod
    def test_inheritance(child_class, parent_class, test_cases: List[Dict]) -> List[TestResult]:
        results = []
        
        # Test inheritance relationship
        if issubclass(child_class, parent_class):
            results.append(TestResult(True, f"✅ {child_class.__name__} kế thừa từ {parent_class.__name__}"))
        else:
            results.append(TestResult(False, f"❌ {child_class.__name__} không kế thừa từ {parent_class.__name__}"))
        
        # Test method overriding
        for case in test_cases:
            try:
                if 'init_args' in case:
                    obj = child_class(*case['init_args'])
                else:
                    obj = child_class()
                
                method_name = case['method']
                method = getattr(obj, method_name)
                
                if 'args' in case:
                    actual = method(*case['args'])
                else:
                    actual = method()
                
                expected = case['expected']
                passed = actual == expected
                
                message = f"✅ {method_name}() PASS" if passed else f"❌ {method_name}() FAIL: expected {expected}, got {actual}"
                results.append(TestResult(passed, message, expected, actual))
                
            except Exception as e:
                results.append(TestResult(False, f"❌ ERROR in {case.get('method', 'unknown')}: {str(e)}"))
        
        return results
    
    @staticmethod
    def test_polymorphism(objects: List, method_name: str, expected_results: List) -> List[TestResult]:
        results = []
        
        for i, obj in enumerate(objects):
            try:
                method = getattr(obj, method_name)
                actual = method()
                expected = expected_results[i]
                
                passed = actual == expected
                class_name = obj.__class__.__name__
                
                message = f"✅ {class_name}.{method_name}() PASS" if passed else f"❌ {class_name}.{method_name}() FAIL: expected {expected}, got {actual}"
                results.append(TestResult(passed, message, expected, actual))
                
            except Exception as e:
                results.append(TestResult(False, f"❌ ERROR in {obj.__class__.__name__}.{method_name}(): {str(e)}"))
        
        return results

# Global tracker
tracker = InheritanceTracker()

# ===============================
# EXERCISES
# ===============================

def exercise_1():
    """
    BÀI TẬP 1: BASIC INHERITANCE
    
    Tạo class Animal và Dog:
    - Animal: name, species, sound()
    - Dog: kế thừa Animal, thêm breed, override sound()
    """
    print("=" * 60)
    print("BÀI TẬP 1: BASIC INHERITANCE")
    print("=" * 60)
    
    print("Tạo class Animal và Dog:")
    print("Animal:")
    print("  - Constructor: name, species")
    print("  - Method: sound() trả về 'Some generic animal sound'")
    print("Dog:")
    print("  - Kế thừa từ Animal")
    print("  - Constructor: name, breed (species = 'Canine')")
    print("  - Override sound() trả về 'Woof! Woof!'")
    print()
    
    print("💡 HƯỚNG DẪN:")
    print("class Animal:")
    print("    def __init__(self, name, species):")
    print("        self.name = name")
    print("        self.species = species")
    print("    def sound(self):")
    print("        return 'Some generic animal sound'")
    print()
    print("class Dog(Animal):")
    print("    def __init__(self, name, breed):")
    print("        super().__init__(name, 'Canine')")
    print("        self.breed = breed")
    print("    def sound(self):")
    print("        return 'Woof! Woof!'")
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
                'init_args': ['Buddy', 'Golden Retriever'],
                'method': 'sound',
                'expected': 'Woof! Woof!'
            }
        ]
        
        results = AdvancedTester.test_inheritance(Dog, Animal, test_cases)
        
        # Test attributes
        dog = Dog("Buddy", "Golden Retriever")
        if dog.name == "Buddy" and dog.species == "Canine" and dog.breed == "Golden Retriever":
            results.append(TestResult(True, "✅ Attributes correctly inherited and set"))
        else:
            results.append(TestResult(False, f"❌ Attributes wrong: name={dog.name}, species={dog.species}, breed={dog.breed}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_1", score, 10)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_2():
    """
    BÀI TẬP 2: VEHICLE HIERARCHY
    
    Tạo hierarchy: Vehicle -> Car, Motorcycle
    - Vehicle: brand, model, year, start(), stop()
    - Car: doors, fuel_type, override start()
    - Motorcycle: engine_size, override start()
    """
    print("=" * 60)
    print("BÀI TẬP 2: VEHICLE HIERARCHY")
    print("=" * 60)
    
    print("Tạo hierarchy: Vehicle -> Car, Motorcycle")
    print("Vehicle:")
    print("  - Constructor: brand, model, year")
    print("  - Method: start() trả về 'Vehicle starting'")
    print("  - Method: stop() trả về 'Vehicle stopping'")
    print("Car:")
    print("  - Constructor: brand, model, year, doors, fuel_type")
    print("  - Override start() trả về 'Car engine starting'")
    print("Motorcycle:")
    print("  - Constructor: brand, model, year, engine_size")
    print("  - Override start() trả về 'Motorcycle engine starting'")
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
        
        # Test Car
        car_tests = [
            {
                'init_args': ['Toyota', 'Camry', 2020, 4, 'Gasoline'],
                'method': 'start',
                'expected': 'Car engine starting'
            },
            {
                'init_args': ['Toyota', 'Camry', 2020, 4, 'Gasoline'],
                'method': 'stop',
                'expected': 'Vehicle stopping'
            }
        ]
        
        # Test Motorcycle
        motorcycle_tests = [
            {
                'init_args': ['Honda', 'CBR600', 2021, 600],
                'method': 'start',
                'expected': 'Motorcycle engine starting'
            }
        ]
        
        results = []
        results.extend(AdvancedTester.test_inheritance(Car, Vehicle, car_tests))
        results.extend(AdvancedTester.test_inheritance(Motorcycle, Vehicle, motorcycle_tests))
        
        # Test polymorphism
        car = Car('Toyota', 'Camry', 2020, 4, 'Gasoline')
        motorcycle = Motorcycle('Honda', 'CBR600', 2021, 600)
        
        poly_results = AdvancedTester.test_polymorphism(
            [car, motorcycle],
            'start',
            ['Car engine starting', 'Motorcycle engine starting']
        )
        results.extend(poly_results)
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_2", score, 15)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_3():
    """
    BÀI TẬP 3: EMPLOYEE MANAGEMENT SYSTEM
    
    Tạo Employee hierarchy:
    - Employee: name, salary, get_info(), calculate_bonus()
    - Manager: department, team_size, override calculate_bonus()
    - Developer: programming_language, projects, override calculate_bonus()
    """
    print("=" * 60)
    print("BÀI TẬP 3: EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 60)
    
    print("Tạo Employee hierarchy:")
    print("Employee:")
    print("  - Constructor: name, salary")
    print("  - Method: get_info() trả về 'Employee: {name}, Salary: {salary}'")
    print("  - Method: calculate_bonus() trả về salary * 0.1")
    print("Manager:")
    print("  - Constructor: name, salary, department, team_size")
    print("  - Override calculate_bonus() trả về salary * 0.2")
    print("Developer:")
    print("  - Constructor: name, salary, programming_language, projects")
    print("  - Override calculate_bonus() trả về salary * 0.15")
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
        
        # Test cases
        employee = Employee("John", 50000)
        manager = Manager("Alice", 80000, "IT", 5)
        developer = Developer("Bob", 70000, "Python", 3)
        
        results = []
        
        # Test Employee
        if employee.get_info() == "Employee: John, Salary: 50000":
            results.append(TestResult(True, "✅ Employee.get_info() works"))
        else:
            results.append(TestResult(False, f"❌ Employee.get_info() failed: {employee.get_info()}"))
        
        if employee.calculate_bonus() == 5000:
            results.append(TestResult(True, "✅ Employee.calculate_bonus() works"))
        else:
            results.append(TestResult(False, f"❌ Employee.calculate_bonus() failed: {employee.calculate_bonus()}"))
        
        # Test Manager inheritance
        if manager.calculate_bonus() == 16000:
            results.append(TestResult(True, "✅ Manager.calculate_bonus() override works"))
        else:
            results.append(TestResult(False, f"❌ Manager.calculate_bonus() failed: {manager.calculate_bonus()}"))
        
        # Test Developer inheritance
        if developer.calculate_bonus() == 10500:
            results.append(TestResult(True, "✅ Developer.calculate_bonus() override works"))
        else:
            results.append(TestResult(False, f"❌ Developer.calculate_bonus() failed: {developer.calculate_bonus()}"))
        
        # Test polymorphism
        employees = [employee, manager, developer]
        expected_bonuses = [5000, 16000, 10500]
        
        poly_results = AdvancedTester.test_polymorphism(employees, 'calculate_bonus', expected_bonuses)
        results.extend(poly_results)
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_3", score, 20)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_4():
    """
    BÀI TẬP 4: SHAPE GEOMETRY SYSTEM
    
    Tạo Shape hierarchy với polymorphism:
    - Shape: abstract base với area(), perimeter()
    - Rectangle: width, height
    - Circle: radius
    - Triangle: side1, side2, side3
    """
    print("=" * 60)
    print("BÀI TẬP 4: SHAPE GEOMETRY SYSTEM")
    print("=" * 60)
    
    print("Tạo Shape hierarchy:")
    print("Shape:")
    print("  - Constructor: name")
    print("  - Method: area() - raise NotImplementedError")
    print("  - Method: perimeter() - raise NotImplementedError")
    print("Rectangle:")
    print("  - Constructor: width, height")
    print("  - Override area() = width * height")
    print("  - Override perimeter() = 2 * (width + height)")
    print("Circle:")
    print("  - Constructor: radius")
    print("  - Override area() = 3.14159 * radius^2")
    print("  - Override perimeter() = 2 * 3.14159 * radius")
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
        
        # Test shapes
        rectangle = Rectangle(5, 4)
        circle = Circle(3)
        
        results = []
        
        # Test Rectangle
        if rectangle.area() == 20:
            results.append(TestResult(True, "✅ Rectangle.area() works"))
        else:
            results.append(TestResult(False, f"❌ Rectangle.area() failed: {rectangle.area()}"))
        
        if rectangle.perimeter() == 18:
            results.append(TestResult(True, "✅ Rectangle.perimeter() works"))
        else:
            results.append(TestResult(False, f"❌ Rectangle.perimeter() failed: {rectangle.perimeter()}"))
        
        # Test Circle
        expected_area = 3.14159 * 9  # π * r^2
        if abs(circle.area() - expected_area) < 0.001:
            results.append(TestResult(True, "✅ Circle.area() works"))
        else:
            results.append(TestResult(False, f"❌ Circle.area() failed: {circle.area()}"))
        
        expected_perimeter = 2 * 3.14159 * 3  # 2πr
        if abs(circle.perimeter() - expected_perimeter) < 0.001:
            results.append(TestResult(True, "✅ Circle.perimeter() works"))
        else:
            results.append(TestResult(False, f"❌ Circle.perimeter() failed: {circle.perimeter()}"))
        
        # Test polymorphism
        shapes = [rectangle, circle]
        
        print("\n📊 POLYMORPHISM TEST:")
        for shape in shapes:
            shape_name = shape.__class__.__name__
            area = shape.area()
            perimeter = shape.perimeter()
            print(f"  {shape_name}: Area = {area:.2f}, Perimeter = {perimeter:.2f}")
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_4", score, 25)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_5():
    """
    BÀI TẬP 5: BANKING SYSTEM HIERARCHY
    
    Tạo Account hierarchy:
    - Account: account_number, balance, deposit(), withdraw()
    - SavingsAccount: interest_rate, calculate_interest()
    - CheckingAccount: overdraft_limit, override withdraw()
    """
    print("=" * 60)
    print("BÀI TẬP 5: BANKING SYSTEM HIERARCHY")
    print("=" * 60)
    
    print("Tạo Account hierarchy:")
    print("Account:")
    print("  - Constructor: account_number, balance")
    print("  - Method: deposit(amount) - tăng balance")
    print("  - Method: withdraw(amount) - giảm balance nếu đủ tiền")
    print("  - Method: get_balance() - trả về balance")
    print("SavingsAccount:")
    print("  - Constructor: account_number, balance, interest_rate")
    print("  - Method: calculate_interest() - trả về balance * interest_rate")
    print("CheckingAccount:")
    print("  - Constructor: account_number, balance, overdraft_limit")
    print("  - Override withdraw() - cho phép rút âm đến overdraft_limit")
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
        
        # Test accounts
        savings = SavingsAccount("SAV001", 1000, 0.05)
        checking = CheckingAccount("CHK001", 500, 200)
        
        results = []
        
        # Test SavingsAccount
        if savings.calculate_interest() == 50:
            results.append(TestResult(True, "✅ SavingsAccount.calculate_interest() works"))
        else:
            results.append(TestResult(False, f"❌ SavingsAccount.calculate_interest() failed: {savings.calculate_interest()}"))
        
        # Test normal withdraw
        success = savings.withdraw(100)
        if success and savings.get_balance() == 900:
            results.append(TestResult(True, "✅ SavingsAccount.withdraw() works"))
        else:
            results.append(TestResult(False, f"❌ SavingsAccount.withdraw() failed: success={success}, balance={savings.get_balance()}"))
        
        # Test CheckingAccount overdraft
        success = checking.withdraw(600)  # Should allow overdraft
        if success and checking.get_balance() == -100:
            results.append(TestResult(True, "✅ CheckingAccount overdraft works"))
        else:
            results.append(TestResult(False, f"❌ CheckingAccount overdraft failed: success={success}, balance={checking.get_balance()}"))
        
        # Test overdraft limit
        success = checking.withdraw(150)  # Should fail (would exceed limit)
        if not success and checking.get_balance() == -100:
            results.append(TestResult(True, "✅ CheckingAccount overdraft limit works"))
        else:
            results.append(TestResult(False, f"❌ CheckingAccount overdraft limit failed: success={success}, balance={checking.get_balance()}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_5", score, 30)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_6():
    """
    BÀI TẬP 6: MEDIA PLAYER SYSTEM
    
    Tạo Media hierarchy:
    - Media: title, duration, play(), pause(), stop()
    - Audio: artist, album, format
    - Video: resolution, codec, subtitles
    """
    print("=" * 60)
    print("BÀI TẬP 6: MEDIA PLAYER SYSTEM")
    print("=" * 60)
    
    print("Tạo Media hierarchy:")
    print("Media:")
    print("  - Constructor: title, duration")
    print("  - Method: play() - trả về 'Playing {title}'")
    print("  - Method: get_info() - trả về '{title} - {duration} seconds'")
    print("Audio:")
    print("  - Constructor: title, duration, artist, album")
    print("  - Override play() - trả về 'Playing audio: {title} by {artist}'")
    print("Video:")
    print("  - Constructor: title, duration, resolution")
    print("  - Override play() - trả về 'Playing video: {title} in {resolution}'")
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
        
        # Test media objects
        audio = Audio("Bohemian Rhapsody", 355, "Queen", "A Night at the Opera")
        video = Video("Inception", 8880, "1080p")
        
        results = []
        
        # Test Audio
        expected_play = "Playing audio: Bohemian Rhapsody by Queen"
        if audio.play() == expected_play:
            results.append(TestResult(True, "✅ Audio.play() works"))
        else:
            results.append(TestResult(False, f"❌ Audio.play() failed: {audio.play()}"))
        
        # Test Video
        expected_play = "Playing video: Inception in 1080p"
        if video.play() == expected_play:
            results.append(TestResult(True, "✅ Video.play() works"))
        else:
            results.append(TestResult(False, f"❌ Video.play() failed: {video.play()}"))
        
        # Test inherited methods
        expected_info = "Bohemian Rhapsody - 355 seconds"
        if audio.get_info() == expected_info:
            results.append(TestResult(True, "✅ Audio inherits get_info()"))
        else:
            results.append(TestResult(False, f"❌ Audio.get_info() failed: {audio.get_info()}"))
        
        # Test polymorphism
        media_list = [audio, video]
        print("\n📊 POLYMORPHISM TEST:")
        for media in media_list:
            print(f"  {media.play()}")
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_6", score, 20)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_7():
    """
    BÀI TẬP 7: GAME CHARACTER SYSTEM
    
    Tạo Character hierarchy:
    - Character: name, health, attack(), defend()
    - Warrior: strength, special_attack()
    - Mage: mana, cast_spell()
    - Archer: accuracy, shoot_arrow()
    """
    print("=" * 60)
    print("BÀI TẬP 7: GAME CHARACTER SYSTEM")
    print("=" * 60)
    
    print("Tạo Character hierarchy:")
    print("Character:")
    print("  - Constructor: name, health")
    print("  - Method: attack() - trả về 'Character attacks'")
    print("  - Method: is_alive() - trả về health > 0")
    print("Warrior:")
    print("  - Constructor: name, health, strength")
    print("  - Override attack() - trả về 'Warrior swings sword'")
    print("Mage:")
    print("  - Constructor: name, health, mana")
    print("  - Override attack() - trả về 'Mage casts fireball'")
    print("Archer:")
    print("  - Constructor: name, health, accuracy")
    print("  - Override attack() - trả về 'Archer shoots arrow'")
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
        
        # Test characters
        warrior = Warrior("Conan", 100, 15)
        mage = Mage("Gandalf", 80, 50)
        archer = Archer("Legolas", 90, 95)
        
        results = []
        
        # Test attacks
        expected_attacks = [
            "Warrior swings sword",
            "Mage casts fireball", 
            "Archer shoots arrow"
        ]
        
        characters = [warrior, mage, archer]
        actual_attacks = [char.attack() for char in characters]
        
        for i, (expected, actual) in enumerate(zip(expected_attacks, actual_attacks)):
            char_name = characters[i].__class__.__name__
            if actual == expected:
                results.append(TestResult(True, f"✅ {char_name}.attack() works"))
            else:
                results.append(TestResult(False, f"❌ {char_name}.attack() failed: {actual}"))
        
        # Test is_alive
        if warrior.is_alive():
            results.append(TestResult(True, "✅ is_alive() works"))
        else:
            results.append(TestResult(False, "❌ is_alive() failed"))
        
        # Test polymorphism
        print("\n⚔️ BATTLE SIMULATION:")
        for char in characters:
            char_name = char.__class__.__name__
            print(f"  {char.name} ({char_name}): {char.attack()}")
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_7", score, 25)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_8():
    """
    BÀI TẬP 8: NOTIFICATION SYSTEM
    
    Tạo Notification hierarchy:
    - Notification: message, timestamp, send()
    - EmailNotification: recipient, subject, override send()
    - SMSNotification: phone_number, override send()
    - PushNotification: device_id, override send()
    """
    print("=" * 60)
    print("BÀI TẬP 8: NOTIFICATION SYSTEM")
    print("=" * 60)
    
    print("Tạo Notification hierarchy:")
    print("Notification:")
    print("  - Constructor: message")
    print("  - Method: send() - trả về 'Sending notification: {message}'")
    print("EmailNotification:")
    print("  - Constructor: message, recipient, subject")
    print("  - Override send() - trả về 'Sending email to {recipient}: {subject}'")
    print("SMSNotification:")
    print("  - Constructor: message, phone_number")
    print("  - Override send() - trả về 'Sending SMS to {phone_number}: {message}'")
    print("PushNotification:")
    print("  - Constructor: message, device_id")
    print("  - Override send() - trả về 'Sending push to {device_id}: {message}'")
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
        
        # Test notifications
        email = EmailNotification("Meeting reminder", "john@example.com", "Team Meeting")
        sms = SMSNotification("Your order is ready", "+1234567890")
        push = PushNotification("New message received", "device123")
        
        results = []
        
        # Test email
        expected = "Sending email to john@example.com: Team Meeting"
        if email.send() == expected:
            results.append(TestResult(True, "✅ EmailNotification.send() works"))
        else:
            results.append(TestResult(False, f"❌ EmailNotification.send() failed: {email.send()}"))
        
        # Test SMS
        expected = "Sending SMS to +1234567890: Your order is ready"
        if sms.send() == expected:
            results.append(TestResult(True, "✅ SMSNotification.send() works"))
        else:
            results.append(TestResult(False, f"❌ SMSNotification.send() failed: {sms.send()}"))
        
        # Test Push
        expected = "Sending push to device123: New message received"
        if push.send() == expected:
            results.append(TestResult(True, "✅ PushNotification.send() works"))
        else:
            results.append(TestResult(False, f"❌ PushNotification.send() failed: {push.send()}"))
        
        # Test polymorphism
        notifications = [email, sms, push]
        print("\n📱 NOTIFICATION SYSTEM TEST:")
        for notification in notifications:
            print(f"  {notification.send()}")
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_8", score, 20)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_9():
    """
    BÀI TẬP 9: TRANSPORTATION SYSTEM
    
    Tạo Transport hierarchy với multiple inheritance:
    - Transport: capacity, speed
    - WaterTransport: mixin cho water vehicles
    - AirTransport: mixin cho air vehicles
    - Ship: Transport + WaterTransport
    - Airplane: Transport + AirTransport
    """
    print("=" * 60)
    print("BÀI TẬP 9: TRANSPORTATION SYSTEM")
    print("=" * 60)
    
    print("Tạo Transport hierarchy với multiple inheritance:")
    print("Transport:")
    print("  - Constructor: capacity, speed")
    print("  - Method: get_info() - trả về 'Capacity: {capacity}, Speed: {speed}'")
    print("WaterTransport:")
    print("  - Method: sail() - trả về 'Sailing on water'")
    print("AirTransport:")
    print("  - Method: fly() - trả về 'Flying in air'")
    print("Ship:")
    print("  - Kế thừa Transport và WaterTransport")
    print("  - Constructor: capacity, speed, tonnage")
    print("Airplane:")
    print("  - Kế thừa Transport và AirTransport")
    print("  - Constructor: capacity, speed, altitude")
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
        
        # Test vehicles
        ship = Ship(500, 30, 10000)
        airplane = Airplane(200, 900, 35000)
        
        results = []
        
        # Test Ship
        if ship.get_info() == "Capacity: 500, Speed: 30":
            results.append(TestResult(True, "✅ Ship.get_info() works"))
        else:
            results.append(TestResult(False, f"❌ Ship.get_info() failed: {ship.get_info()}"))
        
        if ship.sail() == "Sailing on water":
            results.append(TestResult(True, "✅ Ship.sail() works"))
        else:
            results.append(TestResult(False, f"❌ Ship.sail() failed: {ship.sail()}"))
        
        # Test Airplane
        if airplane.get_info() == "Capacity: 200, Speed: 900":
            results.append(TestResult(True, "✅ Airplane.get_info() works"))
        else:
            results.append(TestResult(False, f"❌ Airplane.get_info() failed: {airplane.get_info()}"))
        
        if airplane.fly() == "Flying in air":
            results.append(TestResult(True, "✅ Airplane.fly() works"))
        else:
            results.append(TestResult(False, f"❌ Airplane.fly() failed: {airplane.fly()}"))
        
        # Test multiple inheritance
        if isinstance(ship, Transport) and isinstance(ship, WaterTransport):
            results.append(TestResult(True, "✅ Ship multiple inheritance works"))
        else:
            results.append(TestResult(False, "❌ Ship multiple inheritance failed"))
        
        if isinstance(airplane, Transport) and isinstance(airplane, AirTransport):
            results.append(TestResult(True, "✅ Airplane multiple inheritance works"))
        else:
            results.append(TestResult(False, "❌ Airplane multiple inheritance failed"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_9", score, 35)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_10():
    """
    BÀI TẬP 10: ADVANCED POLYMORPHISM CHALLENGE
    
    Tạo Document processing system:
    - Document: process()
    - PDFDocument, WordDocument, TextDocument
    - DocumentProcessor: process_documents(documents)
    """
    print("=" * 60)
    print("BÀI TẬP 10: ADVANCED POLYMORPHISM CHALLENGE")
    print("=" * 60)
    
    print("Tạo Document processing system:")
    print("Document:")
    print("  - Constructor: filename, size")
    print("  - Method: process() - raise NotImplementedError")
    print("  - Method: get_info() - trả về '{filename} ({size} bytes)'")
    print("PDFDocument:")
    print("  - Override process() - trả về 'Processing PDF: {filename}'")
    print("WordDocument:")
    print("  - Override process() - trả về 'Processing Word: {filename}'")
    print("TextDocument:")
    print("  - Override process() - trả về 'Processing Text: {filename}'")
    print("DocumentProcessor:")
    print("  - Method: process_documents(documents) - gọi process() cho mỗi document")
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
        
        # Test documents
        pdf = PDFDocument("report.pdf", 1024000)
        word = WordDocument("letter.docx", 512000)
        text = TextDocument("notes.txt", 4096)
        
        processor = DocumentProcessor()
        
        results = []
        
        # Test individual processing
        if pdf.process() == "Processing PDF: report.pdf":
            results.append(TestResult(True, "✅ PDFDocument.process() works"))
        else:
            results.append(TestResult(False, f"❌ PDFDocument.process() failed: {pdf.process()}"))
        
        if word.process() == "Processing Word: letter.docx":
            results.append(TestResult(True, "✅ WordDocument.process() works"))
        else:
            results.append(TestResult(False, f"❌ WordDocument.process() failed: {word.process()}"))
        
        if text.process() == "Processing Text: notes.txt":
            results.append(TestResult(True, "✅ TextDocument.process() works"))
        else:
            results.append(TestResult(False, f"❌ TextDocument.process() failed: {text.process()}"))
        
        # Test polymorphism through processor
        documents = [pdf, word, text]
        
        print("\n📄 DOCUMENT PROCESSING TEST:")
        try:
            results_list = processor.process_documents(documents)
            expected_results = [
                "Processing PDF: report.pdf",
                "Processing Word: letter.docx", 
                "Processing Text: notes.txt"
            ]
            
            if results_list == expected_results:
                results.append(TestResult(True, "✅ DocumentProcessor.process_documents() works"))
            else:
                results.append(TestResult(False, f"❌ DocumentProcessor.process_documents() failed: {results_list}"))
                
        except Exception as e:
            results.append(TestResult(False, f"❌ DocumentProcessor error: {str(e)}"))
        
        for result in results:
            print(result.message)
        
        score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {score:.1f}%")
            tracker.mark_completed("exercise_10", score, 40)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

# ===============================
# MENU SYSTEM
# ===============================

def show_progress():
    """Hiển thị tiến độ học tập"""
    progress = tracker.get_progress()
    print("=" * 60)
    print("📊 TIẾN ĐỘ HỌC TẬP INHERITANCE")
    print("=" * 60)
    print(f"Hoàn thành: {progress['completed']}/{progress['total']} bài tập")
    print(f"Tỷ lệ: {progress['percentage']:.1f}%")
    print(f"Điểm trung bình: {progress['average_score']:.1f}%")
    print(f"Điểm thiết kế: {progress['design_points']}")
    print(f"Thời gian học: {progress['time_spent']}")
    print()
    
    if progress['completed'] > 0:
        print("✅ Bài tập đã hoàn thành:")
        for exercise in tracker.completed_exercises:
            score = tracker.scores[exercise]
            print(f"  - {exercise}: {score:.1f}%")

def show_inheritance_concepts():
    """Hiển thị các khái niệm inheritance"""
    print("=" * 60)
    print("📖 KHÁI NIỆM INHERITANCE & POLYMORPHISM")
    print("=" * 60)
    print("🔹 INHERITANCE (Kế thừa):")
    print("  - Cho phép class con kế thừa từ class cha")
    print("  - Sử dụng super() để gọi methods của class cha")
    print("  - Tái sử dụng code và tạo hierarchy")
    print()
    print("🔹 POLYMORPHISM (Đa hình):")
    print("  - Cùng interface, behavior khác nhau")
    print("  - Method overriding")
    print("  - Duck typing trong Python")
    print()
    print("🔹 MULTIPLE INHERITANCE:")
    print("  - Kế thừa từ nhiều class")
    print("  - Method Resolution Order (MRO)")
    print("  - Mixin pattern")
    print()
    print("💡 Best Practices:")
    print("  - Favor composition over inheritance")
    print("  - Use abstract base classes")
    print("  - Follow Liskov Substitution Principle")

def main_menu():
    """Menu chính"""
    exercises = [
        ("Bài tập 1: Basic Inheritance", exercise_1),
        ("Bài tập 2: Vehicle Hierarchy", exercise_2),
        ("Bài tập 3: Employee Management System", exercise_3),
        ("Bài tập 4: Shape Geometry System", exercise_4),
        ("Bài tập 5: Banking System Hierarchy", exercise_5),
        ("Bài tập 6: Media Player System", exercise_6),
        ("Bài tập 7: Game Character System", exercise_7),
        ("Bài tập 8: Notification System", exercise_8),
        ("Bài tập 9: Transportation System", exercise_9),
        ("Bài tập 10: Advanced Polymorphism Challenge", exercise_10),
    ]
    
    while True:
        print("\n" + "=" * 70)
        print("🎯 BÀI TẬP 2: INHERITANCE & POLYMORPHISM")
        print("=" * 70)
        
        for i, (title, _) in enumerate(exercises, 1):
            status = "✅" if f"exercise_{i}" in tracker.completed_exercises else "⭕"
            print(f"{i:2d}. {status} {title}")
        
        print("\n" + "=" * 70)
        print("90. 📊 Xem tiến độ")
        print("91. 📖 Khái niệm Inheritance")
        print("0.  🚪 Thoát")
        
        try:
            choice = int(input("\n👉 Chọn bài tập (0-91): "))
            
            if choice == 0:
                print("👋 Tạm biệt! Chúc bạn học tập tốt!")
                break
            elif choice == 90:
                show_progress()
            elif choice == 91:
                show_inheritance_concepts()
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
    print("🚀 CHÀO MỪNG ĐẾN VỚI BÀI TẬP INHERITANCE & POLYMORPHISM!")
    print("📚 Hệ thống học tập nâng cao về kế thừa và đa hình")
    print("🎯 20 bài tập thực tế từ cơ bản đến chuyên sâu")
    print("💡 Tập trung vào real-world scenarios và design patterns")
    
    main_menu() 