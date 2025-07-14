# Ngày 3-4: Biến, Số Học và String

## Mục Tiêu Học Tập

Sau 2 ngày này, bạn sẽ:

### Kiến Thức Cốt Lõi
- **Biến (Variables)**: Hiểu cách tạo, gán và sử dụng biến
- **Kiểu Dữ Liệu**: int, float, string, boolean
- **Số Học**: Các phép toán cơ bản (+, -, *, /, //, %, **)
- **String**: Tạo, nối, format string cơ bản
- **Type Conversion**: Chuyển đổi kiểu dữ liệu

### Kỹ Năng Thực Hành
- Khai báo và sử dụng biến hiệu quả
- Thực hiện tính toán với số nguyên và số thực
- Xử lý chuỗi ký tự cơ bản
- Debug lỗi kiểu dữ liệu

## Nội Dung Học Tập

### 📖 Lý Thuyết
- `1-ly-thuyet-bien-va-kieu-du-lieu.md` - Concepts cơ bản về biến
- `2-phep-toan-so-hoc.md` - Các phép toán số học
- `3-xu-ly-string.md` - Làm việc với chuỗi

### 💻 Bài Tập Thực Hành
- `bai-tap-1-bien-co-ban.py` - Khai báo và sử dụng biến
- `bai-tap-2-so-hoc.py` - Tính toán với số
- `bai-tap-3-string.py` - Xử lý chuỗi
- `bai-tap-4-chuyen-doi-kieu.py` - Type conversion

### 📋 File Cần Nộp
- `may_tinh_nang_cao.py` - Máy tính với nhiều phép toán
- `thong_tin_chi_tiet.py` - Form thông tin với validation
- `trinh_bay_ban_than.py` - Giới thiệu bản thân định dạng đẹp

### 🏆 Thử Thách
- `thu-thach-ngay-3-4.py` - Bài tập tổng hợp
- `mini-game-doan-so.py` - Game đoán số với hints

## Tiến Độ Học Tập

### Ngày 3: Biến và Số Học
- [ ] Đọc lý thuyết về biến
- [ ] Hoàn thành bài tập biến cơ bản  
- [ ] Đọc lý thuyết phép toán
- [ ] Hoàn thành bài tập số học
- [ ] Tạo file `may_tinh_nang_cao.py`

### Ngày 4: String và Tổng Hợp
- [ ] Đọc lý thuyết string
- [ ] Hoàn thành bài tập string
- [ ] Học type conversion
- [ ] Tạo file `thong_tin_chi_tiet.py`
- [ ] Tạo file `trinh_bay_ban_than.py`
- [ ] Hoàn thành thử thách

## Đánh Giá Kỹ Năng

### Level 1 - Cơ Bản (50-60 điểm)
- Tạo được biến với tên hợp lệ
- Thực hiện phép cộng, trừ, nhân, chia
- Nối được 2 string đơn giản

### Level 2 - Khá (60-70 điểm)
- Sử dụng nhiều kiểu dữ liệu
- Thực hiện tất cả phép toán
- Format string với f-string

### Level 3 - Giỏi (70-80 điểm)
- Kết hợp biến và tính toán phức tạp
- Xử lý string nâng cao
- Debug lỗi type

### Level 4 - Xuất Sắc (80-90 điểm)
- Tối ưu code với biến
- Validation input
- Code sạch, dễ đọc

### Level 5 - Chuyên Nghiệp (90-100 điểm)
- Best practices đặt tên biến
- Error handling cơ bản
- Documentation code

## Kiến Thức Cần Nhớ

### Variables Best Practices
```python
# Tốt
ten_nguoi_dung = "An"
tuoi = 25
diem_trung_binh = 8.5

# Tránh
a = "An"  # Tên không rõ nghĩa
2name = "An"  # Bắt đầu bằng số
ten-nguoi = "An"  # Dấu gạch ngang
```

### Phép Toán Quan Trọng
```python
# Phép toán cơ bản
a + b    # Cộng
a - b    # Trừ
a * b    # Nhân
a / b    # Chia (float)
a // b   # Chia lấy phần nguyên
a % b    # Chia lấy dư
a ** b   # Lũy thừa
```

### String Methods Cơ Bản
```python
text = "Hello World"
text.upper()     # "HELLO WORLD"
text.lower()     # "hello world"
text.title()     # "Hello World"
len(text)        # 11
text.replace("World", "Python")  # "Hello Python"
```

## Lỗi Thường Gặp

1. **NameError**: Sử dụng biến chưa khai báo
2. **TypeError**: Cộng string với số
3. **ValueError**: Convert string không phải số
4. **SyntaxError**: Tên biến không hợp lệ

## Chuẩn Bị Cho Ngày 5-6

- Hiểu rõ boolean (True/False)
- Biết so sánh (==, !=, <, >, <=, >=)
- Thành thạo việc lấy input từ user

---

**Lưu ý**: Hoàn thành tất cả bài tập cơ bản trước khi làm thử thách! 