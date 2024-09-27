#/t는 다음 줄과 연속으로 연결
# print("%s는 %d점을 받았습니다." %("Alice", 85))
# print("%10s는 %50d점을 받았습니다." %("Alice", 85)) <- 간격 조정
# print("%10s는 %.5f점을 받았습니다." %("Alice", 85)) <- 소수점 조정
# key=lambda x=x[1]
# startswith, endswith, strip, lstrip, rstrip
# 디폴트 값 주는 정수는 무조건 제일 뒤로 보냄!! def a(x, y=0)
# help(객체) 하면 도움말 나옴
#map과lambda 같이 사용하면 리스트의 모든 값에 적용

test_list = [1, 2, 3, 4]
square_list = list(map(lambda x: x**2, test_list))
square_list


def hello() :
    '''이  함수는 ㅇㅇㅇ 하는 함수입니다.'''
    print("hello")
help(hello)


dir(__builtins__)

import os
os.getcwd()