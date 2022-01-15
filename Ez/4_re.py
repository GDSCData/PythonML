import re
p = re.compile("ca.e")
# . : 문자 하나 > ca.e > care, case...
# ^ : 문자열 시작 > ^de > desk, destination...
# $ : 문자열 끝 > se$ > case, base ...

def print_match(m):
    if m:
        print("m.group() ", m.group()) #일치하는 문자열
        print("m.string ", m.string) #입력받은 문자열
        print("m.span() ",m.span()) #일치하는 문자열의 시작과 끝
    else:
        print("매칭안됨")

# m = p.match("careless") #match : 처음부터 매치되는 지
# print_match(m)

# m = p.search("good care") #search : 주어진 문자열 중에 있는지
# print_match(m)

lst = p.findall("good care cafe") #findall : 일치하는 모든 것 리스트로 반환
print(lst)

# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("") : 주어진 문자열 중에 일치하는게 있는지
# 4. lst = p.findall("") : 일치하는 모든 것 리스트로 반환
