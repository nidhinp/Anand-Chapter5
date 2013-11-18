import os

def lines_of_code(path):
	contents = os.listdir(path)
	python_files = [f for f in contents if '.py' in f]
	print python_files
	for x in python_files:
		f = open(path +'/'+ x, 'r')
		print x, len(f.readlines())

lines_of_code('/home/nidhin/programs/python/anandpython/chapter5')
