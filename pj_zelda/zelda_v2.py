# 캐릭터 능력치 정의하기
characters = [{"Name" : "Link", "Attack" : 90, "Defense" : 90, "Healing" : 15, "Magic" : 0}, {"Name" : "Zelda", "Attack" : 60, "Defense" : 80, "Healing" : 15, "Magic" : 100}, {"Name" : "Revali", "Attack" : 90, "Defense" : 70, "Healing" : 10, "Magic" : 0}, {"Name" : "Mipha", "Attack" : 70, "Defense" : 70, "Healing" : 100, "Magic" : 50}, {"Name" : "Daruk", "Attack" : 80, "Defense" : 90, "Healing" : 10, "Magic" : 0}, {"Name" : "Urbosa", "Attack" : 90, "Defense" : 80, "Healing" : 10, "Magic" : 40},]

# 전체 캐릭터 보여주기
print("전체 캐릭터 능력치")
print("----------------------------------------")
for i, character in enumerate(characters, start=1) :
    total_stats = character["Attack"] + character["Defense"] + character["Healing"] + character["Magic"]
    print(f"{i}. {character["Name"]}")
    print(f"Attack : {character["Attack"]}")
    print(f"Defense : {character["Defense"]}")
    print(f"Healing : {character["Healing"]}")
    print(f"Magic : {character["Magic"]}")
    print(f"총 능력치 : {character[total_stats]}")

# 캐릭터 선택하기
def choose_character() : 
    choice = int(input("원하는 캐릭터의 번호를 입력하세요 : "))
    selected_character = characters[choice - 1]
    total_stats_sel = selected_character["Attack"] + selected_character["Defense"] + selected_character["Healing"] + selected_character["Magic"]
    if 0 < choice < 7 : 
        print("아래 캐릭터를 선택하시겠습니까?")
        print(f"{i}. {selected_character["Name"]}")
        print(f"Attack : {selected_character["Attack"]}")
        print(f"Defense : {selected_character["Defense"]}")
        print(f"Healing : {selected_character["Healing"]}")
        print(f"Magic : {selected_character["Magic"]}")
        print(f"총 능력치 : {selected_character[total_stats_sel]}")
        print("-------------------------------------------")
        return yes_or_no()
    else : 
        print("올바른 번호를 입력하세요.")
        return choose_character()
    
# 예 아니오
def yes_or_no() :
    yorn = input("번호가 맞다면 y를, 틀리다면 n을 눌러주세요. : ")
    if yorn == "y" : 
        return main()
    elif yorn == "n" :
        return choose_character()
    else :
        print("y와 n 중 하나를 입력해주세요.")
        return yes_or_no()
    
# 메인 화면
def main() : 
    name = input("플레이어 님의 이름을 적어주세요. : ")
    print(f"환영합니다, {name} 님.")
