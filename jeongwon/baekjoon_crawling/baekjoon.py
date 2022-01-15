import requests
from bs4 import BeautifulSoup

code = "1"
url = "https://www.acmicpc.net/step/{code}".format(code=code)

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

datas = soup.select('#problemset > tbody > tr')
list_num = list()

# 크롤링 및 필요 데이터만 배열에 저장
for data in datas:
        number = data.select_one('td.list_problem_id')
        correct = data.select_one('td:nth-child(7)')

        if number == None:
                continue

        else:
                number = number.text
                correct = correct.text
                correct = float(correct.strip('%'))
                list_num.append([number, correct])

# 내림차순 정렬
list_num.sort(key=lambda x:x[1])
list_num.reverse()

for i in list_num:
        print(i[0], i[1])