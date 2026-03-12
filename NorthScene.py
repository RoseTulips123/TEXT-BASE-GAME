import sys

import StateCode

inventory = []

def _check_game_over():
    if StateCode.Game_over(StateCode.Lives):
        sys.exit()
    elif StateCode.Health <= 0:
        sys.exit()


def north():
    print(
        "\nAfter days of sailing you reach an island directly north of your home. You dock your ship, and cold arctic "
        " winds hit your face. Good thing you prepared for this. You walk inland and see a huge mountain in the distance; "
        " after hours of hiking you reach the base of the mountain. You see a cave entrance and, after brushing snow off a "
        " fallen boulder, you notice a blue gemstone engraved in the rock. You enter the cave; it's dark and cold. You walk "
        " deeper into the cave and see a piece of meat laying on the ground. You are very hungry from your voyage.\n"
    )

    while True:
        choice = input(
            "\nDo you eat the meat?\n"
            "1. Eat the meat\n"
            "2. Move on into the cave\n"
        ).strip()

        if choice == "1":
            meat_scene()
            
            break
        elif choice == "2":
            ignore_scene()
            break
        else:
            print("Invalid choice. Please try again.\n")
            north()
    while True:
        choice = input(
            "1. \nCross the frozen floor to the chest\n"
            "2. Look around the chamber first\n"
        ).strip()

        if choice == "1":
            frozenfloor_scene()
            break
        elif choice == "2":
            lookaround_scene()
            break
        else:
            print("Invalid choice. Please try again.\n")


def meat_scene():
    print(
        "You go to pick up the meat, and a huge polar bear jumps out from the shadows and attacks you. You try to fight it off, "
        " but you end up with scratches and bruises. You live to see another day. You Stand up and walk deeper into the cave. You walk inside"
        " a huge room and see a large ice pedestal in the center of the chamber with a chest on top of it, should you cross the frozen floor"
        " to get to the chest? Or look around the chamber first?\n"
    )
 
    StateCode.Health -= 50
    print("You have " + str(StateCode.Health) + " health left.\n")
    _check_game_over()

    north()


def ignore_scene():
        print(
            "You ignore the meat and walk deeper into the cave, after a few minutes you see a light in the distance, you"
              " walk towards it and find a large chamber with the floor frozen over, you see a large ice pedestal in the center"
              " of the chamber with a chest on top of it, should you cross the frozen floor to get to the chest? Or look around"
              " the chamber first?"
    )
    
def frozenfloor_scene():
    print(
        "You make your way across the frozen floor. As you near the pedestal you hear a cracking sound; before you can react "
        " the ice breaks beneath you and you fall into freezing water below. The freezing temperature gives you hypothermia and "
        " you drown.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()


def lookaround_scene():
    print(
        "You observe the ice closely and see that the floor is very thin in some spots. You carefully make your way across the "
        " chamber avoiding the thin ice. You reach the pedestal and open the chest. Inside you find gold, diamonds, a shield, "
        " and a blue gemstone!\n"
    )

    inventory.append("Shield")
    StateCode.add_gem("Blue gemstone")
    StateCode.checkWinOrContinue()



