"""
GAME ĐOÁN SỐ NÂNG CAO
====================

Game đoán số với nhiều tính năng:
- Multiple difficulty levels
- Hint system (higher/lower/close) 
- Lives system
- Score tracking
- Play again option
- Statistics display

Yêu cầu: 200+ dòng code, sử dụng for/while loops
"""

import random
import time

print("🎯 GAME ĐOÁN SỐ NÂNG CAO")
print("=" * 40)

# Global variables để lưu thống kê
player_stats = {
    "name": "",
    "total_games": 0,
    "total_wins": 0,
    "best_score": 0,
    "game_history": []
}

def get_player_info():
    """Lấy thông tin người chơi"""
    print("\n👤 THÔNG TIN NGƯỜI CHƠI")
    while True:
        name = input("Tên của bạn: ").strip()
        if name:
            player_stats["name"] = name
            print(f"Chào mừng {name} đến với Game Đoán Số! 🎮")
            break
        else:
            print("❌ Vui lòng nhập tên!")

def choose_difficulty():
    """Chọn độ khó"""
    difficulties = {
        1: {"name": "Dễ", "range": (1, 50), "lives": 10, "score_multiplier": 1},
        2: {"name": "Trung Bình", "range": (1, 100), "lives": 8, "score_multiplier": 2},
        3: {"name": "Khó", "range": (1, 200), "lives": 6, "score_multiplier": 3},
        4: {"name": "Siêu Khó", "range": (1, 500), "lives": 5, "score_multiplier": 4}
    }
    
    print("\n⚙️ CHỌN ĐỘ KHÓ:")
    print("-" * 40)
    
    for level, info in difficulties.items():
        range_str = f"{info['range'][0]}-{info['range'][1]}"
        print(f"{level}. {info['name']:<12} | Range: {range_str:<8} | Lives: {info['lives']}")
    
    while True:
        try:
            choice = int(input("\nChọn độ khó (1-4): "))
            if 1 <= choice <= 4:
                return difficulties[choice]
            else:
                print("❌ Chọn từ 1-4!")
        except ValueError:
            print("❌ Vui lòng nhập số!")

def give_hint(guess, secret, min_num, max_num):
    """Đưa ra gợi ý thông minh"""
    difference = abs(guess - secret)
    percentage_diff = (difference / (max_num - min_num)) * 100
    
    # Hướng
    if guess < secret:
        direction = "📈 SỐ CẦN TÌM LỚN HỚN!"
    else:
        direction = "📉 SỐ CẦN TÌM NHỎ HỚN!"
    
    # Khoảng cách
    if percentage_diff <= 5:
        proximity = "🔥 RẤT GẦN RỒI!"
    elif percentage_diff <= 15:
        proximity = "🎯 GẦN RỒI!"
    elif percentage_diff <= 30:
        proximity = "🤔 HƠI XA"
    else:
        proximity = "❄️ RẤT XA"
    
    return direction, proximity

def calculate_score(attempts, lives_left, time_taken, difficulty_multiplier):
    """Tính điểm dựa trên performance"""
    base_score = 1000
    time_bonus = max(0, 100 - int(time_taken))
    lives_bonus = lives_left * 50
    attempts_penalty = attempts * 10
    difficulty_bonus = difficulty_multiplier * 100
    
    final_score = base_score + time_bonus + lives_bonus - attempts_penalty + difficulty_bonus
    return max(0, final_score)

def play_game():
    """Chơi game chính"""
    difficulty = choose_difficulty()
    
    # Thiết lập game
    min_num, max_num = difficulty["range"]
    secret_number = random.randint(min_num, max_num)
    lives = difficulty["lives"]
    attempts = 0
    start_time = time.time()
    
    print(f"\n🎯 BẮT ĐẦU GAME - ĐỘ KHÓ: {difficulty['name']}")
    print(f"📊 Range: {min_num}-{max_num} | 💖 Lives: {lives}")
    print("💡 Hints sẽ cho bạn biết hướng và khoảng cách!")
    print("-" * 50)
    
    guess_history = []
    
    # Game loop
    while lives > 0:
        attempts += 1
        print(f"\n🎮 Lần thử {attempts} | 💖 Lives: {lives}")
        
        # Hiển thị lịch sử đoán gần đây
        if guess_history:
            recent_guesses = guess_history[-3:]  # 3 lần gần nhất
            print(f"📝 Đã đoán: {' → '.join(map(str, recent_guesses))}")
        
        try:
            guess = int(input(f"Đoán số ({min_num}-{max_num}): "))
            
            # Kiểm tra range
            if guess < min_num or guess > max_num:
                print(f"❌ Số phải trong khoảng {min_num}-{max_num}!")
                continue
            
            # Kiểm tra đã đoán chưa
            if guess in guess_history:
                print("⚠️ Bạn đã đoán số này rồi!")
                continue
            
            guess_history.append(guess)
            
            if guess == secret_number:
                # THẮNG!
                end_time = time.time()
                game_time = end_time - start_time
                
                score = calculate_score(attempts, lives, game_time, difficulty["score_multiplier"])
                
                print(f"\n🎉 CHÍNH XÁC! Số là {secret_number}")
                print("=" * 50)
                print(f"⭐ ĐIỂM SỐ: {score}")
                print(f"⏱️ Thời gian: {game_time:.1f} giây")
                print(f"🎯 Số lần thử: {attempts}")
                print(f"💖 Lives còn lại: {lives}")
                print(f"🏆 Độ khó: {difficulty['name']}")
                
                # Cập nhật thống kê
                player_stats["total_games"] += 1
                player_stats["total_wins"] += 1
                if score > player_stats["best_score"]:
                    player_stats["best_score"] = score
                    print("🆕 ĐIỂM SỐ TỐT NHẤT MỚI!")
                
                # Lưu vào lịch sử
                game_record = {
                    "difficulty": difficulty['name'],
                    "score": score,
                    "attempts": attempts,
                    "time": game_time,
                    "won": True
                }
                player_stats["game_history"].append(game_record)
                
                return True
            
            else:
                # Sai - đưa hints
                lives -= 1
                direction, proximity = give_hint(guess, secret_number, min_num, max_num)
                
                print(f"❌ Sai rồi! {direction}")
                print(f"💡 Khoảng cách: {proximity}")
                
                # Hints đặc biệt cho số lần thử cao
                if attempts >= 5:
                    if secret_number % 2 == 0:
                        print("🔍 Bonus hint: Số cần tìm là số CHẴN")
                    else:
                        print("🔍 Bonus hint: Số cần tìm là số LẺ")
                
                if lives > 0:
                    print(f"💖 Còn {lives} lives!")
                else:
                    print("💀 HẾT LIVES!")
        
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ!")
            continue
    
    # THUA GAME
    end_time = time.time()
    game_time = end_time - start_time
    
    print(f"\n💀 GAME OVER!")
    print(f"🎯 Số đúng là: {secret_number}")
    print(f"📊 Lịch sử đoán: {' → '.join(map(str, guess_history))}")
    print(f"⏱️ Thời gian: {game_time:.1f} giây")
    
    # Lưu game thua
    player_stats["total_games"] += 1
    game_record = {
        "difficulty": difficulty['name'],
        "score": 0,
        "attempts": attempts,
        "time": game_time,
        "won": False
    }
    player_stats["game_history"].append(game_record)
    
    return False

def show_statistics():
    """Hiển thị thống kê chi tiết"""
    if player_stats["total_games"] == 0:
        print("📊 Chưa có dữ liệu thống kê!")
        return
    
    win_rate = (player_stats["total_wins"] / player_stats["total_games"]) * 100
    
    print(f"\n📊 THỐNG KÊ GAME - {player_stats['name']}")
    print("=" * 50)
    print(f"🎮 Tổng game đã chơi: {player_stats['total_games']}")
    print(f"🏆 Số game thắng: {player_stats['total_wins']}")
    print(f"📈 Tỷ lệ thắng: {win_rate:.1f}%")
    print(f"⭐ Điểm cao nhất: {player_stats['best_score']}")
    
    # Phân tích theo độ khó
    difficulty_stats = {}
    for game in player_stats["game_history"]:
        diff = game['difficulty']
        if diff not in difficulty_stats:
            difficulty_stats[diff] = {"played": 0, "won": 0, "avg_score": 0}
        
        difficulty_stats[diff]["played"] += 1
        if game['won']:
            difficulty_stats[diff]["won"] += 1
            difficulty_stats[diff]["avg_score"] += game['score']
    
    if difficulty_stats:
        print(f"\n📊 PHÂN TÍCH THEO ĐỘ KHÓ:")
        for diff, stats in difficulty_stats.items():
            win_rate_diff = (stats['won'] / stats['played']) * 100 if stats['played'] > 0 else 0
            avg_score = stats['avg_score'] / stats['won'] if stats['won'] > 0 else 0
            print(f"- {diff}: {stats['won']}/{stats['played']} games ({win_rate_diff:.1f}% win rate)")
            if avg_score > 0:
                print(f"  Điểm TB: {avg_score:.0f}")

def show_game_history():
    """Hiển thị lịch sử các game đã chơi"""
    if not player_stats["game_history"]:
        print("📚 Chưa có lịch sử game!")
        return
    
    print(f"\n📚 LỊCH SỬ GAME - {len(player_stats['game_history'])} games")
    print("=" * 60)
    
    # Hiển thị 10 game gần nhất
    recent_games = player_stats["game_history"][-10:]
    
    for i, game in enumerate(recent_games, 1):
        status = "🏆 THẮNG" if game['won'] else "💀 THUA"
        print(f"{i:2}. {status} | {game['difficulty']:<12} | "
              f"Score: {game['score']:4} | Attempts: {game['attempts']:2} | "
              f"Time: {game['time']:.1f}s")
    
    if len(player_stats["game_history"]) > 10:
        print(f"\n... và {len(player_stats['game_history']) - 10} game khác")

def show_leaderboard():
    """Hiển thị bảng xếp hạng điểm cao"""
    winning_games = [g for g in player_stats["game_history"] if g['won']]
    
    if not winning_games:
        print("🏆 Chưa có điểm số nào!")
        return
    
    # Sắp xếp theo điểm số
    sorted_games = sorted(winning_games, key=lambda x: x['score'], reverse=True)
    
    print(f"\n🏆 BẢNG XẾP HẠNG - TOP {min(10, len(sorted_games))}")
    print("=" * 60)
    
    for i, game in enumerate(sorted_games[:10], 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i:2}."
        print(f"{medal} {game['score']:4} điểm | {game['difficulty']:<12} | "
              f"{game['attempts']:2} attempts | {game['time']:.1f}s")

def show_instructions():
    """Hiển thị hướng dẫn chơi"""
    print("\n❓ HƯỚNG DẪN CHƠI GAME")
    print("=" * 40)
    
    print("🎯 MỤC TIÊU:")
    print("- Đoán đúng số bí mật trong giới hạn lives")
    print("- Đạt điểm số cao nhất có thể")
    
    print("\n🎮 CÁCH CHƠI:")
    print("1. Chọn độ khó phù hợp")
    print("2. Nhập số để đoán")
    print("3. Nhận hints và điều chỉnh")
    print("4. Đoán đúng trước khi hết lives")
    
    print("\n💡 HIỂU HINTS:")
    print("📈 Số cần tìm LỚN HỚN số bạn đoán")
    print("📉 Số cần tìm NHỎ HỚN số bạn đoán")
    print("🔥 Rất gần (sai lệch <5%)")
    print("🎯 Gần rồi (sai lệch <15%)")
    print("🤔 Hơi xa (sai lệch <30%)")
    print("❄️ Rất xa (sai lệch >30%)")
    
    print("\n⭐ TÍNH ĐIỂM:")
    print("- Điểm cơ bản: 1000")
    print("- Bonus thời gian: +100 (nếu nhanh)")
    print("- Bonus lives: +50 mỗi life còn lại")
    print("- Trừ điểm: -10 mỗi lần thử")
    print("- Bonus độ khó: +100 x multiplier")
    
    print("\n🧠 CHIẾN THUẬT HAY:")
    print("- Bắt đầu từ giữa khoảng số")
    print("- Sử dụng binary search")
    print("- Chú ý hints về khoảng cách")
    print("- Nhớ các số đã đoán")
    print("- Chơi độ khó cao để điểm cao")

def main_menu():
    """Menu chính của game"""
    get_player_info()
    
    while True:
        print(f"\n🎮 GAME MENU - {player_stats['name']}")
        print("=" * 40)
        print("1. 🎯 Chơi Game")
        print("2. 📊 Xem Thống Kê")
        print("3. 📚 Lịch Sử Game")
        print("4. 🏆 Bảng Xếp Hạng")
        print("5. ❓ Hướng Dẫn")
        print("6. 🚪 Thoát")
        
        try:
            choice = int(input("\nChọn (1-6): "))
            
            if choice == 1:
                # Chơi game
                result = play_game()
                
                # Hỏi chơi tiếp
                while True:
                    play_again = input("\nChơi lại? (y/n): ").lower()
                    if play_again in ['y', 'yes', 'có']:
                        play_game()
                    elif play_again in ['n', 'no', 'không']:
                        break
                    else:
                        print("❌ Vui lòng nhập y hoặc n!")
            
            elif choice == 2:
                show_statistics()
            
            elif choice == 3:
                show_game_history()
            
            elif choice == 4:
                show_leaderboard()
            
            elif choice == 5:
                show_instructions()
            
            elif choice == 6:
                print(f"\n👋 Tạm biệt {player_stats['name']}!")
                if player_stats['total_games'] > 0:
                    print(f"🎮 Bạn đã chơi {player_stats['total_games']} games")
                    print(f"🏆 Thắng {player_stats['total_wins']} games")
                    print(f"⭐ Điểm cao nhất: {player_stats['best_score']}")
                print("🎉 Cảm ơn bạn đã chơi Game Đoán Số!")
                break
            
            else:
                print("❌ Chọn từ 1-6!")
        
        except ValueError:
            print("❌ Vui lòng nhập số!")
        
        input("\nNhấn Enter để tiếp tục...")

# =============================================================================
# CHẠY GAME
# =============================================================================

if __name__ == "__main__":
    print("🎮 CHÀO MỪNG ĐẾN VỚI GAME ĐOÁN SỐ NÂNG CAO!")
    print("Game với đầy đủ tính năng professional")
    print("Hãy thử thách bản thân với các độ khó khác nhau!")
    print("💡 Sử dụng hints thông minh để đoán chính xác!")
    
    main_menu()
    
    print("\n🏁 CẢM ƠN BẠN ĐÃ CHƠI!")
    print("🔥 Dự án hoàn thành: Game Đoán Số Nâng Cao")
    print("💪 Skills đã học: while loops, functions, data management, game logic") 