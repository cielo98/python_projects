# 피자 메뉴 정의
class pizzas :
    def __init__(self, type, price) : 
        self.type = type
        self.price = price
    
    def pizza_menu(self) :
        print(f"{self.type}  : ({self.price}원)")
        print("------------------------------")
    
    def pizza_type(self) :
        return self.type

    def pizza_price(self) :
        return self.price

piz1 = pizzas("페퍼로니", 3000)
piz2 = pizzas("콰트로치즈", 3200)
piz3 = pizzas("콤비네이션", 3500)
piz4 = pizzas("불고기", 3600)
piz5 = pizzas("씨푸드", 3800)

pizza_list = [piz1, piz2, piz3, piz4, piz5]

# 주문 내역
def pizza_receipt() :
    print("피자를 선택해주세요.")
    for pizza in pizza_list : 
        pizzas.pizza_menu()
    
    pizza_order = input("피자 이름을 입력하세요. : ")
    pizza_number = int(input("수량을 입력하세요. : "))
    
    for pizza in pizza_list :
        if pizza_order == pizza.pizza_type() : 
            print("주문 내역 : ")
            print("피자 : ")
            print(f"{pizza_order} : {pizza_number}개 - {pizza.pizza_price() * pizza_number}원")
        else : 
            print("올바른 피자 이름을 입력하세요.")
            return pizza_receipt()