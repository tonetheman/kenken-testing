
import random

def dbg(o):
	print "dbg", o

class Puzzle:
	def __init__(self,size):
		self.size = size
	def gen(self):
		total_squares = self.size * self.size
		self.p = [None] * total_squares
		order = random.sample(xrange(total_squares), total_squares)
		dbg(order)
		for spot in order:
			choice = self.guess(self.size)
			self.check_row(spot, choice)
	def check_row(self, spot, choice):
		pass
	def check_col(self, spot, choice):
		pass
	def guess(self,size):
		return random.randint(1,size)

def makepuzzle(size):
	p = Puzzle(size)
	p.gen()
	return p


makepuzzle(3)
