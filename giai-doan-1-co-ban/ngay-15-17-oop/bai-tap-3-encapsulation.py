#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BÀI TẬP 3: ENCAPSULATION & DATA PROTECTION
==========================================

Hệ thống bài tập chuyên sâu về đóng gói và bảo mật dữ liệu
- 15 bài tập từ cơ bản đến enterprise-level
- Security patterns và data protection
- Properties, descriptors, và access control
- Real-world security scenarios
"""

import sys
import traceback
from datetime import datetime
from typing import List, Dict, Any, Optional
import hashlib
import secrets
import json

# ===============================
# UTILITY CLASSES
# ===============================

class SecurityTestResult:
    """Class để lưu kết quả test security"""
    def __init__(self, passed: bool, message: str, security_level: str = "LOW"):
        self.passed = passed
        self.message = message
        self.security_level = security_level
        self.timestamp = datetime.now()

class EncapsulationTracker:
    """Theo dõi tiến độ bài tập encapsulation"""
    def __init__(self):
        self.completed_exercises = []
        self.scores = {}
        self.security_points = 0
        self.start_time = datetime.now()
    
    def mark_completed(self, exercise_name: str, score: float, security_points: int = 0):
        if exercise_name not in self.completed_exercises:
            self.completed_exercises.append(exercise_name)
        self.scores[exercise_name] = score
        self.security_points += security_points
    
    def get_progress(self) -> Dict:
        total_exercises = 15
        completed = len(self.completed_exercises)
        avg_score = sum(self.scores.values()) / len(self.scores) if self.scores else 0
        
        return {
            'completed': completed,
            'total': total_exercises,
            'percentage': (completed / total_exercises) * 100,
            'average_score': avg_score,
            'security_points': self.security_points,
            'time_spent': datetime.now() - self.start_time
        }

class SecurityTester:
    """Tester chuyên cho security và encapsulation"""
    
    @staticmethod
    def test_access_control(obj, private_attrs: List[str], protected_attrs: List[str]) -> List[SecurityTestResult]:
        results = []
        
        # Test private attributes
        for attr in private_attrs:
            try:
                # Try to access private attribute directly
                private_name = f"_{obj.__class__.__name__}__{attr}"
                if hasattr(obj, private_name):
                    results.append(SecurityTestResult(
                        True, 
                        f"✅ Private attribute '{attr}' is properly mangled",
                        "HIGH"
                    ))
                else:
                    results.append(SecurityTestResult(
                        False, 
                        f"❌ Private attribute '{attr}' not found",
                        "LOW"
                    ))
                    
                # Try to access without mangling (should fail)
                if hasattr(obj, attr):
                    results.append(SecurityTestResult(
                        False, 
                        f"❌ Private attribute '{attr}' is accessible directly",
                        "LOW"
                    ))
                else:
                    results.append(SecurityTestResult(
                        True, 
                        f"✅ Private attribute '{attr}' is not directly accessible",
                        "HIGH"
                    ))
                    
            except Exception as e:
                results.append(SecurityTestResult(
                    False, 
                    f"❌ Error testing private attribute '{attr}': {str(e)}",
                    "LOW"
                ))
        
        # Test protected attributes
        for attr in protected_attrs:
            if hasattr(obj, f"_{attr}"):
                results.append(SecurityTestResult(
                    True, 
                    f"✅ Protected attribute '_{attr}' exists",
                    "MEDIUM"
                ))
            else:
                results.append(SecurityTestResult(
                    False, 
                    f"❌ Protected attribute '_{attr}' not found",
                    "LOW"
                ))
        
        return results
    
    @staticmethod
    def test_property_validation(obj, property_name: str, valid_values: List, invalid_values: List) -> List[SecurityTestResult]:
        results = []
        
        # Test valid values
        for value in valid_values:
            try:
                setattr(obj, property_name, value)
                actual = getattr(obj, property_name)
                if actual == value:
                    results.append(SecurityTestResult(
                        True, 
                        f"✅ Property '{property_name}' accepts valid value: {value}",
                        "MEDIUM"
                    ))
                else:
                    results.append(SecurityTestResult(
                        False, 
                        f"❌ Property '{property_name}' failed to set valid value: {value}",
                        "LOW"
                    ))
            except Exception as e:
                results.append(SecurityTestResult(
                    False, 
                    f"❌ Error setting valid value {value}: {str(e)}",
                    "LOW"
                ))
        
        # Test invalid values
        for value in invalid_values:
            try:
                setattr(obj, property_name, value)
                results.append(SecurityTestResult(
                    False, 
                    f"❌ Property '{property_name}' should reject invalid value: {value}",
                    "LOW"
                ))
            except (ValueError, TypeError):
                results.append(SecurityTestResult(
                    True, 
                    f"✅ Property '{property_name}' correctly rejects invalid value: {value}",
                    "HIGH"
                ))
            except Exception as e:
                results.append(SecurityTestResult(
                    False, 
                    f"❌ Unexpected error with invalid value {value}: {str(e)}",
                    "LOW"
                ))
        
        return results

# Global tracker
tracker = EncapsulationTracker()

# ===============================
# EXERCISES
# ===============================

def exercise_1():
    """
    BÀI TẬP 1: BASIC ENCAPSULATION
    
    Tạo class Person với:
    - Private: __ssn (Social Security Number)
    - Protected: _age
    - Public: name
    - Methods để access private data safely
    """
    print("=" * 60)
    print("BÀI TẬP 1: BASIC ENCAPSULATION")
    print("=" * 60)
    
    print("Tạo class Person với:")
    print("- Private attribute: __ssn (Social Security Number)")
    print("- Protected attribute: _age")
    print("- Public attribute: name")
    print("- Method: get_ssn() trả về __ssn")
    print("- Method: set_age(age) với validation age >= 0")
    print("- Method: get_age() trả về _age")
    print()
    
    print("💡 HƯỚNG DẪN:")
    print("class Person:")
    print("    def __init__(self, name, age, ssn):")
    print("        self.name = name")
    print("        self._age = age")
    print("        self.__ssn = ssn")
    print("    def get_ssn(self):")
    print("        return self.__ssn")
    print("    def set_age(self, age):")
    print("        if age >= 0:")
    print("            self._age = age")
    print("        else:")
    print("            raise ValueError('Age must be non-negative')")
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
        person = Person("John Doe", 30, "123-45-6789")
        
        results = []
        
        # Test access control
        security_results = SecurityTester.test_access_control(
            person, 
            ["ssn"], 
            ["age"]
        )
        results.extend(security_results)
        
        # Test methods
        if person.get_ssn() == "123-45-6789":
            results.append(SecurityTestResult(True, "✅ get_ssn() works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ get_ssn() failed: {person.get_ssn()}", "LOW"))
        
        if person.get_age() == 30:
            results.append(SecurityTestResult(True, "✅ get_age() works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, f"❌ get_age() failed: {person.get_age()}", "LOW"))
        
        # Test validation
        try:
            person.set_age(-5)
            results.append(SecurityTestResult(False, "❌ set_age() should reject negative age", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ set_age() correctly validates age", "HIGH"))
        
        # Display results
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_1", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_2():
    """
    BÀI TẬP 2: PROPERTY DECORATORS
    
    Tạo class Temperature với:
    - Private: __celsius
    - Property: celsius với getter/setter
    - Property: fahrenheit (computed property)
    - Validation: celsius >= -273.15
    """
    print("=" * 60)
    print("BÀI TẬP 2: PROPERTY DECORATORS")
    print("=" * 60)
    
    print("Tạo class Temperature với:")
    print("- Private attribute: __celsius")
    print("- Property: celsius với getter/setter")
    print("- Property: fahrenheit (computed từ celsius)")
    print("- Validation: celsius >= -273.15 (absolute zero)")
    print("- fahrenheit = (celsius * 9/5) + 32")
    print()
    
    print("💡 HƯỚNG DẪN:")
    print("@property")
    print("def celsius(self):")
    print("    return self.__celsius")
    print("@celsius.setter")
    print("def celsius(self, value):")
    print("    if value >= -273.15:")
    print("        self.__celsius = value")
    print("    else:")
    print("        raise ValueError('Temperature below absolute zero')")
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
        temp = Temperature(25)
        
        results = []
        
        # Test property access
        if temp.celsius == 25:
            results.append(SecurityTestResult(True, "✅ celsius property getter works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, f"❌ celsius getter failed: {temp.celsius}", "LOW"))
        
        # Test computed property
        expected_fahrenheit = (25 * 9/5) + 32  # 77
        if temp.fahrenheit == expected_fahrenheit:
            results.append(SecurityTestResult(True, "✅ fahrenheit computed property works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, f"❌ fahrenheit failed: {temp.fahrenheit}", "LOW"))
        
        # Test property validation
        property_results = SecurityTester.test_property_validation(
            temp, 
            "celsius", 
            [0, 100, -100],  # Valid values
            [-300, -500]     # Invalid values
        )
        results.extend(property_results)
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(temp, ["celsius"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_2", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_3():
    """
    BÀI TẬP 3: SECURE BANK ACCOUNT
    
    Tạo class BankAccount với:
    - Private: __balance, __pin
    - Methods: deposit(), withdraw(), get_balance()
    - PIN verification cho sensitive operations
    """
    print("=" * 60)
    print("BÀI TẬP 3: SECURE BANK ACCOUNT")
    print("=" * 60)
    
    print("Tạo class BankAccount với:")
    print("- Private: __balance, __pin")
    print("- Method: deposit(amount) - không cần PIN")
    print("- Method: withdraw(amount, pin) - cần PIN verification")
    print("- Method: get_balance(pin) - cần PIN verification")
    print("- Method: change_pin(old_pin, new_pin)")
    print("- Validation: amount > 0, sufficient balance")
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
        account = BankAccount("123456", 1000, "1234")
        
        results = []
        
        # Test deposit (no PIN required)
        account.deposit(500)
        if account.get_balance("1234") == 1500:
            results.append(SecurityTestResult(True, "✅ deposit() works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, f"❌ deposit() failed", "LOW"))
        
        # Test withdraw with correct PIN
        success = account.withdraw(200, "1234")
        if success and account.get_balance("1234") == 1300:
            results.append(SecurityTestResult(True, "✅ withdraw() with correct PIN works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ withdraw() with correct PIN failed", "LOW"))
        
        # Test withdraw with wrong PIN
        success = account.withdraw(100, "wrong")
        if not success:
            results.append(SecurityTestResult(True, "✅ withdraw() rejects wrong PIN", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ withdraw() should reject wrong PIN", "LOW"))
        
        # Test get_balance with wrong PIN
        try:
            balance = account.get_balance("wrong")
            results.append(SecurityTestResult(False, "❌ get_balance() should reject wrong PIN", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ get_balance() rejects wrong PIN", "HIGH"))
        
        # Test change_pin
        success = account.change_pin("1234", "5678")
        if success:
            # Test with new PIN
            balance = account.get_balance("5678")
            if balance == 1300:
                results.append(SecurityTestResult(True, "✅ change_pin() works", "HIGH"))
            else:
                results.append(SecurityTestResult(False, f"❌ change_pin() failed", "LOW"))
        else:
            results.append(SecurityTestResult(False, f"❌ change_pin() failed", "LOW"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(account, ["balance", "pin"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_3", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_4():
    """
    BÀI TẬP 4: USER AUTHENTICATION SYSTEM
    
    Tạo class User với:
    - Private: __password_hash, __salt
    - Methods: set_password(), verify_password()
    - Password hashing với salt
    """
    print("=" * 60)
    print("BÀI TẬP 4: USER AUTHENTICATION SYSTEM")
    print("=" * 60)
    
    print("Tạo class User với:")
    print("- Private: __password_hash, __salt")
    print("- Public: username, email")
    print("- Method: set_password(password) - hash password with salt")
    print("- Method: verify_password(password) - verify against hash")
    print("- Method: __hash_password(password, salt) - private helper")
    print("- Sử dụng hashlib để hash password")
    print()
    
    print("💡 HƯỚNG DẪN:")
    print("import hashlib")
    print("import secrets")
    print("def __hash_password(self, password, salt):")
    print("    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)")
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
        user = User("john_doe", "john@example.com")
        
        results = []
        
        # Test set_password
        user.set_password("mypassword123")
        
        # Test verify_password with correct password
        if user.verify_password("mypassword123"):
            results.append(SecurityTestResult(True, "✅ verify_password() works with correct password", "HIGH"))
        else:
            results.append(SecurityTestResult(False, "❌ verify_password() failed with correct password", "LOW"))
        
        # Test verify_password with wrong password
        if not user.verify_password("wrongpassword"):
            results.append(SecurityTestResult(True, "✅ verify_password() rejects wrong password", "HIGH"))
        else:
            results.append(SecurityTestResult(False, "❌ verify_password() should reject wrong password", "LOW"))
        
        # Test that password is not stored in plain text
        if not hasattr(user, 'password') and not hasattr(user, '_password'):
            results.append(SecurityTestResult(True, "✅ Password not stored in plain text", "HIGH"))
        else:
            results.append(SecurityTestResult(False, "❌ Password should not be stored in plain text", "LOW"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(user, ["password_hash", "salt"], [])
        results.extend(security_results)
        
        # Test that salt is different for each user
        user2 = User("jane_doe", "jane@example.com")
        user2.set_password("mypassword123")
        
        # Both users have same password but different hashes (due to different salts)
        if user._User__password_hash != user2._User__password_hash:
            results.append(SecurityTestResult(True, "✅ Different salts produce different hashes", "HIGH"))
        else:
            results.append(SecurityTestResult(False, "❌ Same password should produce different hashes", "LOW"))
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_4", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_5():
    """
    BÀI TẬP 5: SECURE CONFIGURATION MANAGER
    
    Tạo class ConfigManager với:
    - Private: __config_data
    - Methods: set_config(), get_config()
    - Encryption cho sensitive data
    """
    print("=" * 60)
    print("BÀI TẬP 5: SECURE CONFIGURATION MANAGER")
    print("=" * 60)
    
    print("Tạo class ConfigManager với:")
    print("- Private: __config_data (dictionary)")
    print("- Method: set_config(key, value, sensitive=False)")
    print("- Method: get_config(key)")
    print("- Method: __encrypt_value(value) - private helper")
    print("- Method: __decrypt_value(value) - private helper")
    print("- Sensitive values được encrypt")
    print()
    
    print("💡 HƯỚNG DẪN:")
    print("- Sử dụng simple encryption: ord(char) + 1")
    print("- Lưu {'value': encrypted_value, 'sensitive': True}")
    print("- Non-sensitive values lưu trực tiếp")
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
        config = ConfigManager()
        
        results = []
        
        # Test non-sensitive config
        config.set_config("app_name", "MyApp", sensitive=False)
        if config.get_config("app_name") == "MyApp":
            results.append(SecurityTestResult(True, "✅ Non-sensitive config works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, f"❌ Non-sensitive config failed", "LOW"))
        
        # Test sensitive config
        config.set_config("api_key", "secret123", sensitive=True)
        if config.get_config("api_key") == "secret123":
            results.append(SecurityTestResult(True, "✅ Sensitive config works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Sensitive config failed", "LOW"))
        
        # Test that sensitive data is encrypted in storage
        raw_data = config._ConfigManager__config_data
        if "api_key" in raw_data:
            stored_value = raw_data["api_key"]
            if isinstance(stored_value, dict) and stored_value.get("sensitive") and stored_value.get("value") != "secret123":
                results.append(SecurityTestResult(True, "✅ Sensitive data is encrypted in storage", "HIGH"))
            else:
                results.append(SecurityTestResult(False, "❌ Sensitive data should be encrypted in storage", "LOW"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(config, ["config_data"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_5", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_6():
    """
    BÀI TẬP 6: SECURE DATABASE CONNECTION
    
    Tạo class DatabaseConnection với:
    - Private: __connection_string, __is_connected
    - Methods: connect(), disconnect(), execute_query()
    - Connection pooling và security
    """
    print("=" * 60)
    print("BÀI TẬP 6: SECURE DATABASE CONNECTION")
    print("=" * 60)
    
    print("Tạo class DatabaseConnection với:")
    print("- Private: __connection_string, __is_connected")
    print("- Method: connect() - establish connection")
    print("- Method: disconnect() - close connection")
    print("- Method: execute_query(query) - requires connection")
    print("- Method: is_connected() - check connection status")
    print("- Security: validate queries, prevent SQL injection")
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
        db = DatabaseConnection("localhost", "mydb", "user", "password")
        
        results = []
        
        # Test initial state
        if not db.is_connected():
            results.append(SecurityTestResult(True, "✅ Initial connection state is False", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, "❌ Initial connection state should be False", "LOW"))
        
        # Test connection
        db.connect()
        if db.is_connected():
            results.append(SecurityTestResult(True, "✅ connect() works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, "❌ connect() failed", "LOW"))
        
        # Test query execution when connected
        try:
            result = db.execute_query("SELECT * FROM users")
            if result:
                results.append(SecurityTestResult(True, "✅ execute_query() works when connected", "MEDIUM"))
            else:
                results.append(SecurityTestResult(False, "❌ execute_query() failed", "LOW"))
        except Exception as e:
            results.append(SecurityTestResult(False, f"❌ execute_query() error: {str(e)}", "LOW"))
        
        # Test disconnection
        db.disconnect()
        if not db.is_connected():
            results.append(SecurityTestResult(True, "✅ disconnect() works", "MEDIUM"))
        else:
            results.append(SecurityTestResult(False, "❌ disconnect() failed", "LOW"))
        
        # Test query execution when disconnected
        try:
            result = db.execute_query("SELECT * FROM users")
            results.append(SecurityTestResult(False, "❌ execute_query() should fail when disconnected", "LOW"))
        except RuntimeError:
            results.append(SecurityTestResult(True, "✅ execute_query() correctly fails when disconnected", "HIGH"))
        
        # Test SQL injection prevention
        db.connect()
        try:
            result = db.execute_query("DROP TABLE users; --")
            results.append(SecurityTestResult(False, "❌ Should prevent dangerous SQL", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ Prevents dangerous SQL queries", "HIGH"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(db, ["connection_string", "is_connected"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_6", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_7():
    """
    BÀI TẬP 7: SECURE FILE MANAGER
    
    Tạo class SecureFileManager với:
    - Private: __allowed_extensions, __base_path
    - Methods: read_file(), write_file(), delete_file()
    - Path validation và security checks
    """
    print("=" * 60)
    print("BÀI TẬP 7: SECURE FILE MANAGER")
    print("=" * 60)
    
    print("Tạo class SecureFileManager với:")
    print("- Private: __allowed_extensions, __base_path")
    print("- Method: read_file(filename) - read file content")
    print("- Method: write_file(filename, content) - write to file")
    print("- Method: delete_file(filename) - delete file")
    print("- Method: __validate_path(path) - security validation")
    print("- Security: prevent directory traversal, validate extensions")
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
        file_manager = SecureFileManager("/safe/path", [".txt", ".json"])
        
        results = []
        
        # Test valid file operations
        try:
            file_manager.write_file("test.txt", "Hello World")
            content = file_manager.read_file("test.txt")
            if content == "Hello World":
                results.append(SecurityTestResult(True, "✅ Valid file operations work", "MEDIUM"))
            else:
                results.append(SecurityTestResult(False, f"❌ File operations failed", "LOW"))
        except Exception as e:
            results.append(SecurityTestResult(False, f"❌ File operations error: {str(e)}", "LOW"))
        
        # Test invalid extension
        try:
            file_manager.write_file("malicious.exe", "virus")
            results.append(SecurityTestResult(False, "❌ Should reject invalid extensions", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ Rejects invalid extensions", "HIGH"))
        
        # Test directory traversal prevention
        try:
            file_manager.read_file("../../../etc/passwd")
            results.append(SecurityTestResult(False, "❌ Should prevent directory traversal", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ Prevents directory traversal", "HIGH"))
        
        # Test path with null bytes
        try:
            file_manager.read_file("test.txt\x00.exe")
            results.append(SecurityTestResult(False, "❌ Should reject null bytes in path", "LOW"))
        except ValueError:
            results.append(SecurityTestResult(True, "✅ Rejects null bytes in path", "HIGH"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(file_manager, ["allowed_extensions", "base_path"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_7", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_8():
    """
    BÀI TẬP 8: SECURE SESSION MANAGER
    
    Tạo class SessionManager với:
    - Private: __sessions, __session_timeout
    - Methods: create_session(), validate_session(), destroy_session()
    - Session security và timeout
    """
    print("=" * 60)
    print("BÀI TẬP 8: SECURE SESSION MANAGER")
    print("=" * 60)
    
    print("Tạo class SessionManager với:")
    print("- Private: __sessions (dict), __session_timeout")
    print("- Method: create_session(user_id) - return session_token")
    print("- Method: validate_session(token) - return user_id or None")
    print("- Method: destroy_session(token) - remove session")
    print("- Method: __generate_token() - create secure token")
    print("- Session timeout after specified seconds")
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
        session_manager = SessionManager(timeout=3600)  # 1 hour
        
        results = []
        
        # Test session creation
        token = session_manager.create_session("user123")
        if token and len(token) > 10:  # Should be a secure token
            results.append(SecurityTestResult(True, "✅ create_session() generates secure token", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ create_session() failed", "LOW"))
        
        # Test session validation
        user_id = session_manager.validate_session(token)
        if user_id == "user123":
            results.append(SecurityTestResult(True, "✅ validate_session() works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ validate_session() failed", "LOW"))
        
        # Test invalid token
        invalid_user = session_manager.validate_session("invalid_token")
        if invalid_user is None:
            results.append(SecurityTestResult(True, "✅ validate_session() rejects invalid token", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ validate_session() should reject invalid token", "LOW"))
        
        # Test session destruction
        session_manager.destroy_session(token)
        destroyed_user = session_manager.validate_session(token)
        if destroyed_user is None:
            results.append(SecurityTestResult(True, "✅ destroy_session() works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ destroy_session() failed", "LOW"))
        
        # Test unique tokens
        token1 = session_manager.create_session("user1")
        token2 = session_manager.create_session("user2")
        if token1 != token2:
            results.append(SecurityTestResult(True, "✅ Generates unique tokens", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Should generate unique tokens", "LOW"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(session_manager, ["sessions", "session_timeout"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_8", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_9():
    """
    BÀI TẬP 9: SECURE API CLIENT
    
    Tạo class SecureAPIClient với:
    - Private: __api_key, __base_url, __rate_limit
    - Methods: get(), post(), __sign_request()
    - Rate limiting và request signing
    """
    print("=" * 60)
    print("BÀI TẬP 9: SECURE API CLIENT")
    print("=" * 60)
    
    print("Tạo class SecureAPIClient với:")
    print("- Private: __api_key, __base_url, __rate_limit")
    print("- Method: get(endpoint) - make GET request")
    print("- Method: post(endpoint, data) - make POST request")
    print("- Method: __sign_request(method, endpoint, data) - sign request")
    print("- Method: __check_rate_limit() - enforce rate limiting")
    print("- Rate limiting: max requests per minute")
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
        api_client = SecureAPIClient("https://api.example.com", "secret_key_123", rate_limit=60)
        
        results = []
        
        # Test GET request
        try:
            response = api_client.get("/users")
            if response and "signed" in response:
                results.append(SecurityTestResult(True, "✅ GET request works with signing", "HIGH"))
            else:
                results.append(SecurityTestResult(False, f"❌ GET request failed", "LOW"))
        except Exception as e:
            results.append(SecurityTestResult(False, f"❌ GET request error: {str(e)}", "LOW"))
        
        # Test POST request
        try:
            response = api_client.post("/users", {"name": "John", "email": "john@example.com"})
            if response and "signed" in response:
                results.append(SecurityTestResult(True, "✅ POST request works with signing", "HIGH"))
            else:
                results.append(SecurityTestResult(False, f"❌ POST request failed", "LOW"))
        except Exception as e:
            results.append(SecurityTestResult(False, f"❌ POST request error: {str(e)}", "LOW"))
        
        # Test rate limiting
        try:
            # Make many requests quickly
            for i in range(65):  # Exceed rate limit
                api_client.get(f"/test{i}")
            results.append(SecurityTestResult(False, "❌ Should enforce rate limiting", "LOW"))
        except RuntimeError:
            results.append(SecurityTestResult(True, "✅ Enforces rate limiting", "HIGH"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(api_client, ["api_key", "base_url", "rate_limit"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_9", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

def exercise_10():
    """
    BÀI TẬP 10: ENTERPRISE SECURITY SYSTEM
    
    Tạo class SecuritySystem với:
    - Private: __users, __permissions, __audit_log
    - Methods: authenticate(), authorize(), audit()
    - Role-based access control
    """
    print("=" * 60)
    print("BÀI TẬP 10: ENTERPRISE SECURITY SYSTEM")
    print("=" * 60)
    
    print("Tạo class SecuritySystem với:")
    print("- Private: __users, __permissions, __audit_log")
    print("- Method: add_user(username, password, role)")
    print("- Method: authenticate(username, password) - return token")
    print("- Method: authorize(token, resource) - check permission")
    print("- Method: audit(action, user, resource) - log activity")
    print("- Roles: admin, user, guest với different permissions")
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
        security = SecuritySystem()
        
        results = []
        
        # Test user creation
        security.add_user("admin", "admin123", "admin")
        security.add_user("user1", "user123", "user")
        security.add_user("guest1", "guest123", "guest")
        
        # Test authentication
        admin_token = security.authenticate("admin", "admin123")
        if admin_token:
            results.append(SecurityTestResult(True, "✅ Admin authentication works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Admin authentication failed", "LOW"))
        
        user_token = security.authenticate("user1", "user123")
        if user_token:
            results.append(SecurityTestResult(True, "✅ User authentication works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ User authentication failed", "LOW"))
        
        # Test wrong password
        wrong_token = security.authenticate("admin", "wrongpassword")
        if not wrong_token:
            results.append(SecurityTestResult(True, "✅ Rejects wrong password", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Should reject wrong password", "LOW"))
        
        # Test authorization
        if security.authorize(admin_token, "admin_panel"):
            results.append(SecurityTestResult(True, "✅ Admin can access admin_panel", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Admin should access admin_panel", "LOW"))
        
        if not security.authorize(user_token, "admin_panel"):
            results.append(SecurityTestResult(True, "✅ User cannot access admin_panel", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ User should not access admin_panel", "LOW"))
        
        # Test audit logging
        security.audit("login", "admin", "system")
        audit_logs = security.get_audit_logs()
        if audit_logs and len(audit_logs) > 0:
            results.append(SecurityTestResult(True, "✅ Audit logging works", "HIGH"))
        else:
            results.append(SecurityTestResult(False, f"❌ Audit logging failed", "LOW"))
        
        # Test private attribute protection
        security_results = SecurityTester.test_access_control(security, ["users", "permissions", "audit_log"], [])
        results.extend(security_results)
        
        for result in results:
            print(result.message)
        
        security_score = sum(10 if r.security_level == "HIGH" else 5 if r.security_level == "MEDIUM" else 1 for r in results if r.passed)
        total_score = (sum(1 for r in results if r.passed) / len(results)) * 100
        
        if all(r.passed for r in results):
            print(f"\n🎉 HOÀN THÀNH! Điểm số: {total_score:.1f}%")
            print(f"🔒 Security Points: {security_score}")
            tracker.mark_completed("exercise_10", total_score, security_score)
        else:
            print(f"\n❌ Cần cải thiện. Điểm số: {total_score:.1f}%")
            
    except Exception as e:
        print(f"❌ LỖI: {str(e)}")

# ===============================
# MENU SYSTEM
# ===============================

def show_progress():
    """Hiển thị tiến độ học tập"""
    progress = tracker.get_progress()
    print("=" * 60)
    print("🔒 TIẾN ĐỘ HỌC TẬP ENCAPSULATION")
    print("=" * 60)
    print(f"Hoàn thành: {progress['completed']}/{progress['total']} bài tập")
    print(f"Tỷ lệ: {progress['percentage']:.1f}%")
    print(f"Điểm trung bình: {progress['average_score']:.1f}%")
    print(f"Security Points: {progress['security_points']}")
    print(f"Thời gian học: {progress['time_spent']}")
    print()
    
    if progress['completed'] > 0:
        print("✅ Bài tập đã hoàn thành:")
        for exercise in tracker.completed_exercises:
            score = tracker.scores[exercise]
            print(f"  - {exercise}: {score:.1f}%")

def show_security_concepts():
    """Hiển thị các khái niệm security"""
    print("=" * 60)
    print("🔒 KHÁI NIỆM ENCAPSULATION & SECURITY")
    print("=" * 60)
    print("🔹 ENCAPSULATION (Đóng gói):")
    print("  - Ẩn implementation details")
    print("  - Kiểm soát quyền truy cập dữ liệu")
    print("  - Private (__), Protected (_), Public")
    print()
    print("🔹 SECURITY PATTERNS:")
    print("  - Password hashing với salt")
    print("  - Input validation và sanitization")
    print("  - Rate limiting")
    print("  - Session management")
    print("  - Audit logging")
    print()
    print("🔹 PROPERTIES:")
    print("  - @property decorator")
    print("  - Getter, setter, deleter")
    print("  - Computed properties")
    print("  - Validation trong setter")
    print()
    print("💡 Security Best Practices:")
    print("  - Never store passwords in plain text")
    print("  - Validate all inputs")
    print("  - Use secure random tokens")
    print("  - Implement proper access controls")
    print("  - Log security events")

def main_menu():
    """Menu chính"""
    exercises = [
        ("Bài tập 1: Basic Encapsulation", exercise_1),
        ("Bài tập 2: Property Decorators", exercise_2),
        ("Bài tập 3: Secure Bank Account", exercise_3),
        ("Bài tập 4: User Authentication System", exercise_4),
        ("Bài tập 5: Secure Configuration Manager", exercise_5),
        ("Bài tập 6: Secure Database Connection", exercise_6),
        ("Bài tập 7: Secure File Manager", exercise_7),
        ("Bài tập 8: Secure Session Manager", exercise_8),
        ("Bài tập 9: Secure API Client", exercise_9),
        ("Bài tập 10: Enterprise Security System", exercise_10),
    ]
    
    while True:
        print("\n" + "=" * 70)
        print("🔒 BÀI TẬP 3: ENCAPSULATION & DATA PROTECTION")
        print("=" * 70)
        
        for i, (title, _) in enumerate(exercises, 1):
            status = "✅" if f"exercise_{i}" in tracker.completed_exercises else "⭕"
            print(f"{i:2d}. {status} {title}")
        
        print("\n" + "=" * 70)
        print("90. 📊 Xem tiến độ")
        print("91. 🔒 Khái niệm Security")
        print("0.  🚪 Thoát")
        
        try:
            choice = int(input("\n👉 Chọn bài tập (0-91): "))
            
            if choice == 0:
                print("👋 Tạm biệt! Chúc bạn học tập tốt!")
                break
            elif choice == 90:
                show_progress()
            elif choice == 91:
                show_security_concepts()
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
    print("🚀 CHÀO MỪNG ĐẾN VỚI BÀI TẬP ENCAPSULATION & DATA PROTECTION!")
    print("🔒 Hệ thống học tập chuyên sâu về bảo mật và đóng gói dữ liệu")
    print("🎯 15 bài tập thực tế từ cơ bản đến enterprise-level")
    print("💡 Tập trung vào security patterns và data protection")
    
    main_menu() 