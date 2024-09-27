# 변수 x에 정수 5를, 변수 y에 문자열 "10"을 할당하고, 이 두 변수를 더한 값을 정수로 변환하여 출력하는 코드를 작성하시오.
x = 5
y = "10"
print(str(x + int(y)))

# [] 안에 인덱스 입력하면 이에 해당하는 문자 출력
s = "Hi, everyone. \n"
s[0]
s[-1]
s[len(s) - 1] # 이건 뭐? -> 15-1 해서 숫자로 [] 안에 들어간다!
print(s[-2])
print(s[-2])

# 변수.startswith() 하면 변수가 특정 글자로 시작하는지
s.startswith("g")
s.endswith("\n")

# in은 문자열 1이 문자열 2에 들어가있는지 확인함
"wor" in s
"ld" in s

# index, find는 문자열1이 문자열2의 어디에 들어가있는지 확인함
s.index("every")
s.find("hi") # find는 만약에 없으면 -1 반환

# 특정 구간에서 찾기도 가능 -> 문자열.index(검색할 문자열, 시작 인덱스, 끝 인덱스)
s.index('i', 0, 6)

# rindex(), rfind()는 뒤에서부터 검색
"Bye Bye". rfind("Bye")
"Bye Bye". rindex("Bye")
s.rindex("every")

# s[시작 인덱스 : 마지막 인덱스]로 문자열 추출 가능. 마지막 인덱스 '전까지!'
s[3:5]
s[:-1]

# lstrip()으로 왼쪽 끝 공백 제거
" hello \n" .lstrip()
" hello \n " .rstrip()

# l/rstrip("문자조합")으로 왼/오 끝에서 나올 수 있는 모든 조합 제거
" hello you가나다" .rstrip("가h나")

# strip은 양쪽 제거
"@rora@" .strip("@")
"aaaaaadoryaaaaaaaaaa" .strip("a") # 입력한 문자를 '모두' 제거

# replace(oldString, newString)으로 문자열 치환 (낱말 전체)
"뜨거운 커피" .replace("뜨거운", "차가운")
"뜨거운 커피, 뜨거운 사랑" .replace("뜨거운", "차가운", 1) # 마지막 숫자로 몇 번 치환할 지 선택 가능

# isalnum() 문자열이 알파벳, 한글, 숫자로만 구성되었는지 확인
"rora99874^^" .isalnum()

# isalpha() 문자열이 알파벳, 한글로만 구성되었는지
"희원isQueen" .isalpha()

# isdigit(), isnumeric() 문자열의 글자가 숫자로만 구성되었는지
"hello98" .isdigit()

# islower 문자열이 소문자로만 구성되었는지
"yooooo" .islower()

# isupper 문자열이 대문자로만 구성되었는지
"KING" .isupper()

# upper() 대문자로 변환
# lower() 소문자로 변환
# swapcase() 대문자는 소문자로, 소문자는 대문자로 변환
# capitalize() 첫 글자만 대문자로
# count(str) 문자열에서 주어진 문자열인 str이 몇 번 나오는지

# She said, "It's a beautiful day." He replied, "Yes, it is!"
print("She said, \"Its a beautiful day.\" He replied, \"Yes, it is!\"")

s = "hi everyone"
s. replace("hi", "greetings")
s.startswith("G")

"test".encode()
"파이썬".encode()
"파이썬".encode("utf-16")
"파이썬".encode("cp949")

"hello".encode("utf-8")
b'hello'.decode("euc-kr")

word = "한국어"
word1 = word.encode('utf-8')
print(word1)
word2 = word1.decode('utf-8)')
print(word2)
word3 = word2.encode('euc-kr')
print(word3)
word4 = word3.decode('euc-kr')
print(word4)

s = "Hello, World!"
len(s)

print(range(10))
print(tuple(range(0, 10, 3)))
a = [0, 10, True, "닐리리야"]
len(a)
b = [4, 7, "옹"]
a + b
b. index("옹")
b.index()
index = 1
hello = "hello"
hello[0]

# 값 고치는 건 리스트 타입만 가능~
b = [4, 7, "옹"]
del b[2]

a[1:1] # 아무거도 안 가져옴
a[1:2] # 하나 가져옴
# 참고로, 출력할 때는 값을 수정하는게 아니라 새로 생성하는 거임

# 인덱스를 특정한 값만큼 증가시키면서 가져올 수도 있음
d = [10, 20, 30, 40, 50, 60, 70, 80, 90]
d[2:8:3]

f = (4, 6, 5)
f[1] = 5

h = "string"
g = [1, 2, 3]
j = (3, 5, 7)
r = range(5, 10, 2)
h[3]
g[2]
j[1]
r[2]
d[0:len(d)-1]
#인덱스로 접근해서 값 바꾸는 건 안됨
# [:7] 이런 식으로 하면 0부터
# numpy(2, 3차원 데이터), pandas 라이브러리로 데이터 처리 가능. include numpy
d[7::2] # 인덱스 7부터 2씩 증가시키면서 마지막 값까지 가져옴
d[::2] # 0부터 2씩 증가, 끝까지
d[0:len(d)-1:2] 
d[:]
d[4::2]
d[:-1]

len(list(r)) #콤마하고 start=1 이런 식으로 줄수도

# 아래처럼 특정 범위를 하나의 값으로 바꿀수도 있음
a = [0, 10, 20, 30, 40, 50, 60, 70, 80]
a[4:7] = ["a"] # 첫 값만 a 적용 
print(a)