""" Write a function peep, that takes an iterator as argument and
    returns the first element and an equivalent iterator.
"""

import itertools

def peep(it):
	iterator = list(it)
	first_element = iterator[0]
	return first_element, iterator

it = iter(range(5))
x, it1 = peep(it)
print x, it1

