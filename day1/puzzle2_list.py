import time
start = time.time()

import sys
freq = 0
frequencies_reached = [0]

while True:
    file = open(sys.argv[1])

    for line in file:
        freq += int(line)
        if freq in frequencies_reached:
            print(freq)
            end = time.time()
            print(end-start)
            exit(0)
        frequencies_reached.append(freq)

    file.close()