def display_characters():
    print("1. Link")
    print("2. Zelda")
    print("3. Revali")
    print("4. Mipha")
    print("5. Daruk")
    print("6. Urbosa")

player_name = input("유저네임을 입력하세요. : ")
def character_stats():
    choice = int(input("원하는 캐릭터의 번호를 입력하세요. : "))

    if choice == 1:
        return "Link", 90, 80, 15, 0
    elif choice == 2:
        return "Zelda", 30, 80, 15, 90
    elif choice == 3:
        return "Revali", 80, 70, 10, 0
    elif choice == 4:
        return "Mipha", 70, 60, 90, 40
    elif choice == 5: 
        return "Daruk", 80, 80, 15, 0
    elif choice == 6:
        return "Urbosa", 90, 70, 10, 50
    else: 
        return(character_stats())

print("-------------------------------------------------")
name, attack, defense, healing, magic = character_stats()
total_stat = attack + defense + healing + magic
print(f"환영합니다, {player_name} 님. 아래 캐릭터로 플레이하시겠습니까?")
print(f"캐릭터: {name}", f"공격력: {attack}", f"방어력: {defense}", f"치유력: {healing}", f"마법력: {magic}", f"총 능력치: {total_stat}", sep = "\n")


# 수정본

# 캐릭터 정의
characters = [
    {"name": "Link", "attack": 90, "defense": 80, "healing": 15, "magic": 0},
    {"name": "Zelda", "attack": 30, "defense": 80, "healing": 15, "magic": 90},
    {"name": "Revali", "attack": 80, "defense": 70, "healing": 10, "magic": 0},
    {"name": "Mipha", "attack": 70, "defense": 60, "healing": 90, "magic": 40},
    {"name": "Daruk", "attack": 80, "defense": 80, "healing": 15, "magic": 0},
    {"name": "Urbosa", "attack": 90, "defense": 70, "healing": 10, "magic": 50},
]

# 캐릭터 출력
for i in enumerate(characters, start=1) : 
    print(i)





