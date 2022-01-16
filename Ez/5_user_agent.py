import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()

with open("nadocoding-2.html", "w", encoding="utf8") as f:
    f.write(res.text)

# print("응답코드: ", res.status_code)
