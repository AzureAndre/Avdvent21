bopen = ['(','[','{', '<']
bclose = [')',']','}','>']

def iscorrupt(line):
    stack = []
    bscore = [3,57,1197,25137]
    for c in line:
        if c in bopen:
            stack.append(c)  
        else:    
            pos = bclose.index(c)
            if bopen[pos] != stack.pop():
              return bscore[pos]
    return 0

def docomplete(line):
    score = 0
    stack = []
    for c in line:
        if c in bopen:
            stack.append(c)
        else:    
            stack.pop()
    for c in stack[::-1]:
        score = (score * 5) + bopen.index(c) + 1
    return score



lines = [] 
f = open("input10","r")
for line in f:
    lines.append(line.strip())
f.close()


score = 0
cscores = []
for line in lines:
    lscore = iscorrupt(line)
    if lscore > 0:
        score += lscore
    else:
        cscores.append(docomplete(line))    
    

print(f"The syntax error score is {score}")    
print(f"The middle score of the completed lines is {sorted(cscores)[int(len(cscores)/2)]}")

