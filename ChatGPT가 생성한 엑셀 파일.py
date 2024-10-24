import random
from openpyxl import Workbook

# 제품 목록
products = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "헤드폰", "스피커", "TV", "모니터", "프린터",
    "키보드", "마우스", "외장하드", "SSD", "USB 메모리", "라우터", "게임 콘솔", "디지털카메라", "캠코더", "드론"
]

# 브랜드 목록
brands = ["삼성", "LG", "애플", "소니", "파나소닉", "필립스", "샤오미", "화웨이", "레노버", "델"]

# 데이터 생성 함수
def generate_product_data(num_records):
    for i in range(1, num_records + 1):
        product_name = f"{random.choice(brands)} {random.choice(products)}"
        quantity = random.randint(1, 100)
        price = round(random.uniform(10000, 2000000), -3)  # 10,000원에서 2,000,000원 사이의 가격, 1000원 단위로 반올림
        yield (i, product_name, quantity, price)

# Excel 파일 생성 및 데이터 저장
def create_excel_file(filename, data):
    wb = Workbook()
    ws = wb.active
    ws.title = "제품 판매 데이터"

    # 헤더 추가
    headers = ["제품ID", "제품명", "수량", "가격"]
    ws.append(headers)

    # 데이터 추가
    for row in data:
        ws.append(row)

    # 열 너비 자동 조정
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column_letter].width = adjusted_width

    # 파일 저장
    wb.save(filename)
    print(f"{filename} 파일이 생성되었습니다.")

# 메인 실행 코드
if __name__ == "__main__":
    num_records = 100
    filename = "products.xlsx"

    # 데이터 생성 및 Excel 파일 저장
    product_data = list(generate_product_data(num_records))
    create_excel_file(filename, product_data)

    # 생성된 데이터 일부 출력 (처음 5개)
    print("\n생성된 데이터 샘플 (처음 5개):")
    for row in product_data[:5]:
        print(row)