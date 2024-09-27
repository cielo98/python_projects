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
# 함수 호출 및 게임 시작
guess_number()