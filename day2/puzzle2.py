import sys
ids = []

file = open(sys.argv[1])

for line in file:
    ids.append(line)

for i in range(len(ids)):
	reference = ids[i]
	for j in range(i+1, len(ids)):
		diffcount = 0
		id = ids[j]
		for index,letter in enumerate(reference):
			if letter != id[index]:
				diffcount += 1
			if diffcount > 1:
				break
		if(diffcount <= 1):
			print(reference)
			print(id)

file.close()