import re
# . : 하나의 문자 (ca.e 는 ca?e 문자)
# ^ : 문자열의 시작 (^d 는 d로 시작하는 문자)
# $ : 문자열의 끝 (hi$ 는 hi 로 끝나는 문자)
p=re.compile("ca.e")
m=p.match("case")  # match 는 해당 re와 일치하는지 확인. 한번 매치 되면 뒤에는 무시한다
m2=p.search("case cake")  # search 는 주어진 문자열 중에 있는지 확인. 이것도 한개의 값을 찾으면 뒤에는 무시
m_lst=p.findall("case cake")  # 여러개를 list 로 반환
print(m.group())  # 일치하는 문자열 반환
print(m.string)  # 입력받은 문자열 반환
print(m.start())  # 일치하는 문자열의 시작 index 반환
print(m.span())  # 일치하는 문자열의 시작, 끝 index 반환
print(m_lst)