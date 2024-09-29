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