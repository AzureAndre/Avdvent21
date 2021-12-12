input = []
output = []
f = open("input8","r")
for rdline in f:
    line = rdline.split("|")
    input.append(line[0].strip().split(" "))
    output.append(line[1].strip().split(" "))
f.close
count = 0
for item in output:
    for entry in item:
        if (len(entry) == 2) | (len(entry) == 3) | (len(entry) == 4) | (len(entry) == 7)  :
            count += 1 
#        elif len(entry) == 3: 
#            count += 1
#        elif len(entry) == 4: 
#            count += 1
#        elif len(entry) == 7:
#            count += 1

print(f"digits 1 4 7 & 8 appear {count} times")