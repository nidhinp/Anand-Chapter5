""" Write a function findfiles that recursively descends the directory 
    tree for the specified directory and generates paths of all the files
    in the tree.
"""

from os import listdir
from os.path import isdir, join
import sys

def findfiles(path):
	contents = listdir(path)
	for files in contents:
		if isdir(join(path, files)):
			findfiles(join(path, files))
		else:
			print join(path, files) 	

if len(sys.argv) < 2:
	print 'usage: python problem3.py path'
else:
	findfiles(sys.argv[1])
