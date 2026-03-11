import sys

import StateCode

inventory = []


def _check_game_over():
    """Exit the game if the player has no lives remaining."""
    if StateCode.Game_over(StateCode.Lives):
        sys.exit()


def west():
    """Entry point for the West scene."""

    print(
        "You decide that your final adventure will be the western island, located directly west of your home. After days of "
        "sailing you reach the island. You dock your ship and step onto the sandy desert. You see nothing but sand dunes and "
        "cacti as far as the eye can see. The sun is blazing hot, and you feel thirsty just by looking at the dry desert. "
        "You scan the desert for any signs of life and spot a rocky formation in the distance. You decide to head toward it, "
        "hoping to find some shade from the scorching sun. When you get there, you find a large mesa with a few desert trees "
        "and plants around it. You take shelter underneath one of the trees. You spot a group of travelers riding camels in the "
        "distance. You walk toward them, hoping they can help you. They see you and stop their camels. Luckily, you speak a bit "
        "of their language from previous travels. You explain your quest, and they say they can help — but you must give them "
        "something in return. What do you give them?\n"
    )

    while True:
        choice = input(
            "35. Gold from previous treasures\n"
            "36. Your compass\n"
            "37. Your weapons\n"
        ).strip()

        if choice == "35":
            gold_path()
            break
        elif choice == "36":
            compass_path()
            break
        elif choice == "37":
            weapons_path()
            break
        else:
            print("Invalid choice. Please try again.\n")


def gold_path():
    print(
        "You reach inside your backpack and hand them the gold from previous adventures. They nod in agreement and "
        "invite you to ride on one of their camels. You hop on and they take you to an ancient temple. They tell you it is "
        "filled with traps and puzzles and no one has ever dared to step inside. You thank them, say goodbye, and step into "
        "the temple. The door closes behind you. Inside the temple is a stone with ancient words written on it. It reads, "
        "'In the heat I stand both day and night, yet I never sweat. Though the sun is bright, I point the way with shadows long—"
        "guess my name and you prove strong.' You take a minute to process the question, then come up with the answer.\n"
    )

    while True:
        choice = input(
            "38. A camel\n"
            "39. A desert well\n"
            "40. A sundial\n"
        ).strip()

        if choice == "38":
            camel_path()
            break
        elif choice == "39":
            desertwell_path()
            break
        elif choice == "40":
            sundial_path()
            break
        else:
            print("Invalid choice. Please try again.\n")


def camel_path():
    print(
        "Suddenly, a bunch of camels come out of a compartment and attack you. You are injured, but luckily you brought "
        "some weapons with you. You fight them off, and they run into a secret room which closes behind them.\n"
    )

    StateCode.Health -= 25
    print("You have " + str(StateCode.Health) + " health left.\n")

    sundial_path()


def desertwell_path():
    print(
        "Suddenly, the temple starts filling with water. You try to break the doors to get out, but they are too strong and thick. "
        "You drown.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    gold_path()


def sundial_path():
    print(
        "A secret door opens. You enter and are met with a straight path leading directly to another door. You feel suspicious "
        "of this. Do you walk straight to the door, or investigate first?\n"
    )

    while True:
        choice = input(
            "41. Walk straight to the door\n"
            "42. Investigate\n"
        ).strip()

        if choice == "41":
            dumb_path()
            break
        elif choice == "42":
            smart_path()
            break
        else:
            print("Invalid choice. Please try again.\n")


def dumb_path():
    print(
        "You decide there would be no harm in walking straight to the door. You do so while thinking of what could be in that "
        "treasure chest. Mid-thought, you trip and fall over something—it’s a trip-wire. The door on the other side closes, "
        "and lava starts pouring into the room. You die in the pool of lava.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    smart_path()


def smart_path():
    print(
        "You are wary of the suspiciously empty walkway. You thoroughly investigate the room and find a trip-wire. "
        "You carefully walk over it and reach the other side. You wonder what would have happened if you hadn't investigated "
        "the room first. When you get to the other end, the door opens. You step inside another room. This time you see another "
        "stone with ancient writing. As you walk closer, it says: 'If you can pass this test, you will be granted what you most desire. "
        "When the door with no hinges finally opens, what is the traveler said to discover?'\n"
    )

    while True:
        choice = input(
            "43. The shell\n"
            "44. The egg\n"
            "45. The yolk\n"
        ).strip()

        if choice == "43":
            shell_path()
            break
        elif choice == "44":
            egg_path()
            break
        elif choice == "45":
            yolk_path()
            break
        else:
            print("Invalid choice. Please try again.\n")


def shell_path():
    print(
        "Suddenly treasure chests start falling from above. You manage to dodge some, but one lands on your leg. The pain is intense, "
        "but you carry on.\n"
    )

    StateCode.Health -= 25
    print("You have " + str(StateCode.Health) + " health left.\n")

    yolk_path()


def egg_path():
    print(
        "Suddenly huge cannons lift up and treasure chests filled with treasure shoot out and come flying towards you. "
        "You are unable to dodge them and are hit by several. You do not survive.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    smart_path()


def yolk_path():
    print(
        "Suddenly the wall behind the stone opens, revealing a treasure chest placed on a mount of gold and gems! "
        "Inside you see gold, gems, a sword, and the red gemstone!\n"
    )

    inventory.append("Sword")
    inventory.append("Red gemstone")


def compass_path():
    print(
        "Without thinking, you hand the group your compass. They look at each other, then laugh. You ask why, and they tell "
        "you to go into the cave on top of the 'table mountain' beside you. You exchange goodbyes and head toward the mountain. "
        "With great struggle, you manage to climb to the top. You reach the cave mentioned by the travelers and go inside. "
        "Once inside, a hungry mountain lion leaps and attacks you. You can't react fast enough to grab your weapons. You are "
        "eaten by the mountain lion.\n"
    )

    print("You have failed your quest.\n")


def weapons_path():
    print(
        "You reach inside your backpack and hand them all your weapons. They nod excitedly in agreement and invite you to ride "
        "on one of their camels. You hop on and they take you to an ancient temple. They tell you it's filled with traps and puzzles "
        "and no one has ever dared to step inside. You thank them and step inside the temple. The door closes behind you. "
        "Inside the temple is a stone with ancient words written on it. It reads, 'In the heat I stand both day and night, yet I never sweat. "
        "Though the sun is bright, I point the way with shadows long—guess my name and you prove strong.' You take a minute to think "
        "and then come up with the answer.\n"
    )

    gold_path()





