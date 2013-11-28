""" The built-in function enumerate takes iterable and returns an
    iterator over pairs(index, value) for each value in the source.
"""

def my_enumerate(x):
	index = 0
	for item in x:
		print index, item
		index += 1

my_enumerate(['a', 'b', 'c'])
