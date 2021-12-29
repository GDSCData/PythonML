import re

p = re.compile("ca.e") #.이 하나의 문제 의미 / ^은 문자열 시작 의미 / $는 문자열의 끝 의미

#m = p.match("case")
#print(m.group())

m = p.search("good care")

print("m.group() ", m.group()) #일치하는 문자열 반환
print("m.string ", m.string)   #입력받은 문자열
print("m.start()", m.start())  #일치하는 문자열의 시작 index
print("m.end() ", m.end())     #일치하는 문자열의 끝 index
print("m.span() ", m.span())   #일치하는 문자열의 시작 / 끝 index