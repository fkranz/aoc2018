import sys
import re

file = open(sys.argv[1])
line = list(file.readlines()[0])[:-1]
line = list(filter(lambda a: a != " ", line))

replaced = True
while replaced:
	replaced = False
	for i in range(len(line)-1):
		if line[i] == line[i+1].swapcase():
			replaced = True
			line[i] = "#"
			line[i+1] = "#"
	line = list(filter(lambda a: a != "#", line))

print(len(line))
file.close()