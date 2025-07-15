"""
MÁY TÍNH KHOA HỌC NÂNG CAO
==========================

Máy tính khoa học với đầy đủ tính năng:
- Menu-driven interface
- All basic operations (+, -, *, /, //, %, **)
- Advanced functions (sqrt, sin, cos, log)
- Memory functions (store, recall, clear)
- History of calculations
- Error handling

Yêu cầu: 300+ dòng code với loops
"""

import math
import time

print("🧮 MÁY TÍNH KHOA HỌC NÂNG CAO")
print("=" * 40)

# Global variables
calculator_memory = 0
calculation_history = []
last_result = 0

def display_main_menu():
    """Hiển thị menu chính"""
    print(f"\n🧮 SCIENTIFIC CALCULATOR")
    print("=" * 40)
    print("📊 BASIC OPERATIONS:")
    print("1. ➕ Cộng")
    print("2. ➖ Trừ") 
    print("3. ✖️ Nhân")
    print("4. ➗ Chia")
    print("5. 📐 Chia lấy nguyên")
    print("6. 🔢 Chia lấy dư")
    print("7. 🔺 Lũy thừa")
    
    print("\n🔬 ADVANCED FUNCTIONS:")
    print("8. √ Căn bậc hai")
    print("9. 📏 Sin, Cos, Tan")
    print("10. 📊 Log, Ln")
    print("11. 🔄 Factorial")
    print("12. 📐 Geometry Calculator")
    
    print("\n💾 MEMORY & HISTORY:")
    print("13. 💾 Memory Functions")
    print("14. 📚 View History")
    print("15. 🗑️ Clear History")
    
    print("\n⚙️ UTILITIES:")
    print("16. 🔢 Number System Converter")
    print("17. 📊 Statistics Calculator")
    print("18. 🧮 Multi-step Calculator")
    print("19. ❓ Help")
    print("20. 🚪 Exit")

def get_number(prompt="Nhập số: "):
    """Lấy số từ user với error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ!")

def save_calculation(operation, operand1, operand2, result):
    """Lưu phép tính vào history"""
    timestamp = time.strftime("%H:%M:%S")
    calculation = {
        "time": timestamp,
        "operation": operation,
        "operand1": operand1,
        "operand2": operand2,
        "result": result
    }
    calculation_history.append(calculation)
    global last_result
    last_result = result

def basic_operations():
    """Các phép tính cơ bản"""
    operations = {
        1: ("+", lambda x, y: x + y, "Cộng"),
        2: ("-", lambda x, y: x - y, "Trừ"),
        3: ("*", lambda x, y: x * y, "Nhân"),
        4: ("/", lambda x, y: x / y if y != 0 else None, "Chia"),
        5: ("//", lambda x, y: x // y if y != 0 else None, "Chia lấy nguyên"),
        6: ("%", lambda x, y: x % y if y != 0 else None, "Chia lấy dư"),
        7: ("**", lambda x, y: x ** y, "Lũy thừa")
    }
    
    print("\n📊 BASIC OPERATIONS")
    for key, (symbol, func, name) in operations.items():
        print(f"{key}. {symbol} {name}")
    
    while True:
        try:
            choice = int(input("Chọn phép tính (1-7): "))
            if choice in operations:
                break
            print("❌ Chọn từ 1-7!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    symbol, func, name = operations[choice]
    
    num1 = get_number("Số thứ nhất: ")
    num2 = get_number("Số thứ hai: ")
    
    try:
        result = func(num1, num2)
        if result is None:
            print("❌ Lỗi: Không thể chia cho 0!")
            return
        
        print(f"\n✅ KẾT QUẢ: {num1} {symbol} {num2} = {result}")
        save_calculation(name, num1, num2, result)
        
    except Exception as e:
        print(f"❌ Lỗi tính toán: {e}")

def sqrt_function():
    """Căn bậc hai"""
    print("\n√ CĂNG BẬC HAI")
    num = get_number("Nhập số (≥ 0): ")
    
    if num < 0:
        print("❌ Không thể tính căn bậc hai của số âm!")
        return
    
    result = math.sqrt(num)
    print(f"✅ √{num} = {result}")
    save_calculation("Căn bậc hai", num, None, result)

def trigonometry():
    """Các hàm lượng giác"""
    print("\n📏 LƯỢNG GIÁC")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Asin (arcsin)")
    print("5. Acos (arccos)")
    print("6. Atan (arctan)")
    
    while True:
        try:
            choice = int(input("Chọn hàm (1-6): "))
            if 1 <= choice <= 6:
                break
            print("❌ Chọn từ 1-6!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    angle = get_number("Nhập góc (độ): ")
    
    # Convert to radians for calculation
    radians = math.radians(angle)
    
    try:
        if choice == 1:
            result = math.sin(radians)
            func_name = "sin"
        elif choice == 2:
            result = math.cos(radians)
            func_name = "cos"
        elif choice == 3:
            result = math.tan(radians)
            func_name = "tan"
        elif choice == 4:
            if -1 <= angle <= 1:
                result = math.degrees(math.asin(angle))
                func_name = "arcsin"
            else:
                print("❌ Arcsin chỉ nhận giá trị từ -1 đến 1!")
                return
        elif choice == 5:
            if -1 <= angle <= 1:
                result = math.degrees(math.acos(angle))
                func_name = "arccos"
            else:
                print("❌ Arccos chỉ nhận giá trị từ -1 đến 1!")
                return
        elif choice == 6:
            result = math.degrees(math.atan(angle))
            func_name = "arctan"
        
        print(f"✅ {func_name}({angle}°) = {result}")
        save_calculation(f"{func_name}", angle, None, result)
        
    except Exception as e:
        print(f"❌ Lỗi tính toán: {e}")

def logarithm():
    """Hàm logarithm"""
    print("\n📊 LOGARITHM")
    print("1. Log₁₀ (logarithm cơ số 10)")
    print("2. Ln (logarithm tự nhiên)")
    print("3. Log_n (logarithm cơ số n)")
    
    while True:
        try:
            choice = int(input("Chọn loại log (1-3): "))
            if 1 <= choice <= 3:
                break
            print("❌ Chọn từ 1-3!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    num = get_number("Nhập số (> 0): ")
    
    if num <= 0:
        print("❌ Logarithm chỉ tính được cho số dương!")
        return
    
    try:
        if choice == 1:
            result = math.log10(num)
            print(f"✅ log₁₀({num}) = {result}")
            save_calculation("log10", num, None, result)
        elif choice == 2:
            result = math.log(num)
            print(f"✅ ln({num}) = {result}")
            save_calculation("ln", num, None, result)
        elif choice == 3:
            base = get_number("Nhập cơ số (> 0, ≠ 1): ")
            if base <= 0 or base == 1:
                print("❌ Cơ số phải > 0 và ≠ 1!")
                return
            result = math.log(num, base)
            print(f"✅ log_{base}({num}) = {result}")
            save_calculation(f"log_{base}", num, None, result)
            
    except Exception as e:
        print(f"❌ Lỗi tính toán: {e}")

def factorial():
    """Giai thừa"""
    print("\n🔄 GIAI THỪA")
    num = get_number("Nhập số nguyên (≥ 0): ")
    
    if num < 0 or num != int(num):
        print("❌ Giai thừa chỉ tính cho số nguyên không âm!")
        return
    
    num = int(num)
    if num > 170:  # Giới hạn để tránh overflow
        print("❌ Số quá lớn! Giới hạn n ≤ 170")
        return
    
    result = 1
    calculation_steps = []
    
    for i in range(1, num + 1):
        result *= i
        calculation_steps.append(str(i))
    
    steps_str = " × ".join(calculation_steps) if calculation_steps else "1"
    print(f"✅ {num}! = {steps_str} = {result}")
    save_calculation("Factorial", num, None, result)

def geometry_calculator():
    """Máy tính hình học"""
    print("\n📐 GEOMETRY CALCULATOR")
    print("1. Diện tích hình vuông")
    print("2. Diện tích hình chữ nhật")
    print("3. Diện tích hình tròn")
    print("4. Diện tích tam giác")
    print("5. Chu vi hình tròn")
    print("6. Thể tích hình cầu")
    print("7. Thể tích hình hộp")
    
    while True:
        try:
            choice = int(input("Chọn (1-7): "))
            if 1 <= choice <= 7:
                break
            print("❌ Chọn từ 1-7!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    if choice == 1:
        side = get_number("Cạnh hình vuông: ")
        result = side ** 2
        print(f"✅ Diện tích = {side}² = {result}")
        save_calculation("Diện tích vuông", side, None, result)
        
    elif choice == 2:
        length = get_number("Chiều dài: ")
        width = get_number("Chiều rộng: ")
        result = length * width
        print(f"✅ Diện tích = {length} × {width} = {result}")
        save_calculation("Diện tích chữ nhật", length, width, result)
        
    elif choice == 3:
        radius = get_number("Bán kính: ")
        result = math.pi * radius ** 2
        print(f"✅ Diện tích = π × {radius}² = {result:.4f}")
        save_calculation("Diện tích tròn", radius, None, result)
        
    elif choice == 4:
        base = get_number("Đáy: ")
        height = get_number("Chiều cao: ")
        result = 0.5 * base * height
        print(f"✅ Diện tích = ½ × {base} × {height} = {result}")
        save_calculation("Diện tích tam giác", base, height, result)
        
    elif choice == 5:
        radius = get_number("Bán kính: ")
        result = 2 * math.pi * radius
        print(f"✅ Chu vi = 2π × {radius} = {result:.4f}")
        save_calculation("Chu vi tròn", radius, None, result)
        
    elif choice == 6:
        radius = get_number("Bán kính: ")
        result = (4/3) * math.pi * radius ** 3
        print(f"✅ Thể tích = ⁴⁄₃π × {radius}³ = {result:.4f}")
        save_calculation("Thể tích cầu", radius, None, result)
        
    elif choice == 7:
        length = get_number("Chiều dài: ")
        width = get_number("Chiều rộng: ")
        height = get_number("Chiều cao: ")
        result = length * width * height
        print(f"✅ Thể tích = {length} × {width} × {height} = {result}")
        save_calculation("Thể tích hộp", length, width, result)

def memory_functions():
    """Các chức năng memory"""
    global calculator_memory
    
    print(f"\n💾 MEMORY FUNCTIONS (Hiện tại: {calculator_memory})")
    print("1. MS - Memory Store")
    print("2. MR - Memory Recall")
    print("3. M+ - Memory Add")
    print("4. M- - Memory Subtract")
    print("5. MC - Memory Clear")
    
    while True:
        try:
            choice = int(input("Chọn (1-5): "))
            if 1 <= choice <= 5:
                break
            print("❌ Chọn từ 1-5!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    if choice == 1:  # Memory Store
        value = get_number("Nhập giá trị để lưu: ")
        calculator_memory = value
        print(f"✅ Đã lưu {value} vào memory")
        
    elif choice == 2:  # Memory Recall
        print(f"✅ Memory hiện tại: {calculator_memory}")
        
    elif choice == 3:  # Memory Add
        value = get_number("Nhập giá trị để cộng: ")
        calculator_memory += value
        print(f"✅ Memory = {calculator_memory - value} + {value} = {calculator_memory}")
        
    elif choice == 4:  # Memory Subtract
        value = get_number("Nhập giá trị để trừ: ")
        calculator_memory -= value
        print(f"✅ Memory = {calculator_memory + value} - {value} = {calculator_memory}")
        
    elif choice == 5:  # Memory Clear
        calculator_memory = 0
        print("✅ Đã xóa memory")

def view_history():
    """Xem lịch sử tính toán"""
    if not calculation_history:
        print("📚 Chưa có lịch sử tính toán!")
        return
    
    print(f"\n📚 LỊCH SỬ TÍNH TOÁN ({len(calculation_history)} phép tính)")
    print("=" * 60)
    
    # Hiển thị 15 phép tính gần nhất
    recent_calculations = calculation_history[-15:]
    
    for i, calc in enumerate(recent_calculations, 1):
        time_str = calc['time']
        operation = calc['operation']
        operand1 = calc['operand1']
        operand2 = calc['operand2']
        result = calc['result']
        
        if operand2 is not None:
            print(f"{i:2}. [{time_str}] {operation}: {operand1} op {operand2} = {result}")
        else:
            print(f"{i:2}. [{time_str}] {operation}({operand1}) = {result}")
    
    if len(calculation_history) > 15:
        print(f"\n... và {len(calculation_history) - 15} phép tính khác")
    
    print(f"\nKết quả cuối cùng: {last_result}")

def number_system_converter():
    """Chuyển đổi hệ số"""
    print("\n🔢 NUMBER SYSTEM CONVERTER")
    print("1. Decimal → Binary")
    print("2. Decimal → Hex")
    print("3. Binary → Decimal")
    print("4. Hex → Decimal")
    print("5. All conversions")
    
    while True:
        try:
            choice = int(input("Chọn (1-5): "))
            if 1 <= choice <= 5:
                break
            print("❌ Chọn từ 1-5!")
        except ValueError:
            print("❌ Vui lòng nhập số!")
    
    if choice == 1:
        num = int(get_number("Nhập số decimal: "))
        binary = bin(num)[2:]  # Bỏ prefix '0b'
        print(f"✅ {num} (decimal) = {binary} (binary)")
        
    elif choice == 2:
        num = int(get_number("Nhập số decimal: "))
        hex_val = hex(num)[2:].upper()  # Bỏ prefix '0x'
        print(f"✅ {num} (decimal) = {hex_val} (hex)")
        
    elif choice == 3:
        binary_str = input("Nhập số binary: ")
        try:
            decimal = int(binary_str, 2)
            print(f"✅ {binary_str} (binary) = {decimal} (decimal)")
        except ValueError:
            print("❌ Số binary không hợp lệ!")
            
    elif choice == 4:
        hex_str = input("Nhập số hex: ")
        try:
            decimal = int(hex_str, 16)
            print(f"✅ {hex_str} (hex) = {decimal} (decimal)")
        except ValueError:
            print("❌ Số hex không hợp lệ!")
            
    elif choice == 5:
        num = int(get_number("Nhập số decimal: "))
        binary = bin(num)[2:]
        hex_val = hex(num)[2:].upper()
        octal = oct(num)[2:]
        
        print(f"✅ CHUYỂN ĐỔI CỦA {num}:")
        print(f"   Binary:  {binary}")
        print(f"   Hex:     {hex_val}")
        print(f"   Octal:   {octal}")

def statistics_calculator():
    """Máy tính thống kê"""
    print("\n📊 STATISTICS CALCULATOR")
    
    numbers = []
    print("Nhập các số (nhập 'done' để kết thúc):")
    
    while True:
        user_input = input(f"Số thứ {len(numbers) + 1}: ")
        
        if user_input.lower() == 'done':
            break
            
        try:
            num = float(user_input)
            numbers.append(num)
            print(f"✅ Đã thêm {num}")
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ!")
    
    if not numbers:
        print("❌ Không có số nào để tính toán!")
        return
    
    # Tính toán các thống kê
    count = len(numbers)
    total = sum(numbers)
    mean = total / count
    sorted_nums = sorted(numbers)
    
    # Median
    if count % 2 == 0:
        median = (sorted_nums[count//2 - 1] + sorted_nums[count//2]) / 2
    else:
        median = sorted_nums[count//2]
    
    # Variance và Standard Deviation
    variance = sum((x - mean)**2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    
    print(f"\n📊 KẾT QUẢ THỐNG KÊ:")
    print(f"Số lượng: {count}")
    print(f"Tổng: {total}")
    print(f"Trung bình: {mean:.4f}")
    print(f"Median: {median}")
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Range: {max(numbers) - min(numbers)}")
    print(f"Variance: {variance:.4f}")
    print(f"Std Dev: {std_dev:.4f}")

def multi_step_calculator():
    """Máy tính nhiều bước"""
    print("\n🧮 MULTI-STEP CALCULATOR")
    print("Nhập các biểu thức để tính toán liên tiếp")
    print("Sử dụng 'ans' để tham chiếu kết quả trước đó")
    print("Nhập 'quit' để thoát")
    
    current_result = 0
    
    while True:
        expression = input(f"\nHiện tại: {current_result}\nNhập biểu thức: ")
        
        if expression.lower() == 'quit':
            break
            
        # Thay thế 'ans' bằng kết quả hiện tại
        expression = expression.replace('ans', str(current_result))
        
        try:
            # Đánh giá biểu thức an toàn
            allowed_names = {
                k: v for k, v in math.__dict__.items() 
                if not k.startswith("__")
            }
            allowed_names.update({"abs": abs, "round": round})
            
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            current_result = result
            
            print(f"✅ {expression} = {result}")
            save_calculation("Multi-step", expression, None, result)
            
        except Exception as e:
            print(f"❌ Lỗi: {e}")

def show_help():
    """Hiển thị hướng dẫn"""
    print("\n❓ HƯỚNG DẪN SỬ DỤNG")
    print("=" * 40)
    
    print("🧮 MÁY TÍNH KHOA HỌC cung cấp:")
    print("• Các phép tính cơ bản (+, -, ×, ÷)")
    print("• Hàm nâng cao (√, sin, cos, log)")
    print("• Memory functions (MS, MR, M+, M-)")
    print("• Lịch sử tính toán")
    print("• Chuyển đổi hệ số")
    print("• Tính toán thống kê")
    print("• Máy tính hình học")
    
    print("\n💡 TIPS:")
    print("• Tất cả kết quả được lưu vào history")
    print("• Sử dụng memory để lưu trữ tạm thời")
    print("• Multi-step calculator cho tính toán phức tạp")
    print("• Góc lượng giác được nhập bằng độ")
    print("• Kết quả được làm tròn hiển thị")

# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Chương trình chính"""
    print("🎉 Chào mừng đến với Máy Tính Khoa Học!")
    print("Máy tính đầy đủ tính năng với giao diện menu")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nChọn chức năng (1-20): "))
            
            if 1 <= choice <= 7:
                basic_operations()
            elif choice == 8:
                sqrt_function()
            elif choice == 9:
                trigonometry()
            elif choice == 10:
                logarithm()
            elif choice == 11:
                factorial()
            elif choice == 12:
                geometry_calculator()
            elif choice == 13:
                memory_functions()
            elif choice == 14:
                view_history()
            elif choice == 15:
                calculation_history.clear()
                print("✅ Đã xóa lịch sử!")
            elif choice == 16:
                number_system_converter()
            elif choice == 17:
                statistics_calculator()
            elif choice == 18:
                multi_step_calculator()
            elif choice == 19:
                show_help()
            elif choice == 20:
                print("\n👋 Cảm ơn bạn đã sử dụng Máy Tính Khoa Học!")
                if calculation_history:
                    print(f"📊 Bạn đã thực hiện {len(calculation_history)} phép tính")
                    print(f"🔢 Kết quả cuối: {last_result}")
                print("🎓 Dự án hoàn thành!")
                break
            else:
                print("❌ Chọn từ 1-20!")
                
        except ValueError:
            print("❌ Vui lòng nhập số!")
        except KeyboardInterrupt:
            print("\n\n👋 Tạm biệt!")
            break
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main() 