import re

words = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
word_dict = dict( [(word,str(x+1)) for (x, word) in enumerate(words)])

def year(x):
	if int(x) >= 50 and int(x) <= 99:
		return '19' + x
	elif int(x) < 50:
		return '20' + x
	else:
		return x

def month(x):
	try:
		return word_dict[x]
	except:
		return x

regexes = [('(\d\d\d\d)-(\d\d)-(\d\d)',(1,2,3)),
			('(\d\d)/(\d\d)/(\d\d)',(3,1,2)),
			('(\d\d)#(\d\d)#(\d\d)', (2,1,3)),
			('(\d\d)\*(\d\d)\*(\d\d\d\d)', (3,1,2)),
			('(\w\w\w) (\d\d), (\d\d+)', (3,1,2))
			 ];


def parser(date):
	for r, (y, m, d) in regexes:
		match = re.match(r,date)
		if match:
			return '{0}-{1}-{2}'.format(year(match.group(y)),month(match.group(m)),match.group(d))

	'''match = re.match('(\d\d\d\d)-(\d\d)-(\d\d)',date)
	if match:
		return match.group(1) + '-' + match.group(2) + '-' + match.group(3)

	match = re.match('(\d\d)/(\d\d)/(\d\d)',date)
	if match:
		return year(match.group(3)) + '-' + match.group(1) + '-' + match.group(2)

	match = re.match('(\d\d)#(\d\d)#(\d\d)',date)
	if match:
		return year(match.group(2)) + '-' + match.group(1) + '-' + match.group(3)

	match = re.match('(\d\d)\*(\d\d)\*(\d\d\d\d)',date)
	if match:
		return match.group(3) + '-' + match.group(2) + '-' + match.group(1)

	match = re.match('(\w\w\w) (\d\d), (\d\d+)',date)
	if match:
		return year(match.group(3)) + '-' + word_dict[match.group(1)] + '-' + match.group(2)

	match = re.match('(')'''
	return 'NO MATCH for ' + date



with open('188-dates.txt','r') as f:
	for line in f:
		print(parser(line.rstrip()))