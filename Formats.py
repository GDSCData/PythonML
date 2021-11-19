from bs4 import BeautifulSoup
import json
import yaml
import csv, codecs
import openpyxl

#xml
savename = "forecast.xml"
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')
la=soup.find_all("location")  # 무조건 소문자로 반환
name = la.find('city').string  # 그 안에서 다시 city 를 찾고 그 안의 string 값 반환


#json
s = open(savename, "r", encoding="utf-8").read()
items = json.loads(s)  # 여기 안에 배열 형태로 저장이 돼있음. load 는 주솟값을 저장
tmp={"data":"wow","time":22}
s2=json.dumps(tmp)  # 바로 제이슨 형식으로 변환.


#yaml
str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
"""
customer = [
    { "name": "InSeong", "age": "24", "gender": "man" },
    { "name": "Akatsuki", "age": "22", "gender": "woman" },
    { "name": "Harin", "age": "23", "gender": "man" },
    { "name": "Yuu", "age": "31", "gender": "woman" }
]
yaml_str = yaml.dump(customer)
print(yaml_str)
data = yaml.safe_load(yaml_str)
for item in data['PriceList']:
    print(item["name"], item["price"])


#csv
fp = codecs.open("list-euckr.csv", "r", "utf-8")
# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])


#xlsx
book = openpyxl.load_workbook("filename")
sheet = book.worksheets[0]
data = []
for row in sheet.rows:
    data.append([row[0].value,row[10].value.replace(",", "")]) # 엑셀에서 , 가 있는 숫자일 경우 저걸로 없애준다.
print(sheet["A4"].value)
filename = "population.xlsx" # 다른 이름으로 다시 저장하기
book.save(filename)