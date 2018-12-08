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
		
	node = [childcount, metacount, children, meta, metasum]
	return (node, metasum)

file = open(sys.argv[1])

inputsnumbers = []
for line in file:
    inputsnumbers = line.split()

for i in range(len(inputsnumbers)):
	inputsnumbers[i] = int(inputsnumbers[i])

print(readnodes(inputsnumbers)[1])

file.close()