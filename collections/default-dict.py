from collections import defaultdict


n, m = map(int, input().split())
dictn = defaultdict(list)
for i in range(1, n+1):
    dictn[input()].append(i)
for i in range(1, m+1):
    key = input()
    if key in dictn:
        print(" ".join(str(c) for c in dictn[key]))
    else:
        print(-1)