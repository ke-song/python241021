# DemoRe.py

import re

result = re.search('[0-9]*th', '  35th')
print(result)
print(result.group())

result2 = re.search('ap', 'this is apple')
print(result2.group())

result3 = re.search('\d{4}', '올해는 2024년')
print(result3.group())

result4 = re.search('\d{5}', '우리동네는 52300')
print(result4.group())




def is_valid_email(email):
    # 이메일 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.search 함수를 사용하여 패턴 매칭
    if re.search(pattern, email):
        return True
    else:
        return False

# 테스트 샘플
test_emails = [
    "user@example.com",                # 유효한 기본 이메일
    "user.name@example.co.kr",         # 유효한 이메일 (복합 도메인)
    "user+tag@example.com",            # 유효한 이메일 (+ 기호 포함)
    "123.456@example.com",             # 유효한 이메일 (숫자 포함)
    "user-name@example.com",           # 유효한 이메일 (하이픈 포함)
    "user@subdomain.example.com",      # 유효한 이메일 (서브도메인)
    "user@example",                    # 잘못된 이메일 (최상위 도메인 없음)
    "user@.com",                       # 잘못된 이메일 (도메인 이름 없음)
    "@example.com",                    # 잘못된 이메일 (로컬 파트 없음)
    "user@example.",                   # 잘못된 이메일 (최상위 도메인 불완전)
]

# 테스트 실행
for email in test_emails:
    if is_valid_email(email):
        print(f"{email} 은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email} 은(는) 유효하지 않은 이메일 주소입니다.")


