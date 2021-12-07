import statistics as st
with open("input7") as f:
    input = [int(n) for n in f.readline().split(",")]

target = st.median(input)
fuel = 0
for i in input:
    fuel += abs(i - target)

print("Part1: The target is: ", target, " - The fuel needed is: ", fuel)

target = int(st.mean(input))
fuel = 0
for i in input:
    dist = abs(i - target)
    fuel += dist * (dist + 1) /2 

print("The target is: ", target, " - The fuel needed is: ", fuel, f2)