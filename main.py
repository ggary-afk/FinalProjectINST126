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
hand = roll_white_dice(3)
locked_dice = []
roll_count = 1
print ("Roll {roll_count}")
print("Current white dice:", hand)
while roll_count <4:
    print(f"\nYou are about to start roll number {roll_count + 1}")

    user_choice = input("Type in roll if you want to keep rolling or score if you want to stop:")
    if user_choice == 'score':
        print("chose to score")
        break

    #locking dice
    #show the user their hand

    user_lock = input("Which dice would you like to lock? write like (1 3)")
    for position in user_lock.split():
        number = int(position)

        index = number- 1

    #raise an issue if the user types in an incorrect number
        if index < 0 or index >= len(hand):
            print(f"warning {number} is not a position in your hand")
            continue
        value = hand[index]
        locked_dice.append(value)

    
    #print the message
    print("you locked", locked_dice)

    #calculate the size of the roll 
    dice_to_roll = len(hand) - len(locked_dice) + 2
    #roll the new dice
    hand = roll_white_dice(dice_to_roll)
    crow_die = roll_crow_die()

    print("new white dice", hand)
    print("crow die", crow_die)
    print("locked dice", locked_dice)

    #build the crow rule

    if crow_die == 12:
        print("You rolled a 12 on the crow die, you've busted!")
        break

    #Account for other numbers on the crow die
    else:
        survivors = []
        for die in hand:
            if die == crow_die:
                print(f"The crow die you rolled is {crow_die} and it eliminates your white {die} ")
            else:
                survivors.append(die)
        hand = survivors
    print("Your remaining white dice", hand)
    #update the count
    roll_count = roll_count + 1