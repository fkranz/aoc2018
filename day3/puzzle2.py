import sys
import numpy as np
file = open(sys.argv[1])
fabricx = 1000
fabricy = 1000

fabric = []
for i in range(fabricx):
    fabi = [[]]
    for j in range(fabricy):
        fabi.append([])
    fabric.append(fabi)
ids = []

for line in file:
    words = line.split(' ')
    id = int(words[0].replace('#',''))
    pos = words[2].split(',')
    posy = int(pos[0])
    posx = int(pos[1].replace(':',''))
    dim = words[3].split('x')
    dimy = int(dim[0])
    dimx = int(dim[1])
    ids.append(id)

    for i in range(dimx):
        for j in range(dimy):
            value = fabric[i+posx][j+posy]
            value.append(id)
            fabric[i+posx][j+posy] = value



#overlapping = 0
for i in range(fabricx):
    for j in range(fabricy):
        if len(fabric[i][j]) > 1:
            for value in fabric[i][j]:
                if value in ids:
                    ids.remove(value)


print(ids)
file.close()