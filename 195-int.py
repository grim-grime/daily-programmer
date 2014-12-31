'''
[2014-12-31] Challenge #195 [Intermediate] Math Dice
Description:
Math Dice is a game where you use dice and number combinations to score. It's a neat way for kids to get mathematical dexterity. In the game, you first roll the 12-sided Target Die to get your target number, then roll the five 6-sided Scoring Dice. Using addition and/or subtraction, combine the Scoring Dice to match the target number. The number of dice you used to achieve the target number is your score for that round. For more information, see the product page for the game: (http://www.thinkfun.com/mathdice)
Input:
You'll be given the dimensions of the dice as NdX where N is the number of dice to roll and X is the size of the dice. In standard Math Dice Jr you have 1d12 and 5d6.
Output:
You should emit the dice you rolled and then the equation with the dice combined. E.g.
 9, 1 3 1 3 5

 3 + 3 + 5 - 1 - 1 = 9
 '''


from random import random

#recursively pull from inp to reach target, selected value stored in out
def func(target,inp):
	#base case
	if len(inp) == 1:
		if target == inp[0]:
			return [inp[0]]
		return []
	#loop over adding, substracting, discarding
	a = func(target-inp[0],inp[1:]) + [inp[0]]
	b = func(target+inp[0],inp[1:]) + [-inp[0]]
	c = func(target,inp[1:])
	ans = max(a,b,c,key=len)
	#len(ans) == 1 -> func() returned no answer
	return ans if len(ans) > 1 else []

#outputs list of random numbers given string of from NdX'
def roll(dice):
	number, val = [int(x) for x in dice.split('d')]
	return [int(random() * val)+1 for _ in range(number)]

while True: 
	target_dice, score_dice = input().split()
	target = sum(roll(target_dice))
	rolled_score_dice = roll(score_dice)
	print(str(target) + ', ' + ' '.join(str(x) for x in rolled_score_dice))

	#get answer
	selected= func(target,rolled_score_dice)
	if selected:
		#format answer
		selected = ['+ '+str(x) if x > 0 else '- '+str(abs(x)) for x in selected]
		selected[0] = selected[0][2:] if selected[0][0] == '+' else selected[0]
		print(' '.join(selected), end =' = {}\n'.format(target))
	else:
		print('NO SOLUTION')