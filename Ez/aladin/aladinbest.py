from dis import disco
import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

for page in range(1):
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=EBookBestseller&BranchType=9&CID=0&page={}&cnt=300&SortOrder=1".format(page)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    books = soup.find_all("div", attrs = {"class" : "ss_book_box"})
    
    for book in books:
        options = soup.find_all("div", attrs = {"class" : "ss_book_list"})
        # for option in options:
        price = int(book.find("span", attrs = {"class" : "ss_p2"}).get_text()[0:-5]+book.find("span", attrs = {"class" : "ss_p2"}).get_text()[-4:-1])
        discount = book.find("span", attrs = {"class" : "ss_p"}).get_text()
        if discount:
            print(discount)
        else:
            print("할인안함")
        # print(price)
        # rate = img scr 	https://image.aladin.co.kr/img/common/star_s10.gif
        # rate_cnt = option.find("a", attrs = {"class" : }).get_text()
        # print(rate_cnt)


