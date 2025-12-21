<<<<<<< HEAD
#Importe random module to give us our random number 

import random
import time
import matplotlib.pyplot as plt
#Created a dice roller
def roll_white_dice(amount):
    rolls=[]
    for i in range(amount):
        roll = random.randint(1,12)
        rolls.append(roll)
    return rolls
#Created a crow dice roller
def roll_crow_die():
    return random.randint(1,12)
#Created a roller
def check_for_sets(current_dice):
    print(f"Checking for Sets in: {current_dice}")

    wild_count = 0
    for die in current_dice:
        if die == 12:
            wild_count = wild_count + 1
#Check for sets            
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
#Check for runs
def check_for_runs(current_dice):
    print(f"Checking for Runs 9 in {current_dice}")

    wild_count = 0
    for die in current_dice:
        if die == 12:
            wild_count = wild_count + 1

    found_run = False

    for start_number in range(1,12):
        current_streak = 0 
        placeholder_wild = wild_count
        run_numbers = []
        for next_num in range(start_number, 13):
            has_number = False
            for die in current_dice:
                if die == next_num:
                    has_number = True

            if has_number:
                current_streak = current_streak +1 
                run_numbers.append(next_num)
                
            elif placeholder_wild > 0:
                    current_streak = current_streak + 1 
                    placeholder_wild = placeholder_wild - 1
                    run_numbers.append (f"{next_num}wild")
            else:
                break
        if current_streak >= 3:
            print(f"You have a run that starts at {start_number}: {run_numbers}")
            found_run = True
    if found_run ==  False:
        print("No runs found")
#Made a graph for the player
def final_score_graph(final_hand):
    print("Final scoresheet")
    counts = [0] * 13
    for die in final_hand:
        counts[die] = counts[die] + 1
    x_numbers = range(1,13)
    y_counts = counts[1:13]
    plt.figure(figsize=(8,5))
    bars = plt.bar(x_numbers, y_counts, color='blue', edgecolor='black')
    for i in range(12):
        if y_counts[i] >= 3:
            bars[i].set_color('green') 
            bars[i].set_edgecolor('black')
        elif y_counts[i] > 0:
            bars[i].set_color('blue')
    plt.title('Your final hand', fontsize=14)
    plt.xlabel('Dice Number (1-12)', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(range(1, 13)) 
    plt.yticks(range(0, 10)) 
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('final_score.png')


hand = roll_white_dice(3)
locked_dice = []
roll_count = 1
print (f"Roll {roll_count}")
print("Current white dice:", hand)
#set up check
has_scored = False
while roll_count <4:
    print(f"\n\n========================================================================")
    print(f"\nYou are about to start roll number {roll_count + 1}")

    user_choice = input("\nType in roll if you want to keep rolling or score if you want to stop:")
    if user_choice == 'score':
        print("Chose to score")
        all_dice = hand + locked_dice
        print("Final dice to score:",all_dice)
        check_for_sets(all_dice)
        check_for_runs(all_dice)

        has_scored = True
        break
#locking dice

    user_lock = input("You have to lock at least one die Which dice would you like to lock? Type the position of the dice in your hand like 1 or 2:")
    for position in user_lock.split():
        number = int(position)

        index = number- 1

    #raise an issue if the user types in an incorrect number
        if index < 0 or index >= len(hand):
            print(f"Warning {number} is not a position in your hand")
            continue
        value = hand[index]
        locked_dice.append(value)

    
    #print the message
    print("You locked", locked_dice)

    #calculate the size of the roll 
    dice_to_roll = len(hand) - len(user_lock.split()) + 2
    print("\nRolling dice...")
    time.sleep(3)
    #roll the new dice
    hand = roll_white_dice(dice_to_roll)
    crow_die = roll_crow_die()
#print messages
    print("\nNew white dice", hand)
    print("\nnow here's the kicker")
    time.sleep(3)
    print("\nCrow die", crow_die)
    print("\nLocked dice", locked_dice)

    #build the crow rule

    if crow_die == 12:
        print("You rolled a 12 on the crow die, you've busted!")
        has_scored = True
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
#check scoring
if has_scored == False: 
    print('End of turn, score is:')
    all_dice = hand + locked_dice
    check_for_sets(all_dice)
    check_for_runs(all_dice)
all_dice = hand + locked_dice
final_score_graph(all_dice)
