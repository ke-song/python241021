# web2.py

from bs4 import BeautifulSoup

import requests

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

#검색이 용이한 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

# f = open("daangn.txt", "wt", encoding="utf-8")
f = open("daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", class_="card-desc")

for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    regionElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n", "").strip()
    price = priceElem.text.replace("\n", "").strip()
    region = regionElem.text.replace("\n", "").strip()
    #내부 문자열 출력
    # print(titleElem.text.strip(), priceElem.text.strip(), regionElem.text.strip())    
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")

f.close()

# <div class="card-desc">
#       <h2 class="card-title">석유 난로</h2>
#       <div class="card-price ">
#         20,000원
#       </div>
#       <div class="card-region-name">
#         강원도 춘천시 효자3동
#       </div>


