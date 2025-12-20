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
def check_for_sets(current_dice):
    print(f"Checking for Sets in: {current_dice}")

    wild_count = 0
    for die in current_dice:
        if die == 12:
            wild_count = wild_count + 1
            
    found_valid_set = False
    for number_check in range(1, 12):
        count_for_number = 0
        for die in current_dice:
            if die == number_check:
                count_for_number = count_for_number + 1
        total_count = count_for_number + wild_count
        if total_count >= 3 and count_for_number > 0:
            print(f"You can score a set of {number_check}s total dice: {total_count}")
            found_valid_set = True

    if found_valid_set == False:
        print("No valid sets found")
hand = roll_white_dice(3)
locked_dice = []
roll_count = 1
print ("Roll {roll_count}")
print("Current white dice:", hand)
#set up check
has_scored = False
while roll_count <4:
    print(f"\nYou are about to start roll number {roll_count + 1}")

    user_choice = input("Type in roll if you want to keep rolling or score if you want to stop:")
    if user_choice == 'score':
        print("chose to score")
        all_dice = hand + locked_dice
        print("final dice to score:",all_dice)
#Count the wilds
        wild_count = 0
        for die in all_dice:
            if die == 12:
                wild_count = wild_count + 1
#check Status
        found_valid_set = False
#Check the range
        for number_check in range(1,12):
            count_for_number = 0
            for die in all_dice:
                if die == number_check:
                    count_for_number = count_for_number + 1

            total_count = count_for_number + wild_count
            if total_count >= 3 and count_for_number > 0:
                print(f"You can score a set of {number_check}s total dice: {total_count}")
                found_valid_set = True
        if not found_valid_set:
            print("Sorry, you don't have a valid set")   
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