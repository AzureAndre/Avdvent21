# Part 1
f = open("input3", "r")
hpos = 0
depth = 0
bit = [0,0,0,0,0,0,0,0,0,0,0,0]
sout = ""
for line in f:
    for i in range(12):
        bit[i] += int(line[i])
for i in range(12):
    if bit[i] >= 500:
       sout += "1"
    else:
       sout += "0"    
f.close()
ACR = int(sout,2)
print("ACR:", ACR)

# Part 2
f = open("input3", "r")
content = f.readlines()
f.close()
sout = ""
for i in range(12):
    hit = 0
    count = 0
    for line in content:
        if line[:len(sout)] == sout:
            hit += int(line[i])
            last = line[:12]
            count += 1
    if hit >= count/2:
        sout += "1"
    else:
        sout += "0" 
    count = 0      
ogen = int(last,2)

sout = ""
for i in range(12):
    hit = 0
    count = 0
    for line in content:
        if line[:len(sout)] == sout:
            hit += int(line[i])
            last = line[:12]
            count += 1
    if hit >= count/2:
        sout += "0"
    else:
        sout += "1"
co2s = int(last,2)


#print("Oxigen generator:", ogen)
#print("C2 scrubber:", co2s)
lsup = ogen * co2s
print("lifesupport nr:", lsup)

    
        

