import sys
import numpy as np


def index(char):
    return(ord(char.lower())-97)


def find_first(matrix):
    result = []
    for i in range(matrix.shape[1]):
        if 1 not in matrix[:,i]:
            result.append(i)
    return result


def find_next(matrix, id):
    result = []
    row = matrix[id,:]
    for i in range(len(row)):
        if row[i] == 1:
            result.append(i)
    return result


def find_pre(matrix, id):
    result = []
    col = matrix[:,id]
    for i in range(len(col)):
        if col[i] == 1:
            result.append(i)
    return result

def letter(ind):
    return(str(chr(ind + 97)).upper())


def printletters(liste):
    for element in liste:
        print(letter(element), end="")  
    print()
    print()


def allin(liste1,liste2):
    result = True   
    for element in liste2:
        if element not in liste1:
            result = False
    return result

def anyidle(workers):
    for id,worker in enumerate(workers):
        if workers[1] == 0:
            return id
    return -1

def anyworking(workers):
    for worker in workers:
        if worker[1] != -1:
            return True
    return False

adjancey_matrix = np.zeros((26,26))


file = open(sys.argv[1])

for line in file:
    ll = line.split()
    pre = index(ll[1])
    next = index(ll[7])
    adjancey_matrix[pre,next] = 1

order = []
working = []
firsts = find_first(adjancey_matrix)
working.extend(firsts)

second = -1
workers = [[-1,-1], [-1, -1],[-1,-1], [-1, -1],[-1, -1]]
test = 0

while True:
#    print()
#    print(second+1, end="\t")
    worker_id = anyidle(workers)
    noinsert = False
    working2 = []
    for id,worker in enumerate(workers):
        time = worker[1]
        if time == -1 and len(working) > 0 and noinsert == False:
            curr = working.pop(0)
            workers[id] = [curr,curr+61] 
        elif time > 1:
            workers[id][1] = time-1
        if workers[id][1] == 1:
            workers[id] = [-1,-1]
            order.append(worker[0])
            nexts = find_next(adjancey_matrix, worker[0])

            for element in nexts:
                pres = find_pre(adjancey_matrix, element)
                if allin(order, pres):
                    working2.append(element)    
#        if worker[0] == -1:
#            print("empty", end="\t")
#        else:
#            print(letter(worker[0]),worker[1], end="\t")

    working.extend(working2)
    working.sort()
    second += 1
    if len(working) == 0 and anyworking(workers) == False:
        break

    
    
#print()
print(second+1)
printletters(order)
file.close()