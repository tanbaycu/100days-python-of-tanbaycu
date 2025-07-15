#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🏢 DỰ ÁN THỰC HÀNH NÂNG CAO - ENTERPRISE ARCHITECTURE
=====================================================

Ngày 15-17: Object-Oriented Programming - Advanced Project
Tác giả: TanBayCu Learning System
Mô tả: Enterprise-level OOP project với design patterns, architecture và testing

🎯 MỤC TIÊU:
- Xây dựng enterprise-level application
- Áp dụng design patterns nâng cao
- Implement clean architecture
- Comprehensive testing strategy
- Performance optimization
- Security best practices

🏗️ KIẾN TRÚC:
✅ Clean Architecture (Layers)
✅ Design Patterns (Strategy, Factory, Observer, etc.)
✅ Dependency Injection
✅ Event-Driven Architecture
✅ SOLID Principles
✅ Testing Pyramid
"""

import asyncio
import json
import logging
import threading
import time
import uuid
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Any, Callable, Union, Generic, TypeVar
import hashlib
import pickle
import sqlite3
from collections import defaultdict, deque
import concurrent.futures
from functools import wraps, lru_cache
import weakref

# ================================
# 🏗️ ENTERPRISE ARCHITECTURE FOUNDATION
# ================================

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('enterprise_app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Type Variables
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# ================================
# 🎯 CORE EXCEPTIONS
# ================================

class EnterpriseException(Exception):
    """Base enterprise exception"""
    def __init__(self, message: str, error_code: str = None, details: Dict = None):
        super().__init__(message)
        self.error_code = error_code or "UNKNOWN_ERROR"
        self.details = details or {}
        self.timestamp = datetime.now()

class ValidationException(EnterpriseException):
    """Validation error"""
    pass

class SecurityException(EnterpriseException):
    """Security error"""
    pass

class BusinessLogicException(EnterpriseException):
    """Business logic error"""
    pass

class InfrastructureException(EnterpriseException):
    """Infrastructure error"""
    pass

# ================================
# 🏛️ DOMAIN LAYER
# ================================

class EntityStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    DELETED = "deleted"

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class BaseEntity:
    """Base entity with common fields"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    status: EntityStatus = EntityStatus.ACTIVE
    version: int = 1
    
    def update(self):
        """Update timestamp and version"""
        self.updated_at = datetime.now()
        self.version += 1

@dataclass
class User(BaseEntity):
    """User domain entity"""
    username: str = ""
    email: str = ""
    password_hash: str = ""
    role: str = "user"
    last_login: Optional[datetime] = None
    login_attempts: int = 0
    is_locked: bool = False
    
    def authenticate(self, password: str) -> bool:
        """Authenticate user"""
        if self.is_locked:
            raise SecurityException("Account is locked", "ACCOUNT_LOCKED")
        
        # Simple hash comparison (in real app, use proper password hashing)
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if password_hash == self.password_hash:
            self.last_login = datetime.now()
            self.login_attempts = 0
            self.update()
            return True
        else:
            self.login_attempts += 1
            if self.login_attempts >= 3:
                self.is_locked = True
            self.update()
            return False
    
    def change_password(self, old_password: str, new_password: str):
        """Change user password"""
        if not self.authenticate(old_password):
            raise SecurityException("Invalid current password", "INVALID_PASSWORD")
        
        self.password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        self.update()

@dataclass
class Task(BaseEntity):
    """Task domain entity"""
    title: str = ""
    description: str = ""
    assignee_id: str = ""
    reporter_id: str = ""
    priority: Priority = Priority.MEDIUM
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    estimated_hours: float = 0.0
    actual_hours: float = 0.0
    tags: List[str] = field(default_factory=list)
    
    @property
    def is_completed(self) -> bool:
        return self.completed_at is not None
    
    @property
    def is_overdue(self) -> bool:
        return (self.due_date and 
                datetime.now() > self.due_date and 
                not self.is_completed)
    
    def complete(self, actual_hours: float = 0.0):
        """Mark task as completed"""
        if self.is_completed:
            raise BusinessLogicException("Task already completed", "TASK_COMPLETED")
        
        self.completed_at = datetime.now()
        self.actual_hours = actual_hours
        self.update()
    
    def estimate_completion_time(self) -> Optional[datetime]:
        """Estimate completion time based on priority and hours"""
        if self.is_completed:
            return self.completed_at
        
        base_time = datetime.now()
        if self.estimated_hours > 0:
            # Add estimated hours plus buffer based on priority
            buffer_multiplier = {
                Priority.LOW: 1.5,
                Priority.MEDIUM: 1.3,
                Priority.HIGH: 1.1,
                Priority.CRITICAL: 1.0
            }
            total_hours = self.estimated_hours * buffer_multiplier[self.priority]
            return base_time + timedelta(hours=total_hours)
        
        return None

@dataclass
class Project(BaseEntity):
    """Project domain entity"""
    name: str = ""
    description: str = ""
    owner_id: str = ""
    team_members: List[str] = field(default_factory=list)
    start_date: datetime = field(default_factory=datetime.now)
    end_date: Optional[datetime] = None
    budget: float = 0.0
    spent_budget: float = 0.0
    
    @property
    def is_active(self) -> bool:
        return (self.status == EntityStatus.ACTIVE and
                (not self.end_date or datetime.now() <= self.end_date))
    
    @property
    def budget_utilization(self) -> float:
        return (self.spent_budget / self.budget * 100) if self.budget > 0 else 0.0
    
    def add_team_member(self, user_id: str):
        """Add team member to project"""
        if user_id not in self.team_members:
            self.team_members.append(user_id)
            self.update()
    
    def remove_team_member(self, user_id: str):
        """Remove team member from project"""
        if user_id in self.team_members:
            self.team_members.remove(user_id)
            self.update()
    
    def add_expense(self, amount: float, description: str = ""):
        """Add expense to project"""
        if amount <= 0:
            raise ValidationException("Expense amount must be positive", "INVALID_AMOUNT")
        
        if self.spent_budget + amount > self.budget:
            raise BusinessLogicException("Expense exceeds budget", "BUDGET_EXCEEDED")
        
        self.spent_budget += amount
        self.update()

# ================================
# 🔧 APPLICATION LAYER
# ================================

class Command(ABC):
    """Command pattern interface"""
    @abstractmethod
    def execute(self) -> Any:
        pass
    
    @abstractmethod
    def undo(self) -> Any:
        pass

class CreateUserCommand(Command):
    """Create user command"""
    def __init__(self, user_service, username: str, email: str, password: str):
        self.user_service = user_service
        self.username = username
        self.email = email
        self.password = password
        self.created_user = None
    
    def execute(self) -> User:
        self.created_user = self.user_service.create_user(
            self.username, self.email, self.password
        )
        return self.created_user
    
    def undo(self) -> None:
        if self.created_user:
            self.user_service.delete_user(self.created_user.id)

class CreateTaskCommand(Command):
    """Create task command"""
    def __init__(self, task_service, title: str, description: str, 
                 assignee_id: str, reporter_id: str, priority: Priority):
        self.task_service = task_service
        self.title = title
        self.description = description
        self.assignee_id = assignee_id
        self.reporter_id = reporter_id
        self.priority = priority
        self.created_task = None
    
    def execute(self) -> Task:
        self.created_task = self.task_service.create_task(
            self.title, self.description, self.assignee_id, 
            self.reporter_id, self.priority
        )
        return self.created_task
    
    def undo(self) -> None:
        if self.created_task:
            self.task_service.delete_task(self.created_task.id)

class CommandInvoker:
    """Command invoker with undo/redo support"""
    def __init__(self):
        self.history: List[Command] = []
        self.current_index = -1
    
    def execute(self, command: Command) -> Any:
        """Execute command and add to history"""
        result = command.execute()
        
        # Remove any commands after current index
        self.history = self.history[:self.current_index + 1]
        
        # Add new command
        self.history.append(command)
        self.current_index += 1
        
        return result
    
    def undo(self) -> bool:
        """Undo last command"""
        if self.current_index >= 0:
            command = self.history[self.current_index]
            command.undo()
            self.current_index -= 1
            return True
        return False
    
    def redo(self) -> bool:
        """Redo next command"""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            command = self.history[self.current_index]
            command.execute()
            return True
        return False

# ================================
# 🏪 REPOSITORY PATTERN
# ================================

class Repository(ABC, Generic[T]):
    """Generic repository interface"""
    
    @abstractmethod
    def save(self, entity: T) -> T:
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[T]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        pass
    
    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        pass
    
    @abstractmethod
    def find_by_criteria(self, criteria: Dict[str, Any]) -> List[T]:
        pass

class InMemoryRepository(Repository[T]):
    """In-memory repository implementation"""
    
    def __init__(self):
        self._data: Dict[str, T] = {}
        self._lock = threading.RLock()
    
    def save(self, entity: T) -> T:
        with self._lock:
            if hasattr(entity, 'update'):
                entity.update()
            self._data[entity.id] = entity
            return entity
    
    def find_by_id(self, entity_id: str) -> Optional[T]:
        with self._lock:
            return self._data.get(entity_id)
    
    def find_all(self) -> List[T]:
        with self._lock:
            return list(self._data.values())
    
    def delete(self, entity_id: str) -> bool:
        with self._lock:
            if entity_id in self._data:
                del self._data[entity_id]
                return True
            return False
    
    def find_by_criteria(self, criteria: Dict[str, Any]) -> List[T]:
        with self._lock:
            results = []
            for entity in self._data.values():
                match = True
                for key, value in criteria.items():
                    if not hasattr(entity, key) or getattr(entity, key) != value:
                        match = False
                        break
                if match:
                    results.append(entity)
            return results

class SQLiteRepository(Repository[T]):
    """SQLite repository implementation"""
    
    def __init__(self, db_path: str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name
        self._init_db()
    
    def _init_db(self):
        """Initialize database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id TEXT PRIMARY KEY,
                    data BLOB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    
    def save(self, entity: T) -> T:
        if hasattr(entity, 'update'):
            entity.update()
        
        data = pickle.dumps(entity)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(f'''
                INSERT OR REPLACE INTO {self.table_name} 
                (id, data, updated_at) VALUES (?, ?, ?)
            ''', (entity.id, data, datetime.now()))
        
        return entity
    
    def find_by_id(self, entity_id: str) -> Optional[T]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(f'''
                SELECT data FROM {self.table_name} WHERE id = ?
            ''', (entity_id,))
            
            row = cursor.fetchone()
            if row:
                return pickle.loads(row[0])
            return None
    
    def find_all(self) -> List[T]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(f'SELECT data FROM {self.table_name}')
            return [pickle.loads(row[0]) for row in cursor.fetchall()]
    
    def delete(self, entity_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(f'''
                DELETE FROM {self.table_name} WHERE id = ?
            ''', (entity_id,))
            return cursor.rowcount > 0
    
    def find_by_criteria(self, criteria: Dict[str, Any]) -> List[T]:
        # For SQLite, we need to load all and filter (not efficient for large datasets)
        all_entities = self.find_all()
        results = []
        
        for entity in all_entities:
            match = True
            for key, value in criteria.items():
                if not hasattr(entity, key) or getattr(entity, key) != value:
                    match = False
                    break
            if match:
                results.append(entity)
        
        return results

# ================================
# 🎯 SERVICE LAYER
# ================================

class EventBus:
    """Event bus for decoupled communication"""
    
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)
        self._lock = threading.RLock()
    
    def subscribe(self, event_type: str, handler: Callable):
        """Subscribe to event type"""
        with self._lock:
            self._subscribers[event_type].append(handler)
    
    def unsubscribe(self, event_type: str, handler: Callable):
        """Unsubscribe from event type"""
        with self._lock:
            if handler in self._subscribers[event_type]:
                self._subscribers[event_type].remove(handler)
    
    def publish(self, event_type: str, data: Any = None):
        """Publish event"""
        with self._lock:
            handlers = self._subscribers[event_type].copy()
        
        for handler in handlers:
            try:
                handler(data)
            except Exception as e:
                logger.error(f"Error handling event {event_type}: {e}")

class CacheService:
    """Cache service with TTL support"""
    
    def __init__(self, default_ttl: int = 3600):
        self.default_ttl = default_ttl
        self._cache: Dict[str, Any] = {}
        self._expiry: Dict[str, datetime] = {}
        self._lock = threading.RLock()
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value"""
        with self._lock:
            if key in self._cache:
                if datetime.now() < self._expiry[key]:
                    return self._cache[key]
                else:
                    # Expired
                    del self._cache[key]
                    del self._expiry[key]
            return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Set cached value"""
        with self._lock:
            self._cache[key] = value
            ttl = ttl or self.default_ttl
            self._expiry[key] = datetime.now() + timedelta(seconds=ttl)
    
    def delete(self, key: str):
        """Delete cached value"""
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                del self._expiry[key]
    
    def clear(self):
        """Clear all cache"""
        with self._lock:
            self._cache.clear()
            self._expiry.clear()

def cached(ttl: int = 3600):
    """Caching decorator"""
    def decorator(func):
        cache = CacheService(ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            # Try to get from cache
            result = cache.get(key)
            if result is not None:
                return result
            
            # Execute function and cache result
            result = func(*args, **kwargs)
            cache.set(key, result)
            return result
        
        return wrapper
    return decorator

class UserService:
    """User service with business logic"""
    
    def __init__(self, user_repository: Repository[User], event_bus: EventBus):
        self.user_repository = user_repository
        self.event_bus = event_bus
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def create_user(self, username: str, email: str, password: str) -> User:
        """Create new user"""
        # Validation
        if not username or len(username) < 3:
            raise ValidationException("Username must be at least 3 characters", "INVALID_USERNAME")
        
        if not email or "@" not in email:
            raise ValidationException("Invalid email format", "INVALID_EMAIL")
        
        if not password or len(password) < 6:
            raise ValidationException("Password must be at least 6 characters", "INVALID_PASSWORD")
        
        # Check if user exists
        existing_users = self.user_repository.find_by_criteria({"username": username})
        if existing_users:
            raise BusinessLogicException("Username already exists", "USERNAME_EXISTS")
        
        existing_emails = self.user_repository.find_by_criteria({"email": email})
        if existing_emails:
            raise BusinessLogicException("Email already exists", "EMAIL_EXISTS")
        
        # Create user
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        
        saved_user = self.user_repository.save(user)
        self.event_bus.publish("user_created", saved_user)
        self.logger.info(f"User created: {username}")
        
        return saved_user
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user"""
        users = self.user_repository.find_by_criteria({"username": username})
        if not users:
            return None
        
        user = users[0]
        if user.authenticate(password):
            self.user_repository.save(user)  # Update last login
            self.event_bus.publish("user_authenticated", user)
            self.logger.info(f"User authenticated: {username}")
            return user
        
        self.user_repository.save(user)  # Update failed attempts
        self.event_bus.publish("authentication_failed", {"username": username})
        return None
    
    @cached(ttl=300)  # Cache for 5 minutes
    def get_user_statistics(self, user_id: str) -> Dict[str, Any]:
        """Get user statistics"""
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {}
        
        return {
            "username": user.username,
            "created_at": user.created_at,
            "last_login": user.last_login,
            "login_attempts": user.login_attempts,
            "is_locked": user.is_locked,
            "status": user.status.value
        }
    
    def delete_user(self, user_id: str) -> bool:
        """Delete user"""
        user = self.user_repository.find_by_id(user_id)
        if user:
            result = self.user_repository.delete(user_id)
            if result:
                self.event_bus.publish("user_deleted", user)
                self.logger.info(f"User deleted: {user.username}")
            return result
        return False

class TaskService:
    """Task service with business logic"""
    
    def __init__(self, task_repository: Repository[Task], 
                 user_repository: Repository[User], event_bus: EventBus):
        self.task_repository = task_repository
        self.user_repository = user_repository
        self.event_bus = event_bus
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def create_task(self, title: str, description: str, assignee_id: str, 
                   reporter_id: str, priority: Priority) -> Task:
        """Create new task"""
        # Validation
        if not title or len(title) < 3:
            raise ValidationException("Title must be at least 3 characters", "INVALID_TITLE")
        
        # Verify users exist
        if not self.user_repository.find_by_id(assignee_id):
            raise ValidationException("Assignee not found", "ASSIGNEE_NOT_FOUND")
        
        if not self.user_repository.find_by_id(reporter_id):
            raise ValidationException("Reporter not found", "REPORTER_NOT_FOUND")
        
        # Create task
        task = Task(
            title=title,
            description=description,
            assignee_id=assignee_id,
            reporter_id=reporter_id,
            priority=priority
        )
        
        saved_task = self.task_repository.save(task)
        self.event_bus.publish("task_created", saved_task)
        self.logger.info(f"Task created: {title}")
        
        return saved_task
    
    def assign_task(self, task_id: str, assignee_id: str) -> Task:
        """Assign task to user"""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValidationException("Task not found", "TASK_NOT_FOUND")
        
        if not self.user_repository.find_by_id(assignee_id):
            raise ValidationException("Assignee not found", "ASSIGNEE_NOT_FOUND")
        
        old_assignee = task.assignee_id
        task.assignee_id = assignee_id
        
        saved_task = self.task_repository.save(task)
        self.event_bus.publish("task_assigned", {
            "task": saved_task,
            "old_assignee": old_assignee,
            "new_assignee": assignee_id
        })
        
        return saved_task
    
    def complete_task(self, task_id: str, actual_hours: float = 0.0) -> Task:
        """Complete task"""
        task = self.task_repository.find_by_id(task_id)
        if not task:
            raise ValidationException("Task not found", "TASK_NOT_FOUND")
        
        task.complete(actual_hours)
        saved_task = self.task_repository.save(task)
        
        self.event_bus.publish("task_completed", saved_task)
        self.logger.info(f"Task completed: {task.title}")
        
        return saved_task
    
    @cached(ttl=600)  # Cache for 10 minutes
    def get_task_statistics(self) -> Dict[str, Any]:
        """Get task statistics"""
        all_tasks = self.task_repository.find_all()
        
        total_tasks = len(all_tasks)
        completed_tasks = len([t for t in all_tasks if t.is_completed])
        overdue_tasks = len([t for t in all_tasks if t.is_overdue])
        
        priority_distribution = {
            Priority.LOW: 0,
            Priority.MEDIUM: 0,
            Priority.HIGH: 0,
            Priority.CRITICAL: 0
        }
        
        for task in all_tasks:
            priority_distribution[task.priority] += 1
        
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "overdue_tasks": overdue_tasks,
            "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
            "priority_distribution": {p.value: count for p, count in priority_distribution.items()}
        }
    
    def delete_task(self, task_id: str) -> bool:
        """Delete task"""
        task = self.task_repository.find_by_id(task_id)
        if task:
            result = self.task_repository.delete(task_id)
            if result:
                self.event_bus.publish("task_deleted", task)
                self.logger.info(f"Task deleted: {task.title}")
            return result
        return False

class ProjectService:
    """Project service with business logic"""
    
    def __init__(self, project_repository: Repository[Project], 
                 user_repository: Repository[User], 
                 task_repository: Repository[Task], event_bus: EventBus):
        self.project_repository = project_repository
        self.user_repository = user_repository
        self.task_repository = task_repository
        self.event_bus = event_bus
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def create_project(self, name: str, description: str, owner_id: str, 
                      budget: float = 0.0) -> Project:
        """Create new project"""
        # Validation
        if not name or len(name) < 3:
            raise ValidationException("Name must be at least 3 characters", "INVALID_NAME")
        
        if not self.user_repository.find_by_id(owner_id):
            raise ValidationException("Owner not found", "OWNER_NOT_FOUND")
        
        if budget < 0:
            raise ValidationException("Budget cannot be negative", "INVALID_BUDGET")
        
        # Create project
        project = Project(
            name=name,
            description=description,
            owner_id=owner_id,
            budget=budget
        )
        
        saved_project = self.project_repository.save(project)
        self.event_bus.publish("project_created", saved_project)
        self.logger.info(f"Project created: {name}")
        
        return saved_project
    
    def get_project_tasks(self, project_id: str) -> List[Task]:
        """Get all tasks for a project"""
        # In a real system, tasks would have project_id field
        # For demo, we'll return all tasks
        return self.task_repository.find_all()
    
    @cached(ttl=300)
    def get_project_progress(self, project_id: str) -> Dict[str, Any]:
        """Get project progress"""
        project = self.project_repository.find_by_id(project_id)
        if not project:
            return {}
        
        tasks = self.get_project_tasks(project_id)
        total_tasks = len(tasks)
        completed_tasks = len([t for t in tasks if t.is_completed])
        
        return {
            "project_name": project.name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
            "budget_utilization": project.budget_utilization,
            "is_active": project.is_active
        }

# ================================
# 🎮 STRATEGY PATTERN FOR NOTIFICATIONS
# ================================

class NotificationStrategy(ABC):
    """Notification strategy interface"""
    
    @abstractmethod
    def send_notification(self, recipient: str, message: str, data: Dict = None):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    """Email notification strategy"""
    
    def send_notification(self, recipient: str, message: str, data: Dict = None):
        logger.info(f"📧 EMAIL to {recipient}: {message}")
        # In real implementation, send actual email

class SMSNotificationStrategy(NotificationStrategy):
    """SMS notification strategy"""
    
    def send_notification(self, recipient: str, message: str, data: Dict = None):
        logger.info(f"📱 SMS to {recipient}: {message}")
        # In real implementation, send actual SMS

class PushNotificationStrategy(NotificationStrategy):
    """Push notification strategy"""
    
    def send_notification(self, recipient: str, message: str, data: Dict = None):
        logger.info(f"🔔 PUSH to {recipient}: {message}")
        # In real implementation, send push notification

class NotificationService:
    """Notification service using strategy pattern"""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.strategies: Dict[str, NotificationStrategy] = {
            "email": EmailNotificationStrategy(),
            "sms": SMSNotificationStrategy(),
            "push": PushNotificationStrategy()
        }
        self.user_preferences: Dict[str, List[str]] = defaultdict(lambda: ["email"])
        
        # Subscribe to events
        self.event_bus.subscribe("user_created", self._handle_user_created)
        self.event_bus.subscribe("task_assigned", self._handle_task_assigned)
        self.event_bus.subscribe("task_completed", self._handle_task_completed)
    
    def set_user_preferences(self, user_id: str, preferences: List[str]):
        """Set notification preferences for user"""
        valid_preferences = [p for p in preferences if p in self.strategies]
        self.user_preferences[user_id] = valid_preferences
    
    def send_notification(self, user_id: str, message: str, data: Dict = None):
        """Send notification to user"""
        preferences = self.user_preferences[user_id]
        
        for preference in preferences:
            strategy = self.strategies[preference]
            strategy.send_notification(user_id, message, data)
    
    def _handle_user_created(self, user: User):
        """Handle user created event"""
        self.send_notification(
            user.id,
            f"Welcome {user.username}! Your account has been created.",
            {"event": "user_created"}
        )
    
    def _handle_task_assigned(self, data: Dict):
        """Handle task assigned event"""
        task = data["task"]
        self.send_notification(
            task.assignee_id,
            f"New task assigned: {task.title}",
            {"event": "task_assigned", "task_id": task.id}
        )
    
    def _handle_task_completed(self, task: Task):
        """Handle task completed event"""
        self.send_notification(
            task.reporter_id,
            f"Task completed: {task.title}",
            {"event": "task_completed", "task_id": task.id}
        )

# ================================
# 🏭 FACTORY PATTERN FOR SERVICES
# ================================

class ServiceFactory:
    """Factory for creating services"""
    
    def __init__(self):
        self._event_bus = EventBus()
        self._cache_service = CacheService()
        
        # Repositories
        self._user_repository = InMemoryRepository[User]()
        self._task_repository = InMemoryRepository[Task]()
        self._project_repository = InMemoryRepository[Project]()
        
        # Services
        self._user_service = None
        self._task_service = None
        self._project_service = None
        self._notification_service = None
    
    @property
    def event_bus(self) -> EventBus:
        return self._event_bus
    
    @property
    def cache_service(self) -> CacheService:
        return self._cache_service
    
    def create_user_service(self) -> UserService:
        """Create user service"""
        if not self._user_service:
            self._user_service = UserService(self._user_repository, self._event_bus)
        return self._user_service
    
    def create_task_service(self) -> TaskService:
        """Create task service"""
        if not self._task_service:
            self._task_service = TaskService(
                self._task_repository, 
                self._user_repository, 
                self._event_bus
            )
        return self._task_service
    
    def create_project_service(self) -> ProjectService:
        """Create project service"""
        if not self._project_service:
            self._project_service = ProjectService(
                self._project_repository,
                self._user_repository,
                self._task_repository,
                self._event_bus
            )
        return self._project_service
    
    def create_notification_service(self) -> NotificationService:
        """Create notification service"""
        if not self._notification_service:
            self._notification_service = NotificationService(self._event_bus)
        return self._notification_service

# ================================
# 🧪 COMPREHENSIVE TESTING FRAMEWORK
# ================================

class TestCase:
    """Base test case"""
    
    def __init__(self, name: str):
        self.name = name
        self.setup_called = False
        self.teardown_called = False
    
    def setup(self):
        """Setup test"""
        self.setup_called = True
    
    def teardown(self):
        """Teardown test"""
        self.teardown_called = True
    
    def assert_equal(self, actual, expected, message: str = ""):
        """Assert equal"""
        if actual != expected:
            raise AssertionError(f"{message}: Expected {expected}, got {actual}")
    
    def assert_true(self, condition: bool, message: str = ""):
        """Assert true"""
        if not condition:
            raise AssertionError(f"{message}: Expected True, got False")
    
    def assert_false(self, condition: bool, message: str = ""):
        """Assert false"""
        if condition:
            raise AssertionError(f"{message}: Expected False, got True")
    
    def assert_raises(self, exception_type: type, func: Callable, *args, **kwargs):
        """Assert raises exception"""
        try:
            func(*args, **kwargs)
            raise AssertionError(f"Expected {exception_type.__name__} to be raised")
        except exception_type:
            pass  # Expected
        except Exception as e:
            raise AssertionError(f"Expected {exception_type.__name__}, got {type(e).__name__}")

class TestRunner:
    """Test runner for comprehensive testing"""
    
    def __init__(self):
        self.test_cases: List[TestCase] = []
        self.results: List[Dict] = []
    
    def add_test_case(self, test_case: TestCase):
        """Add test case"""
        self.test_cases.append(test_case)
    
    def run_all_tests(self):
        """Run all test cases"""
        print("\n🧪 RUNNING COMPREHENSIVE TESTS")
        print("=" * 50)
        
        passed = 0
        failed = 0
        
        for test_case in self.test_cases:
            try:
                # Setup
                test_case.setup()
                
                # Run test methods
                test_methods = [method for method in dir(test_case) 
                              if method.startswith('test_') and callable(getattr(test_case, method))]
                
                for method_name in test_methods:
                    method = getattr(test_case, method_name)
                    start_time = time.time()
                    
                    try:
                        method()
                        execution_time = time.time() - start_time
                        
                        print(f"✅ {test_case.name}.{method_name} ({execution_time:.3f}s)")
                        self.results.append({
                            "test": f"{test_case.name}.{method_name}",
                            "status": "PASSED",
                            "execution_time": execution_time
                        })
                        passed += 1
                        
                    except Exception as e:
                        execution_time = time.time() - start_time
                        
                        print(f"❌ {test_case.name}.{method_name} ({execution_time:.3f}s)")
                        print(f"    Error: {e}")
                        self.results.append({
                            "test": f"{test_case.name}.{method_name}",
                            "status": "FAILED",
                            "error": str(e),
                            "execution_time": execution_time
                        })
                        failed += 1
                
                # Teardown
                test_case.teardown()
                
            except Exception as e:
                print(f"❌ {test_case.name} (Setup/Teardown Error)")
                print(f"    Error: {e}")
                failed += 1
        
        print(f"\n📊 Test Results: {passed} passed, {failed} failed")
        return passed, failed

# ================================
# 🧪 SPECIFIC TEST CASES
# ================================

class UserServiceTest(TestCase):
    """Test cases for UserService"""
    
    def __init__(self):
        super().__init__("UserService")
        self.factory = None
        self.user_service = None
    
    def setup(self):
        super().setup()
        self.factory = ServiceFactory()
        self.user_service = self.factory.create_user_service()
    
    def test_create_user_success(self):
        """Test successful user creation"""
        user = self.user_service.create_user("testuser", "test@example.com", "password123")
        
        self.assert_equal(user.username, "testuser")
        self.assert_equal(user.email, "test@example.com")
        self.assert_true(len(user.password_hash) > 0)
    
    def test_create_user_invalid_username(self):
        """Test user creation with invalid username"""
        self.assert_raises(
            ValidationException,
            self.user_service.create_user,
            "ab", "test@example.com", "password123"
        )
    
    def test_create_user_duplicate_username(self):
        """Test user creation with duplicate username"""
        self.user_service.create_user("testuser", "test1@example.com", "password123")
        
        self.assert_raises(
            BusinessLogicException,
            self.user_service.create_user,
            "testuser", "test2@example.com", "password123"
        )
    
    def test_authenticate_user_success(self):
        """Test successful authentication"""
        user = self.user_service.create_user("testuser", "test@example.com", "password123")
        
        auth_user = self.user_service.authenticate_user("testuser", "password123")
        self.assert_equal(auth_user.id, user.id)
    
    def test_authenticate_user_wrong_password(self):
        """Test authentication with wrong password"""
        self.user_service.create_user("testuser", "test@example.com", "password123")
        
        auth_user = self.user_service.authenticate_user("testuser", "wrongpassword")
        self.assert_equal(auth_user, None)

class TaskServiceTest(TestCase):
    """Test cases for TaskService"""
    
    def __init__(self):
        super().__init__("TaskService")
        self.factory = None
        self.user_service = None
        self.task_service = None
        self.test_user = None
    
    def setup(self):
        super().setup()
        self.factory = ServiceFactory()
        self.user_service = self.factory.create_user_service()
        self.task_service = self.factory.create_task_service()
        
        # Create test user
        self.test_user = self.user_service.create_user("testuser", "test@example.com", "password123")
    
    def test_create_task_success(self):
        """Test successful task creation"""
        task = self.task_service.create_task(
            "Test Task",
            "Test Description",
            self.test_user.id,
            self.test_user.id,
            Priority.MEDIUM
        )
        
        self.assert_equal(task.title, "Test Task")
        self.assert_equal(task.priority, Priority.MEDIUM)
        self.assert_false(task.is_completed)
    
    def test_create_task_invalid_title(self):
        """Test task creation with invalid title"""
        self.assert_raises(
            ValidationException,
            self.task_service.create_task,
            "ab", "Description", self.test_user.id, self.test_user.id, Priority.MEDIUM
        )
    
    def test_complete_task(self):
        """Test task completion"""
        task = self.task_service.create_task(
            "Test Task",
            "Test Description",
            self.test_user.id,
            self.test_user.id,
            Priority.MEDIUM
        )
        
        completed_task = self.task_service.complete_task(task.id, 5.0)
        
        self.assert_true(completed_task.is_completed)
        self.assert_equal(completed_task.actual_hours, 5.0)
    
    def test_assign_task(self):
        """Test task assignment"""
        user2 = self.user_service.create_user("user2", "user2@example.com", "password123")
        
        task = self.task_service.create_task(
            "Test Task",
            "Test Description",
            self.test_user.id,
            self.test_user.id,
            Priority.MEDIUM
        )
        
        assigned_task = self.task_service.assign_task(task.id, user2.id)
        self.assert_equal(assigned_task.assignee_id, user2.id)

class IntegrationTest(TestCase):
    """Integration test cases"""
    
    def __init__(self):
        super().__init__("Integration")
        self.factory = None
        self.services = {}
    
    def setup(self):
        super().setup()
        self.factory = ServiceFactory()
        self.services = {
            "user": self.factory.create_user_service(),
            "task": self.factory.create_task_service(),
            "project": self.factory.create_project_service(),
            "notification": self.factory.create_notification_service()
        }
    
    def test_full_workflow(self):
        """Test complete workflow"""
        # Create users
        user1 = self.services["user"].create_user("user1", "user1@example.com", "password123")
        user2 = self.services["user"].create_user("user2", "user2@example.com", "password123")
        
        # Create project
        project = self.services["project"].create_project(
            "Test Project",
            "Test Description",
            user1.id,
            10000.0
        )
        
        # Create task
        task = self.services["task"].create_task(
            "Test Task",
            "Test Description",
            user2.id,
            user1.id,
            Priority.HIGH
        )
        
        # Complete task
        completed_task = self.services["task"].complete_task(task.id, 8.0)
        
        # Verify
        self.assert_true(completed_task.is_completed)
        self.assert_equal(completed_task.actual_hours, 8.0)
        self.assert_equal(project.owner_id, user1.id)
    
    def test_event_system(self):
        """Test event system"""
        events_received = []
        
        def event_handler(data):
            events_received.append(data)
        
        # Subscribe to events
        self.factory.event_bus.subscribe("user_created", event_handler)
        self.factory.event_bus.subscribe("task_created", event_handler)
        
        # Create user and task
        user = self.services["user"].create_user("eventuser", "event@example.com", "password123")
        task = self.services["task"].create_task(
            "Event Task",
            "Event Description",
            user.id,
            user.id,
            Priority.LOW
        )
        
        # Verify events
        self.assert_equal(len(events_received), 2)
        self.assert_equal(events_received[0].username, "eventuser")
        self.assert_equal(events_received[1].title, "Event Task")

# ================================
# 🎯 PERFORMANCE TESTING
# ================================

class PerformanceTest(TestCase):
    """Performance test cases"""
    
    def __init__(self):
        super().__init__("Performance")
        self.factory = None
        self.services = {}
    
    def setup(self):
        super().setup()
        self.factory = ServiceFactory()
        self.services = {
            "user": self.factory.create_user_service(),
            "task": self.factory.create_task_service()
        }
    
    def test_user_creation_performance(self):
        """Test user creation performance"""
        start_time = time.time()
        
        # Create 100 users
        for i in range(100):
            self.services["user"].create_user(
                f"user{i}",
                f"user{i}@example.com",
                "password123"
            )
        
        execution_time = time.time() - start_time
        
        # Should complete in less than 1 second
        self.assert_true(execution_time < 1.0, f"User creation took {execution_time:.3f}s")
    
    def test_task_creation_performance(self):
        """Test task creation performance"""
        # Create test user
        user = self.services["user"].create_user("perfuser", "perf@example.com", "password123")
        
        start_time = time.time()
        
        # Create 1000 tasks
        for i in range(1000):
            self.services["task"].create_task(
                f"Task {i}",
                f"Description {i}",
                user.id,
                user.id,
                Priority.MEDIUM
            )
        
        execution_time = time.time() - start_time
        
        # Should complete in less than 2 seconds
        self.assert_true(execution_time < 2.0, f"Task creation took {execution_time:.3f}s")
    
    def test_cache_performance(self):
        """Test cache performance"""
        cache = self.factory.cache_service
        
        # Test cache set performance
        start_time = time.time()
        for i in range(10000):
            cache.set(f"key{i}", f"value{i}")
        set_time = time.time() - start_time
        
        # Test cache get performance
        start_time = time.time()
        for i in range(10000):
            cache.get(f"key{i}")
        get_time = time.time() - start_time
        
        # Should complete quickly
        self.assert_true(set_time < 0.5, f"Cache set took {set_time:.3f}s")
        self.assert_true(get_time < 0.5, f"Cache get took {get_time:.3f}s")

# ================================
# 🎯 MAIN APPLICATION
# ================================

class EnterpriseApplication:
    """Main enterprise application"""
    
    def __init__(self):
        self.factory = ServiceFactory()
        self.services = {
            "user": self.factory.create_user_service(),
            "task": self.factory.create_task_service(),
            "project": self.factory.create_project_service(),
            "notification": self.factory.create_notification_service()
        }
        self.command_invoker = CommandInvoker()
        self.current_user = None
    
    def show_main_menu(self):
        """Show main menu"""
        print("\n" + "="*60)
        print("🏢 ENTERPRISE APPLICATION - ADVANCED OOP PROJECT")
        print("="*60)
        print("🏗️  Clean Architecture & Design Patterns")
        print("🧪 Comprehensive Testing Framework")
        print("🚀 Performance Optimization")
        print("🔒 Security Best Practices")
        print("="*60)
        
        print("\n🎯 MAIN MENU:")
        print("1. 👤 User Management")
        print("2. 📝 Task Management")
        print("3. 📊 Project Management")
        print("4. 🔔 Notification Settings")
        print("5. 🧪 Run Tests")
        print("6. ⚡ Performance Tests")
        print("7. 📈 System Statistics")
        print("8. 🎮 Demo Workflow")
        print("9. 🔄 Command History (Undo/Redo)")
        print("0. 🚪 Exit")
        
        return input("\n👉 Choose option (0-9): ").strip()
    
    def user_management_menu(self):
        """User management menu"""
        while True:
            print("\n👤 USER MANAGEMENT")
            print("1. Create User")
            print("2. Login")
            print("3. View User Stats")
            print("4. List All Users")
            print("0. Back to Main Menu")
            
            choice = input("\n👉 Choose option: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.create_user()
            elif choice == "2":
                self.login_user()
            elif choice == "3":
                self.view_user_stats()
            elif choice == "4":
                self.list_users()
    
    def create_user(self):
        """Create new user"""
        try:
            print("\n📝 CREATE NEW USER")
            username = input("Username: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            command = CreateUserCommand(self.services["user"], username, email, password)
            user = self.command_invoker.execute(command)
            
            print(f"✅ User created successfully: {user.username}")
            
        except (ValidationException, BusinessLogicException) as e:
            print(f"❌ Error: {e}")
    
    def login_user(self):
        """Login user"""
        try:
            print("\n🔐 USER LOGIN")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            user = self.services["user"].authenticate_user(username, password)
            
            if user:
                self.current_user = user
                print(f"✅ Login successful! Welcome {user.username}")
            else:
                print("❌ Invalid credentials")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def view_user_stats(self):
        """View user statistics"""
        if not self.current_user:
            print("❌ Please login first")
            return
        
        stats = self.services["user"].get_user_statistics(self.current_user.id)
        
        print(f"\n📊 USER STATISTICS")
        print(f"Username: {stats.get('username', 'N/A')}")
        print(f"Created: {stats.get('created_at', 'N/A')}")
        print(f"Last Login: {stats.get('last_login', 'N/A')}")
        print(f"Status: {stats.get('status', 'N/A')}")
        print(f"Login Attempts: {stats.get('login_attempts', 0)}")
        print(f"Account Locked: {stats.get('is_locked', False)}")
    
    def list_users(self):
        """List all users"""
        users = self.services["user"].user_repository.find_all()
        
        print(f"\n👥 ALL USERS ({len(users)} total)")
        for user in users:
            status = "🔒" if user.is_locked else "✅"
            print(f"{status} {user.username} ({user.email}) - {user.status.value}")
    
    def task_management_menu(self):
        """Task management menu"""
        if not self.current_user:
            print("❌ Please login first")
            return
        
        while True:
            print("\n📝 TASK MANAGEMENT")
            print("1. Create Task")
            print("2. View My Tasks")
            print("3. Complete Task")
            print("4. Task Statistics")
            print("0. Back to Main Menu")
            
            choice = input("\n👉 Choose option: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.create_task()
            elif choice == "2":
                self.view_my_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.view_task_stats()
    
    def create_task(self):
        """Create new task"""
        try:
            print("\n📝 CREATE NEW TASK")
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            
            # For demo, assign to current user
            assignee_id = self.current_user.id
            reporter_id = self.current_user.id
            
            priority_input = input("Priority (1=Low, 2=Medium, 3=High, 4=Critical): ").strip()
            priority_map = {"1": Priority.LOW, "2": Priority.MEDIUM, "3": Priority.HIGH, "4": Priority.CRITICAL}
            priority = priority_map.get(priority_input, Priority.MEDIUM)
            
            command = CreateTaskCommand(
                self.services["task"], title, description, 
                assignee_id, reporter_id, priority
            )
            task = self.command_invoker.execute(command)
            
            print(f"✅ Task created successfully: {task.title}")
            
        except (ValidationException, BusinessLogicException) as e:
            print(f"❌ Error: {e}")
    
    def view_my_tasks(self):
        """View current user's tasks"""
        tasks = self.services["task"].task_repository.find_by_criteria({
            "assignee_id": self.current_user.id
        })
        
        print(f"\n📋 MY TASKS ({len(tasks)} total)")
        for task in tasks:
            status = "✅" if task.is_completed else "⏳"
            priority_emoji = {"LOW": "🔵", "MEDIUM": "🟡", "HIGH": "🟠", "CRITICAL": "🔴"}
            priority_icon = priority_emoji.get(task.priority.name, "⚪")
            
            print(f"{status} {priority_icon} {task.title}")
            print(f"    {task.description}")
            if task.due_date:
                print(f"    Due: {task.due_date}")
            print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()
    
    def complete_task(self):
        """Complete a task"""
        try:
            # Show incomplete tasks
            incomplete_tasks = [
                task for task in self.services["task"].task_repository.find_by_criteria({
                    "assignee_id": self.current_user.id
                }) if not task.is_completed
            ]
            
            if not incomplete_tasks:
                print("❌ No incomplete tasks found")
                return
            
            print("\n📋 INCOMPLETE TASKS:")
            for i, task in enumerate(incomplete_tasks, 1):
                print(f"{i}. {task.title}")
            
            choice = input("\nSelect task number: ").strip()
            task_index = int(choice) - 1
            
            if 0 <= task_index < len(incomplete_tasks):
                task = incomplete_tasks[task_index]
                actual_hours = float(input("Actual hours worked: ") or "0")
                
                completed_task = self.services["task"].complete_task(task.id, actual_hours)
                print(f"✅ Task completed: {completed_task.title}")
            else:
                print("❌ Invalid task number")
                
        except (ValueError, ValidationException, BusinessLogicException) as e:
            print(f"❌ Error: {e}")
    
    def view_task_stats(self):
        """View task statistics"""
        stats = self.services["task"].get_task_statistics()
        
        print(f"\n📊 TASK STATISTICS")
        print(f"Total Tasks: {stats['total_tasks']}")
        print(f"Completed Tasks: {stats['completed_tasks']}")
        print(f"Overdue Tasks: {stats['overdue_tasks']}")
        print(f"Completion Rate: {stats['completion_rate']:.1f}%")
        
        print(f"\n🎯 Priority Distribution:")
        for priority, count in stats['priority_distribution'].items():
            print(f"  {priority.upper()}: {count}")
    
    def run_tests(self):
        """Run comprehensive tests"""
        print("\n🧪 RUNNING COMPREHENSIVE TESTS")
        
        runner = TestRunner()
        
        # Add test cases
        runner.add_test_case(UserServiceTest())
        runner.add_test_case(TaskServiceTest())
        runner.add_test_case(IntegrationTest())
        
        # Run tests
        passed, failed = runner.run_all_tests()
        
        if failed == 0:
            print("\n🎉 All tests passed!")
        else:
            print(f"\n⚠️  {failed} tests failed!")
    
    def run_performance_tests(self):
        """Run performance tests"""
        print("\n⚡ RUNNING PERFORMANCE TESTS")
        
        runner = TestRunner()
        runner.add_test_case(PerformanceTest())
        
        passed, failed = runner.run_all_tests()
        
        if failed == 0:
            print("\n🚀 All performance tests passed!")
        else:
            print(f"\n⚠️  {failed} performance tests failed!")
    
    def show_system_stats(self):
        """Show system statistics"""
        print("\n📈 SYSTEM STATISTICS")
        print("=" * 40)
        
        # User stats
        users = self.services["user"].user_repository.find_all()
        active_users = len([u for u in users if u.status == EntityStatus.ACTIVE])
        
        print(f"👥 Users: {len(users)} total, {active_users} active")
        
        # Task stats
        task_stats = self.services["task"].get_task_statistics()
        print(f"📝 Tasks: {task_stats['total_tasks']} total, {task_stats['completed_tasks']} completed")
        
        # Projects
        projects = self.services["project"].project_repository.find_all()
        print(f"📊 Projects: {len(projects)} total")
        
        # Cache stats
        cache_size = len(self.factory.cache_service._cache)
        print(f"💾 Cache: {cache_size} entries")
        
        # Event stats
        event_subscribers = sum(len(handlers) for handlers in self.factory.event_bus._subscribers.values())
        print(f"🔔 Event Subscribers: {event_subscribers}")
    
    def demo_workflow(self):
        """Demo complete workflow"""
        print("\n🎮 DEMO WORKFLOW")
        print("=" * 40)
        
        try:
            # Create demo users
            print("1. Creating demo users...")
            demo_user1 = self.services["user"].create_user("demo_user1", "demo1@example.com", "password123")
            demo_user2 = self.services["user"].create_user("demo_user2", "demo2@example.com", "password123")
            
            # Create demo project
            print("2. Creating demo project...")
            demo_project = self.services["project"].create_project(
                "Demo Project",
                "Demonstration project for enterprise app",
                demo_user1.id,
                50000.0
            )
            
            # Create demo tasks
            print("3. Creating demo tasks...")
            task1 = self.services["task"].create_task(
                "Setup Development Environment",
                "Configure development tools and environment",
                demo_user1.id,
                demo_user1.id,
                Priority.HIGH
            )
            
            task2 = self.services["task"].create_task(
                "Implement User Authentication",
                "Create login and registration system",
                demo_user2.id,
                demo_user1.id,
                Priority.CRITICAL
            )
            
            # Complete some tasks
            print("4. Completing tasks...")
            self.services["task"].complete_task(task1.id, 4.0)
            
            # Show results
            print("5. Demo results:")
            print(f"   ✅ Created users: {demo_user1.username}, {demo_user2.username}")
            print(f"   ✅ Created project: {demo_project.name}")
            print(f"   ✅ Created tasks: {task1.title}, {task2.title}")
            print(f"   ✅ Completed task: {task1.title}")
            
            # Show statistics
            task_stats = self.services["task"].get_task_statistics()
            print(f"   📊 Task completion rate: {task_stats['completion_rate']:.1f}%")
            
            print("\n🎉 Demo workflow completed successfully!")
            
        except Exception as e:
            print(f"❌ Demo failed: {e}")
    
    def command_history_menu(self):
        """Command history menu"""
        print("\n🔄 COMMAND HISTORY")
        print(f"Commands in history: {len(self.command_invoker.history)}")
        print(f"Current position: {self.command_invoker.current_index + 1}")
        
        print("\n1. Undo last command")
        print("2. Redo next command")
        print("3. Show command history")
        print("0. Back to main menu")
        
        choice = input("\n👉 Choose option: ").strip()
        
        if choice == "1":
            if self.command_invoker.undo():
                print("✅ Command undone")
            else:
                print("❌ No commands to undo")
        elif choice == "2":
            if self.command_invoker.redo():
                print("✅ Command redone")
            else:
                print("❌ No commands to redo")
        elif choice == "3":
            for i, command in enumerate(self.command_invoker.history):
                marker = "👉" if i == self.command_invoker.current_index else "  "
                print(f"{marker} {i+1}. {command.__class__.__name__}")
    
    def run(self):
        """Run the enterprise application"""
        print("🎉 Welcome to Enterprise Application!")
        print("🏢 Advanced OOP Project with Clean Architecture")
        
        while True:
            choice = self.show_main_menu()
            
            if choice == "0":
                print("\n👋 Goodbye! Thanks for using Enterprise Application!")
                break
            elif choice == "1":
                self.user_management_menu()
            elif choice == "2":
                self.task_management_menu()
            elif choice == "3":
                print("📊 Project Management - Coming Soon!")
            elif choice == "4":
                print("🔔 Notification Settings - Coming Soon!")
            elif choice == "5":
                self.run_tests()
            elif choice == "6":
                self.run_performance_tests()
            elif choice == "7":
                self.show_system_stats()
            elif choice == "8":
                self.demo_workflow()
            elif choice == "9":
                self.command_history_menu()
            else:
                print("❌ Invalid choice! Please try again.")
            
            input("\n⏸️  Press Enter to continue...")

# ================================
# 🚀 MAIN EXECUTION
# ================================

if __name__ == "__main__":
    app = EnterpriseApplication()
    app.run() 