import sys

import StateCode


def outro():
    print("Congratulations! You found all 4 gemstones and a full set of armor! You have completed your quest.\n")
    print(
        "\"Now having found all 4 gemstones, you retire back to your homeland. On the way, you can't wait to tell everyone about your adventure, "
        "but you know your grandma will be angry that you touched her vase. Still, you are happy with the outcome you got from it. "
        "There are still some questions weighing on your mind: what are these gemstones? What do they do? Why are they directly North, West, South, and East of your home? (ETC)"
        " You guess you'll find that out in your next adventure!"
    )
    print("\nHere is your final inventory and stats:\n")
    print("Inventory:", StateCode.inventory)
    print("Lives:", StateCode.Lives)
    print("Health:", StateCode.Health)
    print("\nSee you next time!\n")
    print(" ⚔︎ Treasure Quest ⚔︎")
    
outro()

sys.exit()


