import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def add (a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result

file = open(sys.argv[1])

xp = []
yp = []
xv = []
yv = []

for line in file:
    ll = line.replace("<",",").replace(">",",").split(",")

    xp.append(int(ll[1]))
    yp.append(int(ll[2]))

    xv.append(int(ll[4]))
    yv.append(int(ll[5]))

file.close()
 

i = 0
dim = 999999999999
while True:
    x_old = xp
    y_old = yp

    xp = add(xp,xv)
    yp = add(yp,yv)

    curr_dim = (max(xp) - min(xp)) * max(yp) - min(yp)
    if curr_dim < dim:
        dim = curr_dim
    else:
        print(i)
        break

    i += 1

fig = plt.figure(figsize = (192,108))
plt.gca().invert_yaxis()
ax = fig.add_subplot(111)
f = ax.scatter(x_old,y_old, s=50)
plt.show()

plt.close()