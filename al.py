total = 0
for sb in range (1, 6, 1) :
    total = total + sb
print(total)

sb = 1
while sb < 4 : 
    print(sb)
    sb = sb + 1

sb = 0
while sb < 4 : 
    sb = sb + 1
    print(sb)

for sb in range(0, 5, 1) :
    print(sb, end = " ")

total = 0
for sb in range(1, 11, 1) :
    total = total + sb
print("\n", total)

total = 0
sb = 0
while sb < 6 :
    sb = sb + 1
    total = total + sb
print(total)

sb = 1
while True :
    print(sb)
    sb = sb + 1
    if sb > 3 :
        break

num = int(input("숫자를 입력하세요. : "))
total = 0
sb = 0
while sb < num :
    sb = sb + 1
    total = total + sb
print(total)

num = int(input("숫자를 입력하세요. : "))
total = 0
sb = 0
while True :
    sb = sb + 1
    total = total + sb
    if sb > num-1 :
        break
print(total)

first_num = int(input("첫 번째 숫자를 입력하세요. : "))
last_num = int(input("마지막 숫자를 입력하세요. : "))
total = 0
for i in range(first_num-1, last_num, 1) :
    i = i + 1
    total = total + i
print(total)

first_num = int(input("첫 번째 숫자를 입력하세요. : "))
last_num = int(input("마지막 숫자를 입력하세요. : "))
sb = first_num-1
total = 0
while True :
    sb = sb + 1
    total = total + sb
    if sb > last_num-1 :
        break
print(total)

first_num = int(input("첫 번째 숫자를 입력하세요. : "))
last_num = int(input("마지막 숫자를 입력하세요. : "))
total = 0
for i in range(first_num-3, last_num, 1) : 
    if i%3 == 0 :
        i = i + 3
        total = total + i
        if i > last_num :
            break
print(total)


tuple = (3, 6, 9)
tuple.index(6)
(3, 6, 9) + (4, 5)
len(0, 20, 30, 40)
tuple2 = (1, 2, 3, 4)
tuple2[0:2]

a = (1, 3, 5)
b = (2, 4, 6)
c = a + b
list(c)
print(list(c).sort())