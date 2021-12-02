# Part 1
f = open("input2", "r")
hpos = 0
depth = 0
for line in f:
    entry1 = int(line.split()[1])
    if line.split()[0][0] == "f":
        hpos += entry1
    elif line.split()[0][0] == "u":
        depth -= entry1
    elif line.split()[0][0] == "d":
        depth += entry1
f.close()
print("Part1 Ans:", hpos * depth)

# Part 2
f = open("input2", "r")
hpos = 0
depth = 0
aim = 0
for line in f:
    entry1 = int(line.split()[1])
    if line.split()[0][0] == "f":
        hpos += entry1
        depth += (entry1 * aim)
    elif line.split()[0][0] == "u":
        aim -= entry1
    elif line.split()[0][0] == "d":
        aim += entry1
f.close()
print("Part2 Ans:", hpos * depth)