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

#locking dice
#show the user their hand
hand = roll_white_dice(3)
print("Current white dice", hand)
#make a list for locked dice
locked_dice = []

user_lock = input("Which dice would you like to lock? write like (1 3)")
for position in user_lock.split():
    number = int(position)

    index = number- 1

    value = hand[index]
    locked_dice.append(value)
print("you locked", locked_dice)
#calculate the size of the roll 
dice_to_roll = len(hand) - len(locked_dice) + 2
#roll the new dice
hand = roll_white_dice(dice_to_roll)
crow_die = roll_crow_die()

print("new white dice", hand)
print("crow die", crow_die)
print("locked dice", locked_dice)



