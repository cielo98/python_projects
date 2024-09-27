class Characters :
    def __init__(self, name, weapon, attack, defense, magic) :
        self.name = name
        self.weapon = weapon
        self.attack = attack
        self.defense = defense
        self.magic = magic

class Human(Characters) :
    pass

class Wizard(Characters) :
    pass

class Elf(Characters) :
    pass

class Dwarf(Characters) :
    pass

class Hobbit(Characters) :
    pass

class Order :
    def __init__(self) :
        self.fellowship = []
        self.fellowstats = 0
    
    def add_fellows(self, character) :
        self.fellowship.append(character)

    def show_fellows(self) :
        self.fellowstats = 0
        print("아래와 같이 원정대를 구성합니다.")
        for character in self.fellowship :
            stats = character.attack + character.defense + character.magic
            self.fellowstats = self.fellowstats + stats
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("--------------------------------")
        print(f"총합 능력치 : {self.fellowstats}")

class CharactersMenu :
    def __init__(self) :
        self.humans = {
            "Aragorn" : Human("Aragorn", "Longsword", 90, 90, 0), 
            "Boromir" : Human("Boromir", "Longsword", 80, 70, 0),
            "Faramir" : Human("Faramir", "Dagger", 80, 70, 0)
            }
        self.wizards = {
            "Gandalf" : Wizard("Gandalf", "Staff", 95, 90, 95),
            "Radaghast" : Wizard("Radaghast", "Staff", 80, 80, 90),
        }
        self.elves = {
            "Legolas" : Elf("Legolas", "Bow", 90, 90, 30),
            "Elrond" : Elf("Elrond", "Elven Sword", 95, 95, 50),
            "Arwen" : Elf("Arwen", "Dagger", 70, 70, 50)
        }
        self.dwarves = {
            "Gimli" : Dwarf("Gimli", "Hammer", 85, 90, 0),
        }
        self.hobbits = {
            "Frodo" : Hobbit("Frodo", "Ring", 50, 50, 0),
            "Samwise" : Hobbit("Samwise", "Dagger", 60, 60, 0),
            "Merry" : Hobbit("Merry", "Stick", 40, 40, 0),
            "Pippin" : Hobbit("Pippin", "Stick", 40, 40, 0),
        }

    def select_human(self, order) :
        for character in self.humans.values() :
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("----------------------------------")
        character_name = input("원하는 인간 캐릭터의 이름을 입력해주세요. : ")
        if character_name in self.humans :
            order.add_fellows(self.humans[character_name])
    
    def select_wizard(self, order) :
        for character in self.wizards.values() :
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("----------------------------------")
        character_name = input("원하는 마법사 캐릭터의 이름을 입력해주세요. : ")
        if character_name in self.wizards :
            order.add_fellows(self.wizards[character_name])

    def select_elf(self, order) :
        for character in self.elves.values() :
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("----------------------------------")
        character_name = input("원하는 엘프 캐릭터의 이름을 입력해주세요. : ")
        if character_name in self.elves :
            order.add_fellows(self.elves[character_name])

    def select_dwarf(self, order) :
        for character in self.dwarves.values() :
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("----------------------------------")
        character_name = input("원하는 드워프 캐릭터의 이름을 입력해주세요. : ")
        if character_name in self.dwarves :
            order.add_fellows(self.dwarves[character_name])

    def select_hobbit(self, order) :
        for character in self.hobbits.values() :
            print(f"캐릭터 : {character.name}")
            print(f"무기 : {character.weapon}")
            print(f"공격력 : {character.attack}")
            print(f"방어력 : {character.defense}")
            print(f"마법력 : {character.magic}")
            print("----------------------------------")
        character_name = input("원하는 호빗 캐릭터의 이름을 입력해주세요. : ")
        if character_name in self.hobbits :
            order.add_fellows(self.hobbits[character_name])

def main() :
    menu = CharactersMenu()
    order = Order()

    def greet() :
        my_name = input("플레이하실 이름을 입력해주세요. : ")
        print(f"안녕하세요, {my_name} 님.")
        print("<Lord of the Rings : Rebirth of the Fellowship>에 오신 것을 환영합니다.")
        print("새로운 원정대를 구성해봅시다.")
    
    greet()
    menu.select_human(order)
    menu.select_wizard(order)
    menu.select_elf(order)
    menu.select_dwarf(order)
    menu.select_hobbit(order)
    order.show_fellows()
main()
    

    