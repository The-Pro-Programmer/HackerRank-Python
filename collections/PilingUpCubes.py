T = int(input())
for t in range(T):
    cubes = int(input())
    sides = list(map(int, input().split()))
    min_index = sides.index(min(sides))
    left = sides[:min_index]
    right = sides[min_index+1:]
    if left==sorted(left, reverse=True) and right==sorted(right):
        print("Yes")
    else:
        print("No")