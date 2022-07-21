K = int(input())
guests = sorted(map(int, input().split()))
n = len(guests)
for i in range(n):
    if(i!=(n-1)):
        if(guests[i]!=guests[i-1] and guests[i]!=guests[i+1]):
            print(guests[i])
            break
    else:
        print(guests[i])

