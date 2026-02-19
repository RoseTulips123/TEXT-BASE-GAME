inventory = []

def west_sceneA():      
 print("You decide that your final adventure will be the western island (Or whatever the user ends on), located directly west of your home," 
 " after days of sailing you reach the island, you dock your ship and step onto the sandy desert, you see nothing but sand dunes and cacti" 
 " as far as the eye can see, the sun is blazing hot, you feel thirsty by just looking at the dry desert, you scan the desert for any signs of life," 
 " you see a rocky formation in the distance, you decide to head towards it, hoping to find some shade from the scorching sun, you make your way" 
 " towards the rocky formation, When you get there, you see its a large mesa, with a few desert trees and plants, around it, you take shelter" 
 " underneath one of the trees, you spot a group of arabs riding camels in the distance, you walk towards them, hoping they can help you, they" 
 " see you and stop their camels, you luckily speak a good amount of their language from your previous travels, you explain your quest to them," 
 " they say that they can help you but first you must give them something in return, what do you give them?\n")

choice = input("35. Gold from previous treasures\n"
               "36. Your compass\n"
               "3. Your weapons\n")

def choice_path11():
       if choice == "35":
              return gold_path()
       elif choice == "36":
              return compass_path()
       elif choice == "37":
              return weapons_path()
       else:
              print("Invalid choice. Please try again.\n")
              choice_path11()

def gold_path():
       print("You reach inside your backpack and hand them the gold from previous adventures, they nod in agreement and invite you to ride on one of" 
       " their camels, you hop on one, and they take you to an anceint temple, they tell you its filled with various traps and puzzles and no one has" 
       " ever dared to step inside. you thanked them and said goodbye and stepped inside the temple, the door closes from behind you, inside the temple"
       " is a stone with anceint arab words written on it, it reads, *In the heat I stand both day and night, yet I never sweat, though the sun is bright," 
       " I point the way with shadows long~ guess my name and you prove strong*, you take a minute to process the question, then come up with the anwser~\n")

print(" 38. A camel\n"
      " 39. A desert well\n"
      " 40. A sundial\n")

def choice_path12():
       if choice == "38":
              return camel_path()
       elif choice == "39":
              return desertwell_path()
       elif choice == "40":
              return sundial_path()
       else:
              print("Invalid choice. Please try again.\n")
              choice_path12()

def camel_path():
      print("Suddenly, a bunch of camels came out of a compartment and attacked you, luckily you brung some weapons with you, you attack them, they run"
                " off into a secret room, it closes behind them.\n")
      sundial_path()

def desertwell_path():
       print("Suddendly, the temple starts filling with water, you try to break the doors to get out,"
       " but they are too strong and thick, you drown.\n")
       print("You have failed your quest.\n")
       choice_path12()

def sundial_path():
       print("Suddenly a secret door opens, you enter and are met with a straight path leading directly to another door, you feel suspicous of this, do"
              " you walk straight to the door, or investigate first?\n")
       
choice == input("1. walk straight to the door\n"
                " 2. investigate \n")

def choice_path13():
       if choice == "41":
              return dumb_path()
       elif choice == "42":
              return smart_path
       else:
              print("Invalid choice. Please try again.\n")
              choice_path13()

def dumb_path():
       print("you decide that there would be no harm in walking straight to the door, you do so while thinking of what could be in that treasure chest,"
        " you are intrupted mid-thought, when you trip and fall over something, its a trip-wire, the door on the other side of you closes, and lava starts"
        " pouring into the room, you die in the pool of lava.\n")
       print("You have failed your quest.\n")
       choice_path13()

def smart_path():
       ("You are very weary of the suspisously empty walkway, you thoroughly investigate the room and find a trip-wire, you carefully walk over it, and"
       " reach the other side, you wonder what would've happened if you hadn't investigated the room first, when you get to the other end, the door"
       " opens, you step inside another room, this time, you see another stone with anceint writing, as you walk closer, it says, if you can pass this"
       " test, you will be granted what you most desire, below it reads, When the door with no hinges finally opens, what is the traveler said"
       " to discover?\n")

choice = input(" 43. The shell\n"
               " 44. The egg\n"
               " 45. The yolk\n")

def choice_path14():
       if choice == "43":
              return shell_path()
       elif choice == "44":
              return egg_path()
       elif choice == "45":
              return yolk_path()
       else:
              print("Invalid choice. Please try again.\n")
              choice_path14
       
def shell_path():
       print("Suddenly treasure chests starts falling from above and crush you\n")
       print("You have failed your quest.\n")
       choice_path14()

def egg_path():
       print("Suddenly huge canons are lifted up, and treasure chests filled with treasure shoot out and hit you\n")
       print("You have failed your quest.\n")
       choice_path14()

def yolk_path():
      print("Suddenly the wall behind the stone opens, revealing a treasure chest placed on a mount of gold and gems! Inside you see gold, gems a"
            " sword and the red gemstone!\n")
      inventory.append("Sword", "Red gemstone")

def compass_path():
       print("without thinking, you hand the wondering arabic group your compass, they look at each other, then lauph, you ask them why, and they tell" 
       " you to go into the cave thats ontop of the *table mountain* beside you, you each exchange goodbyes, and then you head towards the mountaian,"
       " with great struggle, you manage to climb ontop of it, you reach the cave the arab wonderers where talking about, and then go inside, once inside,"
       " a hungry mountain lion leaps and attacks you, you couldn't react fast enough to reach and grab your weapons, you are eaten by the mountain lion.")
print("You have failed your quest.\n")
choice_path11()

def weapons_path():
       print("You reach inside your backpack and hand them all the weapons you have, they nod excightedly in agreement and invite you to ride on one" 
       " of their camels, you hop on one, and they take you to an anceint temple, they tell you its filled with various traps and puzzles and no one" 
       " has ever dared to step inside. you thanked them and said goodbye and stepped inside the temple, the door closes from behind you, inside the" 
       " temple is a stone with anceint arab words written on it, it reads, *In the heat I stand both day and night, yet I never sweat, though the sun"
       " is bright, I point the way with shadows long~ guess my name and you prove strong,* you take a minute to process the question, then come up"
       " with the anwser~")

print(" 46. A camel\n"
      " 47. A desert well\n"
      " 48. A sundial\n")

if choice == "46":
       print("Suddenly, a bunch of camels came out of a compartment and attacks you, you gave all your weapons to the arab wonderers, you have no defence"
       " for yourself, you die from camels")
       print("You have failed your quest.")
       choice_path11()

if choice == "47":
       desertwell_path()

if choice == "48":
       sundial_path()

from OutroScene import outro_scene;
outro_scene()





