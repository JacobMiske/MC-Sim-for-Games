# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:16:38 2019

@author: Jacob Miske
"""
import numpy as np
#import scipy
import random


### Setting Variables ###
Ndice = 6; Nplayers = 5; NscoreToWin = 5000;
dice = [1,2,3,4,5,6]
#scoring parameters
score1 = 100; score5 = 50;
scorethree1 = 1000; scorethree2 = 200; scorethree3 = 300;
scorethree4= 400; scorethree5 = 500; scorethree6 = 600;
### Setting Variables End ###


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


### Scoring Function ###
def scoreDice(roll):
    #takes a roll, could be 3 dice or 6 dice, returns a highest possible die/combo from that roll and the single highest die/combo
    Nones = roll.count(1); Ntwos = roll.count(2)
    Nthrees = roll.count(3); Nfours = roll.count(4)
    Nfives = roll.count(5); Nsixes = roll.count(6)
    NcountsAll = [Nones, Ntwos, Nthrees, Nfours, Nfives, Nsixes]
    
    
    
    highestScoreRoll = 0
    allScoreRoll = 0
    
    
    return [Ntwos, highestScoreRoll, allScoreRoll]

testScore = scoreDice([1,1,1,2,3,4])

### Scoring Function End ###


### Roll Dice Function ###
def rollDice(strategy):
    # For a random roll of dice, returns a score for that roll, given a strategy list
    score = 0; rollResult = [1,1,1,1,1,1]
    grabbyVariable = strategy[0]; holdScore = strategy[1]; holdDice = strategy[2]
    remainDice = Ndice
    while score <= holdScore: #Until greater than or equal to hold score, barring other strategy rules, keep rolling
        
        for i in range(remainDice):
            rollResult[i] = random.choice(dice)
        score+=100
    return score

testRoll = rollDice(Strategy1)

### Roll Dice Function End ###


### Running Games ###
playersArray = np.zeros(Nplayers)
turn = 0
turnList = []
while max(playersArray) < 5000:
    turn+=1
    playersArray[1] += 100
    
    



