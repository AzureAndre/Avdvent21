import numpy as np
import math as math
rmap = [[0] * 100] * 100
map = np.array(rmap)

f = open("input9","r")
i=0
for line in f:
    line = line.strip()
    j = 0
    for c in line:
        map[i,j] = int(c)
        j += 1
    i += 1

def islow(map,i,j):
    if j == 0:
        n = True
    else:
        n = (map[i,j] < map[i,j-1])
    if j == 99:
        s = True
    else:
        s = (map[i,j] < map[i,j+1])
    if i == 0:
        w = True
    else:
        w = (map[i,j] < map[i-1,j])
    if i == 99:
        e = True
    else:
        e = (map[i,j] < map[i+1,j])
    return (n & s & e & w)

def basinfind(map, i, j):
    if j != 0:
        if map[i,j-1] < 9:
            map[i,j-1] = 10
            basinfind(map,i,j-1)
    if j != 99:
        if map[i,j+1] < 9 :
            map[i,j+1] = 10
            basinfind(map,i,j+1)
    if i != 0:
        if map[i-1,j] < 9:
            map[i-1,j] = 10
            basinfind(map,i-1,j)
    if i != 99:
        if map[i+1,j] < 9:
            map[i+1,j] = 10
            basinfind(map,i+1,j)
    return

def basinsize(map):
    size = 0
    for i in range(100):
        for j in range(100):
            if map[i,j] == 10:
                size += 1
    return size

basins = []
for i in range(100):
    for j in range(100):
        if islow(map,i,j):
            basins.append([i,j,0])

#for basin in basins:
top = [0, 0, 0]
for basin in basins:
    testmap = map.copy()            
    basinfind(testmap,basin[0],basin[1])
    basin[2] = basinsize(testmap)
    if basin[2] > top[0]:
        top[0] = basin[2]
        top = sorted(top)

print(f"The product of the 3 largest basins is {math.prod(top)}")






