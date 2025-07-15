#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BÀI TẬP 4: ỨNG DỤNG THỰC TẾ VỚI LISTS, TUPLES, SETS
Ngày 9-10: 6 Dự án hoàn chỉnh

Mục tiêu học tập:
- Xây dựng các ứng dụng hoàn chỉnh
- Tích hợp kiến thức về Lists, Tuples, Sets
- Xử lý dữ liệu thực tế
- Thiết kế giao diện người dùng đơn giản

Tác giả: Python Learning Journey
Cấp độ: Intermediate đến Advanced
"""

import json
import datetime
from collections import Counter, defaultdict
import random

# ============================================================================
# DỰ ÁN 1: HỆ THỐNG QUẢN LÝ KHO HÀNG (INVENTORY MANAGEMENT)
# ============================================================================

print("=" * 80)
print("DỰ ÁN 1: HỆ THỐNG QUẢN LÝ KHO HÀNG")
print("=" * 80)

class InventoryManager:
    """Hệ thống quản lý kho hàng hoàn chỉnh"""
    
    def __init__(self):
        self.products = {}  # product_id -> {name, category, price, quantity, suppliers}
        self.categories = set()
        self.suppliers = set()
        self.transactions = []  # Lịch sử giao dịch
        self.low_stock_threshold = 10
    
    def add_product(self, product_id, name, category, price, quantity, suppliers):
        """Thêm sản phẩm mới vào kho"""
        if product_id in self.products:
            print(f"Sản phẩm {product_id} đã tồn tại!")
            return False
        
        self.products[product_id] = {
            'name': name,
            'category': category, 
            'price': price,
            'quantity': quantity,
            'suppliers': set(suppliers) if isinstance(suppliers, list) else {suppliers}
        }
        
        self.categories.add(category)
        self.suppliers.update(self.products[product_id]['suppliers'])
        
        # Ghi lại giao dịch
        self.transactions.append({
            'type': 'ADD_PRODUCT',
            'product_id': product_id,
            'quantity': quantity,
            'timestamp': datetime.datetime.now()
        })
        
        print(f"✓ Đã thêm sản phẩm: {name} (ID: {product_id})")
        return True
    
    def update_stock(self, product_id, quantity_change, transaction_type="STOCK_UPDATE"):
        """Cập nhật số lượng tồn kho"""
        if product_id not in self.products:
            print(f"Không tìm thấy sản phẩm {product_id}")
            return False
        
        old_quantity = self.products[product_id]['quantity']
        new_quantity = old_quantity + quantity_change
        
        if new_quantity < 0:
            print(f"Không đủ hàng! Tồn kho hiện tại: {old_quantity}")
            return False
        
        self.products[product_id]['quantity'] = new_quantity
        
        # Ghi lại giao dịch
        self.transactions.append({
            'type': transaction_type,
            'product_id': product_id,
            'quantity_change': quantity_change,
            'old_quantity': old_quantity,
            'new_quantity': new_quantity,
            'timestamp': datetime.datetime.now()
        })
        
        print(f"✓ Cập nhật tồn kho {product_id}: {old_quantity} → {new_quantity}")
        return True
    
    def sell_product(self, product_id, quantity):
        """Bán sản phẩm"""
        return self.update_stock(product_id, -quantity, "SALE")
    
    def restock_product(self, product_id, quantity):
        """Nhập hàng"""
        return self.update_stock(product_id, quantity, "RESTOCK")
    
    def get_low_stock_products(self):
        """Lấy danh sách sản phẩm sắp hết hàng"""
        low_stock = []
        for product_id, product in self.products.items():
            if product['quantity'] <= self.low_stock_threshold:
                low_stock.append((product_id, product['name'], product['quantity']))
        return sorted(low_stock, key=lambda x: x[2])  # Sort by quantity
    
    def get_category_report(self):
        """Báo cáo theo danh mục"""
        category_stats = defaultdict(lambda: {'count': 0, 'total_value': 0, 'total_quantity': 0})
        
        for product in self.products.values():
            cat = product['category']
            category_stats[cat]['count'] += 1
            category_stats[cat]['total_value'] += product['price'] * product['quantity']
            category_stats[cat]['total_quantity'] += product['quantity']
        
        return dict(category_stats)
    
    def search_products(self, keyword=None, category=None, supplier=None):
        """Tìm kiếm sản phẩm theo nhiều tiêu chí"""
        results = []
        
        for product_id, product in self.products.items():
            match = True
            
            if keyword and keyword.lower() not in product['name'].lower():
                match = False
            
            if category and product['category'] != category:
                match = False
                
            if supplier and supplier not in product['suppliers']:
                match = False
            
            if match:
                results.append((product_id, product))
        
        return results
    
    def display_inventory(self):
        """Hiển thị toàn bộ kho hàng"""
        if not self.products:
            print("Kho hàng trống!")
            return
        
        print(f"\n{'ID':<10} {'Tên sản phẩm':<20} {'Danh mục':<15} {'Giá':<10} {'Tồn kho':<10}")
        print("-" * 75)
        
        for product_id, product in self.products.items():
            print(f"{product_id:<10} {product['name']:<20} {product['category']:<15} "
                  f"{product['price']:<10} {product['quantity']:<10}")

# Demo Inventory Manager
print("\n--- DEMO HỆ THỐNG QUẢN LÝ KHO HÀNG ---")

inventory = InventoryManager()

# Thêm sản phẩm mẫu
sample_products = [
    ("P001", "iPhone 15", "Điện thoại", 25000000, 50, ["Apple", "FPT Shop"]),
    ("P002", "Samsung Galaxy S24", "Điện thoại", 22000000, 30, ["Samsung", "Thế Giới Di Động"]),
    ("P003", "MacBook Pro M3", "Laptop", 45000000, 15, ["Apple", "FPT Shop"]),
    ("P004", "Dell XPS 13", "Laptop", 35000000, 8, ["Dell", "Laptop88"]),
    ("P005", "AirPods Pro", "Tai nghe", 6000000, 5, ["Apple"]),
    ("P006", "Sony WH-1000XM4", "Tai nghe", 8000000, 12, ["Sony", "Nguyễn Kim"]),
]

for product_data in sample_products:
    inventory.add_product(*product_data)

# Hiển thị kho hàng
inventory.display_inventory()

# Test các chức năng
print("\n--- THỰC HIỆN CÁC GIAO DỊCH ---")
inventory.sell_product("P001", 5)  # Bán iPhone
inventory.restock_product("P005", 20)  # Nhập AirPods
inventory.sell_product("P004", 3)  # Bán Dell

# Báo cáo sản phẩm sắp hết hàng
print("\n--- SẢN PHẨM SẮP HẾT HÀNG ---")
low_stock = inventory.get_low_stock_products()
for product_id, name, quantity in low_stock:
    print(f"⚠️  {name} (ID: {product_id}): chỉ còn {quantity} sản phẩm")

# Báo cáo theo danh mục
print("\n--- BÁO CÁO THEO DANH MỤC ---")
category_report = inventory.get_category_report()
for category, stats in category_report.items():
    print(f"{category}: {stats['count']} sản phẩm, "
          f"Tổng giá trị: {stats['total_value']:,} VNĐ")

# ============================================================================
# DỰ ÁN 2: HỆ THỐNG QUẢN LÝ HỌC SINH VÀ ĐIỂM SỐ
# ============================================================================

print("\n" + "=" * 80)
print("DỰ ÁN 2: HỆ THỐNG QUẢN LÝ HỌC SINH VÀ ĐIỂM SỐ")
print("=" * 80)

class StudentManagementSystem:
    """Hệ thống quản lý học sinh và điểm số hoàn chỉnh"""
    
    def __init__(self):
        self.students = {}  # student_id -> student_info
        self.classes = {}   # class_id -> set of student_ids
        self.subjects = set()
        self.grades = []    # List of grade records
        self.attendance = []  # List of attendance records
    
    def add_student(self, student_id, name, class_id, birth_date, email):
        """Thêm học sinh mới"""
        if student_id in self.students:
            print(f"Học sinh {student_id} đã tồn tại!")
            return False
        
        self.students[student_id] = {
            'name': name,
            'class_id': class_id,
            'birth_date': birth_date,
            'email': email,
            'enrollment_date': datetime.datetime.now().date()
        }
        
        # Thêm vào lớp
        if class_id not in self.classes:
            self.classes[class_id] = set()
        self.classes[class_id].add(student_id)
        
        print(f"✓ Đã thêm học sinh: {name} (ID: {student_id})")
        return True
    
    def add_grade(self, student_id, subject, score, exam_type="Kiểm tra", date=None):
        """Thêm điểm cho học sinh"""
        if student_id not in self.students:
            print(f"Không tìm thấy học sinh {student_id}")
            return False
        
        if not (0 <= score <= 10):
            print("Điểm phải từ 0 đến 10")
            return False
        
        grade_record = {
            'student_id': student_id,
            'subject': subject,
            'score': score,
            'exam_type': exam_type,
            'date': date or datetime.datetime.now().date()
        }
        
        self.grades.append(grade_record)
        self.subjects.add(subject)
        
        student_name = self.students[student_id]['name']
        print(f"✓ Đã thêm điểm {score} môn {subject} cho {student_name}")
        return True
    
    def mark_attendance(self, student_id, date, status="present"):
        """Điểm danh học sinh"""
        if student_id not in self.students:
            print(f"Không tìm thấy học sinh {student_id}")
            return False
        
        attendance_record = {
            'student_id': student_id,
            'date': date,
            'status': status  # present, absent, late
        }
        
        self.attendance.append(attendance_record)
        return True
    
    def get_student_grades(self, student_id):
        """Lấy tất cả điểm của học sinh"""
        student_grades = [g for g in self.grades if g['student_id'] == student_id]
        
        # Nhóm theo môn học
        subject_grades = defaultdict(list)
        for grade in student_grades:
            subject_grades[grade['subject']].append(grade)
        
        return dict(subject_grades)
    
    def calculate_gpa(self, student_id):
        """Tính điểm trung bình của học sinh"""
        student_grades = self.get_student_grades(student_id)
        
        if not student_grades:
            return 0
        
        subject_averages = []
        for subject, grades in student_grades.items():
            avg = sum(g['score'] for g in grades) / len(grades)
            subject_averages.append(avg)
        
        return sum(subject_averages) / len(subject_averages)
    
    def get_class_ranking(self, class_id):
        """Xếp hạng học sinh trong lớp"""
        if class_id not in self.classes:
            return []
        
        class_students = self.classes[class_id]
        student_gpas = []
        
        for student_id in class_students:
            gpa = self.calculate_gpa(student_id)
            student_name = self.students[student_id]['name']
            student_gpas.append((student_id, student_name, gpa))
        
        return sorted(student_gpas, key=lambda x: x[2], reverse=True)
    
    def get_subject_statistics(self, subject):
        """Thống kê điểm theo môn học"""
        subject_grades = [g['score'] for g in self.grades if g['subject'] == subject]
        
        if not subject_grades:
            return None
        
        return {
            'total_students': len(set(g['student_id'] for g in self.grades if g['subject'] == subject)),
            'total_exams': len(subject_grades),
            'average': sum(subject_grades) / len(subject_grades),
            'highest': max(subject_grades),
            'lowest': min(subject_grades),
            'pass_rate': len([s for s in subject_grades if s >= 5]) / len(subject_grades) * 100
        }
    
    def get_attendance_rate(self, student_id):
        """Tính tỷ lệ chuyên cần"""
        student_attendance = [a for a in self.attendance if a['student_id'] == student_id]
        
        if not student_attendance:
            return 0
        
        present_count = len([a for a in student_attendance if a['status'] == 'present'])
        return (present_count / len(student_attendance)) * 100
    
    def find_top_students(self, n=10):
        """Tìm top học sinh giỏi nhất toàn trường"""
        all_students = []
        
        for student_id in self.students:
            gpa = self.calculate_gpa(student_id)
            if gpa > 0:  # Chỉ tính học sinh có điểm
                student_name = self.students[student_id]['name']
                class_id = self.students[student_id]['class_id']
                all_students.append((student_id, student_name, class_id, gpa))
        
        return sorted(all_students, key=lambda x: x[3], reverse=True)[:n]

# Demo Student Management System  
print("\n--- DEMO HỆ THỐNG QUẢN LÝ HỌC SINH ---")

sms = StudentManagementSystem()

# Thêm học sinh mẫu
sample_students = [
    ("HS001", "Nguyễn Văn An", "10A1", "2008-03-15", "an.nguyen@email.com"),
    ("HS002", "Trần Thị Bình", "10A1", "2008-05-22", "binh.tran@email.com"),
    ("HS003", "Lê Văn Cường", "10A2", "2008-01-10", "cuong.le@email.com"),
    ("HS004", "Phạm Thị Dung", "10A2", "2008-07-08", "dung.pham@email.com"),
    ("HS005", "Hoàng Văn Em", "10A1", "2008-12-03", "em.hoang@email.com"),
]

for student_data in sample_students:
    sms.add_student(*student_data)

# Thêm điểm số mẫu
import random
subjects = ["Toán", "Lý", "Hóa", "Sinh", "Văn", "Sử", "Địa", "Anh"]
exam_types = ["Kiểm tra 15 phút", "Kiểm tra 1 tiết", "Thi học kỳ"]

for student_id in sms.students:
    for subject in subjects:
        for exam_type in exam_types:
            # Tạo điểm ngẫu nhiên với xu hướng tốt
            score = round(random.uniform(5.0, 9.5), 1)
            sms.add_grade(student_id, subject, score, exam_type)

# Hiển thị kết quả
print("\n--- TOP 3 HỌC SINH GIỎI NHẤT ---")
top_students = sms.find_top_students(3)
for i, (student_id, name, class_id, gpa) in enumerate(top_students, 1):
    print(f"{i}. {name} (Lớp {class_id}): GPA {gpa:.2f}")

print("\n--- THỐNG KÊ MÔN TOÁN ---")
math_stats = sms.get_subject_statistics("Toán")
if math_stats:
    print(f"Số học sinh: {math_stats['total_students']}")
    print(f"Điểm trung bình: {math_stats['average']:.2f}")
    print(f"Tỷ lệ đạt: {math_stats['pass_rate']:.1f}%")

print("\n--- XẾP HẠNG LỚP 10A1 ---")
class_ranking = sms.get_class_ranking("10A1")
for i, (student_id, name, gpa) in enumerate(class_ranking, 1):
    print(f"{i}. {name}: GPA {gpa:.2f}")

# ============================================================================
# DỰ ÁN 3: HỆ THỐNG QUẢN LÝ THƯ VIỆN
# ============================================================================

print("\n" + "=" * 80)
print("DỰ ÁN 3: HỆ THỐNG QUẢN LÝ THƯ VIỆN")
print("=" * 80)

class LibraryManagementSystem:
    """Hệ thống quản lý thư viện hoàn chỉnh"""
    
    def __init__(self):
        self.books = {}  # book_id -> book_info
        self.members = {}  # member_id -> member_info
        self.loans = []  # Danh sách cho mượn
        self.reservations = []  # Danh sách đặt trước
        self.categories = set()
        self.authors = set()
        
        # Cài đặt thư viện
        self.max_loan_days = 14
        self.max_books_per_member = 5
        self.fine_per_day = 5000  # VNĐ
    
    def add_book(self, book_id, title, author, category, isbn, publish_year, copies=1):
        """Thêm sách vào thư viện"""
        if book_id in self.books:
            # Nếu sách đã tồn tại, tăng số bản sao
            self.books[book_id]['total_copies'] += copies
            self.books[book_id]['available_copies'] += copies
            print(f"✓ Đã thêm {copies} bản sao cho: {title}")
        else:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'category': category,
                'isbn': isbn,
                'publish_year': publish_year,
                'total_copies': copies,
                'available_copies': copies
            }
            
            self.categories.add(category)
            self.authors.add(author)
            print(f"✓ Đã thêm sách mới: {title}")
        
        return True
    
    def add_member(self, member_id, name, email, phone, address, member_type="standard"):
        """Thêm thành viên mới"""
        if member_id in self.members:
            print(f"Thành viên {member_id} đã tồn tại!")
            return False
        
        self.members[member_id] = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'member_type': member_type,  # standard, premium, student
            'join_date': datetime.datetime.now().date(),
            'current_loans': set(),
            'loan_history': [],
            'total_fines': 0
        }
        
        print(f"✓ Đã thêm thành viên: {name} (ID: {member_id})")
        return True
    
    def loan_book(self, member_id, book_id):
        """Cho mượn sách"""
        # Kiểm tra thành viên
        if member_id not in self.members:
            print(f"Không tìm thấy thành viên {member_id}")
            return False
        
        # Kiểm tra sách
        if book_id not in self.books:
            print(f"Không tìm thấy sách {book_id}")
            return False
        
        member = self.members[member_id]
        book = self.books[book_id]
        
        # Kiểm tra giới hạn mượn sách
        if len(member['current_loans']) >= self.max_books_per_member:
            print(f"Thành viên đã mượn tối đa {self.max_books_per_member} sách")
            return False
        
        # Kiểm tra sách có sẵn
        if book['available_copies'] <= 0:
            print(f"Sách '{book['title']}' hiện không có sẵn")
            return False
        
        # Thực hiện cho mượn
        loan_record = {
            'loan_id': f"L{len(self.loans)+1:04d}",
            'member_id': member_id,
            'book_id': book_id,
            'loan_date': datetime.datetime.now().date(),
            'due_date': datetime.datetime.now().date() + datetime.timedelta(days=self.max_loan_days),
            'return_date': None,
            'fine_amount': 0
        }
        
        self.loans.append(loan_record)
        book['available_copies'] -= 1
        member['current_loans'].add(book_id)
        
        print(f"✓ Cho mượn thành công: {book['title']} → {member['name']}")
        print(f"  Hạn trả: {loan_record['due_date']}")
        return True
    
    def return_book(self, member_id, book_id):
        """Trả sách"""
        # Tìm bản ghi mượn sách
        loan_record = None
        for loan in self.loans:
            if (loan['member_id'] == member_id and 
                loan['book_id'] == book_id and 
                loan['return_date'] is None):
                loan_record = loan
                break
        
        if not loan_record:
            print("Không tìm thấy bản ghi mượn sách")
            return False
        
        # Cập nhật thông tin trả sách
        return_date = datetime.datetime.now().date()
        loan_record['return_date'] = return_date
        
        # Tính phí phạt nếu trả muộn
        if return_date > loan_record['due_date']:
            days_late = (return_date - loan_record['due_date']).days
            fine = days_late * self.fine_per_day
            loan_record['fine_amount'] = fine
            self.members[member_id]['total_fines'] += fine
            print(f"⚠️  Trả muộn {days_late} ngày. Phí phạt: {fine:,} VNĐ")
        
        # Cập nhật trạng thái
        self.books[book_id]['available_copies'] += 1
        self.members[member_id]['current_loans'].discard(book_id)
        self.members[member_id]['loan_history'].append(loan_record['loan_id'])
        
        book_title = self.books[book_id]['title']
        member_name = self.members[member_id]['name']
        print(f"✓ Trả sách thành công: {book_title} ← {member_name}")
        return True
    
    def search_books(self, keyword=None, author=None, category=None):
        """Tìm kiếm sách"""
        results = []
        
        for book_id, book in self.books.items():
            match = True
            
            if keyword and keyword.lower() not in book['title'].lower():
                match = False
            
            if author and author.lower() not in book['author'].lower():
                match = False
                
            if category and book['category'] != category:
                match = False
            
            if match:
                results.append((book_id, book))
        
        return results
    
    def get_overdue_books(self):
        """Lấy danh sách sách quá hạn"""
        today = datetime.datetime.now().date()
        overdue = []
        
        for loan in self.loans:
            if loan['return_date'] is None and loan['due_date'] < today:
                days_overdue = (today - loan['due_date']).days
                overdue.append((loan, days_overdue))
        
        return sorted(overdue, key=lambda x: x[1], reverse=True)
    
    def get_popular_books(self, limit=10):
        """Lấy sách được mượn nhiều nhất"""
        book_loan_count = Counter()
        
        for loan in self.loans:
            book_loan_count[loan['book_id']] += 1
        
        popular = []
        for book_id, count in book_loan_count.most_common(limit):
            book = self.books[book_id]
            popular.append((book_id, book['title'], book['author'], count))
        
        return popular
    
    def generate_member_report(self, member_id):
        """Tạo báo cáo cho thành viên"""
        if member_id not in self.members:
            return None
        
        member = self.members[member_id]
        
        # Sách đang mượn
        current_books = []
        for loan in self.loans:
            if (loan['member_id'] == member_id and 
                loan['return_date'] is None):
                book = self.books[loan['book_id']]
                current_books.append({
                    'title': book['title'],
                    'due_date': loan['due_date'],
                    'days_left': (loan['due_date'] - datetime.datetime.now().date()).days
                })
        
        # Thống kê
        total_loans = len([l for l in self.loans if l['member_id'] == member_id])
        
        return {
            'member_info': member,
            'current_loans': current_books,
            'total_loans': total_loans,
            'total_fines': member['total_fines']
        }

# Demo Library Management System
print("\n--- DEMO HỆ THỐNG QUẢN LÝ THƯ VIỆN ---")

library = LibraryManagementSystem()

# Thêm sách mẫu
sample_books = [
    ("B001", "Clean Code", "Robert C. Martin", "Programming", "978-0132350884", 2008, 3),
    ("B002", "Python Tricks", "Dan Bader", "Programming", "978-1775093305", 2017, 2),
    ("B003", "Sapiens", "Yuval Noah Harari", "History", "978-0062316097", 2014, 5),
    ("B004", "Atomic Habits", "James Clear", "Self-help", "978-0735211292", 2018, 4),
    ("B005", "The Alchemist", "Paulo Coelho", "Fiction", "978-0062315007", 1988, 3),
]

for book_data in sample_books:
    library.add_book(*book_data)

# Thêm thành viên mẫu
sample_members = [
    ("M001", "Nguyễn Văn A", "a.nguyen@email.com", "0901234567", "Hà Nội", "premium"),
    ("M002", "Trần Thị B", "b.tran@email.com", "0912345678", "HCM", "standard"),
    ("M003", "Lê Văn C", "c.le@email.com", "0923456789", "Đà Nẵng", "student"),
]

for member_data in sample_members:
    library.add_member(*member_data)

# Thực hiện giao dịch mẫu
print("\n--- THỰC HIỆN CHO MƯỢN SÁCH ---")
library.loan_book("M001", "B001")  # Nguyễn Văn A mượn Clean Code
library.loan_book("M001", "B003")  # Nguyễn Văn A mượn Sapiens
library.loan_book("M002", "B002")  # Trần Thị B mượn Python Tricks
library.loan_book("M003", "B004")  # Lê Văn C mượn Atomic Habits

# Trả sách
print("\n--- TRẢ SÁCH ---")
library.return_book("M002", "B002")  # Trần Thị B trả Python Tricks

# Tìm kiếm sách
print("\n--- TÌM KIẾM SÁCH ---")
search_results = library.search_books(keyword="python")
print("Kết quả tìm kiếm 'python':")
for book_id, book in search_results:
    status = "Có sẵn" if book['available_copies'] > 0 else "Hết sách"
    print(f"  {book['title']} - {book['author']} ({status})")

# Báo cáo thành viên
print("\n--- BÁO CÁO THÀNH VIÊN M001 ---")
report = library.generate_member_report("M001")
if report:
    print(f"Thành viên: {report['member_info']['name']}")
    print(f"Tổng số lần mượn: {report['total_loans']}")
    print(f"Phí phạt tích lũy: {report['total_fines']:,} VNĐ")
    print("Sách đang mượn:")
    for book in report['current_loans']:
        print(f"  - {book['title']} (còn {book['days_left']} ngày)")

print("\n" + "="*80)
print("HOÀN THÀNH 3/6 DỰ ÁN ỨNG DỤNG THỰC TẾ")
print("✓ Hệ thống quản lý kho hàng")
print("✓ Hệ thống quản lý học sinh và điểm số") 
print("✓ Hệ thống quản lý thư viện")
print("Tiếp tục với 3 dự án còn lại...")
print("="*80) 