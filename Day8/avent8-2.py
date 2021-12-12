input = []
output = []
f = open("input8","r")
for rdline in f:
    line = rdline.split("|")
    input.append(line[0].strip().split(" "))
    output.append(line[1].strip().split(" "))
f.close
for i in range(len(input)):
    for j in range(10):
        input[i][j] = "".join(sorted(input[i][j]))
    for j in range(4):
        output[i][j] = "".join(sorted(output[i][j]))

def wmatch(pcheck, pknown):
    match = True
    for c in pknown:
        match = match & (c in pcheck)
    return match

def getmap(map, item):
    
    for entry in item:
        if len(entry) == 2:
            map[1] = entry
        elif len(entry) == 3: 
            map[7] = entry
        elif len(entry) == 4: 
            map[4] = entry
        elif len(entry) == 7:
            map[8] = entry

    for entry in item:       
        if (len(entry) == 6) & wmatch(entry, map[1]) & wmatch(entry, map[4]) & wmatch(entry, map[7]):
            map[9] = entry
        elif (len(entry) == 6) & wmatch(entry, map[1]) & wmatch(entry, map[7]):
            map[0] = entry
        elif (len(entry) == 6):
            map[6] = entry

    for entry in item:       
        if (len(entry) == 5) & wmatch(entry, map[1]) & wmatch(entry, map[7]):
            map[3] = entry
        elif (len(entry) == 5) & wmatch( map[6], entry):
            map[5] = entry
        elif (len(entry) == 5):
            map[2] = entry


    return         

grand = 0
for i in range(len(input)):
    map = [""] * 10
    getmap(map,input[i])
    total = 0
    for j in range(4):
        total = (total * 10) + map.index(output[i][j]) 
    grand += total


print(f"The total of the output values are {grand}")


#print(count)