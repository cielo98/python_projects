#/t는 다음 줄과 연속으로 연결

# %d = 정수, %f = 소수 %s = 문자열 
adress = "구성로 470 401동 504호"
temperature = 35
print("지역 : %s" %adress)
print("온도 : %d도" %temperature)
print("너비가 %d이고 높이가 %d인 사각형의 넓이는 %d이다" %(20, 30, 20*30)) #인수가 여러 개일 때는 괄호로 묶기
print("원주율: %.2f" %3.1415) # 소수점 n째 자리까지 출력 가능
print("%10s" %"한글") #특정 자릿수까지 문자열을 출력하는 것도 가능
print("오늘의 습도는 %d%%입니다." %70) #뒤에 % 붙이고 싶으면 뒤에 %%

# key=lambda x=x[1] > 리스트의 n번째 항목을 기준으로 정렬
# map(lamda x: x*2) > 리스트의 모든 항목을 한 번에 변경
test_list = [1, 2, 3, 4]
square_list = list(map(lambda x: x**2, test_list))
square_list

# startswith, endswith로 참, 거짓 확인
# strip, lstrip, rstrip으로 특정 위치의 문자열을 지우기
# split으로 문자열 나누기 > x.split(",")
# 함수 혹은 클래스에서 디폴트 값을 주는 인수는 무조건 제일 뒤로 보냄 (Ex. def a(x, y=0))

# help(객체) 하면 도움말 나옴
def hello() :
    '''이  함수는 ㅇㅇㅇ 하는 함수입니다.'''
    print("hello")
help(hello)

#dict의 키 값으로 값 수정 가능한 객체는 사용할 수 없음 (리스트, 딕셔너리 등) values로는 사용 가능
#리스트에서 del[n] 하면 n자리 삭제, remove(a) 하면 a라는 값을 삭제
# append = 하나의 값 더하기 / extend = 리스트 더하기 / insert = 특정 위치에 삽입하기

# import random : 랜덤한 무언가를 가져온다
sum = 0
n = 1
while n < 10 :
    n2 = int(input("숫자를 입력하세요. : "))
    n = n + 1
    sum = sum + n2
    print(sum)

import random
def sum_of_random_numbers(n) :
    total = 0
    for _ in range(n) :
        rand_num = random.randint(1, 100)
        print(f"생성된 랜덤 숫자: {rand_num}")
        total += rand_num
    return total

n = int(input("랜덤 숫자의 개수를 입력하세요. : "))
total_sum = sum_of_random_numbers
print(f"랜덤 숫자들의 합 : {total_sum}")

import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    guessed = False
    while not guessed:
        user_guess = int(input("숫자를 입력하세요 (1-100):"))
        if user_guess < number_to_guess:
            print("더 큰 수입니다.")
        elif user_guess > number_to_guess:
            print("더 작은 수입니다.")
        else:
            print("정답입니다!")
            guessed = True
guess_number()