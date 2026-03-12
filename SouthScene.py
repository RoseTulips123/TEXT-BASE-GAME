import sys

import StateCode

inventory = []


def _check_game_over():
    if StateCode.Game_over(StateCode.Lives):
        sys.exit()
    elif StateCode.Health <= 0:
        sys.exit()


def south():
    print(
        "You decide that your next adventure will be the southern island, located directly south of your home. After a few "
        "days of sailing you reach the island, you dock your ship and step onto the beautiful, sandy beach. You see palm trees "
        "swaying in the warm breeze, beautiful lush greenery and exotic plants and animals you've never seen before — it's like "
        "a paradise. You explore the island and manage to build a temporary shelter of palm leaves and wood. As night creeps "
        "over the island, you go to sleep, but you are then woken up by weird loud noises outside your shelter. Do you investigate "
        "the noises, or stay in your shelter?\n"
    )

    while True:
        choice = input(
            "1. \nInvestigate the noises\n"
            "2. Stay in your shelter\n"
        ).strip()

        if choice ==   "1":
            investigate_path()
            break
        elif choice == "2":
            stay_path()
            break
        else:
            print("Invalid choice. Please try again.\n")
            south()

def investigate_path():
    print(
        "Curiosity gets the better of you and you decide to investigate the noises. You muster up the courage and step "
        "outside your shelter. As you do, you are greeted by unwelcome black tall creatures with glowing purple eyes. You are "
        "stuck in a trance-like state, unable to move, and you can only watch as the figures' purple eyes get closer and closer, "
        "until you can't see anymore.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    south()


def stay_path():
    print(
        "You decide to stay in your shelter, hoping the noises will go away. They eventually move farther away until they are gone. "
        "You cautiously look outside your shelter and see nothing but the night and stars. You go back to sleep and awake to a "
        "beautiful sunny morning. You decide to explore more of the island.\n"
    )

    print(
        "As you walk deeper into the island, you name some of the exotic plants and animals and jot them down in your journal. "
        "After a few hours of exploring you reach a beautiful waterfall with a stream flowing from it. You drink some of the "
        "water and feel refreshed. You see a cave entrance behind the waterfall.\n"
    )

    while True:
        choice = input(
            "1. \nEnter the cave\n"
            "2. Rest by the waterfall\n"
        ).strip()

        if choice ==   "1":
            cave_path()
            break
        elif choice == "2":
            rest_path()
            break
        else:
            print("Invalid choice. Please try again.\n")
            stay_path()

def cave_path():
    print(
        "You have heard stories of hidden treasures in caves behind waterfalls, so you decide to enter the cave. As you step "
        "inside, bats fly past you. The cave is dark and damp. You walk deeper into the cave, and after a few minutes you reach "
        "a large chamber with walls covered in colorful, glowing crystals. In the center you see a large glowing crystal with "
        "a treasure map inside it. You brought some tools with you for your journey — which tool should you use to break the crystal?"
    )

    while True:
        choice = input(
            "1. \nHammer\n"
            "2. Chisel\n"
            "3. Pickaxe\n"
        ).strip()

        if choice ==   "1":
            hammer_path()
            continue
        elif choice == "2":
            chisel_path()
            break
        elif choice == "3":
            pickaxe_path()
            continue
        else:
            print("Invalid choice. Please try again.\n")
            cave_path()

def rest_path():
    print(
        "Exhausted from your exploration and having finally had a drink of the freshest water in your life, you lay down "
        "in a bed of flowers and gaze up into the beautiful sky, full of colorful birds soaring through the air. You close "
        "your eyes and fall asleep. You are awakened by a loud bird-like sound behind you. You turn around and see a huge bird "
        "in front of you, and in its beak is your backpack! You try to snatch it, but it flies off. You quickly run after it, and it "
        "leads you into uncharted territory you've never discovered. You keep running, but then you feel yourself trip. Before "
        "you can catch yourself, you fall off a very tall slope. You hit the ground with a hard and brutal thud. You are now "
        "very injured.\n"
    )

    StateCode.Health -= 50
    print("You have " + str(StateCode.Health) + " health left.\n")
    _check_game_over()

    cave_path()


def hammer_path():
    print(
        "You use the hammer to try and break the crystal. You strike it with all your might, and it shatters into a million "
        "pieces. The shards fly everywhere, and one sharp shard stabs you in the chest. You fall to the ground; you are in "
        "much pain, but you must go on.\n"
    )

    StateCode.Health -= 45
    print("You have " + str(StateCode.Health) + " health left.\n")
    _check_game_over()

    cave_path()


def pickaxe_path():
    print(
        "You use the pickaxe to try and break the crystal. You strike it a little too hard, and the crystal breaks in half, "
        "and so does the map inside. You are left with nothing but shattered glass and torn paper.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    cave_path()


def chisel_path():
    print(
        "You carefully use the chisel to break the crystal. After a few hours of careful work, you manage to break the crystal "
        "without damaging the map inside. You unroll the map and see that it shows different landmarks on the island, with one "
        "landmark marked with an X near the center of the island. You follow the map. After an hour of walking, you reach the "
        "spot marked on the map. When you get there, you see an entrance to an underground tunnel. You enter the tunnel and find "
        "what looks like a maze! You navigate through the maze using the directions on the back of the map. Eventually you reach "
        "a room at the end of the maze with three paths leading left, middle, and right. Which path do you take?\n"
    )

    while True:
        choice = input(
            "1. \nLeft path\n"
            "2. Middle path\n"
            "3. Right path\n"
        ).strip()

        if choice ==   "1":
            left_path()
            continue
        elif choice == "2":
            middle_path()
            continue
        elif choice == "3":
            right_path()
            break
        else:
            print("Invalid choice. Please try again.\n")
            chisel_path()

def left_path():
    print(
        "You take the left path. After a few minutes of walking you reach a dead end. As you turn around to go back, you trigger "
        "a hidden trap. A poison arrow hits you in the shoulder, but you manage to pull it out and lose only a little health.\n"
    )

    StateCode.Health -= 15
    print("You have " + str(StateCode.Health) + " health left.\n")
    _check_game_over()

    chisel_path()


def middle_path():
    print(
        "You take the middle path. It seems most convincing. You walk for a few minutes and at the end of the path you see a lever on "
        "the wall. Do you pull the lever or go back?\n"
    )

    while True:
        choice = input(
            "\n1. Pull the lever\n"
            "2. Go back\n"
        ).strip()

        if choice ==   "1":
            lever_path()
            break
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please try again.\n")
            middle_path()

def lever_path():
    print(
        "You pull the lever. You hear a rumbling sound, the ceiling opens up, then a large anvil falls from above and crushes you instantly.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    chisel_path()


def right_path():
    print(
        "You take the right path. The tunnel is long and narrow. After a while, you hear echoes of flowing water ahead. You walk faster "
        "and soon reach a large underground waterfall with a sparkling pool below. You see a chest at the base of the waterfall. "
        "You swim to the chest and open it. Inside you find gold, jewels, armor, and a pink gemstone!\n"
    )

    inventory.append("Armor")
    StateCode.add_gem("Pink gemstone")
    StateCode.checkWinOrContinue()

    print("Congratulations! You have found the Treasure of Spring!\n")

    from StateCode import checkWinOrContinue

    checkWinOrContinue()

