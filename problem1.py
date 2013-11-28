""" Write an iterator class reverse_iter, that takes a list and iterate it 
    from the reverse direction.
"""

class reverse_iter:
	def __init__(self, n):
		self.i = 0
		self.length = len(n)
		self.n = n[::-1]
	def next(self):
		if self.i < self.length:
			print self.n[self.i]
			self.i += 1
		else:
			raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
it.next()
it.next()
it.next()
it.next()
it.next()
		
