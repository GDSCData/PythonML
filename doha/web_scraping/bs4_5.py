# 구글 무비에서 영화 다 가져오고, movie.html 안에 html 코드도 적어 보기.
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url="https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
movies=soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
for movie in movies:
    print(movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text())
print(len(movies))
with open("movie.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
