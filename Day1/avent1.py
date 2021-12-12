# Part 1
f = open("input1", "r")

last = 10000
incr = 0
for line in f:
    entry1 = int(line)
    if entry1 > last :
        incr += 1
    last = entry1
f.close()
print(incr)

# Part 2
f = open("input1", "r")
incr = 0
entries = []
for line in f:
    entry1 = int(line)
    entries = entries + [entry1]
    if len(entries) == 4:
        if sum(entries[-3:]) > sum(entries[:3]) :
            incr += 1
        entries = entries[1:]
f.close()
print(incr)
