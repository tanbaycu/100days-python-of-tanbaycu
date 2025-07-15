"""
🎯 DỰ ÁN THỰC HÀNH NÂNG CAO - FUNCTIONS MASTER PROJECTS
Ngày 13-14: 3 dự án lớn, code sạch, nhiều function, test case, giải thích
Tác giả: Tanbaycu
"""

# 1. Library Management System (Quản lý thư viện nâng cao)

def create_book(title, author, year, genre):
    return {'title': title, 'author': author, 'year': year, 'genre': genre, 'available': True}

def add_book(library, book):
    library.append(book)
    return library

def search_books(library, keyword):
    return [b for b in library if keyword.lower() in b['title'].lower() or keyword.lower() in b['author'].lower()]

def borrow_book(library, title):
    for b in library:
        if b['title'].lower() == title.lower() and b['available']:
            b['available'] = False
            return True
    return False

def return_book(library, title):
    for b in library:
        if b['title'].lower() == title.lower() and not b['available']:
            b['available'] = True
            return True
    return False

# Test
lib = []
add_book(lib, create_book("Python 101", "Tanbaycu", 2022, "Programming"))
add_book(lib, create_book("AI Cơ Bản", "Nguyễn Văn A", 2021, "AI"))
assert len(search_books(lib, "python")) == 1
assert borrow_book(lib, "Python 101") == True
assert borrow_book(lib, "Python 101") == False
assert return_book(lib, "Python 101") == True

# 2. Data Analysis Toolkit (Bộ công cụ phân tích dữ liệu)

def mean(lst):
    return sum(lst)/len(lst) if lst else 0

def median(lst):
    s = sorted(lst)
    n = len(s)
    if n == 0:
        return 0
    if n % 2 == 1:
        return s[n//2]
    return (s[n//2-1] + s[n//2])/2

def mode(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x,0)+1
    max_freq = max(freq.values())
    return [k for k,v in freq.items() if v==max_freq]

def describe(lst):
    return {
        'mean': mean(lst),
        'median': median(lst),
        'mode': mode(lst),
        'min': min(lst) if lst else None,
        'max': max(lst) if lst else None,
        'count': len(lst)
    }

# Test
data = [1,2,2,3,4,4,4,5]
stat = describe(data)
assert stat['mean'] == sum(data)/len(data)
assert stat['median'] == 3.0
assert stat['mode'] == [4]

# 3. Text Processing System (Hệ thống xử lý văn bản)

def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text.replace(' ','').replace('\n',''))

def most_common_word(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0)+1
    max_freq = max(freq.values())
    return [k for k,v in freq.items() if v==max_freq]

def summary(text):
    return {
        'words': word_count(text),
        'chars': char_count(text),
        'most_common': most_common_word(text)
    }

# Test
sample = "python code python ai code code"
sumr = summary(sample)
assert sumr['words'] == 6
assert sumr['chars'] == 24
assert sumr['most_common'] == ['code']

print("✅ Đã kiểm tra xong 3 dự án Functions nâng cao!") 