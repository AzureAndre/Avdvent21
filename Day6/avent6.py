init = [0] * 9
with open("input6") as f:
    input = [int(n) for n in f.readline().split(",")]
for i in input:
    init[i] += 1

def findfish(d2s, days):
    for day in range(days):
        spawn = d2s[0]
        d2s = d2s[1:]
        d2s.append(spawn)
        d2s[6] += spawn
    return sum(d2s)

print("Part 1(",80,"): ", findfish(init, 80))
print("Part 2(",256,"): ", findfish(init, 256))
