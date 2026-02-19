inventory = []

def south_sceneA():
       print("You decide that your next adventure will be the southern island, located directly south of your home, after a few")
       print("days of sailing you reach the island, you dock you ship and step onto the beautiful, sandy beach, you see palm trees")
       print("swaying in the warm breeze, beatiful lush greenery and exotic plants and animals you've never seen before, its like")
       print("a paradise, you explore the beautiful lush island, and you manage to build an temporary shelter of palm leaves and")
       print("wood. As night creeps over the island, you go to sleep, but you are then woken up by weird loud noises outside your")
       print("shelter, do you investigate the noises, or stay in your shelter?\n")
choice = input("22. Investigate the noises\n"
               "23. Stay in your shelter\n")

def investigate_path():
       print("Curiosity gets the better of you and you decide to investigate the noises, you muster up the courage and step"
      "outside your shelter, as you do, you are greeted by an unwelcomed guest of black tall creatures with glowing"
      "purple eyes, you are stuck in a trance-like state, unable to move, you can only watch as the the figures purple"
      "eyes get bigger and bigger, getting closer and closer, until you cant see no more.")
       print("You have failed your quest.\n")
       choice_path5()

def stay_path():
       print("You decide to stay in your shelter, hoping the noises will go away, they eventually get farther away, until they are gone you cautiously"
       "look outside your shelter, you see nothing but the night and stars, you go back to sleep, and awake to a beautiful sunny morning, you decide"
       "to explore more of the island, as you walk deeper into the island, you name some of the exotic plants and animals, and jot them down in your"
       "journal, after a few hours of exploring you reach a beautiful waterfall, and the stream flowing from it, you drink some out of the stream and"
       "feel refreshed, you see a cave entrance behind the waterfall, do you enter the cave or rest by the waterfall.")

def choice_path5():
       if choice == "22":
        return investigate_path()
if choice == "23":
       stay_path()
        
else:
       print("Invalid choice. Please try again.")
       choice_path5()

choice = input("24. Enter the cave\n"
               "25. Rest by the waterfall\n")

def choice_path6():
       if choice == "24":
              return cave_path()
       elif choice == "25":
              return rest_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path6()

def rest_path():
       print("Exhausted from your exploration and haven finnaly a drink of the freshest water in your life, you lay down in a bed of flowers and gase up"
             " into the beautiful sky, full of colorful birds soaring through the air, you close your eyes, and fall asleep, you are awakend by a loud"
             " bird-like sound behind you, you turn around and see a huge bird in front of you, in its beak is your backpack! You try to snatch it from,"
             " its beak, but it flys off, you quickly run after it, it leads you into uncharted territory you've never discovered, you keep running"
             " but then, you feel yourself trip, before you can catch yourself, you fall off a very tall slope, you hit the ground with a hard and"
             "brutal thud.")
       print("You have failed you quest.")
       choice_path6()

def cave_path():
       print("You are have heard stories of hidden treasures in caves behind waterfalls, so you decide to enter the cave, as you step inside bats"
       "fly past you, the cave is dark and damp, you walk deeper into the cave, after a few minutes you reach a large chamber with walls"
       "covered in colorful, glowing crystals, in the center you see a large glowing crystal with a treasure map inside it, you brought some tools"
       "with you for your journey, witch tool should you use to break the crystal?")

def choice_path7():
       choice = input("26. Hammer\n"
                      "27. Chisel\n"
                      "28. Pickaxe\n")
       
if choice == "28":
       print("You use the pickaxe to try and break the crystal, you strike it a little too hard, the crystal breaks in half, and so does the map"
         "inside, you are left with nothing but shattered glass and torn paper.")
print("You have failed your quest.\n")
choice_path7()

if choice == "26":
       print("You use the hammer to try and break the crystal, you strike it with all your might, the crystal shatters into a million pieces, the" 
       "shards fly everywhere, one sharp shard stabs you in the chest, you fall to the ground, helpless, as you die of loss of blood.")
       print("You have failed your quest.\n")
       choice_path6()

if choice == "27":
       print("You carefully use the chisel to break the crystal, after a few hours of careful work, you manage to break the crystal without damaging"
         "the map inside, you unroll the map and see that it shows different landmarks on the island, with one landmark with an X marking, near"
         "the center of the island, you follow the map, after an hour of walking, you reach the spot marked on the map, when you get to the place,"
         "you see an entrance of an underground tunnel, you enter the tunnel, and find what it looks like a maze! You navigate through the maze using"
         "the direction on the back of the map, you eventually reach a room at the end of the maze, with three paths leading towards the left, right,"
         "and middle, which path do you take.")
       
choice = input("28. Left path\n"
               "29. Middle path\n"
               "30. Right path\n")

def choice_path8():
       if choice == "28":
              return left_path()
       elif choice == "29":
              return middle_path()
       elif choice == "30":
              return right_path()
       else:
              print("Invalid choice. Please try again.")
              choice_path8()

def left_path():
       print("You take the left path, after a few minutes of walking you reach a dead end, as you turn around to go back, you trigger a hidden trap,"
         " the floor opens beneath you, and you fall into a pit of spikes.")
print("You have failed your quest.\n")
choice_path8()

def middle_path():
       print("You take the middle path, as it seems most convincing, you walk for a few minutes and at the end of the path you see a lever on the wall,"
         " do you pull the lever or go back?\n")
       
choice = input("31. Pull the lever\n"
               "32. Go back\n")
def choice_path9():
       if choice == "31":
              return lever_path()
       elif choice == "32":
              return middle_path()
       else:
              print("Invalid choice. Please try again.\n")
              choice_path9()

def lever_path():
       print("You pull the lever, you hear a rumbling sound, the ceiling opens up then a large anvil falls from above, crushing you instantly.")
       print("You have failed your quest.\n")
choice_path9()

def right_path():
       print("You take the right path, the tunnel is long and narrow, after awhile, you hear echos of flowing water ahead, you walk faster and soon reach"
              " a large underground waterfall, with a sparkling pool below, you see a chest at the base of the waterfall, you swim to the chest and open it,"
              " inside you find gold, jewels, armor, and a pink gemstone!\n")
       inventory.append("Armor")
       inventory.append("Pink gemstone")

south_sceneA()

print("Congratulations! You have found the Treasure of Spring!\n")
print("Would you like to go to the final direction?")

choice = input( " 33. Yes" 
                " 34  No")

import sys
def choice_path10():
   if choice ==  "33":
    from WestScene import west_sceneA
    west_sceneA()
   if choice == "34":
      print("Really? After all this work you dont want to finish your quest? Oh well, home you go.")
      print("You have failed your quest.\n")
      sys.exit()



                       