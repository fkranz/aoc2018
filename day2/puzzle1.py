import sys

twos = 0
threes = 0

file = open(sys.argv[1])

for line in file:
	counts = dict()
	for letter in line:
		if letter in counts:
			tmp = counts[letter]
			counts[letter] = tmp+1
		else:
			counts[letter] = 1
	if 2 in counts.values():
		twos += 1
	if 3 in counts.values():
		threes += 1

print(twos * threes)
file.close()