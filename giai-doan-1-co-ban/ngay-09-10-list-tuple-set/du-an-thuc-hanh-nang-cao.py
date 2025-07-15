#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DỰ ÁN THỰC HÀNH NÂNG CAO: LISTS, TUPLES, SETS
Ngày 9-10: 3 Dự án lớn tích hợp kiến thức

Mục tiêu học tập:
- Xây dựng ứng dụng phức tạp với giao diện người dùng
- Tích hợp nhiều cấu trúc dữ liệu
- Xử lý dữ liệu lớn và tối ưu hóa
- Thực hành thiết kế hệ thống

Tác giả: Python Learning Journey  
Cấp độ: Advanced
"""

import json
import random
import datetime
import time
from collections import defaultdict, Counter
import csv
import os

# ============================================================================
# DỰ ÁN 1: HỆ THỐNG PHÂN TÍCH DỮ LIỆU BÁN HÀNG THƯƠNG MẠI ĐIỆN TỬ
# ============================================================================

print("=" * 100)
print("DỰ ÁN 1: HỆ THỐNG PHÂN TÍCH DỮ LIỆU BÁN HÀNG THƯƠNG MẠI ĐIỆN TỬ")
print("=" * 100)

class ECommerceAnalytics:
    """
    Hệ thống phân tích dữ liệu bán hàng thương mại điện tử hoàn chỉnh
    Sử dụng Lists, Tuples, Sets để xử lý và phân tích dữ liệu lớn
    """
    
    def __init__(self):
        # Cấu trúc dữ liệu chính
        self.products = {}  # product_id -> product_info
        self.customers = {}  # customer_id -> customer_info  
        self.orders = []  # List các đơn hàng
        self.order_items = []  # List các item trong đơn hàng
        
        # Indexes để tối ưu truy vấn
        self.product_categories = defaultdict(set)  # category -> set of product_ids
        self.customer_segments = defaultdict(set)  # segment -> set of customer_ids
        self.date_orders = defaultdict(list)  # date -> list of order_ids
        
        # Cache cho các tính toán phức tạp
        self.analytics_cache = {}
        self.cache_timestamp = {}
        
        # Cài đặt hệ thống
        self.cache_timeout = 300  # 5 phút
        
    def add_product(self, product_id, name, category, price, brand, launch_date):
        """Thêm sản phẩm vào hệ thống"""
        self.products[product_id] = {
            'name': name,
            'category': category,
            'price': price,
            'brand': brand,
            'launch_date': launch_date,
            'total_sold': 0,
            'total_revenue': 0,
            'unique_customers': set()
        }
        
        self.product_categories[category].add(product_id)
        print(f"✓ Đã thêm sản phẩm: {name}")
        
    def add_customer(self, customer_id, name, email, join_date, city, age_group):
        """Thêm khách hàng vào hệ thống"""
        self.customers[customer_id] = {
            'name': name,
            'email': email,
            'join_date': join_date,
            'city': city,
            'age_group': age_group,
            'total_orders': 0,
            'total_spent': 0,
            'favorite_categories': Counter(),
            'order_history': []
        }
        
        # Phân khúc khách hàng
        if age_group in ['18-25', '26-35']:
            segment = 'young'
        elif age_group in ['36-45', '46-55']:
            segment = 'middle'
        else:
            segment = 'senior'
            
        self.customer_segments[segment].add(customer_id)
        print(f"✓ Đã thêm khách hàng: {name}")
        
    def add_order(self, order_id, customer_id, order_date, status, items):
        """
        Thêm đơn hàng với các items
        items: [(product_id, quantity, unit_price), ...]
        """
        if customer_id not in self.customers:
            print(f"Khách hàng {customer_id} không tồn tại!")
            return False
            
        # Tạo đơn hàng
        order = {
            'order_id': order_id,
            'customer_id': customer_id,
            'order_date': order_date,
            'status': status,
            'total_amount': 0,
            'total_items': 0
        }
        
        # Xử lý các items
        order_total = 0
        total_quantity = 0
        
        for product_id, quantity, unit_price in items:
            if product_id not in self.products:
                print(f"Sản phẩm {product_id} không tồn tại!")
                continue
                
            item_total = quantity * unit_price
            order_total += item_total
            total_quantity += quantity
            
            # Thêm item detail
            item = {
                'order_id': order_id,
                'product_id': product_id,
                'quantity': quantity,
                'unit_price': unit_price,
                'total_price': item_total
            }
            self.order_items.append(item)
            
            # Cập nhật thống kê sản phẩm
            product = self.products[product_id]
            product['total_sold'] += quantity
            product['total_revenue'] += item_total
            product['unique_customers'].add(customer_id)
            
        # Hoàn thiện đơn hàng
        order['total_amount'] = order_total
        order['total_items'] = total_quantity
        self.orders.append(order)
        
        # Cập nhật index
        self.date_orders[order_date].append(order_id)
        
        # Cập nhật thống kê khách hàng
        customer = self.customers[customer_id]
        customer['total_orders'] += 1
        customer['total_spent'] += order_total
        customer['order_history'].append(order_id)
        
        # Cập nhật sở thích danh mục
        for product_id, quantity, _ in items:
            if product_id in self.products:
                category = self.products[product_id]['category']
                customer['favorite_categories'][category] += quantity
                
        # Xóa cache liên quan
        self._invalidate_cache()
        
        print(f"✓ Đã thêm đơn hàng {order_id}: {order_total:,.0f} VNĐ")
        return True
        
    def _invalidate_cache(self):
        """Xóa cache khi dữ liệu thay đổi"""
        self.analytics_cache.clear()
        self.cache_timestamp.clear()
        
    def _get_cached_result(self, cache_key, compute_func, *args, **kwargs):
        """Lấy kết quả từ cache hoặc tính toán mới"""
        current_time = time.time()
        
        if (cache_key in self.analytics_cache and 
            cache_key in self.cache_timestamp and
            current_time - self.cache_timestamp[cache_key] < self.cache_timeout):
            return self.analytics_cache[cache_key]
            
        # Tính toán và cache
        result = compute_func(*args, **kwargs)
        self.analytics_cache[cache_key] = result
        self.cache_timestamp[cache_key] = current_time
        return result
        
    def _compute_revenue_by_period(self, period='month'):
        """Tính doanh thu theo thời kỳ"""
        revenue_by_period = defaultdict(float)
        
        for order in self.orders:
            if order['status'] == 'completed':
                if period == 'month':
                    key = order['order_date'].strftime('%Y-%m')
                elif period == 'week':
                    # Lấy tuần trong năm
                    year, week, _ = order['order_date'].isocalendar()
                    key = f"{year}-W{week:02d}"
                else:  # day
                    key = order['order_date'].strftime('%Y-%m-%d')
                    
                revenue_by_period[key] += order['total_amount']
                
        return dict(revenue_by_period)
        
    def get_revenue_by_period(self, period='month'):
        """Lấy doanh thu theo thời kỳ (có cache)"""
        cache_key = f"revenue_{period}"
        return self._get_cached_result(cache_key, self._compute_revenue_by_period, period)
        
    def _compute_top_products(self, metric='revenue', limit=10):
        """Tính top sản phẩm theo metric"""
        product_metrics = []
        
        for product_id, product in self.products.items():
            if metric == 'revenue':
                value = product['total_revenue']
            elif metric == 'quantity':
                value = product['total_sold']
            elif metric == 'customers':
                value = len(product['unique_customers'])
            else:
                continue
                
            product_metrics.append((product_id, product['name'], value))
            
        return sorted(product_metrics, key=lambda x: x[2], reverse=True)[:limit]
        
    def get_top_products(self, metric='revenue', limit=10):
        """Lấy top sản phẩm (có cache)"""
        cache_key = f"top_products_{metric}_{limit}"
        return self._get_cached_result(cache_key, self._compute_top_products, metric, limit)
        
    def _compute_customer_segments_analysis(self):
        """Phân tích các phân khúc khách hàng"""
        segment_analysis = {}
        
        for segment, customer_ids in self.customer_segments.items():
            total_customers = len(customer_ids)
            total_revenue = sum(self.customers[cid]['total_spent'] for cid in customer_ids)
            total_orders = sum(self.customers[cid]['total_orders'] for cid in customer_ids)
            
            avg_revenue_per_customer = total_revenue / total_customers if total_customers > 0 else 0
            avg_orders_per_customer = total_orders / total_customers if total_customers > 0 else 0
            
            segment_analysis[segment] = {
                'total_customers': total_customers,
                'total_revenue': total_revenue,
                'avg_revenue_per_customer': avg_revenue_per_customer,
                'avg_orders_per_customer': avg_orders_per_customer,
                'revenue_percentage': 0  # Sẽ tính sau
            }
            
        # Tính phần trăm doanh thu
        total_revenue = sum(data['total_revenue'] for data in segment_analysis.values())
        for segment_data in segment_analysis.values():
            if total_revenue > 0:
                segment_data['revenue_percentage'] = (segment_data['total_revenue'] / total_revenue) * 100
                
        return segment_analysis
        
    def get_customer_segments_analysis(self):
        """Lấy phân tích phân khúc khách hàng (có cache)"""
        cache_key = "customer_segments"
        return self._get_cached_result(cache_key, self._compute_customer_segments_analysis)
        
    def _compute_category_performance(self):
        """Phân tích hiệu suất theo danh mục"""
        category_stats = defaultdict(lambda: {
            'total_revenue': 0,
            'total_quantity': 0,
            'unique_customers': set(),
            'product_count': 0
        })
        
        for product_id, product in self.products.items():
            category = product['category']
            category_stats[category]['total_revenue'] += product['total_revenue']
            category_stats[category]['total_quantity'] += product['total_sold']
            category_stats[category]['unique_customers'].update(product['unique_customers'])
            category_stats[category]['product_count'] += 1
            
        # Chuyển set thành count
        for category, stats in category_stats.items():
            stats['unique_customers'] = len(stats['unique_customers'])
            
        return dict(category_stats)
        
    def get_category_performance(self):
        """Lấy hiệu suất danh mục (có cache)"""
        cache_key = "category_performance"
        return self._get_cached_result(cache_key, self._compute_category_performance)
        
    def find_customer_purchase_patterns(self, customer_id):
        """Phân tích mẫu mua hàng của khách hàng"""
        if customer_id not in self.customers:
            return None
            
        customer = self.customers[customer_id]
        customer_orders = [o for o in self.orders if o['customer_id'] == customer_id]
        customer_items = [i for i in self.order_items 
                         if any(o['order_id'] == i['order_id'] for o in customer_orders)]
        
        # Phân tích patterns
        patterns = {
            'total_orders': len(customer_orders),
            'total_spent': customer['total_spent'],
            'avg_order_value': customer['total_spent'] / len(customer_orders) if customer_orders else 0,
            'favorite_categories': dict(customer['favorite_categories'].most_common(5)),
            'purchase_frequency': self._calculate_purchase_frequency(customer_orders),
            'seasonal_patterns': self._analyze_seasonal_patterns(customer_orders),
            'price_sensitivity': self._analyze_price_sensitivity(customer_items)
        }
        
        return patterns
        
    def _calculate_purchase_frequency(self, orders):
        """Tính tần suất mua hàng"""
        if len(orders) < 2:
            return None
            
        dates = sorted([o['order_date'] for o in orders])
        intervals = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
        
        return {
            'avg_days_between_orders': sum(intervals) / len(intervals),
            'min_interval': min(intervals),
            'max_interval': max(intervals)
        }
        
    def _analyze_seasonal_patterns(self, orders):
        """Phân tích mẫu theo mùa"""
        monthly_orders = defaultdict(int)
        quarterly_orders = defaultdict(int)
        
        for order in orders:
            month = order['order_date'].month
            quarter = f"Q{(month-1)//3 + 1}"
            
            monthly_orders[month] += 1
            quarterly_orders[quarter] += 1
            
        return {
            'monthly': dict(monthly_orders),
            'quarterly': dict(quarterly_orders)
        }
        
    def _analyze_price_sensitivity(self, items):
        """Phân tích độ nhạy cảm giá"""
        if not items:
            return None
            
        prices = [item['unit_price'] for item in items]
        
        return {
            'avg_price': sum(prices) / len(prices),
            'price_range': (min(prices), max(prices)),
            'price_preferences': {
                'low': len([p for p in prices if p < 100000]),
                'medium': len([p for p in prices if 100000 <= p < 500000]),
                'high': len([p for p in prices if p >= 500000])
            }
        }
        
    def generate_comprehensive_report(self):
        """Tạo báo cáo tổng quan toàn diện"""
        report = {
            'summary': {
                'total_products': len(self.products),
                'total_customers': len(self.customers),
                'total_orders': len(self.orders),
                'total_revenue': sum(o['total_amount'] for o in self.orders if o['status'] == 'completed')
            },
            'revenue_trends': self.get_revenue_by_period('month'),
            'top_products': {
                'by_revenue': self.get_top_products('revenue', 5),
                'by_quantity': self.get_top_products('quantity', 5),
                'by_customers': self.get_top_products('customers', 5)
            },
            'customer_segments': self.get_customer_segments_analysis(),
            'category_performance': self.get_category_performance()
        }
        
        return report
        
    def export_data(self, filename_prefix="ecommerce_data"):
        """Xuất dữ liệu ra các file"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Xuất products
        with open(f"{filename_prefix}_products_{timestamp}.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['product_id', 'name', 'category', 'price', 'brand', 'total_sold', 'total_revenue'])
            
            for product_id, product in self.products.items():
                writer.writerow([
                    product_id, product['name'], product['category'], 
                    product['price'], product['brand'], 
                    product['total_sold'], product['total_revenue']
                ])
                
        # Xuất comprehensive report
        report = self.generate_comprehensive_report()
        with open(f"{filename_prefix}_report_{timestamp}.json", 'w', encoding='utf-8') as f:
            # Convert datetime objects to strings for JSON serialization
            def json_serial(obj):
                if isinstance(obj, datetime.date):
                    return obj.isoformat()
                raise TypeError(f"Type {type(obj)} not serializable")
                
            json.dump(report, f, ensure_ascii=False, indent=2, default=json_serial)
            
        print(f"✓ Đã xuất dữ liệu với timestamp: {timestamp}")

# Demo E-commerce Analytics System
print("\n--- DEMO HỆ THỐNG PHÂN TÍCH THƯƠNG MẠI ĐIỆN TỬ ---")

ecommerce = ECommerceAnalytics()

# Tạo dữ liệu mẫu
print("Đang tạo dữ liệu mẫu...")

# Thêm sản phẩm
products_data = [
    ("P001", "iPhone 15 Pro", "Smartphones", 25000000, "Apple", datetime.date(2023, 9, 22)),
    ("P002", "Samsung Galaxy S24", "Smartphones", 22000000, "Samsung", datetime.date(2024, 1, 17)),
    ("P003", "MacBook Pro M3", "Laptops", 45000000, "Apple", datetime.date(2023, 10, 30)),
    ("P004", "Dell XPS 13", "Laptops", 35000000, "Dell", datetime.date(2023, 8, 15)),
    ("P005", "AirPods Pro 2", "Audio", 6000000, "Apple", datetime.date(2023, 9, 23)),
    ("P006", "Sony WH-1000XM5", "Audio", 8000000, "Sony", datetime.date(2023, 5, 12)),
    ("P007", "iPad Air M2", "Tablets", 15000000, "Apple", datetime.date(2024, 3, 8)),
    ("P008", "Surface Pro 10", "Tablets", 25000000, "Microsoft", datetime.date(2024, 2, 20)),
]

for product in products_data:
    ecommerce.add_product(*product)

# Thêm khách hàng  
customers_data = [
    ("C001", "Nguyễn Văn An", "an.nguyen@email.com", datetime.date(2023, 1, 15), "Hà Nội", "26-35"),
    ("C002", "Trần Thị Bình", "binh.tran@email.com", datetime.date(2023, 2, 20), "HCM", "18-25"),
    ("C003", "Lê Văn Cường", "cuong.le@email.com", datetime.date(2023, 3, 10), "Đà Nẵng", "36-45"),
    ("C004", "Phạm Thị Dung", "dung.pham@email.com", datetime.date(2023, 4, 5), "Hà Nội", "46-55"),
    ("C005", "Hoàng Văn Em", "em.hoang@email.com", datetime.date(2023, 5, 12), "Cần Thơ", "26-35"),
]

for customer in customers_data:
    ecommerce.add_customer(*customer)

# Tạo đơn hàng ngẫu nhiên
print("Đang tạo đơn hàng ngẫu nhiên...")
order_id_counter = 1

for month in range(1, 13):  # 12 tháng
    for week in range(4):  # 4 tuần/tháng
        # Tạo 3-7 đơn hàng/tuần
        for _ in range(random.randint(3, 7)):
            customer_id = random.choice(list(ecommerce.customers.keys()))
            order_date = datetime.date(2024, month, random.randint(1, 28))
            
            # Tạo items cho đơn hàng (1-4 sản phẩm)
            items = []
            selected_products = random.sample(list(ecommerce.products.keys()), 
                                           random.randint(1, 3))
            
            for product_id in selected_products:
                quantity = random.randint(1, 3)
                base_price = ecommerce.products[product_id]['price']
                # Thêm biến động giá ±10%
                unit_price = base_price * random.uniform(0.9, 1.1)
                items.append((product_id, quantity, unit_price))
            
            ecommerce.add_order(
                f"ORD{order_id_counter:05d}",
                customer_id,
                order_date,
                'completed',
                items
            )
            order_id_counter += 1

# Phân tích và hiển thị kết quả
print("\n--- KẾT QUẢ PHÂN TÍCH ---")

# Tổng quan
report = ecommerce.generate_comprehensive_report()
summary = report['summary']

print(f"\n📊 TỔNG QUAN:")
print(f"  • Tổng sản phẩm: {summary['total_products']}")
print(f"  • Tổng khách hàng: {summary['total_customers']}")  
print(f"  • Tổng đơn hàng: {summary['total_orders']}")
print(f"  • Tổng doanh thu: {summary['total_revenue']:,.0f} VNĐ")

# Top sản phẩm
print(f"\n🏆 TOP 3 SẢN PHẨM THEO DOANH THU:")
for i, (product_id, name, revenue) in enumerate(report['top_products']['by_revenue'][:3], 1):
    print(f"  {i}. {name}: {revenue:,.0f} VNĐ")

# Phân khúc khách hàng
print(f"\n👥 PHÂN TÍCH PHÂN KHÚC KHÁCH HÀNG:")
for segment, data in report['customer_segments'].items():
    print(f"  • {segment.title()}: {data['total_customers']} KH, "
          f"ARPU: {data['avg_revenue_per_customer']:,.0f} VNĐ "
          f"({data['revenue_percentage']:.1f}% doanh thu)")

# Hiệu suất danh mục
print(f"\n📱 HIỆU SUẤT THEO DANH MỤC:")
category_perf = report['category_performance']
sorted_categories = sorted(category_perf.items(), 
                          key=lambda x: x[1]['total_revenue'], reverse=True)

for category, stats in sorted_categories:
    print(f"  • {category}: {stats['total_revenue']:,.0f} VNĐ, "
          f"{stats['unique_customers']} KH duy nhất")

print("\n" + "="*100)
print("HOÀN THÀNH DỰ ÁN 1: HỆ THỐNG PHÂN TÍCH THƯƠNG MẠI ĐIỆN TỬ")
print("✓ Xử lý dữ liệu lớn với Lists, Tuples, Sets")
print("✓ Hệ thống cache và tối ưu hóa")
print("✓ Phân tích dữ liệu đa chiều")  
print("✓ Báo cáo và xuất dữ liệu")
print("="*100) 