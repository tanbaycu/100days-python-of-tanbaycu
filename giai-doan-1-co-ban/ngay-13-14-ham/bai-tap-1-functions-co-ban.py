"""
🎯 BÀI TẬP 1: FUNCTIONS CƠ BẢN - NỀN TẢNG VỮNG CHẮC
Ngày 13-14: Từ đơn giản đến nâng cao, nhiều tình huống thực tế
Tác giả: Tanbaycu
"""

# 1. Viết hàm tính diện tích hình chữ nhật

def dien_tich_hcn(chieu_dai, chieu_rong):
    """Tính diện tích hình chữ nhật"""
    return chieu_dai * chieu_rong

# Test
assert dien_tich_hcn(5, 3) == 15
assert dien_tich_hcn(10, 2) == 20

# 2. Viết hàm kiểm tra số nguyên tố

def la_so_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test
assert la_so_nguyen_to(2) == True
assert la_so_nguyen_to(4) == False
assert la_so_nguyen_to(17) == True

# 3. Viết hàm đảo ngược chuỗi

def dao_nguoc_chuoi(s):
    """Đảo ngược chuỗi s"""
    return s[::-1]

# Test
assert dao_nguoc_chuoi("python") == "nohtyp"

# 4. Viết hàm tìm số lớn nhất trong list

def tim_max(lst):
    """Tìm số lớn nhất trong list"""
    if not lst:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# Test
assert tim_max([1,2,3,4,5]) == 5
assert tim_max([-1,-2,-3]) == -1

# 5. Viết hàm chuyển đổi nhiệt độ C sang F

def c_to_f(c):
    """Chuyển độ C sang độ F"""
    return c * 9/5 + 32

# Test
assert c_to_f(0) == 32
assert c_to_f(100) == 212

# 6. Viết hàm tính tổng các số lẻ trong list

def tong_le(lst):
    """Tính tổng các số lẻ trong list"""
    return sum(x for x in lst if x % 2 == 1)

# Test
assert tong_le([1,2,3,4,5]) == 9

# 7. Viết hàm kiểm tra chuỗi đối xứng (palindrome)

def la_palindrome(s):
    """Kiểm tra chuỗi đối xứng"""
    return s == s[::-1]

# Test
assert la_palindrome("madam") == True
assert la_palindrome("python") == False

# 8. Viết hàm đếm số từ trong chuỗi

def dem_tu(s):
    """Đếm số từ trong chuỗi"""
    return len(s.split())

# Test
assert dem_tu("Xin chao cac ban") == 4

# 9. Viết hàm kiểm tra năm nhuận

def la_nam_nhuan(nam):
    """Kiểm tra năm nhuận"""
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

# Test
assert la_nam_nhuan(2020) == True
assert la_nam_nhuan(1900) == False

# 10. Viết hàm tính tổng các số trong list (dùng for)

def tong_list(lst):
    """Tính tổng các số trong list"""
    tong = 0
    for x in lst:
        tong += x
    return tong

# Test
assert tong_list([1,2,3]) == 6

# 11. Viết hàm kiểm tra số hoàn hảo

def la_so_hoan_hao(n):
    """Kiểm tra số hoàn hảo"""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Test
assert la_so_hoan_hao(6) == True
assert la_so_hoan_hao(28) == True
assert la_so_hoan_hao(10) == False

# 12. Viết hàm chuyển đổi số thành chữ (0-9)

def so_thanh_chu(n):
    """Chuyển số 0-9 thành chữ tiếng Việt"""
    chu = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    if 0 <= n <= 9:
        return chu[n]
    return "không hợp lệ"

# Test
assert so_thanh_chu(5) == "năm"
assert so_thanh_chu(10) == "không hợp lệ"

# 13. Viết hàm kiểm tra email hợp lệ

def la_email(email):
    """Kiểm tra email hợp lệ"""
    return "@" in email and "." in email

# Test
assert la_email("abc@gmail.com") == True
assert la_email("abcgmail.com") == False

# 14. Viết hàm tính giai thừa (không dùng recursion)

def giai_thua(n):
    """Tính giai thừa n!"""
    if n < 0:
        return None
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt

# Test
assert giai_thua(5) == 120

# 15. Viết hàm kiểm tra số hoàn chỉnh (perfect square)

def la_so_chinh_phuong(n):
    """Kiểm tra số chính phương"""
    return int(n**0.5)**2 == n

# Test
assert la_so_chinh_phuong(9) == True
assert la_so_chinh_phuong(8) == False

# 16. Viết hàm tìm số nhỏ nhất trong list

def tim_min(lst):
    """Tìm số nhỏ nhất trong list"""
    if not lst:
        return None
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

# Test
assert tim_min([1,2,3,-1]) == -1

# 17. Viết hàm kiểm tra số âm hay dương

def am_hay_duong(n):
    """Kiểm tra số âm, dương hay 0"""
    if n > 0:
        return "dương"
    elif n < 0:
        return "âm"
    else:
        return "không"

# Test
assert am_hay_duong(5) == "dương"
assert am_hay_duong(-3) == "âm"
assert am_hay_duong(0) == "không"

# 18. Viết hàm kiểm tra số chẵn lẻ

def chan_le(n):
    """Kiểm tra số chẵn hay lẻ"""
    return "chẵn" if n % 2 == 0 else "lẻ"

# Test
assert chan_le(4) == "chẵn"
assert chan_le(5) == "lẻ"

# 19. Viết hàm tính tổng các số chia hết cho 3 trong list

def tong_chia_het_3(lst):
    """Tính tổng các số chia hết cho 3"""
    return sum(x for x in lst if x % 3 == 0)

# Test
assert tong_chia_het_3([3,6,7,8,9]) == 18

# 20. Viết hàm kiểm tra chuỗi có phải số (isnumeric)

def la_so(s):
    """Kiểm tra chuỗi là số"""
    return s.isdigit()

# Test
assert la_so("123") == True
assert la_so("abc") == False

print("✅ Đã kiểm tra xong 20 bài tập cơ bản Functions!") 