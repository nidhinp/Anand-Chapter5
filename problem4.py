from os import listdir
from os.path import isfile, join
import sys

count = 0
def count_pyfile(path):
	contents = listdir(path)
	for f in contents:
		if isfile(join(path, f)):
			if '.py' in f:
				global count
				count += 1
		else:
			count_pyfile(join(path, f))			

if len(sys.argv) < 2:
	print 'usage: python problem4.py path'
else:
	count_pyfile(sys.argv[1])
	print 'python files:', count
