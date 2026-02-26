

def introA():
     print("⚔︎ Treasure Quest ⚔︎\n")
     print("You are a treasure hunter who is on a quest to find hidden treasures left by four ancient kings, its" 
     "been hidden for centeries and no one has been able to find it, but you wont give up! The only clue the ancient kings" 
     "left behind was a stone tablet with different symbols on it, you remember seeing these symbols on your grand mothers" 
     "vase that she never let you touch. One day, while she was out getting groceries to make cookies, you decided to climb" 
     "on top of the counter to get the vase down, you grabbed the vase and carefully climb down, you inspect the vase and the" 
     "four symbols on it, you look closer at the small writing underneath each symbol, they read: North (Treasure of Winter)," 
     "East(Treasure of autumn), South(Treasure of spring) and west (treasure of summer), these are directions! You put the" 
     "vase back then decide to set out on your quest to find the hidden treasures\n")
    
print("\nType in the number to the choice you want to make.\n")

chosen_direction = input("What direction should you go first?\n"
                         "1. North (Treasure of Winter)\n"
                         "2. East  (Treasure of Autumn)\n"
                         "3. South (Treasure of Spring)\n"
                         "4. West  (Treasure of Summer)\n")

if chosen_direction == "1":
               print("You set sail to the North!\n")
               from NorthScene import north
               north()
if chosen_direction == "2":
               print("You set sail to the East!\n")
               from EastScene import east
               east()
elif chosen_direction == "3":
                print("You set sail to the South!\n")
                from SouthScene import south
                south()
elif chosen_direction == "4":
                print("You set sail to the West!\n")
                from WestScene import west
                west()
else:
  print("Invalid choice. Please try again.")
chosen_direction

