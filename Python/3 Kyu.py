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

#Binomial Expansion
import math
import regex as re
def expand(expr):
    n = re.findall("[- | -\d]+", expr)
    p = int(n[-1])
    y = abs(int(n[-2]))
    try:
        x = -1 if n[-3] == '-' else int(n[-3])
    except: 
        x = 1
    v = re.findall("[a-z]+", expr)[0]
    s = []
    f = {1: "", -1:"-"}
    for i in range(p+1):
        cof = math.comb(p, i)*pow(y, i)*pow(x, p-i)
        cof = f[cof] if cof in f else cof
        s.append(f"{cof}{v+'^'+str(p-i) if p-i not in [1,0] else v if p-i == 1 else '1' if cof == '' else ''}")
    if "+" in expr:
        a = "+".join(s)
    else:
        a = s[0]
        x = 1
        for i in s[1:]:
            a += ('-' if x else '+')+i
            x = not x
    a = a.replace("+-", "-");
    a = a.replace("--", "+");
    return a.replace("-+", "-");
