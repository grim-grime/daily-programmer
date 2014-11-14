'''
This program traverses a directional graph connected with >, <, ^, and v characters.
It returns the cycle with the largest length.
'''

#default data
rawdata = \
'''5 5
>>>>v
^v<<v
^vv^v
^>>v<
^<<<^'''

#load data
try:
	with open('188-hard-data.txt','r') as f:
		rawdata = f.read()
except:
		pass

class Board(object):
	def __init__(self, board):
		self.w = len(board[0])
		self.h = len(board)
		self.board = board
	def __str__(self):
		return '\n'.join(self.board)
	#get tile type
	def pos(self,coord):
		x,y = coord
		return self.board[y][x]
	#get next tile position
	def move(self,coord):
		x,y = coord
		#pseudo-switch statement based off tile type
		return  {'^': lambda x, y: (x,self.h-1) if y <= 0 else (x,y-1),
		'>': lambda x, y: (0,y) if x >= (self.w - 1) else (x+1,y),
		'<': lambda x, y: (self.w-1,y) if x <= 0 else (x-1,y),
		'v': lambda x, y: (x, 0) if y >= (self.h - 1)  else (x,y+1)}[self.pos((x,y))](x,y)
	#follow trail until a cycle is found - return nothing if repeated point is not original point
	def trail(self,coord):
		visited = set()
		point = coord
		while point not in visited:
			visited.add(point)
			point = self.move(point)
		if point == coord:
			return (len(visited),visited)
		else:
			return (0,set())
	def print_only(self,coords):
		for y in range(self.h):
			line = ''
			for x in range(self.w):
				if (x,y) in coords:
					line += self.pos((x,y))
				else:
					line += ' '
			print(line)

myboard = Board(rawdata.split('\n')[1:])

#get the cycle with the greatest length
best_length, best_set = \
	max( [myboard.trail((x,y)) for x in range(myboard.w) for y in range(myboard.h)] )

myboard.print_only(best_set)