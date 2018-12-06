import sys
import numpy as np
coordinates = []
file = open(sys.argv[1])
xmax = 0
xmin = 99999999
ymax = 0
ymin = 99999999

def manhatten(x,y):
    return abs(x[1] - y[1]) + abs(x[0] - y[0])

for line in file:
    xys = line.split(",")
    xc = int(xys[0])
    yc = int(xys[1])
    coordinates.append((xc,yc))
    xmax = max(xc,xmax)
    xmin = min(xc,xmin)
    ymax = max(yc,ymax)
    ymin = min(yc,ymin)

dimx = xmax - xmin + 1
dimy = ymax - ymin + 1


cgrid = np.empty((dimx,dimy))
cgrid.fill(-1)

dgrid = np.empty((dimx,dimy))
dgrid.fill(99999999)

for i in range(dimx):
    for j in range(dimy):
        for index,point in enumerate(coordinates):
            dist = manhatten((i+xmin,j+ymin),point)
            if dist == dgrid[i,j]: 
                dgrid[i,j] = dist
                cgrid[i,j] = 100
            if dist < dgrid[i,j]: 
                dgrid[i,j] = dist
                cgrid[i,j] = index

indices = list(range(len(coordinates)))

for i in range(dimx):
    temp = cgrid[i,0]
    if temp in indices: 
        indices.remove(temp)
    temp = cgrid[i,dimy-1]
    if temp in indices: 
        indices.remove(temp)

for j in range(dimy):
    temp = cgrid[0,j]
    if temp in indices: 
        indices.remove(temp)
    temp = cgrid[dimx-1,j]
    if temp in indices: 
        indices.remove(temp)

_,counts = np.unique(cgrid, return_counts = True)

maxcount = max(counts[indices])

print(maxcount)
file.close()