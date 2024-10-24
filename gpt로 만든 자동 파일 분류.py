import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
image_folder = r'C:\Users\student\Downloads\images'
data_folder = r'C:\Users\student\Downloads\data'
docs_folder = r'C:\Users\student\Downloads\docs'
archive_folder = r'C:\Users\student\Downloads\archive'

# 각 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)  # 이미지 파일을 위한 폴더
os.makedirs(data_folder, exist_ok=True)   # 데이터 파일을 위한 폴더
os.makedirs(docs_folder, exist_ok=True)   # 문서 파일을 위한 폴더
os.makedirs(archive_folder, exist_ok=True) # 압축 파일을 위한 폴더

# 파일 이동 규칙 정의
file_types = {
    ('*.jpg', '*.jpeg'): image_folder,    # jpg, jpeg는 images 폴더로
    ('*.csv', '*.xlsx'): data_folder,     # csv, xlsx는 data 폴더로
    ('*.txt', '*.doc', '*.pdf'): docs_folder,  # txt, doc, pdf는 docs 폴더로
    ('*.zip',): archive_folder            # zip 파일은 archive 폴더로
}

# 다운로드 폴더에서 파일을 순회하면서 이동
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    
    # 파일일 경우만 처리 (폴더는 무시)
    if os.path.isfile(file_path):
        # 파일 확장자에 따른 처리
        file_extension = filename.lower().split('.')[-1]  # 확장자를 소문자로 변환
        
        # 파일을 지정된 폴더로 이동
        if filename.endswith(('.jpg', '.jpeg')):
            shutil.move(file_path, image_folder)
        elif filename.endswith(('.csv', '.xlsx')):
            shutil.move(file_path, data_folder)
        elif filename.endswith(('.txt', '.doc', '.pdf')):
            shutil.move(file_path, docs_folder)
        elif filename.endswith('.zip'):
            shutil.move(file_path, archive_folder)

print("파일 이동이 완료되었습니다.")
