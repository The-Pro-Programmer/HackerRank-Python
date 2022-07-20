T = int(input())
for t in range(T):
    len1 = int(input())
    set1 = set(map(int, input().split()))
    len2 = int(input())
    set2 = set(map(int, input().split()))
    setDiff = set1.difference(set2)
    print(len(setDiff)==0)