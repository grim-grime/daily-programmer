'''
Input Description
You will first input a number N. You will then accept N lines of input in the format:
f:force
This is a short-form definition; this particular example denotes that the flag -f is equivalent to the flag --force. Lastly you are to accept one further line of input containing the flags and other parameters passed to the program. Remember that programs can accept parameters that are not flags. These don't start with a hyphen and there may be several of them. For example,
-Q -rf --no-preserve-root directory1/ directory2/
In which the flags given are -Q -rf (same as -r -f) and --no-preserve-root, and the parameters are directory1/ and directory2/. Remember the Q, r and f flags are defined in the short-form definition format above.
Output Description 
You are to output a list of the full names of all of the flags entered (eg. force rather than f), as well as all of the parameters entered. Alternatively, if a short-form flag is entered that doesn't have a difinition, print an error.
'''

my_input = \
'''4
a:all
f:force
n:networking
N:numerical-list
-aN 12 --verbose 192.168.0.44'''

try:
	my_input = sys.argv[1]
except:
	pass

my_input = my_input.split('\n')

flags = dict([x.split(':') for x in my_input[1:-1]])

for word in my_input[-1].split(' '):
	if word[0] != '-':
		print('parameter: ' + word)
	elif word[1] !='-':
		for char in word[1:]:
			print('flag: ' + flags[char])
	else:
		print ('flag: ' + word)

