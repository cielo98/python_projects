# 수정본

# 캐릭터 정의
characters = [
    {"name": "Link", "attack": 90, "defense": 80, "healing": 15, "magic": 0}, # 변수가 할당되어 있으므로 dict형
    {"name": "Zelda", "attack": 30, "defense": 80, "healing": 15, "magic": 90},
    {"name": "Revali", "attack": 80, "defense": 70, "healing": 10, "magic": 0},
    {"name": "Mipha", "attack": 70, "defense": 60, "healing": 90, "magic": 40},
    {"name": "Daruk", "attack": 80, "defense": 80, "healing": 15, "magic": 0},
    {"name": "Urbosa", "attack": 90, "defense": 70, "healing": 10, "magic": 50},
]

# 캐릭터 출력
def show_character() : 
    for i, character in enumerate(characters, start=1) : # 첫 번째 항목부터 시작해서 리스트의 모든 항목을 반복하여 순서와 함께 출력한다. 
        total_stat = character["attack"] + character["defense"] + character["healing"] + character["magic"] # total_stat을 정의한다.
        print(f"{i}. {character["name"]}")
        print(f"공격력 : {character["attack"]}")
        print(f"방어력 : {character["defense"]}")
        print(f"치유력 : {character["healing"]}")
        print(f"마법력 : {character["magic"]}")
        print(f"총 능력치 : {character[total_stat]}")


# 캐릭터 선택 '기능'
def choose_character() :
    choice = int(input("원하는 캐릭터의 번호를 입력하세요. : ")) 
    if 1 =< choice =< len(characters) :
            selected_character = characters[choice - 1]
            return selected_character
    else : 
             print("숫자로 된 번호를 입력하세요.")
             return choose_character()
    
# 메인 화면
playername = input("유저 네임을 입력하세요. : ")
print("------------------------------------------")
show_character()
selected_character = choose_character()

total_stat = (
    selected_character["attack"]
    + selected_character["defense"]
    + selected_character["healing"]
    + selected_character["magic"]
)

print(f"환영합니다, {playername} 님. 아래 캐릭터로 플레이하시겠습니까?")
print(f"캐릭터: {selected_character['name']}")
print(f"공격력: {selected_character['attack']}")
print(f"방어력: {selected_character['defense']}")
print(f"치유력: {selected_character['healing']}")
print(f"마법력: {selected_character['magic']}")
print(f"총 능력치: {total_stat}")