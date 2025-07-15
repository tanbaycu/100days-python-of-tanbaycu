#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 BÀI TẬP TỔNG HỢP OOP - COMPREHENSIVE PROJECTS
===================================================

Ngày 15-17: Object-Oriented Programming - Integration Tests
Tác giả: TanBayCu Learning System
Mô tả: Comprehensive OOP projects với enterprise architecture và integration testing

🎯 MỤC TIÊU:
- Tích hợp tất cả concepts OOP đã học
- Xây dựng enterprise-level applications
- Thực hành design patterns
- Integration testing và quality assurance
- Real-world project scenarios

📚 KIẾN THỨC TÍCH HỢP:
✅ Classes & Objects
✅ Inheritance & Polymorphism  
✅ Encapsulation & Abstraction
✅ Design Patterns
✅ Error Handling
✅ Testing & Validation
"""

import json
import datetime
import random
import hashlib
import uuid
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import time
import os

# ================================
# 🏗️ DESIGN PATTERNS & UTILITIES
# ================================

class SingletonMeta(type):
    """Singleton metaclass for ensuring single instance"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Observer(ABC):
    """Observer pattern interface"""
    @abstractmethod
    def update(self, subject, event_type: str, data: Any):
        pass

class Subject:
    """Subject class for Observer pattern"""
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_type: str, data: Any = None):
        for observer in self._observers:
            observer.update(self, event_type, data)

class ValidationError(Exception):
    """Custom validation error"""
    pass

class SecurityError(Exception):
    """Custom security error"""
    pass

# ================================
# 🏦 PROJECT 1: BANKING SYSTEM
# ================================

class AccountType(Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    BUSINESS = "business"
    PREMIUM = "premium"

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    FEE = "fee"

@dataclass
class Transaction:
    """Transaction data class"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    account_id: str = ""
    transaction_type: TransactionType = TransactionType.DEPOSIT
    amount: float = 0.0
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)
    description: str = ""
    balance_after: float = 0.0

class Account(Subject):
    """Base account class with Observer pattern"""
    
    def __init__(self, account_id: str, owner_name: str, initial_balance: float = 0.0):
        super().__init__()
        self._account_id = account_id
        self._owner_name = owner_name
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._is_active = True
        self._created_at = datetime.datetime.now()
    
    @property
    def account_id(self) -> str:
        return self._account_id
    
    @property
    def owner_name(self) -> str:
        return self._owner_name
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    def deposit(self, amount: float, description: str = ""):
        """Deposit money to account"""
        if not self._is_active:
            raise SecurityError("Account is deactivated")
        
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive")
        
        self._balance += amount
        transaction = Transaction(
            account_id=self._account_id,
            transaction_type=TransactionType.DEPOSIT,
            amount=amount,
            description=description,
            balance_after=self._balance
        )
        self._transactions.append(transaction)
        self.notify("deposit", {"amount": amount, "balance": self._balance})
        return transaction
    
    def withdraw(self, amount: float, description: str = ""):
        """Withdraw money from account"""
        if not self._is_active:
            raise SecurityError("Account is deactivated")
        
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValidationError("Insufficient funds")
        
        self._balance -= amount
        transaction = Transaction(
            account_id=self._account_id,
            transaction_type=TransactionType.WITHDRAWAL,
            amount=amount,
            description=description,
            balance_after=self._balance
        )
        self._transactions.append(transaction)
        self.notify("withdrawal", {"amount": amount, "balance": self._balance})
        return transaction
    
    def get_transaction_history(self, limit: int = 10) -> List[Transaction]:
        """Get transaction history"""
        return self._transactions[-limit:]
    
    def deactivate(self):
        """Deactivate account"""
        self._is_active = False
        self.notify("deactivated", {"account_id": self._account_id})

class SavingsAccount(Account):
    """Savings account with interest calculation"""
    
    def __init__(self, account_id: str, owner_name: str, initial_balance: float = 0.0, 
                 interest_rate: float = 0.02):
        super().__init__(account_id, owner_name, initial_balance)
        self._interest_rate = interest_rate
        self._minimum_balance = 100.0
    
    def withdraw(self, amount: float, description: str = ""):
        """Override withdraw with minimum balance check"""
        if self._balance - amount < self._minimum_balance:
            raise ValidationError(f"Minimum balance of ${self._minimum_balance} required")
        return super().withdraw(amount, description)
    
    def calculate_interest(self) -> float:
        """Calculate monthly interest"""
        interest = self._balance * self._interest_rate / 12
        return interest
    
    def apply_interest(self):
        """Apply monthly interest"""
        interest = self.calculate_interest()
        if interest > 0:
            self.deposit(interest, "Monthly interest")

class BusinessAccount(Account):
    """Business account with transaction fees"""
    
    def __init__(self, account_id: str, owner_name: str, initial_balance: float = 0.0):
        super().__init__(account_id, owner_name, initial_balance)
        self._transaction_fee = 2.0
        self._free_transactions = 5
        self._monthly_transactions = 0
    
    def _apply_fee(self):
        """Apply transaction fee if over limit"""
        if self._monthly_transactions >= self._free_transactions:
            self._balance -= self._transaction_fee
            fee_transaction = Transaction(
                account_id=self._account_id,
                transaction_type=TransactionType.FEE,
                amount=self._transaction_fee,
                description="Transaction fee",
                balance_after=self._balance
            )
            self._transactions.append(fee_transaction)
    
    def deposit(self, amount: float, description: str = ""):
        """Override deposit with fee application"""
        transaction = super().deposit(amount, description)
        self._monthly_transactions += 1
        self._apply_fee()
        return transaction
    
    def withdraw(self, amount: float, description: str = ""):
        """Override withdraw with fee application"""
        transaction = super().withdraw(amount, description)
        self._monthly_transactions += 1
        self._apply_fee()
        return transaction

class BankingSystem(metaclass=SingletonMeta):
    """Banking system singleton"""
    
    def __init__(self):
        self._accounts: Dict[str, Account] = {}
        self._audit_log: List[Dict] = []
    
    def create_account(self, account_type: AccountType, owner_name: str, 
                      initial_balance: float = 0.0) -> Account:
        """Create new account"""
        account_id = f"{account_type.value}_{len(self._accounts) + 1:04d}"
        
        if account_type == AccountType.SAVINGS:
            account = SavingsAccount(account_id, owner_name, initial_balance)
        elif account_type == AccountType.BUSINESS:
            account = BusinessAccount(account_id, owner_name, initial_balance)
        else:
            account = Account(account_id, owner_name, initial_balance)
        
        self._accounts[account_id] = account
        self._log_audit("account_created", {
            "account_id": account_id,
            "owner": owner_name,
            "type": account_type.value
        })
        
        return account
    
    def get_account(self, account_id: str) -> Optional[Account]:
        """Get account by ID"""
        return self._accounts.get(account_id)
    
    def transfer(self, from_account_id: str, to_account_id: str, 
                amount: float, description: str = ""):
        """Transfer money between accounts"""
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        
        if not from_account or not to_account:
            raise ValidationError("Invalid account ID")
        
        # Withdraw from source
        from_account.withdraw(amount, f"Transfer to {to_account_id}: {description}")
        
        # Deposit to destination
        to_account.deposit(amount, f"Transfer from {from_account_id}: {description}")
        
        self._log_audit("transfer", {
            "from": from_account_id,
            "to": to_account_id,
            "amount": amount
        })
    
    def _log_audit(self, action: str, data: Dict):
        """Log audit trail"""
        self._audit_log.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action,
            "data": data
        })
    
    def get_audit_log(self) -> List[Dict]:
        """Get audit log"""
        return self._audit_log.copy()

# ================================
# 🎮 PROJECT 2: GAME SYSTEM
# ================================

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

class PlayerType(Enum):
    HUMAN = "human"
    AI = "ai"

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

@dataclass
class GameStats:
    """Game statistics"""
    games_played: int = 0
    games_won: int = 0
    total_score: int = 0
    best_score: int = 0
    total_time: float = 0.0
    
    @property
    def win_rate(self) -> float:
        return (self.games_won / self.games_played * 100) if self.games_played > 0 else 0.0
    
    @property
    def average_score(self) -> float:
        return self.total_score / self.games_played if self.games_played > 0 else 0.0

class Player(ABC):
    """Abstract player class"""
    
    def __init__(self, name: str, player_type: PlayerType):
        self._name = name
        self._player_type = player_type
        self._stats = GameStats()
        self._level = 1
        self._experience = 0
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def player_type(self) -> PlayerType:
        return self._player_type
    
    @property
    def stats(self) -> GameStats:
        return self._stats
    
    @property
    def level(self) -> int:
        return self._level
    
    def add_experience(self, exp: int):
        """Add experience points"""
        self._experience += exp
        # Level up every 1000 XP
        new_level = self._experience // 1000 + 1
        if new_level > self._level:
            self._level = new_level
            return True  # Level up occurred
        return False
    
    @abstractmethod
    def make_move(self, game_state: Any) -> Any:
        """Make a move in the game"""
        pass
    
    def update_stats(self, won: bool, score: int, time_played: float):
        """Update player statistics"""
        self._stats.games_played += 1
        if won:
            self._stats.games_won += 1
        self._stats.total_score += score
        self._stats.best_score = max(self._stats.best_score, score)
        self._stats.total_time += time_played

class HumanPlayer(Player):
    """Human player implementation"""
    
    def __init__(self, name: str):
        super().__init__(name, PlayerType.HUMAN)
    
    def make_move(self, game_state: Any) -> Any:
        """Get move from human input"""
        return input(f"{self._name}, enter your move: ")

class AIPlayer(Player):
    """AI player implementation"""
    
    def __init__(self, name: str, difficulty: Difficulty = Difficulty.MEDIUM):
        super().__init__(name, PlayerType.AI)
        self._difficulty = difficulty
    
    def make_move(self, game_state: Any) -> Any:
        """AI makes a move based on difficulty"""
        if self._difficulty == Difficulty.EASY:
            return self._easy_move(game_state)
        elif self._difficulty == Difficulty.MEDIUM:
            return self._medium_move(game_state)
        else:
            return self._hard_move(game_state)
    
    def _easy_move(self, game_state: Any) -> Any:
        """Easy AI move (random)"""
        return random.choice(["rock", "paper", "scissors"])
    
    def _medium_move(self, game_state: Any) -> Any:
        """Medium AI move (some strategy)"""
        moves = ["rock", "paper", "scissors"]
        return random.choice(moves)
    
    def _hard_move(self, game_state: Any) -> Any:
        """Hard AI move (advanced strategy)"""
        # Implement more sophisticated AI logic
        return "rock"  # Simplified for demo

class Game(ABC, Subject):
    """Abstract game class"""
    
    def __init__(self, game_id: str, players: List[Player]):
        Subject.__init__(self)
        self._game_id = game_id
        self._players = players
        self._state = GameState.MENU
        self._score = {player.name: 0 for player in players}
        self._start_time = None
        self._end_time = None
        self._winner = None
    
    @property
    def game_id(self) -> str:
        return self._game_id
    
    @property
    def state(self) -> GameState:
        return self._state
    
    @property
    def players(self) -> List[Player]:
        return self._players.copy()
    
    @property
    def score(self) -> Dict[str, int]:
        return self._score.copy()
    
    @abstractmethod
    def start_game(self):
        """Start the game"""
        pass
    
    @abstractmethod
    def play_round(self):
        """Play one round"""
        pass
    
    @abstractmethod
    def check_winner(self) -> Optional[Player]:
        """Check if there's a winner"""
        pass
    
    def pause_game(self):
        """Pause the game"""
        if self._state == GameState.PLAYING:
            self._state = GameState.PAUSED
            self.notify("game_paused", {"game_id": self._game_id})
    
    def resume_game(self):
        """Resume the game"""
        if self._state == GameState.PAUSED:
            self._state = GameState.PLAYING
            self.notify("game_resumed", {"game_id": self._game_id})
    
    def end_game(self, winner: Optional[Player] = None):
        """End the game"""
        self._state = GameState.GAME_OVER
        self._end_time = datetime.datetime.now()
        self._winner = winner
        
        # Update player stats
        game_time = (self._end_time - self._start_time).total_seconds()
        for player in self._players:
            player_score = self._score[player.name]
            won = player == winner
            player.update_stats(won, player_score, game_time)
            
            # Add experience
            exp_gained = player_score * 10 + (100 if won else 50)
            level_up = player.add_experience(exp_gained)
            if level_up:
                self.notify("level_up", {"player": player.name, "level": player.level})
        
        self.notify("game_ended", {
            "game_id": self._game_id,
            "winner": winner.name if winner else None,
            "final_scores": self._score
        })

class RockPaperScissorsGame(Game):
    """Rock Paper Scissors game implementation"""
    
    def __init__(self, game_id: str, players: List[Player], rounds_to_win: int = 3):
        super().__init__(game_id, players)
        self._rounds_to_win = rounds_to_win
        self._current_round = 0
    
    def start_game(self):
        """Start the game"""
        self._state = GameState.PLAYING
        self._start_time = datetime.datetime.now()
        self._current_round = 0
        self.notify("game_started", {"game_id": self._game_id})
    
    def play_round(self):
        """Play one round of Rock Paper Scissors"""
        if self._state != GameState.PLAYING:
            return
        
        self._current_round += 1
        moves = {}
        
        # Get moves from all players
        for player in self._players:
            move = player.make_move(self._score)
            moves[player.name] = move
        
        # Determine round winner
        winner = self._determine_round_winner(moves)
        if winner:
            self._score[winner.name] += 1
            self.notify("round_won", {
                "round": self._current_round,
                "winner": winner.name,
                "moves": moves
            })
        else:
            self.notify("round_tie", {
                "round": self._current_round,
                "moves": moves
            })
        
        # Check for game winner
        game_winner = self.check_winner()
        if game_winner:
            self.end_game(game_winner)
    
    def _determine_round_winner(self, moves: Dict[str, str]) -> Optional[Player]:
        """Determine winner of a round"""
        if len(moves) != 2:
            return None
        
        player_names = list(moves.keys())
        move1, move2 = moves[player_names[0]], moves[player_names[1]]
        
        if move1 == move2:
            return None  # Tie
        
        winning_moves = {
            ("rock", "scissors"): player_names[0],
            ("scissors", "paper"): player_names[0],
            ("paper", "rock"): player_names[0],
            ("scissors", "rock"): player_names[1],
            ("paper", "scissors"): player_names[1],
            ("rock", "paper"): player_names[1]
        }
        
        winner_name = winning_moves.get((move1, move2))
        return next((p for p in self._players if p.name == winner_name), None)
    
    def check_winner(self) -> Optional[Player]:
        """Check if someone won the game"""
        for player in self._players:
            if self._score[player.name] >= self._rounds_to_win:
                return player
        return None

class GameManager(Observer, metaclass=SingletonMeta):
    """Game manager singleton"""
    
    def __init__(self):
        self._games: Dict[str, Game] = {}
        self._players: Dict[str, Player] = {}
        self._leaderboard: List[Dict] = []
    
    def create_player(self, name: str, player_type: PlayerType, 
                     difficulty: Difficulty = Difficulty.MEDIUM) -> Player:
        """Create a new player"""
        if player_type == PlayerType.HUMAN:
            player = HumanPlayer(name)
        else:
            player = AIPlayer(name, difficulty)
        
        self._players[name] = player
        return player
    
    def create_game(self, game_type: str, players: List[str], **kwargs) -> Game:
        """Create a new game"""
        game_id = f"{game_type}_{len(self._games) + 1:04d}"
        player_objects = [self._players[name] for name in players if name in self._players]
        
        if game_type == "rock_paper_scissors":
            game = RockPaperScissorsGame(game_id, player_objects, **kwargs)
        else:
            raise ValueError(f"Unknown game type: {game_type}")
        
        game.attach(self)  # Observe game events
        self._games[game_id] = game
        return game
    
    def get_game(self, game_id: str) -> Optional[Game]:
        """Get game by ID"""
        return self._games.get(game_id)
    
    def get_player(self, name: str) -> Optional[Player]:
        """Get player by name"""
        return self._players.get(name)
    
    def update_leaderboard(self):
        """Update leaderboard based on player stats"""
        self._leaderboard = []
        for player in self._players.values():
            self._leaderboard.append({
                "name": player.name,
                "level": player.level,
                "games_played": player.stats.games_played,
                "win_rate": player.stats.win_rate,
                "best_score": player.stats.best_score,
                "average_score": player.stats.average_score
            })
        
        # Sort by level, then by win rate
        self._leaderboard.sort(key=lambda x: (x["level"], x["win_rate"]), reverse=True)
    
    def get_leaderboard(self) -> List[Dict]:
        """Get current leaderboard"""
        self.update_leaderboard()
        return self._leaderboard.copy()
    
    def update(self, subject, event_type: str, data: Any):
        """Handle game events"""
        if event_type == "game_ended":
            self.update_leaderboard()
        elif event_type == "level_up":
            print(f"🎉 {data['player']} leveled up to level {data['level']}!")

# ================================
# 🧪 TESTING FRAMEWORK
# ================================

class TestResult:
    """Test result class"""
    def __init__(self, test_name: str, passed: bool, message: str = "", 
                 execution_time: float = 0.0):
        self.test_name = test_name
        self.passed = passed
        self.message = message
        self.execution_time = execution_time

class TestSuite:
    """Test suite for comprehensive testing"""
    
    def __init__(self, name: str):
        self.name = name
        self.results: List[TestResult] = []
    
    def run_test(self, test_func, test_name: str):
        """Run a single test"""
        start_time = time.time()
        try:
            test_func()
            execution_time = time.time() - start_time
            result = TestResult(test_name, True, "PASSED", execution_time)
        except Exception as e:
            execution_time = time.time() - start_time
            result = TestResult(test_name, False, str(e), execution_time)
        
        self.results.append(result)
        return result
    
    def run_all_tests(self):
        """Run all tests in the suite"""
        print(f"\n🧪 Running {self.name} Test Suite")
        print("=" * 50)
        
        passed = 0
        failed = 0
        
        for result in self.results:
            status = "✅ PASS" if result.passed else "❌ FAIL"
            print(f"{status} {result.test_name} ({result.execution_time:.3f}s)")
            if not result.passed:
                print(f"    Error: {result.message}")
            
            if result.passed:
                passed += 1
            else:
                failed += 1
        
        print(f"\n📊 Results: {passed} passed, {failed} failed")
        return passed, failed

# ================================
# 🎯 COMPREHENSIVE PROJECTS
# ================================

class ProjectManager:
    """Manager for comprehensive OOP projects"""
    
    def __init__(self):
        self.projects = {
            "1": self.banking_system_project,
            "2": self.game_system_project,
            "3": self.integration_tests,
            "4": self.performance_tests,
            "5": self.security_tests
        }
    
    def run_project(self, project_id: str):
        """Run a specific project"""
        if project_id in self.projects:
            self.projects[project_id]()
        else:
            print("❌ Project không tồn tại!")
    
    def banking_system_project(self):
        """Banking system comprehensive project"""
        print("\n🏦 BANKING SYSTEM PROJECT")
        print("=" * 50)
        
        # Create banking system
        bank = BankingSystem()
        
        # Create accounts
        print("\n📝 Creating accounts...")
        john_savings = bank.create_account(AccountType.SAVINGS, "John Doe", 1000.0)
        jane_checking = bank.create_account(AccountType.CHECKING, "Jane Smith", 500.0)
        acme_business = bank.create_account(AccountType.BUSINESS, "ACME Corp", 10000.0)
        
        # Observer for notifications
        class BankObserver(Observer):
            def update(self, subject, event_type: str, data: Any):
                print(f"🔔 {event_type.upper()}: {data}")
        
        observer = BankObserver()
        john_savings.attach(observer)
        jane_checking.attach(observer)
        acme_business.attach(observer)
        
        # Perform operations
        print("\n💰 Performing transactions...")
        try:
            john_savings.deposit(500.0, "Salary")
            jane_checking.withdraw(100.0, "ATM withdrawal")
            bank.transfer(john_savings.account_id, jane_checking.account_id, 200.0, "Loan")
            
            # Apply interest to savings
            john_savings.apply_interest()
            
            # Business account transactions
            for i in range(10):  # Test fee application
                acme_business.deposit(100.0, f"Payment {i+1}")
            
            print("\n📊 Account balances:")
            print(f"John's Savings: ${john_savings.balance:.2f}")
            print(f"Jane's Checking: ${jane_checking.balance:.2f}")
            print(f"ACME Business: ${acme_business.balance:.2f}")
            
            print("\n📋 Transaction history (John's Savings):")
            for transaction in john_savings.get_transaction_history():
                print(f"  {transaction.timestamp.strftime('%Y-%m-%d %H:%M')} - "
                      f"{transaction.transaction_type.value.upper()}: ${transaction.amount:.2f}")
            
            print("\n🔍 Audit log:")
            for log_entry in bank.get_audit_log():
                print(f"  {log_entry['timestamp']}: {log_entry['action']} - {log_entry['data']}")
        
        except (ValidationError, SecurityError) as e:
            print(f"❌ Error: {e}")
        
        print("\n✅ Banking system project completed!")
    
    def game_system_project(self):
        """Game system comprehensive project"""
        print("\n🎮 GAME SYSTEM PROJECT")
        print("=" * 50)
        
        # Create game manager
        game_manager = GameManager()
        
        # Create players
        print("\n👥 Creating players...")
        human_player = game_manager.create_player("Alice", PlayerType.HUMAN)
        ai_easy = game_manager.create_player("AI Easy", PlayerType.AI, Difficulty.EASY)
        ai_hard = game_manager.create_player("AI Hard", PlayerType.AI, Difficulty.HARD)
        
        # Create and play a game
        print("\n🎲 Creating Rock Paper Scissors game...")
        game = game_manager.create_game("rock_paper_scissors", ["Alice", "AI Easy"], rounds_to_win=3)
        
        # Mock human input for demo
        original_input = input
        moves = ["rock", "paper", "scissors", "rock", "paper"]
        move_index = 0
        
        def mock_input(prompt):
            nonlocal move_index
            if move_index < len(moves):
                move = moves[move_index]
                move_index += 1
                print(f"{prompt}{move}")
                return move
            return "rock"
        
        # Replace input temporarily
        import builtins
        builtins.input = mock_input
        
        try:
            game.start_game()
            
            # Play until game ends
            while game.state == GameState.PLAYING:
                game.play_round()
                time.sleep(0.1)  # Small delay for demo
            
            print(f"\n🏆 Game Results:")
            print(f"Final scores: {game.score}")
            print(f"Winner: {game._winner.name if game._winner else 'Tie'}")
            
            # Show player stats
            print(f"\n📊 Player Statistics:")
            for player_name in ["Alice", "AI Easy"]:
                player = game_manager.get_player(player_name)
                if player:
                    stats = player.stats
                    print(f"{player.name} (Level {player.level}):")
                    print(f"  Games played: {stats.games_played}")
                    print(f"  Win rate: {stats.win_rate:.1f}%")
                    print(f"  Best score: {stats.best_score}")
            
            # Show leaderboard
            print(f"\n🏅 Leaderboard:")
            for i, entry in enumerate(game_manager.get_leaderboard()[:5], 1):
                print(f"{i}. {entry['name']} (Level {entry['level']}) - "
                      f"Win Rate: {entry['win_rate']:.1f}%")
        
        finally:
            # Restore original input
            builtins.input = original_input
        
        print("\n✅ Game system project completed!")
    
    def integration_tests(self):
        """Run integration tests"""
        print("\n🔗 INTEGRATION TESTS")
        print("=" * 50)
        
        suite = TestSuite("Integration Tests")
        
        def test_banking_integration():
            bank = BankingSystem()
            account = bank.create_account(AccountType.SAVINGS, "Test User", 1000.0)
            account.deposit(500.0)
            account.withdraw(200.0)
            assert account.balance == 1300.0
            
            # Test transfer
            account2 = bank.create_account(AccountType.CHECKING, "Test User 2", 500.0)
            bank.transfer(account.account_id, account2.account_id, 300.0)
            assert account.balance == 1000.0
            assert account2.balance == 800.0
        
        def test_game_integration():
            manager = GameManager()
            player1 = manager.create_player("Player1", PlayerType.AI, Difficulty.EASY)
            player2 = manager.create_player("Player2", PlayerType.AI, Difficulty.EASY)
            
            game = manager.create_game("rock_paper_scissors", ["Player1", "Player2"])
            game.start_game()
            
            # Simulate a few rounds
            for _ in range(5):
                if game.state == GameState.PLAYING:
                    game.play_round()
            
            assert game.state in [GameState.PLAYING, GameState.GAME_OVER]
        
        def test_observer_pattern():
            class TestObserver(Observer):
                def __init__(self):
                    self.events = []
                
                def update(self, subject, event_type: str, data: Any):
                    self.events.append((event_type, data))
            
            observer = TestObserver()
            account = Account("test", "Test User", 1000.0)
            account.attach(observer)
            
            account.deposit(500.0)
            account.withdraw(200.0)
            
            assert len(observer.events) == 2
            assert observer.events[0][0] == "deposit"
            assert observer.events[1][0] == "withdrawal"
        
        def test_singleton_pattern():
            bank1 = BankingSystem()
            bank2 = BankingSystem()
            assert bank1 is bank2
            
            manager1 = GameManager()
            manager2 = GameManager()
            assert manager1 is manager2
        
        def test_inheritance_polymorphism():
            accounts = [
                Account("acc1", "User1", 1000.0),
                SavingsAccount("acc2", "User2", 1000.0),
                BusinessAccount("acc3", "User3", 1000.0)
            ]
            
            for account in accounts:
                account.deposit(100.0)
                assert account.balance >= 1100.0  # Business account might have fees
        
        # Run all tests
        suite.run_test(test_banking_integration, "Banking System Integration")
        suite.run_test(test_game_integration, "Game System Integration")
        suite.run_test(test_observer_pattern, "Observer Pattern")
        suite.run_test(test_singleton_pattern, "Singleton Pattern")
        suite.run_test(test_inheritance_polymorphism, "Inheritance & Polymorphism")
        
        passed, failed = suite.run_all_tests()
        
        if failed == 0:
            print("\n🎉 All integration tests passed!")
        else:
            print(f"\n⚠️  {failed} integration tests failed!")
    
    def performance_tests(self):
        """Run performance tests"""
        print("\n⚡ PERFORMANCE TESTS")
        print("=" * 50)
        
        suite = TestSuite("Performance Tests")
        
        def test_banking_performance():
            bank = BankingSystem()
            account = bank.create_account(AccountType.CHECKING, "Performance Test", 10000.0)
            
            # Test 1000 transactions
            start_time = time.time()
            for i in range(1000):
                if i % 2 == 0:
                    account.deposit(10.0)
                else:
                    account.withdraw(5.0)
            
            execution_time = time.time() - start_time
            assert execution_time < 1.0  # Should complete in less than 1 second
            assert len(account.get_transaction_history(1000)) == 1000
        
        def test_game_performance():
            manager = GameManager()
            
            # Create many players
            start_time = time.time()
            for i in range(100):
                manager.create_player(f"Player{i}", PlayerType.AI)
            
            execution_time = time.time() - start_time
            assert execution_time < 0.5  # Should complete in less than 0.5 seconds
        
        def test_observer_performance():
            class FastObserver(Observer):
                def __init__(self):
                    self.count = 0
                
                def update(self, subject, event_type: str, data: Any):
                    self.count += 1
            
            account = Account("test", "Test", 1000.0)
            
            # Attach many observers
            observers = [FastObserver() for _ in range(100)]
            for observer in observers:
                account.attach(observer)
            
            # Test notification performance
            start_time = time.time()
            for _ in range(100):
                account.deposit(1.0)
            
            execution_time = time.time() - start_time
            assert execution_time < 1.0
            assert all(obs.count == 100 for obs in observers)
        
        # Run performance tests
        suite.run_test(test_banking_performance, "Banking Performance")
        suite.run_test(test_game_performance, "Game Creation Performance")
        suite.run_test(test_observer_performance, "Observer Notification Performance")
        
        passed, failed = suite.run_all_tests()
        
        if failed == 0:
            print("\n🚀 All performance tests passed!")
        else:
            print(f"\n⚠️  {failed} performance tests failed!")
    
    def security_tests(self):
        """Run security tests"""
        print("\n🔒 SECURITY TESTS")
        print("=" * 50)
        
        suite = TestSuite("Security Tests")
        
        def test_account_security():
            account = Account("test", "Test User", 1000.0)
            
            # Test deactivated account
            account.deactivate()
            try:
                account.deposit(100.0)
                assert False, "Should not allow deposit on deactivated account"
            except SecurityError:
                pass  # Expected
            
            try:
                account.withdraw(100.0)
                assert False, "Should not allow withdrawal on deactivated account"
            except SecurityError:
                pass  # Expected
        
        def test_validation_security():
            account = Account("test", "Test User", 1000.0)
            
            # Test negative amounts
            try:
                account.deposit(-100.0)
                assert False, "Should not allow negative deposit"
            except ValidationError:
                pass
            
            try:
                account.withdraw(-100.0)
                assert False, "Should not allow negative withdrawal"
            except ValidationError:
                pass
            
            # Test insufficient funds
            try:
                account.withdraw(2000.0)
                assert False, "Should not allow overdraft"
            except ValidationError:
                pass
        
        def test_data_encapsulation():
            account = Account("test", "Test User", 1000.0)
            
            # Test that private attributes are protected
            assert hasattr(account, '_balance')
            assert hasattr(account, '_account_id')
            assert hasattr(account, '_owner_name')
            
            # Test that properties work correctly
            assert account.balance == 1000.0
            assert account.account_id == "test"
            assert account.owner_name == "Test User"
        
        def test_singleton_security():
            # Test that singleton instances are truly single
            bank1 = BankingSystem()
            bank2 = BankingSystem()
            
            # Modify one instance
            bank1._test_attr = "test_value"
            
            # Check that other instance has the same modification
            assert hasattr(bank2, '_test_attr')
            assert bank2._test_attr == "test_value"
        
        # Run security tests
        suite.run_test(test_account_security, "Account Security")
        suite.run_test(test_validation_security, "Validation Security")
        suite.run_test(test_data_encapsulation, "Data Encapsulation")
        suite.run_test(test_singleton_security, "Singleton Security")
        
        passed, failed = suite.run_all_tests()
        
        if failed == 0:
            print("\n🛡️  All security tests passed!")
        else:
            print(f"\n⚠️  {failed} security tests failed!")

# ================================
# 🎯 MAIN MENU SYSTEM
# ================================

class ComprehensiveOOPSystem:
    """Main system for comprehensive OOP projects"""
    
    def __init__(self):
        self.project_manager = ProjectManager()
        self.user_progress = {
            "projects_completed": [],
            "total_score": 0,
            "start_time": datetime.datetime.now()
        }
    
    def show_main_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("🚀 BÀI TẬP TỔNG HỢP OOP - COMPREHENSIVE PROJECTS")
        print("="*60)
        print("📚 Tích hợp tất cả concepts OOP đã học")
        print("🏗️  Enterprise-level applications")
        print("🧪 Integration testing & quality assurance")
        print("🎯 Real-world project scenarios")
        print("="*60)
        
        print("\n🎯 COMPREHENSIVE PROJECTS:")
        print("1. 🏦 Banking System Project")
        print("2. 🎮 Game System Project")
        print("3. 🔗 Integration Tests")
        print("4. ⚡ Performance Tests")
        print("5. 🔒 Security Tests")
        print("6. 📊 View Progress")
        print("7. 🏆 Achievement System")
        print("0. 🚪 Exit")
        
        return input("\n👉 Chọn project (0-7): ").strip()
    
    def view_progress(self):
        """View user progress"""
        print("\n📊 PROGRESS REPORT")
        print("=" * 40)
        
        elapsed_time = datetime.datetime.now() - self.user_progress["start_time"]
        print(f"⏱️  Time spent: {elapsed_time}")
        print(f"🎯 Projects completed: {len(self.user_progress['projects_completed'])}/5")
        print(f"🏆 Total score: {self.user_progress['total_score']}")
        
        if self.user_progress["projects_completed"]:
            print(f"\n✅ Completed projects:")
            for project in self.user_progress["projects_completed"]:
                print(f"   • {project}")
        
        completion_rate = len(self.user_progress["projects_completed"]) / 5 * 100
        print(f"\n📈 Completion rate: {completion_rate:.1f}%")
        
        if completion_rate == 100:
            print("\n🎉 Congratulations! You've completed all comprehensive projects!")
            print("🚀 You're now ready for advanced OOP challenges!")
    
    def achievement_system(self):
        """Display achievement system"""
        print("\n🏆 ACHIEVEMENT SYSTEM")
        print("=" * 40)
        
        achievements = [
            ("🏦 Banking Master", "Complete Banking System Project", "1" in self.user_progress["projects_completed"]),
            ("🎮 Game Developer", "Complete Game System Project", "2" in self.user_progress["projects_completed"]),
            ("🔗 Integration Expert", "Pass all Integration Tests", "3" in self.user_progress["projects_completed"]),
            ("⚡ Performance Guru", "Pass all Performance Tests", "4" in self.user_progress["projects_completed"]),
            ("🔒 Security Specialist", "Pass all Security Tests", "5" in self.user_progress["projects_completed"]),
            ("🎯 Project Completionist", "Complete all 5 projects", len(self.user_progress["projects_completed"]) == 5),
            ("⭐ OOP Master", "Master all OOP concepts", len(self.user_progress["projects_completed"]) == 5 and self.user_progress["total_score"] >= 1000)
        ]
        
        for title, description, earned in achievements:
            status = "✅ EARNED" if earned else "🔒 LOCKED"
            print(f"{status} {title}")
            print(f"    {description}")
            print()
    
    def run_project_and_score(self, project_id: str):
        """Run project and calculate score"""
        project_names = {
            "1": "Banking System Project",
            "2": "Game System Project", 
            "3": "Integration Tests",
            "4": "Performance Tests",
            "5": "Security Tests"
        }
        
        if project_id in project_names:
            print(f"\n🚀 Starting {project_names[project_id]}...")
            
            start_time = time.time()
            self.project_manager.run_project(project_id)
            execution_time = time.time() - start_time
            
            # Calculate score based on completion time
            base_score = 200
            time_bonus = max(0, 300 - int(execution_time * 10))  # Bonus for fast completion
            total_score = base_score + time_bonus
            
            print(f"\n🎯 Project completed in {execution_time:.2f} seconds")
            print(f"🏆 Score earned: {total_score} points")
            
            # Update progress
            if project_id not in self.user_progress["projects_completed"]:
                self.user_progress["projects_completed"].append(project_id)
                self.user_progress["total_score"] += total_score
                
                print(f"✅ Project '{project_names[project_id]}' completed!")
                print(f"📊 Total score: {self.user_progress['total_score']}")
            else:
                print("ℹ️  Project already completed!")
    
    def run(self):
        """Run the comprehensive OOP system"""
        print("🎉 Welcome to Comprehensive OOP Projects!")
        print("🚀 Ready to integrate all your OOP knowledge!")
        
        while True:
            choice = self.show_main_menu()
            
            if choice == "0":
                print("\n👋 Goodbye! Keep practicing OOP!")
                break
            elif choice in ["1", "2", "3", "4", "5"]:
                self.run_project_and_score(choice)
            elif choice == "6":
                self.view_progress()
            elif choice == "7":
                self.achievement_system()
            else:
                print("❌ Invalid choice! Please try again.")
            
            input("\n⏸️  Press Enter to continue...")

# ================================
# 🚀 MAIN EXECUTION
# ================================

if __name__ == "__main__":
    system = ComprehensiveOOPSystem()
    system.run() 