# Ngày 5-6: Điều Kiện If/Else

## Mục Tiêu Học Tập

Sau 2 ngày này, bạn sẽ:

### Kiến Thức Cốt Lõi
- **Câu lệnh điều kiện**: if, elif, else
- **Toán tử so sánh**: ==, !=, <, >, <=, >=
- **Toán tử logic**: and, or, not
- **Boolean**: True/False và truthiness
- **Nested conditions**: if lồng nhau

### Kỹ Năng Thực Hành
- Viết logic rẽ nhánh đơn giản và phức tạp
- Kết hợp nhiều điều kiện
- Xử lý input và validation
- Tạo menu và hệ thống lựa chọn

## Nội Dung Học Tập

### 📖 Lý Thuyết
- `1-dieu-kien-if-else.md` - Cơ bản về if/else
- `2-toan-tu-so-sanh-va-logic.md` - Operators và boolean
- `3-dieu-kien-phuc-tap.md` - Nested if và best practices

### 💻 Bài Tập Thực Hành
- `bai-tap-1-if-else-co-ban.py` - Điều kiện đơn giản
- `bai-tap-2-toan-tu-so-sanh.py` - So sánh và logic
- `bai-tap-3-dieu-kien-phuc-tap.py` - If lồng nhau
- `bai-tap-4-menu-lua-chon.py` - Tạo menu interactive

### 📋 File Cần Nộp
- `kiem_tra_diem.py` - Hệ thống phân loại điểm
- `may_tinh_co_menu.py` - Máy tính với menu lựa chọn
- `game_doan_so_nang_cao.py` - Game đoán số với hints

### 🏆 Thử Thách
- `thu-thach-ngay-5-6.py` - Bài tập tổng hợp
- `he-thong-dang-nhap.py` - Login system đơn giản

## Tiến Độ Học Tập

### Ngày 5: If/Else Cơ Bản
- [ ] Đọc lý thuyết điều kiện
- [ ] Hoàn thành bài tập if/else cơ bản
- [ ] Đọc lý thuyết toán tử
- [ ] Hoàn thành bài tập so sánh
- [ ] Tạo file `kiem_tra_diem.py`

### Ngày 6: Điều Kiện Phức Tạp
- [ ] Đọc lý thuyết điều kiện phức tạp
- [ ] Hoàn thành bài tập nested if
- [ ] Tạo menu và system
- [ ] Tạo file `may_tinh_co_menu.py`
- [ ] Tạo file `game_doan_so_nang_cao.py`
- [ ] Hoàn thành thử thách

## Đánh Giá Kỹ Năng

### Level 1 - Cơ Bản (50-60 điểm)
- Viết được if/else đơn giản
- Sử dụng toán tử so sánh cơ bản
- Xử lý 2-3 trường hợp

### Level 2 - Khá (60-70 điểm)
- Kết hợp nhiều điều kiện với and/or
- Sử dụng elif hiệu quả
- Validation input cơ bản

### Level 3 - Giỏi (70-80 điểm)
- If lồng nhau hợp lý
- Logic phức tạp nhưng clear
- Handle edge cases

### Level 4 - Xuất Sắc (80-90 điểm)
- Code clean và DRY
- Error handling tốt
- UX friendly

### Level 5 - Chuyên Nghiệp (90-100 điểm)
- Optimize performance
- Maintainable code
- Professional logic flow

## Kiến Thức Cần Nhớ

### Cú Pháp If/Else
```python
if condition:
    # code khi đúng
elif another_condition:
    # code khi điều kiện khác đúng
else:
    # code khi tất cả sai
```

### Toán Tử So Sánh
```python
a == b    # Bằng
a != b    # Khác
a < b     # Nhỏ hơn
a > b     # Lớn hơn
a <= b    # Nhỏ hơn hoặc bằng
a >= b    # Lớn hơn hoặc bằng
```

### Toán Tử Logic
```python
and    # Cả hai đều đúng
or     # Ít nhất một đúng
not    # Đảo ngược boolean
```

### Truthiness trong Python
```python
# Falsy values
False, 0, 0.0, "", [], {}, None

# Truthy values
True, bất kỳ số khác 0, string không rỗng, list/dict có phần tử
```

## Pattern Thường Dùng

### 1. Validation Input
```python
tuoi = int(input("Tuổi: "))
if 0 <= tuoi <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")
```

### 2. Menu System
```python
lua_chon = input("Chọn (1/2/3): ")
if lua_chon == "1":
    print("Tùy chọn 1")
elif lua_chon == "2":
    print("Tùy chọn 2")
elif lua_chon == "3":
    print("Tùy chọn 3")
else:
    print("Lựa chọn không hợp lệ")
```

### 3. Range Checking
```python
if diem >= 8.5:
    loai = "Giỏi"
elif diem >= 7.0:
    loai = "Khá"
elif diem >= 5.0:
    loai = "Trung bình"
else:
    loai = "Yếu"
```

## Lỗi Thường Gặp

1. **Quên dấu hai chấm (:)**
2. **Indentation sai**
3. **Dùng = thay vì ==**
4. **Logic sai thứ tự điều kiện**
5. **Không handle edge case**

## Best Practices

1. **Điều kiện đơn giản trước**
2. **Tránh quá nhiều nested if**
3. **Sử dụng elif thay vì if liên tiếp**
4. **Comment cho logic phức tạp**
5. **Test tất cả trường hợp**

## Chuẩn Bị Cho Ngày 7-8

- Hiểu rõ loops concept
- Thành thạo range() function
- Biết break và continue
- Nested structure thinking

---

**Lưu ý**: Điều kiện là nền tảng của logic programming. Hãy practice nhiều! 