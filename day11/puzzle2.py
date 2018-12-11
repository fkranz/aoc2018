import sys
import numpy as np 
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
        #print(computePowerLevel(i+1,j+1,serial))

maxPower = 0
maxx = 0
maxy = 0
maxss = 0
start = time.time()
for squaresize in range(1,301):
    for i in range(300 - squaresize):
        for j in range(300 - squaresize):
            pl = int(sum(sum(grid[i:i+squaresize,j:j+squaresize])))
            if pl > maxPower:
                maxPower = pl
                maxx = i+1
                maxy = j+1
                maxss = squaresize
print(time.time()-start)
print(maxx,maxy,maxss,maxPower)