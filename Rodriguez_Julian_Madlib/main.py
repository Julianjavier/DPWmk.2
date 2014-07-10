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

BEAST_HP= random.randint(2000, 9999)
Damage= 0

# i = random.randint(0,3) Original random


#Print Beast Encounter
print "Your adventure begins wile you make your way to an old dungeon were you face a mighty "+BEASTS[i]+"!"

SKILL= raw_input ("What Skill do you wish to use?")

def playerDPS(a, b):
    DPS = (a * b)
    return DPS

DPS= playerDPS(int(STR), int(DEX))

def MonsterDefence(a, b, c):
    DPS = (a / b) * c
    print "You inflict "+str(DPS)+" points of damage!"
    if DPS <= 9999:
        print("The "+BEASTS[i]+" Has proven more of a challenge than expected, you decide to retreat and return another day.")
    else:
        print("Congratulations you have slain the "+BEASTS[i]+" and you return with a bounty of great spoils!")


# DPS= playerDPS(20, 100)


while BEAST_HP > 0:
    BEAST_HP - DPS
    print "You inflicted"+str(DPS)+". on the foul Beast, it now has"+str(BEAST_HP)

