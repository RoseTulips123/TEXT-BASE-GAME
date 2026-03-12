import sys

import StateCode

inventory = []

def _check_game_over():
    if StateCode.Game_over(StateCode.Lives):
        sys.exit()

def east():
    print(
    "Upon arriving at the island directly East of your home, you immediately see beautiful mountainous " \
    "terrain and colorful trees. You see two paths ahead of you: one leading into a beautiful forest, and one " \
    "leading towards a treehouse village built into the mountainside.\n"
    )

    while True:
        choice = input(
            "\nWhich path do you take?\n"
            "1. Beautiful forest\n"
            "2. Treehouse village\n"
        ).strip()

        if choice ==   "1":
            forest_path()
            break
        elif choice == "2":
            treehouse_path()
            break
        else:
            print("Invalid choice. Please try again.\n")
            east()

def forest_path():
    print(
    "You enter the forest; the trees are tall and the leaves are a beautiful array of reds, oranges, and " \
    "yellows. As you walk deeper into the forest you see a clearing ahead, and in the middle of the clearing you " \
    "see an injured rare fox that's colored gold and red. Do you help the fox, ignore it, or take its fur for profit?\n"
    )

    while True:
        choice = input(
            "\n1. Help the fox\n"
            "2. Ignore the fox\n"
            "3. Take its fur for profit\n"
        ).strip()

        if choice ==   "1":
            help_fox()
            break
        elif choice == "2":
            ignore_fox()
            break
        elif choice == "3":
            take_fur()
            break
        else:
            print("Invalid choice, Please try again.\n")
            forest_path()

def help_fox():
    print(
          "You carefully approach the injured fox; it looks at you with pleading eyes. You reach into your bag to find some"
          "bandages and medicine. Luckily you packed extra supplies for your journey, so you carefully bandage the fox's wounds"
          "and give it some water. After a few minutes the fox gets up and hands you what looks like a small map."
          "The fox then runs off into the forest. You look at the map and see that it shows an X marking a spot deeper in"
          "the forest. You decide to follow the map, and after a few hours of searching you reach the spot marked on the map."
          "You dig and find a chest buried in the ground. Inside you find gold, jewels, a cape, and a green gemstone!\n"
    )

    inventory.append("Cape")
    StateCode.add_gem("Green gemstone")
    StateCode.checkWinOrContinue()

    print("Congratulations! You have found the Treasure of Autumn!\n")
    


def ignore_fox():
    print(
          "You decide to ignore the fox and continue on your way. As you walk deeper into the forest, suddenly a tribe of"
          "hostile natives ambush you. They overpower you and take all your supplies, leaving you stranded in the forest with"
          "no food or water. After days of wandering you give up hope and succumb to starvation.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()
    
    forest_path()

    
def take_fur():
    print(
          "You see the fox's fur would be worth a ton of gold. You quickly grab your knife and skin the fox, then put the fur"
          "in your bag and turn back toward the path. As you walk back, a gigantic tree falls beside you, and before you could"
          "run it crushes you.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    forest_path()

    
def treehouse_path():
    print(
        "You decide that going to the treehouse village might have a better chance of finding the treasure. You make your"
        "way toward the village. As you get closer you see that the village is bustling with activity; people are going"
        "about their daily lives. You approach one of the villagers; they look at you like they've seen an alien. How"
        "should you talk to them?\n"
    )

    while True:
        choice = input(
            "\n1. Try to communicate with gestures\n"
            "2. Attempt to speak their language\n"
            "3. Offer them a gift from your homeland\n"
        ).strip()

        if choice == "1":
            communication_path()
            break
        elif choice == "2":
            language_path()
            break
        elif choice == "3":
            gift_path()
            break
        else:
            print("Invalid choice. Please try again.\n")
            treehouse_path()

def communication_path():
    print(
        "You try to communicate with gestures. The villager looks confused but seems to understand you want to say "
        "something, and they motion for you to follow them. They lead you to the village elder. The elder listens to your "
        "story and decides to help you. They give you a map with an X marking a spot deep in the nearby forest. "
        "You follow the map and after a few hours of searching you reach the spot marked on the map. You dig and find "
        "a chest buried in the ground. Inside you find gold, jewels, a cape, and a green gemstone!\n"
    )

    inventory.append("Cape")
    StateCode.add_gem("Green gemstone")
    StateCode.checkWinOrContinue()

    print("Congratulations! You have found the Treasure of Autumn!\n")
    
    

def language_path():
    print(
        "You attempt to speak their language, but you only manage to butcher a few words. The villagers look at you angrily\n"
        "and call for others. Soon you are surrounded by hostile villagers; they attack and kidnap you. You are held\n"
        "captive for weeks before you manage to escape, but you are left with nothing but the clothes on your back. You\n"
        "eventually make your way back home dehydrated, starved, exhausted, and empty-handed. You give up.\n"
    )

    StateCode.Lives -= 1
    print("You have " + str(StateCode.Lives) + " lives left.\n")
    _check_game_over()

    treehouse_path()


def gift_path():
    print(
        "You offer the villager a gift from your homeland. They look at the gift curiously, and after examining it they smile\n"
        "and motion for you to follow them. They lead you to their hut, give you food and water, and you explain your\n"
        "quest through gestures. They take you to the village elder, who decides to help you. The elder gives you a map with\n"
        "an 'X' marking a spot deep in the nearby forest. You follow the map and after a few hours of searching you reach the\n"
        "spot marked on the map. You dig and find a chest buried in the ground. Inside you find gold, jewels, a cape, and a\n"
        "green gemstone!\n"
    )

    inventory.append("Cape")
    StateCode.add_gem("Green gemstone")
    StateCode.checkWinOrContinue()

    print("Congratulations! You have found the Treasure of Autumn!\n")

