#Isograms
def is_isogram(string):
    string = [x.lower() for x in string]
    y = list(map(lambda x: string.count(x), string))
    return max(y) <= 1 if y else True


#Growth of a Population
def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:p0 = int(p0); y += 1; p0 += (p0*(percent/100) + aug)
    return y