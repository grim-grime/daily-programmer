'''
iso 8601 standard for dates tells us the proper way to do an extended day is yyyy-mm-dd
yyyy = year
mm = month
dd = day
A company's database has become polluted with mixed date formats. They could be one of 6 different formats
yyyy-mm-dd
mm/dd/yy
mm#yy#dd
dd*mm*yyyy
(month word) dd, yy
(month word) dd, yyyy
(month word) can be: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Note if is yyyy it is a full 4 digit year. If it is yy then it is only the last 2 digits of the year. Years only go between 1950-2049.

Input:
You will be given 1000 dates to correct.

Output:
You must output the dates to the proper iso 8601 standard of yyyy-mm-dd

Challenge Input:
https://gist.github.com/coderd00d/a88d4d2da014203898af
'''

import re
from requests import get

words = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
word_dict = dict( [(word,str(x+1)) for (x, word) in enumerate(words)])
body = get('https://gist.github.com/coderd00d/a88d4d2da014203898af').text
dates = re.findall('">([\w\d][\w\d\s,]+[\w\d])</div>',body)

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
	return 'NO MATCH for ' + date

for date in dates:
	print(parser(date.rstrip()))