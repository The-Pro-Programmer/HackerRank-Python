#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations


N = int(input())
letters = input().split()
KIndces = int(input())

combos = list(combinations(letters, KIndces))
requiredLetter = 'a'
filtered = list(filter(lambda c: requiredLetter in c, combos))
print("{0:3}".format(len(filtered)/len(combos)))

