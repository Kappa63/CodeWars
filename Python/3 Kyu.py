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
import math, regex as re
def expand(expr):
    nums = re.findall("[- | -\d]+", expr)
    pwr, y, xcof = int(nums[-1]), abs(int(nums[-2])), (-1 if nums[-3] == '-' else int(nums[-3])) if len(nums)>2 else 1
    var, sols, srpl = re.findall("[a-z]+", expr)[0], [], {1:"", -1:"-"}
    for i in range(pwr+1):
        cof = math.comb(pwr, i)*pow(y, i)*pow(xcof, pwr-i)
        cof = srpl[cof] if cof in srpl else cof
        sols.append(f"{cof}{var+'^'+str(pwr-i) if pwr-i not in [1,0] else var if pwr-i == 1 else '1' if not cof else ''}")
    if "+" in expr: ans = "+".join(sols)
    else:
        ans, sign = sols[0], 1
        for i in sols[1:]:
            ans += ('-' if sign else '+')+i
            sign = not sign
    for fm, to in zip(["+-", "--", "-+"], ["-", "+", "-"]): ans = ans.replace(fm, to)
    return ans


#Rail Fence Cipher: Encoding and Decoding
def encode_rail_fence_cipher(s, n):
    c = n2 = (n-1)*2
    a = ""
    for i in range(n):
        u, t = 0, c
        try: a += s[i]
        except: break
        while 1:
            try: a += s[i+c]
            except: break
            c += t if (u or not n2-t) else n2-t
            u = not u
        c = t-2 if t-2 else n2
    return a       
    
def decode_rail_fence_cipher(s, n):
    ns = [""]*len(s)
    c = n2 = (n-1)*2
    x = 0
    for i in range(n):
        u, t = 0, c
        try: ns[i] += s[x]
        except: break
        x+=1
        while 1:
            try: ns[i+c] = s[x]
            except: break
            c += t if (u or not n2-t) else n2-t
            u = not u
            x+=1
        c = t-2 if t-2 else n2
    return "".join(ns)
