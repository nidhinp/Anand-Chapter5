""" Write a function to compute the total number of lines of code,
    ignoring empty and command lines, in all python in the specified 
    directory recursively.
"""

from os import listdir
from os.path import isfile, join
import sys

def count_lines(filename):
	count = 0
	for line in open(filename):
		if line == '\n' or line[0] == '#':
			continue
		else:
			count +=1
	return count

line_count = 0
def count_pyfile(path):
	contents = listdir(path)
	for f in contents:
		if isfile(join(path, f)):
			if '.py' in f:
				global line_count
				line_count += count_lines(join(path, f))	
		else:
			count_pyfile(join(path, f))			

if len(sys.argv) < 2:
	print 'usage: python problem4.py path'
else:
	count_pyfile(sys.argv[1])
	print 'number of lines in python files:', line_count
