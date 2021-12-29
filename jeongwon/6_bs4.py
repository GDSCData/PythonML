import requests
from bs4 import BeautifulSoup

url = "http://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)                 #soup 객체에서 처음 발견되는 a element
print(soup.a.attrs)           #a element의 속성정보
print(soup.a["href"])         #a element의 href 속성 값 정보

print(soup.find("a", attrs={"class":"Nbtn_upload"}))        #class="Nbtn_upload"인 a element
print(soup.find(attrs={"class":"Nbtn_upload"}))             #class="Nbtn_upload"인 어떤 element

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

print(rank1.parent)
print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="전지적 독자 시점-083. Ep. 18 독자의 싸움 (1)")
print(webtoon)

rank = rank1.find_next_siblings("li")

print("1위:", rank1.a.get_text())
for row, i in enumerate(rank):
    print(f"{row + 2}위: {i.a.get_text()}")

cartoons = soup.find_all("a", attrs={"class":"title"})

for i in cartoons:
    print(i.get_text())