import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()

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

adjancey_matrix = np.zeros((26,26))


file = open(sys.argv[1])

for line in file:
    ll = line.split()
    pre = index(ll[1])
    next = index(ll[7])
    adjancey_matrix[pre,next] = 1

#print(adjancey_matrix)


G.add_nodes_from = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(adjancey_matrix.shape[0]):
    for j in range(adjancey_matrix.shape[1]):
        if adjancey_matrix[i,j] == 1:
            G.add_edge(i,j)

nx.draw_circular(G, with_labels=True)
plt.show()

order = []
working = []
firsts = find_first(adjancey_matrix)
working.extend(firsts)

while len(working) > 0:
    curr = working.pop(0)
    order.append(curr)
    nexts = find_next(adjancey_matrix, curr)

    for element in nexts:
        pres = find_pre(adjancey_matrix, element)
        if allin(order, pres):
            working.append(element)

    working.sort()


printletters(order)
file.close()