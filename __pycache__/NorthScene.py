from random import choice

import StateCode

inventory = []

def north():
 print("after days of sailing you reach an island directly North of your home, you dock your ship,"
       "cold, arctic winds hit you face, good thing you prepared for this, you walk inland and see a huge"
       "mountain in the distance, you start to make your way to the mountain as big as mount everest,"
       "after hours of hiking you reach the base of the mountain, you see a cave entrance, you brush off"
       "some snow from a fallen boulder next to it and see a blue gemstone engraved in the rock, you enter"
       "the cave, its dark and cold, you walk deeper into the cave until you see a peice of meat laying"
       "on the ground, you are very hungry from your voyage," "\n"
 )


def choice0():
  choice = input(
        "Do you eat the meat?\n"
        "5. Eat the meat\n"
        "6. Move on into the cave\n"
)
 
def Meat_scene():
        print("You go to pick up the meat, as you do a huge polar bear jumps out from the shadows and attacks you, you try")
        print("to fight it off but you end up with scratches and bruises, yet you live to see another day.\n")

        StateCode.Health -= 50
        print("You have " + str(StateCode.Health) + " health left.\n")

def ignore_scene():
        print("You ignore the meat and walk deeper into the cave, after a few minutes you see a light in the distance, you")
        print("walk towards it and find a large chamber with the floor frozen over, you see a large ice pedestal in the center")
        print("of the chamber with a chest on top of it, should you cross the frozen floor to get to the chest? Or look around")
        print("the chamber first?")

if choice == "5":
               Meat_scene()
elif choice == "6":
               ignore_scene()
else:
        print("Invalid choice. Please try again.\n")
        choice0()


choice = input(
        "7. Cross the frozen floor to the chest\n"
        "8. Look around the chamber first\n"
)

def frozenfloor_scene():
        print("You make your way across the frozen floor, as you near the pedestal you hear a cracking sound, before you can")
        print("react the ice breaks beneath you, and you fall into freezing water below, the freezing temperature of the water")
        print("gives you hypothermia and you drown.\n")

        StateCode.Lives -= 1
        print("You have " + str(StateCode.Lives) + " lives left.\n")
        ignore_scene()

def Lookaround_scene():
        print("You observe the ice closely and see that the floor is very thin in some spots, you carefully make your way across")
        print("the chamber avoiding the thin ice, you reach the pedestal and open the chest, inside you find gold, diamonds,")
        print("a sheild, and a Blue gemstone!\n")
        

        inventory.append("Sheild")
        inventory.append("Blue gemstone")
       
if choice == "7":
        frozenfloor_scene()
elif choice == "8":
              Lookaround_scene()
else:
 print("Invalid choice. Please try again.")
 ignore_scene()

print("Congratulations! You have found the Treasure of Winter!\n")


def directionpath1():
       choice = input(
               "What direction should you go to next?\n"
               "9. East (Treasure of Autumn)\n"
               "10. South (Treasure of Spring)\n"
               "11. West (Treasure of Summer)\n"
)
       
       if choice == "9":
              print("You set sail to the East!\n")
              from EastScene import east
              east()
       elif choice == "10":
              print("You set sail to the South!\n")
              from SouthScene import south
              south()
       elif choice == "11":
              print("You set sail to the West!\n")
              from WestScene import west
              west()
       else:
              print("Invalid choice. Please try again.\n")
              directionpath1()

directionpath1()
