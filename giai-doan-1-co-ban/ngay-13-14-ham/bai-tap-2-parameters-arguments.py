"""
🎯 BÀI TẬP 2: PARAMETERS & ARGUMENTS - LINH HOẠT VÀ ỨNG DỤNG
Ngày 13-14: Đa dạng tình huống, test case, giải thích chi tiết
Tác giả: Tanbaycu
"""

# 1. Viết hàm nhận vào nhiều số bất kỳ, trả về tổng các số lẻ

def tong_le(*args):
    """Tính tổng các số lẻ từ *args"""
    return sum(x for x in args if x % 2 == 1)

# Test
assert tong_le(1,2,3,4,5) == 9
assert tong_le(2,4,6) == 0

# 2. Viết hàm nhận vào list và nhiều hàm xử lý, áp dụng lần lượt các hàm đó lên list

def xu_ly_da_ham(lst, *funcs):
    """Áp dụng nhiều hàm xử lý lên list"""
    for f in funcs:
        lst = f(lst)
    return lst

# Test
lst = [1,2,3]
def nhan2(x): return [i*2 for i in x]
def cong1(x): return [i+1 for i in x]
assert xu_ly_da_ham(lst, nhan2, cong1) == [3,5,7]

# 3. Viết hàm nhận vào **kwargs, trả về dict chỉ chứa các key có giá trị là số chẵn

def loc_chan(**kwargs):
    """Trả về dict chỉ chứa key có value là số chẵn"""
    return {k:v for k,v in kwargs.items() if isinstance(v,int) and v%2==0}

# Test
assert loc_chan(a=1, b=2, c=3, d=4) == {'b':2,'d':4}

# 4. Viết hàm validate form với các trường động và điều kiện kiểm tra

def validate_form(data, *required, **validators):
    """Kiểm tra các trường required và validate từng trường"""
    for field in required:
        if field not in data:
            return False, f"Thiếu trường {field}"
    for field, func in validators.items():
        if field in data and not func(data[field]):
            return False, f"Trường {field} không hợp lệ"
    return True, "Hợp lệ"

# Test
user = {'name':'An','age':20,'email':'an@gmail.com'}
assert validate_form(user, 'name','age','email', age=lambda x:x>=18, email=lambda x:'@' in x)[0] == True
user2 = {'name':'B','age':15,'email':'b@gmail.com'}
assert validate_form(user2, 'name','age','email', age=lambda x:x>=18)[0] == False

# 5. Viết hàm nhận vào n số, trả về tuple (min, max, average)

def thong_ke(*args):
    """Trả về (min, max, average) của các số"""
    if not args:
        return None, None, None
    return min(args), max(args), sum(args)/len(args)

# Test
assert thong_ke(1,2,3,4,5) == (1,5,3.0)

# 6. Viết hàm nhận vào list và function, trả về list sau khi áp dụng function cho từng phần tử

def ap_dung(lst, func):
    """Áp dụng func cho từng phần tử trong list"""
    return [func(x) for x in lst]

# Test
assert ap_dung([1,2,3], lambda x: x*3) == [3,6,9]

# 7. Viết hàm nhận vào nhiều list, trả về list ghép nối tất cả

def ghep_noi(*lists):
    """Ghép nối nhiều list"""
    result = []
    for l in lists:
        result.extend(l)
    return result

# Test
assert ghep_noi([1,2],[3,4],[5]) == [1,2,3,4,5]

# 8. Viết hàm nhận vào dict và nhiều key, trả về dict chỉ chứa các key đó

def loc_keys(d, *keys):
    """Lọc dict chỉ giữ các key chỉ định"""
    return {k:d[k] for k in keys if k in d}

# Test
d = {'a':1,'b':2,'c':3}
assert loc_keys(d, 'a','c') == {'a':1,'c':3}

# 9. Viết hàm nhận vào list và function, trả về True nếu tất cả phần tử thỏa mãn điều kiện

def tat_ca(lst, func):
    """Kiểm tra tất cả phần tử thỏa mãn func"""
    return all(func(x) for x in lst)

# Test
assert tat_ca([2,4,6], lambda x:x%2==0) == True

# 10. Viết hàm nhận vào list và function, trả về số lượng phần tử thỏa mãn điều kiện

def dem_dieu_kien(lst, func):
    """Đếm số phần tử thỏa mãn func"""
    return sum(1 for x in lst if func(x))

# Test
assert dem_dieu_kien([1,2,3,4,5], lambda x:x>2) == 3

print("✅ Đã kiểm tra xong 10 bài tập Parameters & Arguments!") 