import time
from selenium import webdriver
from bs4 import BeautifulSoup
options= webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
browser=webdriver.Chrome(options=options)
browser.maximize_window()
url="https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpb" \
    "mdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
browser.get(url)
prev_height=0
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 현재 페이지 가장 아래까지 내리기. 숫자도 가능
    time.sleep(2)
    cur_height=browser.execute_script("return document.body.scrollHeight")
    if cur_height==prev_height:
        break

    prev_height=cur_height


soup=BeautifulSoup(browser.page_source,'lxml')
movies=soup.find_all("div",attrs={"class":["Vpfmgd"]})  # list 로 2개 이상의 class 도 가져올 수 있다.
for movie in movies:
    print(movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text())
print(len(movies))
with open("movie.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
