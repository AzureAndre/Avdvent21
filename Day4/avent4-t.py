import numpy as np
with open("input4") as f:
    calls = [int(n) for n in f.readline().split(",")]
    boards = []
    while f.readline():
        board = []
        for line in range(5):
            board.append([int(n) for n in f.readline().split()])
        boards.append(board)

nboards = np.array(boards)

print(nboards)