# Part 1

import numpy as np

def wincard(card):
    win = False
    for i in range(5):
        win = win | (sum(card[i]) == 50000) | (sum(card[:,i]) == 50000)
    return win


bcards = [[ [0] * 5 ] * 5] * 100
tab = -1    
col = 0
row = 0
bcalls = [0] * 100
cards = np.array(bcards)
calls = np.array(bcalls)
f = open("input4", "r")
cntr = 0
for line in f:
    if cntr == 0:
        n = 0
        for num in line.split(','):
            calls[n] = int(num)
            n += 1
    else:
        if line == "\n":
            tab += 1
            row = 0
        else:
            col = 0
            for num in line.split(' '):
                if (num != "\n") & (num != ""):
                    cards[tab, row, col] = int(num)
                    col += 1
            row += 1    
    cntr += 1
    #print(cards)
f.close()
call = 0
bwin = [0] * 100
while (sum(bwin) < 100)  & (call < 100):
    tab = 0
    while (sum(bwin) < 100) and (tab < 100):
        for row in range(5):
            for col in range(5):
                if cards[tab,row,col] == calls[call]:
                    cards[tab,row,col] = 10000
        if wincard(cards[tab]):
            bwin[tab] = 1

        tab += 1
    call +=1
    
lastcall = calls[call-1]
boardtot = sum(sum(cards[tab-1])) % 10000 
score = lastcall * boardtot
print("Score:", score)

