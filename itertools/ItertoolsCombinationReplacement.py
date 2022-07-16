#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true


from itertools import combinations_with_replacement


inputs = input()
str = sorted(inputs.split()[0])
num = int(inputs.split()[1])

for combo in combinations_with_replacement(str, num):
    print(''.join(combo))
