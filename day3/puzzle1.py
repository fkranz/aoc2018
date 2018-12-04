import sys
import numpy as np
file = open(sys.argv[1])
fabricx = 1000
fabricy = 1000

fabric = np.zeros((fabricx,fabricy))

for line in file:
    words = line.split(' ')
    id = int(words[0].replace('#',''))
    pos = words[2].split(',')
    posy = int(pos[0])
    posx = int(pos[1].replace(':',''))
    dim = words[3].split('x')
    dimy = int(dim[0])
    dimx = int(dim[1])

    for i in range(dimx):
        for j in range(dimy):
            value = fabric[i+posx,j+posy]
            fabric[i+posx,j+posy] = value + 1


overlapping = 0
for i in range(fabricx):
    for j in range(fabricy):
        if fabric[i,j] > 1:
            overlapping += 1

print(overlapping)
file.close()