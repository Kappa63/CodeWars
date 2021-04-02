#Make a spiral
from itertools import cycle
def spiralize(size):
    A = [[0]*size for _ in range(size)]
    Dir = cycle([(0,1), (1,0), (0,-1), (-1,0)])
    x, y = 0, 0
    for i in range(size):
        D = next(Dir)
        for _ in range(size-1):
            xt, yt = (x+D[0],y+D[1]) 
            A[x][y] = 1
            if i>2 and  A[xt+D[0]][yt+D[1]] == 1: break
            x, y = xt, yt
    return A