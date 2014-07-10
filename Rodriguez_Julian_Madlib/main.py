import random

#First Prompt
print "Well hello hail and harty traveler, welcome to my humble Inn. May I ask your name?"

NAME= raw_input(" Full Name?:")
print "Ahhh so your name is "+NAME+ " ....I see."

#Second Prompt
CLASS= raw_input(" What Vocation are you?:_")
print "Ohh so you are a mighty, "+CLASS+", Very interesting..."

#Third Prompt
HOME= raw_input("Where do you hail from?:_")
print "I see, so you come from the land of "+HOME+", How nice."

###Luck Stay(Random)
LUK= random.randint(0,3)

#Fifth Prompt
print "Tell me more about yourself!"
STR= raw_input("What is your strength value?")
DEX= raw_input("What is your dexterity value?")
# LUK= raw_input("How much of a wizard are you?(0-3!)")

#stats, class, beasts
print "I see, I see... So you have "+STR+" points of STR and "+DEX+" points of DEX ."

CharacterInfo= {'Name':NAME, 'Class':CLASS, 'Home':HOME}

BEASTS= ["Dragon", "Ogre", "Litch", "Hell Hound"]

BEAST_HP= random.randint(100, 999)
damage= BEAST_HP

# i = random.randint(0,3) #Original random

for i in range(0, int(LUK)):
    if LUK > 4:
        LUK == 4
    else:
        LUK == LUK

    BEAST=BEASTS[i]

#Print Beast Encounter
print "Your adventure begins wile you make your way to an old dungeon were you face a mighty "+BEAST+"!"

# SKILL= raw_input ("What Skill do you wish to use?")

# def playerDPS(a, b):
#     DPS = (a * b)
#     return DPS


def playerDPS(a, b):
    DPS = (a * b)
    print "You inflict "+str(DPS)+" points of damage!"
    if DPS <= BEAST_HP:
        print("The "+BEAST+" Has proven more of a challenge than expected, you decide to retreat and return another day.")
    else:
        print("Congratulations you have slain the "+BEAST+" and you return with a bounty of great spoils!")

DPS= playerDPS(int(STR), int(DEX))


# DPS= playerDPS(20, 100)
#
# ##Original Loop for monster fight
# while damage > 0:
#     damage== BEAST_HP - DPS
#     print "You inflicted"+str(DPS)+". on the foul Beast, it now has"+str(BEAST_HP)

