import sys
import re

file = open(sys.argv[1])
inputline = list(file.readlines()[0])[:-1]
inputline = list(filter(lambda a: a != " ", inputline))
lengths = {}
for c in "abcdefghijklmnopqrstuvwxyz":
	line = inputline
	line = list(filter(lambda a: a != c, line))
	line = list(filter(lambda a: a != c.swapcase(), line))

	replaced = True
	while replaced:
		replaced = False
		for i in range(len(line)-1):
			if line[i] == line[i+1].swapcase():
				replaced = True
				line[i] = "#"
				line[i+1] = "#"
		line = list(filter(lambda a: a != "#", line))
	lengths[c] = len(line)

minkey = min(lengths, key=lengths.get)
print(minkey, lengths[minkey])
file.close()