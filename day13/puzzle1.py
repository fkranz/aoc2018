import sys
import numpy as np 
import copy

def add(a,b):
	c = (a[0]+b[0], a[1]+b[1])
	return c

def printGrid(grid, carts):
	bla = copy.deepcopy(grid)
	for cart in carts:
		x,y = cart[0]
		dx,dy = cart[1]

		insert = ""
		if cart[1] == (0,1):
			insert = 5#">"
		elif cart[1] == (0,-1):
			insert = 6#"<"
		elif cart[1] == (-1,0):
			insert = 7#"^"
		elif cart[1] == (1,0):
			insert = 8#"v"

		if grid[x,y] in [5,6,7,8]:
			insert = 9

		bla[x,y] = insert

	chars = [" ", ".", "\\", "/", "+", ">", "<", "^", "v", "X"]

	for i in range(bla.shape[0]):
		for j in range(bla.shape[1]):
			print(chars[int(bla[i,j])], end="")
		print()

grid = np.zeros((int(sys.argv[2]),int(sys.argv[2])))  #150,150
row,col = grid.shape
file = open(sys.argv[1])

charToInt = {"-":1, "\\":2,  "/":3, "+":4, "v":1, "^":1, ">":1, "<":1, "|":1}
cartToInt = {"v":(1,0), "^":(-1,0), ">":(0,1), "<":(0,-1)}
directions = [2,0,3]
i = 0
j = 0

carts = []


for line in file:
	j = 0
	for letter in line:
		if letter in charToInt:
			grid[i,j] = charToInt[letter]
		if letter in cartToInt:
			carts.append(((i,j), cartToInt[letter], 0))
		j += 1
	i += 1

file.close


blub = True
while blub:
	sorted(carts , key=lambda k: [(k[0][0], k[0][1])])
	positions = []
	cartpos = []
	for cart in carts:
		i,j = cart[0]
		cartpos.append(i* col + j)

	for index,cart in enumerate(carts):
		if cart == None:
			positions.append(None)
			continue

		p,v,t = cart
		p_new = add(p,v)

		p_lin = p_new[0]* col + p_new[1]
		if p_lin in cartpos:
			print(p_new[1], ",", p_new[0], sep="")
			exit(0)

		if p_lin in positions:
			print(p_new[1], ",", p_new[0], sep="")
			exit(0)
			
		positions.append(p_lin)

		i,j = p_new
		vx,vy = v

		if grid[i,j] == 2:
			v_new = (vy,vx)
		elif grid[i,j] == 3:
			v_new = (-vy,-vx)
		elif grid[i,j] == 4:
			if directions[t] == 2:
				v_new = (-vy,vx)
			elif directions[t] == 3:
				v_new = (vy,-vx)
			else:
				v_new = v
			t = (t + 1) %3
		else:
			v_new = v


		carts[index] = (p_new, v_new, t)
	carts = list(filter(lambda a: a != None, carts))
	if(len(carts) == 1):
		break


print(carts[0][0][1], ",", carts[0][0][0], sep="")