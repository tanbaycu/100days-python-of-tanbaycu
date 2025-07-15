"""
🎯 BÀI TẬP 3: ADVANCED FUNCTIONS - CHUYÊN SÂU & ỨNG DỤNG
Ngày 13-14: Lambda, higher-order, decorator, generator, recursion, functional programming
Tác giả: Tanbaycu
"""

# 1. Viết hàm lambda tính bình phương một số
binh_phuong = lambda x: x**2
assert binh_phuong(5) == 25

# 2. Viết hàm lambda kiểm tra số chẵn
la_chan = lambda x: x%2==0
assert la_chan(4) == True
assert la_chan(5) == False

# 3. Viết higher-order function nhận 1 hàm và 1 list, trả về list sau khi áp dụng hàm đó

def ap_dung_func(func, lst):
    """Áp dụng func cho từng phần tử trong lst"""
    return [func(x) for x in lst]

assert ap_dung_func(lambda x: x+1, [1,2,3]) == [2,3,4]

# 4. Viết decorator log thời gian chạy của hàm
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Thời gian chạy: {end-start:.4f}s")
        return result
    return wrapper

@timing
def slow_sum(n):
    time.sleep(0.5)
    return sum(range(n))

assert slow_sum(10) == 45

# 5. Viết generator sinh dãy số nguyên tố vô hạn

def prime_generator():
    """Generator sinh số nguyên tố vô hạn"""
    n = 2
    while True:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

gen = prime_generator()
primes = [next(gen) for _ in range(5)]
assert primes == [2,3,5,7,11]

# 6. Viết hàm đệ quy tính tổng các số trong list lồng nhau

def tong_de_quy(lst):
    """Tính tổng các số trong list lồng nhau"""
    total = 0
    for x in lst:
        if isinstance(x, list):
            total += tong_de_quy(x)
        else:
            total += x
    return total

assert tong_de_quy([1,2,[3,4,[5]],6]) == 21

# 7. Viết closure tạo bộ đếm tăng dần

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
assert c() == 1
assert c() == 2

# 8. Viết hàm sử dụng map/filter/reduce để xử lý list số
from functools import reduce

def xu_ly_list(lst):
    """Trả về tổng bình phương các số chẵn trong lst"""
    return reduce(lambda a,b: a+b, map(lambda x: x**2, filter(lambda x: x%2==0, lst)), 0)

assert xu_ly_list([1,2,3,4]) == 20

# 9. Viết decorator kiểm tra quyền admin

def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_admin'):
            print("Truy cập bị từ chối!")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def xoa_user(user, user_id):
    return f"Đã xóa user {user_id}"

admin = {'name':'An','is_admin':True}
user = {'name':'Bình','is_admin':False}
assert xoa_user(admin, 123) == "Đã xóa user 123"
assert xoa_user(user, 456) == None

# 10. Viết generator đọc từng dòng của file (giả lập)

def fake_file_reader(lines):
    for line in lines:
        yield line.strip()

lines = ["  hello  ", " world ", "python  "]
assert list(fake_file_reader(lines)) == ["hello","world","python"]

print("✅ Đã kiểm tra xong 10 bài tập Advanced Functions!") 