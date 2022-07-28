

n, lines = map(int, input().split())
rows = []
for l in range(lines):
    rows.append(list(map(float, input().split())))


for i in zip(*rows): 
    print( sum(i)/len(i) ) 
