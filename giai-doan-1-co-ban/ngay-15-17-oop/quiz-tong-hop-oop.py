#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎯 QUIZ TỔNG HỢP OOP - ADAPTIVE LEARNING SYSTEM
===============================================

Ngày 15-17: Object-Oriented Programming - Comprehensive Assessment
Tác giả: TanBayCu Learning System
Mô tả: Hệ thống quiz thích ứng với AI-powered assessment và comprehensive evaluation

🎯 TÍNH NĂNG ĐẶC BIỆT:
- 🧠 Adaptive Learning Algorithm
- 🎮 Gamification System
- 📊 Real-time Analytics
- 🏆 Achievement System
- 🔄 Dynamic Difficulty Adjustment
- 🎨 Interactive Visualization
- 🤖 AI-Powered Hints
- 📈 Progress Tracking
- 🌟 Personalized Learning Path
- 🎭 Multiple Question Types
"""

import json
import random
import time
import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any, Callable
import math
import statistics

# ================================
# 🎯 CORE SYSTEM ARCHITECTURE
# ================================

class DifficultyLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    CODE_COMPLETION = "code_completion"
    CODE_DEBUGGING = "code_debugging"
    SCENARIO_BASED = "scenario_based"
    DRAG_DROP = "drag_drop"

class SkillArea(Enum):
    CLASSES_OBJECTS = "classes_objects"
    INHERITANCE = "inheritance"
    POLYMORPHISM = "polymorphism"
    ENCAPSULATION = "encapsulation"
    ABSTRACTION = "abstraction"
    DESIGN_PATTERNS = "design_patterns"

@dataclass
class LearningMetrics:
    """Metrics for adaptive learning"""
    accuracy: float = 0.0
    speed: float = 0.0  # questions per minute
    consistency: float = 0.0
    difficulty_comfort: float = 0.0
    skill_strengths: Dict[SkillArea, float] = field(default_factory=dict)
    skill_weaknesses: Dict[SkillArea, float] = field(default_factory=dict)
    learning_velocity: float = 0.0
    confidence_level: float = 0.0

@dataclass
class QuizQuestion:
    """Enhanced quiz question with metadata"""
    id: str
    question_type: QuestionType
    skill_area: SkillArea
    difficulty: DifficultyLevel
    question_text: str
    options: List[str] = field(default_factory=list)
    correct_answer: Any = None
    explanation: str = ""
    hint: str = ""
    code_snippet: str = ""
    estimated_time: int = 60  # seconds
    tags: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)

@dataclass
class QuizResponse:
    """User response to quiz question"""
    question_id: str
    user_answer: Any
    is_correct: bool
    time_taken: float
    hint_used: bool = False
    attempts: int = 1
    confidence: int = 3  # 1-5 scale
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)

@dataclass
class Achievement:
    """Achievement system"""
    id: str
    title: str
    description: str
    icon: str
    condition: Callable
    points: int
    unlocked: bool = False
    unlock_date: Optional[datetime.datetime] = None

# ================================
# 🧠 ADAPTIVE LEARNING ENGINE
# ================================

class AdaptiveLearningEngine:
    """AI-powered adaptive learning system"""
    
    def __init__(self):
        self.user_metrics = LearningMetrics()
        self.question_history: List[QuizResponse] = []
        self.difficulty_adjustment_factor = 0.1
        self.skill_decay_rate = 0.05
        self.confidence_threshold = 0.7
        
    def analyze_performance(self, responses: List[QuizResponse]) -> LearningMetrics:
        """Analyze user performance and update metrics"""
        if not responses:
            return self.user_metrics
            
        # Calculate accuracy
        correct_answers = sum(1 for r in responses if r.is_correct)
        self.user_metrics.accuracy = correct_answers / len(responses)
        
        # Calculate speed (questions per minute)
        total_time = sum(r.time_taken for r in responses)
        self.user_metrics.speed = len(responses) / (total_time / 60) if total_time > 0 else 0
        
        # Calculate consistency (standard deviation of response times)
        times = [r.time_taken for r in responses]
        if len(times) > 1:
            consistency = 1 - (statistics.stdev(times) / statistics.mean(times))
            self.user_metrics.consistency = max(0, consistency)
        
        # Update skill-specific metrics
        self._update_skill_metrics(responses)
        
        # Calculate learning velocity
        self._calculate_learning_velocity(responses)
        
        # Update confidence level
        self._update_confidence_level(responses)
        
        return self.user_metrics
    
    def _update_skill_metrics(self, responses: List[QuizResponse]):
        """Update skill-specific metrics"""
        skill_performance = {}
        
        for response in responses:
            # Find question to get skill area
            question = self._find_question_by_id(response.question_id)
            if question:
                skill = question.skill_area
                if skill not in skill_performance:
                    skill_performance[skill] = []
                skill_performance[skill].append(response.is_correct)
        
        # Update strengths and weaknesses
        for skill, results in skill_performance.items():
            accuracy = sum(results) / len(results)
            if accuracy >= 0.8:
                self.user_metrics.skill_strengths[skill] = accuracy
            elif accuracy <= 0.5:
                self.user_metrics.skill_weaknesses[skill] = 1 - accuracy
    
    def _calculate_learning_velocity(self, responses: List[QuizResponse]):
        """Calculate how quickly user is improving"""
        if len(responses) < 5:
            return
            
        # Take recent responses and calculate improvement trend
        recent_responses = responses[-10:]
        first_half = recent_responses[:len(recent_responses)//2]
        second_half = recent_responses[len(recent_responses)//2:]
        
        first_accuracy = sum(1 for r in first_half if r.is_correct) / len(first_half)
        second_accuracy = sum(1 for r in second_half if r.is_correct) / len(second_half)
        
        self.user_metrics.learning_velocity = second_accuracy - first_accuracy
    
    def _update_confidence_level(self, responses: List[QuizResponse]):
        """Update confidence level based on recent performance"""
        if not responses:
            return
            
        recent_responses = responses[-5:]
        avg_confidence = sum(r.confidence for r in recent_responses) / len(recent_responses)
        performance_factor = sum(1 for r in recent_responses if r.is_correct) / len(recent_responses)
        
        self.user_metrics.confidence_level = (avg_confidence / 5) * 0.6 + performance_factor * 0.4
    
    def recommend_next_difficulty(self, current_difficulty: DifficultyLevel) -> DifficultyLevel:
        """Recommend next difficulty level"""
        if self.user_metrics.accuracy >= 0.8 and self.user_metrics.confidence_level >= 0.7:
            # Increase difficulty
            if current_difficulty == DifficultyLevel.BEGINNER:
                return DifficultyLevel.INTERMEDIATE
            elif current_difficulty == DifficultyLevel.INTERMEDIATE:
                return DifficultyLevel.ADVANCED
            elif current_difficulty == DifficultyLevel.ADVANCED:
                return DifficultyLevel.EXPERT
        elif self.user_metrics.accuracy <= 0.5 and self.user_metrics.confidence_level <= 0.4:
            # Decrease difficulty
            if current_difficulty == DifficultyLevel.EXPERT:
                return DifficultyLevel.ADVANCED
            elif current_difficulty == DifficultyLevel.ADVANCED:
                return DifficultyLevel.INTERMEDIATE
            elif current_difficulty == DifficultyLevel.INTERMEDIATE:
                return DifficultyLevel.BEGINNER
        
        return current_difficulty
    
    def recommend_skill_focus(self) -> List[SkillArea]:
        """Recommend skills to focus on"""
        # Sort skills by weakness level
        weaknesses = sorted(
            self.user_metrics.skill_weaknesses.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return [skill for skill, level in weaknesses[:3] if level > 0.3]
    
    def _find_question_by_id(self, question_id: str) -> Optional[QuizQuestion]:
        """Find question by ID (placeholder)"""
        # In real implementation, this would query question database
        return None

# ================================
# 🎮 GAMIFICATION SYSTEM
# ================================

class GamificationSystem:
    """Advanced gamification with achievements and rewards"""
    
    def __init__(self):
        self.user_points = 0
        self.user_level = 1
        self.streak_count = 0
        self.achievements: List[Achievement] = []
        self.badges: List[str] = []
        self.experience_points = 0
        self.multiplier = 1.0
        
        self._initialize_achievements()
    
    def _initialize_achievements(self):
        """Initialize achievement system"""
        achievements_data = [
            {
                "id": "first_correct",
                "title": "🎯 First Success",
                "description": "Answer your first question correctly",
                "icon": "🎯",
                "points": 10,
                "condition": lambda stats: stats.get("correct_answers", 0) >= 1
            },
            {
                "id": "streak_5",
                "title": "🔥 Hot Streak",
                "description": "Get 5 questions correct in a row",
                "icon": "🔥",
                "points": 50,
                "condition": lambda stats: stats.get("max_streak", 0) >= 5
            },
            {
                "id": "speed_demon",
                "title": "⚡ Speed Demon",
                "description": "Answer 10 questions in under 5 minutes",
                "icon": "⚡",
                "points": 75,
                "condition": lambda stats: stats.get("speed_achievements", 0) >= 1
            },
            {
                "id": "perfectionist",
                "title": "💎 Perfectionist",
                "description": "Complete a quiz with 100% accuracy",
                "icon": "💎",
                "points": 100,
                "condition": lambda stats: stats.get("perfect_quizzes", 0) >= 1
            },
            {
                "id": "oop_master",
                "title": "🏆 OOP Master",
                "description": "Master all OOP concepts",
                "icon": "🏆",
                "points": 500,
                "condition": lambda stats: all(
                    stats.get(f"{skill.value}_mastery", 0) >= 0.8 
                    for skill in SkillArea
                )
            }
        ]
        
        for data in achievements_data:
            achievement = Achievement(
                id=data["id"],
                title=data["title"],
                description=data["description"],
                icon=data["icon"],
                condition=data["condition"],
                points=data["points"]
            )
            self.achievements.append(achievement)
    
    def award_points(self, base_points: int, difficulty: DifficultyLevel, 
                    time_bonus: bool = False, streak_bonus: bool = False) -> int:
        """Award points with bonuses"""
        # Difficulty multiplier
        difficulty_multiplier = {
            DifficultyLevel.BEGINNER: 1.0,
            DifficultyLevel.INTERMEDIATE: 1.5,
            DifficultyLevel.ADVANCED: 2.0,
            DifficultyLevel.EXPERT: 2.5
        }
        
        points = base_points * difficulty_multiplier[difficulty]
        
        # Time bonus
        if time_bonus:
            points *= 1.2
        
        # Streak bonus
        if streak_bonus:
            points *= (1 + self.streak_count * 0.1)
        
        # Global multiplier
        points *= self.multiplier
        
        final_points = int(points)
        self.user_points += final_points
        self.experience_points += final_points
        
        # Level up check
        self._check_level_up()
        
        return final_points
    
    def _check_level_up(self):
        """Check if user should level up"""
        required_exp = self.user_level * 100
        if self.experience_points >= required_exp:
            self.user_level += 1
            self.multiplier += 0.1
            return True
        return False
    
    def update_streak(self, correct: bool):
        """Update streak counter"""
        if correct:
            self.streak_count += 1
        else:
            self.streak_count = 0
    
    def check_achievements(self, stats: Dict[str, Any]) -> List[Achievement]:
        """Check for newly unlocked achievements"""
        newly_unlocked = []
        
        for achievement in self.achievements:
            if not achievement.unlocked and achievement.condition(stats):
                achievement.unlocked = True
                achievement.unlock_date = datetime.datetime.now()
                self.user_points += achievement.points
                newly_unlocked.append(achievement)
        
        return newly_unlocked
    
    def get_progress_to_next_level(self) -> Dict[str, Any]:
        """Get progress to next level"""
        current_level_exp = (self.user_level - 1) * 100
        next_level_exp = self.user_level * 100
        progress = (self.experience_points - current_level_exp) / (next_level_exp - current_level_exp)
        
        return {
            "current_level": self.user_level,
            "experience_points": self.experience_points,
            "progress_percentage": progress * 100,
            "points_to_next_level": next_level_exp - self.experience_points
        }

# ================================
# 📊 ANALYTICS & VISUALIZATION
# ================================

class AnalyticsEngine:
    """Real-time analytics and visualization"""
    
    def __init__(self):
        self.session_data = {
            "start_time": datetime.datetime.now(),
            "questions_answered": 0,
            "correct_answers": 0,
            "total_time": 0,
            "skill_performance": {},
            "difficulty_progression": [],
            "response_times": [],
            "confidence_levels": []
        }
    
    def record_response(self, response: QuizResponse, question: QuizQuestion):
        """Record user response for analytics"""
        self.session_data["questions_answered"] += 1
        if response.is_correct:
            self.session_data["correct_answers"] += 1
        
        self.session_data["total_time"] += response.time_taken
        self.session_data["response_times"].append(response.time_taken)
        self.session_data["confidence_levels"].append(response.confidence)
        
        # Track skill performance
        skill = question.skill_area.value
        if skill not in self.session_data["skill_performance"]:
            self.session_data["skill_performance"][skill] = {"correct": 0, "total": 0}
        
        self.session_data["skill_performance"][skill]["total"] += 1
        if response.is_correct:
            self.session_data["skill_performance"][skill]["correct"] += 1
        
        # Track difficulty progression
        self.session_data["difficulty_progression"].append({
            "question_id": response.question_id,
            "difficulty": question.difficulty.value,
            "correct": response.is_correct,
            "time": response.time_taken
        })
    
    def generate_session_report(self) -> Dict[str, Any]:
        """Generate comprehensive session report"""
        session_time = (datetime.datetime.now() - self.session_data["start_time"]).total_seconds()
        
        # Calculate accuracy
        accuracy = (self.session_data["correct_answers"] / 
                   self.session_data["questions_answered"]) * 100 if self.session_data["questions_answered"] > 0 else 0
        
        # Calculate average response time
        avg_response_time = (sum(self.session_data["response_times"]) / 
                            len(self.session_data["response_times"])) if self.session_data["response_times"] else 0
        
        # Calculate questions per minute
        qpm = (self.session_data["questions_answered"] / (session_time / 60)) if session_time > 0 else 0
        
        # Skill breakdown
        skill_breakdown = {}
        for skill, data in self.session_data["skill_performance"].items():
            skill_breakdown[skill] = {
                "accuracy": (data["correct"] / data["total"]) * 100 if data["total"] > 0 else 0,
                "questions": data["total"]
            }
        
        return {
            "session_duration": session_time,
            "questions_answered": self.session_data["questions_answered"],
            "accuracy": accuracy,
            "avg_response_time": avg_response_time,
            "questions_per_minute": qpm,
            "skill_breakdown": skill_breakdown,
            "difficulty_progression": self.session_data["difficulty_progression"],
            "confidence_trend": self.session_data["confidence_levels"]
        }
    
    def create_progress_visualization(self) -> str:
        """Create ASCII progress visualization"""
        if not self.session_data["difficulty_progression"]:
            return "No data available"
        
        # Create accuracy over time chart
        chart = "\n📈 ACCURACY OVER TIME\n"
        chart += "=" * 40 + "\n"
        
        # Calculate rolling accuracy
        rolling_window = 5
        rolling_accuracy = []
        
        for i in range(len(self.session_data["difficulty_progression"])):
            start_idx = max(0, i - rolling_window + 1)
            window_data = self.session_data["difficulty_progression"][start_idx:i+1]
            correct_count = sum(1 for item in window_data if item["correct"])
            accuracy = correct_count / len(window_data) * 100
            rolling_accuracy.append(accuracy)
        
        # Create ASCII chart
        max_accuracy = max(rolling_accuracy) if rolling_accuracy else 100
        for i, accuracy in enumerate(rolling_accuracy):
            bar_length = int((accuracy / max_accuracy) * 30)
            bar = "█" * bar_length + "░" * (30 - bar_length)
            chart += f"Q{i+1:2d} |{bar}| {accuracy:.1f}%\n"
        
        return chart
    
    def create_skill_radar_chart(self) -> str:
        """Create ASCII radar chart for skills"""
        if not self.session_data["skill_performance"]:
            return "No skill data available"
        
        chart = "\n🎯 SKILL PERFORMANCE RADAR\n"
        chart += "=" * 40 + "\n"
        
        for skill, data in self.session_data["skill_performance"].items():
            accuracy = (data["correct"] / data["total"]) * 100 if data["total"] > 0 else 0
            bar_length = int(accuracy / 100 * 20)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            chart += f"{skill:15} |{bar}| {accuracy:.1f}%\n"
        
        return chart

# ================================
# 🎯 QUESTION BANK SYSTEM
# ================================

class QuestionBank:
    """Comprehensive OOP question bank"""
    
    def __init__(self):
        self.questions: List[QuizQuestion] = []
        self._initialize_questions()
    
    def _initialize_questions(self):
        """Initialize comprehensive question bank"""
        
        # Classes & Objects Questions
        self.questions.extend([
            QuizQuestion(
                id="class_001",
                question_type=QuestionType.MULTIPLE_CHOICE,
                skill_area=SkillArea.CLASSES_OBJECTS,
                difficulty=DifficultyLevel.BEGINNER,
                question_text="What is a class in OOP?",
                options=[
                    "A blueprint for creating objects",
                    "A function that returns data",
                    "A variable that stores multiple values",
                    "A type of loop structure"
                ],
                correct_answer=0,
                explanation="A class is a blueprint or template for creating objects. It defines the structure and behavior that objects of that class will have.",
                hint="Think of a class as a template or blueprint...",
                estimated_time=30
            ),
            
            QuizQuestion(
                id="class_002",
                question_type=QuestionType.CODE_COMPLETION,
                skill_area=SkillArea.CLASSES_OBJECTS,
                difficulty=DifficultyLevel.INTERMEDIATE,
                question_text="Complete the class definition:",
                code_snippet="""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        # Complete this method
        ____
                """,
                correct_answer="return f'{self.brand} {self.model} engine started!'",
                explanation="The method should return a string indicating the car has started.",
                hint="Use f-string formatting with self.brand and self.model",
                estimated_time=45
            ),
            
            QuizQuestion(
                id="inherit_001",
                question_type=QuestionType.SCENARIO_BASED,
                skill_area=SkillArea.INHERITANCE,
                difficulty=DifficultyLevel.ADVANCED,
                question_text="""
You have a base class Animal and derived classes Dog and Cat. 
The Animal class has a method make_sound(). 
How would you implement polymorphism so that each animal makes its specific sound?
                """,
                options=[
                    "Override make_sound() in each derived class",
                    "Create separate methods for each animal",
                    "Use if-else statements in the base class",
                    "Create a global function for sounds"
                ],
                correct_answer=0,
                explanation="Polymorphism is achieved by overriding the make_sound() method in each derived class to provide specific implementations.",
                hint="Think about method overriding...",
                estimated_time=60
            ),
            
            QuizQuestion(
                id="encap_001",
                question_type=QuestionType.CODE_DEBUGGING,
                skill_area=SkillArea.ENCAPSULATION,
                difficulty=DifficultyLevel.EXPERT,
                question_text="Fix the encapsulation issues in this code:",
                code_snippet="""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Should be private
    
    def withdraw(self, amount):
        self.balance -= amount  # No validation
        return self.balance
                """,
                correct_answer="""
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute
    
    def withdraw(self, amount):
        if amount <= self._balance and amount > 0:
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("Invalid withdrawal amount")
    
    @property
    def balance(self):
        return self._balance
                """,
                explanation="Proper encapsulation requires private attributes, validation, and controlled access through properties.",
                hint="Use underscore for private attributes and add validation...",
                estimated_time=90
            )
        ])
        
        # Add more questions for each skill area
        self._add_inheritance_questions()
        self._add_polymorphism_questions()
        self._add_abstraction_questions()
        self._add_design_pattern_questions()
    
    def _add_inheritance_questions(self):
        """Add inheritance-specific questions"""
        self.questions.extend([
            QuizQuestion(
                id="inherit_002",
                question_type=QuestionType.TRUE_FALSE,
                skill_area=SkillArea.INHERITANCE,
                difficulty=DifficultyLevel.BEGINNER,
                question_text="A child class inherits all methods and attributes from its parent class.",
                correct_answer=True,
                explanation="Yes, child classes inherit all public and protected methods and attributes from their parent class.",
                hint="Think about what inheritance means...",
                estimated_time=20
            ),
            
            QuizQuestion(
                id="inherit_003",
                question_type=QuestionType.MULTIPLE_CHOICE,
                skill_area=SkillArea.INHERITANCE,
                difficulty=DifficultyLevel.INTERMEDIATE,
                question_text="What is the super() function used for?",
                options=[
                    "To call methods from the parent class",
                    "To create a new object",
                    "To delete an object",
                    "To check object type"
                ],
                correct_answer=0,
                explanation="The super() function is used to call methods from the parent class, especially useful in method overriding.",
                hint="Think about accessing parent class methods...",
                estimated_time=35
            )
        ])
    
    def _add_polymorphism_questions(self):
        """Add polymorphism-specific questions"""
        self.questions.extend([
            QuizQuestion(
                id="poly_001",
                question_type=QuestionType.SCENARIO_BASED,
                skill_area=SkillArea.POLYMORPHISM,
                difficulty=DifficultyLevel.ADVANCED,
                question_text="""
You have different shapes (Circle, Rectangle, Triangle) that all need to calculate area. 
How would you implement this using polymorphism?
                """,
                options=[
                    "Create a base Shape class with abstract calculate_area() method",
                    "Create separate functions for each shape",
                    "Use a single function with multiple if-else statements",
                    "Create a dictionary mapping shapes to calculations"
                ],
                correct_answer=0,
                explanation="Polymorphism is best implemented using a base class with abstract methods that derived classes override.",
                hint="Think about abstract base classes...",
                estimated_time=70
            )
        ])
    
    def _add_abstraction_questions(self):
        """Add abstraction-specific questions"""
        self.questions.extend([
            QuizQuestion(
                id="abs_001",
                question_type=QuestionType.CODE_COMPLETION,
                skill_area=SkillArea.ABSTRACTION,
                difficulty=DifficultyLevel.EXPERT,
                question_text="Create an abstract class for a Vehicle:",
                code_snippet="""
from abc import ABC, abstractmethod

class Vehicle(____):
    def __init__(self, brand):
        self.brand = brand
    
    @____
    def start_engine(self):
        ____
                """,
                correct_answer="ABC, abstractmethod, pass",
                explanation="Abstract classes inherit from ABC and use @abstractmethod decorator for abstract methods.",
                hint="Import ABC and use abstractmethod decorator...",
                estimated_time=60
            )
        ])
    
    def _add_design_pattern_questions(self):
        """Add design pattern questions"""
        self.questions.extend([
            QuizQuestion(
                id="pattern_001",
                question_type=QuestionType.MULTIPLE_CHOICE,
                skill_area=SkillArea.DESIGN_PATTERNS,
                difficulty=DifficultyLevel.EXPERT,
                question_text="Which design pattern ensures only one instance of a class exists?",
                options=[
                    "Singleton Pattern",
                    "Factory Pattern",
                    "Observer Pattern",
                    "Strategy Pattern"
                ],
                correct_answer=0,
                explanation="The Singleton pattern ensures that only one instance of a class can exist throughout the application.",
                hint="Think about single instance...",
                estimated_time=40
            )
        ])
    
    def get_questions_by_criteria(self, skill_area: Optional[SkillArea] = None,
                                difficulty: Optional[DifficultyLevel] = None,
                                question_type: Optional[QuestionType] = None) -> List[QuizQuestion]:
        """Get questions filtered by criteria"""
        filtered_questions = self.questions
        
        if skill_area:
            filtered_questions = [q for q in filtered_questions if q.skill_area == skill_area]
        
        if difficulty:
            filtered_questions = [q for q in filtered_questions if q.difficulty == difficulty]
        
        if question_type:
            filtered_questions = [q for q in filtered_questions if q.question_type == question_type]
        
        return filtered_questions
    
    def get_adaptive_questions(self, metrics: LearningMetrics, count: int = 5) -> List[QuizQuestion]:
        """Get questions adapted to user's learning metrics"""
        # Focus on weak skill areas
        weak_skills = [skill for skill, weakness in metrics.skill_weaknesses.items() if weakness > 0.3]
        
        if weak_skills:
            # Get questions from weak skill areas
            questions = []
            for skill in weak_skills:
                skill_questions = self.get_questions_by_criteria(skill_area=skill)
                questions.extend(skill_questions)
        else:
            # Get questions from all areas
            questions = self.questions
        
        # Adjust difficulty based on performance
        target_difficulty = DifficultyLevel.INTERMEDIATE
        if metrics.accuracy >= 0.8:
            target_difficulty = DifficultyLevel.ADVANCED
        elif metrics.accuracy <= 0.5:
            target_difficulty = DifficultyLevel.BEGINNER
        
        # Filter by difficulty and randomize
        difficulty_questions = [q for q in questions if q.difficulty == target_difficulty]
        if not difficulty_questions:
            difficulty_questions = questions
        
        random.shuffle(difficulty_questions)
        return difficulty_questions[:count]

# ================================
# 🎯 MAIN QUIZ SYSTEM
# ================================

class AdaptiveQuizSystem:
    """Main adaptive quiz system"""
    
    def __init__(self):
        self.question_bank = QuestionBank()
        self.learning_engine = AdaptiveLearningEngine()
        self.gamification = GamificationSystem()
        self.analytics = AnalyticsEngine()
        
        self.current_session = {
            "questions": [],
            "responses": [],
            "current_question_index": 0,
            "start_time": None,
            "end_time": None
        }
        
        self.user_stats = {
            "total_sessions": 0,
            "total_questions": 0,
            "correct_answers": 0,
            "max_streak": 0,
            "current_streak": 0,
            "perfect_quizzes": 0,
            "speed_achievements": 0,
            "skill_mastery": {skill.value: 0.0 for skill in SkillArea}
        }
    
    def start_adaptive_quiz(self, question_count: int = 10):
        """Start an adaptive quiz session"""
        print("\n🎯 ADAPTIVE QUIZ SYSTEM")
        print("=" * 50)
        print("🧠 AI-Powered Adaptive Learning")
        print("🎮 Gamification & Achievements")
        print("📊 Real-time Analytics")
        print("=" * 50)
        
        # Initialize session
        self.current_session = {
            "questions": [],
            "responses": [],
            "current_question_index": 0,
            "start_time": datetime.datetime.now(),
            "end_time": None
        }
        
        # Get adaptive questions
        questions = self.question_bank.get_adaptive_questions(
            self.learning_engine.user_metrics, 
            question_count
        )
        
        if not questions:
            print("❌ No questions available!")
            return
        
        self.current_session["questions"] = questions
        
        print(f"\n🎯 Starting adaptive quiz with {len(questions)} questions")
        print(f"📊 Your current level: {self.gamification.user_level}")
        print(f"🏆 Current points: {self.gamification.user_points}")
        
        # Run quiz
        self._run_quiz_session()
    
    def _run_quiz_session(self):
        """Run the quiz session"""
        questions = self.current_session["questions"]
        
        for i, question in enumerate(questions, 1):
            print(f"\n" + "="*60)
            print(f"📝 QUESTION {i}/{len(questions)}")
            print(f"🎯 Skill: {question.skill_area.value.replace('_', ' ').title()}")
            print(f"⭐ Difficulty: {question.difficulty.name}")
            print(f"⏱️  Estimated time: {question.estimated_time}s")
            print("="*60)
            
            # Ask question
            response = self._ask_question(question)
            
            # Record response
            self.current_session["responses"].append(response)
            self.analytics.record_response(response, question)
            
            # Update gamification
            self._update_gamification(response, question)
            
            # Show immediate feedback
            self._show_immediate_feedback(response, question)
            
            # Update learning metrics
            self.learning_engine.analyze_performance(self.current_session["responses"])
            
            # Short break between questions
            if i < len(questions):
                input("\n⏸️  Press Enter for next question...")
        
        # End session
        self._end_quiz_session()
    
    def _ask_question(self, question: QuizQuestion) -> QuizResponse:
        """Ask a single question and get response"""
        start_time = time.time()
        
        print(f"\n❓ {question.question_text}")
        
        if question.code_snippet:
            print(f"\n💻 Code:")
            print(question.code_snippet)
        
        user_answer = None
        hint_used = False
        attempts = 1
        
        if question.question_type == QuestionType.MULTIPLE_CHOICE:
            user_answer = self._handle_multiple_choice(question)
        elif question.question_type == QuestionType.TRUE_FALSE:
            user_answer = self._handle_true_false(question)
        elif question.question_type == QuestionType.CODE_COMPLETION:
            user_answer = self._handle_code_completion(question)
        elif question.question_type == QuestionType.CODE_DEBUGGING:
            user_answer = self._handle_code_debugging(question)
        elif question.question_type == QuestionType.SCENARIO_BASED:
            user_answer = self._handle_scenario_based(question)
        
        # Check if hint was used
        if hasattr(self, '_hint_used'):
            hint_used = self._hint_used
            delattr(self, '_hint_used')
        
        # Get confidence level
        confidence = self._get_confidence_level()
        
        time_taken = time.time() - start_time
        is_correct = self._check_answer(user_answer, question.correct_answer, question.question_type)
        
        return QuizResponse(
            question_id=question.id,
            user_answer=user_answer,
            is_correct=is_correct,
            time_taken=time_taken,
            hint_used=hint_used,
            attempts=attempts,
            confidence=confidence
        )
    
    def _handle_multiple_choice(self, question: QuizQuestion) -> int:
        """Handle multiple choice question"""
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                choice = input(f"\n👉 Your answer (1-{len(question.options)}, 'h' for hint): ").strip()
                
                if choice.lower() == 'h':
                    print(f"💡 Hint: {question.hint}")
                    self._hint_used = True
                    continue
                
                answer = int(choice) - 1
                if 0 <= answer < len(question.options):
                    return answer
                else:
                    print("❌ Invalid choice! Please try again.")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def _handle_true_false(self, question: QuizQuestion) -> bool:
        """Handle true/false question"""
        while True:
            choice = input("\n👉 Your answer (t/f, 'h' for hint): ").strip().lower()
            
            if choice == 'h':
                print(f"💡 Hint: {question.hint}")
                self._hint_used = True
                continue
            
            if choice in ['t', 'true', '1']:
                return True
            elif choice in ['f', 'false', '0']:
                return False
            else:
                print("❌ Please enter 't' for true or 'f' for false!")
    
    def _handle_code_completion(self, question: QuizQuestion) -> str:
        """Handle code completion question"""
        print("\n💻 Complete the code:")
        
        while True:
            choice = input("\n👉 Your answer ('h' for hint): ").strip()
            
            if choice.lower() == 'h':
                print(f"💡 Hint: {question.hint}")
                self._hint_used = True
                continue
            
            return choice
    
    def _handle_code_debugging(self, question: QuizQuestion) -> str:
        """Handle code debugging question"""
        print("\n🐛 Fix the code:")
        
        while True:
            print("\n👉 Enter your corrected code (type 'DONE' on a new line when finished):")
            print("👉 Type 'h' for hint")
            
            lines = []
            while True:
                line = input()
                if line.strip() == 'DONE':
                    break
                elif line.strip().lower() == 'h':
                    print(f"💡 Hint: {question.hint}")
                    self._hint_used = True
                    continue
                lines.append(line)
            
            return '\n'.join(lines)
    
    def _handle_scenario_based(self, question: QuizQuestion) -> int:
        """Handle scenario-based question"""
        return self._handle_multiple_choice(question)
    
    def _get_confidence_level(self) -> int:
        """Get user's confidence level"""
        while True:
            try:
                confidence = input("\n🎯 How confident are you? (1-5): ").strip()
                conf_level = int(confidence)
                if 1 <= conf_level <= 5:
                    return conf_level
                else:
                    print("❌ Please enter a number between 1 and 5!")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def _check_answer(self, user_answer: Any, correct_answer: Any, question_type: QuestionType) -> bool:
        """Check if answer is correct"""
        if question_type in [QuestionType.MULTIPLE_CHOICE, QuestionType.SCENARIO_BASED]:
            return user_answer == correct_answer
        elif question_type == QuestionType.TRUE_FALSE:
            return user_answer == correct_answer
        elif question_type in [QuestionType.CODE_COMPLETION, QuestionType.CODE_DEBUGGING]:
            # Simple string comparison (in real system, use more sophisticated checking)
            return user_answer.strip().lower() in correct_answer.lower()
        
        return False
    
    def _update_gamification(self, response: QuizResponse, question: QuizQuestion):
        """Update gamification system"""
        if response.is_correct:
            # Calculate points
            base_points = 10
            time_bonus = response.time_taken < question.estimated_time
            
            self.gamification.update_streak(True)
            points = self.gamification.award_points(
                base_points, 
                question.difficulty, 
                time_bonus, 
                self.gamification.streak_count > 0
            )
            
            # Update user stats
            self.user_stats["correct_answers"] += 1
            self.user_stats["current_streak"] += 1
            self.user_stats["max_streak"] = max(self.user_stats["max_streak"], self.user_stats["current_streak"])
        else:
            self.gamification.update_streak(False)
            self.user_stats["current_streak"] = 0
        
        self.user_stats["total_questions"] += 1
        
        # Check for achievements
        achievements = self.gamification.check_achievements(self.user_stats)
        if achievements:
            for achievement in achievements:
                print(f"\n🏆 ACHIEVEMENT UNLOCKED: {achievement.title}")
                print(f"📝 {achievement.description}")
                print(f"🎯 +{achievement.points} points!")
    
    def _show_immediate_feedback(self, response: QuizResponse, question: QuizQuestion):
        """Show immediate feedback"""
        if response.is_correct:
            print("\n✅ Correct!")
            if response.time_taken < question.estimated_time:
                print("⚡ Time bonus earned!")
            if self.gamification.streak_count > 1:
                print(f"🔥 Streak: {self.gamification.streak_count}")
        else:
            print("\n❌ Incorrect!")
            print(f"💡 Correct answer: {self._format_correct_answer(question)}")
        
        print(f"📖 Explanation: {question.explanation}")
        print(f"⏱️  Time taken: {response.time_taken:.1f}s")
    
    def _format_correct_answer(self, question: QuizQuestion) -> str:
        """Format correct answer for display"""
        if question.question_type == QuestionType.MULTIPLE_CHOICE:
            return question.options[question.correct_answer]
        elif question.question_type == QuestionType.TRUE_FALSE:
            return "True" if question.correct_answer else "False"
        else:
            return str(question.correct_answer)
    
    def _end_quiz_session(self):
        """End quiz session and show results"""
        self.current_session["end_time"] = datetime.datetime.now()
        
        # Generate session report
        report = self.analytics.generate_session_report()
        
        print("\n" + "="*60)
        print("🎉 QUIZ SESSION COMPLETED!")
        print("="*60)
        
        # Show results
        print(f"\n📊 SESSION RESULTS:")
        print(f"Questions answered: {report['questions_answered']}")
        print(f"Accuracy: {report['accuracy']:.1f}%")
        print(f"Average response time: {report['avg_response_time']:.1f}s")
        print(f"Questions per minute: {report['questions_per_minute']:.1f}")
        
        # Show gamification results
        progress = self.gamification.get_progress_to_next_level()
        print(f"\n🎮 GAMIFICATION:")
        print(f"Current level: {progress['current_level']}")
        print(f"Points earned this session: {self.gamification.user_points}")
        print(f"Progress to next level: {progress['progress_percentage']:.1f}%")
        
        # Show skill breakdown
        print(f"\n🎯 SKILL BREAKDOWN:")
        for skill, data in report['skill_breakdown'].items():
            print(f"{skill.replace('_', ' ').title()}: {data['accuracy']:.1f}% ({data['questions']} questions)")
        
        # Show visualizations
        print(self.analytics.create_progress_visualization())
        print(self.analytics.create_skill_radar_chart())
        
        # Show recommendations
        self._show_recommendations()
        
        # Update user stats
        self.user_stats["total_sessions"] += 1
        if report['accuracy'] == 100:
            self.user_stats["perfect_quizzes"] += 1
        
        # Save session data (in real system, save to database)
        self._save_session_data()
    
    def _show_recommendations(self):
        """Show personalized recommendations"""
        print(f"\n🎯 PERSONALIZED RECOMMENDATIONS:")
        
        # Difficulty recommendation
        current_difficulty = DifficultyLevel.INTERMEDIATE  # Default
        next_difficulty = self.learning_engine.recommend_next_difficulty(current_difficulty)
        print(f"📈 Recommended difficulty: {next_difficulty.name}")
        
        # Skill focus recommendation
        focus_skills = self.learning_engine.recommend_skill_focus()
        if focus_skills:
            print(f"🎯 Focus on skills: {', '.join(skill.value.replace('_', ' ').title() for skill in focus_skills)}")
        
        # Study suggestions
        if self.learning_engine.user_metrics.accuracy < 0.6:
            print("📚 Suggestion: Review OOP fundamentals and practice more basic concepts")
        elif self.learning_engine.user_metrics.accuracy > 0.8:
            print("🚀 Suggestion: Try advanced OOP challenges and design patterns")
        
        # Time management
        if self.learning_engine.user_metrics.speed < 0.5:
            print("⏱️  Suggestion: Practice more to improve response time")
    
    def _save_session_data(self):
        """Save session data (placeholder)"""
        # In real system, save to database
        session_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "responses": [
                {
                    "question_id": r.question_id,
                    "correct": r.is_correct,
                    "time_taken": r.time_taken,
                    "confidence": r.confidence
                }
                for r in self.current_session["responses"]
            ],
            "final_score": self.gamification.user_points,
            "level": self.gamification.user_level
        }
        
        # Could save to JSON file or database
        pass
    
    def show_main_menu(self):
        """Show main menu"""
        print("\n" + "="*60)
        print("🎯 QUIZ TỔNG HỢP OOP - ADAPTIVE LEARNING SYSTEM")
        print("="*60)
        print("🧠 AI-Powered Adaptive Learning")
        print("🎮 Gamification & Achievements")
        print("📊 Real-time Analytics & Visualization")
        print("🏆 Personalized Learning Path")
        print("="*60)
        
        print("\n🎯 MENU OPTIONS:")
        print("1. 🎯 Start Adaptive Quiz")
        print("2. 🎮 Quick Challenge (5 questions)")
        print("3. 🎯 Skill-Specific Quiz")
        print("4. 📊 View Analytics")
        print("5. 🏆 Achievements")
        print("6. 📈 Progress Report")
        print("7. ⚙️  Settings")
        print("0. 🚪 Exit")
        
        return input("\n👉 Choose option (0-7): ").strip()
    
    def skill_specific_quiz(self):
        """Start skill-specific quiz"""
        print("\n🎯 SKILL-SPECIFIC QUIZ")
        print("=" * 40)
        
        skills = list(SkillArea)
        for i, skill in enumerate(skills, 1):
            print(f"{i}. {skill.value.replace('_', ' ').title()}")
        
        while True:
            try:
                choice = int(input(f"\n👉 Choose skill (1-{len(skills)}): "))
                if 1 <= choice <= len(skills):
                    selected_skill = skills[choice - 1]
                    
                    # Get questions for selected skill
                    questions = self.question_bank.get_questions_by_criteria(skill_area=selected_skill)
                    if questions:
                        self.current_session["questions"] = questions[:5]  # Limit to 5 questions
                        self.current_session["start_time"] = datetime.datetime.now()
                        self._run_quiz_session()
                    else:
                        print("❌ No questions available for this skill!")
                    break
                else:
                    print("❌ Invalid choice!")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    def view_analytics(self):
        """View detailed analytics"""
        print("\n📊 DETAILED ANALYTICS")
        print("=" * 40)
        
        print(f"📈 Overall Statistics:")
        print(f"Total sessions: {self.user_stats['total_sessions']}")
        print(f"Total questions: {self.user_stats['total_questions']}")
        print(f"Correct answers: {self.user_stats['correct_answers']}")
        
        if self.user_stats['total_questions'] > 0:
            accuracy = (self.user_stats['correct_answers'] / self.user_stats['total_questions']) * 100
            print(f"Overall accuracy: {accuracy:.1f}%")
        
        print(f"Max streak: {self.user_stats['max_streak']}")
        print(f"Perfect quizzes: {self.user_stats['perfect_quizzes']}")
        
        # Show skill mastery
        print(f"\n🎯 Skill Mastery:")
        for skill, mastery in self.user_stats['skill_mastery'].items():
            print(f"{skill.replace('_', ' ').title()}: {mastery:.1f}%")
    
    def view_achievements(self):
        """View achievements"""
        print("\n🏆 ACHIEVEMENTS")
        print("=" * 40)
        
        unlocked = [a for a in self.gamification.achievements if a.unlocked]
        locked = [a for a in self.gamification.achievements if not a.unlocked]
        
        print(f"✅ Unlocked ({len(unlocked)}):")
        for achievement in unlocked:
            print(f"{achievement.icon} {achievement.title}")
            print(f"   {achievement.description}")
            print(f"   Unlocked: {achievement.unlock_date.strftime('%Y-%m-%d') if achievement.unlock_date else 'N/A'}")
            print()
        
        print(f"🔒 Locked ({len(locked)}):")
        for achievement in locked:
            print(f"{achievement.icon} {achievement.title}")
            print(f"   {achievement.description}")
            print(f"   Reward: {achievement.points} points")
            print()
    
    def run(self):
        """Run the adaptive quiz system"""
        print("🎉 Welcome to Adaptive OOP Quiz System!")
        print("🧠 AI-powered learning tailored to your progress!")
        
        while True:
            choice = self.show_main_menu()
            
            if choice == "0":
                print("\n👋 Thank you for using Adaptive Quiz System!")
                print("🚀 Keep practicing OOP concepts!")
                break
            elif choice == "1":
                self.start_adaptive_quiz(10)
            elif choice == "2":
                self.start_adaptive_quiz(5)
            elif choice == "3":
                self.skill_specific_quiz()
            elif choice == "4":
                self.view_analytics()
            elif choice == "5":
                self.view_achievements()
            elif choice == "6":
                print("📈 Progress Report - Coming Soon!")
            elif choice == "7":
                print("⚙️  Settings - Coming Soon!")
            else:
                print("❌ Invalid choice! Please try again.")
            
            if choice != "0":
                input("\n⏸️  Press Enter to continue...")

# ================================
# 🚀 MAIN EXECUTION
# ================================

if __name__ == "__main__":
    quiz_system = AdaptiveQuizSystem()
    quiz_system.run() 