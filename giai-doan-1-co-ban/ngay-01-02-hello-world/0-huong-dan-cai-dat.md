# Hướng Dẫn Cài Đặt Python & VS Code - Bước Đầu Tiên

## Bước 1: Cài Đặt Python

### Windows
1. **Truy cập trang web chính thức**: https://python.org
2. **Download Python**: Click vào nút "Download Python 3.11.x" (phiên bản mới nhất)
3. **Chạy file cài đặt**:
   - ✅ **QUAN TRỌNG**: Tick vào "Add Python to PATH"
   - Click "Install Now"
   - Đợi quá trình cài đặt hoàn tất

### macOS
1. **Truy cập**: https://python.org
2. **Download**: Chọn phiên bản cho macOS
3. **Cài đặt**: Mở file .pkg và làm theo hướng dẫn

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Kiểm Tra Cài Đặt
Mở **Command Prompt** (Windows) hoặc **Terminal** (Mac/Linux):
```bash
python --version
# Hoặc
python3 --version
```
**Kết quả mong đợi**: `Python 3.11.x`

## Bước 2: Cài Đặt VS Code

### Download VS Code
1. **Truy cập**: https://code.visualstudio.com
2. **Download**: Chọn phiên bản cho hệ điều hành của bạn
3. **Cài đặt**: Chạy file cài đặt và làm theo hướng dẫn

### Cài Đặt Extension Python
1. **Mở VS Code**
2. **Mở Extensions**: `Ctrl+Shift+X` (Windows) hoặc `Cmd+Shift+X` (Mac)
3. **Tìm kiếm**: "Python"
4. **Cài đặt**: Extension "Python" của Microsoft (có hàng triệu lượt tải)

### Extensions Khuyên Dùng
```
1. Python (Microsoft) - Bắt buộc
2. Python Docstring Generator - Tự động tạo docstring
3. Bracket Pair Colorizer - Màu sắc cho dấu ngoặc
4. Material Icon Theme - Icon đẹp cho file
5. GitLens - Git integration
```

## Bước 3: Tạo Workspace Đầu Tiên

### Tạo Thư Mục Học Tập
```bash
# Windows
mkdir C:\python-learning
cd C:\python-learning

# Mac/Linux
mkdir ~/python-learning
cd ~/python-learning
```

### Mở Trong VS Code
1. **Mở VS Code**
2. **File** → **Open Folder**
3. **Chọn thư mục** `python-learning` vừa tạo

## Bước 4: Tạo File Python Đầu Tiên

### Tạo File Mới
1. **Click chuột phải** trong VS Code Explorer
2. **New File** → Đặt tên `hello.py`

### Viết Code Đầu Tiên
```python
print("Hello World!")
print("Chào mừng đến với Python!")
```

### Chạy Code
**Cách 1**: Click vào nút ▶️ (Run Python File) ở góc trên bên phải

**Cách 2**: Mở Terminal trong VS Code
- `Ctrl+`` (backtick) để mở terminal
- Gõ: `python hello.py`

**Kết quả mong đợi**:
```
Hello World!
Chào mừng đến với Python!
```

## Xử Lý Lỗi Thường Gặp

### Lỗi 1: "python" is not recognized
**Nguyên nhân**: Python chưa được thêm vào PATH

**Giải pháp**:
1. **Windows**: Cài lại Python và nhớ tick "Add Python to PATH"
2. **Manual fix**: Thêm Python vào PATH:
   - Tìm đường dẫn Python (thường là `C:\Users\[Username]\AppData\Local\Programs\Python\Python311\`)
   - Thêm vào Environment Variables

### Lỗi 2: VS Code không nhận diện Python
**Kiểm tra Python Interpreter**:
1. `Ctrl+Shift+P` → gõ "Python: Select Interpreter"
2. Chọn phiên bản Python đã cài

### Lỗi 3: Terminal không hoạt động
**Windows**: Thay đổi default terminal:
1. `Ctrl+Shift+P` → "Terminal: Select Default Profile"
2. Chọn "Command Prompt" hoặc "PowerShell"

## Thiết Lập Tùy Chọn VS Code

### Settings.json Khuyến Nghị
1. `Ctrl+Shift+P` → "Preferences: Open Settings (JSON)"
2. Thêm cấu hình:

```json
{
    "python.defaultInterpreterPath": "python",
    "python.terminal.activateEnvironment": true,
    "editor.fontSize": 14,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "terminal.integrated.fontSize": 12
}
```

## Shortcuts Quan Trọng

### VS Code Shortcuts
```
Ctrl+S          - Lưu file
Ctrl+N          - File mới
Ctrl+`          - Mở/đóng terminal
Ctrl+Shift+P    - Command Palette
F5              - Chạy code (debug mode)
Ctrl+F5         - Chạy code (không debug)
```

### Python Interactive
1. `Ctrl+Shift+P` → "Python: Start REPL"
2. Gõ code trực tiếp và nhận kết quả ngay

## Kiểm Tra Hoàn Tất

### Checklist Cài Đặt
- [ ] Python đã cài và chạy được lệnh `python --version`
- [ ] VS Code đã cài và mở được
- [ ] Extension Python đã cài đặt
- [ ] Tạo được file .py và chạy được
- [ ] Terminal trong VS Code hoạt động
- [ ] Có thể chạy code bằng nút Run

### Test Cuối Cùng
Tạo file `test.py`:
```python
import sys
print(f"Python version: {sys.version}")
print("Thiết lập hoàn tất! ✅")

# Test input/output
name = input("Nhập tên của bạn: ")
print(f"Xin chào {name}! Bạn đã sẵn sàng học Python!")
```

Nếu code này chạy được và hiển thị kết quả, bạn đã cài đặt thành công! 🎉

## Tiếp Theo

Bây giờ bạn đã có môi trường Python hoàn chỉnh. Hãy chuyển sang file `1-bai-tap-co-ban.md` để bắt đầu học các khái niệm cơ bản!

## Hỗ Trợ

Nếu gặp vấn đề:
1. **Google**: Tìm kiếm lỗi chính xác
2. **Stack Overflow**: Hỏi đáp lập trình
3. **Python.org**: Tài liệu chính thức
4. **YouTube**: Video hướng dẫn bằng tiếng Việt 