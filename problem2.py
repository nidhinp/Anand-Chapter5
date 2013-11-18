def longer(*filenames):
	for files in filenames:
		for line in open(files):
			if len(line) > 40:
				print line

longer('help.txt', 'she.txt')
