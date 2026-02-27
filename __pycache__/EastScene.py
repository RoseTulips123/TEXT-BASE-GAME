import StateCode
inventory = []

def east():
         print("Upon arriving at the island directly East of your home, you immediately see beautiful mountainous terrain") 
         print("and colorful trees, you see two paths ahead of you, one leading into a beautiful forest, and one leading")
         print("towards a treehouse village built into the mountainside, which path do you take?\n") 

choice_path3 = input("Which path do you take?\n"
                     "12. Beautiful forest\n"
                     "13 Treehouse village\n")

def forest_path():  
         print("You enter the forest, the trees are tall and the leaves are a beautiful array of reds, oranges, and yellows, as you")
         print("walk deeper into the forest you see a clearing ahead, in the middle of the clearing you see an injured rare fox")
         print("thats colored gold and red, do you help the fox, ignore it or take its fur for profit\n")


choicepath4 = input("14. Help the fox" \
                    "15. Ignore the fox" \
                    "16. Take its fur for profit\n")
          
if choicepath4 == "14":
         print("You carefully approach the injured fox, it looks at you with pleading eyes, you reach into you bag to find some")
         print("bandages and medicine, luckily you packed extra supplies for your journey, you carefully bandage the fox's wounds")
         print("and give it some water, after a few minutes the fox gets up and  hands you what it looks like a small map, the")
         print("fox then runs off into the forest, you look at the map and see that it shows an X marking to a spot deeper in")
         print("the forest, you decide to follow the map, after a few hours of searching you reach the spot marked on the map, you")
         print("finnaly find the spot, you start digging and find a chest buried in the ground, you open the chest and find gold, jewels,")
         print("a cape, and a yellow gemstone!\n")
         inventory.append("Cape")
         inventory.append("Yellow gemstone")
         print("Congratulations! You have found the Treasure of Autumn!\n")
        

if choicepath4 == "15":
         print("You decide to ignore the fox and continue on your way, as you walk deeper into the forest, suddenly an tribe of")
         print("hostile natives ambush you, they overpower you and take all your supplies, leaving you stranded in the forest with")
         print("no food or water, after days of wandering you give up hope and succumb to starvation.\n")
         StateCode.Lives -= 1
         print("You have " + str(StateCode.Lives) + " lives left.\n")
         choicepath4()
         

if choicepath4 == "16":
         print("You see the foxes fur would be worth a ton of gold, you quickly grab your knife and skin the fox, you put the fur")
         print("in your bag and turn back towards the path, as you walk back, a gigantic tree falls beside you, and before you")
         print("could run, it crushes you.\n")
         StateCode.Lives -= 1
         print("You have " + str(StateCode.Lives) + " lives left.\n")
         choicepath4()

def treehouse_path():  
         print("You decide that going to the treehouse village might have a better chance of finding the treasure, you make your")
         print("way towards the village, as you get closer you see that the village is bustling with activity, people are going")
         print("about their daily lives, you approach one of the villagers, they look at you like they've seen an alien, how ")
         print("should you talk to them?\n")
         choice = input("17. Try to communicate with gestures\n"  
                       "18. Attempt to speak their language\n" 
                       "19. Offer them a gift from your homeland\n")
       
         if choice ==   "17":
                 return communication_path()
         elif choice == "18":
              return language_path()
         elif choice == "19":
              return gift_path()
         else:
              print("Invalid choice, please try again.")
              treehouse_path()

def communication_path():
         print("You try to communicate with gestures, the villager looks confused but seems to understand you want to say, they"
               "Motion for you to follow them, they lead you to the village elder, the elder listens to your story and decides to"
               "help you, they give you a map with an X marking a spot deep in the nearby forest, you follow the map and after"
               "a few hours of searching you reach the spot marked on the map, you start digging and find a chest buried in the"
               "ground, inside you find gold, jewels, a cape, and a red gemstone!")
         print("Congratulations! You have found the Treasure of Autumn!\n")
         inventory.append("Cape")
         inventory.append("Yellow gemstone")
         print("What direction should you go to next?")
         directionpath3A()

def language_path():
         print("You attempt to speak their language, but you only manage to butcher a few words, the villager looks at you angrily\n"
               "and calls for others, soon you are surrounded by hostile villagers, they attack and kidnap you, you are held\n" 
               "captive for weeks before you manage to escape, but you are left with nothing but the clothes on your back, you\n"
               "eventually make your way back home dehydrated, starved, exhausted, and empty handed, you give up.\n")
StateCode.Lives -= 1
print("You have " + str(StateCode.Lives) + " lives left.\n")
choice_path3()

def gift_path():
         print("You offer the villager a gift from your homeland, they look at the gift curiously, after examining it they smile\n"
              "and motion for you to follow them, they lead you to their hut, they give you food and water, you explain your\n"
              "quest to them through gestures, they take you to the village elder, the villager explains your story to the\n"
              "elder, the elder decides to help you, they give you a map with an \"x\" marking a spot deep in the nearby forest,\n"
              "you follow the map and after a few hours of searching you reach the spot marked on the map, you start digging and\n"
              "find a chest buried in the ground, inside you find gold, jewels, a cape, and a red gemstone!\n")
         print("Congratulations! You have found the Treasure of Autumn!\n")
         inventory.append("Cape")
         inventory.append("Yellow gemstone")

east()

directionpath3A = input("What direction should you go to next? \n"
                        "20. South (Treasure of Spring)\n"
                        "21. West  (Treasure of Summer)\n")
       
if directionpath3A == "20":
        print("You set sail to the South!\n")
        from SouthScene import south
        south()        
elif directionpath3A == "21": 
        print ("You sail to the West!")  
        from WestScene import west
        west()       
else:
        print("Invalid choice. Please try again.")
        directionpath3A()