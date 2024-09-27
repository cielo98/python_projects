ra = int(input("첫 번째 정수를 입력해랑: "))
rb = int(input("두 번째 정수를 입력해랑: "))
rc = ra + rb
print(ra, "+", rb, "값은", rc, "이당")

a = float(input("실수 1: "))
b = float(input("실수 2: "))
result = a + b
print(a, "+", b, "는", result, "이다.")

coffee100 = 10000
coffeeprice = coffee100
coffeeprice += coffee100

print("커피 200g", coffeeprice)

print("안녕하세요. 제 이름은 %s입니다." %"파이썬")
print("안녕하세요. 제 나이는 %d입니다." %25)

adress = "구성로 470 401동 504호"
temperature = 35
print("지역 : %s" %adress)
print("온도 : %d도" %temperature)

print("너비가 %d이고 높이가 %d인 사각형의 넓이는 %d이다" %(20, 30, 20*30))
print("원주율: %.2f" %3.1415)
# pi:.2f 아니면 %.2f

print("%10s" %"한글")
#특정 자릿수로 문자열을 출력

print("오늘의 습도는 %d%%입니다." %70)
#뒤에 % 붙이고 싶으면 뒤에 %%

print("그가 말했다, \"사랑한다고\"")

print("%d년 아카데미 영화제 작품상은 %s가 받았다." %(2020, "기생충"))
#다수 서식자를 입력할 때는 괄호에 묶어서 한 번에

coffee100 = 10000
weight = 200
print("커피 원두 %dg 가격: %d" %(weight,  weight // 100 * coffee100))

width = 30
height = 30
print(f"{{너비가 {width}이고 높이가 {height}인 사각형의 넓이는 {width * height}이다.}}")

coffee100 = 10000
weight = 200
print(f"커피 원두 {weight}g 가격: {weight // 100 * coffee100}")
weight = 300
print(f"커피 원두 {weight}g 가격: {weight // 100 * coffee100}")

age = int(input("나이를 입력하세요: "))
print("당신의 나이는", age, "입니다.")

x = 10
y = 20
z = 30
print(x + y + z)

x, y = y, x

a = "Hello"
a = "World"
print(a, a, sep=" ")

x = 5
y = x + 10
x = y + 5
print(x, y)

x = 30
y = 28
print((x + y) / 2)

print(type(x))

name = input("이름 : ")
age = int(input("나이 : "))
print(f"안녕하세요, {name}님. 당신은 {age}살 입니다.")

x = int(input())
y = int(input())
print(x*y)

print("%.1s" %input())

x = "python"
print(f"{x}")

x = 20
y = 30
z = 40
print((x + y + z) / 3)


