""" Write a program that takes an integer n and a filename as command line
    arguments and split the file into multiple small files with each having 
    n lines.
"""

import sys

def write_file(lines, newfiles):
	f = open('%d.txt' %newfiles, 'w')
	for line in lines:
		f.write(line)
	f.close()

def split(count, filename):
	f = open(filename)
	line_list = f.readlines()
	newfiles = len(line_list) / count
	i = 0
	while newfiles > 0:
		write_file(line_list[i:i+count], newfiles)
		i += count
		newfiles -= 1 	
		

if len(sys.argv) < 3:
	print 'usage python problem7.py number filename'
else:
	split(int(sys.argv[1]), sys.argv[2])
