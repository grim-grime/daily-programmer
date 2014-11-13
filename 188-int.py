'''
This program makes a box and whisker plot and prints it with ASCII art.
'''

import math

with open('188-int-data.txt','r') as f:
	numbers = []
	for line in f:
		numbers += [int(x) for x in line.split()]

#get basic info
numbers = sorted(numbers)
idxes = [math.ceil(len(numbers) * x/4) - 1 for x in [1, 2, 3]]
quartiles = [numbers[x] for x in idxes]
IQR = quartiles[2] - quartiles[0]
maximum = quartiles[2] + 1.5 * IQR
minimum = quartiles[0] - 1.5 * IQR

#get outliers
left_outliers = []
right_outliers = []
for i, x in enumerate(numbers):
	if x < minimum:
		left_outliers += [x]
		numbers[i] = 'x' + ' ' * (len(str(x)) - 1)
	elif x > maximum:
		right_outliers += [x]
		numbers[i] = 'X' + ' ' * (len(str(x)) - 1)

#convert data to string
chars = ' '.join([str(x) for x in numbers])
left_outliers = ' '.join([str(x) for x in left_outliers])
right_outliers = ' '.join([str(x) for x in right_outliers])
char_idxes = [chars.index(str(q)) for q in quartiles]
right_outlier_start = chars.index('X')

#print art
print(' '*char_idxes[0] + '_' * (char_idxes[2]-char_idxes[0]))
print(left_outliers, end = '') 
print(' '*(char_idxes[0]-len(left_outliers)) + '|' + ' ' * (char_idxes[1]-char_idxes[0]-1) + '|' + \
	' '*(char_idxes[2]-char_idxes[1]-1) + '|' + ' ' * (right_outlier_start - char_idxes[2] -1) , end = '')
print(right_outliers)
print(chars)
print(' '*char_idxes[0] + '|' + '_' * (char_idxes[1]-char_idxes[0]-1) + '|' + \
	'_'*(char_idxes[2]-char_idxes[1]-1) + '|' )
