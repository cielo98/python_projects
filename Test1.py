print("안녕하세요")
print('안녕하세요')
print(2)
'''
@this code is test.
@author tester
@write day is 2024/09/09

c = "asssskd"
'''

a= "hello"
b= "python"
c= "world"
d= "!"

print(a)
print(b)
print(c, d)

pizza_menu = {
    "small" : 8.99,
    "medium" : 12.99,
    "large" : 15.99
}

topping_menu = {
    "pepperoni" : 1.50,
    "mushrooms" : 1.00,
    "extra cheese" : 1.25,
    "olives" : 1.00
}

name = "강희원"

print(name)

print("홍길동", end=" ")
print("홍길동", end="(끝)")
print("홍길동", end = "(끝)\n")

print("홍", "길동", sep = "\n")
print("성 : 홍", "길동", sep = " 이름 : ")
print("홍", "길", "동", sep= "\n", end = "씨\n")
print("원주율 값", "3.1415", sep = " : ", end= "15\n")

print("홍길동", end = ' ')
print(2000, 1, 1, sep = '/')

print("python is fun!");
print("hello", "cruel", "world", sep = "\n")
print("He said, \"Python is awesome!\"") 
print(13%5)

name = "Alice"
print("Hello, " + name + "!")

name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

pi = 3.14159
print(f"{pi:.2f}")

x = 5
y = 10
print(f"x는 {x}이고 y는 {y}입니다.")

#This is a simple print statement.
'''
이 코드는...
'''

x = 15
if x > 10:
    print("x is greater than 10")
else:
    print("x is smaller than 10")

print(1, 2, 3, sep = ", ", end = ", 끝!")
print("hello")

print("python is fun!")
print("hello", "cruel", "world", sep = "\n")
print("He said, \"Python is awesome!\"") 
print(13%5)

print("쉘에서 작성하는 첫 번째 프로그램")
print("화면에 지금 입력하고 있는 내용이")
print("출력됩니다")
print("엔터키를 누를 때마다 한 줄씩")
print("따로 출력되는 것을 볼 수 있습니다.")
print("따옴표 없이 글자들만 출력되는")
print("것에 주의하세요")

# greet 함수
def greet(name):
    print("Hello, " + name)
greet("Alice")

# calculate_sum 함수
def calculate_sum(a, b):
    result = a + b
    print("두 수의 합은: ", result)

calculate_sum(2, 5)

nc = 30
nd = 40
print("nc=", nc, "nd=", nd)
nd = nc
print("nc=", nc, "nd=", nd)

result = nc * nd
print(nc, "*", nd, "는", result, "이다.")

pizza1 = "pepperoni pizza"
pizza2 = "cheese pizza"
price1 = 3500

print(pizza1, "(", price1, "원)")

Name = input("이름을 입력해주세요.")
print("그녀의 이름은 ", Name, "입니다.")

price = 10000
total_price = price * int(input("몇백그램 살 거니"))
print(total_price, "원")

a = 5
a += 2
print(a)

a *= 2
a /= 2
a //= 2
a %= 2
a **= 2

# Escape Sequence인 \
# \n: 줄바꿈
# \t: 탭
# \', \\. \" 등: 문자열 내에 해당 부호를 출력하고 싶을 때
print("첫\t번째 문장\n새로운 문장")

# type()은 자료형 구분할 때. type(True)할 때 반드시 대문자 T.
type(True)

complex(1.2, .3)