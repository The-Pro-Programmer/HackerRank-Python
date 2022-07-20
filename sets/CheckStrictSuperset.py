setA = set(map(int, input().split()))
num = int(input())
flag = True
for n in range(num):
    setB = set(map(int, input().split()))
    flag = flag and len(setA)>len(setB) and len(setB.difference(setA))==0
    if not flag:
        break
print(flag)