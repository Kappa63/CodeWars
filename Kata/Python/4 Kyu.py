#Permutations
import itertools
def permutations(string):
    return set(map("".join,itertools.permutations(string)))


#Matrix Determinant
import numpy as np
def determinant(matrix):
    return round(np.linalg.det(np.array(matrix)))


#Most frequently used words in a text
from collections import Counter
import re
def top_3_words(text):  
    text = ' '.join(re.findall("[a-zA-Z0-9']*", text))
    f = [i[0] for i in Counter([i.strip() for i in text.lower().split()]).most_common()[:3] if i[0] not in ["'", "'''"]]
    return f if f else []