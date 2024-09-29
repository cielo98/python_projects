s = "hello world and everyone in it"

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

s = "hi everyone"
s. replace("hi", "greetings")
s.startswith("G")

# 인코딩과 디코딩
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