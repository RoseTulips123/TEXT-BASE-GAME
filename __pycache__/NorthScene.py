import sys

import StateCode

inventory = []


def _check_game_over():
    """Exit the game if the player has no lives remaining."""
    if StateCode.Game_over(StateCode.Lives):
        sys.exit()


def north():
    """Entry point for the North scene."""

    print(
        "After days of sailing you reach an island directly north of your home. You dock your ship, and cold arctic "
        "winds hit your face. Good thing you prepared for this. You walk inland and see a huge mountain in the distance; "
        "after hours of hiking you reach the base of the mountain. You see a cave entrance and, after brushing snow off a "
        "fallen boulder, you notice a blue gemstone engraved in the rock. You enter the cave; it's dark and cold. You walk "
        "deeper into the cave and see a piece of meat laying on the ground. You are very hungry from your voyage.\n"
    )

    while True:
        choice = input(
            "Do you eat the meat?\n"
            "5. Eat the meat\n"
            "6. Move on into the cave\n"
        ).strip()

        if choice == "5":
            meat_scene()
            break
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.\n")

    while True:
        choice = input(
            "7. Cross the frozen floor to the chest\n"
            "8. Look around the chamber first\n"
        ).strip()

        if choice == "7":
            frozenfloor_scene()
            break
        elif choice == "8":
            lookaround_scene()
            break
        else:
            print("Invalid choice. Please try again.\n")

    print("Congratulations! You have found the Treasure of Winter!\n")
    directionpath1()


def meat_scene():
    print(
        "You go to pick up the meat, and a huge polar bear jumps out from the shadows and attacks you. You try to fight it off, "
        "but you end up with scratches and bruises. You live to see another day.\n"
    )

    StateCode.Health -= 50
    print("You have " + str(StateCode.Health) + " health left.\n")
    _check_game_over()


def frozenfloor_scene():
    print(
        "You make your way across the frozen floor. As you near the pedestal you hear a cracking sound; before you can react "
        "the ice breaks beneath you and you fall into freezing water below. The freezing temperature gives you hypothermia and "
        "you drown.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()


def lookaround_scene():
    print(
        "You observe the ice closely and see that the floor is very thin in some spots. You carefully make your way across the "
        "chamber avoiding the thin ice. You reach the pedestal and open the chest. Inside you find gold, diamonds, a shield, "
        "and a blue gemstone!\n"
    )

    inventory.append("Shield")
    inventory.append("Blue gemstone")


def directionpath1():
    while True:
        choice = input(
            "What direction should you go to next?\n"
            "9. East (Treasure of Autumn)\n"
            "10. South (Treasure of Spring)\n"
            "11. West (Treasure of Summer)\n"
        ).strip()

        if choice == "9":
            print("You set sail to the East!\n")
            from EastScene import east

            east()
            break
        elif choice == "10":
            print("You set sail to the South!\n")
            from SouthScene import south

            south()
            break
        elif choice == "11":
            print("You set sail to the West!\n")
            from WestScene import west

            west()
            break
        else:
            print("Invalid choice. Please try again.\n")
