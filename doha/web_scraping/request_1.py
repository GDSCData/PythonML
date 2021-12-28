import requests
url="http://nadocoding.tistory.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url,headers=headers)
# res.raise_for_status()  # 제대로 응답 되는지 체크. 안되면 error

print(res.status_code)
print(len(res.text))
print(res.text)

with open("my_google.html","w",encoding='utf8') as f:
    f.write(res.text)
