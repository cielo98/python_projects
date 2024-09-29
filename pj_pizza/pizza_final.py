pizzas = {"페퍼로니" : 3000, "치즈" : 3200, "콤비네이션" : 3500, "불고기" : 3600, "해산물" : 3800}
drinks = {"콜라" : 1500, "사이다" : 1500, "생수" : 1000}

def select_menu() :
    order = []
    def select_pizza() :
        while True :
            pizza = input("원하는 피자를 입력하세요. 주문을 종료하려면 -을 입력하세요. : ")
            if pizza in pizzas :
                pnumber = int(input("원하는 수량을 입력하세요. : "))
                pprice = pizzas[pizza] * pnumber
                order.append([pizza, pnumber, pprice])
            elif pizza == "-" :
                return
            else : 
                print("올바른 피자 이름을 입력하세요. : ")
    select_pizza()

    def select_drink() :
        while True :
            drink = input("원하는 음료를 입력하세요. 주문을 종료하려면 -을 입력하세요. : ")
            if drink in drinks :
                dnumber = int(input("원하는 수량을 입력하세요. : "))
                dprice = drinks[drink] * dnumber
                order.append([drink, dnumber, dprice])
            elif drink == "-" :
                return
            else :
                print("올바른 음료 이름을 입력하세요. : ")
    select_drink()
    
    total_all = 0
    for menu, number, total in order :
        print(f"{menu} / {number}개 / {total}원")
        total_all = total_all + total
    print(f"총 가격 : {total_all}원")
select_menu()

# 개선된 코드
class MenuItem: # 메뉴 양식에 대한 클래스
    def __init__(self, name, price): # 메뉴 안에 들어가는 인스턴스
        self.name = name
        self.price = price

class Pizza(MenuItem): # 피자 메뉴도 양식 똑같아서 패스
    pass 

class Drink(MenuItem): # 음료 메뉴도 양식 똑같아서 패스
    pass 

class Order: # 주문에 대한 클래스
    def __init__(self): # 주문 클래스 안에 들어가는 인스턴스
        self.items = []
        self.total_price = 0

    def add_item(self, item, quantity): #상품 넣기
        total = item.price * quantity
        self.items.append((item.name, quantity, total))
        self.total_price += total

    def show_order(self):
        for name, quantity, total in self.items:
            print(f"{name} / {quantity}개 / {total}원")
        print(f"총 가격: {self.total_price}원")

class Menu:
    def __init__(self):
        self.pizzas = {
            "페퍼로니": Pizza("페퍼로니", 3000),
            "치즈": Pizza("치즈", 3200),
            "콤비네이션": Pizza("콤비네이션", 3500),
            "불고기": Pizza("불고기", 3600),
            "해산물": Pizza("해산물", 3800)
        }
        self.drinks = {
            "콜라": Drink("콜라", 1500),
            "사이다": Drink("사이다", 1500),
            "생수": Drink("생수", 1000)
        }

    def select_pizza(self, order):
        while True:
            pizza_name = input("원하는 피자를 입력하세요. 주문을 종료하려면 -을 입력하세요. : ")
            if pizza_name in self.pizzas:
                quantity = int(input("원하는 수량을 입력하세요. : "))
                order.add_item(self.pizzas[pizza_name], quantity)
            elif pizza_name == "-":
                break
            else:
                print("올바른 피자 이름을 입력하세요.")

    def select_drink(self, order):
        while True:
            drink_name = input("원하는 음료를 입력하세요. 주문을 종료하려면 -을 입력하세요. : ")
            if drink_name in self.drinks:
                quantity = int(input("원하는 수량을 입력하세요. : "))
                order.add_item(self.drinks[drink_name], quantity)
            elif drink_name == "-":
                break
            else:
                print("올바른 음료 이름을 입력하세요.")


# 실제 실행 부분
def main():
    menu = Menu()
    order = Order()

    menu.select_pizza(order)
    menu.select_drink(order)

    order.show_order()

main()

input_str = input("문자열을 입력하세요 : ")
reversed_str = input_str[::-1]
print(f"역순문자열 : {reversed_str}")

# 문자열에서... 영문 < 한글, 영문 대문자 < 소문자, 특수기호 및 숫자 < 영문 알파벳
# 정수형 실수형 섞을수도, 불린 값 비교할 수도
# True, False를 int화 하면 1, 0이 됨
# 단락 평가에서는 왼쪽 피연산자만 간단히 계산하여 참 거짓 = 판명
# .2f : 두 자리수까지
# all, any 활용하자

num = 30
divisor = 0
if divisor != 0 and num / divisor :
    print(f"{num} / {divisor} = {num / divisor}")
# 비트 연산: 비트는 데이터의 최소 단위로, 비트 연산은 정수를 이진수로 표현하여 각각 비트 단위로 수행하는 연산임 
# & : AND / l : OR / ^ : XOR / ~ : NOT / << : 비트 왼쪽 시프트 / >> : 비트 오른쪽 시프트
bin(10)
int('1010', 2)

password = input("비밀번호를 입력하세요. : ")
has_digit = any(char.isdigit() for char in password)
has_alpha = any(char.isalpha() for char in password)
is_valid_length = len(password) >= 8
is_valid_password = has_digit and has_alpha and is_valid_length
print(f"패스워드 검증 결과 : {"유효함" if is_valid_password else "유효하지 않음"}")
