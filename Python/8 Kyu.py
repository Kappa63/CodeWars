#Multiply
multiply = lambda a, b: a*b


#String repeat
repeat_str = lambda i,j: j*i


#Twice as old
twice_as_old = lambda x,y: abs(x-y*2)


#Object Oriented Piracy 
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self): return self.draft - self.crew * 1.5 >= 20


#Find the first non-consecutive number
def first_non_consecutive(arr):
    A = None
    for i in range(len(arr)-1): 
        if arr[i]-arr[i+1] != -1: A = arr[i+1];break
    return A


#Counting sheep...
count_sheeps = lambda x: x.count(1)