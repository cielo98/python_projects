# continue 밑 블록을 실행하지 않고 다시 맨 처음으로
for sb in range (1, 11, 1) : 
    if sb&2 == 0 :
        continue
        stra = "짝수이다"
    else :
        stra = "홀수이다."
print(sb, "는", stra)

# 응용 - 369 게임
for sb in range(1, 11, 1) : 
    if sb%3 == 0 :
        continue
    else :
        print(sb)

# break를 걸면 특정 변수에서 멈출 수 있음
na = int(input("멈추려는 정수값? : "))
for sb in range(0, 100, 1) : 
    if sb == na :
        break
        print(sb, "는 종료값이다.")
    print(sb + 1, sep = "\n", end = "\n")

# total로 누적합 가능한데, 각 라인의 indentation에 따라 결과값이 달라짐
total = 0 # <- total=0이 for 구문 밖에. 올바르게 출력
for sb in range(1, 6, 1):
    total = total + sb
print(total)

for sb in range(1, 6, 1):
    total = 0 # <- total=0이 for 구문 안에. total+sb가 값에 대한 더하기가 아니라 값으로 출력되어 범위 안 마지막 값이 출력됨
    total = total + sb
print(total)

for sb in range(1, 6, 1):
    total = 0
    total = total + sb
    print(total) # <- print가 for 구문 안에. 더하기가 안되고 for 반복문만 출력됨

# while 조건문은 무한 반복되지 않도록 block이 필요함
sb=0
while sb < 3:
    sb = sb + 1
    print(sb)

# for, while 모두 반복변수 정의(a=0)는 구문 밖에서, 반복변수 + 1(a=a+1)은 구문 안에서 print 다음에
sc = 0
while sc < 9 :
    print(sc)
    sc = sc + 1

sc = 0
total = 0
while sc < 9 :
    sc = sc + 1
    total = total + sc
print(total)


''' 클래스 (Class)
클래스는 객체를 생성하기 위한 설계도(청사진)입니다.
클래스는 속성(변수)과 메서드(함수)를 정의하고, 이 클래스의 인스턴스를 만들어서 사용할 수 있습니다.
예를 들어, Person이라는 클래스를 만들면, 사람의 이름, 나이 등의 속성(데이터)과 걷기, 말하기 등의 동작(메서드)을 정의할 수 있습니다. '''

class person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def greet(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고 나이는 {self.age}입니다.")

''' 2. 인스턴스 (Instance)

    인스턴스는 클래스에서 만들어낸 구체적인 객체입니다. 클래스로부터 생성된 실체라고 볼 수 있습니다.
    클래스는 설계도이고, 인스턴스는 그 설계도로 만든 실제 물건입니다.
    예를 들어, Person 클래스를 사용해서 여러 명의 사람을 인스턴스로 생성할 수 있습니다. '''

p1 = person("Alice", 30)
p2 = person("Bob", 25)

p1.greet()
p2.greet()

''' 1. 인스턴스 메서드 (Instance Method)

    인스턴스 메서드는 클래스의 인스턴스와 연결된 메서드입니다.
    첫 번째 매개변수로 항상 self를 받아야 하며, 이를 통해 해당 인스턴스의 속성에 접근하거나 다른 메서드를 호출할 수 있습니다.
    self는 현재 인스턴스를 가리킵니다. '''

class Dog :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def bark(self) :
        print(f"멍멍! {self.name}이 짖습니다!")

    def get_age(self) :
        print(f"{self.name}의 나이는 {self.age}살입니다.")

dog1 = Dog("Mango", 10)
dog2 = Dog("Tofu", 4)

dog1.bark()
dog2.get_age()

''' 2. 클래스 메서드 (Class Method)

    클래스 메서드는 클래스 자체에 속하는 메서드입니다.
    첫 번째 매개변수로 cls를 받아야 하며, 이는 현재 클래스를 가리킵니다.
    클래스 메서드는 클래스의 속성에 접근하거나 클래스 레벨에서 무언가를 처리할 때 유용합니다.
    @classmethod 데코레이터를 사용하여 정의합니다. '''

class Dogs :
    dogs_count = 0

    def __init__(self, name, age) :
        self.name = name
        self.age = age
        Dogs.dogs_count += 1
    
    @classmethod
    def get_dogs_count(cls) :
        return cls.dogs_count
    
dog3 = Dogs("Hayase", 15)
dog4 = Dogs("Zelda", 3)

print(f"개는 {Dogs.get_dogs_count()} 마리 입니다.")

''' 3. 정적 메서드 (Static Method)

    정적 메서드는 클래스나 인스턴스와 무관한 메서드입니다.
    첫 번째 매개변수로 self나 cls를 받지 않으며, 클래스와 독립적으로 동작합니다.
    @staticmethod 데코레이터를 사용하여 정의합니다.
    주로 클래스와 연관된 유틸리티 함수를 정의할 때 사용됩니다. '''

class Doggy : 
    @staticmethod
    def is_puppy(age) :
        return age < 1

print(Doggy.is_puppy(0.5))
print(Doggy.is_puppy(3))