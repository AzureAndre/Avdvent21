import numpy as np

init = [0] * 9
with open("input6") as f:
    input = [int(n) for n in f.readline().split(",")]
for i in input:
    init[i] += 1

# set up the transformation array
N = [[0,1,0,0,0,0,0,0,0], 
     [0,0,1,0,0,0,0,0,0], 
     [0,0,0,1,0,0,0,0,0], 
     [0,0,0,0,1,0,0,0,0], 
     [0,0,0,0,0,1,0,0,0], 
     [0,0,0,0,0,0,1,0,0], 
     [1,0,0,0,0,0,0,1,0], 
     [0,0,0,0,0,0,0,0,1], 
     [1,0,0,0,0,0,0,0,0]]
M = np.array(N)
v = np.array(init)


def findfish(M, v, t):
    for i in range(t):
        v = np.matmul(np.power(M, 80),v)
    return sum(v)
print(v)
print("Part 1(",80,"): ", findfish(M, v, 80))
print("Part 2(",256,"): ", findfish(M, v, 256))
