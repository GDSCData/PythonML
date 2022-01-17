from dis import disco
import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

year = input("원하는 년도를 입력하세요 : ")
month = input("원하는 월을 입력하세요 : ")
week = input("원하는 주를 입력하세요 : ")

num = int(input("랭킹 : "))
num = num % 50 + 1

print("원하는 가격!")
want_price_h = int(input("최대 : "))
want_price_l = int(input("최소 : "))


for page in range(num):
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&Year={}&Month={}&Week={}&page={}&cnt=1000&SortOrder=1".format(year, month, week, num)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    books = soup.find_all("div", attrs = {"class" : "ss_book_box"})
    for book in books:
        book_info = book.find("td", attrs = {"width" : "*"}).find("li")
        if book_info.find("span", attrs = {"class" : "ss_ht1"}):
            book_info = book_info.next_sibling
        name = book_info.find("b")
        author = book_info.next_sibling.next_sibling
        price_a = author.next_sibling
        price = price_a.find("span").get_text()
        price = int(re.sub("\,","",price))


        if want_price_l > price or want_price_h < price:
            continue
        
        info_a = price_a.next_sibling
        info = info_a.find("b").get_text()
        info = int(re.sub("\,|\ ","",info))      #공백 , 제거
        if info < 10000:
            continue

        print(name.get_text())
        print(author.get_text())
        print(str(price)+"원")
        print(str(info)+"점")
        print("-------")