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


a = 1
while a <= 100: 
    print(a)
    a = a + 1

a = int(input("숫자 입력" ))
b = int(input("다른 숫자 입력" ))
print("두 수의 합은" + str(a + b) + "임")
print(f"두 수의 합은 {a + b}임")

c = input("아무 말이나 써라 : ")
print(len(c))

d = int(input("숫자 써라: "))
is_even = d%2==0
print("입력한 수는 짝수임?" + str(is_even))

score_1 = float(input("과목 1"))
score_2 = float(input("과목2"))
score_3 = float(input("과목3"))
average = (score_1 + score_2 + score_3)/3
print("세 과목의 평균은 %.1f입니다." %average)
print(f"세 과목의 평균은 {average: .1f}입니다.")