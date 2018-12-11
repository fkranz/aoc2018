import sys
import numpy as np 
from scipy import ndimage
import time

serial = int(sys.argv[1])

def computePowerLevel(x, y, serial):
    rackID = x + 10
    result = rackID * y
    result += serial
    result *= rackID
    result /= 100
    result = int(result)
    if result >= 10:
        tmp = str(result)
        result = int(tmp[len(tmp)-1])
    result -= 5
    return result
 
def computeTotalPower(x,y,grid,squaresize):
    result =  0
    for i in range(squaresize):
        for j in range(squaresize):
            result += grid[x+i, y+j]
    return int(result)

grid = np.empty((300,300))

for i in range(300):
    for j in range(300):
        grid[i,j] = computePowerLevel(i+1,j+1,serial)

maxPower = 0
maxx = 0
maxy = 0
maxss = 0
start = time.time()

for squaresize in range(1,301):
    filtered_grid = ndimage.uniform_filter(grid, size=squaresize, origin=(-int(squaresize/2), -int(squaresize/2)))
    filtered_grid *= squaresize*squaresize
    for i in range(300 - int(squaresize/2)):
        for j in range(300 - int(squaresize/2)):
            pl = filtered_grid[i,j]
            if pl > maxPower:
                maxPower = pl
                maxx = i
                maxy = j
                maxss = squaresize
print(time.time()-start)
print(maxx+1,maxy+1,maxss,maxPower)