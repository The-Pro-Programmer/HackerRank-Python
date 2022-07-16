#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations


inputs = input()
s = sorted(inputs.split()[0])
nums = int(inputs.split()[1])

for perm in permutations(s, nums):
    print("".join(perm))
