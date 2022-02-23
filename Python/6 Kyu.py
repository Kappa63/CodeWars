#Create Phone Number
def create_phone_number(n):
    n = [str(c) for c in n]
    return f'({"".join(n[:3])}) {"".join(n[3:6])}-{"".join(n[6:])}'


#Stop gninnipS My sdroW!
def spin_words(sentence):
    return " ".join([x[::-1] if len(x)>=5 else x for x in sentence.split(" ")])


#Bit Counting
def count_bits(n):
    return eval("+".join(list("{0:b}".format(n))))


#Replace With Alphabet Position
def alphabet_position(text):
    return " ".join(list(filter(None,[str(ord(i.lower())-96) if i.isalpha() else None for i in list(text)])))


#Build Tower
def tower_builder(n_floors):
    return list(map(lambda x: f"{' '*(n_floors-(x+1))}*{'*'*(x*2)}{' '*(n_floors-(x+1))}",range(n_floors)))


#Your order, please
def order(sentence):
    x=[]
    for i in range(len(sentence.split(' '))+1):
        for c in sentence.split(' '):
            if str(i) in c:
                x.append(c)
    return " ".join(x)


#Split Strings
solution = lambda x: [f"{x[i:i+2]}{'_' if len(x[i:i+2])==1 else ''}" for i in range(0,len(x), 2)]

#Find the unique number
def find_uniq(arr):
    return [i for i in list(set(arr)) if arr.count(i)==1][0]


#Does my number look big in this?
def narcissistic( value ):
    return sum(list(map(lambda x: int(x)**len(str(value)), str(value)))) == value


#Simple Encryption #1 - Alternating Split
def decrypt(encrypted_text, n):
    if encrypted_text:
        i = encrypted_text
    else:
        i = "aa"
    for _ in range(n):
        encrypted_text="".join(map("".join, zip(encrypted_text[(len(encrypted_text)//2):],encrypted_text[:(len(encrypted_text)//2)])))
    return encrypted_text if ((len(i)/2).is_integer() or n<=0) else encrypted_text+i[-1]

def encrypt(text, n):
    for _ in range(n):
        text=text[1::2]+text[::2]
    return text


#The Supermarket Queue
def queue_time(customers, n):
    Q = [0]*n
    for c in customers: Q[0]+=c;Q.sort()
    return max(Q)


#Who likes it?
def likes(names):
    L = len(names)
    if L == 1: return f'{names[0]} likes this'
    if L == 2: return f'{names[0]} and {names[1]} like this'
    if L == 3: return f'{names[0]}, {names[1]} and {names[2]} like this'
    if L > 3: return f'{names.pop(0)}, {names.pop(0)} and {len(names)} others like this'
    return "no one likes this"


#Is a number prime?
import math
def is_prime(num):    
    return all(num % i for i in range(2,int(math.sqrt(num))+1)) if num > 1 else False


#Vasya - Clerk
def tickets(people):
    B = {100:0, 50:0, 25:0}
    for p in people: 
        x = p-25
        B[p] += 1
        if x == 75: 
            if B[25] - 1 < 0 or B[50] - 1 < 0:
                if B[25] - 3 < 0: return "NO"
                else: B[25] -= 3
            else: B[25] -= 1; B[50] -= 1
        elif x == 25: 
            if B[25] - 1 < 0: return "NO"
            else: B[25] -= 1
    return "YES"


#Next multiple of 5
def next_multiple_of_five(n):
    b = bin(n)
    o = "p0"
    if not n: return 5
    Path = {"p0":{"0":"p0","1":"p1"},
            "p1":{"0":"p2","1":"p3"},
            "p2":{"0":"p4","1":"p0"},
            "p3":{"0":"p1","1":"p2"},
            "p4":{"0":"p3","1":"p4"}}
    Fin = {"p0":"0","p1":"01","p2":"1","p3":"11","p4":"011"}
    for i in b[2:]: o = Path[o][i]
    return int(b+Fin[o],2)
