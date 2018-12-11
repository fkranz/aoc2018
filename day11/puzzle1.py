import sys
import numpy as np 

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


grid = np.empty((300,300))

for i in range(300):
    for j in range(300):
        grid[i,j] = computePowerLevel(i+1,j+1,serial)

maxPower = 0
maxx = 0
maxy = 0

for i in range(298):
    for j in range(298):
        pl = int(sum(sum(grid[i:i+3,j:j+3])))
        if pl > maxPower:
            maxPower = pl
            maxx = i+1
            maxy = j+1

print(maxx,maxy,maxPower)