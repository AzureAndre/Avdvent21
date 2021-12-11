import numpy as np
cflash = 0

def flash(octopi, i , j):
    adjs = [[-1,-1], [-1,0], [-1,1],[0,-1], [0,1],[1,-1], [1,0], [1,1]]
    global cflash
    cflash += 1
    octopi[i,j] = -1
    for adj in adjs:
        m = i + adj[0] 
        n = j + adj[1]
        if (m in range(10)) and (n in range(10)):
            if octopi[m,n] >= 0:
                octopi[m,n] += 1
            if octopi[m,n]  > 9:
              flash(octopi,m,n)
    return 

def step(octopi):
    octopi += 1
    for i in range(10):
        for j in range(10):
            if octopi[i,j] == 10:
                flash(octopi,i,j)
    for i in range(10):
        for j in range(10):
            if octopi[i,j] == -1:
                octopi[i,j] =  0
    return                

f = open("input11","r")
octopi = np.array([[0] * 10] * 10)

i = 0
for rdline in f:
    j = 0
    for c in rdline.strip():
       octopi[i,j] = int(c)
       j += 1
    i += 1
    
f.close

#print(octopi)
target = 100
for i in range(target):
    step(octopi)
#    print(octopi)


print(f"There are {cflash} flashes after {target} steps")
