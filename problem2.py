""" Write a program that takes one or more filename as arguments and 
    prints all the lines which are longer than 40 characters.
"""

def longer(*filenames):
	for files in filenames:
		for line in open(files):
			if len(line) > 40:
				print line

longer('help.txt', 'she.txt')
