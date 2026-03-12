

Lives = 3
Health = 100

def State():
       global Lives
       global Health

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
       
       
# Added a function to check if player colleccted all 4 gemstones or not.

def checkWinOrContinue():
    inventory = []
    if "Blue gemstone" in inventory and "Green gemstone" in inventory and "Red gemstone" in inventory and "Pink gemstone" in inventory:
         from OutroScene import outro
         outro()

    elif "Blue gemstone" not in inventory and "Green gemstone" not in inventory and "Red gemstone" not in inventory and "Pink gemstone" not in inventory:
         from MainIntro import chosen_direction
         chosen_direction()