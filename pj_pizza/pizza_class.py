# 피자 메뉴 정의
class pizzas:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def pizza_menu(self):
        print(f"{self.type} : ({self.price}원)")
        print("------------------------------")

piz1 = pizzas("페퍼로니", 3000)
piz2 = pizzas("콰트로치즈", 3200)
piz3 = pizzas("콤비네이션", 3500)
piz4 = pizzas("불고기", 3600)
piz5 = pizzas("씨푸드", 3800)

pizza_list = [piz1, piz2, piz3, piz4, piz5]

# 주문 내역
def pizza_receipt():
    print("피자를 선택해주세요.")
    for pizza in pizza_list:
        pizza.pizza_menu()  # 인스턴스를 통해 메서드 호출
    
    pizza_order = input("피자 이름을 입력하세요. : ")
    pizza_number = int(input("수량을 입력하세요. : "))

    for pizza in pizza_list:
        if pizza_order == pizza.type:
            print("주문 내역 : ")
            print("피자 : ")
            print(f"{pizza_order} : {pizza_number}개 - {pizza.price * pizza_number}원")
            return  # 주문이 완료되면 함수 종료
    print("올바른 피자 이름을 입력하세요.")
    pizza_receipt()  # 올바르지 않은 경우 함수 재호출

pizza_receipt()