# import random
#
# print random.randint(1,5)
#
# #First Prompt
# print "Well hello hail and harty traveler, welcome to my humble Inn. May I ask your name?"
#
# NAME= raw_input(" Full Name?:")
# print "Ahhh so your name is "+NAME+ " ....I see."
#
# #Second Prompt
# CLASS= raw_input(" What Vocation are you?:_")
# print "Ohh so you are a mighty, "+CLASS+", Very interesting..."
#
# #Third Prompt
# HOME= raw_input("Where do you hail from?:_")
# print "I see, so you come from the land of "+HOME+", How nice."
#
#
# #Fifth Prompt
# print "Tell me more about yourself!"
# STR= raw_input("What is your strength value?")
# DEX= raw_input("What is your dexterity value?")
# # LUK= raw_input("How much of a wizard are you?(0-3!)")
#
# #stats, class, beasts
# print "I see, I see... So you have "+STR+" points of STR, "+DEX+" points of DEX and "+LUK+" points LUK."
#
# CharacterInfo= {'Name':NAME, 'Class':CLASS, 'Home':HOME}
#
# BEASTS= ["Dragon", "Ogre", "Litch", "Hell Hound"]
#
# i = random.randint(1,5)
#
#
# #Print Beast Encounter
# print "Your adventure begins wile you make your way to an old dungeon were you face a mighty "+BEASTS[i]+"!"

def playerDPS(a, b):
    DPS = (a * b)

