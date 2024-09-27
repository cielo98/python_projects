a = (1, 3, 5)
b = (2, 4, 6)
c = list(a + b)
c.sort()
print(c)

d = [1, 2, 3, 4, 5]  # 리스트 d 생성
e = tuple(d)  # 리스트 d를 튜플 e로 변환
e = list(e)  # 튜플을 다시 리스트로 변환해 수정 가능하게 함
for i in range(len(e)):  # 리스트의 길이만큼 반복
    e[i] = e[i] + 10  # 각 요소에 10을 더함
e = tuple(e)  # 리스트를 다시 튜플로 변환
print(e)  # 최종 튜플 출력

a = [1, 2, 3, 4]
for i in a : 
	if i%2 == 0 :
		a.remove(i) 
	else :  
		continue
	print(a)
	
a = [1, 2, 3, 4]
a = [i for i in a if i % 2 != 0]  # 짝수를 제외하고 새 리스트 생성
print(a)

b = (5, 6, 7, 8)
b = [i for i in range(len(b)) if i%2 != 0]
print(tuple(b))	

# 두 개의 리스트 [1, 3, 5]와 [2, 4, 6]을 합쳐서 짝수와 홀수로 각각 나눈 튜플 (짝수 리스트, 홀수 리스트)를 생성하는 코드를 작성하시오.
a = [1, 3, 5] + [2, 4, 6]
a.sort()
a1 = [i for i in a if i%2 == 0]
a2 = [i for i in a if i%2 != 0]
print(tuple(a1))
print(tuple(a2))

# 사용자로부터 숫자들을 입력받아, 리스트와 튜플로 각각 변환한 뒤, 리스트는 오름차순으로 정렬하고 튜플은 내림차순으로 정렬하여 결과를 출력하는 코드를 작성하시오.
a = int(input("첫 번째 숫자를 입력하세요. : "))
b = int(input("두 번째 숫자를 입력하세요. : "))
c = int(input("세 번째 숫자를 입력하세요. : "))
x = list([a, b, c])
y = tuple((a, b, c))
x.sort()
y = list(y)
y.sort(reverse=True)
print(x)
print(tuple(y))

# a.append(x): 마지막 자리에 요소 추가, a.insert(i, x): 몇 번 자리에 무슨 요소 추가, a.extend([]): 마지막 자리에 리스트 추가
# del a[i]: 몇 번 자리의 요소 삭제, a.remove(a): 특정 요소 삭제, a. clear(): 모든 요소 삭제
# for i in 에서 리스트가 아니라 순서 없는 튜플이면 for i in range(len(a))
# 리스트 값 바꿀 때는 걍 list[2]=4 이런 식으로

total = 0
num = int(input("숫자를 입력하세요. : "))
for i in range(1, num + 1, 1) :
	if i%3 != 0 :
		continue
	else :
		total = total + i
print(total)


num1 = int(input("숫자를 입력하세요. : "))
total = 0
sb = 0
while sb < num1 :
	sb = sb +1
	if sb % 3 == 0:  # 3의 배수인 경우만 합산
		total = total + sb  # total에 3의 배수를 더함
print(f"3의 배수의 합은: {total}")

a = [35, 24, 46, 76, 52]
smallest = a[0]
for i in a:
	if i < smallest :
		a[0] = i
print(a[0])

while True :
	name = input("이름을 입력하세요. : ")
	bday = int(input("생년월일 6자리를 입력하세요. : "))
	if name == "강희원" and bday == 980820 :
		print("확인 완료")
		break
	elif name == "강희원" and bday != 980820 :
		print("bday가 잘못되었습니다.")
	elif name != "강희원" and bday == 980820 :
		print("name이 잘못되었습니다.")
	else : 
		print("다시 입력하세요.")

num = int(input("몇 단을 알고 싶으신가요? : "))
for i in range(1, 10, 1) :
	print(f"{num} x {i} = {i*num}")

i = 0
while i < 9 :
	i = i + 1
	print(f"{num} x {i} = {i*num}")

for i in range(1, 10, 1) :
	for j in range(1, 10, 1) :
		print(f"{i} x {j} = {i*j}")

for i in range(1, 6, 1) :
	for j in range(1, i+1, 1) :
		print(j, end=" ")
	print()

a = (('철수', 90, 85, 70, 86), ('영희', 68, 95, 89, 59), ('희원', 80, 70, 45, 100))
print


for i in a :
	name, korean, english, math, history = a[i][0:4]
	print(f"성명 :{name}")
	print(f"국어 :{korean}점")
	print(f"영어 :{english}점")
	print(f"수학 :{math}점")
	print(f"역사 :{history}점")
	print("------------------")