import sys
import numpy as np

import matplotlib.pyplot as plt


coordinates = []
file = open(sys.argv[1])
maxdist = int(sys.argv[2])
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

dimx = xmax - xmin
dimy = ymax - ymin


dgrid = np.zeros((dimx,dimy))

for i in range(dimx):
    for j in range(dimy):
        for point in coordinates:
            dist = manhatten((i,j),point)
            dgrid[i,j] += dist



edges = []
for i in range(dimx):
    if dgrid[i,0] < maxdist:
        edges.append(0)
        break

for i in range(dimx):
    if dgrid[i,dimy-1] < maxdist:
        edges.append(1)
        break

for i in range(dimy):
    if dgrid[0,i] < maxdist:
        edges.append(2)
        break

for i in range(dimy):
    if dgrid[dimx-1,i] < maxdist:
        edges.append(3)
        break


print(edges)
offset = 0
#additionalRows = []


if 3 in edges:
    while True:
        anySmallerMax = False
        row = []
        for i in range(dgrid.shape[1]):
            dist = 0
            for point in coordinates:
                dist += manhatten((dimx+offset,i),point)
            row.append(dist)
            if dist < maxdist:
                anySmallerMax = True
        rowA = np.array([row])
        dgrid = np.append(dgrid, rowA, axis = 0)

        offset += 1
        if anySmallerMax == False:
            break


if 2 in edges:
    while True:
        offset += 1
        anySmallerMax = False
        row = []
        for i in range(dgrid.shape[1]):
            dist = 0
            for point in coordinates:
                dist += manhatten((-offset,i),point)
            row.append(dist)
            if dist < maxdist:
                anySmallerMax = True
        rowA = np.array([row])
        dgrid = np.insert(dgrid, 0, rowA, axis = 0)

        
        if anySmallerMax == False:
            break

if 0 in edges:
    while True:
        offset += 1
        anySmallerMax = False
        row = []
        for i in range(dgrid.shape[0]):
            dist = 0
            for point in coordinates:
                dist += manhatten((i,-offset),point)
            row.append(dist)
            if dist < maxdist:
                anySmallerMax = True
        rowA = np.array([row]).T
        dgrid = np.insert(dgrid, 0, rowA, axis = 1)

        
        if anySmallerMax == False:
            break


if 1 in edges:
    while True:
        anySmallerMax = False
        row = []
        for i in range(dgrid.shape[0]):
            dist = 0
            for point in coordinates:
                dist += manhatten((i,dimy+offset),point)
            row.append(dist)
            if dist < maxdist:
                anySmallerMax = True
        rowA = np.array([row]).T
        dgrid = np.append(dgrid, rowA, axis = 1)

        offset += 1
        if anySmallerMax == False:
            break


dgrid[np.where( dgrid < maxdist )] = 2
dgrid[np.where( dgrid == maxdist )] = 1
dgrid[np.where( dgrid > maxdist )] = 0

plt.pcolor(dgrid)
plt.show()

print(len(dgrid[np.where( dgrid == 2 )]))

file.close()