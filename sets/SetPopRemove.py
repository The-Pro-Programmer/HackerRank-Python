n = int(input())
s = set(map(int, input().split()))
ops = int(input())
for i in range(ops):
    inputs = input().split()
    operation = inputs[0]
    if('pop'==operation):
        s.pop()
    elif('remove'==operation):
        s.remove(int(inputs[1]))
    elif('discard'==operation):
        s.discard(int(inputs[1]))


print(sum(s))