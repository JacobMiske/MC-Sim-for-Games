# MC-Sim-for-Games
Monte Carlo Attempt to Solve Strategy in N.G.


SCORING:
1 	100 points
5 	50 points
Three 1's 	1,000 points
Three 2's 	200 points
Three 3's 	300 points
Three 4's 	400 points
Three 5's 	500 points
Three 6's 	600 points
1-2-3-4-5-6 3000 points

Note that scoring combinations only count when made with a single throw. (Example: If a player rolls a 1 and sets it aside and then rolls two 1’s on their next throw, they only score 300 points, not 1000.)

Sometimes a single roll will provide multiple ways to score. For example, a player rolling 1-2-4-5-5-5 could score one of the following:

    100 points for the 1
    150 points for the 1 and a 5
    500 points for the three 5's
    600 points for the 1 and the three 5's

Caveat, at the end of game. If you go out, exceeding 5000 points, then the dice freeze, everyone gets one roll, if they bet the person who went out, they come on from behind.

First person to start is random. 

WINNING:
The first player to score a total of 5,000 or more points wins, provided that no other players with a remaining turn can exceed that score.


EXAMINED STRATEGIES
You look at the six dice rolled, how many scoring dice do you leave? How many rolling dice do you hold at? Players need to get at least 350 in their first scoring roll. 

For the following strategies, we'll assume that the strategizing player will want to score about 200 points in a turn unless they are shooting to convert. For someone who pushes to convert, we'll say they wish to get 500 points.

1. If you have five dice, you are likely to score if you roll, 4 good, 3 okay, 2 bad, 1 very bad. This strategy says 'hold' at two dice or less (ie one). Hold all scoring dice, hold at 2 or 1 dice left. Hold at 200 pnts.

2. If you have five dice, you are likely to score if you roll, 4 good, 3 okay, 2 bad, 1 very bad. This strategy says 'hold' at two dice or less (ie one). Hold all scoring dice, hold at 3 or 2 or 1 dice left. Hold at 200 pnts.

3. Each time you roll, pick only the highest scoring dice/combo of dice and keep rolling until 2 or 1 dice left. Hold at 200 pnts.

4. Each time you roll, pick only the highest scoring dice/combo of dice and keep rolling until 3 or 2 or 1 dice left. Hold at 200 pnts.

5. Roll until lose or convert. Hold at 500 pnts.

