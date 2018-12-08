import sys

def readnodes(numbers):
	childcount = numbers.pop(0)
	metacount = numbers.pop(0)
	children = []
	metasum = 0
	for i in range(childcount):
		temp = readnodes(numbers)
		children.append(temp[0])
		metasum += temp[1]
	meta = []
	for i in range(metacount):
		temp = numbers.pop(0)
		metasum += temp
		meta.append(temp)
	value = 0
	if childcount == 0:
		value = metasum
	else:
		for item in meta:
			if item == 0:
				continue
			if item > childcount:
				continue
			else:
				value += children[item-1][4]

	node = [childcount, metacount, children, meta, value]
	return (node, value)

file = open(sys.argv[1])

inputsnumbers = []
for line in file:
    inputsnumbers = line.split()

for i in range(len(inputsnumbers)):
	inputsnumbers[i] = int(inputsnumbers[i])

print(readnodes(inputsnumbers)[1])

file.close()