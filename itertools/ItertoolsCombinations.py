from itertools import combinations


inputs = input()
str = sorted(inputs.split()[0])
num = int(inputs.split()[1])

for n in range(1, num+1):
    for combo in combinations(str, n):
        print("".join(combo))
