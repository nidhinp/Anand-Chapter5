def my_izip(a, b):
	index = 0
	for item in a:
		print a[index], b[index]
		index += 1

my_izip(['a', 'b', 'c'], [1, 2, 3])
