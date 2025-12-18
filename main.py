#Build the dice machine

#Import random module to give us our random number 

import random

def roll_white_dice(amount):
    rolls=[]
    for i in range(amount):
        roll = random.randint(1,12)
        rolls.append(roll)
    return rolls

def roll_crow_die():
    return random.randint(1,12) 
    