def display_menu():
    print("=== Pizza Menu ===")
    print("1. Margherita - $10")
    print("2. Pepperoni - $12")
    print("3. BBQ Chicken - $15")
    print("4. Veggie - $8")

def select_pizza():
    choice = int(input("Choose your pizza (1-4): "))
    
    if choice == 1:
        return "Margherita", 10
    elif choice == 2:
        return "Pepperoni", 12
    elif choice == 3:
        return "BBQ Chicken", 15
    elif choice == 4:
        return "Veggie", 8
    else:
        print("Invalid choice. Please select again.")
        return select_pizza()

def main():
    display_menu()
    pizza, price = select_pizza()
    print(f"You have selected {pizza}. Total price is ${price}.")

    