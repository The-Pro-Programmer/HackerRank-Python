
from collections import deque


n = int(input())
d = deque()
for i in range(n):
    instr = input().split()
    operation = instr[0]
    if operation=='append':
        num = int(instr[1])
        d.append(num)
    elif operation=='appendleft':
        num = int(instr[1])
        d.appendleft(num)
    elif operation=='pop':
        d.pop()
    elif operation=='popleft':
        d.popleft()
    
print(" ".join([str(num) for num in d]))