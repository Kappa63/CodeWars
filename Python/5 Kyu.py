#Simple Pig Latin
def pig_it(text):
    return " ".join((map(lambda x: x[1:] + x[0] + "ay" if x not in ["!",".","?"] else x, text.split(" "))))


#RGB To Hex Conversion
def rgb(r, g, b):
    def c(cc):
        return 0 if cc<0 else 255 if cc>255 else cc
    return ("%02x%02x%02x"%(c(r), c(g), c(b))).upper()


#Human Readable Time
def make_readable(seconds):
    mins, secs = divmod(seconds,60);hrs, mins=divmod(mins,60)
    return "%02d:%02d:%02d" % (hrs, mins, secs) 


#Did I Finish my Sudoku?
import numpy as np
def done_or_not(board): 
    A = np.array(board)
    return "Finished!" if min([min([set(range(1,10)).issubset(i) for i in A]),min([set(range(1,10)).issubset(i) for i in A.T]),min([set(range(1,10)).issubset(i) for i in A.reshape((3,3,3,3)).transpose((0,2,1,3)).reshape((9,9))])]) else "Try again!"


#Maximum subarray sum
def max_sequence(arr):
    return max([sum(arr[j:i]) for j in range(0,len(arr)+1) for i in range(j,len(arr)+1)]) if arr else 0


#Primes in numbers
def prime_factors(n):
    i=2
    f=[]
    while i*i <= n: 
        if n%i: i+=1 
        else: n //= i; f.append(i)
    if n>1: f.append(n)
    return "".join(f"({i}**{f.count(i)})" if f.count(i)>1 else f"({i})" for i in sorted(set(f)))


#PaginationHelper
import math
import numpy as np
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        if collection:
            self.i = items_per_page
            self.m = collection
            self.s = math.ceil(len(collection)/items_per_page)
            self.p = [self.m[i:i + self.i] for i in range(0, len(self.m), self.i)]
            self.c = False
        else:
            self.c = True

    def item_count(self):
        if self.c:
            return -1
        return len(self.m)

    def page_count(self):
        if self.c:
            return -1
        return self.s
    
    def page_item_count(self,page_index):
        if self.c:
            return -1
        return len(self.p[page_index]) if 0<=page_index<len(self.p) else -1

    def page_index(self,item_index):
        if self.c:
            return -1
        return item_index//self.i if 0<=item_index<len(self.m) else -1


#Moving Zeros To The End
def move_zeros(array):
    x = list(filter(lambda x: (x is not 0) and (x is not float(0)),array))
    x.extend([0]*array.count(0))
    return x


#A Chain adding function
class add(int): 
    def __call__ (self, n): return add(self+n)


#Function Algebra
class Function():
    def __init__(self, f, df): self.f, self.df = f, df
    def __call__(self, x, grad=False): return (self.df(x)) if grad else self.f(x)
    def __add__(self, Td): return lambda x, grad=False: (self.df(x)+Td.df(x)) if grad else (self.f(x)+Td.f(x))
    def __sub__(self, Td): return lambda x, grad=False: (self.df(x)-Td.df(x)) if grad else (self.f(x)-Td.f(x))
    def __mul__(self, Td): return lambda x, grad=False: (self.df(x)*Td.f(x)+self.f(x)*Td.df(x)) if grad else (self.f(x)*Td.f(x))
    def __truediv__(self, Td): return lambda x, grad=False: ((self.df(x)*Td.f(x)-self.f(x)*Td.df(x))/(Td.f(x)**2)) if grad else (self.f(x))/(Td.f(x))
    def __matmul__(self, Td): return lambda x, grad=False: (self.df(Td.f(x))*Td.df(x)) if grad else (self.f(Td.f(x)))


#Directions Reduction
def dirReduc(arr):
    Opp, s = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}, []
    [s.pop() if s and Opp[i] == s[-1] else s.append(i) for i in arr]
    return s


#Product of consecutive Fib numbers
def productFib(prod):
    fib, c, x, y = {0:0,1:1,2:1}, 0, 0, 1
    def f(n): 
        if n not in fib: fib[n] = f(n-1)+f(n-2)
        return fib[n]
    while x*y < prod: x, y = f(c), f(c+1); c+=1
    return [x, y, x*y==prod]