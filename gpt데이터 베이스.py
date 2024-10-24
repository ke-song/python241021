import sqlite3
import random

# ProductDatabase 클래스 정의
class ProductDatabase:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    # 테이블 생성
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """)
        self.conn.commit()

    # 제품 추가
    def insert_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    # 제품 수정
    def update_product(self, product_id, name=None, price=None):
        if name and price:
            self.cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, price, product_id))
        elif name:
            self.cursor.execute("UPDATE products SET name = ? WHERE id = ?", (name, product_id))
        elif price:
            self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, product_id))
        self.conn.commit()

    # 제품 삭제
    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    # 모든 제품 조회
    def select_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    # 특정 제품 조회
    def select_product_by_id(self, product_id):
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

    # 데이터베이스 연결 종료
    def close(self):
        self.conn.close()

# 샘플 데이터 생성 함수
def generate_sample_data(db, num_samples=100):
    product_names = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", 
                     "Monitor", "Keyboard", "Mouse", "Printer", "Speaker"]
    
    for i in range(num_samples):
        name = random.choice(product_names) + f" Model-{i+1}"
        price = round(random.uniform(100, 2000), 2)  # 가격은 100 ~ 2000 사이의 랜덤 값
        db.insert_product(name, price)

# 메인 실행 부분
if __name__ == "__main__":
    # 데이터베이스 객체 생성
    db = ProductDatabase()

    # 샘플 데이터 100개 생성
    generate_sample_data(db, 100)

    # 모든 제품 조회
    products = db.select_all_products()
    for product in products:
        print(product)

    # 예시: 제품 업데이트 (1번 제품의 이름과 가격 수정)
    db.update_product(1, name="Updated Laptop", price=1500.00)

    # 예시: 특정 제품 조회
    product = db.select_product_by_id(1)
    print("\nUpdated Product:", product)

    # 예시: 제품 삭제 (1번 제품 삭제)
    db.delete_product(1)

    # 삭제 후 다시 조회
    products = db.select_all_products()
    print("\nAfter Deletion:")
    for product in products:
        print(product)

    # 데이터베이스 연결 종료
    db.close()
