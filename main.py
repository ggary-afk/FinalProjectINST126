#Build the dice machine

#Import random module to give us our random number 

import random

def roll_white_dice(amount):
    return [random.randint(1,12) for _ in range(amount)]

def roll_crow_die():
    return random.randint(1,12) 
    