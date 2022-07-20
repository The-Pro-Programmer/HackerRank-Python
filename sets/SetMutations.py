n = int(input())
s = set(map(int, input().split()))
ops = int(input())
for i in range(ops):
    operation = input().split()[0]
    s2 = set(map(int, input().split()))
    if('intersection_update'==operation):
        s.intersection_update(s2)
    elif('update'==operation):
        s.update(s2)
    elif('symmetric_difference_update'==operation):
        s.symmetric_difference_update(s2)
    elif('difference_update'==operation):
        s.difference_update(s2)


print(sum(s))