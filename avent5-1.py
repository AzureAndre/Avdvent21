import numpy as np

f = open("input5", "r")

cntr = 0
bcoords = [[ [0] * 2 ] * 2] * 500
coords = np.array(bcoords)
map = np.array([ [0] * 1000 ] * 1000)

for line in f:
    svec = line.split(' -> ')
    coords[cntr,0] = [int(n) for n in svec[0].split(",")]
    coords[cntr,1] = [int(n) for n in svec[1].split(",")]
    cntr += 1
    #print(cards)
f.close()

for vec in coords:
    if vec[0,0] == vec[1,0]:
        smax = max(vec[0,1],vec[1,1])
        smin = min(vec[0,1],vec[1,1])
        for step in range(smin,smax+1):
            map[vec[0,0], step] += 1
    if vec[0,1] == vec[1,1]:
        smax = max(vec[0,0],vec[1,0])
        smin = min(vec[0,0],vec[1,0])
        for step in range(smin, smax+1):
            map[step, vec[1,1]] += 1

peaks = 0
for i in range(1000):
    for j in range(1000):
        if map[i,j] > 1:
            peaks += 1

print("peaks: ", peaks)