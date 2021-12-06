import time

s=time.time()
with open("input6") as f:
    input = [int(n) for n in f.readline().split(",")]
f.close()

init = [0] * 9
for i in input:
    init[i] += 1


def findfish(d2s, days):
    for day in range(days):
        spawn = d2s[0]
        d2s = d2s[1:]
        d2s.append(spawn)
        d2s[6] += spawn
    return sum(d2s)

s=time.time()
print("Part 1: ", findfish(init, 80), " time: ", time.time()-s)
s=time.time()
print("Part 2: ", findfish(init, 256), " time: ", time.time()-s)
print
