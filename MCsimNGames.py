# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:16:38 2019

@author: Jacob Miske
"""
### Libraries ###
import numpy as np
#import scipy
import random
import collections
### Libraries End ###


print('Tool for Analysing Farkle \n')


### Configuration Variables ###
Ndice = 6; Nplayers = 5; NscoreToWin = 5000;
dice = [1,2,3,4,5,6]
#scoring parameters
score1 = 100; score5 = 50;
scoreThree1 = 1000; scoreThree2 = 200; scoreThree3 = 300;
scoreThree4= 400; scoreThree5 = 500; scoreThree6 = 600;
config = {'players': Nplayers, 'target_score': NscoreToWin, 'scoring':{'1':100, '5':50, '111':1000, '222':200, '333':300, '444': 400, '555': 500, '666': 600}}
### Configuration Variables End ###


### Strategies ###
# Strategy 1 #
grabbyVariableS1 = 1; #whether or not to grab all scoring dice or just the highest combo for # of dice to hold
# 1 for grabby means all scoring dice will be held, 0 means only the highest scoring dice/combo of dice will be held
holdScoreS1 = 200; holdDiceS1 = [1, 2]
Strategy1 = [grabbyVariableS1, holdScoreS1, holdDiceS1]
# Strategy 1 End #
# Strategy 2 #
grabbyVariableS2 = 1
holdScoreS2 = 200; holdDiceS2 = [1, 2, 3]
Strategy2 = [grabbyVariableS2, holdScoreS2, holdDiceS2]
# Strategy 2 End #
# Strategy 3 #
grabbyVariableS3 = 0
holdScoreS3 = 200; holdDiceS3 = [1, 2]
Strategy3 = [grabbyVariableS3, holdScoreS3, holdDiceS3]
# Strategy 3 End #
# Strategy 4 #
grabbyVariableS4 = 0
holdScoreS4 = 200; holdDiceS4 = [1, 2, 3]
Strategy4 = [grabbyVariableS4, holdScoreS4, holdDiceS4]
# Strategy 4 End #
# Strategy 5 #
grabbyVariableS5 = 1
holdScoreS5 = 500; holdDiceS5 = [1, 2, 3, 4, 5, 6]
Strategy5 = [grabbyVariableS5, holdScoreS5, holdDiceS5]
# Strategy 5 End #
### Strategies End ###
# {die: {count: value, ... }, ... }
valuedict = {1: {1: 100,
                 2: 200,
                 3: 1000,
                 4: 2000,
                 5: 2100,
                 6: 2200},
             2: {3: 200,
                 4: 400},
             3: {3: 300,
                 4: 600},
             4: {3: 400,
                 4: 800},
             5: {1: 50,
                 2: 100,
                 3: 500,
                 4: 1000,
                 5: 1050,
                 6: 1100},
             6: {3: 600,
                 4: 1200}}



### User Start ### WIP
while True:
    try:
        #Ask for rolling dice, a game, or simulation.
        simOrGame = str(input("Would you like to 'roll dice', 'play farkle', or 'run a simulation'? \n"))
    except ValueError:
        print("Sorry, I didn't understand that input.")
        continue
    else:
        break
        #Got a response
### User Start End ###



### Roll Dice Function ###
def get_rollDice(NumberDice):
    # Input x of dice (number of dice to roll)
    # Returns a dice roll of possible [1,2,3,4,5,6] in list
    rollResult = np.zeros(NumberDice) #empty list
    remainDice = NumberDice; 
    dice = [1,2,3,4,5,6] # possible values on a die
    for i in range(remainDice):
        rollResult[i] = random.choice(dice)
    return rollResult
#testRoll = get_rollDice(6)
#print("\n test roll")
#print(testRoll)
### Roll Dice Function End ###

# Scoring Dice Rolls #
def score(my_roll):
    # Input a certain number of dice, apply scoring rules of Farkle
    # Returns a biggest score, which is to continue rolling until reaching 
    #a certain score and Returns a single score, which is how far someone can go
    #with only one hand of dice
    
    #Make a dictionary type to hold the roll information
    counts = collections.Counter(my_roll)
    print(counts)
    single_score = 0 #conservative player's score
    biggest_score = 0 #grabby player's score, rolls twice 
    for die, count in counts.items():
        print('die')
        print(die)
        print('count')
        print(count)
        print(counts.get("1"))
    
    #if all(value != 0 for value in counts.values()):
    print(counts.values())
    #If the player busts with their roll
    if all(value == 0 for value in counts.values()):
        single_score = 0
        biggest_score = 0
        print("Biggest Score " + str(biggest_score))
        print("Single Score " + str(single_score))
        return(single_score, biggest_score)
    #running through all possible scoring combinations
    if counts[1.0] >= 3:
        single_score = 1000
        biggest_score = 1000
        three_ones = collections.Counter({1.0:3})
        counts.subtract(three_ones)
    if counts[6.0] >= 3:
        single_score = single_score + 600
        biggest_score = biggest_score + 600
        three_sixes = collections.Counter({6.0:3})
        counts.subtract(three_sixes)
    if counts[5.0] >= 3:
        single_score = single_score + 500
        biggest_score = biggest_score + 500
        three_fives = collections.Counter({5.0:3})
        counts.subtract(three_fives)
    if counts[4.0] >= 3:
        single_score = single_score + 400
        biggest_score = biggest_score + 400
        three_fours = collections.Counter({4.0:3})
        counts.subtract(three_fours)
    if counts[3.0] >= 3:
        single_score = single_score + 300
        biggest_score = biggest_score + 300
        three_threes = collections.Counter({3.0:3})
        counts.subtract(three_threes)
    if counts[2.0] >= 3:
        single_score = single_score + 200
        biggest_score = biggest_score + 200
        three_twos = collections.Counter({2.0:3})
        counts.subtract(three_twos)
    if counts[1.0] == 2:
        single_score = single_score + 200
        biggest_score = biggest_score + 200
        two_ones = collections.Counter({1.0:2})
        counts.subtract(two_ones)
    if counts[1.0] == 1:
        single_score = single_score + 100
        biggest_score = biggest_score + 100
        two_ones = collections.Counter({1.0:1})
        counts.subtract(two_ones)
    if counts[5.0] == 2:
        single_score = single_score + 100
        biggest_score = biggest_score + 100
        two_ones = collections.Counter({5.0:2})
        counts.subtract(two_ones)
    if counts[5.0] == 1:
        single_score = single_score + 50
        biggest_score = biggest_score + 50
        two_ones = collections.Counter({5.0:1})
        counts.subtract(two_ones)
    #Biggest score tries another time 
    if all(value == 0 for value in counts.values()):
        my_roll = get_rollDice(6)
        counts = collections.Counter(my_roll)
        print(counts)
        #If the player busts with their roll
        if all(value == 1 for value in counts.values()):
            biggest_score = 0
            print("Biggest Score " + str(biggest_score))
            print("Single Score " + str(single_score))
            return(single_score, biggest_score)
        if counts[1.0] >= 3:
            biggest_score = 1000
            three_ones = collections.Counter({1.0:3})
            counts.subtract(three_ones)
        if counts[6.0] >= 3:
            biggest_score = biggest_score + 600
            three_sixes = collections.Counter({6.0:3})
            counts.subtract(three_sixes)
        if counts[5.0] >= 3:
            biggest_score = biggest_score + 500
            three_fives = collections.Counter({5.0:3})
            counts.subtract(three_fives)
        if counts[4.0] >= 3:
            biggest_score = biggest_score + 400
            three_fours = collections.Counter({4.0:3})
            counts.subtract(three_fours)
        if counts[3.0] >= 3:
            biggest_score = biggest_score + 300
            three_threes = collections.Counter({3.0:3})
            counts.subtract(three_threes)
        if counts[2.0] >= 3:
            biggest_score = biggest_score + 200
            three_twos = collections.Counter({2.0:3})
            counts.subtract(three_twos)
        if counts[1.0] == 2:
            biggest_score = biggest_score + 200
            two_ones = collections.Counter({1.0:2})
            counts.subtract(two_ones)
        if counts[1.0] == 1:
            biggest_score = biggest_score + 100
            two_ones = collections.Counter({1.0:1})
            counts.subtract(two_ones)
        if counts[5.0] == 2:
            biggest_score = biggest_score + 100
            two_ones = collections.Counter({5.0:2})
            counts.subtract(two_ones)
        if counts[5.0] == 1:
            biggest_score = biggest_score + 50
            two_ones = collections.Counter({5.0:1})
            counts.subtract(two_ones)
    print("Biggest Score " + str(biggest_score))
    print("Single Score " + str(single_score))
    return(single_score, biggest_score)

test_score = score(get_rollDice(6))
# End Scoring Dice Rolls #

### Scoring Dice Function ###
def scoreDice(roll):
    #takes a roll, could be 3 dice or 6 dice, returns a highest 
    #possible die/combo from that roll and the single highest die/combo
    runningScore = 0 #type(int) for counting up total scoring
    Nones = roll.count(1); Ntwos = roll.count(2)
    Nthrees = roll.count(3); Nfours = roll.count(4)
    Nfives = roll.count(5); Nsixes = roll.count(6)
    NcountsAll = [Nones, Ntwos, Nthrees, Nfours, Nfives, Nsixes]
    if NcountsAll.count(0):
        runningScore = 3000
        #if at least one of all 6 possible, it's a straight, 
        #3000 points, best possible result
    highestScoreRoll = runningScore
    allScoreRoll = runningScore
    return [Ntwos, highestScoreRoll, allScoreRoll]

#testScore = scoreDice([1,1,1,2,3,4])
### Scoring Function End ###










   
### Dice Rolling ###
if(simOrGame == 'roll dice'):
    print('\n Dice Roller')
    while True:
        diceRolled = input('How many dice would you like to roll? ')
        print(diceRolled)
        if diceRolled == 'x':
            break
        try:
            diceRolled = int(diceRolled)
        except ValueError:
            print('Please give an integer value')
            continue
        else:
            print(get_rollDice(diceRolled))
            print('Score: ')
            print(score(get_rollDice(diceRolled)))
            continue
### Dice Rolling End ###







### Game Start ###
if(simOrGame == 'play farkle'):
    while True:
        players_number = int(input('How many players are present? '))
        players_list = np.zeros(players_number)
        print(players_list)
        while max(players_list) <= 10000:
            for i in players_list:
                print('player {}'.format(players_list[i])); print('\n');
                players_roll = input('Enter to roll dice')
                players_roll = get_rollDice(6)
                scoring = score(players_roll)
                players_list[i] = players_list[i]+scoring
            winning_players = [i for i in players_list if i >= 10000]
            # print winning players
            print('Congrats to winners: ')
            print(winning_players)
        break
    
### Game Start End ###




### Run a Simulation ###
if(simOrGame == 'run a simulation'):
    print('\n Farkle Simulation')
    while True:
        players_number = input('How many players? ')
        
        print(players_number)
        if players_number == 'x':
            break
        #generate list of players
        players_list = np.zeros(int(players_number))
        print(players_list)
        #determine risk (either risky or not risky) for each player
        player_risk = []; #empty list
        for i in range(len(players_list)):
            player_risk.append(input('Is player {} risky? (y or n)'.format(players_list[i]))); print('\n');
        #determine number of times to run the game
        simulate_times = input('How many simulation rounds?')
        print(simulate_times)
        try:
            simulate_times = int(simulate_times)
        except ValueError:
            print('Please give an integer value')
            continue
        try:
            players_number = int(players_number)
        except ValueError:
            print('Please give an integer value')
            continue
        else:
            while max(players_list) <= 10000:
                
                for i in range(len(players_list)):
                    #print('player {}'.format(players_list[i])); print('\n');
                    players_roll = get_rollDice(6)
                    scoring = score(players_roll)
                    if player_risk[i] == 'n':
                        print(player_risk)
                        players_list[i] = players_list[i]+scoring[0]
                    if player_risk[i] == 'y':
                        players_list[i] = players_list[i]+scoring[1]
                winning_players = [i for i in players_list if i >= 10000]
            # print winning players
            print('Congrats to winners: ')
            print(players_list)
            print(winning_players)
            break
### Run a simulation End ###






#quit statement
quit