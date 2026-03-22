Lives = 3
Health = 100
inventory = []  # keep collected gemstones between calls

def State():
    global Lives, Health

def Game_over(Current_lives):
    if Current_lives == 0:
        print("You have failed your quest.\n")
        return True
    return False

def Lose_HP(Current_HP, Current_Lives, Amount, Max_HP):
    Current_HP -= Amount
    if Current_HP <= 0:
        Current_Lives -= 1
        Current_HP = Max_HP
        print("You lost a Life! Please be more careful next time.\n")

    if Game_over(Current_Lives):
        return Current_HP, Current_Lives, True

    print("HP:", Current_HP, "Lives:", Current_Lives, "\n")
    return Current_HP, Current_Lives, False

# Inventory management functions
def add_gem(gem_name: str):
    normalized = gem_name.strip().lower()
    if normalized not in inventory:
        inventory.append(normalized)

def has_all_gems():
    required = {"blue gemstone", "green gemstone", "red gemstone", "pink gemstone"}
    return required.issubset(set(inventory))



# Check if player has won or not
def checkWinOrContinue():
    if has_all_gems():
        from OutroScene import outro
        outro()
        

    while True:
        choice = input(
            "What direction should you go?\n"
            "1. North (Treasure of Winter)\n"
            "2. East  (Treasure of Autumn)\n"
            "3. South (Treasure of Spring)\n"
            "4. West  (Treasure of Summer)\n\n"
        ).strip()

        if choice == "1":
            print("You set sail to the North!\n")
            from NorthScene import north
            north()
            break
        elif choice == "2":
            print("You set sail to the East!\n")
            from EastScene import east
            east()
            break
        elif choice == "3":
            print("You set sail to the South!\n")
            from SouthScene import south
            south()
            break
        elif choice == "4":
            print("You set sail to the West!\n")
            from WestScene import west
            west()
            break
        else:
            print("Invalid choice. Please try again.\n")
