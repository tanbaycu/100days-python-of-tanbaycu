"""
🎯 QUIZ TỔNG HỢP NGÀY 13-14: FUNCTIONS
20 câu trắc nghiệm, 5 coding, 4 mức độ, tự động chấm điểm, giải thích đáp án
Tác giả: Tanbaycu
"""

import random

# =====================
# 1. Câu hỏi trắc nghiệm
# =====================
quiz_mc = [
    {
        'q': 'Hàm nào trả về tổng các phần tử trong list?',
        'a': ['sum(lst)', 'add(lst)', 'total(lst)', 'plus(lst)'],
        'correct': 0,
        'explain': 'sum(lst) là hàm tích hợp của Python.'
    },
    {
        'q': 'Kết quả của def f(x=2): return x*3; f(4) là?',
        'a': ['6', '8', '12', '14'],
        'correct': 2,
        'explain': 'f(4) = 4*3 = 12.'
    },
    {
        'q': 'Tham số nào cho phép truyền số lượng đối số không giới hạn?',
        'a': ['*args', '**kwargs', 'default', 'optional'],
        'correct': 0,
        'explain': '*args gom các đối số thành tuple.'
    },
    {
        'q': 'Hàm lambda nào đúng để kiểm tra số lẻ?',
        'a': ['lambda x: x%2==1', 'lambda x: x%2==0', 'lambda x: x>0', 'lambda x: x<0'],
        'correct': 0,
        'explain': 'x%2==1 kiểm tra số lẻ.'
    },
    {
        'q': 'Kết quả của list(map(lambda x: x+1, [1,2,3]))?',
        'a': ['[2,3,4]', '[1,2,3]', '[0,1,2]', '[3,4,5]'],
        'correct': 0,
        'explain': 'Tăng mỗi phần tử lên 1.'
    },
    {
        'q': 'Hàm nào trả về True nếu tất cả phần tử đều thỏa mãn điều kiện?',
        'a': ['all()', 'any()', 'sum()', 'filter()'],
        'correct': 0,
        'explain': 'all() kiểm tra tất cả True.'
    },
    {
        'q': 'Kết quả của def f(a,b=2): return a+b; f(3)?',
        'a': ['5', '3', '2', 'None'],
        'correct': 0,
        'explain': 'f(3) = 3+2 = 5.'
    },
    {
        'q': 'Hàm nào dùng để tạo generator?',
        'a': ['yield', 'return', 'break', 'continue'],
        'correct': 0,
        'explain': 'yield tạo generator.'
    },
    {
        'q': 'Kết quả của def f(): return 1,2; x,y = f(); x=?',
        'a': ['1', '2', '(1,2)', 'None'],
        'correct': 0,
        'explain': 'f() trả về tuple (1,2), x=1.'
    },
    {
        'q': 'Hàm nào dùng để kiểm tra biến trong scope toàn cục?',
        'a': ['global', 'nonlocal', 'local', 'static'],
        'correct': 0,
        'explain': 'global dùng để khai báo biến toàn cục.'
    },
    # 10 câu tiếp theo
    {
        'q': 'Kết quả của def f(lst): lst.append(1); return lst; f([])?',
        'a': ['[1]', '[]', '[0,1]', '[1,1]'],
        'correct': 0,
        'explain': 'append(1) vào list rỗng.'
    },
    {
        'q': 'Hàm nào trả về phần tử lớn nhất trong list?',
        'a': ['max(lst)', 'min(lst)', 'sum(lst)', 'len(lst)'],
        'correct': 0,
        'explain': 'max(lst) trả về phần tử lớn nhất.'
    },
    {
        'q': 'Kết quả của def f(x): return x if x>0 else -x; f(-3)?',
        'a': ['3', '-3', '0', 'None'],
        'correct': 0,
        'explain': 'f(-3) trả về 3 (giá trị tuyệt đối).'
    },
    {
        'q': 'Hàm nào trả về số lượng phần tử trong list?',
        'a': ['len(lst)', 'sum(lst)', 'count(lst)', 'size(lst)'],
        'correct': 0,
        'explain': 'len(lst) trả về số lượng phần tử.'
    },
    {
        'q': 'Kết quả của def f(*args): return sum(args); f(1,2,3)?',
        'a': ['6', '3', '1', 'None'],
        'correct': 0,
        'explain': 'sum(1,2,3) = 6.'
    },
    {
        'q': 'Hàm nào dùng để kiểm tra số nguyên tố?',
        'a': ['is_prime()', 'prime()', 'la_so_nguyen_to()', 'check_prime()'],
        'correct': 2,
        'explain': 'la_so_nguyen_to là hàm kiểm tra số nguyên tố.'
    },
    {
        'q': 'Kết quả của def f(x): return x*2; f(f(2))?',
        'a': ['8', '4', '2', '6'],
        'correct': 0,
        'explain': 'f(2)=4, f(4)=8.'
    },
    {
        'q': 'Hàm nào trả về True nếu ít nhất 1 phần tử thỏa mãn?',
        'a': ['any()', 'all()', 'sum()', 'filter()'],
        'correct': 0,
        'explain': 'any() kiểm tra ít nhất 1 True.'
    },
    {
        'q': 'Kết quả của def f(x): return x+1; list(map(f, [1,2]))?',
        'a': ['[2,3]', '[1,2]', '[0,1]', '[3,4]'],
        'correct': 0,
        'explain': 'Tăng mỗi phần tử lên 1.'
    },
    {
        'q': 'Hàm nào dùng để kiểm tra chuỗi là số?',
        'a': ['isnumeric()', 'isdigit()', 'la_so()', 'isnumber()'],
        'correct': 2,
        'explain': 'la_so là hàm kiểm tra chuỗi là số.'
    },
]

# =====================
# 2. Coding Quiz
# =====================
coding_quiz = [
    {
        'q': 'Viết hàm kiểm tra số hoàn hảo.',
        'test': lambda f: f(6) == True and f(10) == False,
        'explain': 'Số hoàn hảo là tổng các ước nhỏ hơn nó bằng chính nó.'
    },
    {
        'q': 'Viết hàm đảo ngược chuỗi.',
        'test': lambda f: f("python") == "nohtyp",
        'explain': 'Sử dụng slicing: s[::-1]'
    },
    {
        'q': 'Viết hàm tính tổng các số lẻ trong list.',
        'test': lambda f: f([1,2,3,4,5]) == 9,
        'explain': 'Duyệt list, cộng các số lẻ.'
    },
    {
        'q': 'Viết hàm kiểm tra email hợp lệ.',
        'test': lambda f: f("abc@gmail.com") == True and f("abcgmail.com") == False,
        'explain': 'Kiểm tra có @ và . trong chuỗi.'
    },
    {
        'q': 'Viết hàm tính giai thừa (không dùng recursion).',
        'test': lambda f: f(5) == 120,
        'explain': 'Dùng vòng lặp for.'
    },
]

# =====================
# 3. Giao diện Quiz
# =====================
def run_quiz():
    print("\n🎯 QUIZ TỔNG HỢP NGÀY 13-14: FUNCTIONS")
    print("="*50)
    score = 0
    # Trắc nghiệm
    for i, q in enumerate(quiz_mc, 1):
        print(f"\nCâu {i}: {q['q']}")
        for idx, ans in enumerate(q['a']):
            print(f"  {idx+1}. {ans}")
        try:
            user = int(input("Đáp án của bạn (1-4): "))-1
        except:
            user = -1
        if user == q['correct']:
            print("✅ Đúng!", q['explain'])
            score += 1
        else:
            print(f"❌ Sai! Đáp án đúng: {q['a'][q['correct']]} - {q['explain']}")
    # Coding
    print("\n=== PHẦN CODING ===")
    for i, q in enumerate(coding_quiz, 1):
        print(f"\nCâu {i+len(quiz_mc)}: {q['q']}")
        print("(Bạn tự code và kiểm tra với test case)")
        print(f"Giải thích: {q['explain']}")
    print(f"\n🏆 Tổng điểm trắc nghiệm: {score}/{len(quiz_mc)}")
    print("(Phần coding tự kiểm tra)")
    if score >= 18:
        print("🌟 Xuất sắc! Bạn đã thành thạo Functions!")
    elif score >= 15:
        print("👍 Tốt! Bạn đã hiểu rõ Functions!")
    elif score >= 10:
        print("📈 Cần luyện thêm!")
    else:
        print("💪 Hãy ôn lại lý thuyết và thực hành!")

if __name__ == "__main__":
    run_quiz() 