"""
🎯 BÀI TẬP 3: NESTED & ADVANCED DICTIONARY - SIMULATION-BASED LEARNING
📚 Ngày 11-12: Phương pháp Simulation - Học qua mô phỏng thực tế

🌟 PHƯƠNG PHÁP SIMULATION MỚI:
- 🎮 Game-Based Simulation: Học qua game mô phỏng
- 🏢 Real-World Scenarios: Tình huống thực tế
- 🔄 Progressive Complexity: Độ phức tạp tăng dần
- 📊 Data-Driven Learning: Học qua dữ liệu thực
- 🎯 Mission-Based Tasks: Nhiệm vụ cụ thể

Tác giả: Tanbaycu
Cập nhật: 2024
"""

import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict, Counter
import uuid

# =============================================================================
# 🎮 PHẦN 1: SIMULATION ENGINE - ĐỘNG CƠ MÔ PHỎNG
# =============================================================================

class SimulationEngine:
    """Động cơ mô phỏng cho Dictionary Learning"""
    
    def __init__(self):
        self.current_simulation = None
        self.player_stats = {
            "level": 1,
            "xp": 0,
            "missions_completed": 0,
            "skills": {
                "nested_dict": 0,
                "data_manipulation": 0,
                "optimization": 0,
                "real_world_app": 0
            }
        }
        self.achievements = []
        
    def start_simulation(self, sim_type: str):
        """Bắt đầu simulation"""
        print(f"\n🎮 KHỞI ĐỘNG SIMULATION: {sim_type.upper()}")
        print("="*60)
        self.current_simulation = sim_type
        
    def add_xp(self, amount: int, skill: str = None):
        """Thêm XP và skill points"""
        self.player_stats["xp"] += amount
        if skill and skill in self.player_stats["skills"]:
            self.player_stats["skills"][skill] += amount // 10
        
        # Level up check
        new_level = self.player_stats["xp"] // 100 + 1
        if new_level > self.player_stats["level"]:
            self.player_stats["level"] = new_level
            print(f"🎉 LEVEL UP! Bạn đã đạt level {new_level}")
    
    def show_stats(self):
        """Hiển thị thống kê người chơi"""
        print(f"\n📊 PLAYER STATS:")
        print(f"🎯 Level: {self.player_stats['level']}")
        print(f"⭐ XP: {self.player_stats['xp']}")
        print(f"🏆 Missions: {self.player_stats['missions_completed']}")
        print(f"🎮 Skills: {self.player_stats['skills']}")

# =============================================================================
# 🏢 PHẦN 2: CORPORATE SIMULATION - MÔ PHỎNG DOANH NGHIỆP
# =============================================================================

def corporate_data_simulation():
    """
    🏢 SIMULATION: Quản lý dữ liệu doanh nghiệp
    🎯 Nested Dictionary trong môi trường công ty thực tế
    """
    engine = SimulationEngine()
    engine.start_simulation("CORPORATE DATA MANAGEMENT")
    
    print("""
    🎯 NHIỆM VỤ: Bạn là Data Manager của TechCorp
    📊 Quản lý dữ liệu nhân viên, dự án, và hiệu suất
    🏆 Mục tiêu: Xây dựng hệ thống quản lý hoàn chỉnh
    """)
    
    # Khởi tạo corporate database
    corporate_db = {
        "company_info": {
            "name": "TechCorp Vietnam",
            "founded": "2020",
            "employees_count": 0,
            "departments": {},
            "projects": {},
            "financial": {
                "revenue": 0,
                "expenses": 0,
                "profit": 0
            }
        },
        "employees": {},
        "projects": {},
        "performance_metrics": {
            "monthly": {},
            "quarterly": {},
            "yearly": {}
        }
    }
    
    # Mission 1: Tạo cấu trúc phòng ban
    print("\n🎯 MISSION 1: Tạo cấu trúc phòng ban")
    print("-" * 40)
    
    departments = {
        "IT": {
            "manager": "Nguyễn Văn A",
            "budget": 2000000000,
            "employees": [],
            "projects": [],
            "kpis": {
                "productivity": 0,
                "satisfaction": 0,
                "delivery_rate": 0
            }
        },
        "Marketing": {
            "manager": "Trần Thị B", 
            "budget": 1500000000,
            "employees": [],
            "projects": [],
            "kpis": {
                "conversion_rate": 0,
                "roi": 0,
                "brand_awareness": 0
            }
        },
        "Sales": {
            "manager": "Lê Văn C",
            "budget": 1000000000,
            "employees": [],
            "projects": [],
            "kpis": {
                "revenue": 0,
                "deals_closed": 0,
                "customer_satisfaction": 0
            }
        }
    }
    
    corporate_db["company_info"]["departments"] = departments
    print(f"✅ Đã tạo {len(departments)} phòng ban")
    engine.add_xp(20, "nested_dict")
    
    # Mission 2: Thêm nhân viên
    print("\n🎯 MISSION 2: Thêm nhân viên vào hệ thống")
    print("-" * 40)
    
    def add_employee(name, department, position, salary, skills):
        """Thêm nhân viên mới"""
        emp_id = f"EMP{len(corporate_db['employees']) + 1:03d}"
        
        employee = {
            "personal_info": {
                "name": name,
                "emp_id": emp_id,
                "join_date": datetime.now().strftime("%Y-%m-%d"),
                "department": department,
                "position": position
            },
            "employment": {
                "salary": salary,
                "contract_type": "Full-time",
                "status": "Active"
            },
            "skills": skills,
            "performance": {
                "current_projects": [],
                "completed_projects": [],
                "ratings": [],
                "achievements": []
            },
            "attendance": {
                "total_days": 0,
                "present_days": 0,
                "late_days": 0,
                "absent_days": 0
            }
        }
        
        corporate_db["employees"][emp_id] = employee
        corporate_db["company_info"]["departments"][department]["employees"].append(emp_id)
        corporate_db["company_info"]["employees_count"] += 1
        
        return emp_id
    
    # Thêm nhân viên mẫu
    sample_employees = [
        ("Phạm Văn D", "IT", "Senior Developer", 25000000, ["Python", "JavaScript", "React"]),
        ("Hoàng Thị E", "IT", "DevOps Engineer", 22000000, ["Docker", "AWS", "Kubernetes"]),
        ("Đỗ Văn F", "Marketing", "Digital Marketing", 18000000, ["SEO", "SEM", "Analytics"]),
        ("Vũ Thị G", "Sales", "Account Manager", 20000000, ["CRM", "Negotiation", "B2B"])
    ]
    
    for name, dept, pos, salary, skills in sample_employees:
        emp_id = add_employee(name, dept, pos, salary, skills)
        print(f"✅ Đã thêm {name} ({emp_id}) vào phòng {dept}")
    
    engine.add_xp(30, "data_manipulation")
    
    # Mission 3: Tạo dự án và phân công
    print("\n🎯 MISSION 3: Tạo dự án và phân công nhân viên")
    print("-" * 40)
    
    def create_project(name, department, budget, deadline, team_members):
        """Tạo dự án mới"""
        project_id = f"PRJ{len(corporate_db['projects']) + 1:03d}"
        
        project = {
            "info": {
                "name": name,
                "project_id": project_id,
                "department": department,
                "status": "Planning",
                "created_date": datetime.now().strftime("%Y-%m-%d"),
                "deadline": deadline
            },
            "resources": {
                "budget": budget,
                "allocated_budget": 0,
                "remaining_budget": budget
            },
            "team": {
                "members": team_members,
                "roles": {},
                "workload": {}
            },
            "progress": {
                "completion_rate": 0,
                "milestones": [],
                "tasks": {},
                "issues": []
            },
            "metrics": {
                "hours_spent": 0,
                "efficiency": 0,
                "quality_score": 0
            }
        }
        
        corporate_db["projects"][project_id] = project
        corporate_db["company_info"]["departments"][department]["projects"].append(project_id)
        
        # Cập nhật current_projects cho nhân viên
        for emp_id in team_members:
            if emp_id in corporate_db["employees"]:
                corporate_db["employees"][emp_id]["performance"]["current_projects"].append(project_id)
        
        return project_id
    
    # Tạo dự án mẫu
    projects = [
        ("E-commerce Platform", "IT", 500000000, "2024-06-30", ["EMP001", "EMP002"]),
        ("Brand Awareness Campaign", "Marketing", 300000000, "2024-04-15", ["EMP003"]),
        ("Q1 Sales Drive", "Sales", 200000000, "2024-03-31", ["EMP004"])
    ]
    
    for name, dept, budget, deadline, team in projects:
        project_id = create_project(name, dept, budget, deadline, team)
        print(f"✅ Đã tạo dự án {name} ({project_id})")
    
    engine.add_xp(40, "real_world_app")
    
    # Mission 4: Phân tích hiệu suất
    print("\n🎯 MISSION 4: Phân tích hiệu suất và báo cáo")
    print("-" * 40)
    
    def generate_performance_report():
        """Tạo báo cáo hiệu suất"""
        report = {
            "company_overview": {
                "total_employees": corporate_db["company_info"]["employees_count"],
                "total_departments": len(corporate_db["company_info"]["departments"]),
                "active_projects": len([p for p in corporate_db["projects"].values() if p["info"]["status"] in ["Planning", "In Progress"]]),
                "total_budget": sum(dept["budget"] for dept in corporate_db["company_info"]["departments"].values())
            },
            "department_analysis": {},
            "employee_insights": {},
            "project_status": {}
        }
        
        # Phân tích theo phòng ban
        for dept_name, dept_data in corporate_db["company_info"]["departments"].items():
            report["department_analysis"][dept_name] = {
                "employee_count": len(dept_data["employees"]),
                "project_count": len(dept_data["projects"]),
                "budget_utilization": random.uniform(0.6, 0.9),  # Simulated
                "avg_salary": sum(corporate_db["employees"][emp_id]["employment"]["salary"] 
                                for emp_id in dept_data["employees"]) / len(dept_data["employees"]) if dept_data["employees"] else 0
            }
        
        # Phân tích nhân viên
        for emp_id, emp_data in corporate_db["employees"].items():
            report["employee_insights"][emp_id] = {
                "name": emp_data["personal_info"]["name"],
                "department": emp_data["personal_info"]["department"],
                "active_projects": len(emp_data["performance"]["current_projects"]),
                "skill_count": len(emp_data["skills"]),
                "performance_score": random.uniform(7.0, 9.5)  # Simulated
            }
        
        # Phân tích dự án
        for project_id, project_data in corporate_db["projects"].items():
            report["project_status"][project_id] = {
                "name": project_data["info"]["name"],
                "department": project_data["info"]["department"],
                "team_size": len(project_data["team"]["members"]),
                "budget_remaining": project_data["resources"]["remaining_budget"],
                "estimated_completion": random.uniform(0.3, 0.8)  # Simulated
            }
        
        return report
    
    # Tạo báo cáo
    performance_report = generate_performance_report()
    
    print("📊 BÁO CÁO HIỆU SUẤT TỔNG HỢP:")
    print(f"   👥 Tổng nhân viên: {performance_report['company_overview']['total_employees']}")
    print(f"   🏢 Tổng phòng ban: {performance_report['company_overview']['total_departments']}")
    print(f"   📋 Dự án đang thực hiện: {performance_report['company_overview']['active_projects']}")
    print(f"   💰 Tổng ngân sách: {performance_report['company_overview']['total_budget']:,} VND")
    
    print("\n📈 PHÂN TÍCH THEO PHÒNG BAN:")
    for dept, analysis in performance_report["department_analysis"].items():
        print(f"   {dept}: {analysis['employee_count']} nhân viên, {analysis['project_count']} dự án")
        print(f"      💰 Lương TB: {analysis['avg_salary']:,.0f} VND")
        print(f"      📊 Sử dụng ngân sách: {analysis['budget_utilization']:.1%}")
    
    engine.add_xp(50, "optimization")
    
    # Mission 5: Advanced Analytics
    print("\n🎯 MISSION 5: Advanced Analytics & Predictions")
    print("-" * 40)
    
    def advanced_analytics():
        """Phân tích nâng cao"""
        analytics = {
            "skill_distribution": defaultdict(int),
            "salary_analysis": {
                "by_department": {},
                "by_position": {},
                "overall_stats": {}
            },
            "project_insights": {
                "budget_distribution": {},
                "team_size_analysis": {},
                "department_workload": {}
            },
            "predictions": {
                "hiring_needs": {},
                "budget_forecast": {},
                "performance_trends": {}
            }
        }
        
        # Phân tích kỹ năng
        for emp_data in corporate_db["employees"].values():
            for skill in emp_data["skills"]:
                analytics["skill_distribution"][skill] += 1
        
        # Phân tích lương theo phòng ban
        for emp_data in corporate_db["employees"].values():
            dept = emp_data["personal_info"]["department"]
            salary = emp_data["employment"]["salary"]
            
            if dept not in analytics["salary_analysis"]["by_department"]:
                analytics["salary_analysis"]["by_department"][dept] = []
            analytics["salary_analysis"]["by_department"][dept].append(salary)
        
        # Tính thống kê lương
        all_salaries = [emp["employment"]["salary"] for emp in corporate_db["employees"].values()]
        analytics["salary_analysis"]["overall_stats"] = {
            "min": min(all_salaries),
            "max": max(all_salaries),
            "avg": sum(all_salaries) / len(all_salaries),
            "median": sorted(all_salaries)[len(all_salaries)//2]
        }
        
        # Phân tích dự án
        for project_data in corporate_db["projects"].values():
            dept = project_data["info"]["department"]
            budget = project_data["resources"]["budget"]
            team_size = len(project_data["team"]["members"])
            
            if dept not in analytics["project_insights"]["budget_distribution"]:
                analytics["project_insights"]["budget_distribution"][dept] = 0
            analytics["project_insights"]["budget_distribution"][dept] += budget
            
            if dept not in analytics["project_insights"]["team_size_analysis"]:
                analytics["project_insights"]["team_size_analysis"][dept] = []
            analytics["project_insights"]["team_size_analysis"][dept].append(team_size)
        
        # Predictions (simulated)
        for dept in corporate_db["company_info"]["departments"].keys():
            analytics["predictions"]["hiring_needs"][dept] = random.randint(1, 5)
            analytics["predictions"]["budget_forecast"][dept] = random.uniform(1.1, 1.3)
        
        return analytics
    
    # Thực hiện analytics
    analytics_result = advanced_analytics()
    
    print("🔍 ADVANCED ANALYTICS:")
    print(f"   📊 Top 3 skills: {dict(Counter(analytics_result['skill_distribution']).most_common(3))}")
    print(f"   💰 Lương trung bình: {analytics_result['salary_analysis']['overall_stats']['avg']:,.0f} VND")
    print(f"   📈 Dự báo tuyển dụng: {analytics_result['predictions']['hiring_needs']}")
    
    engine.add_xp(60, "optimization")
    engine.player_stats["missions_completed"] += 1
    
    # Interactive Challenge
    print("\n🎮 INTERACTIVE CHALLENGE:")
    print("Tìm nhân viên có lương cao nhất và dự án có ngân sách lớn nhất")
    
    # Tìm nhân viên lương cao nhất
    highest_paid = max(corporate_db["employees"].items(), 
                      key=lambda x: x[1]["employment"]["salary"])
    print(f"✅ Nhân viên lương cao nhất: {highest_paid[1]['personal_info']['name']} - {highest_paid[1]['employment']['salary']:,} VND")
    
    # Tìm dự án ngân sách lớn nhất
    biggest_project = max(corporate_db["projects"].items(),
                         key=lambda x: x[1]["resources"]["budget"])
    print(f"✅ Dự án ngân sách lớn nhất: {biggest_project[1]['info']['name']} - {biggest_project[1]['resources']['budget']:,} VND")
    
    engine.show_stats()
    return corporate_db

# =============================================================================
# 🎮 PHẦN 3: GAME DEVELOPMENT SIMULATION
# =============================================================================

def game_development_simulation():
    """
    🎮 SIMULATION: Phát triển game với nested dictionary
    🎯 Quản lý game world, players, items, quests
    """
    engine = SimulationEngine()
    engine.start_simulation("GAME DEVELOPMENT")
    
    print("""
    🎯 NHIỆM VỤ: Bạn là Game Developer
    🎮 Tạo một RPG game hoàn chỉnh
    🏆 Mục tiêu: Xây dựng game world với nested dict
    """)
    
    # Khởi tạo game database
    game_db = {
        "game_info": {
            "title": "Dragon Quest Python",
            "version": "1.0.0",
            "max_players": 1000,
            "current_players": 0
        },
        "world": {
            "maps": {},
            "npcs": {},
            "items": {},
            "quests": {}
        },
        "players": {},
        "guilds": {},
        "economy": {
            "currency": "Gold",
            "market": {},
            "transactions": []
        },
        "events": {
            "daily": {},
            "weekly": {},
            "special": {}
        }
    }
    
    # Mission 1: Tạo game world
    print("\n🎯 MISSION 1: Tạo thế giới game")
    print("-" * 40)
    
    def create_map(name, level_range, monsters, treasures):
        """Tạo bản đồ game"""
        map_id = f"MAP{len(game_db['world']['maps']) + 1:03d}"
        
        game_map = {
            "info": {
                "name": name,
                "map_id": map_id,
                "level_range": level_range,
                "type": "Dungeon" if "dungeon" in name.lower() else "Field"
            },
            "monsters": monsters,
            "treasures": treasures,
            "npcs": [],
            "spawn_points": {
                "player": {"x": 0, "y": 0},
                "monsters": [{"x": random.randint(1, 100), "y": random.randint(1, 100)} for _ in range(5)]
            },
            "environment": {
                "weather": random.choice(["sunny", "rainy", "cloudy"]),
                "difficulty": random.uniform(1.0, 5.0),
                "resources": ["wood", "stone", "herbs"]
            }
        }
        
        game_db["world"]["maps"][map_id] = game_map
        return map_id
    
    # Tạo maps
    maps_data = [
        ("Beginner Forest", (1, 10), ["Slime", "Goblin"], ["Health Potion", "Copper Coin"]),
        ("Dark Cave", (10, 20), ["Bat", "Spider"], ["Silver Coin", "Magic Crystal"]),
        ("Dragon Mountain", (20, 30), ["Dragon", "Orc"], ["Gold Coin", "Legendary Sword"])
    ]
    
    for name, level_range, monsters, treasures in maps_data:
        map_id = create_map(name, level_range, monsters, treasures)
        print(f"✅ Đã tạo map {name} ({map_id})")
    
    engine.add_xp(30, "nested_dict")
    
    # Mission 2: Tạo items và equipment
    print("\n🎯 MISSION 2: Tạo items và equipment system")
    print("-" * 40)
    
    def create_item(name, item_type, rarity, stats, price):
        """Tạo item"""
        item_id = f"ITEM{len(game_db['world']['items']) + 1:03d}"
        
        item = {
            "info": {
                "name": name,
                "item_id": item_id,
                "type": item_type,
                "rarity": rarity,
                "description": f"A {rarity} {item_type}"
            },
            "stats": stats,
            "economy": {
                "base_price": price,
                "current_price": price,
                "demand": random.uniform(0.5, 2.0)
            },
            "requirements": {
                "level": stats.get("level_req", 1),
                "class": "Any"
            },
            "effects": {
                "buffs": [],
                "debuffs": [],
                "special": []
            }
        }
        
        game_db["world"]["items"][item_id] = item
        return item_id
    
    # Tạo items
    items_data = [
        ("Iron Sword", "Weapon", "Common", {"attack": 10, "level_req": 1}, 100),
        ("Steel Armor", "Armor", "Uncommon", {"defense": 15, "level_req": 5}, 250),
        ("Magic Staff", "Weapon", "Rare", {"magic_power": 20, "level_req": 10}, 500),
        ("Dragon Scale", "Material", "Legendary", {"craft_value": 100}, 1000)
    ]
    
    for name, item_type, rarity, stats, price in items_data:
        item_id = create_item(name, item_type, rarity, stats, price)
        print(f"✅ Đã tạo item {name} ({item_id}) - {rarity}")
    
    engine.add_xp(25, "data_manipulation")
    
    # Mission 3: Player management system
    print("\n🎯 MISSION 3: Tạo hệ thống quản lý player")
    print("-" * 40)
    
    def create_player(username, character_class, starting_stats):
        """Tạo player mới"""
        player_id = str(uuid.uuid4())[:8]
        
        player = {
            "account": {
                "username": username,
                "player_id": player_id,
                "created_date": datetime.now().isoformat(),
                "last_login": datetime.now().isoformat(),
                "status": "Online"
            },
            "character": {
                "class": character_class,
                "level": 1,
                "xp": 0,
                "xp_to_next": 100,
                "stats": starting_stats,
                "location": "MAP001"
            },
            "inventory": {
                "items": {},
                "equipment": {
                    "weapon": None,
                    "armor": None,
                    "accessory": None
                },
                "currency": {"gold": 100, "gems": 0}
            },
            "progress": {
                "quests": {
                    "active": [],
                    "completed": [],
                    "available": []
                },
                "achievements": [],
                "statistics": {
                    "monsters_killed": 0,
                    "quests_completed": 0,
                    "items_collected": 0,
                    "gold_earned": 0
                }
            },
            "social": {
                "friends": [],
                "guild": None,
                "messages": []
            }
        }
        
        game_db["players"][player_id] = player
        game_db["game_info"]["current_players"] += 1
        return player_id
    
    # Tạo players mẫu
    players_data = [
        ("DragonSlayer", "Warrior", {"hp": 100, "mp": 20, "attack": 15, "defense": 12}),
        ("MagicMaster", "Mage", {"hp": 60, "mp": 80, "attack": 8, "defense": 6}),
        ("ShadowHunter", "Archer", {"hp": 80, "mp": 40, "attack": 12, "defense": 8})
    ]
    
    for username, char_class, stats in players_data:
        player_id = create_player(username, char_class, stats)
        print(f"✅ Đã tạo player {username} ({player_id}) - {char_class}")
    
    engine.add_xp(35, "real_world_app")
    
    # Mission 4: Quest system
    print("\n🎯 MISSION 4: Tạo hệ thống quest")
    print("-" * 40)
    
    def create_quest(title, quest_type, requirements, rewards, story):
        """Tạo quest"""
        quest_id = f"QUEST{len(game_db['world']['quests']) + 1:03d}"
        
        quest = {
            "info": {
                "title": title,
                "quest_id": quest_id,
                "type": quest_type,
                "difficulty": random.choice(["Easy", "Medium", "Hard"]),
                "story": story
            },
            "requirements": requirements,
            "objectives": {
                "main": [],
                "optional": [],
                "completed": []
            },
            "rewards": rewards,
            "status": {
                "available": True,
                "active_players": [],
                "completion_rate": 0
            },
            "progression": {
                "steps": [],
                "current_step": 0,
                "auto_complete": False
            }
        }
        
        game_db["world"]["quests"][quest_id] = quest
        return quest_id
    
    # Tạo quests
    quests_data = [
        ("Defeat the Goblin King", "Kill", {"level": 5, "location": "MAP001"}, 
         {"xp": 200, "gold": 150, "items": ["ITEM001"]}, "The goblins are terrorizing the village!"),
        ("Collect Magic Crystals", "Collect", {"level": 10, "items_needed": 5},
         {"xp": 300, "gold": 200, "items": ["ITEM003"]}, "The wizard needs magic crystals for his spell."),
        ("Explore the Dragon Mountain", "Explore", {"level": 20, "location": "MAP003"},
         {"xp": 500, "gold": 400, "items": ["ITEM004"]}, "Ancient treasures await in the dragon's lair!")
    ]
    
    for title, quest_type, requirements, rewards, story in quests_data:
        quest_id = create_quest(title, quest_type, requirements, rewards, story)
        print(f"✅ Đã tạo quest: {title} ({quest_id})")
    
    engine.add_xp(40, "nested_dict")
    
    # Mission 5: Game analytics
    print("\n🎯 MISSION 5: Game Analytics Dashboard")
    print("-" * 40)
    
    def generate_game_analytics():
        """Tạo analytics cho game"""
        analytics = {
            "player_stats": {
                "total_players": len(game_db["players"]),
                "online_players": len([p for p in game_db["players"].values() if p["account"]["status"] == "Online"]),
                "avg_level": sum(p["character"]["level"] for p in game_db["players"].values()) / len(game_db["players"]) if game_db["players"] else 0,
                "class_distribution": Counter(p["character"]["class"] for p in game_db["players"].values())
            },
            "world_stats": {
                "total_maps": len(game_db["world"]["maps"]),
                "total_items": len(game_db["world"]["items"]),
                "total_quests": len(game_db["world"]["quests"]),
                "active_quests": len([q for q in game_db["world"]["quests"].values() if q["status"]["available"]])
            },
            "economy_stats": {
                "total_gold_in_game": sum(p["inventory"]["currency"]["gold"] for p in game_db["players"].values()),
                "item_values": {item_id: item["economy"]["current_price"] for item_id, item in game_db["world"]["items"].items()},
                "market_activity": random.randint(50, 200)  # Simulated
            },
            "engagement_metrics": {
                "avg_session_time": random.uniform(30, 120),  # minutes
                "quest_completion_rate": random.uniform(0.6, 0.9),
                "player_retention": random.uniform(0.7, 0.95)
            }
        }
        
        return analytics
    
    # Tạo analytics
    analytics = generate_game_analytics()
    
    print("📊 GAME ANALYTICS DASHBOARD:")
    print(f"   👥 Total Players: {analytics['player_stats']['total_players']}")
    print(f"   🟢 Online Players: {analytics['player_stats']['online_players']}")
    print(f"   🎯 Average Level: {analytics['player_stats']['avg_level']:.1f}")
    print(f"   🗺️ Total Maps: {analytics['world_stats']['total_maps']}")
    print(f"   🎒 Total Items: {analytics['world_stats']['total_items']}")
    print(f"   📋 Active Quests: {analytics['world_stats']['active_quests']}")
    print(f"   💰 Total Gold: {analytics['economy_stats']['total_gold_in_game']:,}")
    print(f"   📈 Completion Rate: {analytics['engagement_metrics']['quest_completion_rate']:.1%}")
    
    engine.add_xp(50, "optimization")
    engine.player_stats["missions_completed"] += 1
    
    # Interactive Challenge
    print("\n🎮 INTERACTIVE CHALLENGE:")
    print("Tìm player có level cao nhất và quest khó nhất")
    
    # Tìm player level cao nhất
    if game_db["players"]:
        highest_level_player = max(game_db["players"].items(),
                                 key=lambda x: x[1]["character"]["level"])
        print(f"✅ Player level cao nhất: {highest_level_player[1]['account']['username']} - Level {highest_level_player[1]['character']['level']}")
    
    # Tìm quest khó nhất
    hard_quests = [q for q in game_db["world"]["quests"].values() if q["info"]["difficulty"] == "Hard"]
    if hard_quests:
        print(f"✅ Quest khó nhất: {hard_quests[0]['info']['title']}")
    
    engine.show_stats()
    return game_db

# =============================================================================
# 🎯 PHẦN 4: MAIN SIMULATION CONTROLLER
# =============================================================================

def main():
    """Chương trình chính - Simulation Controller"""
    
    print("🎮 NESTED & ADVANCED DICTIONARY SIMULATIONS")
    print("📚 Phương pháp: Simulation-Based Learning")
    print("🎯 Mục tiêu: Thành thạo Nested Dictionary qua mô phỏng thực tế")
    
    while True:
        print("\n" + "="*60)
        print("🎯 SIMULATION MENU")
        print("="*60)
        
        simulations = [
            "1. 🏢 Corporate Data Management",
            "2. 🎮 Game Development System",
            "3. 🏥 Hospital Management (Coming Soon)",
            "4. 🎓 University System (Coming Soon)",
            "5. 🚪 Exit"
        ]
        
        for sim in simulations:
            print(sim)
        
        choice = input("\nChọn simulation (1-5): ")
        
        if choice == "1":
            print("\n🏢 Khởi động Corporate Simulation...")
            result = corporate_data_simulation()
            print(f"\n✅ Simulation hoàn thành! Đã tạo {len(result['employees'])} nhân viên và {len(result['projects'])} dự án")
            
        elif choice == "2":
            print("\n🎮 Khởi động Game Development Simulation...")
            result = game_development_simulation()
            print(f"\n✅ Simulation hoàn thành! Đã tạo {len(result['players'])} players và {len(result['world']['quests'])} quests")
            
        elif choice == "3":
            print("🏥 Hospital Management Simulation - Coming Soon!")
            print("📋 Features: Patient records, Medical staff, Treatment plans")
            
        elif choice == "4":
            print("🎓 University System Simulation - Coming Soon!")
            print("📋 Features: Student management, Course scheduling, Grade tracking")
            
        elif choice == "5":
            print("\n🎉 Cảm ơn bạn đã tham gia Simulation-Based Learning!")
            print("🏆 Bạn đã thành thạo Nested Dictionary qua các tình huống thực tế!")
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ!")
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    print("🎓 NESTED & ADVANCED DICTIONARY SIMULATIONS - VERSION 1.0")
    print("📚 Phương pháp mới: Simulation-Based Learning")
    print("🎯 Mục tiêu: Thành thạo Nested Dictionary qua mô phỏng")
    print("\n" + "🚀 SIMULATION STARTING..." + "\n")
    
    main()

"""
🎯 TỔNG KẾT BÀI TẬP 3:

✅ PHƯƠNG PHÁP SIMULATION MỚI:
- Game-Based Simulation: Học qua game mô phỏng
- Real-World Scenarios: Tình huống thực tế
- Progressive Complexity: Độ phức tạp tăng dần
- Mission-Based Learning: Học qua nhiệm vụ cụ thể

🏆 NỘI DUNG CHÍNH:
1. Corporate Data Management (Quản lý doanh nghiệp)
2. Game Development System (Phát triển game)
3. Advanced Analytics (Phân tích nâng cao)
4. Performance Optimization (Tối ưu hóa)
5. Interactive Challenges (Thách thức tương tác)

🎮 TÍNH NĂNG ĐẶC BIỆT:
- Simulation Engine với XP system
- Nested Dictionary trong tình huống thực tế
- Progressive missions với độ khó tăng dần
- Real-time analytics và reporting
- Interactive challenges và achievements

📊 KẾT QUẢ MONG ĐỢI:
- Thành thạo Nested Dictionary structures
- Hiểu cách áp dụng trong dự án thực tế
- Kỹ năng phân tích và tối ưu dữ liệu
- Tư duy system design với Dictionary
- Kinh nghiệm xử lý dữ liệu phức tạp
"""