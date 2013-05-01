# also known as anagrams
from collections import Counter

def is_permutation(a, b):
    return Counter(a) == Counter(b)
