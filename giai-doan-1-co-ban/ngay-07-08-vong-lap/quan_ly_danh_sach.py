"""
HỆ THỐNG QUẢN LÝ DANH SÁCH CRUD
===============================

Hệ thống quản lý danh sách hoàn chỉnh với:
- CRUD operations (Create, Read, Update, Delete)
- Search and filter functions
- Sort options
- Data validation
- Statistics and reports

Yêu cầu: 400+ dòng code với loops
"""

import time
import json

print("📋 HỆ THỐNG QUẢN LÝ DANH SÁCH CRUD")
print("=" * 50)

# Global database
items_database = []
category_list = ["Công việc", "Cá nhân", "Học tập", "Mua sắm", "Khác"]

def generate_id():
    """Tạo ID duy nhất cho item"""
    if not items_database:
        return 1
    return max(item['id'] for item in items_database) + 1

def display_main_menu():
    """Hiển thị menu chính"""
    print(f"\n📋 QUẢN LÝ DANH SÁCH - {len(items_database)} items")
    print("=" * 50)
    print("📝 CRUD OPERATIONS:")
    print("1. ➕ Create - Thêm item mới")
    print("2. 👀 Read - Xem danh sách")
    print("3. ✏️ Update - Cập nhật item")
    print("4. 🗑️ Delete - Xóa item")
    
    print("\n🔍 SEARCH & FILTER:")
    print("5. 🔎 Search - Tìm kiếm")
    print("6. 🏷️ Filter by Category")
    print("7. ⭐ Filter by Priority")
    print("8. ✅ Filter by Status")
    
    print("\n📊 MANAGEMENT:")
    print("9. 🔄 Sort Options")
    print("10. 📊 Statistics")
    print("11. 📈 Reports")
    print("12. 📁 Categories Management")
    
    print("\n💾 DATA:")
    print("13. 💾 Export Data")
    print("14. 📂 Import Data")
    print("15. 🗑️ Clear All")
    print("16. 🚪 Exit")

def create_item():
    """Tạo item mới - CREATE operation"""
    print("\n➕ THÊM ITEM MỚI")
    print("-" * 30)
    
    # Nhập thông tin cơ bản
    while True:
        title = input("Tiêu đề (*): ").strip()
        if title:
            break
        print("❌ Tiêu đề không được rỗng!")
    
    description = input("Mô tả: ").strip()
    
    # Chọn category
    print("\nCHỌN DANH MỤC:")
    for i, cat in enumerate(category_list, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            cat_choice = int(input("Chọn danh mục (1-5): "))
            if 1 <= cat_choice <= len(category_list):
                category = category_list[cat_choice - 1]
                break
            print("❌ Chọn từ 1-5!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    # Chọn priority
    priority_levels = ["Thấp", "Trung bình", "Cao", "Khẩn cấp"]
    print("\nMỨC ĐỘ ƯU TIÊN:")
    for i, priority in enumerate(priority_levels, 1):
        print(f"{i}. {priority}")
    
    while True:
        try:
            priority_choice = int(input("Chọn mức độ (1-4): "))
            if 1 <= priority_choice <= 4:
                priority = priority_levels[priority_choice - 1]
                break
            print("❌ Chọn từ 1-4!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    # Ngày deadline (optional)
    deadline = input("Deadline (dd/mm/yyyy, để trống nếu không có): ").strip()
    if deadline and len(deadline) != 10:
        deadline = ""
    
    # Tags
    tags_input = input("Tags (phân cách bằng dấu phẩy): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
    
    # Tạo item object
    new_item = {
        "id": generate_id(),
        "title": title,
        "description": description,
        "category": category,
        "priority": priority,
        "status": "Chưa bắt đầu",
        "deadline": deadline,
        "tags": tags,
        "created_at": time.strftime("%d/%m/%Y %H:%M"),
        "updated_at": time.strftime("%d/%m/%Y %H:%M"),
        "completed_at": ""
    }
    
    items_database.append(new_item)
    print(f"\n✅ Đã tạo item ID: {new_item['id']} - '{title}'")

def read_items():
    """Đọc và hiển thị danh sách - READ operation"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    print(f"\n👀 DANH SÁCH ITEMS ({len(items_database)} items)")
    print("=" * 80)
    
    # Header
    print(f"{'ID':<3} {'Tiêu đề':<20} {'Danh mục':<12} {'Ưu tiên':<10} {'Trạng thái':<15} {'Deadline':<12}")
    print("-" * 80)
    
    # Display items
    for item in items_database:
        title_short = item['title'][:17] + "..." if len(item['title']) > 20 else item['title']
        deadline_display = item['deadline'] if item['deadline'] else "N/A"
        
        print(f"{item['id']:<3} {title_short:<20} {item['category']:<12} "
              f"{item['priority']:<10} {item['status']:<15} {deadline_display:<12}")
    
    # Quick stats
    total = len(items_database)
    completed = len([item for item in items_database if item['status'] == 'Hoàn thành'])
    in_progress = len([item for item in items_database if item['status'] == 'Đang thực hiện'])
    
    print("-" * 80)
    print(f"📊 Tổng: {total} | Hoàn thành: {completed} | Đang thực hiện: {in_progress}")

def view_item_details():
    """Xem chi tiết một item"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    try:
        item_id = int(input("Nhập ID item để xem chi tiết: "))
        item = next((item for item in items_database if item['id'] == item_id), None)
        
        if not item:
            print("❌ Không tìm thấy item!")
            return
        
        print(f"\n📋 CHI TIẾT ITEM #{item['id']}")
        print("=" * 40)
        print(f"Tiêu đề: {item['title']}")
        print(f"Mô tả: {item['description']}")
        print(f"Danh mục: {item['category']}")
        print(f"Ưu tiên: {item['priority']}")
        print(f"Trạng thái: {item['status']}")
        print(f"Deadline: {item['deadline'] if item['deadline'] else 'Không có'}")
        print(f"Tags: {', '.join(item['tags']) if item['tags'] else 'Không có'}")
        print(f"Tạo lúc: {item['created_at']}")
        print(f"Cập nhật: {item['updated_at']}")
        if item['completed_at']:
            print(f"Hoàn thành: {item['completed_at']}")
            
    except ValueError:
        print("❌ Vui lòng nhập số!")

def update_item():
    """Cập nhật item - UPDATE operation"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    read_items()
    
    try:
        item_id = int(input("\nNhập ID item cần cập nhật: "))
        item = next((item for item in items_database if item['id'] == item_id), None)
        
        if not item:
            print("❌ Không tìm thấy item!")
            return
        
        print(f"\n✏️ CẬP NHẬT ITEM #{item['id']}: {item['title']}")
        print("(Để trống để giữ nguyên giá trị hiện tại)")
        print("-" * 40)
        
        # Update title
        new_title = input(f"Tiêu đề hiện tại: '{item['title']}'\nTiêu đề mới: ").strip()
        if new_title:
            item['title'] = new_title
        
        # Update description
        new_desc = input(f"Mô tả hiện tại: '{item['description']}'\nMô tả mới: ").strip()
        if new_desc:
            item['description'] = new_desc
        
        # Update category
        print(f"\nDanh mục hiện tại: {item['category']}")
        print("Danh mục mới:")
        for i, cat in enumerate(category_list, 1):
            print(f"{i}. {cat}")
        
        cat_input = input("Chọn danh mục mới (để trống để giữ nguyên): ").strip()
        if cat_input:
            try:
                cat_choice = int(cat_input)
                if 1 <= cat_choice <= len(category_list):
                    item['category'] = category_list[cat_choice - 1]
            except ValueError:
                pass
        
        # Update priority
        priority_levels = ["Thấp", "Trung bình", "Cao", "Khẩn cấp"]
        print(f"\nƯu tiên hiện tại: {item['priority']}")
        print("Ưu tiên mới:")
        for i, priority in enumerate(priority_levels, 1):
            print(f"{i}. {priority}")
        
        priority_input = input("Chọn ưu tiên mới (để trống để giữ nguyên): ").strip()
        if priority_input:
            try:
                priority_choice = int(priority_input)
                if 1 <= priority_choice <= 4:
                    item['priority'] = priority_levels[priority_choice - 1]
            except ValueError:
                pass
        
        # Update status
        status_options = ["Chưa bắt đầu", "Đang thực hiện", "Hoàn thành", "Tạm dừng", "Hủy bỏ"]
        print(f"\nTrạng thái hiện tại: {item['status']}")
        print("Trạng thái mới:")
        for i, status in enumerate(status_options, 1):
            print(f"{i}. {status}")
        
        status_input = input("Chọn trạng thái mới (để trống để giữ nguyên): ").strip()
        if status_input:
            try:
                status_choice = int(status_input)
                if 1 <= status_choice <= 5:
                    new_status = status_options[status_choice - 1]
                    if new_status == "Hoàn thành" and item['status'] != "Hoàn thành":
                        item['completed_at'] = time.strftime("%d/%m/%Y %H:%M")
                    item['status'] = new_status
            except ValueError:
                pass
        
        # Update deadline
        new_deadline = input(f"Deadline hiện tại: '{item['deadline']}'\nDeadline mới (dd/mm/yyyy): ").strip()
        if new_deadline:
            if len(new_deadline) == 10:
                item['deadline'] = new_deadline
        
        # Update tags
        current_tags = ', '.join(item['tags']) if item['tags'] else 'Không có'
        new_tags_input = input(f"Tags hiện tại: '{current_tags}'\nTags mới (phân cách bằng dấu phẩy): ").strip()
        if new_tags_input:
            item['tags'] = [tag.strip() for tag in new_tags_input.split(",")]
        
        # Update timestamp
        item['updated_at'] = time.strftime("%d/%m/%Y %H:%M")
        
        print(f"\n✅ Đã cập nhật item #{item['id']}")
        
    except ValueError:
        print("❌ Vui lòng nhập số!")

def delete_item():
    """Xóa item - DELETE operation"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    read_items()
    
    try:
        item_id = int(input("\nNhập ID item cần xóa: "))
        item = next((item for item in items_database if item['id'] == item_id), None)
        
        if not item:
            print("❌ Không tìm thấy item!")
            return
        
        print(f"\n🗑️ XÓA ITEM:")
        print(f"ID: {item['id']}")
        print(f"Tiêu đề: {item['title']}")
        print(f"Danh mục: {item['category']}")
        
        confirm = input("\nXác nhận xóa? (yes/no): ").lower()
        
        if confirm in ['yes', 'y', 'có']:
            items_database.remove(item)
            print(f"✅ Đã xóa item #{item_id}")
        else:
            print("❌ Đã hủy xóa!")
            
    except ValueError:
        print("❌ Vui lòng nhập số!")

def search_items():
    """Tìm kiếm items"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    print("\n🔎 TÌM KIẾM ITEMS")
    print("1. Tìm theo tiêu đề")
    print("2. Tìm theo mô tả")
    print("3. Tìm theo tags")
    print("4. Tìm tổng hợp")
    
    while True:
        try:
            choice = int(input("Chọn loại tìm kiếm (1-4): "))
            if 1 <= choice <= 4:
                break
            print("❌ Chọn từ 1-4!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    search_term = input("Nhập từ khóa tìm kiếm: ").lower().strip()
    
    if not search_term:
        print("❌ Từ khóa không được rỗng!")
        return
    
    found_items = []
    
    for item in items_database:
        if choice == 1:  # Tìm theo tiêu đề
            if search_term in item['title'].lower():
                found_items.append(item)
        elif choice == 2:  # Tìm theo mô tả
            if search_term in item['description'].lower():
                found_items.append(item)
        elif choice == 3:  # Tìm theo tags
            if any(search_term in tag.lower() for tag in item['tags']):
                found_items.append(item)
        elif choice == 4:  # Tìm tổng hợp
            if (search_term in item['title'].lower() or 
                search_term in item['description'].lower() or
                any(search_term in tag.lower() for tag in item['tags'])):
                found_items.append(item)
    
    if found_items:
        print(f"\n🎯 TÌM THẤY {len(found_items)} KẾT QUẢ cho '{search_term}':")
        print("-" * 60)
        
        for item in found_items:
            print(f"ID: {item['id']} | {item['title']} | {item['category']} | {item['status']}")
    else:
        print(f"❌ Không tìm thấy kết quả cho '{search_term}'")

def filter_by_category():
    """Lọc theo danh mục"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    print("\n🏷️ LỌC THEO DANH MỤC:")
    for i, cat in enumerate(category_list, 1):
        count = len([item for item in items_database if item['category'] == cat])
        print(f"{i}. {cat} ({count} items)")
    
    while True:
        try:
            choice = int(input("Chọn danh mục (1-5): "))
            if 1 <= choice <= len(category_list):
                selected_category = category_list[choice - 1]
                break
            print("❌ Chọn từ 1-5!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    filtered_items = [item for item in items_database if item['category'] == selected_category]
    
    if filtered_items:
        print(f"\n📋 ITEMS TRONG DANH MỤC '{selected_category}' ({len(filtered_items)} items):")
        print("-" * 60)
        
        for item in filtered_items:
            print(f"ID: {item['id']} | {item['title']} | {item['priority']} | {item['status']}")
    else:
        print(f"❌ Không có item nào trong danh mục '{selected_category}'")

def filter_by_priority():
    """Lọc theo mức độ ưu tiên"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    priority_levels = ["Thấp", "Trung bình", "Cao", "Khẩn cấp"]
    
    print("\n⭐ LỌC THEO MỨC ĐỘ ƯU TIÊN:")
    for i, priority in enumerate(priority_levels, 1):
        count = len([item for item in items_database if item['priority'] == priority])
        print(f"{i}. {priority} ({count} items)")
    
    while True:
        try:
            choice = int(input("Chọn mức độ (1-4): "))
            if 1 <= choice <= 4:
                selected_priority = priority_levels[choice - 1]
                break
            print("❌ Chọn từ 1-4!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    filtered_items = [item for item in items_database if item['priority'] == selected_priority]
    
    if filtered_items:
        print(f"\n⭐ ITEMS MỨC ĐỘ '{selected_priority}' ({len(filtered_items)} items):")
        print("-" * 60)
        
        for item in filtered_items:
            print(f"ID: {item['id']} | {item['title']} | {item['category']} | {item['status']}")
    else:
        print(f"❌ Không có item nào ở mức độ '{selected_priority}'")

def filter_by_status():
    """Lọc theo trạng thái"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    status_options = ["Chưa bắt đầu", "Đang thực hiện", "Hoàn thành", "Tạm dừng", "Hủy bỏ"]
    
    print("\n✅ LỌC THEO TRẠNG THÁI:")
    for i, status in enumerate(status_options, 1):
        count = len([item for item in items_database if item['status'] == status])
        print(f"{i}. {status} ({count} items)")
    
    while True:
        try:
            choice = int(input("Chọn trạng thái (1-5): "))
            if 1 <= choice <= 5:
                selected_status = status_options[choice - 1]
                break
            print("❌ Chọn từ 1-5!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    filtered_items = [item for item in items_database if item['status'] == selected_status]
    
    if filtered_items:
        print(f"\n✅ ITEMS TRẠNG THÁI '{selected_status}' ({len(filtered_items)} items):")
        print("-" * 60)
        
        for item in filtered_items:
            print(f"ID: {item['id']} | {item['title']} | {item['category']} | {item['priority']}")
    else:
        print(f"❌ Không có item nào ở trạng thái '{selected_status}'")

def sort_items():
    """Sắp xếp danh sách"""
    if not items_database:
        print("📭 Danh sách trống!")
        return
    
    print("\n🔄 SORT OPTIONS:")
    print("1. Sắp xếp theo ID")
    print("2. Sắp xếp theo tiêu đề")
    print("3. Sắp xếp theo danh mục")
    print("4. Sắp xếp theo ưu tiên")
    print("5. Sắp xếp theo trạng thái")
    print("6. Sắp xếp theo ngày tạo")
    
    while True:
        try:
            choice = int(input("Chọn cách sắp xếp (1-6): "))
            if 1 <= choice <= 6:
                break
            print("❌ Chọn từ 1-6!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    reverse_order = input("Sắp xếp ngược (y/n): ").lower() == 'y'
    
    # Sort logic
    if choice == 1:
        items_database.sort(key=lambda x: x['id'], reverse=reverse_order)
        sort_field = "ID"
    elif choice == 2:
        items_database.sort(key=lambda x: x['title'].lower(), reverse=reverse_order)
        sort_field = "tiêu đề"
    elif choice == 3:
        items_database.sort(key=lambda x: x['category'], reverse=reverse_order)
        sort_field = "danh mục"
    elif choice == 4:
        priority_order = {"Khẩn cấp": 4, "Cao": 3, "Trung bình": 2, "Thấp": 1}
        items_database.sort(key=lambda x: priority_order[x['priority']], reverse=reverse_order)
        sort_field = "ưu tiên"
    elif choice == 5:
        items_database.sort(key=lambda x: x['status'], reverse=reverse_order)
        sort_field = "trạng thái"
    elif choice == 6:
        items_database.sort(key=lambda x: x['created_at'], reverse=reverse_order)
        sort_field = "ngày tạo"
    
    order_text = "giảm dần" if reverse_order else "tăng dần"
    print(f"✅ Đã sắp xếp theo {sort_field} ({order_text})")
    
    # Show result
    read_items()

def show_statistics():
    """Hiển thị thống kê"""
    if not items_database:
        print("📊 Không có dữ liệu để thống kê!")
        return
    
    print("\n📊 THỐNG KÊ TỔNG QUAN")
    print("=" * 40)
    
    total_items = len(items_database)
    print(f"📋 Tổng số items: {total_items}")
    
    # Thống kê theo trạng thái
    status_stats = {}
    for item in items_database:
        status = item['status']
        status_stats[status] = status_stats.get(status, 0) + 1
    
    print("\n📈 THEO TRẠNG THÁI:")
    for status, count in status_stats.items():
        percentage = (count / total_items) * 100
        print(f"- {status}: {count} ({percentage:.1f}%)")
    
    # Thống kê theo danh mục
    category_stats = {}
    for item in items_database:
        category = item['category']
        category_stats[category] = category_stats.get(category, 0) + 1
    
    print("\n🏷️ THEO DANH MỤC:")
    for category, count in category_stats.items():
        percentage = (count / total_items) * 100
        print(f"- {category}: {count} ({percentage:.1f}%)")
    
    # Thống kê theo ưu tiên
    priority_stats = {}
    for item in items_database:
        priority = item['priority']
        priority_stats[priority] = priority_stats.get(priority, 0) + 1
    
    print("\n⭐ THEO ƯU TIÊN:")
    for priority, count in priority_stats.items():
        percentage = (count / total_items) * 100
        print(f"- {priority}: {count} ({percentage:.1f}%)")
    
    # Items có deadline
    items_with_deadline = [item for item in items_database if item['deadline']]
    print(f"\n📅 Items có deadline: {len(items_with_deadline)}")
    
    # Tags phổ biến
    all_tags = []
    for item in items_database:
        all_tags.extend(item['tags'])
    
    if all_tags:
        tag_stats = {}
        for tag in all_tags:
            tag_stats[tag] = tag_stats.get(tag, 0) + 1
        
        popular_tags = sorted(tag_stats.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"\n🏷️ TOP 5 TAGS PHỔ BIẾN:")
        for tag, count in popular_tags:
            print(f"- {tag}: {count} lần")

def generate_reports():
    """Tạo báo cáo chi tiết"""
    if not items_database:
        print("📈 Không có dữ liệu để tạo báo cáo!")
        return
    
    print("\n📈 BÁO CÁO CHI TIẾT")
    print("=" * 50)
    
    # Báo cáo hiệu suất
    completed_items = [item for item in items_database if item['status'] == 'Hoàn thành']
    in_progress_items = [item for item in items_database if item['status'] == 'Đang thực hiện']
    overdue_items = []
    
    # Tìm items quá hạn
    from datetime import datetime
    today = datetime.now()
    
    for item in items_database:
        if item['deadline'] and item['status'] != 'Hoàn thành':
            try:
                deadline_date = datetime.strptime(item['deadline'], "%d/%m/%Y")
                if deadline_date < today:
                    overdue_items.append(item)
            except ValueError:
                pass
    
    print(f"📊 HIỆU SUẤT:")
    print(f"- Hoàn thành: {len(completed_items)} items")
    print(f"- Đang thực hiện: {len(in_progress_items)} items")
    print(f"- Quá hạn: {len(overdue_items)} items")
    
    if overdue_items:
        print(f"\n⚠️ ITEMS QUÁ HẠN:")
        for item in overdue_items:
            print(f"- ID {item['id']}: {item['title']} (Deadline: {item['deadline']})")
    
    # Productivity by category
    print(f"\n📋 PRODUCTIVITY THEO DANH MỤC:")
    for category in category_list:
        cat_items = [item for item in items_database if item['category'] == category]
        cat_completed = [item for item in cat_items if item['status'] == 'Hoàn thành']
        
        if cat_items:
            completion_rate = (len(cat_completed) / len(cat_items)) * 100
            print(f"- {category}: {len(cat_completed)}/{len(cat_items)} ({completion_rate:.1f}%)")
    
    # Recent activity
    recent_items = sorted(items_database, key=lambda x: x['updated_at'], reverse=True)[:5]
    print(f"\n🕒 HOẠT ĐỘNG GẦN ĐÂY:")
    for item in recent_items:
        print(f"- {item['updated_at']}: {item['title']} ({item['status']})")

def manage_categories():
    """Quản lý danh mục"""
    global category_list
    
    while True:
        print(f"\n📁 QUẢN LÝ DANH MỤC")
        print("=" * 30)
        print("DANH SÁCH HIỆN TẠI:")
        for i, cat in enumerate(category_list, 1):
            count = len([item for item in items_database if item['category'] == cat])
            print(f"{i}. {cat} ({count} items)")
        
        print("\nTHAO TÁC:")
        print("1. Thêm danh mục")
        print("2. Xóa danh mục")
        print("3. Đổi tên danh mục")
        print("4. Quay lại")
        
        try:
            choice = int(input("Chọn (1-4): "))
            
            if choice == 1:
                new_cat = input("Tên danh mục mới: ").strip()
                if new_cat and new_cat not in category_list:
                    category_list.append(new_cat)
                    print(f"✅ Đã thêm danh mục '{new_cat}'")
                else:
                    print("❌ Danh mục đã tồn tại hoặc rỗng!")
            
            elif choice == 2:
                if len(category_list) <= 1:
                    print("❌ Phải có ít nhất 1 danh mục!")
                    continue
                
                cat_index = int(input("Nhập số thứ tự danh mục cần xóa: ")) - 1
                if 0 <= cat_index < len(category_list):
                    cat_to_delete = category_list[cat_index]
                    
                    # Kiểm tra có items không
                    items_in_cat = [item for item in items_database if item['category'] == cat_to_delete]
                    if items_in_cat:
                        print(f"⚠️ Có {len(items_in_cat)} items trong danh mục này!")
                        confirm = input("Xóa và chuyển items sang danh mục 'Khác'? (y/n): ")
                        if confirm.lower() == 'y':
                            for item in items_in_cat:
                                item['category'] = 'Khác'
                    
                    category_list.pop(cat_index)
                    print(f"✅ Đã xóa danh mục '{cat_to_delete}'")
                
            elif choice == 3:
                cat_index = int(input("Nhập số thứ tự danh mục cần đổi tên: ")) - 1
                if 0 <= cat_index < len(category_list):
                    old_name = category_list[cat_index]
                    new_name = input(f"Tên mới cho '{old_name}': ").strip()
                    
                    if new_name and new_name not in category_list:
                        # Update items
                        for item in items_database:
                            if item['category'] == old_name:
                                item['category'] = new_name
                        
                        category_list[cat_index] = new_name
                        print(f"✅ Đã đổi tên '{old_name}' thành '{new_name}'")
                    else:
                        print("❌ Tên mới rỗng hoặc đã tồn tại!")
            
            elif choice == 4:
                break
                
        except (ValueError, IndexError):
            print("❌ Lựa chọn không hợp lệ!")

def export_data():
    """Export dữ liệu"""
    if not items_database:
        print("💾 Không có dữ liệu để export!")
        return
    
    filename = input("Tên file export (ví dụ: backup.json): ").strip()
    if not filename:
        filename = f"export_{time.strftime('%Y%m%d_%H%M%S')}.json"
    
    if not filename.endswith('.json'):
        filename += '.json'
    
    try:
        export_data = {
            "items": items_database,
            "categories": category_list,
            "export_time": time.strftime("%d/%m/%Y %H:%M:%S"),
            "total_items": len(items_database)
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã export {len(items_database)} items vào '{filename}'")
        
    except Exception as e:
        print(f"❌ Lỗi export: {e}")

def import_data():
    """Import dữ liệu"""
    filename = input("Tên file import: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            import_data = json.load(f)
        
        if 'items' in import_data:
            global items_database, category_list
            
            print(f"📂 File chứa {len(import_data['items'])} items")
            print(f"Export time: {import_data.get('export_time', 'Unknown')}")
            
            choice = input("Import mode (1=Replace all, 2=Merge): ")
            
            if choice == '1':
                items_database = import_data['items']
                if 'categories' in import_data:
                    category_list = import_data['categories']
                print(f"✅ Đã thay thế tất cả dữ liệu")
            
            elif choice == '2':
                # Merge data
                current_max_id = max([item['id'] for item in items_database]) if items_database else 0
                
                for item in import_data['items']:
                    # Tạo ID mới để tránh conflict
                    current_max_id += 1
                    item['id'] = current_max_id
                    items_database.append(item)
                
                # Merge categories
                if 'categories' in import_data:
                    for cat in import_data['categories']:
                        if cat not in category_list:
                            category_list.append(cat)
                
                print(f"✅ Đã merge {len(import_data['items'])} items")
        else:
            print("❌ File không đúng format!")
            
    except FileNotFoundError:
        print("❌ File không tồn tại!")
    except json.JSONDecodeError:
        print("❌ File JSON không hợp lệ!")
    except Exception as e:
        print(f"❌ Lỗi import: {e}")

def clear_all_data():
    """Xóa tất cả dữ liệu"""
    if not items_database:
        print("🗑️ Danh sách đã trống!")
        return
    
    print(f"⚠️ CẢNH BÁO: Sẽ xóa tất cả {len(items_database)} items!")
    confirm1 = input("Nhập 'DELETE' để xác nhận: ")
    
    if confirm1 == 'DELETE':
        confirm2 = input("Bạn có chắc chắn? (yes/no): ")
        if confirm2.lower() == 'yes':
            global items_database
            items_database = []
            print("✅ Đã xóa tất cả dữ liệu!")
        else:
            print("❌ Đã hủy!")
    else:
        print("❌ Đã hủy!")

def main():
    """Chương trình chính"""
    print("🎉 Chào mừng đến với Hệ Thống Quản Lý Danh Sách CRUD!")
    print("Hệ thống quản lý hoàn chỉnh với đầy đủ tính năng")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nChọn chức năng (1-16): "))
            
            if choice == 1:
                create_item()
            elif choice == 2:
                read_items()
                if items_database:
                    detail_choice = input("\nXem chi tiết item? (y/n): ")
                    if detail_choice.lower() == 'y':
                        view_item_details()
            elif choice == 3:
                update_item()
            elif choice == 4:
                delete_item()
            elif choice == 5:
                search_items()
            elif choice == 6:
                filter_by_category()
            elif choice == 7:
                filter_by_priority()
            elif choice == 8:
                filter_by_status()
            elif choice == 9:
                sort_items()
            elif choice == 10:
                show_statistics()
            elif choice == 11:
                generate_reports()
            elif choice == 12:
                manage_categories()
            elif choice == 13:
                export_data()
            elif choice == 14:
                import_data()
            elif choice == 15:
                clear_all_data()
            elif choice == 16:
                print("\n👋 Cảm ơn bạn đã sử dụng Hệ Thống Quản Lý!")
                if items_database:
                    print(f"📊 Bạn đã quản lý {len(items_database)} items")
                    completed = len([item for item in items_database if item['status'] == 'Hoàn thành'])
                    print(f"✅ Hoàn thành: {completed} items")
                print("🎓 Dự án CRUD hoàn thành!")
                break
            else:
                print("❌ Chọn từ 1-16!")
                
        except ValueError:
            print("❌ Vui lòng nhập số!")
        except KeyboardInterrupt:
            print("\n\n👋 Tạm biệt!")
            break
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main() 