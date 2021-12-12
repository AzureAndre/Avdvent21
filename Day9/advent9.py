from typing import TYPE_CHECKING
import numpy as np
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


risk = 0
for i in range(100):
    for j in range(100):
        if islow(map,i,j):
            risk += map[i,j] + 1


print(f"The total risk of the map is {risk}")