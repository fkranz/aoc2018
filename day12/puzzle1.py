import sys
import numpy as np
import matplotlib.pyplot as plt

file = open(sys.argv[1])
generations = int(sys.argv[2])
initial = True
rules = {}
config = ""
for line in file:
    if initial:
        ll = line.split()
        config = ll[2]
        initial = False
    else:
        ll = line.split("=>")
        rules[ll[0].replace(" ","")] = ll[1].rstrip().replace(" ","")

#print(rules)
#print(config)
addedleft = 0
for i in range(generations):
    generation = []
    while config[0:3] == "...":
        config = config[1:]
        addedleft -= 1
    if config[0] == "#":
       # print(config)
        config = ".."+config
       # print(config)
        addedleft += 2
    elif config[1] == "#":
       # print(config)
        config = "."+config
       # print(config)
        addedleft += 1
    if config[len(config)-1] == "#":
        config += ".."
    elif config[len(config)-2] == "#":
        config += "."
    config.replace(" ", "")
    #print(config)
    #print(i,config, addedleft)
    for index in range(len(config)):
        if index == 0:
            curr = ".." + config[index:index+3] 
        elif index == 1:
            curr = "." + config[index-1:index+3]
        elif index == len(config)-2:
            curr = config[index-2:index+2] + "."
        elif index == len(config)-1:
            curr = config[index-2:index+1] + ".."
        else:
            curr = config[index-2:index+3]

        #print(curr)
        if curr in rules:
            new = rules[curr]
            generation.append(new)
        else:
            generation.append(".")
            #print("outch")
    #print(generation)
    config = "".join(generation)
    plants = 0
    for index in range(len(config)):
        if config[index] == "#":
            plants += index-addedleft
    print(i+1,config, addedleft, plants, config.count("#"))

print(config)
plants = 0
for index in range(len(config)):
    if config[index] == "#":
        plants += index-addedleft
print(addedleft)
print(plants)
file.close()