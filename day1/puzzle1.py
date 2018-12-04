import sys
freq = 0

file = open(sys.argv[1])

for line in file:
    freq += int(line)

print(freq)
file.close()