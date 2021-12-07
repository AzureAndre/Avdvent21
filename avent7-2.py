import statistics as st
with open("input7") as f:
    input = [int(n) for n in f.readline().split(",")]

target = int(st.mean(input))

fuel = 0
for i in input:
    dist = abs(i - target)
    for i in range(dist):
        fuel += i + 1      


print("The target is: ", target, " - The fuel needed is: ", fuel)
